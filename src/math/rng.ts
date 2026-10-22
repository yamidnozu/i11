/** Mulberry32: generador pseudoaleatorio determinista. Devuelve [valor en [0,1), nuevaSemilla]. */
export function nextRand(seed: number): [number, number] {
  let t = (seed + 0x6d2b79f5) >>> 0;
  let r = Math.imul(t ^ (t >>> 15), 1 | t);
  r = (r + Math.imul(r ^ (r >>> 7), 61 | r)) ^ r;
  return [((r ^ (r >>> 14)) >>> 0) / 4294967296, t];
}

export function makeRng(seed: number): () => number {
  let s = seed >>> 0;
  return () => { const [v, n] = nextRand(s); s = n; return v; };
}

/** Normal estándar por Box-Muller. */
export function gauss(rng: () => number): number {
  let u = 0;
  while (u === 0) u = rng();
  return Math.sqrt(-2 * Math.log(u)) * Math.cos(2 * Math.PI * rng());
}
