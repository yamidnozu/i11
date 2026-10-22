/** IRT 3PL + EAP en rejilla con prior N(0,1). Logística estable. */
export interface Item { b: number; c: number; a?: number }
export interface Resp { item: Item; correct: boolean }

export const P3 = (th: number, it: Item) => { const a = it.a ?? 1; return it.c + (1 - it.c) / (1 + Math.exp(-a * (th - it.b))); };

export function fisher(th: number, it: Item): number {
  const a = it.a ?? 1, p = P3(th, it), q = 1 - p;
  const pstar = (p - it.c) / (1 - it.c);
  return p > 0 ? (a * a * q * pstar * pstar) / p : 0;
}

const GRID = Array.from({ length: 121 }, (_, i) => -4 + i * (8 / 120));

export function eap(resps: Resp[]): { theta: number; se: number } {
  const lp = GRID.map((t) => {
    let l = -0.5 * t * t;
    for (const r of resps) { const p = P3(t, r.item); l += Math.log(r.correct ? p : 1 - p); }
    return l;
  });
  const mx = Math.max(...lp);
  const w = lp.map((v) => Math.exp(v - mx));
  const z = w.reduce((a, b) => a + b, 0);
  const th = GRID.reduce((a, t, i) => a + (t * w[i]) / z, 0);
  const v = GRID.reduce((a, t, i) => a + ((t - th) ** 2 * w[i]) / z, 0);
  return { theta: th, se: Math.sqrt(v) };
}

/** Elige el ítem de mayor información cerca de theta (aleatorio entre top-k para no repetir). */
export function pickItem<T extends { item: Item }>(th: number, pool: T[], rnd: () => number, k = 3): T | undefined {
  if (!pool.length) return undefined;
  const ranked = [...pool].sort((x, y) => fisher(th, y.item) - fisher(th, x.item)).slice(0, k);
  return ranked[Math.floor(rnd() * ranked.length)];
}
