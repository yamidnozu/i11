import { gridFill, niceStep, label, mono, hand, COLORS, INK, MUT, PEN } from '../render/plot';
import type { Extra } from '../core/types';
import { theoretical, type PrState } from '../sims/probability';
import { n } from './util';

const ways = (s: number) => 6 - Math.abs(s - 7);

export const probabilityExtra: Extra<PrState> = {
  size: { width: 800, height: 380 },
  readouts: ['lanzamientos', 'desviacion_max'],
  paramHints: {
    modo: 'Un dado tiene 6 resultados igual de probables. La suma de dos dados tiene 11 resultados que NO son igual de probables.',
    N: 'Cuántas veces se lanza en total. Más lanzamientos → las barras se acercan más a la teoría.',
  },
  learn: {
    resumen: 'La probabilidad es una predicción; los lanzamientos son la prueba. Con pocos lanzamientos el azar engaña, con muchos se acerca a la teoría.',
    objetivos: [
      'Calcular probabilidades clásicas contando casos.',
      'Distinguir probabilidad teórica de frecuencia observada.',
      'Entender la ley de los grandes números.',
    ],
    idea: [
      'La **probabilidad teórica** de un suceso es $\\frac{\\text{casos favorables}}{\\text{casos posibles}}$ cuando todos los casos son igual de probables. En un dado, cada cara tiene $\\frac16$. Con dos dados hay $36$ combinaciones: la suma $7$ aparece en $6$ de ellas, pero la suma $2$ solo en una.',
      'La **frecuencia observada** es lo que realmente sale: $\\frac{\\text{veces que ocurrió}}{\\text{lanzamientos}}$. Con pocos lanzamientos puede alejarse mucho; con miles, se acerca a la teoría. Eso es la **ley de los grandes números**. Pero ojo: no «corrige» el pasado, solo lo diluye.',
    ],
    analogia: 'Si lanzas una moneda 10 veces, ver 7 caras no sorprende. Si la lanzas 10 000 veces y sale 70 % cara, algo raro pasa. El azar es ruidoso al principio y se calma con el tiempo.',
    formulas: [
      { tex: 'P(A)=\\frac{\\text{casos favorables}}{\\text{casos posibles}}', nombre: 'Probabilidad clásica', vars: [['P(A)', 'entre 0 y 1'], ['0', 'imposible'], ['1', 'seguro']] },
      { tex: 'P(\\text{suma}=s)=\\frac{6-|s-7|}{36}', nombre: 'Suma de dos dados', vars: [['s', 'valor de la suma, de 2 a 12'], ['6-|s-7|', 'formas de obtener esa suma']] },
      { tex: '\\sigma_f=\\sqrt{\\frac{p(1-p)}{n}}', nombre: 'Error típico de la frecuencia', vars: [['p', 'probabilidad teórica'], ['n', 'lanzamientos']] },
      { tex: 'P(A\\text{ y }B)=P(A)\\cdot P(B)', nombre: 'Sucesos independientes', vars: [['independientes', 'uno no afecta al otro']] },
    ],
    ejemplos: [
      { titulo: 'Suma 7 con dos dados', texto: '¿Cuál es la probabilidad de que la suma sea 7?', pasos: ['Casos posibles: $6\\cdot6=36$.', 'Casos favorables: $(1,6),(2,5),(3,4),(4,3),(5,2),(6,1)$, o sea $6$.', '$P=\\frac{6}{36}=\\frac16\\approx0{,}167$. Es la suma más probable.'] },
      { titulo: 'Cuántas veces esperar', texto: 'Si lanzas dos dados $3600$ veces, ¿cuántas veces esperas suma $7$?', pasos: ['Esperado $E=n\\cdot p=3600\\cdot\\frac16=600$.', 'Lo normal es que se desvíe unas decenas: el error típico es $\\sqrt{3600\\cdot\\frac16\\cdot\\frac56}\\approx22$.'] },
    ],
    errores: [
      { mito: '«Después de 5 caras seguidas, toca sello».', realidad: 'Cada lanzamiento es independiente: la moneda no tiene memoria.' },
      { mito: '«Todas las sumas de dos dados son igual de probables».', realidad: 'Hay 6 formas de sumar 7 pero solo 1 de sumar 2 o 12.' },
      { mito: '«Con 6 lanzamientos debe salir cada cara una vez».', realidad: 'Eso es muy improbable. La teoría se cumple en el largo plazo, no en pocos intentos.' },
    ],
    saber11: 'Cuenta casos con cuidado (tabla de doble entrada). Si dos sucesos son independientes, multiplica; si se excluyen, suma. Y no confundas «esperado» con «seguro»: la frecuencia solo se acerca a la probabilidad con muchos ensayos.',
  },
  presets: [
    { id: 'dado600', label: 'Un dado, 600 lanzamientos', desc: 'Debería salir cada cara unas 100 veces, pero verás diferencias visibles.', params: { modo: 1, N: 600 } },
    { id: 'dado10k', label: 'Un dado, 10 000 lanzamientos', desc: 'Las barras casi tocan la línea teórica de $1/6$. La desviación máxima baja a ~1 %.', params: { modo: 1, N: 10000 } },
    { id: 'dos2k', label: 'Dos dados, 2 000', desc: 'Se forma la «campana» con el 7 al centro. Los extremos (2 y 12) son raros.', params: { modo: 2, N: 2000 } },
    { id: 'dos20k', label: 'Dos dados, 20 000', desc: 'Con muchísimos lanzamientos las barras coinciden con la teoría casi exacta.', params: { modo: 2, N: 20000 } },
  ],
  experiments: [
    { id: 'lln', titulo: 'Más lanzamientos', setup: { modo: 1, N: 100 }, cambio: { N: 10000 },
      pregunta: 'Pasas de 100 a 10 000 lanzamientos de un dado. La diferencia entre cada frecuencia y $1/6$...',
      opciones: ['Crece', 'Se hace menor', 'Queda igual'], correcta: 1,
      explicacion: 'Ley de los grandes números: el error típico baja como $1/\\sqrt{n}$. Con 100 lanzamientos la desviación máxima ronda el 4 %; con 10 000, cerca del 1 %.',
      check: (b, a) => a.desviacion_max < b.desviacion_max && a.desviacion_max < 0.02 },
    { id: 'siete', titulo: 'La suma más probable', setup: { modo: 2, N: 2000 }, cambio: { modo: 2 },
      pregunta: 'Lanzas dos dados. ¿Qué suma es la más probable?',
      opciones: ['6', '7', '12'], correcta: 1,
      explicacion: 'El 7 se forma de 6 maneras: $(1,6),(2,5),(3,4),(4,3),(5,2),(6,1)$. Probabilidad $6/36=1/6$.',
      check: () => { const t = theoretical(2); return t.indexOf(Math.max(...t)) + 2 === 7 && Math.abs(Math.max(...t) - 1 / 6) < 1e-12; } },
    { id: 'extremo', titulo: 'Sumas extremas', setup: { modo: 2, N: 2000 }, cambio: { modo: 2 },
      pregunta: 'Con dos dados, ¿cuál es la probabilidad de que la suma sea exactamente 2?',
      opciones: ['1/12', '1/36', '1/6'], correcta: 1,
      explicacion: 'Solo hay una combinación, $(1,1)$, entre 36 posibles: $1/36\\approx2{,}8\\,\\%$.',
      check: () => Math.abs(theoretical(2)[0] - 1 / 36) < 1e-12 },
    { id: 'cara', titulo: 'Una cara concreta', setup: { modo: 1, N: 600 }, cambio: { modo: 1 },
      pregunta: 'En 6 000 lanzamientos de un dado, ¿cuántas veces esperas que salga el 3?',
      opciones: ['600', '1 000', '3 000'], correcta: 1,
      explicacion: 'Esperado $E=6000\\cdot\\frac16=1000$. En la práctica saldrá cerca de 1 000, no exactamente.',
      check: () => Math.abs(6000 * theoretical(1)[2] - 1000) < 1e-9 },
  ],
  solution: (p, m) => {
    const modo = +p.modo, N = +p.N;
    if (modo === 1) {
      const pr = 1 / 6, sd = Math.sqrt((pr * (1 - pr)) / N);
      return [
        { t: 'Casos', tex: '\\text{Posibles: }6\\qquad\\text{Favorables para cada cara: }1' },
        { t: 'Probabilidad teórica', tex: 'P(\\text{cada cara})=\\frac{1}{6}\\approx0{,}1667' },
        { t: 'Cuántas veces esperar', tex: `n\\cdot p=${n(N, 0)}\\cdot\\frac16=${n(N / 6, 1)}\;\\text{veces por cara}` },
        { t: 'Error típico de la frecuencia', tex: `\\sigma_f=\\sqrt{\\frac{p(1-p)}{n}}=\\sqrt{\\frac{(1/6)(5/6)}{${n(N, 0)}}}=${n(sd, 4)}`, nota: `Es normal ver diferencias de ±${n(sd * 100, 2)} puntos porcentuales. La desviación máxima observada fue ${n((m.desviacion_max || 0) * 100, 2)} %.` },
      ];
    }
    const p7 = 6 / 36, sd = Math.sqrt((p7 * (1 - p7)) / N);
    return [
      { t: 'Tabla de casos', tex: '6\\times6=36\;\\text{combinaciones posibles}', nota: 'Cada una $(d_1,d_2)$ es igual de probable.' },
      { t: 'Formas de obtener cada suma', tex: Array.from({ length: 11 }, (_, i) => `${i + 2}\\!:\\!${ways(i + 2)}`).join('\;\;'), nota: 'Crece hasta el 7 y luego baja: de ahí la forma de campana.' },
      { t: 'Probabilidades', tex: Array.from({ length: 11 }, (_, i) => `P(${i + 2})=\\frac{${ways(i + 2)}}{36}`).slice(0, 6).join('\;\;') + '\;\\dots', nota: 'La más alta es $P(7)=6/36=1/6$.' },
      { t: 'Esperado para el 7', tex: `n\\cdot\\frac16=${n(N / 6, 1)}\;\\text{veces}\\qquad\\sigma_f=${n(sd, 4)}`, nota: `La desviación máxima observada entre todas las barras fue ${n((m.desviacion_max || 0) * 100, 2)} %.` },
    ];
  },
  insight: (p, m) => {
    const N = +p.N;
    return m.lanzamientos >= N ? `Con ${n(N, 0)} lanzamientos, la barra más lejana de la teoría se desvía ${n((m.desviacion_max || 0) * 100, 2)} puntos porcentuales.` : 'Corre la simulación y mira cómo las barras se acercan a las líneas teóricas.';
  },
  view({ ctx, w, h, state: s }) {
    gridFill(ctx, w, h, 20);
    const th = theoretical(s.modo), k = th.length, first = s.modo === 1 ? 1 : 2;
    const pl = 56, pr = w - 24, pt = 52, pb = h - 70, bw = (pr - pl) / k;
    const ymax = Math.max(0.2, ...th) * 1.35, Y = (v: number) => pb - (v / ymax) * (pb - pt);
    ctx.strokeStyle = INK; ctx.lineWidth = 1.5; ctx.beginPath(); ctx.moveTo(pl, pt - 10); ctx.lineTo(pl, pb); ctx.lineTo(pr, pb); ctx.stroke();
    const sy = niceStep(ymax, 5);
    for (let v = 0; v <= ymax; v += sy) { ctx.strokeStyle = 'rgba(234,243,255,.14)'; ctx.beginPath(); ctx.moveTo(pl, Y(v)); ctx.lineTo(pr, Y(v)); ctx.stroke(); mono(ctx, `${n(v * 100, 0)}%`, pl - 8, Y(v) + 4, 'right', 10); }
    th.forEach((t, i) => {
      const x = pl + i * bw, f = s.n ? s.counts[i] / s.n : 0, sd = s.n ? Math.sqrt((t * (1 - t)) / s.n) : 0;
      // banda de ±2σ alrededor de la teoría
      if (s.n) { ctx.fillStyle = 'rgba(255,210,63,.16)'; ctx.fillRect(x + 3, Y(t + 2 * sd), bw - 6, Math.max(2, Y(t - 2 * sd) - Y(t + 2 * sd))); }
      ctx.fillStyle = 'rgba(92,225,255,.72)'; ctx.fillRect(x + 6, Y(f), bw - 12, pb - Y(f));
      ctx.strokeStyle = INK; ctx.lineWidth = 1; ctx.strokeRect(x + 6, Y(f), bw - 12, pb - Y(f));
      ctx.strokeStyle = PEN; ctx.lineWidth = 3; ctx.setLineDash([6, 4]); ctx.beginPath(); ctx.moveTo(x + 2, Y(t)); ctx.lineTo(x + bw - 2, Y(t)); ctx.stroke(); ctx.setLineDash([]);
      mono(ctx, String(i + first), x + bw / 2, pb + 18, 'center', 12, INK);
      mono(ctx, s.modo === 1 ? '1/6' : `${ways(i + 2)}/36`, x + bw / 2, Y(t) - 8, 'center', 10.5, PEN);
      if (s.n) mono(ctx, `${s.counts[i]}`, x + bw / 2, pb + 34, 'center', 10, MUT);
    });
    label(ctx, s.modo === 1 ? 'cara del dado' : 'suma de los dos dados', (pl + pr) / 2, h - 12, 'center', 12, MUT);
    mono(ctx, `n = ${s.n}`, pl + 4, 28, 'left', 15, INK);
    hand(ctx, 'línea punteada: probabilidad teórica', pr, 24, 'right', 18, PEN);
    hand(ctx, 'zona amarilla: dónde cae la barra el 95 % de las veces', pr, 44, 'right', 16, COLORS[1]);
    mono(ctx, s.n ? `desviación máxima: ${n(s.maxDev * 100, 2)} %` : '', pl + 4, 46, 'left', 12, COLORS[4]);
  },
};
