/** Mini-tipografía matemática (sin dependencias). Soporta \frac \sqrt ^ _ \text \bar, letras griegas y símbolos. */
const ESC = (s: string) => s.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
const GREEK: Record<string, string> = { alpha: 'α', beta: 'β', gamma: 'γ', delta: 'δ', epsilon: 'ε', theta: 'θ', lambda: 'λ', mu: 'μ', pi: 'π', rho: 'ρ', sigma: 'σ', omega: 'ω', phi: 'φ', tau: 'τ', Delta: 'Δ', Omega: 'Ω', Sigma: 'Σ' };
const SYM: Record<string, string> = { cdot: '·', times: '×', pm: '±', approx: '≈', neq: '≠', leq: '≤', geq: '≥', rightarrow: '→', to: '→', infty: '∞', degree: '°', circ: '°', ldots: '…', sum: '∑', Rightarrow: '⇒', div: '÷', propto: '∝', partial: '∂', checkmark: '✓', quad: '\u2003', qquad: '\u2003\u2003' };
const FUNCS = new Set(['sin', 'cos', 'tan', 'ln', 'log', 'exp', 'max', 'min', 'sen', 'lim']);

const OPD = String.raw`(?:\d[\d{},.]*|[A-Za-z](?:_\{?\w+\}?)?|\\(?:gamma|delta|theta))`;
const FRAC = new RegExp(String.raw`(${OPD}(?:\\cdot\s?${OPD})*)\s?/\s?(${OPD})`, 'g');
/** a/b escrito en línea se dibuja como fracción apilada (fuera de \text{...}, donde m/s se queda como unidad). */
const apilar = (src: string): string => src.split(/(\\text\{[^{}]*\})/).map((p, k) => (k % 2 ? p : p.replace(FRAC, '\\frac{$1}{$2}'))).join('');

export function tex(src0: string): string {
  const src = apilar(src0);
  let i = 0;
  const skip = () => { while (src[i] === ' ') i++; };
  const chr = (c: string) => (/[A-Za-z]/.test(c) ? `<i>${c}</i>` : c === '-' ? '−' : ESC(c));
  const group = () => { i++; const o = seq('}'); if (src[i] === '}') i++; return o; };
  const raw = () => { skip(); if (src[i] !== '{') return ''; i++; const j = src.indexOf('}', i); const t = src.slice(i, j < 0 ? src.length : j); i = j < 0 ? src.length : j + 1; return t; };
  const atom = (): string => { skip(); if (src[i] === '{') return group(); if (src[i] === '\\') return command(); const c = src[i++]; return c === undefined ? '' : chr(c); };
  function command(): string {
    i++;
    let n = '';
    while (i < src.length && /[A-Za-z]/.test(src[i])) n += src[i++];
    if (!n) { const c = src[i++]; return c === ',' ? '\u2009' : c === ';' ? '\u2005' : c === ' ' ? ' ' : ESC(c ?? ''); }
    if (n === 'frac' || n === 'tfrac' || n === 'dfrac') { const a = atom(), b = atom(); return `<span class="frac"><span class="n">${a}</span><span class="d">${b}</span></span>`; }
    if (n === 'sqrt') { const a = atom(); return `<span class="sqrt"><span class="rd">√</span><span class="rc">${a}</span></span>`; }
    if (n === 'text') return `<span class="tx">${ESC(raw())}</span>`;
    if (n === 'bar') return `<span class="ob">${atom()}</span>`;
    if (n === 'vec') return `<span class="vc">${atom()}</span>`;
    if (GREEK[n]) return /^[A-Z]/.test(n) ? GREEK[n] : `<i class="gr">${GREEK[n]}</i>`;
    if (SYM[n]) return SYM[n];
    if (FUNCS.has(n)) return `<span class="fn">${n}</span>`;
    return ESC(n);
  }
  function seq(end?: string): string {
    let out = '';
    while (i < src.length && src[i] !== end) {
      const c = src[i];
      if (c === ' ') { i++; continue; }
      if (c === '{') out += group();
      else if (c === '\\') out += command();
      else if (c === '^' || c === '_') {
        i++;
        const first = atom();
        skip();
        const other = c === '^' ? '_' : '^';
        if (src[i] === other) { i++; const second = atom(); const up = c === '^' ? first : second, dn = c === '^' ? second : first; out += `<span class="ss"><sup>${up}</sup><sub>${dn}</sub></span>`; }
        else out += c === '^' ? `<sup>${first}</sup>` : `<sub>${first}</sub>`;
      } else { i++; out += chr(c); }
    }
    return out;
  }
  return `<span class="tex">${seq()}</span>`;
}

/** Texto enriquecido: escapa HTML, admite **negrita** y fórmulas entre $...$. */
export let autoMath: ((s: string) => string) | null = null;
export const setAutoMath = (f: (s: string) => string) => { autoMath = f; };
/** Matemática explícita: $...$ sin espacio pegado a los signos, para no confundirla con pesos ($4.000). */
export const EXPLICIT = '\\$(?=\\S)[^$]*?(?<=\\S)\\$';
const OPS: Record<string, string> = { '×': '\\times ', '·': '\\cdot ', '+': '+', '=': '=', '−': '-', '÷': '÷' };
/** "$6$ × $6$ = $36$" son tres fórmulas pegadas: se funden en una sola para que se lea y se vea como una cuenta. */
const fundir = (s: string): string => { let p = ''; while (p !== s) { p = s; s = s.replace(/\$(?=\S)([^$]*?)(?<=\S)\$\s*([×·+=−÷])\s*\$(?=\S)([^$]*?)(?<=\S)\$/g, (_, a, o, b) => `$${a}${OPS[o]}${b}$`); } return s; };
export function rich(s0: string): string {
  const s = fundir(s0);
  const trozos = s.split(new RegExp(`(${EXPLICIT})`));
  // si la ecuación se parte en renglones, el punto o la coma que la sigue viaja con el último renglón
  for (let k = 1; k < trozos.length; k += 2) { const m = trozos[k + 1]?.match(/^[.,;:]/); if (m && (/=[^=]*=|\\Rightarrow/.test(trozos[k]))) { trozos[k] = trozos[k].slice(0, -1) + `\\text{${m[0]}}$`; trozos[k + 1] = trozos[k + 1].slice(1); } }
  return trozos.map((part, k) => (k % 2 ? eqn(part.slice(1, -1)) : part.split('**').map((seg, j) => { const h = seg.split(/(\{\{.+?\}\})/).map((q, n) => { if (n % 2 === 0) return autoMath ? autoMath(q) : ESC(q); const e = q.slice(2, -2).replace(/^!/, ''); return `<span class="en" role="button" tabindex="0" lang="en" data-en="${ESC(e).replace(/"/g, '&quot;')}">${ESC(e)}</span>`; }).join(''); return j % 2 ? `<strong>${h}</strong>` : h; }).join(''))).join('');
}

/** Ecuación en varias líneas: parte las cadenas "a = b = c" y los "⇒" en renglones alineados por el signo "=". */
export function eqn(src: string): string {
  const cortar = (t: string, ini: RegExp): { sep: string; txt: string }[] => {
    const out: { sep: string; txt: string }[] = [];
    let d = 0, cur = '', sep = '';
    for (let i = 0; i < t.length; i++) {
      const c = t[i];
      if (c === '{') d++; else if (c === '}') d--;
      const m = d === 0 ? t.slice(i).match(ini) : null;
      if (m) { out.push({ sep, txt: cur.trim() }); sep = m[1] ?? m[0]; cur = ''; i += m[0].length - 1; continue; }
      cur += c;
    }
    out.push({ sep, txt: cur.trim() });
    return out;
  };
  const rows: { l: string; r: string; e: string; solo?: boolean }[] = [];
  for (const g of cortar(src, /^(?:\\ )?(\\Rightarrow)(?:\\ )?|^(,)\\ /)) {
    const lead = g.sep.includes('Rightarrow') ? '⇒ ' : '';
    const segs = /\\text\{o\}/.test(g.txt) ? [{ sep: '', txt: g.txt }] : cortar(g.txt, /^(=|\\approx)(?:\\ )?/);
    if (segs.length === 1) { rows.push({ l: lead + segs[0].txt, r: '', e: '', solo: true }); continue; }
    segs.forEach((x, k) => rows.push(k === 0 ? { l: lead + x.txt, r: '', e: '' } : { l: '', r: x.sep.startsWith('\\approx') ? '≈' : '=', e: x.txt }));
    const n = rows.length - segs.length;
    rows.splice(n, 2, { l: rows[n].l, r: rows[n + 1].r, e: rows[n + 1].e });
  }
  if (rows.length <= 1) return tex(src);
  const cel = (c: string) => (c ? tex(c) : '');
  return `<span class="eqs">${rows.map((x) => `<span class="eq${x.solo ? ' solo' : ''}"><span class="el">${x.l.startsWith('⇒ ') ? '<span class="imp">⇒</span> ' + cel(x.l.slice(2)) : cel(x.l)}</span>${x.solo ? '' : `<span class="er">${x.r}</span><span class="ee">${cel(x.e)}</span>`}</span>`).join('')}</span>`;
}
