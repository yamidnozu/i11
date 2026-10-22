import { axes, mapper, label, COLORS, INK } from '../render/plot';
import type { SimConfig, Params } from '../core/types';

export interface MState { t: number; x: number; v: number; a: number }
export const muaX = (x0: number, v0: number, a: number, t: number) => x0 + v0 * t + 0.5 * a * t * t;
export const muaV = (v0: number, a: number, t: number) => v0 + a * t;

const P = (p: Params) => ({ x0: +p.x0, v0: +p.v0, a: +p.a, T: +p.T });
const at = (p: Params, t: number): MState => { const q = P(p); return { t, x: muaX(q.x0, q.v0, q.a, t), v: muaV(q.v0, q.a, t), a: q.a }; };

export const muaSim: SimConfig<MState> = {
  id: 'fis.mrua',
  title: 'Movimiento rectilíneo (MRU / MRUA)',
  area: 'ciencias', subarea: 'fisica',
  competencia: 'explicacion_de_fenomenos',
  evidencias: ['CIE_E2.5', 'CIE_E4.2'],
  nivel: 2, tiempoMin: 8, mode: 'dynamic',
  params: [
    { key: 'x0', label: 'Posición inicial', type: 'slider', min: -20, max: 50, step: 1, default: 0, unit: 'm' },
    { key: 'v0', label: 'Velocidad inicial', type: 'slider', min: -10, max: 20, step: 0.5, default: 2, unit: 'm/s' },
    { key: 'a', label: 'Aceleración (0 = MRU)', type: 'slider', min: -5, max: 5, step: 0.5, default: 1, unit: 'm/s²' },
    { key: 'T', label: 'Duración', type: 'slider', min: 1, max: 10, step: 1, default: 6, unit: 's' },
  ],
  logic: {
    init: (p) => at(p, 0),
    step: (s, p, dt) => at(p, Math.min(s.t + dt, P(p).T)),
    done: (s, p) => s.t >= P(p).T - 1e-12,
    sample: (s) => ({ t: s.t, x: s.x, v: s.v, a: s.a }),
    measures: (traj) => {
      const f = traj[traj.length - 1], i = traj[0];
      return { x_final: f.x, v_final: f.v, desplazamiento: f.x - i.x };
    },
  },
  graphs: [
    { id: 'xt', x: 't', y: 'x', title: 'x (m) vs t (s)' },
    { id: 'vt', x: 't', y: 'v', title: 'v (m/s) vs t (s)' },
    { id: 'at', x: 't', y: 'a', title: 'a (m/s²) vs t (s)' },
  ],
  measureLabels: { x_final: 'Posición final (m)', v_final: 'Velocidad final (m/s)', desplazamiento: 'Desplazamiento (m)' },
  challenges: [
    { id: 'ch1', prompt: 'Con x₀ = 0, v₀ = 2 m/s y T = 6 s, elige la aceleración para que el móvil termine en x = 66 m.', fixed: { x0: 0, v0: 2, T: 6 }, checks: [{ measure: 'x_final', target: 66, tol: 0.5 }], hint: 'x = x₀ + v₀t + ½at²' },
  ],
  render: {
    width: 800, height: 200,
    view({ ctx, w, h, state, p }) {
      const q = P(p);
      const xs = [q.x0, muaX(q.x0, q.v0, q.a, q.T), state.x];
      const lo = Math.min(...xs, -5) - 5, hi = Math.max(...xs, 20) + 5;
      const m = mapper(w, h, lo, hi, 0, 1, 40);
      axes(ctx, m, w, h, lo, hi, 0, 1, 'x (m)');
      ctx.fillStyle = COLORS[0]; ctx.fillRect(m.X(state.x) - 18, h / 2 - 12, 36, 24);
      ctx.strokeStyle = INK; ctx.strokeRect(m.X(state.x) - 18, h / 2 - 12, 36, 24);
      label(ctx, `v = ${state.v.toFixed(1)} m/s`, m.X(state.x), h / 2 - 20, 'center', 12);
      label(ctx, `t = ${state.t.toFixed(2)} s`, w - 10, 18, 'right', 13);
    },
  },
};
