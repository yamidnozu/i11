import { label, COLORS, INK, BG } from '../render/plot';
import type { SimConfig, Params } from '../core/types';

export interface Circuit {
  V: number; R1: number; R2: number; R3: number;
  Rp: number; Rt: number; I: number; V1: number; Vp: number; I2: number; I3: number; Ptot: number;
}

/** Fuente V en serie con R1 y la rama paralela R2 || R3. */
export function solveCircuit(V: number, R1: number, R2: number, R3: number): Circuit {
  const Rp = (R2 * R3) / (R2 + R3);
  const Rt = R1 + Rp;
  const I = V / Rt;
  const Vp = I * Rp;
  return { V, R1, R2, R3, Rp, Rt, I, V1: I * R1, Vp, I2: Vp / R2, I3: Vp / R3, Ptot: V * I };
}

const C = (p: Params) => solveCircuit(+p.V, +p.R1, +p.R2, +p.R3);

export const ohmSim: SimConfig<Circuit> = {
  id: 'fis.ohm',
  title: 'Circuitos: Ley de Ohm, serie y paralelo',
  area: 'ciencias', subarea: 'fisica',
  competencia: 'uso_comprensivo_del_conocimiento_cientifico',
  evidencias: ['CIE_E2.4', 'CIE_E4.1'],
  nivel: 3, tiempoMin: 8, mode: 'static',
  params: [
    { key: 'V', label: 'Voltaje de la fuente', type: 'slider', min: 1, max: 24, step: 1, default: 12, unit: 'V' },
    { key: 'R1', label: 'R1 (en serie)', type: 'slider', min: 0.5, max: 20, step: 0.5, default: 2, unit: 'Ω' },
    { key: 'R2', label: 'R2 (paralelo)', type: 'slider', min: 0.5, max: 20, step: 0.5, default: 6, unit: 'Ω' },
    { key: 'R3', label: 'R3 (paralelo)', type: 'slider', min: 0.5, max: 20, step: 0.1, default: 3, unit: 'Ω' },
  ],
  logic: {
    init: (p) => C(p),
    measures: (traj) => { const c = traj[0]; return { R_paralelo: c.Rp, R_total: c.Rt, I_total: c.I, V_R1: c.V1, V_paralelo: c.Vp, I_R2: c.I2, I_R3: c.I3, potencia: c.Ptot }; },
  },
  measureLabels: { R_paralelo: 'R paralelo (Ω)', R_total: 'R total (Ω)', I_total: 'I total (A)', V_R1: 'V en R1 (V)', V_paralelo: 'V en la rama paralela (V)', I_R2: 'I en R2 (A)', I_R3: 'I en R3 (A)', potencia: 'Potencia total (W)' },
  challenges: [
    { id: 'ch1', prompt: 'Con V = 12 V, R1 = 2 Ω y R2 = 6 Ω, ajusta R3 para que la corriente total sea 4 A.', fixed: { V: 12, R1: 2, R2: 6 }, checks: [{ measure: 'I_total', target: 4, tol: 0.05 }], hint: 'Necesitas R_paralelo = 1 Ω.' },
  ],
  describe: (m) => `Corriente total ${m.I_total?.toFixed(2)} A, resistencia total ${m.R_total?.toFixed(2)} ohmios`,
  render: {
    width: 800, height: 320,
    view({ ctx, w, h, state: c }) {
      ctx.fillStyle = BG; ctx.fillRect(0, 0, w, h);
      ctx.strokeStyle = INK; ctx.lineWidth = 3;
      const L = 90, R = 710, T = 70, B = 250;
      ctx.beginPath(); ctx.moveTo(L, T); ctx.lineTo(300, T); ctx.moveTo(380, T); ctx.lineTo(480, T); ctx.lineTo(R, T);
      ctx.lineTo(R, B); ctx.lineTo(L, B); ctx.lineTo(L, T); ctx.stroke();
      ctx.beginPath(); ctx.moveTo(480, T); ctx.lineTo(480, B); ctx.moveTo(600, T); ctx.lineTo(600, B); ctx.stroke();
      const box = (x: number, y: number, bw: number, bh: number, txt: string, col: string) => { ctx.fillStyle = '#fff'; ctx.fillRect(x, y, bw, bh); ctx.strokeStyle = col; ctx.lineWidth = 3; ctx.strokeRect(x, y, bw, bh); label(ctx, txt, x + bw / 2, y + bh / 2 + 4, 'center', 12); };
      box(300, T - 14, 80, 28, `R1 ${c.R1}Ω`, COLORS[0]);
      box(445, 140, 70, 30, `R2 ${c.R2}Ω`, COLORS[1]);
      box(565, 140, 70, 30, `R3 ${c.R3}Ω`, COLORS[2]);
      ctx.fillStyle = '#fff'; ctx.fillRect(L - 14, 130, 28, 50);
      label(ctx, `${c.V} V`, L, 160, 'center', 13);
      label(ctx, `I = ${c.I.toFixed(2)} A`, 200, T - 14, 'center', 13, COLORS[3]);
      label(ctx, `I2 = ${c.I2.toFixed(2)} A`, 480, 122, 'center', 12);
      label(ctx, `I3 = ${c.I3.toFixed(2)} A`, 600, 122, 'center', 12);
      label(ctx, `Rtotal = ${c.Rt.toFixed(2)} Ω   |   P = ${c.Ptot.toFixed(1)} W`, w / 2, B + 40, 'center', 14);
    },
  },
};
