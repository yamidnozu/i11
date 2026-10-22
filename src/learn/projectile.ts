import { gridFill, ground, mapper, niceStep, label, mono, hand, arrow, dim, callout, COLORS, INK, MUT, PEN } from '../render/plot';
import type { Extra } from '../core/types';
import type { PState } from '../sims/projectile';
import { rad, n, near } from './util';

export const analytic = (v0: number, th: number, g: number) => {
  const t = rad(th), vx = v0 * Math.cos(t), vy = v0 * Math.sin(t);
  return { vx, vy, tUp: vy / g, T: (2 * vy) / g, H: (vy * vy) / (2 * g), R: (vx * 2 * vy) / g };
};

export const projectileExtra: Extra<PState> = {
  size: { width: 800, height: 420 },
  readouts: ['alcance', 'altura_max', 't_vuelo'],
  paramHints: {
    v0: 'Rapidez con la que sale el proyectil. Si la duplicas, el alcance se cuadruplica.',
    theta: 'Ángulo sobre el piso: 0° es horizontal y 90° es vertical.',
    g: 'Aceleración hacia abajo que impone la gravedad. Elige otro lugar y mira qué cambia.',
    drag: 'Añade una fuerza del aire que se opone al movimiento y crece con el cuadrado de la rapidez.',
  },
  learn: {
    resumen: 'Un balón, una piedra o un chorro de agua siguen la misma curva. Mueve el ángulo y la rapidez, y mira por qué la trayectoria es una parábola.',
    objetivos: [
      'Separar cualquier lanzamiento en un movimiento horizontal y otro vertical.',
      'Predecir alcance, altura máxima y tiempo de vuelo con las fórmulas.',
      'Explicar por qué dos ángulos distintos pueden llegar al mismo punto.',
    ],
    idea: [
      'Un proyectil lanzado con rapidez $v_0$ y ángulo $\\theta$ vive dos movimientos a la vez. En horizontal no hay fuerza (sin aire): la velocidad $v_x$ **no cambia**. En vertical actúa la gravedad: $v_y$ disminuye $g$ cada segundo, llega a cero en el punto más alto y luego se hace negativa.',
      'Las dos «películas» comparten el mismo reloj. El tiempo de vuelo lo decide la parte vertical; el alcance es lo que avanza la parte horizontal en ese tiempo: $R = v_x\\,t_v$.',
    ],
    analogia: 'Es como patear un balón dentro de un bus que avanza a velocidad constante: para ti el balón sube y baja recto; para alguien en la calle, dibuja una curva.',
    formulas: [
      { tex: 'v_x=v_0\\cos\\theta\\qquad v_{y0}=v_0\\sin\\theta', nombre: 'Componentes de la velocidad inicial', vars: [['v_0', 'rapidez de salida (m/s)'], ['\\theta', 'ángulo sobre la horizontal'], ['v_x', 'componente horizontal, constante'], ['v_{y0}', 'componente vertical inicial']] },
      { tex: 'y=v_{y0}\\,t-\\frac{1}{2}\\,g\\,t^2', nombre: 'Altura en cada instante', vars: [['y', 'altura (m)'], ['t', 'tiempo desde el lanzamiento (s)'], ['g', 'gravedad, 9,8 m/s² en la Tierra']] },
      { tex: 't_v=\\frac{2\\,v_0\\sin\\theta}{g}\\qquad H=\\frac{v_0^2\\sin^2\\theta}{2g}', nombre: 'Tiempo de vuelo y altura máxima', vars: [['t_v', 'tiempo hasta volver al piso (s)'], ['H', 'altura máxima (m)']] },
      { tex: 'R=\\frac{v_0^2\\,\\sin 2\\theta}{g}', nombre: 'Alcance horizontal (sin aire)', vars: [['R', 'distancia horizontal recorrida (m)'], ['\\sin 2\\theta', 'máximo (=1) cuando θ = 45°']] },
    ],
    ejemplos: [
      { titulo: 'Un balón con g = 10 m/s²', texto: 'Un balón sale a $20\\,\\text{m/s}$ con $30°$. ¿Dónde cae y qué tan alto llega?', pasos: ['Componentes: $v_x=20\\cos30°=17{,}3$ m/s y $v_{y0}=20\\sin30°=10$ m/s.', 'Sube hasta que $v_y=0$: $t_{sub}=10/10=1$ s, así que el vuelo dura $t_v=2$ s.', 'Alcance: $R=v_x\\,t_v=17{,}3\\cdot2=34{,}6$ m.', 'Altura máxima: $H=10^2/(2\\cdot10)=5$ m.'] },
      { titulo: 'Dos ángulos, un mismo punto', texto: 'Con $v_0=20$ m/s y $g=9{,}8$ m/s², ¿con qué ángulos se llega a 40 m?', pasos: ['De $R=\\frac{v_0^2\\sin2\\theta}{g}$ sale $\\sin2\\theta=\\frac{R\\,g}{v_0^2}=\\frac{40\\cdot9{,}8}{400}=0{,}98$.', '$2\\theta\\approx78{,}5°$ o $2\\theta\\approx101{,}5°$.', '$\\theta\\approx39{,}3°$ o $\\theta\\approx50{,}7°$: suman 90°, son complementarios.'] },
    ],
    errores: [
      { mito: '«A 90° llega más lejos porque sube más».', realidad: 'A 90° solo sube y baja en el mismo lugar: $R=0$. Sin aire, el máximo está en 45°.' },
      { mito: '«La velocidad horizontal va disminuyendo mientras vuela».', realidad: 'Sin aire, $v_x$ es constante: nada la frena. Solo cambia $v_y$.' },
      { mito: '«En el punto más alto el proyectil está quieto».', realidad: 'Ahí $v_y=0$, pero $v_x$ sigue igual. La rapidez no es cero.' },
    ],
    saber11: 'Si el enunciado dice «g = 10 m/s²», úsala tal cual aunque la real sea 9,8. Si piden «la misma distancia», piensa en ángulos complementarios. Y recuerda: en el punto más alto solo $v_y$ vale cero.',
  },
  presets: [
    { id: 'tirolibre', label: 'Tiro libre de fútbol', desc: 'Un balón pateado desde el piso a $25\\,\\text{m/s}$ y $20°$ cae a unos 41 m si no hubiera aire. Activa la resistencia y compara.', params: { v0: 25, theta: 20, g: 9.8, drag: false } },
    { id: 'examen', label: 'Con g = 10 (examen)', desc: 'Números cómodos como los de una prueba: $v_0=20\\,\\text{m/s}$, $30°$ y $g=10$. Salen $R=34{,}6$ m, $H=5$ m y $t_v=2$ s.', params: { v0: 20, theta: 30, g: 10, drag: false } },
    { id: 'luna', label: 'En la Luna', desc: 'Sin atmósfera y con gravedad seis veces menor, el mismo lanzamiento llega seis veces más lejos.', params: { v0: 20, theta: 45, g: 1.62, drag: false } },
    { id: 'aire', label: 'Con aire', desc: 'A $40\\,\\text{m/s}$ la resistencia del aire pesa mucho: la parábola ideal (línea punteada) queda muy por encima de la trayectoria real.', params: { v0: 40, theta: 45, g: 9.8, drag: true } },
    { id: 'salto', label: 'Salto de longitud', desc: 'Un saltador despega a unos $9\\,\\text{m/s}$ con unos $20°$. El modelo da 5,3 m; las marcas reales son mayores porque el cuerpo sale y cae a alturas distintas. Es un buen ejemplo de los límites de un modelo.', params: { v0: 9, theta: 20, g: 9.8, drag: false } },
  ],
  experiments: [
    { id: 'e45', titulo: '¿Siempre gana 45°?', setup: { v0: 20, theta: 45, g: 9.8, drag: false }, cambio: { theta: 60 },
      pregunta: 'Con $45°$ el proyectil llega a 40,8 m. Si subes el ángulo a $60°$ (sube más), ¿qué pasa con el alcance?',
      opciones: ['Aumenta, porque sube más', 'Disminuye', 'Se queda igual'], correcta: 1,
      explicacion: 'Disminuye a 35,4 m. Con $60°$ sube más pero avanza menos. Lo que cuenta es $\\sin2\\theta$, y $\\sin120°<\\sin90°$.',
      check: (b, a) => a.alcance < b.alcance && near(a.alcance, 35.35, 0.3) },
    { id: 'compl', titulo: 'Ángulos complementarios', setup: { v0: 20, theta: 30, g: 9.8, drag: false }, cambio: { theta: 60 },
      pregunta: 'Con $30°$ el proyectil cae a 35,4 m. ¿Qué ocurre si lanzas a $60°$ con la misma rapidez?',
      opciones: ['Cae en el mismo punto, pero tarda más', 'Cae más lejos', 'Cae más cerca'], correcta: 0,
      explicacion: '$\\theta$ y $90°-\\theta$ tienen el mismo $\\sin2\\theta$, así que el alcance coincide. A $60°$ el vuelo es más alto y dura más: 3,5 s frente a 2,0 s.',
      check: (b, a) => near(a.alcance, b.alcance, 0.2) && a.t_vuelo > b.t_vuelo },
    { id: 'luna', titulo: 'Llevarlo a la Luna', setup: { v0: 20, theta: 45, g: 9.8, drag: false }, cambio: { g: 1.62 },
      pregunta: 'El mismo lanzamiento (20 m/s, 45°) llega a 40,8 m en la Tierra. En la Luna ($g=1{,}62$), el alcance será aproximadamente...',
      opciones: ['El doble', 'Seis veces mayor', 'Igual', '36 veces mayor'], correcta: 1,
      explicacion: 'El alcance es inversamente proporcional a $g$: $9{,}8/1{,}62\\approx6$. Llega a unos 247 m.',
      check: (b, a) => near(a.alcance / b.alcance, 6.05, 0.1) },
    { id: 'v2', titulo: 'Doblar la rapidez', setup: { v0: 10, theta: 45, g: 9.8, drag: false }, cambio: { v0: 20 },
      pregunta: 'Pasas de $10$ a $20\\,\\text{m/s}$ con el mismo ángulo. El alcance se multiplica por...',
      opciones: ['2', '3', '4', '8'], correcta: 2,
      explicacion: 'El alcance depende de $v_0^2$: al duplicar $v_0$ se cuadruplica (10,2 → 40,8 m). El tiempo de vuelo, en cambio, solo se duplica.',
      check: (b, a) => near(a.alcance / b.alcance, 4, 0.05) && near(a.t_vuelo / b.t_vuelo, 2, 0.05) },
    { id: 'aire', titulo: 'Entra el aire', setup: { v0: 30, theta: 45, g: 9.8, drag: false }, cambio: { drag: true },
      pregunta: 'Activas la resistencia del aire en un lanzamiento de $30\\,\\text{m/s}$ a $45°$. El alcance...',
      opciones: ['Aumenta', 'Disminuye mucho', 'Casi no cambia'], correcta: 1,
      explicacion: 'Disminuye mucho. La fuerza del aire se opone al movimiento y crece con $v^2$. La trayectoria deja de ser simétrica: baja más inclinada de lo que sube.',
      check: (b, a) => a.alcance < 0.8 * b.alcance },
  ],
  solution: (p) => {
    const v0 = +p.v0, th = +p.theta, g = +p.g, A = analytic(v0, th, g);
    return [
      { t: 'Descompón la velocidad inicial', tex: `v_x=v_0\\cos\\theta=${n(v0)}\\cdot\\cos ${n(th, 0)}°=${n(A.vx)}\;\\text{m/s}\\qquad v_{y0}=v_0\\sin\\theta=${n(v0)}\\cdot\\sin ${n(th, 0)}°=${n(A.vy)}\;\\text{m/s}`, nota: 'Horizontal y vertical se calculan por separado. $v_x$ no cambiará durante el vuelo.' },
      { t: 'Tiempo de subida y de vuelo', tex: `t_{sub}=\\frac{v_{y0}}{g}=\\frac{${n(A.vy)}}{${n(g)}}=${n(A.tUp)}\;\\text{s}\\qquad t_v=2\\,t_{sub}=${n(A.T)}\;\\text{s}`, nota: 'Sube hasta que $v_y=0$. Bajar toma el mismo tiempo que subir, por eso se duplica.' },
      { t: 'Altura máxima', tex: `H=\\frac{v_{y0}^2}{2g}=\\frac{${n(A.vy)}^2}{2\\cdot${n(g)}}=${n(A.H)}\;\\text{m}` },
      { t: 'Alcance', tex: `R=v_x\\cdot t_v=${n(A.vx)}\\cdot${n(A.T)}=${n(A.R)}\;\\text{m}`, nota: 'Lo que avanza en horizontal durante todo el vuelo.' },
      { t: 'Comprueba con la fórmula directa', tex: `R=\\frac{v_0^2\\sin2\\theta}{g}=\\frac{${n(v0)}^2\\cdot\\sin ${n(2 * th, 0)}°}{${n(g)}}=${n(A.R)}\;\\text{m}`, nota: p.drag ? 'Estos valores son del modelo **sin aire**. Con la resistencia activada, la simulación da menos a propósito.' : 'Las dos vías coinciden: buena señal.' },
    ];
  },
  compare: (p, m) => {
    const A = analytic(+p.v0, +p.theta, +p.g);
    return [
      { label: 'Alcance (m)', teoria: A.R, sim: m.alcance, nota: p.drag ? 'Con aire activado la simulación difiere de la teoría ideal: es lo esperado.' : undefined },
      { label: 'Altura máxima (m)', teoria: A.H, sim: m.altura_max },
      { label: 'Tiempo de vuelo (s)', teoria: A.T, sim: m.t_vuelo },
    ];
  },
  insight: (p) => {
    const v0 = +p.v0, th = +p.theta, g = +p.g, A = analytic(v0, th, g);
    const out: string[] = [];
    if (th >= 89) out.push('A $90°$ el proyectil solo sube y baja: no avanza nada.');
    else if (th <= 1) out.push('A $0°$ sale horizontal desde el piso: no alcanza a subir.');
    else if (near(th, 45, 1)) out.push(`Con $\\theta\\approx45°$ el alcance es el máximo posible para esta rapidez: ${n(v0 * v0 / g)} m.`);
    else out.push(`Con $${n(th, 0)}°$ llega a ${n(A.R)} m. Con $${n(90 - th, 0)}°$ (su complementario) llegaría al mismo punto.`);
    if (p.drag) out.push('El aire hace que la trayectoria real quede por debajo de la ideal (línea punteada).');
    return out.join(' ');
  },
  view({ ctx, w, h, state, traj, p }) {
    const v0 = +p.v0, th = +p.theta, g = +p.g;
    const A = analytic(v0, th, g);
    const padL = 66, padR = 30, padT = 50, padB = 96, gy = h - padB;
    const xmax = ((v0 * v0) / g) * 1.06 + 1, ymax = ((v0 * v0) / (2 * g)) * 1.1 + 0.5;
    const sc = Math.min((w - padL - padR) / xmax, (gy - padT) / ymax);
    const X = (x: number) => padL + x * sc, Y = (y: number) => gy - y * sc;
    gridFill(ctx, w, h, 20);
    ground(ctx, padL - 16, w - padR + 8, gy);
    ctx.strokeStyle = INK; ctx.lineWidth = 1.4; ctx.beginPath(); ctx.moveTo(padL, gy); ctx.lineTo(padL, padT - 10); ctx.stroke();
    const sx = niceStep(xmax, 7), sy = niceStep(ymax, 5);
    for (let x = 0; x <= xmax; x += sx) { ctx.beginPath(); ctx.moveTo(X(x), gy); ctx.lineTo(X(x), gy + 5); ctx.stroke(); mono(ctx, String(+x.toFixed(2)), X(x), gy + 19, 'center', 10); }
    for (let y = sy; y <= ymax; y += sy) { ctx.beginPath(); ctx.moveTo(padL - 5, Y(y)); ctx.lineTo(padL, Y(y)); ctx.stroke(); mono(ctx, String(+y.toFixed(2)), padL - 9, Y(y) + 3, 'right', 10); }
    label(ctx, 'x (m)', w - padR, gy + 19, 'right', 12, MUT); label(ctx, 'y (m)', padL + 8, padT - 2, 'left', 12, MUT);
    // parábola ideal (guía)
    ctx.strokeStyle = 'rgba(234,243,255,.4)'; ctx.lineWidth = 1.5; ctx.setLineDash([6, 6]); ctx.beginPath();
    for (let i = 0; i <= 120; i++) { const t = (A.T * i) / 120, x = A.vx * t, y = A.vy * t - 0.5 * g * t * t; i ? ctx.lineTo(X(x), Y(y)) : ctx.moveTo(X(x), Y(y)); }
    ctx.stroke(); ctx.setLineDash([]);
    // ángulo de lanzamiento
    ctx.strokeStyle = MUT; ctx.lineWidth = 1.2; ctx.beginPath(); ctx.arc(X(0), Y(0), 40, -rad(th), 0); ctx.stroke();
    ctx.setLineDash([4, 4]); ctx.beginPath(); ctx.moveTo(X(0), Y(0)); ctx.lineTo(X(0) + 78 * Math.cos(rad(th)), Y(0) - 78 * Math.sin(rad(th))); ctx.stroke(); ctx.setLineDash([]);
    mono(ctx, `θ = ${n(th, 0)}°`, X(0) + 48, Y(0) - 8, 'left', 12, INK);
    // trayectoria
    ctx.strokeStyle = COLORS[0]; ctx.lineWidth = 3; ctx.lineJoin = 'round'; ctx.beginPath();
    traj.forEach((s, i) => (i ? ctx.lineTo(X(s.x), Y(s.y)) : ctx.moveTo(X(s.x), Y(s.y))));
    ctx.stroke();
    // marcas cada 0,25 s (estroboscópico)
    let lastK = -1;
    for (const s of traj) {
      const k = Math.floor(s.t / 0.25 + 1e-9);
      if (k === lastK) continue;
      lastK = k;
      ctx.fillStyle = '#121821'; ctx.strokeStyle = INK; ctx.lineWidth = 1.4; ctx.beginPath(); ctx.arc(X(s.x), Y(s.y), 3.6, 0, 7); ctx.fill(); ctx.stroke();
      if (k % 2 === 0 && k > 0) mono(ctx, `${n(k * 0.25, 1)} s`, X(s.x), Y(s.y) - 10, 'center', 10);
    }
    // punto más alto y cotas
    let ap = traj[0];
    for (const s of traj) if (s.y > ap.y) ap = s;
    const passed = state.vy <= 0 || state.done;
    if (passed && ap.y > 0.01) {
      ctx.strokeStyle = 'rgba(234,243,255,.35)'; ctx.setLineDash([3, 4]); ctx.beginPath(); ctx.moveTo(X(ap.x), Y(ap.y)); ctx.lineTo(X(ap.x), gy); ctx.stroke(); ctx.setLineDash([]);
      dim(ctx, X(ap.x), gy, X(ap.x), Y(ap.y), `H = ${n(ap.y)} m`, { off: -30, color: COLORS[4] });
      callout(ctx, X(ap.x), Y(ap.y), X(ap.x) + 20, Y(ap.y) - 26, 'aquí vy = 0', PEN);
    }
    if (state.done) {
      dim(ctx, X(0), gy, X(state.x), gy, `R = ${n(state.x)} m`, { off: 50, color: COLORS[2] });
      callout(ctx, X(state.x), gy, X(state.x) - 14, gy - 40, 'impacto', PEN);
    } else if (state.t > 0) {
      ctx.strokeStyle = 'rgba(234,243,255,.3)'; ctx.setLineDash([2, 4]); ctx.beginPath(); ctx.moveTo(X(state.x), Y(state.y)); ctx.lineTo(X(state.x), gy); ctx.stroke(); ctx.setLineDash([]);
      mono(ctx, `x = ${n(state.x, 1)}`, X(state.x), gy + 36, 'center', 11, INK);
    }
    // móvil y vectores
    const bx = X(state.x), by = Y(state.y), k = 2.4;
    if (!state.done) {
      arrow(ctx, bx, by, bx + state.vx * k, by, COLORS[2], 2.2);
      arrow(ctx, bx, by, bx, by - state.vy * k, COLORS[3], 2.2);
      arrow(ctx, bx, by, bx + state.vx * k, by - state.vy * k, PEN, 2.6);
      mono(ctx, `vx ${n(state.vx, 1)}`, bx + state.vx * k + 6, by + 14, 'left', 11, COLORS[2]);
      mono(ctx, `vy ${n(state.vy, 1)}`, bx + 8, by - state.vy * k - 2, 'left', 11, COLORS[3]);
    }
    ctx.fillStyle = PEN; ctx.strokeStyle = INK; ctx.lineWidth = 2; ctx.beginPath(); ctx.arc(bx, by, 7, 0, 7); ctx.fill(); ctx.stroke();
    // leyenda y reloj
    const leg: [string, string][] = [[COLORS[2], 'vx: horizontal, constante'], [COLORS[3], 'vy: vertical, cambia'], [PEN, 'v: velocidad total']];
    leg.forEach(([c, t], i) => { arrow(ctx, w - 214, 24 + i * 18, w - 190, 24 + i * 18, c, 2, 6); label(ctx, t, w - 184, 28 + i * 18, 'left', 11, INK); });
    mono(ctx, `t = ${n(state.t)} s`, padL + 8, padT + 14, 'left', 14, INK);
  },
};
