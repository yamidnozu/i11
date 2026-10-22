export type Vec = number[];

/** Un paso de Runge-Kutta de 4.º orden para y' = f(t, y). */
export function rk4(f: (t: number, y: Vec) => Vec, t: number, y: Vec, h: number): Vec {
  const add = (a: Vec, b: Vec, s: number) => a.map((v, i) => v + s * b[i]);
  const k1 = f(t, y);
  const k2 = f(t + h / 2, add(y, k1, h / 2));
  const k3 = f(t + h / 2, add(y, k2, h / 2));
  const k4 = f(t + h, add(y, k3, h));
  return y.map((v, i) => v + (h / 6) * (k1[i] + 2 * k2[i] + 2 * k3[i] + k4[i]));
}

/** Raíz de g en [a,b] suponiendo g(a) > 0 y g(b) <= 0 (bisección). */
export function bisect(g: (x: number) => number, a: number, b: number, it = 60): number {
  let ga = g(a);
  for (let i = 0; i < it; i++) {
    const m = (a + b) / 2;
    const gm = g(m);
    if (gm <= 0 === ga <= 0) { a = m; ga = gm; } else b = m;
  }
  return (a + b) / 2;
}
