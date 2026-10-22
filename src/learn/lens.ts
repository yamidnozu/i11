import { gridFill, label, mono, hand, arrow, dim, COLORS, INK, MUT, PEN } from '../render/plot';
import type { Extra } from '../core/types';
import { thinLens, type LensState } from '../sims/lens';
import { n, near } from './util';

export const lensExtra: Extra<LensState> = {
  size: { width: 800, height: 380 },
  readouts: ['d_i', 'M', 'h_i'],
  paramHints: {
    f: 'La distancia focal manda: positiva = lente convergente (lupa), negativa = divergente.',
    d_o: 'Qué tan lejos de la lente pones el objeto. Prueba pasar por F y por 2F.',
    h_o: 'Tamaño del objeto. No cambia el tipo de imagen, solo la escala.',
  },
  learn: {
    resumen: 'Una lente forma imágenes con luz. Tres rayos «especiales» te dicen dónde queda la imagen y cómo es: real o virtual, derecha o invertida, grande o pequeña.',
    objetivos: [
      'Dibujar los tres rayos principales de una lente delgada.',
      'Calcular dónde se forma la imagen con $\\frac{1}{f}=\\frac{1}{d_o}+\\frac{1}{d_i}$.',
      'Describir la imagen según la posición del objeto respecto a $F$ y $2F$.',
    ],
    idea: [
      'Una lente **convergente** desvía los rayos paralelos hacia un punto, el foco $F$. Una **divergente** los abre como si vinieran de un foco al frente. Con la posición del objeto y esa distancia focal queda decidida toda la imagen.',
      'Si los rayos realmente se cruzan, la imagen es **real** (se puede proyectar en una pantalla) e invertida. Si solo parecen cruzarse al prolongarlos hacia atrás, es **virtual** (se ve a través de la lente, como con una lupa) y derecha.',
    ],
    analogia: 'Una lupa pegada a un texto lo agranda: es una imagen virtual. Si alejas la lupa y proyectas el sol en una hoja, formas una imagen real, pequeña y puesta al revés.',
    formulas: [
      { tex: '\\frac{1}{f}=\\frac{1}{d_o}+\\frac{1}{d_i}', nombre: 'Ecuación de la lente delgada', vars: [['f', 'distancia focal (+ convergente, − divergente)'], ['d_o', 'distancia del objeto a la lente'], ['d_i', 'distancia de la imagen (+ real, − virtual)']] },
      { tex: 'M=\\frac{h_i}{h_o}=-\\frac{d_i}{d_o}', nombre: 'Aumento', vars: [['M', 'negativo = invertida, positivo = derecha'], ['|M|>1', 'imagen agrandada']] },
    ],
    ejemplos: [
      { titulo: 'Un proyector', texto: 'Lente convergente de $f=10$ cm con el objeto a $d_o=15$ cm. ¿Dónde y cómo es la imagen?', pasos: ['$\\frac{1}{d_i}=\\frac{1}{10}-\\frac{1}{15}=\\frac{1}{30}$, así que $d_i=30$ cm (positiva: real).', '$M=-\\frac{30}{15}=-2$: invertida y del doble de tamaño.', 'El objeto está entre $F$ y $2F$, y la imagen sale más allá de $2F$.'] },
      { titulo: 'Una lupa', texto: 'La misma lente con el objeto a $d_o=6$ cm (dentro de $F$).', pasos: ['$\\frac{1}{d_i}=\\frac{1}{10}-\\frac{1}{6}=-\\frac{1}{15}$, o sea $d_i=-15$ cm.', 'Negativa: imagen virtual, al mismo lado que el objeto.', '$M=-\\frac{-15}{6}=+2{,}5$: derecha y aumentada.'] },
    ],
    errores: [
      { mito: '«Toda imagen de una lente sale invertida».', realidad: 'Solo las reales. Las virtuales (lupa, lente divergente) salen derechas.' },
      { mito: '«Una lente divergente puede dar una imagen real».', realidad: 'Con un objeto real, la divergente siempre da imagen virtual, derecha y reducida.' },
      { mito: '«Si el objeto está en el foco, la imagen es muy pequeña».', realidad: 'En $F$ los rayos salen paralelos: no hay imagen (queda en el infinito).' },
    ],
    saber11: 'Memoriza las zonas: más allá de $2F$ → imagen real, invertida y reducida (cámara). Entre $F$ y $2F$ → real, invertida y mayor (proyector). Dentro de $F$ → virtual, derecha y mayor (lupa). Si el signo de $d_i$ es negativo, es virtual.',
  },
  presets: [
    { id: 'camara', label: 'Cámara', desc: 'Con el objeto lejos ($d_o=25$ cm, $f=5$ cm) la imagen sale real, invertida y pequeña, justo lo que graba un sensor.', params: { f: 5, d_o: 25, h_o: 4 } },
    { id: 'proyector', label: 'Proyector', desc: 'Con $f=10$ y $d_o=15$ la imagen queda a 30 cm, invertida y del doble: sirve para proyectar sobre una pantalla.', params: { f: 10, d_o: 15, h_o: 4 } },
    { id: 'lupa', label: 'Lupa', desc: 'Objeto dentro del foco ($d_o=6$ cm, $f=10$): imagen virtual, derecha y 2,5 veces mayor.', params: { f: 10, d_o: 6, h_o: 4 } },
    { id: 'foco', label: 'Justo en el foco', desc: 'Con $d_o=f$ los rayos salen paralelos. No se forma imagen en ninguna parte.', params: { f: 10, d_o: 10, h_o: 4 } },
    { id: 'divergente', label: 'Lente divergente', desc: 'Con $f=-10$ la imagen es siempre virtual, derecha y más pequeña que el objeto.', params: { f: -10, d_o: 15, h_o: 4 } },
  ],
  experiments: [
    { id: 'acerca', titulo: 'Acercar el objeto', setup: { f: 10, d_o: 25, h_o: 4 }, cambio: { d_o: 15 },
      pregunta: 'Con $f=10$ cm, acercas el objeto de $25$ a $15$ cm. La imagen real...',
      opciones: ['Crece y se aleja de la lente', 'Se encoge y se acerca', 'Queda igual'], correcta: 0,
      explicacion: 'Pasa de $d_i=16{,}7$ cm ($M=-0{,}67$) a $d_i=30$ cm ($M=-2$). Al acercar el objeto hacia $F$, la imagen real se va lejos y se agranda.',
      check: (b, a) => Math.abs(a.M) > Math.abs(b.M) && a.d_i > b.d_i && near(a.d_i, 30, 0.01) },
    { id: 'dentro', titulo: 'Cruzar el foco', setup: { f: 10, d_o: 15, h_o: 4 }, cambio: { d_o: 6 },
      pregunta: 'Mueves el objeto de $15$ cm a $6$ cm ($f=10$). La imagen pasa de real e invertida a...',
      opciones: ['Real e invertida, aún mayor', 'Virtual, derecha y aumentada', 'Desaparece'], correcta: 1,
      explicacion: 'Al entrar dentro de $F$ los rayos ya no llegan a cruzarse: $d_i=-15$ cm (virtual) y $M=+2{,}5$.',
      check: (b, a) => b.d_i > 0 && a.d_i < 0 && a.M > 0 && near(a.M, 2.5, 0.01) },
    { id: 'dos-f', titulo: 'Justo a 2F', setup: { f: 10, d_o: 30, h_o: 4 }, cambio: { d_o: 20 },
      pregunta: 'Pones el objeto exactamente a $2F$ ($20$ cm, con $f=10$). El tamaño de la imagen es...',
      opciones: ['Mayor que el objeto', 'Igual al objeto', 'Menor que el objeto'], correcta: 1,
      explicacion: '$d_i=20$ cm y $M=-1$: imagen real, invertida y del mismo tamaño. Es el punto de cambio entre «reducida» y «aumentada».',
      check: (b, a) => near(a.M, -1, 1e-9) && near(a.d_i, 20, 1e-9) },
    { id: 'diverge', titulo: 'Lente divergente', setup: { f: -10, d_o: 30, h_o: 4 }, cambio: { d_o: 10 },
      pregunta: 'Con una lente divergente, acercas el objeto de $30$ a $10$ cm. La imagen...',
      opciones: ['Se vuelve real', 'Sigue siendo virtual, derecha y reducida', 'Se hace infinita'], correcta: 1,
      explicacion: 'Sigue virtual: $d_i$ pasa de $-7{,}5$ a $-5$ cm y $M$ de $0{,}25$ a $0{,}5$. Una divergente nunca da imagen real con un objeto real.',
      check: (b, a) => a.d_i < 0 && b.d_i < 0 && a.M > 0 && a.M < 1 && b.M < 1 },
  ],
  solution: (p) => {
    const s = thinLens(+p.f, +p.d_o, +p.h_o);
    if (!Number.isFinite(s.d_i)) return [
      { t: 'Ecuación de la lente', tex: `\\frac{1}{d_i}=\\frac{1}{f}-\\frac{1}{d_o}=\\frac{1}{${n(s.f)}}-\\frac{1}{${n(s.d_o)}}=0` },
      { t: 'Conclusión', tex: 'd_i\\to\\infty', nota: 'El objeto está en el foco: los rayos salen paralelos y no se forma imagen.' },
    ];
    return [
      { t: 'Despeja la distancia de la imagen', tex: `\\frac{1}{d_i}=\\frac{1}{f}-\\frac{1}{d_o}=\\frac{1}{${n(s.f)}}-\\frac{1}{${n(s.d_o)}}=${n(1 / s.d_i, 4)}`, nota: 'Usa f positiva para convergente y negativa para divergente.' },
      { t: 'Invierte', tex: `d_i=${n(s.d_i)}\;\\text{cm}`, nota: s.d_i > 0 ? 'Positiva: imagen **real**, al otro lado de la lente.' : 'Negativa: imagen **virtual**, del mismo lado que el objeto.' },
      { t: 'Aumento', tex: `M=-\\frac{d_i}{d_o}=-\\frac{${n(s.d_i)}}{${n(s.d_o)}}=${n(s.M, 3)}`, nota: s.M < 0 ? 'Negativo: invertida.' : 'Positivo: derecha.' },
      { t: 'Altura de la imagen', tex: `h_i=M\\,h_o=${n(s.M, 3)}\\cdot${n(s.h_o)}=${n(s.h_i)}\;\\text{cm}` },
      { t: 'Descripción', tex: `\\text{${s.tipo}}` },
    ];
  },
  compare: (p, m) => {
    const f = +p.f, d = +p.d_o, di = 1 / (1 / f - 1 / d);
    if (!Number.isFinite(di) || Math.abs(1 / f - 1 / d) < 1e-9) return [];
    return [
      { label: 'Distancia de la imagen (cm)', teoria: di, sim: m.d_i },
      { label: 'Aumento M', teoria: -di / d, sim: m.M },
    ];
  },
  insight: (p) => {
    const s = thinLens(+p.f, +p.d_o, +p.h_o), f = Math.abs(s.f);
    if (!Number.isFinite(s.d_i)) return 'Objeto en el foco: los rayos salen paralelos, no hay imagen.';
    if (s.f < 0) return 'Lente divergente: la imagen es virtual, derecha y reducida sin importar dónde pongas el objeto.';
    if (s.d_o > 2 * f) return 'Objeto más allá de $2F$: imagen real, invertida y reducida (como en una cámara).';
    if (near(s.d_o, 2 * f, 0.05)) return 'Objeto en $2F$: la imagen es real, invertida y del mismo tamaño.';
    if (s.d_o > f) return 'Objeto entre $F$ y $2F$: imagen real, invertida y mayor (como en un proyector).';
    return 'Objeto dentro de $F$: imagen virtual, derecha y mayor (como en una lupa).';
  },
  view({ ctx, w, h, state: s }) {
    gridFill(ctx, w, h, 20);
    const xr = 44, sc = (w - 40) / (2 * xr), cx = w / 2, cy = h / 2 + 22;
    const X = (x: number) => cx + x * sc, Y = (y: number) => cy - y * sc;
    const f = s.f, af = Math.abs(f), real = Number.isFinite(s.d_i) && s.d_i > 0, virt = Number.isFinite(s.d_i) && s.d_i < 0;
    const seg = (x0: number, y0: number, x1: number, y1: number) => { ctx.beginPath(); ctx.moveTo(X(x0), Y(y0)); ctx.lineTo(X(x1), Y(y1)); ctx.stroke(); };
    // eje y marcas
    ctx.strokeStyle = INK; ctx.lineWidth = 1.2; ctx.beginPath(); ctx.moveTo(14, cy); ctx.lineTo(w - 14, cy); ctx.stroke();
    for (let x = -40; x <= 40; x += 10) { if (!x) continue; ctx.beginPath(); ctx.moveTo(X(x), cy - 4); ctx.lineTo(X(x), cy + 4); ctx.stroke(); mono(ctx, String(Math.abs(x)), X(x), cy + 18, 'center', 10, MUT); }
    label(ctx, 'cm', w - 18, cy + 18, 'right', 11, MUT);
    // rayos
    const xe = xr + 3, xl = -xr - 3;
    ctx.save(); ctx.beginPath(); ctx.rect(8, 8, w - 16, h - 16); ctx.clip();
    ctx.lineWidth = 1.8; ctx.setLineDash([]);
    const ray = (c: string, pts: [number, number][], dashedBack?: [number, number][]) => {
      ctx.strokeStyle = c; ctx.setLineDash([]);
      for (let i = 0; i < pts.length - 1; i++) seg(pts[i][0], pts[i][1], pts[i + 1][0], pts[i + 1][1]);
      if (dashedBack) { ctx.setLineDash([5, 5]); seg(dashedBack[0][0], dashedBack[0][1], dashedBack[1][0], dashedBack[1][1]); ctx.setLineDash([]); }
    };
    const ho = s.h_o, tip = [-s.d_o, ho] as [number, number];
    ray(COLORS[2], [tip, [0, ho], [xe, ho * (1 - xe / f)]], virt ? [[0, ho], [s.d_i, s.h_i]] : undefined);
    ray(COLORS[3], [tip, [xe, (-ho / s.d_o) * xe]]);
    if (Math.abs(s.d_o - af) > 1e-6 || f < 0) {
      const yl = (-ho * f) / (s.d_o - f);
      ray(COLORS[4], [tip, [0, yl], [xe, yl]], virt ? [[0, yl], [s.d_i, s.h_i]] : undefined);
    }
    ctx.restore();
    // lente
    const hp = 150;
    ctx.strokeStyle = COLORS[0]; ctx.lineWidth = 3.4; ctx.beginPath(); ctx.moveTo(cx, cy - hp); ctx.lineTo(cx, cy + hp); ctx.stroke();
    ctx.lineWidth = 3;
    for (const sgn of [-1, 1]) {
      const ty = cy + sgn * hp, ds = (f > 0 ? -sgn : sgn) * 12;
      ctx.beginPath(); ctx.moveTo(cx - 9, ty + ds); ctx.lineTo(cx, ty); ctx.lineTo(cx + 9, ty + ds); ctx.stroke();
    }
    mono(ctx, f > 0 ? 'convergente' : 'divergente', cx, cy - hp - 10, 'center', 12, COLORS[0]);
    // focos
    for (const sgn of [-1, 1]) for (const k of [1, 2]) {
      const x = sgn * k * af; if (Math.abs(x) > xr) continue;
      ctx.fillStyle = COLORS[4]; ctx.beginPath(); ctx.arc(X(x), cy, k === 1 ? 4.5 : 3, 0, 7); ctx.fill();
      mono(ctx, k === 1 ? 'F' : '2F', X(x), cy - 10, 'center', 11, COLORS[4]);
    }
    // objeto e imagen
    arrow(ctx, X(-s.d_o), cy, X(-s.d_o), Y(ho), COLORS[0], 3.4);
    hand(ctx, 'objeto', X(-s.d_o), Y(ho) - 10, 'center', 18, COLORS[0]);
    if (Number.isFinite(s.d_i) && Math.abs(s.d_i) < xr + 2) {
      ctx.setLineDash(virt ? [6, 5] : []);
      arrow(ctx, X(s.d_i), cy, X(s.d_i), Y(s.h_i), PEN, 3.4);
      ctx.setLineDash([]);
      hand(ctx, virt ? 'imagen virtual' : 'imagen real', X(s.d_i), s.h_i > 0 ? Y(s.h_i) - 10 : Y(s.h_i) + 22, 'center', 18, PEN);
    }
    // cotas
    dim(ctx, X(-s.d_o), cy, X(0), cy, `dₒ = ${n(s.d_o, 1)} cm`, { off: 64, color: COLORS[0] });
    if (Number.isFinite(s.d_i) && Math.abs(s.d_i) < xr) dim(ctx, X(0), cy, X(s.d_i), cy, `dᵢ = ${n(s.d_i, 1)} cm`, { off: 92, color: PEN });
    // leyenda
    const leg: [string, string][] = [[COLORS[2], '① paralelo al eje → pasa por F'], [COLORS[3], '② por el centro → no se desvía'], [COLORS[4], '③ por F → sale paralelo']];
    leg.forEach(([c, t], i) => { ctx.strokeStyle = c; ctx.lineWidth = 2.4; ctx.beginPath(); ctx.moveTo(18, 22 + i * 18); ctx.lineTo(42, 22 + i * 18); ctx.stroke(); label(ctx, t, 50, 26 + i * 18, 'left', 11.5, INK); });
    mono(ctx, `f = ${n(f, 0)} cm   M = ${Number.isFinite(s.M) ? n(s.M, 2) : '—'}`, w - 16, 26, 'right', 13, INK);
    label(ctx, s.tipo, w - 16, h - 14, 'right', 13, PEN);
  },
};
