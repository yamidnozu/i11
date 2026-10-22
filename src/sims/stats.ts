import { label, COLORS, BG, INK, mapper, axes } from '../render/plot';
import type { SimConfig, Params } from '../core/types';

export function describeData(d: number[]) {
  const s = [...d].sort((a, b) => a - b), n = s.length;
  const mean = d.reduce((a, b) => a + b, 0) / n;
  const median = n % 2 ? s[(n - 1) / 2] : (s[n / 2 - 1] + s[n / 2]) / 2;
  const freq = new Map<number, number>();
  d.forEach((v) => freq.set(v, (freq.get(v) || 0) + 1));
  const best = Math.max(...freq.values());
  const modes = [...freq].filter(([, c]) => c === best).map(([v]) => v).sort((a, b) => a - b);
  const med = (a: number[]) => { const m = a.length; return m % 2 ? a[(m - 1) / 2] : (a[m / 2 - 1] + a[m / 2]) / 2; };
  const half = Math.floor(n / 2);
  const q1 = n === 1 ? s[0] : med(s.slice(0, half)), q3 = n === 1 ? s[0] : med(s.slice(n - half));
  const sd = Math.sqrt(d.reduce((a, v) => a + (v - mean) ** 2, 0) / n);
  return { n, mean, median, mode: best > 1 ? modes[0] : NaN, range: s[n - 1] - s[0], sorted: s, sd, q1, q3 };
}

export interface StState { data: number[]; error?: string; stats?: ReturnType<typeof describeData> }
const S = (p: Params): StState => {
  const data = String(p.data).split(/[\s,;]+/).filter(Boolean).map(Number);
  if (!data.length || data.some((v) => !Number.isFinite(v))) return { data: [], error: 'Escribe números separados por coma.' };
  if (data.length > 40) return { data: [], error: 'Máximo 40 datos.' };
  return { data, stats: describeData(data) };
};

export const statsSim: SimConfig<StState> = {
  id: 'mat.estadistica',
  title: 'Estadística: media, mediana y moda',
  area: 'matematicas',
  competencia: 'argumentacion',
  evidencias: ['MAT_E1.1', 'MAT_E3.2'],
  nivel: 2, tiempoMin: 8, mode: 'static',
  params: [{ key: 'data', label: 'Datos (separados por coma)', type: 'text', default: '2, 3, 3, 4, 8' }],
  logic: {
    init: (p) => S(p),
    measures: (traj): Record<string, number> => { const s = traj[0].stats; return s ? { media: s.mean, mediana: s.median, moda: s.mode, rango: s.range, n: s.n, desviacion: s.sd, q1: s.q1, q3: s.q3 } : {}; },
  },
  measureLabels: { media: 'Media', mediana: 'Mediana', moda: 'Moda', rango: 'Rango', n: 'Cantidad de datos', desviacion: 'Desviación estándar', q1: 'Primer cuartil Q1', q3: 'Tercer cuartil Q3' },
  challenges: [
    { id: 'ch1', prompt: 'Partiendo de 2, 3, 3, 4, 8: cambia UN dato para que la media sea 6 y la mediana siga siendo 3.', checks: [{ measure: 'media', target: 6, tol: 0.01 }, { measure: 'mediana', target: 3, tol: 0.01 }], hint: 'La media es sensible a valores extremos; la mediana no.' },
  ],
  table: (p) => { const s = S(p); return { cols: ['posición', 'dato ordenado'], rows: (s.stats?.sorted ?? []).map((v, i) => [i + 1, v]) }; },
  describe: (m) => `Media ${m.media}, mediana ${m.mediana}, rango ${m.rango}`,
  render: {
    width: 700, height: 300,
    view({ ctx, w, h, state: s }) {
      if (s.error || !s.stats) { ctx.fillStyle = BG; ctx.fillRect(0, 0, w, h); label(ctx, s.error ?? '', 20, 40, 'left', 15, '#B91C1C'); return; }
      const st = s.stats, lo = Math.floor(Math.min(...s.data) - 1), hi = Math.ceil(Math.max(...s.data) + 1);
      const m = mapper(w, h, lo, hi, 0, 8, 36);
      axes(ctx, m, w, h, lo, hi, 0, 8, 'valor', 'frecuencia');
      const stack = new Map<number, number>();
      s.data.forEach((v) => { const k = stack.get(v) || 0; stack.set(v, k + 1); ctx.fillStyle = COLORS[0]; ctx.beginPath(); ctx.arc(m.X(v), m.Y(k + 0.5), 9, 0, 7); ctx.fill(); ctx.strokeStyle = INK; ctx.stroke(); });
      ctx.strokeStyle = COLORS[1]; ctx.lineWidth = 3; ctx.beginPath(); ctx.moveTo(m.X(st.median), m.Y(0)); ctx.lineTo(m.X(st.median), m.Y(8)); ctx.stroke();
      label(ctx, `mediana ${st.median}`, m.X(st.median) + 5, m.Y(7.6), 'left', 12, COLORS[1]);
      ctx.fillStyle = COLORS[2]; ctx.beginPath(); ctx.moveTo(m.X(st.mean) - 9, m.Y(0) + 2); ctx.lineTo(m.X(st.mean) + 9, m.Y(0) + 2); ctx.lineTo(m.X(st.mean), m.Y(0) - 14); ctx.fill();
      label(ctx, `media ${+st.mean.toFixed(2)}`, m.X(st.mean), m.Y(0) - 20, 'center', 12, COLORS[2]);
    },
  },
};
