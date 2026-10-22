import { F, Fraction, add, sub, mul, div, neg, isZero, gcd, lcm } from './fractions';

export type Atoms = Record<string, number>;

/** Cuenta átomos de una fórmula, con paréntesis anidados: Ca(OH)2 -> {Ca:1,O:2,H:2}. */
export function parseFormula(f: string): Atoms {
  const s = f.replace(/\s+/g, '');
  let i = 0;
  const num = () => {
    const m = /^\d+/.exec(s.slice(i));
    if (!m) return 1;
    i += m[0].length;
    return parseInt(m[0], 10);
  };
  const group = (): Atoms => {
    const out: Atoms = {};
    while (i < s.length && s[i] !== ')') {
      if (s[i] === '(') {
        i++;
        const g = group();
        if (s[i] !== ')') throw new Error('Paréntesis sin cerrar');
        i++;
        const n = num();
        for (const k in g) out[k] = (out[k] || 0) + g[k] * n;
      } else {
        const m = /^[A-Z][a-z]?/.exec(s.slice(i));
        if (!m) throw new Error(`Fórmula no válida: "${f}"`);
        i += m[0].length;
        out[m[0]] = (out[m[0]] || 0) + num();
      }
    }
    return out;
  };
  const r = group();
  if (i < s.length) throw new Error('Paréntesis sin abrir');
  return r;
}

export interface ParsedEq { left: string[]; right: string[] }

export function parseEquation(eq: string): ParsedEq {
  const parts = eq.split(/->|→|=>|=/);
  if (parts.length !== 2) throw new Error('Usa una flecha: A + B -> C');
  const side = (x: string) => x.split('+').map((t) => t.trim()).filter(Boolean);
  const left = side(parts[0]), right = side(parts[1]);
  if (!left.length || !right.length) throw new Error('Faltan reactivos o productos');
  return { left, right };
}

export interface BalanceResult { ok: boolean; coefs?: number[]; message?: string; nullity?: number }

/** Balanceo por espacio nulo en Q (Gauss-Jordan con fracciones exactas). */
export function balance(eq: string): BalanceResult {
  let parsed: ParsedEq;
  let cols: Atoms[];
  try {
    parsed = parseEquation(eq);
    cols = [...parsed.left, ...parsed.right].map(parseFormula);
  } catch (e) {
    return { ok: false, message: (e as Error).message };
  }
  const nl = parsed.left.length;
  const elements = [...new Set(cols.flatMap((c) => Object.keys(c)))];
  let M: Fraction[][] = elements.map((el) => cols.map((c, j) => F((c[el] || 0) * (j < nl ? 1 : -1))));
  const nC = cols.length;
  const pivots: number[] = [];
  let r = 0;
  for (let c = 0; c < nC && r < M.length; c++) {
    let p = -1;
    for (let i = r; i < M.length; i++) if (!isZero(M[i][c])) { p = i; break; }
    if (p < 0) continue;
    [M[r], M[p]] = [M[p], M[r]];
    const pv = M[r][c];
    M[r] = M[r].map((x) => div(x, pv));
    for (let i = 0; i < M.length; i++) {
      if (i !== r && !isZero(M[i][c])) {
        const f = M[i][c];
        M[i] = M[i].map((x, j) => sub(x, mul(f, M[r][j])));
      }
    }
    pivots.push(c);
    r++;
  }
  const free = [...Array(nC).keys()].filter((c) => !pivots.includes(c));
  if (free.length === 0) return { ok: false, nullity: 0, message: 'No se puede balancear: revisa que los mismos elementos estén a ambos lados.' };
  if (free.length > 1) return { ok: false, nullity: free.length, message: 'Hay varias combinaciones posibles: la ecuación mezcla más de una reacción.' };
  const f = free[0];
  const x: Fraction[] = Array.from({ length: nC }, () => F(0));
  x[f] = F(1);
  pivots.forEach((c, ri) => { x[c] = neg(M[ri][f]); });
  const L = x.reduce((a, v) => lcm(a, v.d), 1n);
  let ints = x.map((v) => v.n * (L / v.d));
  const g = ints.reduce((a, v) => gcd(a, v), 0n) || 1n;
  ints = ints.map((v) => v / g);
  if (ints.every((v) => v <= 0n)) ints = ints.map((v) => -v);
  if (ints.some((v) => v <= 0n)) return { ok: false, nullity: 1, message: 'Esta ecuación no tiene coeficientes positivos: revisa las sustancias.' };
  return { ok: true, nullity: 1, coefs: ints.map((v) => Number(v)) };
}

/** Átomos totales a cada lado dados los coeficientes del usuario. */
export function countSides(eq: string, coefs: number[]) {
  const p = parseEquation(eq);
  const all = [...p.left, ...p.right].map(parseFormula);
  const nl = p.left.length;
  const left: Atoms = {}, right: Atoms = {};
  all.forEach((a, j) => {
    const tgt = j < nl ? left : right;
    for (const k in a) tgt[k] = (tgt[k] || 0) + a[k] * (coefs[j] ?? 1);
  });
  const elements = [...new Set([...Object.keys(left), ...Object.keys(right)])];
  return { left, right, elements, balanced: elements.every((e) => (left[e] || 0) === (right[e] || 0)), species: [...p.left, ...p.right], nl };
}
