import { gridFill, label, mono, hand, COLORS, INK, MUT, PEN } from '../render/plot';
import type { Extra } from '../core/types';
import { cross } from '../sims/punnett';
import { n as num } from './util';

type PState = ReturnType<typeof cross> & { error?: string };
const gcd = (a: number, b: number): number => (b ? gcd(b, a % b) : a);
const ratio = (vals: number[]) => { const g = vals.reduce((a, v) => gcd(a, v), 0) || 1; return vals.map((v) => v / g).join(' : '); };
const frac = (k: number, t: number) => { const g = gcd(k, t) || 1; return k === 0 ? '0' : `${k / g}/${t / g}`; };

export const punnettExtra: Extra<PState> = {
  size: { width: 760, height: 440 },
  readouts: ['p_todo_dominante', 'p_todo_recesivo', 'celdas'],
  paramHints: {
    p1: 'Genotipo del padre. Una letra mayúscula es el alelo dominante y la minúscula el recesivo (Aa, AA, aa). Con dos genes: AaBb.',
    p2: 'Genotipo de la madre, con el mismo formato.',
  },
  learn: {
    resumen: 'Cada padre entrega un alelo por gen. El cuadro de Punnett muestra todas las combinaciones posibles y con qué probabilidad aparece cada una.',
    objetivos: [
      'Obtener los gametos de un genotipo.',
      'Construir el cuadro de Punnett y leer genotipos y fenotipos.',
      'Calcular proporciones y probabilidades de la descendencia.',
    ],
    idea: [
      'Cada gen tiene dos **alelos**, uno heredado de cada padre. Un individuo $AA$ o $aa$ es **homocigoto**; uno $Aa$ es **heterocigoto**. El alelo **dominante** ($A$) se nota en el fenotipo aunque haya solo una copia; el **recesivo** ($a$) solo se nota si hay dos copias.',
      'Al formar gametos, los dos alelos de un padre se separan: un $Aa$ produce la mitad de gametos $A$ y la mitad $a$. Cada casilla del cuadro es la unión de un gameto del padre con uno de la madre; todas son igual de probables.',
    ],
    analogia: 'Es como lanzar dos monedas: cada padre «lanza» una de sus dos monedas (alelos) y el resultado combina ambas. Las cuatro casillas son los cuatro resultados posibles.',
    formulas: [
      { tex: 'P(\\text{casilla})=\\frac{1}{\\text{número de casillas}}', nombre: 'Cada casilla es igualmente probable', vars: [['2\\times2', '4 casillas → 1/4 cada una'], ['4\\times4', '16 casillas → 1/16 cada una']] },
      { tex: 'Aa\\times Aa\\Rightarrow AA:Aa:aa=1:2:1\\qquad \\text{fenotipos }3:1', nombre: 'Monohíbrido clásico (Mendel)', vars: [['3/4', 'fenotipo dominante'], ['1/4', 'fenotipo recesivo']] },
      { tex: 'AaBb\\times AaBb\\Rightarrow 9:3:3:1', nombre: 'Dihíbrido (dos genes independientes)', vars: [['9/16', 'ambos dominantes'], ['1/16', 'ambos recesivos']] },
    ],
    ejemplos: [
      { titulo: 'Dos heterocigotos', texto: 'Dos padres $Aa$. ¿Qué probabilidad hay de un hijo con fenotipo recesivo?', pasos: ['Gametos: padre $A,a$; madre $A,a$.', 'Casillas: $AA$, $Aa$, $Aa$, $aa$.', 'Solo $aa$ es recesivo: $1/4$. El fenotipo dominante es $3/4$.'] },
      { titulo: 'Cruce de prueba', texto: '¿Cómo saber si un individuo dominante es $AA$ o $Aa$? Se cruza con $aa$.', pasos: ['Si es $AA$: toda la descendencia es $Aa$ (dominante).', 'Si es $Aa$: la mitad es $Aa$ y la mitad $aa$ (recesiva).', 'Si aparece cualquier hijo recesivo, el individuo era heterocigoto.'] },
    ],
    errores: [
      { mito: '«Si el alelo es dominante, aparece en 3 de cada 4 hijos siempre».', realidad: 'Son probabilidades, no reparto exacto: una familia de 4 hijos puede tener cualquier combinación.' },
      { mito: '«Dominante significa más común».', realidad: 'Dominante solo dice cómo se expresa. Un alelo dominante puede ser muy raro en la población.' },
      { mito: '«Aa y AA se ven distintos si A es dominante».', realidad: 'Tienen el mismo fenotipo; solo el genotipo es diferente.' },
    ],
    saber11: 'Escribe los gametos antes de hacer el cuadro. Distingue **genotipo** (letras: AA, Aa) de **fenotipo** (lo que se observa). Para probabilidades usa fracciones simples; si te piden dos hijos sucesivos, multiplica las probabilidades.',
  },
  presets: [
    { id: 'mendel', label: 'Mendel: Aa × Aa', desc: 'Dos heterocigotos. Genotipos 1:2:1 y fenotipos 3 dominantes por 1 recesivo.', params: { p1: 'Aa', p2: 'Aa' } },
    { id: 'prueba', label: 'Cruce de prueba: Aa × aa', desc: 'Mitad dominantes, mitad recesivos. Se usa para descubrir si un individuo es heterocigoto.', params: { p1: 'Aa', p2: 'aa' } },
    { id: 'homo', label: 'Homocigotos: AA × aa', desc: 'Todos los hijos son $Aa$ y se ven dominantes.', params: { p1: 'AA', p2: 'aa' } },
    { id: 'di', label: 'Dihíbrido: AaBb × AaBb', desc: '16 casillas y cuatro fenotipos en proporción 9:3:3:1.', params: { p1: 'AaBb', p2: 'AaBb' } },
    { id: 'dom', label: 'Uno puro dominante: AA × Aa', desc: 'Todos los hijos se ven dominantes, aunque la mitad son heterocigotos.', params: { p1: 'AA', p2: 'Aa' } },
  ],
  experiments: [
    { id: 'prueba', titulo: 'Cruce de prueba', setup: { p1: 'Aa', p2: 'Aa' }, cambio: { p2: 'aa' },
      pregunta: 'Cambias la madre de $Aa$ a $aa$ (padre $Aa$). ¿Qué fracción de la descendencia es recesiva?',
      opciones: ['1/4', '1/2', '3/4'], correcta: 1,
      explicacion: 'Gametos del padre $A,a$ y de la madre $a,a$: dos casillas $Aa$ y dos $aa$. Recesivos: 2/4 = 1/2.',
      check: (b, a) => b.p_todo_recesivo === 0.25 && a.p_todo_recesivo === 0.5 },
    { id: 'homo', titulo: 'Padres puros', setup: { p1: 'AA', p2: 'aa' }, cambio: { p2: 'aa' },
      pregunta: 'Cruzas $AA\\times aa$. ¿Qué fenotipo tienen todos los hijos?',
      opciones: ['Dominante', 'Recesivo', 'Mitad y mitad'], correcta: 0,
      explicacion: 'Todos son $Aa$ y el alelo dominante se expresa: fenotipo dominante en el 100 %.',
      check: (_b, a) => a.p_todo_dominante === 1 && a.p_todo_recesivo === 0 },
    { id: 'mendel', titulo: 'La razón 3:1', setup: { p1: 'AA', p2: 'Aa' }, cambio: { p1: 'Aa' },
      pregunta: 'Pasas de $AA\\times Aa$ a $Aa\\times Aa$. La fracción de hijos con fenotipo dominante baja a...',
      opciones: ['1/2', '3/4', '1/4'], correcta: 1,
      explicacion: 'Con $Aa\\times Aa$ solo el $aa$ (1 de 4) es recesivo, así que el 3/4 es dominante.',
      check: (b, a) => b.p_todo_dominante === 1 && a.p_todo_dominante === 0.75 },
    { id: 'di', titulo: 'Dos genes a la vez', setup: { p1: 'Aa', p2: 'Aa' }, cambio: { p1: 'AaBb', p2: 'AaBb' },
      pregunta: 'En $AaBb\\times AaBb$, ¿qué fracción de los hijos es recesiva en los dos genes ($aabb$)?',
      opciones: ['1/4', '1/8', '1/16'], correcta: 2,
      explicacion: 'Son independientes: $\\frac14\\cdot\\frac14=\\frac1{16}$. El cuadro tiene 16 casillas y solo una es $aabb$.',
      check: (b, a) => a.celdas === 16 && a.p_todo_recesivo === 1 / 16 && b.celdas === 4 },
  ],
  solution: (p) => {
    try {
      const c = cross(String(p.p1).trim(), String(p.p2).trim());
      const gen = Object.entries(c.genotypes), ph = Object.entries(c.phenotypes);
      return [
        { t: 'Gametos del padre', tex: `${String(p.p1)}\\to\\{${c.g1.join(',\\,')}\\}`, nota: 'Cada gameto lleva un alelo de cada gen.' },
        { t: 'Gametos de la madre', tex: `${String(p.p2)}\\to\\{${c.g2.join(',\\,')}\\}` },
        { t: 'Casillas del cuadro', tex: `${c.g1.length}\\times${c.g2.length}=${c.total}\;\\text{casillas, cada una de probabilidad }\\frac{1}{${c.total}}` },
        { t: 'Genotipos', tex: gen.map(([g, k]) => `${g}:\\,${frac(k, c.total)}`).join('\\quad '), nota: `Proporción: ${ratio(gen.map(([, k]) => k))}.` },
        { t: 'Fenotipos', tex: ph.map(([f, k]) => `${f.replace(/_/g, '\\_')}:\\,${frac(k, c.total)}`).join('\\quad '), nota: `Proporción fenotípica: ${ratio(ph.map(([, k]) => k))}. «_» significa que el segundo alelo puede ser cualquiera.` },
      ];
    } catch (e) { return [{ t: 'Revisa los genotipos', tex: `\\text{${(e as Error).message.replace(/[{}\\]/g, '')}}` }]; }
  },
  insight: (_p, m) => (m.celdas ? `Hay ${num(m.celdas, 0)} casillas. Fenotipo dominante en todos los genes: ${frac(Math.round(m.p_todo_dominante * m.celdas), m.celdas)}; recesivo en todos: ${frac(Math.round(m.p_todo_recesivo * m.celdas), m.celdas)}.` : 'Escribe genotipos como Aa o AaBb.'),
  view({ ctx, w, h, state: s }) {
    gridFill(ctx, w, h, 20);
    if (s.error) { label(ctx, s.error, 20, 44, 'left', 15, COLORS[4]); return; }
    const k = s.g1.length, cell = Math.min(82, (h - 150) / k, 320 / k), ox = 130, oy = 120;
    const keys = Object.keys(s.phenotypes), col = (g: string) => COLORS[keys.indexOf(s.pheno(g)) % COLORS.length];
    hand(ctx, 'gametos del padre', ox + (k * cell) / 2, oy - 52, 'center', 20, MUT);
    hand(ctx, 'gametos', 16, oy + (k * cell) / 2 - 6, 'left', 18, MUT); hand(ctx, 'de la madre', 16, oy + (k * cell) / 2 + 14, 'left', 18, MUT);
    s.g1.forEach((g, i) => { const x = ox + i * cell + cell / 2; ctx.strokeStyle = INK; ctx.lineWidth = 1.6; ctx.beginPath(); ctx.arc(x, oy - 22, 13 + (g.length > 2 ? 8 : 0), 0, 7); ctx.stroke(); mono(ctx, g, x, oy - 18, 'center', 13, INK); });
    s.g2.forEach((g, j) => { const y = oy + j * cell + cell / 2; ctx.strokeStyle = INK; ctx.lineWidth = 1.6; ctx.beginPath(); ctx.arc(ox - 24, y, 13 + (g.length > 2 ? 8 : 0), 0, 7); ctx.stroke(); mono(ctx, g, ox - 24, y + 4, 'center', 13, INK); });
    s.cells.forEach((row, j) => row.forEach((g, i) => {
      const x = ox + i * cell, y = oy + j * cell, c = col(g);
      ctx.fillStyle = c; ctx.globalAlpha = 0.28; ctx.fillRect(x + 1, y + 1, cell - 2, cell - 2); ctx.globalAlpha = 1;
      ctx.strokeStyle = INK; ctx.lineWidth = 1.3; ctx.strokeRect(x + 1, y + 1, cell - 2, cell - 2);
      mono(ctx, g, x + cell / 2, y + cell / 2 + 5, 'center', k > 2 ? 12 : 17, INK);
    }));
    const px = Math.max(ox + k * cell + 40, 470);
    label(ctx, 'Genotipos', px, 94, 'left', 13, MUT);
    Object.entries(s.genotypes).slice(0, 9).forEach(([g, c], i) => { const y = 114 + i * 20; mono(ctx, g, px, y, 'left', 12, INK); ctx.fillStyle = 'rgba(92,225,255,.5)'; ctx.fillRect(px + 70, y - 11, (c / s.total) * 150, 12); mono(ctx, `${c}/${s.total}`, px + 76 + (c / s.total) * 150, y, 'left', 11, MUT); });
    const y2 = 114 + Math.min(9, Object.keys(s.genotypes).length) * 20 + 22;
    label(ctx, 'Fenotipos', px, y2, 'left', 13, MUT);
    keys.forEach((f, i) => { const y = y2 + 22 + i * 20; ctx.fillStyle = COLORS[i % COLORS.length]; ctx.fillRect(px, y - 11, 12, 12); mono(ctx, `${f.replace(/_/g, '·')}  ${frac(s.phenotypes[f], s.total)}`, px + 20, y, 'left', 12, INK); });
    hand(ctx, `razón ${ratio(Object.values(s.phenotypes))}`, w - 16, h - 14, 'right', 24, PEN);
  },
};
