import { gridFill, niceStep, label, mono, hand, COLORS, INK, MUT, PEN } from '../render/plot';
import type { Extra } from '../core/types';
import type { StState } from '../sims/stats';
import { n, near } from './util';

const list = (a: number[], max = 8) => (a.length <= max ? a.map((v) => n(v)).join(',\\,') : `${a.slice(0, max - 2).map((v) => n(v)).join(',\\,')},\\dots,${n(a[a.length - 1])}`);

export const statsExtra: Extra<StState> = {
  size: { width: 760, height: 400 },
  readouts: ['media', 'mediana', 'desviacion'],
  paramHints: { data: 'Escribe los números separados por coma y con punto decimal (por ejemplo: 3.5, 4, 4.2). Máximo 40 datos.' },
  learn: {
    resumen: 'Resumir muchos datos en un número: ¿cuál es el típico?, ¿cuánto se dispersan? Cambia un dato y mira qué medida se mueve y cuál no.',
    objetivos: [
      'Calcular y distinguir media, mediana y moda.',
      'Medir la dispersión con rango y desviación estándar.',
      'Leer un diagrama de caja y detectar datos atípicos.',
    ],
    idea: [
      'La **media** es el punto de equilibrio de los datos (suma entre cantidad), la **mediana** es el dato del medio al ordenarlos y la **moda** es el que más se repite. Un valor extremo mueve mucho la media, pero casi no mueve la mediana.',
      'Para saber qué tan dispersos están, usa el **rango** (máximo − mínimo) o la **desviación estándar** (el promedio de las distancias a la media). El **diagrama de caja** reparte los datos en cuartos: la caja contiene la mitad central, y la línea interior es la mediana.',
    ],
    analogia: 'La media es como el punto de una regla donde se equilibra si pones pesos en cada dato: un peso muy lejos lo desplaza mucho. La mediana solo cuenta cuántos hay a cada lado.',
    formulas: [
      { tex: '\\bar{x}=\\frac{x_1+x_2+\\dots+x_n}{n}', nombre: 'Media', vars: [['x_i', 'cada dato'], ['n', 'cantidad de datos']] },
      { tex: '\\text{Mediana}=\\begin{cases}x_{(n+1)/2}&n\\text{ impar}\\\\ \\frac{x_{n/2}+x_{n/2+1}}{2}&n\\text{ par}\\end{cases}', nombre: 'Mediana (datos ordenados)', vars: [['x_{(k)}', 'dato en la posición k al ordenar']] },
      { tex: '\\sigma=\\sqrt{\\frac{\\sum (x_i-\\bar{x})^2}{n}}', nombre: 'Desviación estándar', vars: [['\\sigma', 'dispersión típica alrededor de la media']] },
      { tex: 'IQR=Q_3-Q_1\\qquad \\text{atípico si } x<Q_1-1{,}5\\,IQR\\ \\text{ó}\\ x>Q_3+1{,}5\\,IQR', nombre: 'Rango intercuartílico y atípicos', vars: [['Q_1,Q_3', 'primer y tercer cuartil']] },
    ],
    ejemplos: [
      { titulo: 'Cinco datos', texto: 'Para $2,3,3,4,8$ halla media, mediana y moda.', pasos: ['Media: $\\frac{2+3+3+4+8}{5}=\\frac{20}{5}=4$.', 'Mediana: ya está ordenado; el del medio es $3$.', 'Moda: el $3$ aparece dos veces.', 'La media (4) es mayor que la mediana (3) por culpa del $8$.'] },
      { titulo: 'Efecto de un atípico', texto: 'Cambias el $8$ por $80$.', pasos: ['Nueva media: $\\frac{2+3+3+4+80}{5}=18{,}4$. ¡Se multiplicó por 4,6!', 'Mediana: sigue siendo $3$.', 'Por eso se usa la mediana para sueldos o precios de vivienda: no se deja engañar por unos pocos valores enormes.'] },
    ],
    errores: [
      { mito: '«La media siempre representa bien al grupo».', realidad: 'Con datos muy desiguales o atípicos, la mediana describe mejor lo típico.' },
      { mito: '«Si sumo 10 a todos los datos, la dispersión sube».', realidad: 'La desviación no cambia: todos se desplazan igual. Solo cambia la media y la mediana.' },
      { mito: '«Si multiplico los datos por 2, la desviación se mantiene».', realidad: 'Se duplica (y la varianza se cuadruplica).' },
    ],
    saber11: 'Fíjate en qué pregunta el enunciado: «el valor central» (mediana), «el más frecuente» (moda), «el promedio» (media). Si hay un valor muy distinto, recuerda que la media se desplaza hacia él. En una tabla de frecuencias, usa la frecuencia como «cuántas veces» al promediar.',
  },
  presets: [
    { id: 'base', label: 'Cinco datos', desc: '$2,3,3,4,8$: media 4, mediana 3, moda 3. La media se ve arrastrada por el 8.', params: { data: '2, 3, 3, 4, 8' } },
    { id: 'atipico', label: 'Un atípico enorme', desc: 'El 40 dispara la media (9) pero la mediana sigue en 5. El diagrama de caja marca el 40 como atípico.', params: { data: '3, 4, 4, 5, 5, 6, 40' } },
    { id: 'simetrico', label: 'Datos simétricos', desc: 'Con $1,\\dots,7$ la media y la mediana coinciden en 4.', params: { data: '1, 2, 3, 4, 5, 6, 7' } },
    { id: 'bimodal', label: 'Dos modas', desc: 'Dos valores se repiten igual: 1 y 5. La media (3,7) no describe a nadie.', params: { data: '1, 1, 1, 5, 5, 5, 9' } },
    { id: 'notas', label: 'Notas de un curso', desc: 'Notas entre 3 y 5: media cerca de 4,3, poca dispersión.', params: { data: '3.2, 3.8, 4.0, 4.0, 4.5, 4.7, 5.0' } },
    { id: 'iguales', label: 'Sin dispersión', desc: 'Todos iguales: la desviación estándar es 0.', params: { data: '10, 10, 10, 10' } },
  ],
  experiments: [
    { id: 'atipico', titulo: 'El dato extremo', setup: { data: '2, 3, 3, 4, 8' }, cambio: { data: '2, 3, 3, 4, 80' },
      pregunta: 'Cambias el 8 por 80. ¿Qué medida casi no se mueve?',
      opciones: ['La media', 'La mediana', 'Ambas igual'], correcta: 1,
      explicacion: 'La media pasa de 4 a 18,4, pero la mediana sigue en 3. Solo cuenta el orden, no qué tan lejos está el extremo.',
      check: (b, a) => a.mediana === b.mediana && a.media > b.media * 4 },
    { id: 'suma', titulo: 'Sumar a todos', setup: { data: '2, 3, 3, 4, 8' }, cambio: { data: '12, 13, 13, 14, 18' },
      pregunta: 'Sumas 10 a cada dato. La desviación estándar...',
      opciones: ['Sube 10', 'No cambia', 'Se duplica'], correcta: 1,
      explicacion: 'Todos los datos se desplazan lo mismo, así que las distancias entre ellos y a la media no cambian. La media sí sube 10.',
      check: (b, a) => near(a.desviacion, b.desviacion, 1e-9) && near(a.media - b.media, 10, 1e-9) },
    { id: 'multiplica', titulo: 'Multiplicar por 2', setup: { data: '2, 3, 3, 4, 8' }, cambio: { data: '4, 6, 6, 8, 16' },
      pregunta: 'Multiplicas todos los datos por 2. La desviación estándar...',
      opciones: ['Se duplica', 'Queda igual', 'Se cuadruplica'], correcta: 0,
      explicacion: 'Las distancias se duplican, por lo que $\\sigma$ se duplica (la varianza $\\sigma^2$ sí se cuadruplica). También se duplican la media y el rango.',
      check: (b, a) => near(a.desviacion / b.desviacion, 2, 1e-9) && near(a.rango / b.rango, 2, 1e-9) },
    { id: 'repetir', titulo: 'Repetir un dato', setup: { data: '2, 3, 3, 4, 8' }, cambio: { data: '2, 3, 3, 3, 3, 4, 8' },
      pregunta: 'Agregas dos veces más el dato 3. ¿Qué pasa con la moda?',
      opciones: ['Sigue siendo 3', 'Cambia a 8', 'Desaparece'], correcta: 0,
      explicacion: 'La moda es el valor más frecuente: ahora el 3 aparece cuatro veces. La mediana también sigue siendo 3.',
      check: (b, a) => a.moda === 3 && b.moda === 3 && a.mediana === 3 },
  ],
  solution: (p, m) => {
    const d = String(p.data).split(/[\s,;]+/).filter(Boolean).map(Number);
    if (!d.length || d.some((v) => !Number.isFinite(v))) return [{ t: 'Revisa los datos', tex: '\\text{Escribe números separados por coma}' }];
    const s = [...d].sort((a, b) => a - b), N = d.length, mean = d.reduce((a, b) => a + b, 0) / N;
    const dev = s.map((v) => (v - mean) ** 2), sd = Math.sqrt(dev.reduce((a, b) => a + b, 0) / N);
    return [
      { t: 'Ordena los datos', tex: list(s, 12), nota: `Son ${N} datos.` },
      { t: 'Media', tex: `\\bar{x}=\\frac{${list(s)}}{${N}}=\\frac{${n(d.reduce((a, b) => a + b, 0))}}{${N}}=${n(mean)}`.replace(/,\\,/g, '+') },
      { t: 'Mediana', tex: N % 2 ? `\\text{posición }\\frac{${N}+1}{2}=${(N + 1) / 2}\;\\Rightarrow\;${n(m.mediana)}` : `\\frac{x_{${N / 2}}+x_{${N / 2 + 1}}}{2}=\\frac{${n(s[N / 2 - 1])}+${n(s[N / 2])}}{2}=${n(m.mediana)}` },
      { t: 'Moda', tex: Number.isFinite(m.moda) ? `\\text{Moda}=${n(m.moda)}` : '\\text{Todos aparecen una sola vez: no hay moda}' },
      { t: 'Rango', tex: `${n(s[N - 1])}-${n(s[0])}=${n(m.rango)}` },
      { t: 'Desviación estándar', tex: `\\sigma=\\sqrt{\\frac{${dev.slice(0, 5).map((v) => n(v)).join('+')}${N > 5 ? '+\\dots' : ''}}{${N}}}=\\sqrt{${n(dev.reduce((a, b) => a + b, 0) / N, 3)}}=${n(sd, 3)}`, nota: 'Cada sumando es $(x-\\bar{x})^2$.' },
      { t: 'Cuartiles', tex: `Q_1=${n(m.q1)}\\qquad Q_3=${n(m.q3)}\\qquad IQR=${n(m.q3 - m.q1)}`, nota: `Un dato es atípico si cae fuera de $[${n(m.q1 - 1.5 * (m.q3 - m.q1))},\\,${n(m.q3 + 1.5 * (m.q3 - m.q1))}]$.` },
    ];
  },
  insight: (_p, m) => {
    if (!Number.isFinite(m.media)) return 'Escribe algunos números para empezar.';
    const diff = m.media - m.mediana, tol = (m.rango || 1) * 0.05;
    return Math.abs(diff) < tol ? 'La media y la mediana casi coinciden: los datos son más o menos simétricos.' : diff > 0 ? 'La media es mayor que la mediana: hay valores altos que la arrastran hacia arriba.' : 'La media es menor que la mediana: hay valores bajos que la arrastran hacia abajo.';
  },
  view({ ctx, w, h, state: s }) {
    gridFill(ctx, w, h, 20);
    if (s.error || !s.stats) { label(ctx, s.error ?? 'Escribe datos', 20, 44, 'left', 15, COLORS[4]); return; }
    const st = s.stats, d = s.data, lo = Math.min(...d), hi = Math.max(...d), pad = (hi - lo || 2) * 0.1 + 0.5;
    const pl = 56, pr = w - 40, X = (v: number) => pl + ((v - (lo - pad)) / (hi - lo + 2 * pad)) * (pr - pl);
    const base = 214, r = 8.5, step = 2 * r + 1;
    // eje
    ctx.strokeStyle = INK; ctx.lineWidth = 1.6; ctx.beginPath(); ctx.moveTo(pl - 10, 330); ctx.lineTo(pr + 10, 330); ctx.stroke();
    const sx = niceStep(hi - lo + 2 * pad, 8);
    for (let v = Math.ceil((lo - pad) / sx) * sx; v <= hi + pad; v += sx) { ctx.beginPath(); ctx.moveTo(X(v), 330); ctx.lineTo(X(v), 336); ctx.stroke(); mono(ctx, String(+v.toFixed(2)), X(v), 352, 'center', 10.5); }
    // desviación estándar
    ctx.fillStyle = 'rgba(110,240,176,.12)'; ctx.fillRect(X(st.mean - st.sd), 28, X(st.mean + st.sd) - X(st.mean - st.sd), 284);
    // puntos apilados por posición de píxel
    const bins = new Map<number, number>();
    const fences = [st.q1 - 1.5 * (st.q3 - st.q1), st.q3 + 1.5 * (st.q3 - st.q1)];
    [...d].sort((a, b) => a - b).forEach((v) => {
      const b = Math.round(X(v) / (2 * r)), k = bins.get(b) || 0; bins.set(b, k + 1);
      const out = v < fences[0] || v > fences[1];
      ctx.fillStyle = out ? COLORS[4] : COLORS[0]; ctx.strokeStyle = INK; ctx.lineWidth = 1.2; ctx.beginPath(); ctx.arc(X(v), base - r - k * step, r, 0, 7); ctx.fill(); ctx.stroke();
    });
    ctx.strokeStyle = MUT; ctx.lineWidth = 1; ctx.beginPath(); ctx.moveTo(pl - 10, base); ctx.lineTo(pr + 10, base); ctx.stroke();
    // mediana, media y moda
    ctx.strokeStyle = PEN; ctx.lineWidth = 2.4; ctx.beginPath(); ctx.moveTo(X(st.median), 36); ctx.lineTo(X(st.median), base + 4); ctx.stroke();
    hand(ctx, `mediana ${n(st.median, 2)}`, X(st.median) + 6, 44, 'left', 19, PEN);
    ctx.fillStyle = COLORS[2]; ctx.strokeStyle = INK; ctx.lineWidth = 1.4; ctx.beginPath(); ctx.moveTo(X(st.mean) - 10, base + 24); ctx.lineTo(X(st.mean) + 10, base + 24); ctx.lineTo(X(st.mean), base + 6); ctx.closePath(); ctx.fill(); ctx.stroke();
    hand(ctx, `media ${n(st.mean, 2)}`, X(st.mean), base + 44, 'center', 19, COLORS[2]);
    if (Number.isFinite(st.mode)) { ctx.strokeStyle = COLORS[3]; ctx.lineWidth = 2; ctx.setLineDash([4, 3]); ctx.beginPath(); ctx.arc(X(st.mode), base - r - ((bins.get(Math.round(X(st.mode) / (2 * r))) || 1) - 1) * step / 2, 20 + ((bins.get(Math.round(X(st.mode) / (2 * r))) || 1) - 1) * step / 2, 0, 7); ctx.stroke(); ctx.setLineDash([]); hand(ctx, `moda ${n(st.mode, 2)}`, X(st.mode), base - 2 * r - ((bins.get(Math.round(X(st.mode) / (2 * r))) || 1)) * step - 6, 'center', 17, COLORS[3]); }
    hand(ctx, `±1 desviación (${n(st.sd, 2)})`, X(st.mean + st.sd) - 6, 24, 'right', 16, COLORS[2]);
    // diagrama de caja
    const by = 286, bh = 26;
    const inside = d.filter((v) => v >= fences[0] && v <= fences[1]), wl = Math.min(...inside), wh = Math.max(...inside);
    ctx.strokeStyle = INK; ctx.lineWidth = 1.8; ctx.beginPath(); ctx.moveTo(X(wl), by); ctx.lineTo(X(st.q1), by); ctx.moveTo(X(st.q3), by); ctx.lineTo(X(wh), by); ctx.moveTo(X(wl), by - 9); ctx.lineTo(X(wl), by + 9); ctx.moveTo(X(wh), by - 9); ctx.lineTo(X(wh), by + 9); ctx.stroke();
    ctx.fillStyle = 'rgba(92,225,255,.28)'; ctx.fillRect(X(st.q1), by - bh / 2, X(st.q3) - X(st.q1), bh); ctx.strokeRect(X(st.q1), by - bh / 2, X(st.q3) - X(st.q1), bh);
    ctx.strokeStyle = PEN; ctx.lineWidth = 3; ctx.beginPath(); ctx.moveTo(X(st.median), by - bh / 2); ctx.lineTo(X(st.median), by + bh / 2); ctx.stroke();
    d.filter((v) => v < fences[0] || v > fences[1]).forEach((v) => { ctx.fillStyle = COLORS[4]; ctx.beginPath(); ctx.arc(X(v), by, 5, 0, 7); ctx.fill(); mono(ctx, 'atípico', X(v), by - 16, 'center', 10.5, COLORS[4]); });
    mono(ctx, `Q1 ${n(st.q1, 2)}`, X(st.q1), by + 30, 'center', 11, MUT); mono(ctx, `Q3 ${n(st.q3, 2)}`, X(st.q3), by + 30, 'center', 11, MUT);
    label(ctx, 'diagrama de caja', pl - 10, by - 20, 'left', 12, MUT);
    mono(ctx, `n = ${st.n}   rango = ${n(st.range, 2)}`, pr + 10, 20, 'right', 12, INK);
  },
};
