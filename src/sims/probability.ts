import { nextRand } from '../math/rng';
import { label, COLORS, INK, mapper, axes } from '../render/plot';
import type { SimConfig, Params } from '../core/types';

export interface PrState { t: number; n: number; seed: number; counts: number[]; modo: number; maxDev: number }

/** Probabilidades teóricas: 1 dado (6 caras) o suma de 2 dados (2..12). */
export function theoretical(modo: number): number[] {
  if (modo === 1) return Array(6).fill(1 / 6);
  return Array.from({ length: 11 }, (_, i) => (6 - Math.abs(i + 2 - 7)) / 36);
}

export function rollMany(s: PrState, k: number): PrState {
  const counts = s.counts.slice();
  let seed = s.seed;
  for (let i = 0; i < k; i++) {
    let r: number;
    [r, seed] = nextRand(seed);
    const d1 = Math.floor(r * 6);
    if (s.modo === 1) counts[d1]++;
    else { let r2: number; [r2, seed] = nextRand(seed); counts[d1 + Math.floor(r2 * 6)]++; }
  }
  const n = s.n + k, th = theoretical(s.modo);
  const maxDev = Math.max(...counts.map((c, i) => Math.abs(c / n - th[i])));
  return { ...s, n, seed, counts, maxDev };
}

export const initProb = (modo: number): PrState => ({ t: 0, n: 0, seed: 12345, counts: Array(modo === 1 ? 6 : 11).fill(0), modo, maxDev: 1 });
const I = (p: Params): PrState => initProb(+p.modo);

export const probabilitySim: SimConfig<PrState> = {
  id: 'mat.probabilidad',
  title: 'Probabilidad: miles de lanzamientos vs. teoría',
  area: 'matematicas',
  competencia: 'argumentacion',
  evidencias: ['MAT_E2.3', 'MAT_E3.1'],
  nivel: 3, tiempoMin: 8, mode: 'dynamic',
  params: [
    { key: 'modo', label: 'Experimento', type: 'select', default: 2, options: [{ v: 1, l: '1 dado' }, { v: 2, l: 'Suma de 2 dados' }] },
    { key: 'N', label: 'Lanzamientos totales', type: 'slider', min: 100, max: 20000, step: 100, default: 2000 },
  ],
  logic: {
    init: (p) => I(p),
    step: (s, p, dt) => { const k = Math.min(Math.ceil(+p.N / 240), +p.N - s.n); return k > 0 ? { ...rollMany(s, k), t: s.t + dt } : { ...s, t: s.t + dt }; },
    done: (s, p) => s.n >= +p.N,
    sample: (s) => ({ n: s.n, desviacion: s.maxDev }),
    measures: (traj) => { const l = traj[traj.length - 1]; return { lanzamientos: l.n, desviacion_max: l.n ? l.maxDev : NaN }; },
  },
  graphs: [{ id: 'dev', x: 'n', y: 'desviacion', title: 'Desviación máxima vs n (ley de los grandes números)' }],
  measureLabels: { lanzamientos: 'Lanzamientos', desviacion_max: 'Desviación máxima |frecuencia − teórica|' },
  challenges: [
    { id: 'ch1', prompt: 'Con 1 dado, aumenta los lanzamientos hasta que la desviación máxima sea menor que 0,01.', fixed: { modo: 1 }, checks: [{ measure: 'desviacion_max', target: 0, tol: 0.01 }], hint: 'Más lanzamientos → frecuencia más cercana a la teoría.' },
  ],
  render: {
    width: 700, height: 340,
    view({ ctx, w, h, state: s }) {
      const th = theoretical(s.modo), k = th.length;
      const ymax = Math.max(0.2, ...th) * 1.2;
      const m = mapper(w, h, 0, k, 0, ymax, 36);
      axes(ctx, m, w, h, 0, k, 0, ymax, s.modo === 1 ? 'cara' : 'suma', 'frecuencia');
      const bw = (w - 72) / k;
      s.counts.forEach((c, i) => {
        const f = s.n ? c / s.n : 0;
        ctx.fillStyle = COLORS[0]; ctx.globalAlpha = 0.8; ctx.fillRect(m.X(i) + 4, m.Y(f), bw - 8, m.Y(0) - m.Y(f)); ctx.globalAlpha = 1;
        ctx.strokeStyle = COLORS[1]; ctx.lineWidth = 3; ctx.setLineDash([5, 3]); ctx.beginPath(); ctx.moveTo(m.X(i) + 2, m.Y(th[i])); ctx.lineTo(m.X(i) + bw - 2, m.Y(th[i])); ctx.stroke(); ctx.setLineDash([]);
        label(ctx, String(s.modo === 1 ? i + 1 : i + 2), m.X(i) + bw / 2, h - 22, 'center', 11);
      });
      label(ctx, `n = ${s.n}   (barras: simulado · línea naranja: teórico)`, 10, 18, 'left', 13, INK);
    },
  },
};
