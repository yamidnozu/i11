import { label, COLORS, BG, INK } from '../render/plot';
import type { SimConfig, Params } from '../core/types';

/** Gametos de un genotipo con locus independientes: "AaBb" -> AB, Ab, aB, ab. */
export function gametes(g: string): string[] {
  const loci = g.match(/[A-Za-z]{2}/g) ?? [];
  if (!loci.length || loci.join('') !== g) throw new Error(`Genotipo no válido: "${g}". Usa pares como Aa o AaBb.`);
  let out = [''];
  for (const l of loci) {
    if (l[0].toLowerCase() !== l[1].toLowerCase()) throw new Error(`Cada par debe usar la misma letra: ${l}`);
    out = out.flatMap((o) => [...new Set([l[0], l[1]])].map((a) => o + a));
  }
  return out;
}
const normLocus = (a: string, b: string) => (a === a.toUpperCase() && b !== b.toUpperCase() ? a + b : b === b.toUpperCase() && a !== a.toUpperCase() ? b + a : a + b);

export function cross(p1: string, p2: string) {
  const g1 = gametes(p1), g2 = gametes(p2);
  if (g1[0].length !== g2[0].length) throw new Error('Los padres deben tener el mismo número de genes.');
  const cells = g1.map((a) => g2.map((b) => { let s = ''; for (let i = 0; i < a.length; i++) s += normLocus(a[i], b[i]); return s; }));
  const pheno = (g: string) => (g.match(/../g) ?? []).map((l) => (l[0] === l[0].toUpperCase() ? l[0] + '_' : l[0] + l[0])).join('');
  const counts: Record<string, number> = {};
  const gen: Record<string, number> = {};
  cells.flat().forEach((g) => { counts[pheno(g)] = (counts[pheno(g)] || 0) + 1; gen[g] = (gen[g] || 0) + 1; });
  return { g1, g2, cells, phenotypes: counts, genotypes: gen, total: g1.length * g2.length, pheno };
}

type PState = ReturnType<typeof cross> & { error?: string };
const S = (p: Params): PState => {
  try { return cross(String(p.p1).trim(), String(p.p2).trim()); } catch (e) { return { error: (e as Error).message } as PState; }
};

export const punnettSim: SimConfig<PState> = {
  id: 'bio.punnett',
  title: 'Genética: cuadro de Punnett',
  area: 'ciencias', subarea: 'biologia',
  competencia: 'explicacion_de_fenomenos',
  evidencias: ['CIE_E3.3', 'CIE_E4.4'],
  nivel: 2, tiempoMin: 8, mode: 'static',
  params: [
    { key: 'p1', label: 'Genotipo del padre (ej. Aa o AaBb)', type: 'text', default: 'Aa' },
    { key: 'p2', label: 'Genotipo de la madre', type: 'text', default: 'Aa' },
  ],
  logic: {
    init: (p) => S(p),
    measures: (traj): Record<string, number> => {
      const s = traj[0];
      if (s.error) return {};
      const dom = Object.entries(s.phenotypes).filter(([k]) => !/[a-z]/.test(k)).reduce((a, [, v]) => a + v, 0);
      const rec = Object.entries(s.phenotypes).filter(([k]) => !/_/.test(k)).reduce((a, [, v]) => a + v, 0);
      return { celdas: s.total, p_todo_dominante: dom / s.total, p_todo_recesivo: rec / s.total, num_fenotipos: Object.keys(s.phenotypes).length };
    },
  },
  measureLabels: { celdas: 'Celdas del cuadro', p_todo_dominante: 'P(fenotipo dominante en todos los genes)', p_todo_recesivo: 'P(fenotipo recesivo en todos los genes)', num_fenotipos: 'Fenotipos distintos' },
  challenges: [
    { id: 'ch1', prompt: 'Elige los genotipos de los padres (un gen, p. ej. Aa, AA, aa) para que exactamente la mitad de la descendencia sea recesiva.', checks: [{ measure: 'p_todo_recesivo', target: 0.5, tol: 0.001 }], hint: 'Un heterocigoto cruzado con un homocigoto recesivo.' },
  ],
  describe: (m) => `Probabilidad de fenotipo dominante: ${m.p_todo_dominante}, recesivo: ${m.p_todo_recesivo}`,
  render: {
    width: 700, height: 460,
    view({ ctx, w, h, state: s }) {
      ctx.fillStyle = BG; ctx.fillRect(0, 0, w, h);
      if (s.error) { label(ctx, s.error, 20, 40, 'left', 15, '#B91C1C'); return; }
      const n = s.g1.length, cell = Math.min(80, (w - 120) / n, (h - 140) / n), ox = 90, oy = 70;
      const keys = Object.keys(s.phenotypes);
      const col = (g: string) => COLORS[keys.indexOf(s.pheno(g)) % COLORS.length];
      s.g1.forEach((g, i) => label(ctx, g, ox + i * cell + cell / 2, oy - 10, 'center', 13));
      s.g2.forEach((g, j) => label(ctx, g, ox - 10, oy + j * cell + cell / 2 + 4, 'right', 13));
      s.cells.forEach((row, j) => row.forEach((g, i) => {
        ctx.fillStyle = col(g); ctx.globalAlpha = 0.25; ctx.fillRect(ox + i * cell, oy + j * cell, cell - 2, cell - 2); ctx.globalAlpha = 1;
        ctx.strokeStyle = INK; ctx.lineWidth = 1; ctx.strokeRect(ox + i * cell, oy + j * cell, cell - 2, cell - 2);
        label(ctx, g, ox + i * cell + cell / 2, oy + j * cell + cell / 2 + 4, 'center', n > 2 ? 11 : 15);
      }));
      keys.forEach((k, i) => { label(ctx, `${k}: ${s.phenotypes[k]}/${s.total}`, 20, h - 14 - (keys.length - 1 - i) * 18, 'left', 13, COLORS[i % COLORS.length]); });
    },
  },
};
