/** Fracciones exactas con BigInt (para balanceo químico sin errores de redondeo). */
export interface Fraction { n: bigint; d: bigint }

const babs = (a: bigint) => (a < 0n ? -a : a);
export function gcd(a: bigint, b: bigint): bigint {
  a = babs(a); b = babs(b);
  while (b) [a, b] = [b, a % b];
  return a;
}
export const lcm = (a: bigint, b: bigint) => (a / gcd(a, b)) * b;

export function F(n: number | bigint, d: number | bigint = 1): Fraction {
  let nn = BigInt(n), dd = BigInt(d);
  if (dd === 0n) throw new Error('División por cero');
  if (dd < 0n) { nn = -nn; dd = -dd; }
  const g = gcd(nn, dd) || 1n;
  return { n: nn / g, d: dd / g };
}
export const add = (a: Fraction, b: Fraction) => F(a.n * b.d + b.n * a.d, a.d * b.d);
export const sub = (a: Fraction, b: Fraction) => F(a.n * b.d - b.n * a.d, a.d * b.d);
export const mul = (a: Fraction, b: Fraction) => F(a.n * b.n, a.d * b.d);
export const div = (a: Fraction, b: Fraction) => F(a.n * b.d, a.d * b.n);
export const neg = (a: Fraction) => F(-a.n, a.d);
export const isZero = (a: Fraction) => a.n === 0n;
