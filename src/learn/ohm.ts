import { gridFill, label, mono, hand, arrow, dim, COLORS, INK, MUT, PEN, BG } from '../render/plot';
import type { Extra } from '../core/types';
import { solveCircuit, type Circuit } from '../sims/ohm';
import { n, near } from './util';

type Rect = [number, number, number, number];
const inside = (rs: Rect[], x: number, y: number) => rs.some(([a, b, c, d]) => x > a && x < c && y > b && y < d);

function flow(ctx: CanvasRenderingContext2D, pts: [number, number][], cur: number, time: number, skip: Rect[], color: string) {
  const sp = Math.min(150, 14 + 26 * Math.sqrt(Math.abs(cur))), gap = 26;
  let acc = 0;
  for (let i = 0; i < pts.length - 1; i++) {
    const [x0, y0] = pts[i], [x1, y1] = pts[i + 1], len = Math.hypot(x1 - x0, y1 - y0);
    for (let s = (((time * sp - acc) % gap) + gap) % gap; s < len; s += gap) {
      const x = x0 + ((x1 - x0) * s) / len, y = y0 + ((y1 - y0) * s) / len;
      if (inside(skip, x, y)) continue;
      ctx.fillStyle = color; ctx.beginPath(); ctx.arc(x, y, 3.2, 0, 7); ctx.fill();
    }
    acc += len;
  }
}

function zig(ctx: CanvasRenderingContext2D, x: number, y: number, len: number, vert: boolean, color: string) {
  ctx.strokeStyle = color; ctx.lineWidth = 2.6; ctx.lineJoin = 'round'; ctx.beginPath();
  const k = 7, a = 9;
  for (let i = 0; i <= k; i++) {
    const u = -len / 2 + (len * i) / k, off = i === 0 || i === k ? 0 : i % 2 ? -a : a;
    const px = vert ? x + off : x + u, py = vert ? y + u : y + off;
    i ? ctx.lineTo(px, py) : ctx.moveTo(px, py);
  }
  ctx.stroke();
}

export const ohmExtra: Extra<Circuit> = {
  size: { width: 800, height: 350 },
  ambient: true,
  readouts: ['I_total', 'R_total', 'potencia'],
  paramHints: {
    V: 'Empuje que da la pila a las cargas. Más voltaje, más corriente.',
    R1: 'Resistencia por la que pasa TODA la corriente (está en serie).',
    R2: 'Primera rama del paralelo. Recibe el mismo voltaje que R3.',
    R3: 'Segunda rama del paralelo. Cambia R3 y mira cómo se reparte la corriente.',
  },
  learn: {
    resumen: 'Un circuito con una resistencia en serie y dos en paralelo. Los puntitos son la corriente: van más rápido cuando pasa más.',
    objetivos: [
      'Aplicar la ley de Ohm $V=IR$ a una resistencia o a todo el circuito.',
      'Calcular la resistencia equivalente en serie y en paralelo.',
      'Predecir cómo se reparten el voltaje y la corriente.',
    ],
    idea: [
      'La ley de Ohm dice que, en una resistencia, el voltaje y la corriente son proporcionales: $V=IR$. Una resistencia grande deja pasar poca corriente con el mismo voltaje.',
      'En **serie** (una tras otra) pasa la misma corriente por todas y los voltajes se suman. En **paralelo** (ramas lado a lado) todas reciben el mismo voltaje y las corrientes se suman. Por eso un paralelo siempre tiene menos resistencia que su rama más pequeña: le das más caminos a la corriente.',
    ],
    analogia: 'Piensa en agua en tuberías: el voltaje es la presión, la corriente es el caudal y la resistencia es lo angosto del tubo. Dos tubos en paralelo dejan pasar más agua que uno solo.',
    formulas: [
      { tex: 'V=I\\,R', nombre: 'Ley de Ohm', vars: [['V', 'voltaje (V)'], ['I', 'corriente (A)'], ['R', 'resistencia (Ω)']] },
      { tex: 'R_s=R_1+R_2', nombre: 'Resistencias en serie', vars: [['R_s', 'resistencia equivalente']] },
      { tex: '\\frac{1}{R_p}=\\frac{1}{R_2}+\\frac{1}{R_3}\\quad\\Rightarrow\\quad R_p=\\frac{R_2R_3}{R_2+R_3}', nombre: 'Resistencias en paralelo', vars: [['R_p', 'siempre menor que la menor de las ramas']] },
      { tex: 'P=V\\,I=I^2R=\\frac{V^2}{R}', nombre: 'Potencia eléctrica', vars: [['P', 'potencia (W)'], ['I^2R', 'calor en una resistencia']] },
      { tex: 'I=I_2+I_3', nombre: 'Nudo: lo que entra es lo que sale', vars: [['I', 'corriente total'], ['I_2,I_3', 'corrientes de cada rama']] },
    ],
    ejemplos: [
      { titulo: 'El circuito por defecto', texto: 'Fuente de $12$ V, $R_1=2\\,\\Omega$, $R_2=6\\,\\Omega$ y $R_3=3\\,\\Omega$. Halla la corriente en cada rama.', pasos: ['Paralelo: $R_p=\\frac{6\\cdot3}{6+3}=2\\,\\Omega$.', 'Total: $R_t=2+2=4\\,\\Omega$, así que $I=12/4=3$ A.', 'Voltaje en R1: $3\\cdot2=6$ V; queda $12-6=6$ V para el paralelo.', 'Ramas: $I_2=6/6=1$ A e $I_3=6/3=2$ A. Suman $3$ A. ✓'] },
      { titulo: 'Dos iguales en paralelo', texto: 'Dos resistencias de $10\\,\\Omega$ en paralelo, ¿cuánto valen juntas?', pasos: ['$R_p=\\frac{10\\cdot10}{10+10}=5\\,\\Omega$.', 'Regla rápida: $n$ resistencias iguales $R$ en paralelo equivalen a $R/n$.'] },
    ],
    errores: [
      { mito: '«La corriente se va gastando al pasar por las resistencias».', realidad: 'La corriente es la misma en serie. Lo que baja es el voltaje: la energía se convierte en calor.' },
      { mito: '«Más resistencias siempre aumentan la resistencia total».', realidad: 'En serie sí; en paralelo disminuye, porque abres más caminos.' },
      { mito: '«Por la resistencia más grande pasa más corriente».', realidad: 'En paralelo pasa menos: $I=V/R$. La corriente prefiere el camino fácil.' },
    ],
    saber11: 'Identifica primero qué está en serie y qué en paralelo, y reduce el circuito paso a paso. Si dos ramas están en paralelo, comparten voltaje: calcula la corriente de cada una con $I=V/R$ y verifica que sumen la total.',
  },
  presets: [
    { id: 'base', label: 'Circuito del ejemplo', desc: '$12$ V, $R_1=2$, $R_2=6$, $R_3=3$. Total $4\\,\\Omega$ y $3$ A: todo cuadra con números enteros.', params: { V: 12, R1: 2, R2: 6, R3: 3 } },
    { id: 'iguales', label: 'Ramas iguales', desc: 'Con $R_2=R_3=6$ la corriente se reparte por la mitad y el paralelo vale $3\\,\\Omega$.', params: { V: 12, R1: 2, R2: 6, R3: 6 } },
    { id: 'abierta', label: 'Una rama casi abierta', desc: 'Con $R_3=20\\,\\Omega$ casi toda la corriente se va por $R_2$.', params: { V: 12, R1: 2, R2: 2, R3: 20 } },
    { id: 'casi', label: 'Casi un cortocircuito', desc: 'Una rama de $0{,}5\\,\\Omega$ deja pasar una corriente enorme. Por eso los cables se calientan.', params: { V: 12, R1: 0.5, R2: 6, R3: 0.5 } },
  ],
  experiments: [
    { id: 'rp', titulo: 'Un camino más', setup: { V: 12, R1: 2, R2: 6, R3: 20 }, cambio: { R3: 3 },
      pregunta: 'Bajas $R_3$ de $20$ a $3\\,\\Omega$ (una rama más fácil). La resistencia total del circuito...',
      opciones: ['Aumenta', 'Disminuye', 'Queda igual'], correcta: 1,
      explicacion: 'Disminuye: pasa de 6,6 Ω a 4 Ω. En paralelo, abrir un camino más fácil siempre baja la resistencia equivalente.',
      check: (b, a) => a.R_total < b.R_total && near(a.R_total, 4, 0.01) },
    { id: 'v2', titulo: 'Doble voltaje', setup: { V: 6, R1: 2, R2: 6, R3: 3 }, cambio: { V: 12 },
      pregunta: 'Duplicas la fuente de $6$ a $12$ V. La corriente total se multiplica por 2. ¿Y la potencia total?',
      opciones: ['Se duplica', 'Se cuadruplica', 'Queda igual'], correcta: 1,
      explicacion: '$P=V^2/R$: con $R$ fija, duplicar $V$ cuadruplica $P$ (9 W → 36 W).',
      check: (b, a) => near(a.I_total / b.I_total, 2, 0.01) && near(a.potencia / b.potencia, 4, 0.01) },
    { id: 'div', titulo: 'Divisor de voltaje', setup: { V: 12, R1: 2, R2: 6, R3: 3 }, cambio: { R1: 6 },
      pregunta: 'Subes $R_1$ de $2$ a $6\\,\\Omega$. El voltaje que llega al paralelo ($R_2$ y $R_3$)...',
      opciones: ['Sube', 'Baja', 'Queda igual'], correcta: 1,
      explicacion: 'Baja de 6 V a 3 V. En serie el voltaje se reparte en proporción a las resistencias: R1 se queda con una parte mayor.',
      check: (b, a) => a.V_paralelo < b.V_paralelo && near(a.V_paralelo, 3, 0.01) },
    { id: 'igual', titulo: 'Dos ramas iguales', setup: { V: 12, R1: 2, R2: 6, R3: 3 }, cambio: { R3: 6 },
      pregunta: 'Cambias $R_3$ para que sea igual a $R_2=6\\,\\Omega$. El paralelo vale...',
      opciones: ['12 Ω', '6 Ω', '3 Ω'], correcta: 2,
      explicacion: 'Dos resistencias iguales en paralelo valen la mitad: $6/2=3\\,\\Omega$. Cada rama lleva la mitad de la corriente.',
      check: (b, a) => near(a.R_paralelo, 3, 0.01) && near(a.I_R2, a.I_R3, 1e-9) },
  ],
  solution: (p) => {
    const c = solveCircuit(+p.V, +p.R1, +p.R2, +p.R3);
    return [
      { t: 'Reduce el paralelo', tex: `R_p=\\frac{R_2R_3}{R_2+R_3}=\\frac{${n(c.R2)}\\cdot${n(c.R3)}}{${n(c.R2)}+${n(c.R3)}}=${n(c.Rp)}\;\\Omega`, nota: 'Sale menor que cualquiera de las dos ramas.' },
      { t: 'Suma lo que queda en serie', tex: `R_t=R_1+R_p=${n(c.R1)}+${n(c.Rp)}=${n(c.Rt)}\;\\Omega` },
      { t: 'Corriente total (Ohm)', tex: `I=\\frac{V}{R_t}=\\frac{${n(c.V)}}{${n(c.Rt)}}=${n(c.I)}\;\\text{A}` },
      { t: 'Reparte el voltaje', tex: `V_1=I\\,R_1=${n(c.V1)}\;\\text{V}\\qquad V_p=V-V_1=${n(c.Vp)}\;\\text{V}`, nota: 'Lo que no se queda R1 llega a las dos ramas, y a ambas por igual.' },
      { t: 'Corriente de cada rama', tex: `I_2=\\frac{V_p}{R_2}=${n(c.I2)}\;\\text{A}\\qquad I_3=\\frac{V_p}{R_3}=${n(c.I3)}\;\\text{A}`, nota: `Comprobación: $I_2+I_3=${n(c.I2 + c.I3)}$ A, igual que la corriente total.` },
      { t: 'Potencia entregada', tex: `P=V\\,I=${n(c.V)}\\cdot${n(c.I)}=${n(c.Ptot)}\;\\text{W}` },
    ];
  },
  compare: (p, m) => {
    const c = solveCircuit(+p.V, +p.R1, +p.R2, +p.R3);
    return [
      { label: 'R total (Ω)', teoria: c.Rt, sim: m.R_total },
      { label: 'Corriente total (A)', teoria: c.I, sim: m.I_total },
      { label: 'Potencia (W)', teoria: c.V * c.I, sim: m.potencia },
    ];
  },
  insight: (p) => {
    const c = solveCircuit(+p.V, +p.R1, +p.R2, +p.R3);
    const big = c.I2 > c.I3 ? 'R2' : c.I3 > c.I2 ? 'R3' : '';
    return big ? `La rama de **${big}** lleva más corriente porque tiene menos resistencia. Recibe el mismo voltaje que la otra (${n(c.Vp)} V).` : `Las dos ramas son iguales y llevan lo mismo: ${n(c.I2)} A cada una.`;
  },
  view({ ctx, w, h, state: c, time }) {
    gridFill(ctx, w, h, 20);
    const L = 80, T = 92, B = 282, X2 = 540, X3 = 670, my = (T + B) / 2;
    const r1: Rect = [190, T - 16, 310, T + 16], r2: Rect = [X2 - 16, my - 36, X2 + 16, my + 36], r3: Rect = [X3 - 16, my - 36, X3 + 16, my + 36], bat: Rect = [L - 20, my - 12, L + 20, my + 12];
    const skip = [r1, r2, r3, bat];
    // cables
    ctx.strokeStyle = INK; ctx.lineWidth = 2.4; ctx.lineCap = 'round';
    ctx.beginPath(); ctx.moveTo(L, my - 8); ctx.lineTo(L, T); ctx.lineTo(r1[0], T); ctx.moveTo(r1[2], T); ctx.lineTo(X3, T); ctx.moveTo(X2, T); ctx.lineTo(X2, r2[1]); ctx.moveTo(X2, r2[3]); ctx.lineTo(X2, B); ctx.moveTo(X3, T); ctx.lineTo(X3, r3[1]); ctx.moveTo(X3, r3[3]); ctx.lineTo(X3, B); ctx.moveTo(X3, B); ctx.lineTo(L, B); ctx.lineTo(L, my + 8); ctx.stroke();
    for (const [x, y] of [[X2, T], [X2, B]] as [number, number][]) { ctx.fillStyle = INK; ctx.beginPath(); ctx.arc(x, y, 4, 0, 7); ctx.fill(); }
    // pila
    ctx.lineWidth = 3; ctx.beginPath(); ctx.moveTo(L - 18, my - 7); ctx.lineTo(L + 18, my - 7); ctx.stroke(); ctx.lineWidth = 5; ctx.beginPath(); ctx.moveTo(L - 9, my + 7); ctx.lineTo(L + 9, my + 7); ctx.stroke();
    label(ctx, '+', L - 30, my - 3, 'center', 16, COLORS[4]); label(ctx, '−', L - 30, my + 17, 'center', 18, COLORS[0]);
    mono(ctx, `${n(c.V, 0)} V`, L + 28, my + 4, 'left', 14, PEN);
    // resistencias
    zig(ctx, 250, T, 120, false, COLORS[0]); zig(ctx, X2, my, 72, true, COLORS[1]); zig(ctx, X3, my, 72, true, COLORS[2]);
    // corriente
    const dc = PEN;
    flow(ctx, [[L, my - 8], [L, T], [X2, T]], c.I, time, skip, dc);
    flow(ctx, [[X2, T], [X3, T], [X3, B], [X2, B]], c.I3, time, skip, dc);
    flow(ctx, [[X2, T], [X2, B]], c.I2, time, skip, dc);
    flow(ctx, [[X2, B], [L, B], [L, my + 8]], c.I, time, skip, dc);
    // rótulos
    mono(ctx, `R₁ = ${n(c.R1, 1)} Ω`, 250, T - 28, 'center', 13, COLORS[0]);
    mono(ctx, `V₁ = ${n(c.V1, 2)} V`, 250, T + 34, 'center', 12, MUT);
    mono(ctx, `R₂ = ${n(c.R2, 1)} Ω`, X2 - 24, my - 6, 'right', 13, COLORS[1]);
    mono(ctx, `I₂ = ${n(c.I2, 2)} A`, X2 - 24, my + 12, 'right', 12, MUT);
    mono(ctx, `R₃ = ${n(c.R3, 1)} Ω`, X3 + 24, my - 6, 'left', 13, COLORS[2]);
    mono(ctx, `I₃ = ${n(c.I3, 2)} A`, X3 + 24, my + 12, 'left', 12, MUT);
    arrow(ctx, 330, T - 24, 380, T - 24, PEN, 2.4);
    mono(ctx, `I = ${n(c.I, 2)} A`, 392, T - 20, 'left', 14, PEN);
    dim(ctx, X2, B + 4, X3, B + 4, `mismo voltaje: ${n(c.Vp, 2)} V`, { off: 26, color: COLORS[3] });
    hand(ctx, 'serie: misma I', 250, B - 24, 'center', 18, PEN);
    hand(ctx, 'paralelo: mismo V', (X2 + X3) / 2, T - 34, 'center', 18, PEN);
    mono(ctx, `R_total = ${n(c.Rt, 2)} Ω   ·   P = ${n(c.Ptot, 1)} W`, w / 2, h - 12, 'center', 13, INK);
  },
};
