import { balance, countSides } from '../math/chem';
import { label, COLORS, BG, INK } from '../render/plot';
import type { SimConfig, Params } from '../core/types';

export interface BState {
  error?: string; species: string[]; coefs: number[]; elements: string[];
  left: Record<string, number>; right: Record<string, number>; balanced: boolean; solution?: number[]; solMsg?: string; nl: number;
}

function parseCoefs(txt: string, n: number): number[] {
  const parts = txt.split(/[\s,;]+/).filter(Boolean).map((v) => Math.max(0, Math.round(Number(v)) || 0));
  return Array.from({ length: n }, (_, i) => (parts[i] === undefined ? 1 : parts[i]));
}

const B = (p: Params): BState => {
  const eq = String(p.eq);
  const sol = balance(eq);
  try {
    const n = countSides(eq, []).species.length;
    const coefs = parseCoefs(String(p.coefs), n);
    const c = countSides(eq, coefs);
    return { species: c.species, coefs, elements: c.elements, left: c.left, right: c.right, balanced: c.balanced && coefs.every((v) => v > 0), solution: sol.coefs, solMsg: sol.message, nl: c.nl };
  } catch (e) {
    return { error: (e as Error).message, species: [], coefs: [], elements: [], left: {}, right: {}, balanced: false, nl: 0 };
  }
};

export const balanceSim: SimConfig<BState> = {
  id: 'qui.balanceo',
  title: 'Balanceo de ecuaciones y conservación de átomos',
  area: 'ciencias', subarea: 'quimica',
  competencia: 'explicacion_de_fenomenos',
  evidencias: ['CIE_E2.1', 'CIE_E4.6'],
  nivel: 3, tiempoMin: 10, mode: 'static',
  params: [
    { key: 'eq', label: 'Ecuación (usa ->). Ej: C3H8 + O2 -> CO2 + H2O', type: 'text', default: 'C3H8 + O2 -> CO2 + H2O' },
    { key: 'coefs', label: 'Tus coeficientes (separados por coma)', type: 'text', default: '1,1,1,1' },
    { key: 'sol', label: 'Mostrar la solución exacta', type: 'toggle', default: false },
  ],
  logic: {
    init: (p) => B(p),
    measures: (traj) => { const s = traj[0]; return { balanceada: s.balanced ? 1 : 0, especies: s.species.length, suma_coef_solucion: s.solution ? s.solution.reduce((a, b) => a + b, 0) : NaN }; },
  },
  measureLabels: { balanceada: 'Balanceada (1 = sí)', especies: 'Número de sustancias', suma_coef_solucion: 'Suma de coeficientes mínimos' },
  challenges: [
    { id: 'ch1', prompt: 'Balancea la combustión del propano: C3H8 + O2 -> CO2 + H2O. Ajusta tus coeficientes hasta que los átomos coincidan.', fixed: { eq: 'C3H8 + O2 -> CO2 + H2O' }, checks: [{ measure: 'balanceada', target: 1, tol: 0 }], hint: 'Empieza por el carbono y el hidrógeno; deja el oxígeno para el final.' },
  ],
  describe: (m) => (m.balanceada ? 'La ecuación está balanceada' : 'La ecuación aún no está balanceada'),
  render: {
    width: 760, height: 380,
    view({ ctx, w, h, state: s, p }) {
      ctx.fillStyle = BG; ctx.fillRect(0, 0, w, h);
      if (s.error) { label(ctx, s.error, 20, 40, 'left', 15, '#B91C1C'); return; }
      const eqTxt = s.species.map((sp, i) => `${s.coefs[i] === 1 ? '' : s.coefs[i]}${sp}${i === s.nl - 1 ? ' →' : i < s.species.length - 1 ? ' +' : ''}`).join(' ');
      label(ctx, eqTxt, 20, 34, 'left', 18);
      s.elements.forEach((el, i) => {
        const y = 80 + i * 52;
        const l = s.left[el] || 0, r = s.right[el] || 0;
        const ok = l === r;
        label(ctx, el, 20, y + 14, 'left', 16);
        const sq = (n: number, x0: number, col: string) => { for (let k = 0; k < Math.min(n, 28); k++) { ctx.fillStyle = col; ctx.fillRect(x0 + k * 11, y, 9, 20); } if (n > 28) label(ctx, `+${n - 28}`, x0 + 28 * 11 + 4, y + 14, 'left', 11); };
        sq(l, 70, COLORS[0]); sq(r, 400, COLORS[1]);
        label(ctx, `${l}`, 372, y + 15, 'right', 13); label(ctx, `${r}`, 740, y + 15, 'right', 13);
        label(ctx, ok ? '=' : '≠', 385, y + 15, 'center', 16, ok ? COLORS[2] : '#B91C1C');
      });
      label(ctx, 'Reactivos', 70, h - 40, 'left', 12, COLORS[0]); label(ctx, 'Productos', 400, h - 40, 'left', 12, COLORS[1]);
      label(ctx, s.balanced ? '✔ Balanceada' : '✖ No balanceada', w / 2, h - 12, 'center', 16, s.balanced ? COLORS[2] : '#B91C1C');
      if (p.sol) label(ctx, s.solution ? `Solución mínima: ${s.solution.join(', ')}` : (s.solMsg ?? ''), w - 10, 20, 'right', 13, INK);
    },
  },
};
