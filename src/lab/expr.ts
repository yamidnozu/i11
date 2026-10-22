/** Evaluador de expresiones seguro (sin eval): lo que se escribe en los JSON de laboratorios. */
export type Val = number | boolean | string | Val[] | { [k: string]: Val } | undefined;
export type Scope = Record<string, any>;
type Fn = (args: any[], sc: Scope) => any;

const rad = (d: number) => (d * Math.PI) / 180;
export const fmt = (x: number, d = 2) => (Number.isFinite(x) ? (+x.toFixed(d)).toString().replace('.', ',') : '—');
const col = (sc: Scope, k: string): number[] => ((sc.traj as any[]) ?? []).map((s) => +s[k]);
const num = (x: any) => (typeof x === 'boolean' ? +x : x);

export const FUNCS: Record<string, Fn> = {
  sin: ([x]) => Math.sin(x), cos: ([x]) => Math.cos(x), tan: ([x]) => Math.tan(x), asin: ([x]) => Math.asin(x), acos: ([x]) => Math.acos(x), atan: ([x]) => Math.atan(x), atan2: ([y, x]) => Math.atan2(y, x),
  sqrt: ([x]) => Math.sqrt(x), abs: ([x]) => Math.abs(x), exp: ([x]) => Math.exp(x), ln: ([x]) => Math.log(x), log10: ([x]) => Math.log10(x), log2: ([x]) => Math.log2(x),
  floor: ([x]) => Math.floor(x), ceil: ([x]) => Math.ceil(x), round: ([x, d = 0]) => { const f = 10 ** d; return Math.round(x * f) / f; }, sign: ([x]) => Math.sign(x),
  pow: ([a, b]) => a ** b, min: (a) => Math.min(...a.map(num)), max: (a) => Math.max(...a.map(num)), hypot: (a) => Math.hypot(...a), mod: ([a, b]) => ((a % b) + b) % b,
  rad: ([d]) => rad(d), deg: ([r]) => (r * 180) / Math.PI, clamp: ([x, a, b]) => Math.min(b, Math.max(a, x)), si: ([c, a, b]) => (c ? a : b), cerca: ([a, b, t]) => Math.abs(a - b) <= t,
  n: ([x, d]) => fmt(x, d ?? 2), len: ([a]) => (Array.isArray(a) ? a.length : 0),
  colmax: ([k], sc) => Math.max(...col(sc, k)), colmin: ([k], sc) => Math.min(...col(sc, k)), collast: ([k], sc) => { const c = col(sc, k); return c[c.length - 1]; }, colfirst: ([k], sc) => col(sc, k)[0],
  colmean: ([k], sc) => { const c = col(sc, k); return c.reduce((a, b) => a + b, 0) / (c.length || 1); }, colsum: ([k], sc) => col(sc, k).reduce((a, b) => a + b, 0), colcount: (_a, sc) => ((sc.traj as any[]) ?? []).length,
  atmax: ([r, b], sc) => { const B = col(sc, b), R = col(sc, r); return R[B.indexOf(Math.max(...B))]; }, atmin: ([r, b], sc) => { const B = col(sc, b), R = col(sc, r); return R[B.indexOf(Math.min(...B))]; },
  colat: ([k, i], sc) => col(sc, k)[Math.max(0, Math.min(col(sc, k).length - 1, i | 0))],
  // al azar con semilla: alea(i) está en [0,1) y siempre da lo mismo para la misma semilla e índice
  alea: ([i, seed = 1]) => { let x = (Math.imul(i + 1, 374761393) ^ Math.imul(seed + 7, 668265263)) >>> 0; x = Math.imul(x ^ (x >>> 13), 1274126177) >>> 0; return ((x ^ (x >>> 16)) >>> 0) / 4294967296; },
};
const CONST: Record<string, number> = { pi: Math.PI, e: Math.E, PI: Math.PI };
const BLOCK = new Set(['__proto__', 'constructor', 'prototype']);

type Tok = { t: 'n' | 'id' | 's' | 'op'; v: string };
function lex(src: string): Tok[] {
  const out: Tok[] = []; let i = 0;
  while (i < src.length) {
    const c = src[i];
    if (/\s/.test(c)) { i++; continue; }
    if (/[0-9]/.test(c) || (c === '.' && /[0-9]/.test(src[i + 1] ?? ''))) { const m = /^(\d+\.?\d*|\.\d+)([eE][+-]?\d+)?/.exec(src.slice(i)); if (!m) throw new Error(`número mal escrito en «${src}»`); out.push({ t: 'n', v: m[0] }); i += m[0].length; continue; }
    if (/[A-Za-z_À-ɏ]/.test(c)) { const m = /^[A-Za-z_À-ɏ][A-Za-z0-9_À-ɏ]*/.exec(src.slice(i))!; out.push({ t: 'id', v: m[0] }); i += m[0].length; continue; }
    if (c === '"' || c === "'") { const j = src.indexOf(c, i + 1); if (j < 0) throw new Error(`texto sin cerrar en «${src}»`); out.push({ t: 's', v: src.slice(i + 1, j) }); i = j + 1; continue; }
    const two = src.slice(i, i + 2);
    if (['&&', '||', '==', '!=', '<=', '>='].includes(two)) { out.push({ t: 'op', v: two }); i += 2; continue; }
    if ('+-*/%^<>!?:,()[].'.includes(c)) { out.push({ t: 'op', v: c }); i++; continue; }
    throw new Error(`carácter no permitido «${c}» en «${src}»`);
  }
  return out;
}

type Node = (sc: Scope) => any;
export function compile(src: string): Node {
  const tk = lex(String(src)); let p = 0;
  const peek = () => tk[p], eat = (v?: string) => { const t = tk[p++]; if (v && (!t || t.v !== v)) throw new Error(`se esperaba «${v}» en «${src}»`); return t; };
  const isOp = (v: string) => peek()?.t === 'op' && peek().v === v;
  function ternary(): Node { const c = or(); if (isOp('?')) { eat(); const a = ternary(); eat(':'); const b = ternary(); return (s) => (c(s) ? a(s) : b(s)); } return c; }
  function or(): Node { let l = and(); while (isOp('||')) { eat(); const r = and(), a = l; l = (s) => a(s) || r(s); } return l; }
  function and(): Node { let l = eq(); while (isOp('&&')) { eat(); const r = eq(), a = l; l = (s) => a(s) && r(s); } return l; }
  function eq(): Node { let l = cmp(); while (isOp('==') || isOp('!=')) { const o = eat().v, r = cmp(), a = l; l = o === '==' ? (s) => a(s) === r(s) : (s) => a(s) !== r(s); } return l; }
  function cmp(): Node { let l = add(); while (['<', '>', '<=', '>='].some(isOp)) { const o = eat().v, r = add(), a = l; l = (s) => { const x = a(s), y = r(s); return o === '<' ? x < y : o === '>' ? x > y : o === '<=' ? x <= y : x >= y; }; } return l; }
  function add(): Node { let l = mul(); while (isOp('+') || isOp('-')) { const o = eat().v, r = mul(), a = l; l = o === '+' ? (s) => a(s) + r(s) : (s) => a(s) - r(s); } return l; }
  function mul(): Node { let l = unary(); while (isOp('*') || isOp('/') || isOp('%')) { const o = eat().v, r = unary(), a = l; l = o === '*' ? (s) => a(s) * r(s) : o === '/' ? (s) => a(s) / r(s) : (s) => a(s) % r(s); } return l; }
  function unary(): Node { if (isOp('-')) { eat(); const a = unary(); return (s) => -a(s); } if (isOp('!')) { eat(); const a = unary(); return (s) => !a(s); } return pow(); }
  function pow(): Node { const b = post(); if (isOp('^')) { eat(); const e = unary(); return (s) => b(s) ** e(s); } return b; }
  function post(): Node {
    let n = prim();
    for (;;) {
      if (isOp('.')) { eat(); const k = eat().v; if (BLOCK.has(k)) throw new Error('propiedad no permitida'); const a = n; n = (s) => a(s)?.[k]; continue; }
      if (isOp('[')) { eat(); const i = ternary(); eat(']'); const a = n; n = (s) => { const k = i(s); if (typeof k === 'string' && BLOCK.has(k)) return undefined; return a(s)?.[k]; }; continue; }
      return n;
    }
  }
  function prim(): Node {
    const t = eat(); if (!t) throw new Error(`expresión incompleta: «${src}»`);
    if (t.t === 'n') { const v = +t.v; return () => v; }
    if (t.t === 's') { const v = t.v; return () => v; }
    if (t.t === 'op' && t.v === '(') { const e = ternary(); eat(')'); return e; }
    if (t.t === 'op' && t.v === '[') { const items: Node[] = []; if (!isOp(']')) { do { items.push(ternary()); } while (isOp(',') && eat()); } eat(']'); return (s) => items.map((f) => f(s)); }
    if (t.t === 'id') {
      const name = t.v;
      if (BLOCK.has(name)) throw new Error('nombre no permitido');
      if (isOp('(')) {
        eat(); const args: Node[] = []; if (!isOp(')')) { do { args.push(ternary()); } while (isOp(',') && eat()); } eat(')');
        return (s) => { const f = (s.__f && s.__f[name]) || FUNCS[name]; if (!f) throw new Error(`función desconocida «${name}»`); return f(args.map((a) => a(s)), s); };
      }
      if (name === 'verdadero') return () => true; if (name === 'falso') return () => false;
      if (Object.prototype.hasOwnProperty.call(CONST, name)) return (s) => (Object.prototype.hasOwnProperty.call(s, name) ? s[name] : CONST[name]);
      
      return (s) => s[name];
    }
    throw new Error(`no se entiende «${t.v}» en «${src}»`);
  }
  const root = ternary();
  if (p < tk.length) throw new Error(`sobra «${tk[p].v}» en «${src}»`);
  return root;
}
const cache = new Map<string, Node>();
export const ev = (src: string | number | boolean, sc: Scope): any => { if (typeof src !== 'string') return src; let f = cache.get(src); if (!f) { f = compile(src); cache.set(src, f); } return f(sc); };
export const evNum = (src: string | number | boolean, sc: Scope): number => { const v = ev(src, sc); return typeof v === 'boolean' ? +v : +v; };
/** Revisa que una expresión se pueda compilar (para validar JSON sin ejecutarla). */
export function checkExpr(src: unknown): string | null { if (typeof src === 'number' || typeof src === 'boolean') return null; if (typeof src !== 'string') return 'debe ser texto o número'; try { compile(src); return null; } catch (e) { return (e as Error).message; } }

/** Plantillas: «t = #{t|2} s» sustituye la expresión por su valor (|d = decimales, con coma). */
export function tpl(text: string, sc: Scope): string {
  let out = '', i = 0;
  while (i < text.length) {
    if (text[i] === '#' && text[i + 1] === '{') {
      let d = 1, j = i + 2; while (j < text.length && d) { if (text[j] === '{') d++; else if (text[j] === '}') d--; j++; }
      const inner = text.slice(i + 2, j - 1), bar = inner.lastIndexOf('|');
      const expr = bar >= 0 && /^\d+$/.test(inner.slice(bar + 1).trim()) ? inner.slice(0, bar) : inner, dec = bar >= 0 && /^\d+$/.test(inner.slice(bar + 1).trim()) ? +inner.slice(bar + 1) : 2;
      const v = ev(expr, sc); out += typeof v === 'number' ? fmt(v, dec) : String(v ?? ''); i = j; continue;
    }
    out += text[i++];
  }
  return out;
}
export function checkTpl(text: string): string[] {
  const errs: string[] = []; let i = 0;
  while (i < text.length) { if (text[i] === '#' && text[i + 1] === '{') { let d = 1, j = i + 2; while (j < text.length && d) { if (text[j] === '{') d++; else if (text[j] === '}') d--; j++; } if (d) { errs.push('llave sin cerrar en «#{…}»'); break; } const inner = text.slice(i + 2, j - 1), bar = inner.lastIndexOf('|'); const e = checkExpr(bar >= 0 && /^\d+$/.test(inner.slice(bar + 1).trim()) ? inner.slice(0, bar) : inner); if (e) errs.push(e); i = j; } else i++; }
  return errs;
}
