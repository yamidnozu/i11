import { axes, mapper, label, COLORS, INK } from '../render/plot';
import type { SimConfig, Params } from '../core/types';

export interface LensState { f: number; d_o: number; h_o: number; d_i: number; M: number; h_i: number; tipo: string }

/** Lente delgada: 1/f = 1/do + 1/di ; M = -di/do. */
export function thinLens(f: number, d_o: number, h_o: number): LensState {
  const inv = 1 / f - 1 / d_o;
  const d_i = Math.abs(inv) < 1e-12 ? Infinity : 1 / inv;
  const M = Number.isFinite(d_i) ? -d_i / d_o : Infinity;
  const h_i = M * h_o;
  const tipo = !Number.isFinite(d_i) ? 'Sin imagen (rayos paralelos)'
    : `${d_i > 0 ? 'Real' : 'Virtual'}, ${M < 0 ? 'invertida' : 'derecha'} y ${Math.abs(M) > 1 ? 'aumentada' : Math.abs(M) < 1 ? 'reducida' : 'del mismo tamaño'}`;
  return { f, d_o, h_o, d_i, M, h_i, tipo };
}

const L = (p: Params) => thinLens(+p.f, +p.d_o, +p.h_o);

export const lensSim: SimConfig<LensState> = {
  id: 'fis.lentes',
  title: 'Óptica: lentes delgadas',
  area: 'ciencias', subarea: 'fisica',
  competencia: 'explicacion_de_fenomenos',
  evidencias: ['CIE_E2.7', 'CIE_E5.1'],
  nivel: 3, tiempoMin: 8, mode: 'static',
  params: [
    { key: 'f', label: 'Distancia focal (− divergente)', type: 'select', default: 10, options: [{ v: 10, l: '+10 cm (convergente)' }, { v: 5, l: '+5 cm (convergente)' }, { v: -10, l: '−10 cm (divergente)' }] },
    { key: 'd_o', label: 'Distancia del objeto', type: 'slider', min: 2, max: 40, step: 0.5, default: 15, unit: 'cm' },
    { key: 'h_o', label: 'Altura del objeto', type: 'slider', min: 1, max: 6, step: 0.5, default: 4, unit: 'cm' },
  ],
  logic: {
    init: (p) => L(p),
    measures: (traj) => { const s = traj[0]; return { d_i: s.d_i, M: s.M, h_i: s.h_i }; },
  },
  measureLabels: { d_i: 'Distancia de la imagen (cm)', M: 'Aumento M', h_i: 'Altura de la imagen (cm)' },
  challenges: [
    { id: 'ch1', prompt: 'Con f = +10 cm, ubica el objeto para que la imagen sea real, invertida y del doble de tamaño (M = −2).', fixed: { f: 10, h_o: 4 }, checks: [{ measure: 'M', target: -2, tol: 0.1 }], hint: 'Entre f y 2f.' },
  ],
  describe: (_m, p) => { const s = L(p); return `Imagen: ${s.tipo}`; },
  render: {
    width: 800, height: 340,
    view({ ctx, w, h, state: s, p }) {
      const xr = 50;
      const m = mapper(w, h, -xr, xr, -12, 12, 30);
      axes(ctx, m, w, h, -xr, xr, -12, 12, 'cm', 'cm');
      ctx.strokeStyle = INK; ctx.lineWidth = 3; ctx.beginPath(); ctx.moveTo(m.X(0), m.Y(-11)); ctx.lineTo(m.X(0), m.Y(11)); ctx.stroke();
      const arrow = (x: number, hh: number, c: string, dash = false) => { ctx.setLineDash(dash ? [6, 4] : []); ctx.strokeStyle = c; ctx.lineWidth = 4; ctx.beginPath(); ctx.moveTo(m.X(x), m.Y(0)); ctx.lineTo(m.X(x), m.Y(hh)); ctx.stroke(); ctx.setLineDash([]); };
      arrow(-s.d_o, s.h_o, COLORS[0]);
      for (const sign of [-1, 1]) { ctx.fillStyle = COLORS[4]; ctx.beginPath(); ctx.arc(m.X(sign * Math.abs(s.f)), m.Y(0), 4, 0, 7); ctx.fill(); }
      if (Number.isFinite(s.d_i)) {
        arrow(s.d_i, s.h_i, COLORS[1], s.d_i < 0);
        ctx.lineWidth = 1.5; ctx.strokeStyle = COLORS[2];
        const tip = [s.d_i, s.h_i];
        const ray = (x0: number, y0: number, x1: number, y1: number) => { ctx.beginPath(); ctx.moveTo(m.X(x0), m.Y(y0)); ctx.lineTo(m.X(x1), m.Y(y1)); ctx.stroke(); };
        ray(-s.d_o, s.h_o, 0, s.h_o); ray(0, s.h_o, tip[0] * 2 || 40, tip[1] + (tip[1] - s.h_o) / (tip[0] || 1) * tip[0]);
        ray(-s.d_o, s.h_o, 0, 0 + (0 - s.h_o) / (0 + s.d_o) * (0 + s.d_o) * 0 + (-s.h_o / -s.d_o) * 0);
      }
      label(ctx, `f = ${+p.f} cm   do = ${s.d_o} cm   di = ${Number.isFinite(s.d_i) ? s.d_i.toFixed(1) : '∞'} cm`, 10, 20, 'left', 13);
      label(ctx, s.tipo, 10, h - 8, 'left', 13);
    },
  },
};
