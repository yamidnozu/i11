import { rk4 } from '../math/rk4';
import { axes, mapper, label, COLORS } from '../render/plot';
import type { SimConfig, Params } from '../core/types';

export interface LVState { t: number; x: number; y: number; V: number; xmin: number; xmax: number }
export interface LVPar { alpha: number; beta: number; delta: number; gamma: number }

/** Invariante de Lotka-Volterra: V = δx − γ ln x + βy − α ln y. */
export const invariant = (x: number, y: number, q: LVPar) => q.delta * x - q.gamma * Math.log(x) + q.beta * y - q.alpha * Math.log(y);

export function stepLV(s: LVState, q: LVPar, dt: number): LVState {
  const f = (_t: number, v: number[]) => [q.alpha * v[0] - q.beta * v[0] * v[1], q.delta * v[0] * v[1] - q.gamma * v[1]];
  const [x, y] = rk4(f, s.t, [s.x, s.y], dt);
  return { t: s.t + dt, x, y, V: invariant(x, y, q), xmin: Math.min(s.xmin, x), xmax: Math.max(s.xmax, x) };
}
export const initLV = (x: number, y: number, q: LVPar): LVState => ({ t: 0, x, y, V: invariant(x, y, q), xmin: x, xmax: x });

const Q = (p: Params): LVPar => ({ alpha: +p.alpha, beta: +p.beta, delta: +p.delta, gamma: +p.gamma });

export const lotkaSim: SimConfig<LVState> = {
  id: 'bio.lotka',
  title: 'Depredador y presa (Lotka-Volterra)',
  area: 'ciencias', subarea: 'biologia',
  competencia: 'indagacion',
  evidencias: ['CIE_E2.8', 'CIE_E5.4', 'CIE_E3.3'],
  nivel: 3, tiempoMin: 10, mode: 'dynamic',
  params: [
    { key: 'alpha', label: 'Crecimiento de presas (α)', type: 'slider', min: 0.5, max: 2, step: 0.1, default: 1 },
    { key: 'beta', label: 'Depredación (β)', type: 'slider', min: 0.05, max: 0.2, step: 0.01, default: 0.1 },
    { key: 'delta', label: 'Beneficio al depredador (δ)', type: 'slider', min: 0.01, max: 0.05, step: 0.01, default: 0.02 },
    { key: 'gamma', label: 'Mortalidad de depredadores (γ)', type: 'slider', min: 0.2, max: 1, step: 0.1, default: 0.5 },
    { key: 'x0', label: 'Presas iniciales', type: 'slider', min: 5, max: 60, step: 1, default: 40 },
    { key: 'y0', label: 'Depredadores iniciales', type: 'slider', min: 2, max: 30, step: 1, default: 9 },
  ],
  logic: {
    init: (p) => initLV(+p.x0, +p.y0, Q(p)),
    step: (s, p, dt) => stepLV(s, Q(p), dt),
    done: (s) => s.t >= 40,
    sample: (s) => ({ t: s.t, presas: s.x, depredadores: s.y }),
    measures: (traj, p) => {
      const l = traj[traj.length - 1], q = Q(p);
      return { amplitud_presas: l.xmax - l.xmin, eq_presas: q.gamma / q.delta, eq_depredadores: q.alpha / q.beta, deriva_invariante: Math.abs(l.V - traj[0].V) / Math.abs(traj[0].V) };
    },
  },
  graphs: [
    { id: 'xt', x: 't', y: 'presas', title: 'Presas vs t' },
    { id: 'yt', x: 't', y: 'depredadores', title: 'Depredadores vs t' },
  ],
  measureLabels: { amplitud_presas: 'Oscilación de presas (máx − mín)', eq_presas: 'Equilibrio de presas γ/δ', eq_depredadores: 'Equilibrio de depredadores α/β', deriva_invariante: 'Error relativo del invariante' },
  challenges: [
    { id: 'ch1', prompt: 'Con α=1, β=0,1, δ=0,02 y γ=0,5, elige presas y depredadores iniciales para que las poblaciones NO oscilen (equilibrio).', fixed: { alpha: 1, beta: 0.1, delta: 0.02, gamma: 0.5 }, checks: [{ measure: 'amplitud_presas', target: 0, tol: 0.5 }], hint: 'El equilibrio está en x = γ/δ, y = α/β.' },
  ],
  render: {
    width: 700, height: 380,
    view({ ctx, w, h, state, traj }) {
      const xs = traj.map((s) => s.x), ys = traj.map((s) => s.y);
      const xmax = Math.max(70, ...xs) * 1.05, ymax = Math.max(35, ...ys) * 1.05;
      const m = mapper(w, h, 0, xmax, 0, ymax, 40);
      axes(ctx, m, w, h, 0, xmax, 0, ymax, 'presas', 'depredadores');
      ctx.strokeStyle = COLORS[0]; ctx.lineWidth = 2.5; ctx.beginPath();
      traj.forEach((s, i) => (i ? ctx.lineTo(m.X(s.x), m.Y(s.y)) : ctx.moveTo(m.X(s.x), m.Y(s.y)))); ctx.stroke();
      ctx.fillStyle = COLORS[1]; ctx.beginPath(); ctx.arc(m.X(state.x), m.Y(state.y), 6, 0, 7); ctx.fill();
      label(ctx, 'Plano de fases', 10, 18, 'left', 13);
    },
  },
};
