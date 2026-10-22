import { gridFill, niceStep, label, mono, hand, callout, COLORS, INK, MUT, PEN } from '../render/plot';
import type { Extra } from '../core/types';
import type { FState } from '../sims/functions';
import { n, near } from './util';

const sg = (x: number, d = 2) => (x < 0 ? `-${n(-x, d)}` : `+${n(x, d)}`);
const P0 = { custom: '' };

export const functionsExtra: Extra<FState> = {
  size: { width: 600, height: 480 },
  readouts: ['intercepto_y', 'num_raices', 'vertice_x'],
  paramHints: {
    family: 'Elige la familia de funciones. Cada una tiene su «forma» característica.',
    a: 'En la lineal es la pendiente; en la cuadrática decide si abre arriba o abajo; en las otras estira la gráfica.',
    b: 'En la lineal sube o baja la recta; en la cuadrática desplaza el vértice; en la exponencial y la onda cambia la rapidez.',
    c: 'Mueve toda la gráfica hacia arriba o hacia abajo.',
    custom: 'Si escribes algo aquí, reemplaza a la familia. Puedes usar x, a, b y c (por ejemplo: a*x^2 + c).',
  },
  learn: {
    resumen: 'Cada función es una receta: das un $x$ y te devuelve un $y$. Mueve $a$, $b$ y $c$ y mira cómo se deforma la gráfica y dónde cortan los ejes.',
    objetivos: [
      'Relacionar la fórmula de una función con la forma de su gráfica.',
      'Hallar cortes con los ejes y, en la parábola, el vértice.',
      'Usar el discriminante para saber cuántas raíces tiene una cuadrática.',
    ],
    idea: [
      'Una **raíz** es un valor de $x$ donde $f(x)=0$: ahí la gráfica toca el eje horizontal. El **corte con $y$** es $f(0)$. Con esos puntos y la forma de la curva puedes reconstruir casi toda la función.',
      'La lineal $ax+b$ es una recta: $a$ la inclina y $b$ marca dónde corta el eje $y$. La cuadrática $ax^2+bx+c$ es una parábola: el signo de $a$ decide si abre hacia arriba o hacia abajo, y el vértice está en $x=-\\frac{b}{2a}$.',
    ],
    analogia: 'Una parábola es la trayectoria de un balón: sube hasta un punto más alto (el vértice) y baja. Las raíces son los lugares donde el balón está a ras del piso.',
    formulas: [
      { tex: 'f(x)=ax+b', nombre: 'Función lineal', vars: [['a', 'pendiente: cuánto sube $y$ por cada unidad de $x$'], ['b', 'corte con el eje $y$'], ['x=-b/a', 'raíz']] },
      { tex: 'x_v=-\\frac{b}{2a}\\qquad \\Delta=b^2-4ac', nombre: 'Vértice y discriminante', vars: [['x_v', 'posición del vértice'], ['\\Delta', '>0: dos raíces · =0: una · <0: ninguna']] },
      { tex: 'x=\\frac{-b\\pm\\sqrt{\\Delta}}{2a}', nombre: 'Fórmula general', vars: [['\\pm', 'una raíz con + y otra con −']] },
      { tex: 'f(x)=a\\sin(bx)+c', nombre: 'Onda sinusoidal', vars: [['|a|', 'amplitud'], ['2\\pi/|b|', 'periodo'], ['c', 'línea media']] },
    ],
    ejemplos: [
      { titulo: 'Parábola con dos raíces', texto: 'Para $f(x)=x^2-4x+3$ halla las raíces y el vértice.', pasos: ['$\\Delta=(-4)^2-4\\cdot1\\cdot3=4>0$: dos raíces.', '$x=\\frac{4\\pm2}{2}$, o sea $x=1$ y $x=3$.', 'Vértice: $x_v=\\frac{4}{2}=2$, $y_v=4-8+3=-1$. Está justo entre las raíces.'] },
      { titulo: 'Sin raíces', texto: '¿Corta el eje $x$ la parábola $f(x)=x^2+2$?', pasos: ['$\\Delta=0-4\\cdot1\\cdot2=-8<0$.', 'Como $a>0$ y el mínimo está en $y=2$, la curva queda siempre por encima del eje: no hay raíces.'] },
    ],
    errores: [
      { mito: '«El vértice es donde la parábola corta el eje y».', realidad: 'Corta el eje $y$ en $c$. El vértice está en $x=-b/(2a)$ y es el punto más bajo (o más alto).' },
      { mito: '«Cambiar $c$ hace la parábola más angosta».', realidad: 'Solo la sube o la baja. El ancho lo controla $a$.' },
      { mito: '«Una exponencial puede tocar el eje $x$».', realidad: '$ae^{bx}$ se acerca al eje (asíntota) pero nunca lo toca, salvo que $c$ la haya movido.' },
    ],
    saber11: 'Si te dan una gráfica y piden la fórmula, usa los puntos que ves: el corte con $y$ te da $c$ (o $b$ en la recta) y las raíces te dan los factores. Revisa siempre el signo de $a$: abre hacia arriba o hacia abajo.',
  },
  presets: [
    { id: 'recta', label: 'Una recta', desc: '$f(x)=2x-1$: pendiente 2 y corte con $y$ en $-1$. Raíz en $x=0{,}5$.', params: { family: 1, a: 2, b: -1, c: 0, ...P0 } },
    { id: 'parabola', label: 'Parábola con dos raíces', desc: '$x^2-4x+3$ corta el eje en $x=1$ y $x=3$ y tiene vértice en $(2,-1)$.', params: { family: 2, a: 1, b: -4, c: 3, ...P0 } },
    { id: 'abajo', label: 'Parábola hacia abajo', desc: 'Con $a=-1$ la parábola abre hacia abajo: el vértice es un máximo, en $(1,4)$.', params: { family: 2, a: -1, b: 2, c: 3, ...P0 } },
    { id: 'sin', label: 'Parábola sin raíces', desc: '$x^2+2$ nunca toca el eje $x$ porque el mínimo está en $y=2$.', params: { family: 2, a: 1, b: 0, c: 2, ...P0 } },
    { id: 'exp', label: 'Crecimiento exponencial', desc: '$e^{0{,}5x}$ crece cada vez más rápido y tiene el eje $x$ como asíntota.', params: { family: 3, a: 1, b: 0.5, c: 0, ...P0 } },
    { id: 'onda', label: 'Una onda', desc: '$3\\sin(2x)$: amplitud 3 y periodo $\\pi\\approx3{,}14$.', params: { family: 4, a: 3, b: 2, c: 0, ...P0 } },
  ],
  experiments: [
    { id: 'c-sube', titulo: 'Subir la parábola', setup: { family: 2, a: 1, b: -4, c: 3, ...P0 }, cambio: { c: 5 },
      pregunta: 'En $x^2-4x+c$ subes $c$ de $3$ a $5$. La parábola ahora corta el eje $x$ en...',
      opciones: ['Dos puntos', 'Un punto', 'Ningún punto'], correcta: 2,
      explicacion: '$\\Delta=16-20=-4<0$. Al subir la parábola, su mínimo ($y=1$) queda por encima del eje.',
      check: (b, a) => b.num_raices === 2 && a.num_raices === 0 },
    { id: 'b-vertice', titulo: 'Mover el vértice', setup: { family: 2, a: 1, b: -4, c: 3, ...P0 }, cambio: { b: -2 },
      pregunta: 'Cambias $b$ de $-4$ a $-2$ (con $a=1$). El vértice pasa a estar en $x=$...',
      opciones: ['2 (no cambia)', '1', '-1'], correcta: 1,
      explicacion: '$x_v=-\\frac{b}{2a}=\\frac{2}{2}=1$. Cambiar $b$ desplaza el vértice hacia la derecha o la izquierda.',
      check: (b, a) => near(b.vertice_x, 2, 1e-9) && near(a.vertice_x, 1, 1e-9) },
    { id: 'b-recta', titulo: 'El corte de la recta', setup: { family: 1, a: 2, b: -1, c: 0, ...P0 }, cambio: { b: 3 },
      pregunta: 'En $y=2x+b$ cambias $b$ de $-1$ a $3$. ¿Qué cambia?',
      opciones: ['La pendiente', 'El corte con el eje y: pasa de −1 a 3', 'Nada'], correcta: 1,
      explicacion: '$b$ es $f(0)$: la recta sube paralela a sí misma. La pendiente $a=2$ no cambia.',
      check: (b, a) => near(b.intercepto_y, -1, 1e-9) && near(a.intercepto_y, 3, 1e-9) },
    { id: 'c-exp', titulo: 'Desplazar la exponencial', setup: { family: 3, a: 1, b: 1, c: 0, ...P0 }, cambio: { c: 2 },
      pregunta: 'En $e^{x}+c$ cambias $c$ de $0$ a $2$. La gráfica...',
      opciones: ['Se desplaza 2 hacia arriba (corta en y = 3)', 'Se estira al doble', 'Se desplaza 2 a la derecha'], correcta: 0,
      explicacion: 'Sumar $c$ sube toda la curva. El corte con $y$ pasa de $e^0=1$ a $1+2=3$, y la asíntota deja de ser el eje $x$ y pasa a $y=2$.',
      check: (b, a) => near(b.intercepto_y, 1, 1e-9) && near(a.intercepto_y, 3, 1e-9) },
    { id: 'b-onda', titulo: 'Frecuencia de la onda', setup: { family: 4, a: 3, b: 1, c: 0, ...P0 }, cambio: { b: 2 },
      pregunta: 'En $3\\sin(bx)$ duplicas $b$ de $1$ a $2$. La onda...',
      opciones: ['Se hace el doble de alta', 'Oscila el doble de rápido (más ciclos)', 'Se desplaza a la derecha'], correcta: 1,
      explicacion: 'El periodo es $2\\pi/b$: se reduce a la mitad. Entre $-10$ y $10$ la onda corta el eje 13 veces en vez de 7.',
      check: (b, a) => b.num_raices === 7 && a.num_raices === 13 },
  ],
  solution: (p, m) => {
    const a = +p.a, b = +p.b, c = +p.c, fam = +p.family;
    if (String(p.custom ?? '').trim()) return [
      { t: 'Función propia', tex: `\\text{${String(p.custom).replace(/[{}\\^_]/g, ' ')}}`, nota: 'Prueba valores de $x$ en la tabla y busca dónde cambia el signo de $f(x)$: ahí hay una raíz.' },
      { t: 'Lo que midió la simulación', tex: `f(0)=${n(m.intercepto_y)}\\qquad \\text{raíces en }[-10,10]:\;${n(m.num_raices, 0)}` },
    ];
    if (fam === 1) return [
      { t: 'Identifica pendiente y corte', tex: `a=${n(a)}\;(\\text{pendiente})\\qquad b=${n(b)}\;(f(0))` },
      { t: 'Raíz: resuelve f(x)=0', tex: a ? `${n(a)}x${sg(b)}=0\;\\Rightarrow\;x=-\\frac{b}{a}=${n(-b / a)}` : `0\\cdot x${sg(b)}=0\;\\text{(constante)}`, nota: a ? 'La recta corta el eje $x$ en un solo punto.' : 'Con $a=0$ es una recta horizontal: o nunca corta el eje o es el eje.' },
    ];
    if (fam === 2) {
      if (!a) return [{ t: 'Con a = 0 ya no es parábola', tex: `f(x)=${n(b)}x${sg(c)}`, nota: 'Es una recta. Sube $a$ para recuperar la parábola.' }];
      const D = b * b - 4 * a * c, xv = -b / (2 * a), yv = a * xv * xv + b * xv + c;
      const steps = [
        { t: 'Identifica los coeficientes', tex: `a=${n(a)},\;b=${n(b)},\;c=${n(c)}`, nota: a > 0 ? 'Como $a>0$, abre hacia arriba: el vértice es un mínimo.' : 'Como $a<0$, abre hacia abajo: el vértice es un máximo.' },
        { t: 'Corte con el eje y', tex: `f(0)=c=${n(c)}` },
        { t: 'Vértice', tex: `x_v=-\\frac{b}{2a}=${n(xv)}\\qquad y_v=f(x_v)=${n(yv)}` },
        { t: 'Discriminante', tex: `\\Delta=b^2-4ac=${n(b)}^2-4(${n(a)})(${n(c)})=${n(D)}`, nota: near(D, 0, 1e-9) ? '$\\Delta=0$: una sola raíz (el vértice toca el eje).' : D > 0 ? '$\\Delta>0$: dos raíces distintas.' : '$\\Delta<0$: no hay raíces reales.' },
      ];
      if (D >= -1e-9) { const sq = Math.sqrt(Math.max(0, D)); steps.push({ t: 'Raíces', tex: `x=\\frac{${n(-b)}\\pm\\sqrt{${n(Math.max(0, D))}}}{${n(2 * a)}}\;\\Rightarrow\;x_1=${n((-b - sq) / (2 * a))},\;x_2=${n((-b + sq) / (2 * a))}`, nota: 'Se obtienen con la fórmula general.' }); }
      return steps;
    }
    if (fam === 3) return [
      { t: 'Corte con y', tex: `f(0)=a\\,e^{0}+c=${n(a)}+${n(c)}=${n(a + c)}` },
      { t: 'Asíntota', tex: `y=c=${n(c)}`, nota: 'La curva se acerca a esa recta horizontal sin tocarla.' },
      { t: 'Raíz (si existe)', tex: a * -c > 0 && b ? `x=\\frac{1}{b}\\ln\\!\\left(-\\frac{c}{a}\\right)=${n(Math.log(-c / a) / b)}` : '\\text{no corta el eje }x', nota: 'Solo hay raíz si $-c/a>0$.' },
    ];
    return [
      { t: 'Amplitud', tex: `|a|=${n(Math.abs(a))}`, nota: 'Qué tanto sube y baja respecto a la línea media.' },
      { t: 'Periodo', tex: b ? `T=\\frac{2\\pi}{|b|}=${n((2 * Math.PI) / Math.abs(b), 3)}` : '\\text{(b = 0: constante)}' },
      { t: 'Línea media y rango', tex: `y=${n(c)}\\qquad y\\in[${n(c - Math.abs(a))},\\,${n(c + Math.abs(a))}]` },
    ];
  },
  compare: (p, m) => {
    const a = +p.a, b = +p.b, c = +p.c, fam = +p.family;
    if (String(p.custom ?? '').trim()) return [];
    if (fam === 1 && a) return [{ label: 'Raíz −b/a', teoria: -b / a, sim: m.raiz_1 }];
    if (fam === 2 && a) {
      const D = b * b - 4 * a * c, rows = [{ label: 'Vértice x', teoria: -b / (2 * a), sim: m.vertice_x }, { label: 'Vértice y', teoria: c - (b * b) / (4 * a), sim: m.vertice_y }];
      if (D > 1e-9) { const r = [(-b - Math.sqrt(D)) / (2 * a), (-b + Math.sqrt(D)) / (2 * a)].sort((x, y) => x - y); rows.push({ label: 'Raíz 1', teoria: r[0], sim: m.raiz_1 }, { label: 'Raíz 2', teoria: r[1], sim: m.raiz_2 }); }
      return rows;
    }
    return [];
  },
  insight: (p, m) => {
    const fam = +p.family, a = +p.a, b = +p.b, c = +p.c;
    if (String(p.custom ?? '').trim()) return `Tu función corta el eje $x$ en ${n(m.num_raices, 0)} punto(s) dentro de $[-10,10]$.`;
    if (fam === 2 && a) { const D = b * b - 4 * a * c; return `${a > 0 ? 'Abre hacia arriba' : 'Abre hacia abajo'}. $\\Delta=${n(D)}$: ${D > 1e-9 ? 'dos raíces' : near(D, 0, 1e-9) ? 'una raíz' : 'ninguna raíz'}.`; }
    if (fam === 1) return a > 0 ? 'Pendiente positiva: la recta sube.' : a < 0 ? 'Pendiente negativa: la recta baja.' : 'Pendiente cero: recta horizontal.';
    if (fam === 3) return b > 0 ? 'Con $b>0$ crece sin parar hacia la derecha.' : 'Con $b<0$ decrece y se acerca a la asíntota.';
    return `Periodo $${b ? n((2 * Math.PI) / Math.abs(b), 2) : '∞'}$ y amplitud $${n(Math.abs(a))}$.`;
  },
  view({ ctx, w, h, state: s, pointer }) {
    gridFill(ctx, w, h, 24);
    const sc = 24, ox = w / 2, oy = h / 2, X = (x: number) => ox + x * sc, Y = (y: number) => oy - y * sc;
    const xm = ox / sc, ym = oy / sc;
    // ejes y marcas
    ctx.strokeStyle = INK; ctx.lineWidth = 1.6; ctx.beginPath(); ctx.moveTo(0, oy); ctx.lineTo(w, oy); ctx.moveTo(ox, 0); ctx.lineTo(ox, h); ctx.stroke();
    const st = niceStep(2 * xm, 10);
    for (let x = Math.ceil(-xm / st) * st; x <= xm; x += st) if (Math.abs(x) > 1e-9) { ctx.beginPath(); ctx.moveTo(X(x), oy - 4); ctx.lineTo(X(x), oy + 4); ctx.stroke(); mono(ctx, String(+x.toFixed(2)), X(x), oy + 17, 'center', 10); }
    for (let y = Math.ceil(-ym / st) * st; y <= ym; y += st) if (Math.abs(y) > 1e-9) { ctx.beginPath(); ctx.moveTo(ox - 4, Y(y)); ctx.lineTo(ox + 4, Y(y)); ctx.stroke(); mono(ctx, String(+y.toFixed(2)), ox - 8, Y(y) + 4, 'right', 10); }
    label(ctx, 'x', w - 12, oy - 8, 'right', 13, MUT); label(ctx, 'y', ox + 10, 16, 'left', 13, MUT);
    if (s.error) { label(ctx, `Revisa tu fórmula: ${s.error}`, 16, 48, 'left', 14, COLORS[4]); return; }
    // guías según familia
    const custom = false; void custom;
    ctx.setLineDash([6, 5]); ctx.lineWidth = 1.3; ctx.strokeStyle = 'rgba(234,243,255,.45)';
    if (Number.isFinite(s.vx) && s.family === 2) { ctx.beginPath(); ctx.moveTo(X(s.vx), 0); ctx.lineTo(X(s.vx), h); ctx.stroke(); }
    if (s.family === 3) { ctx.beginPath(); ctx.moveTo(0, Y(s.c)); ctx.lineTo(w, Y(s.c)); ctx.stroke(); }
    if (s.family === 4) { ctx.beginPath(); ctx.moveTo(0, Y(s.c)); ctx.lineTo(w, Y(s.c)); ctx.stroke(); }
    ctx.setLineDash([]);
    // curva
    ctx.save(); ctx.beginPath(); ctx.rect(0, 0, w, h); ctx.clip();
    ctx.strokeStyle = COLORS[0]; ctx.lineWidth = 3.2; ctx.lineJoin = 'round'; ctx.beginPath();
    let pen = false;
    for (let i = 0; i <= 900; i++) {
      const x = -xm + (2 * xm * i) / 900, y = s.fn(x);
      if (!Number.isFinite(y) || Math.abs(y) > 400) { pen = false; continue; }
      pen ? ctx.lineTo(X(x), Y(y)) : (ctx.moveTo(X(x), Y(y)), (pen = true));
    }
    ctx.stroke(); ctx.restore();
    // puntos notables
    const y0 = s.fn(0);
    if (Number.isFinite(y0) && Math.abs(y0) < ym) { ctx.fillStyle = COLORS[2]; ctx.beginPath(); ctx.arc(X(0), Y(y0), 5.5, 0, 7); ctx.fill(); callout(ctx, X(0), Y(y0), X(0) + 38, Y(y0) + (y0 > 0 ? 34 : -34), `corte con y: ${n(y0, 2)}`, COLORS[2], 16); }
    s.roots.forEach((r, i) => { ctx.fillStyle = PEN; ctx.strokeStyle = INK; ctx.lineWidth = 1.5; ctx.beginPath(); ctx.arc(X(r), Y(0), 6, 0, 7); ctx.fill(); ctx.stroke(); if (i < 4) mono(ctx, `x=${n(r, 2)}`, X(r), Y(0) + (i % 2 ? -14 : 24), 'center', 11, PEN); });
    if (Number.isFinite(s.vx) && Math.abs(s.vy) < ym) { ctx.fillStyle = COLORS[3]; ctx.strokeStyle = INK; ctx.beginPath(); ctx.rect(X(s.vx) - 5.5, Y(s.vy) - 5.5, 11, 11); ctx.fill(); ctx.stroke(); callout(ctx, X(s.vx), Y(s.vy), X(s.vx) + 46, Y(s.vy) + (s.a > 0 ? 30 : -30), `vértice (${n(s.vx, 1)}; ${n(s.vy, 1)})`, COLORS[3], 16); }
    if (s.family === 3) hand(ctx, `asíntota y = ${n(s.c)}`, 14, Y(s.c) - 8, 'left', 16, MUT);
    if (s.family === 4) hand(ctx, `línea media y = ${n(s.c)}`, 14, Y(s.c) - 8, 'left', 16, MUT);
    // cursor
    if (pointer) {
      const x = (pointer.x - ox) / sc, y = s.fn(x);
      if (Number.isFinite(y) && Math.abs(y) < ym) { ctx.fillStyle = INK; ctx.beginPath(); ctx.arc(X(x), Y(y), 4, 0, 7); ctx.fill(); mono(ctx, `(${n(x, 2)} ; ${n(y, 2)})`, Math.min(w - 80, X(x) + 10), Y(y) - 10, 'left', 12, INK); }
    }
    label(ctx, s.expr, 14, 24, 'left', 15, INK);
    hand(ctx, 'pasa el cursor sobre la curva', w - 12, h - 12, 'right', 16, MUT);
  },
};
