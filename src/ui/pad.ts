import { h } from './dom';

interface Stroke { c: string; w: number; e: boolean; p: [number, number][] }
const COLORS: [string, string][] = [['#3B82C4', 'Azul'], ['#D9A400', 'Ámbar'], ['#2B9468', 'Verde'], ['#D6513E', 'Rojo']];

/** Hoja de borrador a mano libre: lápiz, colores, borrador, deshacer. Funciona con mouse, lápiz táctil y dedo. */
export function crearPad(): HTMLElement {
  const cv = h('canvas', { class: 'pad', role: 'img', 'aria-label': 'Hoja para escribir y dibujar a mano' }) as HTMLCanvasElement;
  const strokes: Stroke[] = [];
  let color = COLORS[0][0], erase = false, cur: Stroke | null = null, height = 240;
  const ctx = () => cv.getContext('2d')!;
  const fit = () => {
    const r = cv.getBoundingClientRect(), d = Math.min(window.devicePixelRatio || 1, 2);
    if (!r.width) return;
    cv.width = Math.round(r.width * d); cv.height = Math.round(height * d); cv.style.height = height + 'px';
    ctx().setTransform(d, 0, 0, d, 0, 0); redraw();
  };
  const draw = (s: Stroke) => {
    const c = ctx(); if (!s.p.length) return;
    c.save(); c.lineCap = 'round'; c.lineJoin = 'round'; c.lineWidth = s.w;
    c.globalCompositeOperation = s.e ? 'destination-out' : 'source-over'; c.strokeStyle = s.c;
    c.beginPath(); c.moveTo(s.p[0][0], s.p[0][1]);
    if (s.p.length === 1) c.lineTo(s.p[0][0] + 0.01, s.p[0][1]);
    for (let i = 1; i < s.p.length - 1; i++) { const [x, y] = s.p[i], [nx, ny] = s.p[i + 1]; c.quadraticCurveTo(x, y, (x + nx) / 2, (y + ny) / 2); }
    if (s.p.length > 1) c.lineTo(...s.p[s.p.length - 1]);
    c.stroke(); c.restore();
  };
  const redraw = () => { const c = ctx(); c.clearRect(0, 0, cv.width, cv.height); strokes.forEach(draw); };
  const pt = (e: PointerEvent): [number, number] => { const r = cv.getBoundingClientRect(); return [e.clientX - r.left, e.clientY - r.top]; };
  cv.addEventListener('pointerdown', (e) => {
    if (e.button > 0) return;
    if (!cv.width) fit();
    cv.setPointerCapture(e.pointerId); e.preventDefault();
    cur = { c: color, w: erase ? 18 : 2.4 + (e.pressure && e.pointerType === 'pen' ? e.pressure * 1.6 : 0), e: erase, p: [pt(e)] }; strokes.push(cur); draw(cur);
  });
  cv.addEventListener('pointermove', (e) => { if (!cur) return; for (const ev of e.getCoalescedEvents?.() ?? [e]) cur.p.push(pt(ev)); redraw(); });
  const end = () => { cur = null; };
  cv.addEventListener('pointerup', end); cv.addEventListener('pointercancel', end);

  const tool = (label: string, on: () => void, cls = '') => h('button', { class: `btn sm ${cls}`, type: 'button', onclick: on }, label);
  const sw = COLORS.map(([c, n]) => { const b = h('button', { class: 'sw', type: 'button', style: `--sw:${c}`, 'aria-label': `Lápiz ${n}`, onclick: () => { color = c; erase = false; mark(); } }); (b as any)._c = c; return b; });
  const bEr = tool('Borrador', () => { erase = true; mark(); }, 'er');
  const mark = () => { sw.forEach((b) => b.classList.toggle('on', !erase && (b as any)._c === color)); bEr.classList.toggle('on', erase); };
  mark();
  const bar = h('div', { class: 'padbar' }, ...sw, bEr,
    tool('Deshacer', () => { strokes.pop(); redraw(); }), tool('Limpiar', () => { strokes.length = 0; redraw(); }), tool('+ Espacio', () => { height += 160; fit(); }));
  const root = h('div', { class: 'padwrap' }, bar, cv);
  new ResizeObserver(() => { if (cv.width / (Math.min(window.devicePixelRatio || 1, 2)) !== cv.getBoundingClientRect().width) fit(); }).observe(root);
  return root;
}
