import { gridFill, ground, mapper, niceStep, label, mono, arrow, dim, callout, COLORS, INK, MUT, PEN } from '../render/plot';
import type { Extra } from '../core/types';
import type { MState } from '../sims/mrua';
import { n, near } from './util';

export const muaExtra: Extra<MState> = {
  size: { width: 800, height: 280 },
  readouts: ['x_final', 'v_final', 'desplazamiento'],
  paramHints: {
    x0: 'Dónde está el móvil cuando empieza a contar el tiempo.',
    v0: 'Rapidez inicial. Negativa significa que va hacia atrás (hacia la izquierda).',
    a: 'Cuánto cambia la velocidad cada segundo. Con 0 el movimiento es uniforme (MRU).',
    T: 'Cuánto tiempo dura el recorrido que se simula.',
  },
  learn: {
    resumen: 'Un carro que acelera. Mira cómo la posición, la velocidad y la aceleración se conectan entre sí en tres gráficas.',
    objetivos: [
      'Distinguir MRU (velocidad constante) de MRUA (aceleración constante).',
      'Leer una gráfica $x$–$t$, $v$–$t$ y $a$–$t$.',
      'Calcular posición y velocidad con las ecuaciones del MRUA.',
    ],
    idea: [
      'Si la aceleración es cero, la velocidad no cambia y la posición crece en línea recta: $x=x_0+vt$ (MRU). Si la aceleración es constante, la **velocidad** crece en línea recta y la **posición** dibuja una parábola.',
      'Las gráficas se conectan: la pendiente de $x$–$t$ es la velocidad, la pendiente de $v$–$t$ es la aceleración, y el área bajo $v$–$t$ es el desplazamiento.',
    ],
    analogia: 'Es como el velocímetro de un carro: si el conductor pisa el acelerador igual todo el rato, la aguja sube a ritmo constante, pero los kilómetros recorridos crecen cada vez más rápido.',
    formulas: [
      { tex: 'v=v_0+a\\,t', nombre: 'Velocidad en el tiempo t', vars: [['v_0', 'velocidad inicial (m/s)'], ['a', 'aceleración (m/s²)'], ['t', 'tiempo (s)']] },
      { tex: 'x=x_0+v_0\\,t+\\frac{1}{2}\\,a\\,t^2', nombre: 'Posición en el tiempo t', vars: [['x_0', 'posición inicial (m)'], ['x', 'posición en t (m)']] },
      { tex: 'v^2=v_0^2+2\\,a\\,\\Delta x', nombre: 'Sin usar el tiempo', vars: [['\\Delta x', 'desplazamiento = x − x₀']] },
    ],
    ejemplos: [
      { titulo: 'Un carro que arranca', texto: 'Parte del reposo en $x=0$ con $a=2\\,\\text{m/s}^2$. ¿Dónde está y qué tan rápido va a los $5$ s?', pasos: ['Velocidad: $v=0+2\\cdot5=10$ m/s.', 'Posición: $x=0+0\\cdot5+\\tfrac12\\cdot2\\cdot5^2=25$ m.', 'Revisa: $v^2=2a\\Delta x=2\\cdot2\\cdot25=100$, o sea $v=10$ m/s. ✓'] },
      { titulo: 'Frenar', texto: 'Un móvil va a $12$ m/s y frena con $a=-3\\,\\text{m/s}^2$. ¿Cuánto avanza hasta detenerse?', pasos: ['Se detiene cuando $v=0$: $t=12/3=4$ s.', '$x=12\\cdot4+\\tfrac12(-3)(4^2)=48-24=24$ m.'] },
    ],
    errores: [
      { mito: '«Aceleración negativa significa que frena».', realidad: 'Significa que apunta hacia la izquierda. Si el móvil también va hacia la izquierda, ¡acelera!' },
      { mito: '«Si la velocidad es cero, la aceleración es cero».', realidad: 'Al lanzar algo hacia arriba, en el punto más alto $v=0$ y $a=-g$ sigue actuando.' },
      { mito: '«La gráfica x–t curva significa que va en curva».', realidad: 'El móvil va en línea recta; la curva dice que su velocidad cambia.' },
    ],
    saber11: 'En una gráfica $v$–$t$, el área es distancia y la pendiente es aceleración. En una $x$–$t$, la pendiente es velocidad. Ojo con las unidades: km/h → m/s se divide entre 3,6.',
  },
  presets: [
    { id: 'mru', label: 'Velocidad constante', desc: 'Con $a=0$ la gráfica $x$–$t$ es una recta: recorre $2\\,\\text{m}$ cada segundo.', params: { x0: 0, v0: 2, a: 0, T: 6 } },
    { id: 'arranque', label: 'Arrancar del reposo', desc: 'Sale quieto y acelera a $2\\,\\text{m/s}^2$. A los 6 s va a 12 m/s y lleva 36 m.', params: { x0: 0, v0: 0, a: 2, T: 6 } },
    { id: 'freno', label: 'Frenar hasta parar', desc: 'Va a $12\\,\\text{m/s}$ y frena con $-3\\,\\text{m/s}^2$: se detiene a los 4 s, tras 24 m.', params: { x0: 0, v0: 12, a: -3, T: 4 } },
    { id: 'vuelta', label: 'Ir y devolverse', desc: 'Sale hacia adelante pero la aceleración negativa lo frena, lo detiene y lo regresa.', params: { x0: 10, v0: 8, a: -2, T: 10 } },
  ],
  experiments: [
    { id: 'dobla', titulo: 'El doble de tiempo', setup: { x0: 0, v0: 0, a: 2, T: 3 }, cambio: { T: 6 },
      pregunta: 'Un móvil que arranca del reposo recorre 9 m en 3 s. ¿Cuánto recorre en 6 s?',
      opciones: ['18 m', '27 m', '36 m'], correcta: 2,
      explicacion: 'La distancia depende de $t^2$: al duplicar el tiempo se cuadruplica. $9\\cdot4=36$ m.',
      check: (b, a) => near(a.x_final / b.x_final, 4, 0.01) },
    { id: 'frenaneg', titulo: 'Aceleración negativa', setup: { x0: 0, v0: 6, a: 0, T: 4 }, cambio: { a: -1.5 },
      pregunta: 'Un móvil va a $6\\,\\text{m/s}$ en MRU. Si le pones $a=-1{,}5\\,\\text{m/s}^2$, a los 4 s su velocidad será...',
      opciones: ['0 m/s', '6 m/s', '-6 m/s'], correcta: 0,
      explicacion: '$v=6-1{,}5\\cdot4=0$: justo se detiene.',
      check: (b, a) => near(a.v_final, 0, 0.01) && near(b.v_final, 6, 0.01) },
    { id: 'atras', titulo: 'Velocidad hacia atrás', setup: { x0: 10, v0: 5, a: 0, T: 4 }, cambio: { v0: -5 },
      pregunta: 'Con $x_0=10$ m y $v_0=-5$ m/s, ¿dónde estará a los 4 s?',
      opciones: ['30 m', '-10 m', '10 m'], correcta: 1,
      explicacion: '$x=10+(-5)(4)=-10$ m. El signo negativo indica que se mueve a la izquierda.',
      check: (b, a) => near(a.x_final, -10, 0.01) },
  ],
  solution: (p) => {
    const x0 = +p.x0, v0 = +p.v0, a = +p.a, T = +p.T;
    const v = v0 + a * T, x = x0 + v0 * T + 0.5 * a * T * T;
    return [
      { t: 'Velocidad final', tex: `v=v_0+aT=${n(v0)}+(${n(a)})(${n(T)})=${n(v)}\;\\text{m/s}` },
      { t: 'Posición final', tex: `x=x_0+v_0T+\\tfrac12aT^2=${n(x0)}+${n(v0)}(${n(T)})+\\tfrac12(${n(a)})(${n(T)})^2=${n(x)}\;\\text{m}` },
      { t: 'Desplazamiento', tex: `\\Delta x=x-x_0=${n(x - x0)}\;\\text{m}`, nota: 'Es la posición final menos la inicial (puede ser negativo).' },
      { t: 'Comprobación sin tiempo', tex: `v^2=v_0^2+2a\\Delta x:\;${n(v * v)}=${n(v0 * v0 + 2 * a * (x - x0))}`, nota: 'Si los dos lados coinciden, las cuentas están bien.' },
    ];
  },
  compare: (p, m) => {
    const x0 = +p.x0, v0 = +p.v0, a = +p.a, T = +p.T;
    return [
      { label: 'Posición final (m)', teoria: x0 + v0 * T + 0.5 * a * T * T, sim: m.x_final },
      { label: 'Velocidad final (m/s)', teoria: v0 + a * T, sim: m.v_final },
    ];
  },
  insight: (p) => {
    const a = +p.a, v0 = +p.v0, T = +p.T;
    if (a === 0) return 'Con $a=0$ es MRU: la velocidad no cambia y $x$–$t$ es una recta.';
    if (v0 * a < 0) { const ts = -v0 / a; return `La aceleración se opone a la velocidad: se detiene en $t=${n(ts)}$ s${ts < T ? ' y luego se devuelve' : ''}.`; }
    return 'Aceleración y velocidad apuntan igual: cada vez va más rápido.';
  },
  view({ ctx, w, h, state, traj, p }) {
    const x0 = +p.x0, v0 = +p.v0, a = +p.a, T = +p.T;
    const xs = traj.map((s) => s.x).concat([x0, x0 + v0 * T + 0.5 * a * T * T, state.x]);
    const lo = Math.min(...xs, 0) - 6, hi = Math.max(...xs, 20) + 6;
    const padL = 40, padR = 40, ty = h * 0.58;
    const X = (x: number) => padL + ((x - lo) / (hi - lo)) * (w - padL - padR);
    gridFill(ctx, w, h, 20);
    ground(ctx, padL - 10, w - padR + 10, ty + 22);
    const st = niceStep(hi - lo, 9);
    ctx.strokeStyle = INK; ctx.lineWidth = 1.2;
    for (let x = Math.ceil(lo / st) * st; x <= hi; x += st) { ctx.beginPath(); ctx.moveTo(X(x), ty + 22); ctx.lineTo(X(x), ty + 30); ctx.stroke(); mono(ctx, String(+x.toFixed(2)), X(x), ty + 44, 'center', 10); }
    label(ctx, 'x (m)', w - padR, ty + 58, 'right', 12, MUT);
    // estela: una marca por segundo
    let last = -1;
    for (const s of traj) { const k = Math.floor(s.t + 1e-9); if (k === last) continue; last = k; ctx.fillStyle = 'rgba(92,225,255,.25)'; ctx.fillRect(X(s.x) - 14, ty - 10, 28, 22); ctx.strokeStyle = MUT; ctx.strokeRect(X(s.x) - 14, ty - 10, 28, 22); mono(ctx, `${k}s`, X(s.x), ty + 3, 'center', 9, MUT); }
    // carro
    const cx = X(state.x);
    ctx.fillStyle = COLORS[0]; ctx.strokeStyle = INK; ctx.lineWidth = 2; ctx.fillRect(cx - 18, ty - 12, 36, 24); ctx.strokeRect(cx - 18, ty - 12, 36, 24);
    ctx.fillStyle = '#121821'; for (const dx of [-10, 10]) { ctx.beginPath(); ctx.arc(cx + dx, ty + 14, 5, 0, 7); ctx.fill(); ctx.stroke(); }
    if (Math.abs(state.v) > 0.05) arrow(ctx, cx, ty - 28, cx + state.v * 9, ty - 28, COLORS[2], 2.6);
    mono(ctx, `v = ${n(state.v, 1)} m/s`, cx, ty - 42, 'center', 12, COLORS[2]);
    if (Math.abs(a) > 0.01) { arrow(ctx, cx, ty + 70, cx + a * 16, ty + 70, COLORS[4], 2.6); mono(ctx, `a = ${n(a, 1)} m/s²`, cx, ty + 90, 'center', 12, COLORS[4]); }
    dim(ctx, X(x0), ty - 92, X(state.x), ty - 92, `Δx = ${n(state.x - x0, 1)} m`, { off: 0, color: PEN });
    mono(ctx, `t = ${n(state.t)} s`, padL, 26, 'left', 14, INK);
    label(ctx, 'cada cuadro = 1 s', w - padR, 26, 'right', 12, MUT);
  },
};
