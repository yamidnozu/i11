import { rk4, bisect } from '../math/rk4';
import { axes, mapper, label, COLORS, INK } from '../render/plot';
import type { SimConfig, Params } from '../core/types';

export interface PState { t: number; x: number; y: number; vx: number; vy: number; ymax: number; done: boolean }

const DRAG = 0.02; // coeficiente cuadrático por unidad de masa (1/m)

export function initProjectile(v0: number, thetaDeg: number): PState {
  const th = (thetaDeg * Math.PI) / 180;
  return { t: 0, x: 0, y: 0, vx: v0 * Math.cos(th), vy: v0 * Math.sin(th), ymax: 0, done: false };
}

export function stepProjectile(s: PState, g: number, drag: boolean, dt: number): PState {
  if (s.done) return s;
  const k = drag ? DRAG : 0;
  const f = (_t: number, y: number[]) => {
    const sp = Math.hypot(y[2], y[3]);
    return [y[2], y[3], -k * sp * y[2], -g - k * sp * y[3]];
  };
  const y0 = [s.x, s.y, s.vx, s.vy];
  const adv = (hh: number) => rk4(f, s.t, y0, hh);
  let hh = dt;
  let n = adv(hh);
  let ymax = Math.max(s.ymax, s.y);
  if (s.vy > 0 && n[3] <= 0) {
    const ha = bisect((q) => adv(q)[3], 0, dt);
    ymax = Math.max(ymax, adv(ha)[1]);
  }
  let done = false;
  if (n[1] < 0) {
    hh = s.y <= 1e-12 ? 0 : bisect((q) => adv(q)[1], 0, dt);
    n = hh === 0 ? [...y0] : adv(hh);
    n[1] = 0; done = true;
  }
  ymax = Math.max(ymax, n[1]);
  return { t: s.t + hh, x: n[0], y: n[1], vx: n[2], vy: n[3], ymax, done };
}

/** Simula hasta el impacto (para pruebas y medidas). */
export function simulateProjectile(v0: number, thetaDeg: number, g: number, drag = false, dt = 1 / 120): PState {
  let s = initProjectile(v0, thetaDeg);
  for (let i = 0; i < 2_000_000 && !s.done; i++) s = stepProjectile(s, g, drag, dt);
  return s;
}

const P = (p: Params) => ({ v0: +p.v0, th: +p.theta, g: +p.g, drag: !!p.drag });

export const projectileSim: SimConfig<PState> = {
  id: 'fis.proyectil',
  title: 'Lanzamiento de proyectiles',
  area: 'ciencias', subarea: 'fisica',
  competencia: 'uso_comprensivo_del_conocimiento_cientifico',
  evidencias: ['CIE_E2.5', 'CIE_E4.2', 'CIE_E5.3'],
  nivel: 2, tiempoMin: 8, mode: 'dynamic',
  params: [
    { key: 'v0', label: 'Velocidad inicial', type: 'slider', min: 1, max: 50, step: 0.5, default: 20, unit: 'm/s' },
    { key: 'theta', label: 'Ángulo', type: 'slider', min: 0, max: 90, step: 1, default: 45, unit: '°' },
    { key: 'g', label: 'Gravedad', type: 'select', options: [{ v: 9.8, l: 'Tierra (9,8)' }, { v: 10, l: 'Modo examen ICFES (10)' }, { v: 1.62, l: 'Luna (1,62)' }], default: 9.8 },
    { key: 'drag', label: 'Resistencia del aire', type: 'toggle', default: false },
  ],
  logic: {
    init: (p) => initProjectile(P(p).v0, P(p).th),
    step: (s, p, dt) => stepProjectile(s, P(p).g, P(p).drag, dt),
    done: (s) => s.done,
    sample: (s) => ({ t: s.t, x: s.x, y: s.y, vy: s.vy, vx: s.vx }),
    measures: (traj) => {
      const l = traj[traj.length - 1];
      return { alcance: l.x, altura_max: l.ymax, t_vuelo: l.t };
    },
  },
  graphs: [
    { id: 'xt', x: 't', y: 'x', title: 'x (m) vs t (s)' },
    { id: 'yt', x: 't', y: 'y', title: 'y (m) vs t (s)' },
    { id: 'vt', x: 't', y: 'vy', title: 'vy (m/s) vs t (s)' },
  ],
  measureLabels: { alcance: 'Alcance (m)', altura_max: 'Altura máxima (m)', t_vuelo: 'Tiempo de vuelo (s)' },
  challenges: [
    { id: 'ch1', prompt: 'Con v₀ = 20 m/s y g = 9,8 m/s², ajusta el ángulo para que el proyectil llegue a 40 m (±0,5).', fixed: { v0: 20, g: 9.8, drag: false }, checks: [{ measure: 'alcance', target: 40, tol: 0.5 }], hint: 'Hay dos ángulos posibles: complementarios.' },
    { id: 'ch2', prompt: 'Con v₀ = 20 m/s y g = 9,8, encuentra el ángulo de máximo alcance.', fixed: { v0: 20, g: 9.8, drag: false }, checks: [{ measure: 'alcance', target: 40.82, tol: 0.1 }], hint: 'Piensa en sen(2θ).' },
  ],
  describe: (m) => `Alcance ${m.alcance?.toFixed(1)} m, altura máxima ${m.altura_max?.toFixed(1)} m, tiempo de vuelo ${m.t_vuelo?.toFixed(2)} s`,
  render: {
    width: 800, height: 400,
    view({ ctx, w, h, state, traj, p }) {
      const { v0, g } = P(p);
      const xmax = Math.max(5, ((v0 * v0) / g) * 1.05), ymax = Math.max(3, ((v0 * v0) / (2 * g)) * 1.05);
      const pad = 40, sc = Math.min((w - 2 * pad) / xmax, (h - 2 * pad) / ymax);
      const m = mapper(w, h, 0, (w - 2 * pad) / sc, 0, (h - 2 * pad) / sc, pad);
      axes(ctx, m, w, h, 0, (w - 2 * pad) / sc, 0, (h - 2 * pad) / sc, 'x (m)', 'y (m)');
      ctx.strokeStyle = COLORS[0]; ctx.lineWidth = 3; ctx.beginPath();
      traj.forEach((s, i) => (i ? ctx.lineTo(m.X(s.x), m.Y(s.y)) : ctx.moveTo(m.X(s.x), m.Y(s.y))));
      ctx.stroke();
      ctx.fillStyle = COLORS[1]; ctx.beginPath(); ctx.arc(m.X(state.x), m.Y(state.y), 8, 0, 7); ctx.fill();
      ctx.strokeStyle = INK; ctx.lineWidth = 2; ctx.stroke();
      const arrow = (dx: number, dy: number, c: string) => {
        ctx.strokeStyle = c; ctx.lineWidth = 3; ctx.beginPath();
        ctx.moveTo(m.X(state.x), m.Y(state.y)); ctx.lineTo(m.X(state.x) + dx, m.Y(state.y) - dy); ctx.stroke();
      };
      if (!state.done) { arrow(state.vx * 2.5, 0, COLORS[2]); arrow(0, state.vy * 2.5, COLORS[3]); }
      label(ctx, 'vx', m.X(state.x) + state.vx * 2.5 + 4, m.Y(state.y) - 4, 'left', 11, COLORS[2]);
      label(ctx, `t = ${state.t.toFixed(2)} s`, w - 10, 20, 'right', 13);
    },
  },
};
