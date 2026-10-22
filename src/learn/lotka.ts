import { gridFill, niceStep, label, mono, hand, arrow, COLORS, INK, MUT, PEN } from '../render/plot';
import type { Extra } from '../core/types';
import type { LVState } from '../sims/lotka';
import { n, near } from './util';

const DEF = { alpha: 1, beta: 0.1, delta: 0.02, gamma: 0.5 };

export const lotkaExtra: Extra<LVState> = {
  size: { width: 800, height: 420 },
  readouts: ['amplitud_presas', 'eq_presas', 'eq_depredadores'],
  paramHints: {
    alpha: 'Qué tan rápido se reproducen las presas cuando no hay depredadores.',
    beta: 'Qué tan eficaces son los depredadores cazando presas.',
    delta: 'Cuántos depredadores nuevos nacen por cada presa comida.',
    gamma: 'Qué tan rápido mueren los depredadores sin comida.',
    x0: 'Presas con las que empieza la simulación.',
    y0: 'Depredadores con los que empieza.',
  },
  learn: {
    resumen: 'Conejos y zorros. Cuando hay muchos conejos, los zorros prosperan; cuando hay muchos zorros, los conejos caen; y entonces los zorros pasan hambre. El ciclo se repite.',
    objetivos: [
      'Explicar el ciclo depredador–presa con sus retrasos.',
      'Leer el plano de fases y las gráficas en el tiempo.',
      'Calcular el punto de equilibrio y predecir cómo cambia.',
    ],
    idea: [
      'Las presas crecen solas (a tasa $\\alpha$) y las comen los depredadores (a tasa $\\beta$ por encuentro). Los depredadores mueren (a tasa $\\gamma$) y nacen más si comen presas (a tasa $\\delta$). Esas cuatro reglas producen oscilaciones: **las presas suben primero, los depredadores las siguen con retraso**.',
      'El **plano de fases** dibuja una población contra la otra: cada ciclo es una curva cerrada que gira. En el centro hay un punto de **equilibrio**, donde ambas poblaciones permanecen constantes: $x^*=\\gamma/\\delta$ y $y^*=\\alpha/\\beta$.',
    ],
    analogia: 'Es como una persecución en círculos: nunca se alcanzan del todo. Cuando los depredadores abundan, las presas escasean y los depredadores se quedan sin comida, lo que da una nueva oportunidad a las presas.',
    formulas: [
      { tex: '\\frac{dx}{dt}=\\alpha x-\\beta xy', nombre: 'Presas', vars: [['x', 'número de presas'], ['\\alpha x', 'crecimiento natural'], ['\\beta xy', 'presas cazadas (encuentros)']] },
      { tex: '\\frac{dy}{dt}=\\delta xy-\\gamma y', nombre: 'Depredadores', vars: [['y', 'número de depredadores'], ['\\delta xy', 'nacimientos por alimento'], ['\\gamma y', 'muertes']] },
      { tex: 'x^*=\\frac{\\gamma}{\\delta}\\qquad y^*=\\frac{\\alpha}{\\beta}', nombre: 'Equilibrio (ambas derivadas = 0)', vars: [['x^*', 'presas en equilibrio'], ['y^*', 'depredadores en equilibrio']] },
      { tex: 'T\\approx\\frac{2\\pi}{\\sqrt{\\alpha\\gamma}}', nombre: 'Periodo de oscilaciones pequeñas', vars: [['T', 'tiempo de un ciclo completo']] },
    ],
    ejemplos: [
      { titulo: 'El punto de equilibrio', texto: 'Con $\\alpha=1$, $\\beta=0{,}1$, $\\delta=0{,}02$ y $\\gamma=0{,}5$, ¿dónde se detiene el ciclo?', pasos: ['Presas: $x^*=\\gamma/\\delta=0{,}5/0{,}02=25$.', 'Depredadores: $y^*=\\alpha/\\beta=1/0{,}1=10$.', 'Si empiezas en 25 y 10, no cambia nada. Cualquier otro punto da un ciclo alrededor.'] },
      { titulo: 'Un resultado sorprendente', texto: '¿Qué pasa con las presas en equilibrio si los depredadores mueren más rápido ($\\gamma$ sube)?', pasos: ['$x^*=\\gamma/\\delta$ crece con $\\gamma$.', 'Aumenta el nivel de presas en equilibrio. La razón: con menos depredadores sobreviviendo, las presas necesitan ser más abundantes para sostenerlos.'] },
    ],
    errores: [
      { mito: '«Más presas siempre es mejor para los depredadores».', realidad: 'Hay un retraso: el exceso de depredadores acaba con las presas y luego los propios depredadores caen.' },
      { mito: '«Si aumentas la mortalidad de depredadores, las presas se estabilizan en un valor menor».', realidad: 'En este modelo el equilibrio de presas sube con $\\gamma$.' },
      { mito: '«El ciclo se amortigua hasta detenerse».', realidad: 'En este modelo ideal el ciclo se repite siempre igual. En la naturaleza hay límites de recursos que lo amortiguan.' },
    ],
    saber11: 'Lee las gráficas en el tiempo: el pico de depredadores va después del pico de presas. Si una pregunta cambia solo una condición, identifica qué población se ve afectada primero y cuál la sigue.',
  },
  presets: [
    { id: 'ciclo', label: 'Ciclo clásico', desc: 'Parte con 40 presas y 9 depredadores y oscila en un ciclo grande.', params: { ...DEF, x0: 40, y0: 9 } },
    { id: 'eq', label: 'En equilibrio', desc: 'Empieza justo en $(25,10)$: no hay cambios. Es el centro del ciclo.', params: { ...DEF, x0: 25, y0: 10 } },
    { id: 'plaga', label: 'Plaga de depredadores', desc: 'Pocas presas y muchos depredadores: las presas se desploman, luego caen los depredadores.', params: { ...DEF, x0: 15, y0: 25 } },
    { id: 'rapido', label: 'Presas que se multiplican', desc: 'Con $\\alpha=2$ el ciclo es más rápido y el equilibrio de depredadores sube a 20.', params: { alpha: 2, beta: 0.1, delta: 0.02, gamma: 0.5, x0: 25, y0: 20 } },
  ],
  experiments: [
    { id: 'eq', titulo: 'Empezar en el equilibrio', setup: { ...DEF, x0: 40, y0: 9 }, cambio: { x0: 25, y0: 10 },
      pregunta: 'Empiezas con 25 presas y 10 depredadores (los valores de equilibrio). Las poblaciones...',
      opciones: ['Oscilan con fuerza', 'Se quedan constantes', 'Se extinguen'], correcta: 1,
      explicacion: 'En $(x^*,y^*)$ ambas derivadas valen cero: las presas que nacen son justo las que comen los depredadores, y los depredadores que nacen son los que mueren.',
      check: (b, a) => b.amplitud_presas > 10 && a.amplitud_presas < 0.5 },
    { id: 'gamma', titulo: 'Depredadores que mueren más rápido', setup: { ...DEF, x0: 40, y0: 9 }, cambio: { gamma: 1 },
      pregunta: 'Doblas la mortalidad de los depredadores (γ de 0,5 a 1). El nivel de equilibrio de presas...',
      opciones: ['Baja a la mitad', 'Sube al doble', 'No cambia'], correcta: 1,
      explicacion: '$x^*=\\gamma/\\delta$ pasa de 25 a 50. Parece contradictorio, pero con depredadores muriendo más rápido, el equilibrio requiere más presas para sostenerlos.',
      check: (b, a) => near(b.eq_presas, 25, 1e-9) && near(a.eq_presas, 50, 1e-9) },
    { id: 'alpha', titulo: 'Presas que se reproducen más rápido', setup: { ...DEF, x0: 40, y0: 9 }, cambio: { alpha: 2 },
      pregunta: 'Duplicas el crecimiento de las presas (α de 1 a 2). El equilibrio de DEPREDADORES...',
      opciones: ['Sube al doble', 'Baja a la mitad', 'No cambia'], correcta: 0,
      explicacion: '$y^*=\\alpha/\\beta$ pasa de 10 a 20. Más presas disponibles sostienen más depredadores.',
      check: (b, a) => near(b.eq_depredadores, 10, 1e-9) && near(a.eq_depredadores, 20, 1e-9) },
    { id: 'ciclo', titulo: '¿Se amortigua?', setup: { ...DEF, x0: 40, y0: 9 }, cambio: { x0: 30 },
      pregunta: 'En este modelo (sin límites de recursos), una vez empezado el ciclo, ¿qué pasa con la oscilación?',
      opciones: ['Se amortigua hasta un punto fijo', 'Se repite siempre igual', 'Crece sin parar'], correcta: 1,
      explicacion: 'El modelo conserva una cantidad $V$ constante, por eso las órbitas son cerradas. (En la realidad otros factores amortiguan el ciclo.)',
      check: (_b, a) => a.deriva_invariante < 0.01 },
  ],
  solution: (p) => {
    const al = +p.alpha, be = +p.beta, de = +p.delta, ga = +p.gamma, xs = ga / de, ys = al / be, T = (2 * Math.PI) / Math.sqrt(al * ga);
    return [
      { t: 'Escribe las dos ecuaciones', tex: `\\dot x=${n(al)}x-${n(be, 3)}xy\\qquad \\dot y=${n(de, 3)}xy-${n(ga)}y` },
      { t: 'Busca el equilibrio: derivadas = 0', tex: `x(\\alpha-\\beta y)=0\;\\Rightarrow\;y^*=\\frac{\\alpha}{\\beta}=${n(ys)}\\qquad y(\\delta x-\\gamma)=0\;\\Rightarrow\;x^*=\\frac{\\gamma}{\\delta}=${n(xs)}`, nota: 'Son las líneas punteadas del plano de fases.' },
      { t: 'Interpreta', tex: `\\text{Si }x=${n(xs)}\\text{ y }y=${n(ys)}\\text{, nada cambia.}`, nota: `Con ${n(+p.x0, 0)} presas y ${n(+p.y0, 0)} depredadores, el sistema ${near(+p.x0, xs, 0.6) && near(+p.y0, ys, 0.3) ? 'está casi en equilibrio.' : 'gira alrededor de ese punto.'}` },
      { t: 'Duración aproximada de un ciclo', tex: `T\\approx\\frac{2\\pi}{\\sqrt{\\alpha\\gamma}}=\\frac{2\\pi}{\\sqrt{${n(al)}\\cdot${n(ga)}}}=${n(T, 1)}\;\\text{u. de tiempo}`, nota: 'Vale para ciclos pequeños; en los grandes dura más.' },
    ];
  },
  compare: (_p, m) => [{ label: 'Error del invariante (debe ser ~0)', teoria: 0, sim: m.deriva_invariante, nota: 'Mide qué tan bien el cálculo numérico conserva la cantidad que el modelo dice constante.' }],
  insight: (p) => {
    const xs = +p.gamma / +p.delta, ys = +p.alpha / +p.beta;
    return `El equilibrio está en ${n(xs, 0)} presas y ${n(ys, 0)} depredadores. Empiezas con ${n(+p.x0, 0)} y ${n(+p.y0, 0)}: ${+p.x0 > xs ? 'más presas' : 'menos presas'} y ${+p.y0 > ys ? 'más depredadores' : 'menos depredadores'} de lo que el equilibrio sostiene.`;
  },
  view({ ctx, w, h, state: s, traj, p }) {
    gridFill(ctx, w, h, 20);
    const al = +p.alpha, be = +p.beta, de = +p.delta, ga = +p.gamma, xs = ga / de, ys = al / be;
    const xmax = Math.ceil(Math.max(70, xs * 2.4, ...traj.map((t) => t.x * 1.1)) / 10) * 10, ymax = Math.ceil(Math.max(35, ys * 2.6, ...traj.map((t) => t.y * 1.1)) / 5) * 5;
    const pl = 56, pr = 450, pt = 40, pb = h - 54, X = (x: number) => pl + (x / xmax) * (pr - pl), Y = (y: number) => pb - (y / ymax) * (pb - pt);
    ctx.strokeStyle = INK; ctx.lineWidth = 1.5; ctx.beginPath(); ctx.moveTo(pl, pt - 8); ctx.lineTo(pl, pb); ctx.lineTo(pr + 6, pb); ctx.stroke();
    const sx = niceStep(xmax, 6), sy = niceStep(ymax, 5);
    for (let x = 0; x <= xmax; x += sx) mono(ctx, String(x), X(x), pb + 16, 'center', 10);
    for (let y = 0; y <= ymax; y += sy) mono(ctx, String(y), pl - 8, Y(y) + 3, 'right', 10);
    label(ctx, 'presas →', pr, pb + 34, 'right', 12, COLORS[0]); label(ctx, 'depredadores ↑', pl + 6, pt - 14, 'left', 12, COLORS[4]);
    // campo de direcciones
    for (let i = 1; i < 10; i++) for (let j = 1; j < 8; j++) {
      const x = (xmax * i) / 10, y = (ymax * j) / 8, dx = al * x - be * x * y, dy = de * x * y - ga * y, vx = dx * ((pr - pl) / xmax), vy = -dy * ((pb - pt) / ymax), m = Math.hypot(vx, vy) || 1;
      arrow(ctx, X(x) - (vx / m) * 7, Y(y) - (vy / m) * 7, X(x) + (vx / m) * 7, Y(y) + (vy / m) * 7, 'rgba(159,192,240,.45)', 1.2, 5);
    }
    // isoclinas
    ctx.setLineDash([6, 5]); ctx.lineWidth = 1.4; ctx.strokeStyle = COLORS[0]; ctx.beginPath(); ctx.moveTo(X(xs), pt); ctx.lineTo(X(xs), pb); ctx.stroke();
    ctx.strokeStyle = COLORS[4]; ctx.beginPath(); ctx.moveTo(pl, Y(ys)); ctx.lineTo(pr, Y(ys)); ctx.stroke(); ctx.setLineDash([]);
    mono(ctx, `x* = ${n(xs, 0)}`, X(xs) + 5, pt + 10, 'left', 11, COLORS[0]); mono(ctx, `y* = ${n(ys, 0)}`, pr - 4, Y(ys) - 6, 'right', 11, COLORS[4]);
    hand(ctx, 'mucha presa,', X(xs) + (pr - X(xs)) / 2, Y(ys) + (pb - Y(ys)) / 2 - 4, 'center', 15, MUT); hand(ctx, 'pocos depredadores: todo crece', X(xs) + (pr - X(xs)) / 2, Y(ys) + (pb - Y(ys)) / 2 + 12, 'center', 15, MUT);
    hand(ctx, 'muchos depredadores:', X(xs) + (pr - X(xs)) / 2, pt + 40, 'center', 15, MUT); hand(ctx, 'caen las presas', X(xs) + (pr - X(xs)) / 2, pt + 56, 'center', 15, MUT);
    hand(ctx, 'poca presa:', pl + (X(xs) - pl) / 2, pt + 40, 'center', 15, MUT); hand(ctx, 'caen los depredadores', pl + (X(xs) - pl) / 2, pt + 56, 'center', 15, MUT);
    hand(ctx, 'pocos depredadores:', pl + (X(xs) - pl) / 2, pb - 30, 'center', 15, MUT); hand(ctx, 'se recuperan las presas', pl + (X(xs) - pl) / 2, pb - 14, 'center', 15, MUT);
    // equilibrio y trayectoria
    ctx.fillStyle = COLORS[2]; ctx.strokeStyle = INK; ctx.lineWidth = 1.5; ctx.beginPath(); ctx.arc(X(xs), Y(ys), 5.5, 0, 7); ctx.fill(); ctx.stroke();
    ctx.strokeStyle = PEN; ctx.lineWidth = 2.6; ctx.lineJoin = 'round'; ctx.beginPath(); traj.forEach((t, i) => (i ? ctx.lineTo(X(t.x), Y(t.y)) : ctx.moveTo(X(t.x), Y(t.y)))); ctx.stroke();
    ctx.fillStyle = PEN; ctx.strokeStyle = INK; ctx.beginPath(); ctx.arc(X(s.x), Y(s.y), 7, 0, 7); ctx.fill(); ctx.stroke();
    hand(ctx, 'plano de fases', pl + 8, pt + 4, 'left', 18, INK);
    // series en el tiempo
    const tl = 500, tr = w - 20, tt = pt, tb = pb, Tm = 40, Ym = Math.max(ymax, ...traj.map((t) => t.x * 1.05));
    const TX = (t: number) => tl + (t / Tm) * (tr - tl), TY = (v: number) => tb - (v / Ym) * (tb - tt);
    ctx.strokeStyle = INK; ctx.lineWidth = 1.5; ctx.beginPath(); ctx.moveTo(tl, tt - 8); ctx.lineTo(tl, tb); ctx.lineTo(tr, tb); ctx.stroke();
    for (let t = 0; t <= Tm; t += 10) mono(ctx, String(t), TX(t), tb + 16, 'center', 10);
    label(ctx, 'tiempo →', tr, tb + 34, 'right', 12, MUT);
    const line = (key: 'x' | 'y', c: string) => { ctx.strokeStyle = c; ctx.lineWidth = 2.4; ctx.beginPath(); traj.forEach((t, i) => (i ? ctx.lineTo(TX(t.t), TY(t[key])) : ctx.moveTo(TX(t.t), TY(t[key])))); ctx.stroke(); };
    line('x', COLORS[0]); line('y', COLORS[4]);
    ctx.setLineDash([3, 4]); ctx.strokeStyle = MUT; ctx.lineWidth = 1; ctx.beginPath(); ctx.moveTo(TX(s.t), tt); ctx.lineTo(TX(s.t), tb); ctx.stroke(); ctx.setLineDash([]);
    hand(ctx, 'presas', tr - 4, tt + 6, 'right', 18, COLORS[0]); hand(ctx, 'depredadores', tr - 4, tt + 26, 'right', 18, COLORS[4]);
    mono(ctx, `t = ${n(s.t, 1)}   presas ${n(s.x, 1)}   depredadores ${n(s.y, 1)}`, pl, h - 10, 'left', 12, INK);
  },
};
