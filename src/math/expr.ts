/**
 * Parser seguro de expresiones (sin eval ni new Function).
 * Soporta + - * / ^, multiplicación implícita (2x, 3sin(x), (x+1)(x-1)),
 * constantes pi y e, y funciones sin cos tan asin acos atan sqrt ln log abs exp.
 */
type Tok = { t: 'num' | 'id' | 'op'; v: string };
export type Env = Record<string, number>;
export type Compiled = (env: Env) => number;

const FUNCS: Record<string, (x: number) => number> = {
  sin: Math.sin, cos: Math.cos, tan: Math.tan, asin: Math.asin, acos: Math.acos, atan: Math.atan,
  sqrt: Math.sqrt, ln: Math.log, log: Math.log10, abs: Math.abs, exp: Math.exp,
};
const CONSTS: Env = { pi: Math.PI, e: Math.E };

function tokenize(src: string): Tok[] {
  const out: Tok[] = [];
  const s = src.replace(/\s+/g, '').replace(/,/g, '.').replace(/π/g, 'pi').replace(/·/g, '*').replace(/−/g, '-');
  let i = 0;
  while (i < s.length) {
    const c = s[i];
    const num = /^(\d+\.?\d*|\.\d+)/.exec(s.slice(i));
    if (num) { out.push({ t: 'num', v: num[0] }); i += num[0].length; continue; }
    const id = /^[A-Za-z_]+/.exec(s.slice(i));
    if (id) { out.push({ t: 'id', v: id[0] }); i += id[0].length; continue; }
    if ('+-*/^()'.includes(c)) { out.push({ t: 'op', v: c }); i++; continue; }
    throw new Error(`Carácter no permitido: "${c}"`);
  }
  return out;
}

export function compile(src: string, vars: string[]): Compiled {
  const toks = tokenize(src);
  let p = 0;
  const peek = () => toks[p];
  const isOp = (v: string) => peek()?.t === 'op' && peek().v === v;
  const known = new Set([...vars, ...Object.keys(CONSTS)]);

  const expr = (): Compiled => {
    let l = term();
    while (isOp('+') || isOp('-')) {
      const op = toks[p++].v; const r = term(); const a = l;
      l = op === '+' ? (e) => a(e) + r(e) : (e) => a(e) - r(e);
    }
    return l;
  };
  const startsFactor = () => {
    const k = peek();
    return !!k && (k.t === 'num' || k.t === 'id' || (k.t === 'op' && k.v === '('));
  };
  const term = (): Compiled => {
    let l = unary();
    for (;;) {
      if (isOp('*') || isOp('/')) {
        const op = toks[p++].v; const r = unary(); const a = l;
        l = op === '*' ? (e) => a(e) * r(e) : (e) => a(e) / r(e);
      } else if (startsFactor()) {
        const r = unary(); const a = l; l = (e) => a(e) * r(e);
      } else break;
    }
    return l;
  };
  const unary = (): Compiled => {
    if (isOp('-')) { p++; const a = unary(); return (e) => -a(e); }
    if (isOp('+')) { p++; return unary(); }
    return power();
  };
  const power = (): Compiled => {
    const base = atom();
    if (isOp('^')) { p++; const ex = unary(); return (e) => Math.pow(base(e), ex(e)); }
    return base;
  };
  const atom = (): Compiled => {
    const k = toks[p++];
    if (!k) throw new Error('Expresión incompleta');
    if (k.t === 'num') { const v = parseFloat(k.v); return () => v; }
    if (k.t === 'id') {
      if (FUNCS[k.v] && isOp('(')) {
        p++; const a = expr();
        if (!isOp(')')) throw new Error('Falta ")"');
        p++; const f = FUNCS[k.v]; return (e) => f(a(e));
      }
      if (!known.has(k.v)) throw new Error(`Variable desconocida: ${k.v}`);
      const name = k.v;
      return (e) => (name in e ? e[name] : CONSTS[name]);
    }
    if (k.v === '(') {
      const a = expr();
      if (!isOp(')')) throw new Error('Falta ")"');
      p++; return a;
    }
    throw new Error(`Símbolo inesperado: ${k.v}`);
  };

  const root = expr();
  if (p < toks.length) throw new Error(`Símbolo inesperado: ${toks[p].v}`);
  return root;
}
