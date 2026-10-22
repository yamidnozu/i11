import { gridFill, label, mono, hand, arrow, COLORS, INK, MUT, PEN } from '../render/plot';
import type { Extra } from '../core/types';
import type { GState } from '../sims/gases';
import { n, near } from './util';

export const gasExtra: Extra<GState> = {
  size: { width: 800, height: 390 },
  readouts: ['presion', 'energia_cinetica_media', 'P_por_A_sobre_NT'],
  paramHints: {
    N: 'Cuántas partículas hay. Es el equivalente a los moles $n$.',
    T: 'Temperatura: mide qué tan rápido se mueven las partículas en promedio.',
    W: 'Ancho de la caja. Mueve la pared de la derecha: menos ancho es menos volumen.',
  },
  learn: {
    resumen: 'Un gas es un montón de partículas rebotando. La presión es el golpeteo contra las paredes. Cambia la caja, la temperatura o la cantidad de gas y mira cómo cambia ese golpeteo.',
    objetivos: [
      'Explicar presión, volumen y temperatura con el modelo de partículas.',
      'Predecir qué pasa con $P$ al cambiar $V$, $T$ o $n$.',
      'Usar $PV=nRT$ y las leyes de Boyle y Gay-Lussac.',
    ],
    idea: [
      'Las partículas del gas se mueven en línea recta hasta chocar con una pared. Cada choque empuja la pared un poquito; millones de choques por segundo forman la **presión**. Más choques o más fuertes → más presión.',
      'La **temperatura** es la energía cinética media de las partículas: más caliente es más rápido (y choques más fuertes). Reducir el volumen aumenta la frecuencia de choques; añadir partículas también. Todo se resume en $PV=nRT$.',
    ],
    analogia: 'Imagina una caja con pelotas de ping-pong sueltas, agitadas por un ventilador. Si encoges la caja o metes más pelotas, golpean las paredes más seguido. Si aumentas el ventilador, golpean más fuerte.',
    formulas: [
      { tex: 'P\\,V=n\\,R\\,T', nombre: 'Gas ideal', vars: [['P', 'presión (atm)'], ['V', 'volumen (L)'], ['n', 'cantidad de gas (mol)'], ['R', '0,082 atm·L/(mol·K)'], ['T', 'temperatura absoluta (K)']] },
      { tex: 'P_1V_1=P_2V_2', nombre: 'Ley de Boyle (T y n fijas)', vars: [['P_1,V_1', 'estado inicial'], ['P_2,V_2', 'estado final']] },
      { tex: '\\frac{P_1}{T_1}=\\frac{P_2}{T_2}', nombre: 'Ley de Gay-Lussac (V y n fijos)', vars: [['T', 'siempre en kelvin']] },
      { tex: 'T(K)=T(^{\\circ}C)+273', nombre: 'Pasar a kelvin', vars: [['K', 'escala absoluta']] },
    ],
    ejemplos: [
      { titulo: 'Comprimir un gas (Boyle)', texto: 'Un gas ocupa $4$ L a $1$ atm. Se comprime a $1$ L sin cambiar la temperatura. ¿Cuál es la nueva presión?', pasos: ['$P_1V_1=P_2V_2 \\Rightarrow 1\\cdot4=P_2\\cdot1$.', '$P_2=4$ atm. Un cuarto del volumen, cuatro veces la presión.'] },
      { titulo: 'Calentar una olla cerrada', texto: 'Un recipiente rígido tiene gas a $27\\,^{\\circ}$C y $2$ atm. Se calienta hasta $127\\,^{\\circ}$C.', pasos: ['Pasa a kelvin: $T_1=300$ K, $T_2=400$ K.', '$P_2=P_1\\frac{T_2}{T_1}=2\\cdot\\frac{400}{300}=2{,}67$ atm.'] },
    ],
    errores: [
      { mito: '«La temperatura se puede usar en °C en las fórmulas».', realidad: 'Siempre en kelvin. Duplicar los °C no duplica la energía de las partículas.' },
      { mito: '«Las partículas se mueven más rápido si hay más».', realidad: 'La rapidez media depende solo de $T$. Más partículas = más choques, no choques más fuertes.' },
      { mito: '«Al comprimir, las partículas se hacen más pequeñas».', realidad: 'No cambian: solo hay menos espacio entre ellas y chocan más seguido.' },
    ],
    saber11: 'Identifica qué se mantiene constante (T, V o n) y escoge la ley correspondiente. Convierte siempre a kelvin. Si la gráfica $P$–$V$ es una hipérbola, es Boyle; si $P$–$T$ es una recta que sale del origen, es Gay-Lussac.',
  },
  presets: [
    { id: 'base', label: 'Estado inicial', desc: '60 partículas, $T=300$, caja completa. Sirve de referencia para comparar los demás.', params: { N: 60, T: 300, W: 100 } },
    { id: 'comprimir', label: 'Comprimir a la mitad', desc: 'Con el ancho en 50 el volumen se reduce a la mitad y la presión se duplica (Boyle).', params: { N: 60, T: 300, W: 50 } },
    { id: 'calentar', label: 'Calentar el doble', desc: 'Con $T=600$ las partículas van más rápido (en color más cálido) y la presión se duplica.', params: { N: 60, T: 600, W: 100 } },
    { id: 'mas', label: 'Meter más gas', desc: 'Con 120 partículas hay el doble de choques: la presión se duplica.', params: { N: 120, T: 300, W: 100 } },
    { id: 'frio', label: 'Enfriar mucho', desc: 'Con $T=100$ casi no se mueven: baja la presión.', params: { N: 60, T: 100, W: 100 } },
  ],
  experiments: [
    { id: 'boyle', titulo: 'Reducir el volumen', setup: { N: 60, T: 300, W: 100 }, cambio: { W: 50 },
      pregunta: 'Reduces el ancho de la caja a la mitad (el volumen también baja a la mitad). La presión...',
      opciones: ['Se reduce a la mitad', 'Se duplica', 'Queda igual'], correcta: 1,
      explicacion: 'Boyle: $P\\propto 1/V$. Las partículas tienen menos espacio y golpean las paredes el doble de seguido.',
      check: (b, a) => near(a.presion / b.presion, 2, 0.3) },
    { id: 'gay', titulo: 'Calentar el gas', setup: { N: 60, T: 150, W: 100 }, cambio: { T: 300 },
      pregunta: 'Duplicas la temperatura de $150$ a $300$ (volumen y cantidad fijos). La presión...',
      opciones: ['Se duplica', 'Aumenta un poco', 'Queda igual'], correcta: 0,
      explicacion: 'Gay-Lussac: $P\\propto T$. Las partículas van más rápido y golpean más seguido y con más fuerza.',
      check: (b, a) => near(a.presion / b.presion, 2, 0.3) },
    { id: 'mol', titulo: 'Agregar partículas', setup: { N: 30, T: 300, W: 100 }, cambio: { N: 60 },
      pregunta: 'Duplicas la cantidad de partículas (misma caja y temperatura). La presión...',
      opciones: ['Se duplica', 'Se reduce a la mitad', 'Queda igual'], correcta: 0,
      explicacion: '$P\\propto n$: el doble de partículas da el doble de choques por segundo.',
      check: (b, a) => near(a.presion / b.presion, 2, 0.4) },
    { id: 'ke', titulo: 'Energía por partícula', setup: { N: 30, T: 300, W: 100 }, cambio: { N: 120 },
      pregunta: 'Cuadruplicas las partículas a la misma temperatura. La energía cinética media de cada partícula...',
      opciones: ['Se cuadruplica', 'Queda igual', 'Se reduce a la cuarta parte'], correcta: 1,
      explicacion: 'La energía cinética media depende solo de $T$. Hay más partículas, pero cada una se mueve igual de rápido en promedio.',
      check: (b, a) => near(a.energia_cinetica_media / b.energia_cinetica_media, 1, 0.15) },
  ],
  solution: (p) => {
    const N = Math.round(+p.N), T = +p.T, W = +p.W, A = W * 100, P = (N * T) / A;
    return [
      { t: 'Ecuación del gas ideal en esta caja 2D', tex: 'P\\,A=N\\,k\\,T\\quad(k=1)', nota: 'En el modelo, la «masa» y la constante de Boltzmann valen 1; por eso las unidades son arbitrarias, pero la proporción es la de $PV=nRT$.' },
      { t: 'Área (volumen) de la caja', tex: `A=W\\cdot H=${n(W, 0)}\\cdot100=${n(A, 0)}` },
      { t: 'Presión esperada', tex: `P=\\frac{N\\,T}{A}=\\frac{${N}\\cdot${n(T, 0)}}{${n(A, 0)}}=${n(P, 3)}` },
      { t: 'Lo que debe cumplirse', tex: `\\frac{P\\,A}{N\\,T}\\approx1`, nota: 'Corre la simulación: la medición hace ese cociente y debe quedar cerca de 1 (con algo de ruido por el azar).' },
    ];
  },
  compare: (p, m) => [{ label: 'Presión (u.a.)', teoria: (Math.round(+p.N) * +p.T) / (+p.W * 100), sim: m.presion, nota: 'Hay ruido: al correr más tiempo se acerca más.' }],
  insight: (p) => {
    const T = +p.T, W = +p.W;
    if (W <= 60) return 'Caja pequeña: choques más frecuentes con las paredes, presión alta.';
    if (T >= 500) return 'Temperatura alta: las partículas (en amarillo) son rápidas y golpean fuerte.';
    if (T <= 150) return 'Temperatura baja: las partículas casi no se mueven y la presión es baja.';
    return 'Ajusta una variable a la vez y mira qué pasa con la presión.';
  },
  view({ ctx, w, h, state: s }) {
    gridFill(ctx, w, h, 20);
    const sc = 3.1, ox = 34, oy = 36, bh = s.H * sc;
    // caja con pistón móvil (la pared derecha)
    ctx.strokeStyle = INK; ctx.lineWidth = 2.6; ctx.beginPath(); ctx.moveTo(ox + 100 * sc, oy); ctx.lineTo(ox, oy); ctx.lineTo(ox, oy + bh); ctx.lineTo(ox + 100 * sc, oy + bh); ctx.stroke();
    ctx.fillStyle = COLORS[4]; ctx.fillRect(ox + s.W * sc, oy - 4, 9, bh + 8);
    ctx.fillStyle = 'rgba(234,243,255,.07)'; ctx.fillRect(ox, oy, s.W * sc, bh);
    ctx.strokeStyle = MUT; ctx.lineWidth = 1; ctx.setLineDash([4, 4]); ctx.strokeRect(ox, oy, s.W * sc, bh); ctx.setLineDash([]);
    // partículas por rapidez
    const sd = Math.sqrt(s.T);
    for (let i = 0; i < s.N; i++) {
      const sp = Math.hypot(s.vx[i], s.vy[i]) / sd;
      ctx.fillStyle = sp > 1.6 ? COLORS[4] : sp > 1 ? COLORS[1] : COLORS[0];
      ctx.beginPath(); ctx.arc(ox + s.x[i] * sc, oy + s.y[i] * sc, 3.4, 0, 7); ctx.fill();
    }
    const gp = Math.min(60, 8 + s.pressure * 70);
    arrow(ctx, ox + s.W * sc + 46, oy + bh / 2, ox + s.W * sc + 14, oy + bh / 2, COLORS[4], 3); 
    hand(ctx, 'presión', ox + s.W * sc + 28, oy + bh / 2 - 12, 'center', 17, COLORS[4]);
    mono(ctx, `ancho = ${n(s.W, 0)}`, ox + (s.W * sc) / 2, oy + bh + 22, 'center', 12, MUT);
    label(ctx, 'lento', ox, oy - 14, 'left', 11, COLORS[0]); label(ctx, 'medio', ox + 50, oy - 14, 'left', 11, COLORS[1]); label(ctx, 'rápido', ox + 100, oy - 14, 'left', 11, COLORS[4]);
    // histograma de rapideces + curva teórica de Maxwell-Boltzmann 2D
    const hx = 440, hy = 70, hw = 320, hh = 220, vmax = 3.4 * sd, nb = 16, bins = Array(nb).fill(0);
    for (let i = 0; i < s.N; i++) { const b = Math.min(nb - 1, Math.floor((Math.hypot(s.vx[i], s.vy[i]) / vmax) * nb)); bins[b]++; }
    const dens = bins.map((c) => c / (s.N * (vmax / nb))), th = (v: number) => (v / s.T) * Math.exp((-v * v) / (2 * s.T));
    const ymax = Math.max(...dens, th(sd)) * 1.15;
    ctx.strokeStyle = INK; ctx.lineWidth = 1.4; ctx.beginPath(); ctx.moveTo(hx, hy); ctx.lineTo(hx, hy + hh); ctx.lineTo(hx + hw, hy + hh); ctx.stroke();
    dens.forEach((d, i) => { const bw = hw / nb, bh2 = (d / ymax) * hh; ctx.fillStyle = 'rgba(92,225,255,.55)'; ctx.fillRect(hx + i * bw + 1, hy + hh - bh2, bw - 2, bh2); });
    ctx.strokeStyle = PEN; ctx.lineWidth = 2.4; ctx.beginPath();
    for (let i = 0; i <= 80; i++) { const v = (vmax * i) / 80, x = hx + (v / vmax) * hw, y = hy + hh - (th(v) / ymax) * hh; i ? ctx.lineTo(x, y) : ctx.moveTo(x, y); }
    ctx.stroke();
    label(ctx, 'rapidez de las partículas →', hx + hw, hy + hh + 20, 'right', 12, MUT);
    label(ctx, 'cuántas', hx + 6, hy + 10, 'left', 12, MUT);
    hand(ctx, 'curva teórica', hx + hw - 10, hy + 40, 'right', 18, PEN);
    // manómetro
    const my0 = hy + hh + 52;
    label(ctx, 'presión medida', hx, my0 - 8, 'left', 12, MUT);
    ctx.strokeStyle = INK; ctx.strokeRect(hx, my0, hw, 16); ctx.fillStyle = COLORS[4]; ctx.fillRect(hx, my0, Math.min(hw, (s.pressure / 8) * hw), 16);
    mono(ctx, `P = ${n(s.pressure, 2)}   V = ${n(s.W * s.H, 0)}   N = ${s.N}   T = ${n(s.T, 0)}`, ox, h - 10, 'left', 13, INK);
    void gp;
  },
};
