import { AREAS, AREA_IDS, type AreaId } from './areas';

/** Puntaje por área (0–100) = mu + sigma·θ, recortado. Es una ESTIMACIÓN, no un puntaje ICFES oficial. */
export const areaScore = (area: AreaId, theta: number) => {
  const a = AREAS[area];
  return Math.max(0, Math.min(100, Math.round(a.mu + a.sigma * theta)));
};

export const areaSE = (area: AreaId, se: number) => AREAS[area].sigma * se;

/** Global (0–500) = round(5·Σ w·S / Σ w); sin inglés el denominador de pesos baja a 10. */
export function globalScore(scores: Partial<Record<AreaId, number>>): number | null {
  let num = 0, den = 0;
  for (const id of AREA_IDS) {
    const s = scores[id];
    if (s === undefined) continue;
    num += AREAS[id].peso * s; den += AREAS[id].peso;
  }
  if (!den) return null;
  return Math.round((num / den) * 5);
}

export function globalSE(ses: Partial<Record<AreaId, number>>): number {
  let v = 0, den = 0;
  for (const id of AREA_IDS) { const s = ses[id]; if (s === undefined) continue; v += (AREAS[id].peso * s) ** 2; den += AREAS[id].peso; }
  return den ? (Math.sqrt(v) / den) * 5 : 0;
}
