import { gridFill, label, mono, hand, COLORS, INK, MUT, PEN } from '../render/plot';
import type { Extra, Step } from '../core/types';
import type { BState } from '../sims/balance';
import { balance, parseFormula, parseEquation } from '../math/chem';

const SUB = '₀₁₂₃₄₅₆₇₈₉';
const sub = (f: string) => f.replace(/\d/g, (d) => SUB[+d]);
const ELCOL: Record<string, string> = { H: COLORS[0], C: COLORS[1], O: COLORS[4], N: COLORS[5], Fe: COLORS[3], Cl: COLORS[2], Na: COLORS[5], Mg: COLORS[2], Al: COLORS[3], Ca: COLORS[1], S: COLORS[1] };
const colOf = (el: string, i: number) => ELCOL[el] ?? COLORS[i % COLORS.length];
const L = 'abcdefgh';
const EQ0 = { sol: false };

export const balanceExtra: Extra<BState> = {
  size: { width: 760, height: 420 },
  readouts: ['balanceada', 'especies', 'suma_coef_solucion'],
  paramHints: {
    eq: 'Escribe la reacción con -> entre reactivos y productos. Los subíndices van como números: H2O, Ca(OH)2.',
    coefs: 'Un coeficiente por sustancia, en orden, separados por coma. Es el número que multiplica toda la molécula.',
    sol: 'Muestra la solución mínima, calculada con álgebra exacta (fracciones, sin redondeos).',
  },
  learn: {
    resumen: 'Los átomos no se crean ni se destruyen: los que entran son los que salen. Balancear es ajustar coeficientes hasta que cada elemento tenga el mismo número de átomos a ambos lados.',
    objetivos: [
      'Explicar por qué una ecuación química debe estar balanceada (conservación de la masa).',
      'Contar átomos con coeficientes y subíndices.',
      'Balancear ecuaciones sencillas por tanteo y con un sistema de ecuaciones.',
    ],
    idea: [
      'En una reacción los átomos se reordenan, pero no cambian de número. Por eso, a la izquierda y a la derecha de la flecha debe haber la misma cantidad de átomos de cada elemento.',
      'Para igualar los átomos solo puedes cambiar los **coeficientes** (el número grande delante de la fórmula). Nunca cambies los **subíndices**: $H_2O$ y $H_2O_2$ son sustancias distintas (agua y agua oxigenada). El coeficiente multiplica toda la fórmula: $3H_2O$ son 6 átomos de H y 3 de O.',
    ],
    analogia: 'Es como una receta: para hacer 2 bocadillos necesitas 4 panes y 2 lonchas. Cambiar el coeficiente es cambiar cuántos bocadillos haces; cambiar un subíndice sería cambiar el bocadillo por otra cosa.',
    formulas: [
      { tex: 'a\\,\\text{C}_3\\text{H}_8+b\\,\\text{O}_2\\to c\\,\\text{CO}_2+d\\,\\text{H}_2\\text{O}', nombre: 'Plantear con letras', vars: [['a,b,c,d', 'coeficientes por hallar']] },
      { tex: '\\text{C: }3a=c\\quad\\text{H: }8a=2d\\quad\\text{O: }2b=2c+d', nombre: 'Una ecuación por elemento', vars: [['átomos de la izquierda', '= átomos de la derecha']] },
      { tex: 'a=1\\Rightarrow c=3,\;d=4,\;b=5', nombre: 'Resolver dando a una letra el valor 1', vars: [['solución', 'C₃H₈ + 5 O₂ → 3 CO₂ + 4 H₂O']] },
    ],
    ejemplos: [
      { titulo: 'Agua', texto: 'Balancea $H_2+O_2\\to H_2O$.', pasos: ['Oxígeno: hay 2 a la izquierda y 1 a la derecha. Pones $2H_2O$: ahora 2 y 2.', 'Hidrógeno: a la derecha hay 4. Pones $2H_2$ a la izquierda.', 'Resultado: $2H_2+O_2\\to2H_2O$. Cuenta: 4 H y 2 O por cada lado. ✓'] },
      { titulo: 'Combustión del metano', texto: 'Balancea $CH_4+O_2\\to CO_2+H_2O$.', pasos: ['Carbono: 1 y 1, ya está.', 'Hidrógeno: 4 a la izquierda, así que $2H_2O$.', 'Oxígeno: a la derecha $2+2=4$, entonces $2O_2$.', 'Resultado: $CH_4+2O_2\\to CO_2+2H_2O$. ✓'] },
    ],
    errores: [
      { mito: '«Para balancear puedo cambiar el subíndice».', realidad: 'Cambiar un subíndice cambia la sustancia. Solo se ajustan coeficientes.' },
      { mito: '«Con $2H_2O$ hay 2 átomos de hidrógeno».', realidad: 'El coeficiente multiplica todo: $2H_2O$ tiene 4 átomos de H y 2 de O.' },
      { mito: '«Una ecuación balanceada tiene los mismos coeficientes en ambos lados».', realidad: 'Lo que debe coincidir es el número de átomos de cada elemento, no los coeficientes.' },
    ],
    saber11: 'Empieza por el elemento que aparece en menos sustancias y deja para el final el oxígeno o el hidrógeno si están en varias. Verifica siempre contando átomos. Si te piden la suma de coeficientes, usa los enteros más pequeños.',
  },
  presets: [
    { id: 'propano', label: 'Combustión del propano', desc: 'El gas de cocina: $C_3H_8+5O_2\\to3CO_2+4H_2O$. Prueba con coeficientes y mira cómo se cuadran los átomos.', params: { eq: 'C3H8 + O2 -> CO2 + H2O', coefs: '1,1,1,1', ...EQ0 } },
    { id: 'agua', label: 'Formación del agua', desc: '$2H_2+O_2\\to2H_2O$: el primer ejemplo que conviene dominar.', params: { eq: 'H2 + O2 -> H2O', coefs: '1,1,1', ...EQ0 } },
    { id: 'amoniaco', label: 'Amoníaco', desc: 'El proceso Haber: $N_2+3H_2\\to2NH_3$. Base de los fertilizantes.', params: { eq: 'N2 + H2 -> NH3', coefs: '1,1,1', ...EQ0 } },
    { id: 'oxido', label: 'Oxidación del hierro', desc: 'La herrumbre: $4Fe+3O_2\\to2Fe_2O_3$.', params: { eq: 'Fe + O2 -> Fe2O3', coefs: '1,1,1', ...EQ0 } },
    { id: 'glucosa', label: 'Respiración celular', desc: 'La glucosa se oxida: $C_6H_{12}O_6+6O_2\\to6CO_2+6H_2O$.', params: { eq: 'C6H12O6 + O2 -> CO2 + H2O', coefs: '1,1,1,1', ...EQ0 } },
    { id: 'acido', label: 'Ácido con un metal', desc: 'Con paréntesis: $Al+HCl\\to AlCl_3+H_2$ se balancea como $2Al+6HCl\\to2AlCl_3+3H_2$.', params: { eq: 'Al + HCl -> AlCl3 + H2', coefs: '1,1,1,1', ...EQ0 } },
  ],
  experiments: [
    { id: 'agua', titulo: '¿Está balanceada?', setup: { eq: 'H2 + O2 -> H2O', coefs: '1,1,1', ...EQ0 }, cambio: { coefs: '2,1,2' },
      pregunta: 'Pones coeficientes 2, 1 y 2 en $H_2+O_2\\to H_2O$. ¿Queda balanceada?',
      opciones: ['Sí: 4 H y 2 O por lado', 'No: sobra oxígeno', 'No: faltan hidrógenos'], correcta: 0,
      explicacion: '$2H_2$ tiene 4 H, $O_2$ tiene 2 O, y $2H_2O$ tiene 4 H y 2 O. Todo coincide.',
      check: (b, a) => b.balanceada === 0 && a.balanceada === 1 },
    { id: 'doble', titulo: 'Multiplicar todo', setup: { eq: 'H2 + O2 -> H2O', coefs: '2,1,2', ...EQ0 }, cambio: { coefs: '4,2,4' },
      pregunta: 'Duplicas todos los coeficientes de una ecuación balanceada ($4,2,4$). ¿Sigue balanceada?',
      opciones: ['Sí, pero ya no son los mínimos', 'No, hay que volver a balancear', 'Solo si cambias los subíndices'], correcta: 0,
      explicacion: 'Multiplicar todo por el mismo número mantiene la igualdad. Por convención se usan los enteros más pequeños ($2,1,2$).',
      check: (b, a) => b.balanceada === 1 && a.balanceada === 1 },
    { id: 'propano', titulo: 'Casi, casi', setup: { eq: 'C3H8 + O2 -> CO2 + H2O', coefs: '1,5,3,4', ...EQ0 }, cambio: { coefs: '1,5,3,3' },
      pregunta: 'Con $1,5,3,4$ el propano está balanceado. Si cambias el agua a $3H_2O$, ¿qué elemento se descuadra?',
      opciones: ['El carbono', 'El hidrógeno y el oxígeno', 'Ninguno'], correcta: 1,
      explicacion: 'Con $3H_2O$ quedan 6 H (de 8) y el O sería $6+3=9$ en vez de 10. El carbono sigue en 3 y 3.',
      check: (b, a) => b.balanceada === 1 && a.balanceada === 0 },
    { id: 'ruido', titulo: 'Más de una solución', setup: { eq: 'C3H8 + O2 -> CO2 + H2O', coefs: '1,5,3,4', ...EQ0 }, cambio: { coefs: '2,10,6,8' },
      pregunta: 'Cambias $1,5,3,4$ por $2,10,6,8$. ¿Qué pasa?',
      opciones: ['Sigue balanceada', 'Se descuadra', 'Cambia el producto'], correcta: 0,
      explicacion: 'Es el doble de cada coeficiente. Los átomos siguen coincidiendo, así que es otra forma válida de escribir la misma reacción.',
      check: (b, a) => b.balanceada === 1 && a.balanceada === 1 },
  ],
  solution: (p) => {
    const eq = String(p.eq);
    try {
      const pe = parseEquation(eq), sp = [...pe.left, ...pe.right], cols = sp.map(parseFormula), nl = pe.left.length;
      const els = [...new Set(cols.flatMap((c) => Object.keys(c)))];
      const letters = sp.map((_, i) => L[i]);
      const side = (el: string, from: number, to: number) => { const t: string[] = []; for (let j = from; j < to; j++) { const k = cols[j][el]; if (k) t.push(`${k > 1 ? k : ''}${letters[j]}`); } return t.join('+') || '0'; };
      const sol = balance(eq);
      const steps: Step[] = [
        { t: 'Ponle una letra a cada coeficiente', tex: sp.map((f, i) => `${letters[i]}\\,\\text{${sub(f)}}`).join('\\;\\;') },
        { t: 'Una ecuación por elemento (átomos izq. = átomos der.)', tex: els.map((el) => `\\text{${el}: }${side(el, 0, nl)}=${side(el, nl, sp.length)}`).join('\\quad ') },
      ];
      if (!sol.ok) return [...steps, { t: 'Resultado', tex: `\\text{${sol.message}}` }];
      steps.push({ t: 'Da el valor 1 a una letra y resuelve', tex: `\\text{Coeficientes enteros mínimos: }${sol.coefs!.map((c, i) => `${letters[i]}=${c}`).join(',\;')}`, nota: 'Si salen fracciones, se multiplica todo por el mínimo común múltiplo de los denominadores.' });
      steps.push({ t: 'Ecuación balanceada', tex: sp.map((f, i) => `${sol.coefs![i] > 1 ? sol.coefs![i] : ''}\\text{${sub(f)}}`).reduce((acc, t, i) => acc + (i === 0 ? '' : i === nl ? '\;\\to\;' : '\;+\;') + t, '') });
      return steps;
    } catch { return [{ t: 'Revisa la ecuación', tex: '\\text{Usa una flecha ->, y formulas como H2O o Ca(OH)2}' }]; }
  },
  insight: (_p, m) => (m.balanceada ? '¡Balanceada! Cada elemento tiene los mismos átomos a ambos lados.' : 'Mira las filas con ≠: ahí faltan o sobran átomos. Ajusta el coeficiente de una sustancia que contenga ese elemento.'),
  view({ ctx, w, h, state: s }) {
    gridFill(ctx, w, h, 20);
    if (s.error) { label(ctx, `Revisa la ecuación: ${s.error}`, 20, 44, 'left', 15, COLORS[4]); return; }
    // ecuación grande
    let x = 24; const y = 44;
    ctx.textBaseline = 'alphabetic';
    s.species.forEach((sp, i) => {
      const c = s.coefs[i], t = sub(sp);
      if (i === s.nl) { hand(ctx, '→', x + 10, y + 2, 'center', 30, PEN); x += 38; }
      else if (i > 0) { label(ctx, '+', x + 8, y, 'center', 20, MUT); x += 26; }
      if (c !== 1) { mono(ctx, String(c), x, y, 'left', 22, PEN); x += 12 + String(c).length * 11; }
      label(ctx, t, x, y, 'left', 21, INK); x += t.length * 12.4 + 4;
    });
    const els = s.elements, rowH = Math.min(50, (h - 150) / Math.max(1, els.length));
    const lx = 90, rx = 440, cap = 22, d = 14;
    label(ctx, 'Átomos a la izquierda', lx, 92, 'left', 12, MUT); label(ctx, 'Átomos a la derecha', rx, 92, 'left', 12, MUT);
    els.forEach((el, i) => {
      const yy = 118 + i * rowH, l = s.left[el] || 0, r = s.right[el] || 0, ok = l === r, col = colOf(el, i);
      ctx.fillStyle = col; ctx.strokeStyle = INK; ctx.lineWidth = 1.5; ctx.beginPath(); ctx.arc(46, yy + 6, 17, 0, 7); ctx.fill(); ctx.stroke();
      ctx.fillStyle = BGc; label(ctx, el, 46, yy + 11, 'center', 14, '#121821');
      const dots = (cnt: number, x0: number) => { for (let k = 0; k < Math.min(cnt, cap * 2); k++) { const cx = x0 + (k % cap) * d, cy = yy + Math.floor(k / cap) * d; ctx.fillStyle = col; ctx.beginPath(); ctx.arc(cx, cy, 5, 0, 7); ctx.fill(); } if (cnt > cap * 2) mono(ctx, `+${cnt - cap * 2}`, x0 + cap * d, yy + 4, 'left', 11, MUT); };
      dots(l, lx); dots(r, rx);
      mono(ctx, String(l), rx - 28, yy + 5, 'right', 16, INK); mono(ctx, String(r), w - 20, yy + 5, 'right', 16, INK);
      hand(ctx, ok ? '=' : '≠', rx - 12, yy + 10, 'center', 28, ok ? COLORS[2] : COLORS[4]);
    });
    hand(ctx, s.balanced ? '¡Balanceada!' : 'Aún no está balanceada', w / 2, h - 14, 'center', 26, s.balanced ? COLORS[2] : COLORS[4]);
  },
};
const BGc = '#121821';
