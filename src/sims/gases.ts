import { makeRng, gauss } from '../math/rng';
import { label, COLORS, INK, BG } from '../render/plot';
import type { SimConfig, Params } from '../core/types';

/** Ley de gases ideales PV = nRT. R en atm·L/(mol·K). */
export const R_ATM = 0.082057366;
export const idealVolume = (n: number, T: number, P: number, R = R_ATM) => (n * R * T) / P;

/** Gas 2D de discos sin interacción (gas ideal) en una caja W×H; unidades m=1, k=1. */
export interface GState { t: number; W: number; H: number; N: number; T: number; x: number[]; y: number[]; vx: number[]; vy: number[]; impulse: number; pressure: number }
const TIME_SCALE = 4;

export function initGas(N: number, T: number, W: number, H = 100, seed = 42): GState {
  const rng = makeRng(seed);
  const sd = Math.sqrt(T);
  return {
    t: 0, W, H, N, T,
    x: Array.from({ length: N }, () => rng() * W), y: Array.from({ length: N }, () => rng() * H),
    vx: Array.from({ length: N }, () => gauss(rng) * sd), vy: Array.from({ length: N }, () => gauss(rng) * sd),
    impulse: 0, pressure: 0,
  };
}

export function stepGas(s: GState, dt: number): GState {
  const x = s.x.slice(), y = s.y.slice(), vx = s.vx.slice(), vy = s.vy.slice();
  let imp = s.impulse;
  for (let i = 0; i < s.N; i++) {
    x[i] += vx[i] * dt; y[i] += vy[i] * dt;
    while (x[i] < 0 || x[i] > s.W) { if (x[i] < 0) x[i] = -x[i]; else x[i] = 2 * s.W - x[i]; imp += 2 * Math.abs(vx[i]); vx[i] = -vx[i]; }
    while (y[i] < 0 || y[i] > s.H) { if (y[i] < 0) y[i] = -y[i]; else y[i] = 2 * s.H - y[i]; imp += 2 * Math.abs(vy[i]); vy[i] = -vy[i]; }
  }
  const t = s.t + dt;
  const perim = 2 * (s.W + s.H);
  return { ...s, t, x, y, vx, vy, impulse: imp, pressure: t > 0.5 ? imp / (t * perim) : 0 };
}

const G = (p: Params) => initGas(Math.round(+p.N), +p.T, +p.W);
const ke = (s: GState) => s.vx.reduce((a, v, i) => a + 0.5 * (v * v + s.vy[i] * s.vy[i]), 0) / s.N;

export const gasSim: SimConfig<GState> = {
  id: 'qui.gases',
  title: 'Gases: presión, volumen y temperatura (modelo de partículas)',
  area: 'ciencias', subarea: 'quimica',
  competencia: 'explicacion_de_fenomenos',
  evidencias: ['CIE_E2.3', 'CIE_E4.7', 'CIE_E2.6'],
  nivel: 3, tiempoMin: 10, mode: 'dynamic',
  params: [
    { key: 'N', label: 'Cantidad de partículas (∝ moles)', type: 'slider', min: 20, max: 120, step: 10, default: 60 },
    { key: 'T', label: 'Temperatura (u.a.)', type: 'slider', min: 100, max: 600, step: 50, default: 300 },
    { key: 'W', label: 'Ancho del recipiente (volumen)', type: 'slider', min: 40, max: 100, step: 10, default: 100 },
  ],
  logic: {
    init: (p) => G(p),
    step: (s, _p, dt) => stepGas(s, dt * TIME_SCALE),
    done: (s) => s.t >= 40,
    sample: (s) => ({ t: s.t, P: s.pressure }),
    measures: (traj, p) => {
      const s = traj[traj.length - 1];
      const A = s.W * s.H;
      return { presion: s.pressure, area: A, energia_cinetica_media: ke(s), P_por_A_sobre_NT: s.pressure && s.N ? (s.pressure * A) / (s.N * s.T) : 0 };
    },
  },
  graphs: [{ id: 'pt', x: 't', y: 'P', title: 'Presión (u.a.) vs tiempo' }],
  measureLabels: { presion: 'Presión (u.a.)', area: 'Volumen/área (u.a.)', energia_cinetica_media: 'Energía cinética media', P_por_A_sobre_NT: 'P·V / (N·T) ≈ constante' },
  challenges: [
    { id: 'ch1', prompt: 'Con N = 60 y T = 300, reduce el ancho a 50 y ejecuta. P·V/(N·T) debe seguir ≈ 1 (ley de Boyle).', fixed: { N: 60, T: 300 }, checks: [{ measure: 'P_por_A_sobre_NT', target: 1, tol: 0.15 }], hint: 'Si el volumen baja, la presión sube.' },
  ],
  render: {
    width: 800, height: 380,
    view({ ctx, w, h, state: s }) {
      ctx.fillStyle = BG; ctx.fillRect(0, 0, w, h);
      const sc = Math.min((w - 80) / 100, (h - 60) / 100);
      const ox = 40, oy = 30;
      ctx.strokeStyle = INK; ctx.lineWidth = 3; ctx.strokeRect(ox, oy, s.W * sc, s.H * sc);
      ctx.fillStyle = COLORS[4]; ctx.fillRect(ox + s.W * sc, oy - 6, 8, s.H * sc + 12);
      for (let i = 0; i < s.N; i++) {
        const sp = Math.hypot(s.vx[i], s.vy[i]);
        ctx.fillStyle = sp > 1.4 * Math.sqrt(s.T) ? COLORS[1] : COLORS[0];
        ctx.beginPath(); ctx.arc(ox + s.x[i] * sc, oy + s.y[i] * sc, 3.5, 0, 7); ctx.fill();
      }
      label(ctx, `P = ${s.pressure.toFixed(2)}   V = ${(s.W * s.H).toFixed(0)}   N = ${s.N}   T = ${s.T}`, ox, h - 8, 'left', 13);
      label(ctx, 'Tiempo acelerado ×4', w - 10, 20, 'right', 12);
    },
  },
};
