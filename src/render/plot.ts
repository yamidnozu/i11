/** Estilo plano técnico (cianotipo): fondo azul, trazos claros, cotas y anotaciones a mano. */
export const BG = '#121821';
export const INK = '#E8EDF3';
export const MUT = '#8E9AAB';
export const COLORS = ['#5BC8D6', '#F2C14E', '#6FCF97', '#E58AA8', '#F08A6B', '#9AA7F0'];
export const PEN = COLORS[1];
const SANS = '"IBM Plex Sans","Segoe UI",system-ui,sans-serif';
const MONO = '"IBM Plex Mono",ui-monospace,Menlo,monospace';
const HAND = '"Caveat","Segoe Script","Comic Sans MS",cursive';

export function mapper(w: number, h: number, xmin: number, xmax: number, ymin: number, ymax: number, pad = 36) {
  const sx = (w - 2 * pad) / (xmax - xmin || 1);
  const sy = (h - 2 * pad) / (ymax - ymin || 1);
  return { X: (x: number) => pad + (x - xmin) * sx, Y: (y: number) => h - pad - (y - ymin) * sy, sx, sy, pad };
}

export function niceStep(range: number, target = 6): number {
  const raw = range / target;
  const mag = Math.pow(10, Math.floor(Math.log10(raw || 1)));
  const n = raw / mag;
  return (n < 1.5 ? 1 : n < 3.5 ? 2 : n < 7.5 ? 5 : 10) * mag;
}

function txt(ctx: CanvasRenderingContext2D, s: string, x: number, y: number, align: CanvasTextAlign, font: string, color: string) {
  ctx.font = font; ctx.textAlign = align; ctx.lineJoin = 'round';
  ctx.lineWidth = 4; ctx.strokeStyle = BG; ctx.strokeText(s, x, y);
  ctx.fillStyle = color; ctx.fillText(s, x, y);
}
export const label = (ctx: CanvasRenderingContext2D, s: string, x: number, y: number, align: CanvasTextAlign = 'left', size = 12, color = INK) => txt(ctx, s, x, y, align, `${size}px ${SANS}`, color);
export const mono = (ctx: CanvasRenderingContext2D, s: string, x: number, y: number, align: CanvasTextAlign = 'left', size = 11, color = MUT) => txt(ctx, s, x, y, align, `${size}px ${MONO}`, color);
export const hand = (ctx: CanvasRenderingContext2D, s: string, x: number, y: number, align: CanvasTextAlign = 'left', size = 18, color = PEN) => txt(ctx, s, x, y, align, `600 ${size}px ${HAND}`, color);

/** Fondo milimetrado de plano técnico. */
export function gridFill(ctx: CanvasRenderingContext2D, w: number, h: number, step = 20) {
  ctx.fillStyle = BG; ctx.fillRect(0, 0, w, h);
  ctx.lineWidth = 1;
  for (let k = 0, x = 0; x <= w; x += step, k++) { ctx.strokeStyle = k % 5 === 0 ? 'rgba(159,192,240,.2)' : 'rgba(159,192,240,.08)'; ctx.beginPath(); ctx.moveTo(x + .5, 0); ctx.lineTo(x + .5, h); ctx.stroke(); }
  for (let k = 0, y = 0; y <= h; y += step, k++) { ctx.strokeStyle = k % 5 === 0 ? 'rgba(159,192,240,.2)' : 'rgba(159,192,240,.08)'; ctx.beginPath(); ctx.moveTo(0, y + .5); ctx.lineTo(w, y + .5); ctx.stroke(); }
}

export function axes(ctx: CanvasRenderingContext2D, m: ReturnType<typeof mapper>, w: number, h: number, xmin: number, xmax: number, ymin: number, ymax: number, xl = '', yl = '') {
  ctx.fillStyle = BG; ctx.fillRect(0, 0, w, h);
  const sx = niceStep(xmax - xmin), sy = niceStep(ymax - ymin);
  const L = m.X(xmin), R = m.X(xmax), T = m.Y(ymax), B = m.Y(ymin);
  ctx.save(); ctx.beginPath(); ctx.rect(L, T, R - L, B - T); ctx.clip(); ctx.lineWidth = 1;
  const lines = (step: number, lo: number, hi: number, vertical: boolean, stroke: string) => {
    ctx.strokeStyle = stroke; ctx.beginPath();
    for (let v = Math.ceil(lo / step - 1e-9) * step; v <= hi + 1e-9; v += step) {
      if (vertical) { const x = Math.round(m.X(v)) + .5; ctx.moveTo(x, T); ctx.lineTo(x, B); } else { const y = Math.round(m.Y(v)) + .5; ctx.moveTo(L, y); ctx.lineTo(R, y); }
    }
    ctx.stroke();
  };
  if (sx * m.sx / 5 >= 7) lines(sx / 5, xmin, xmax, true, 'rgba(159,192,240,.08)');
  if (sy * m.sy / 5 >= 7) lines(sy / 5, ymin, ymax, false, 'rgba(159,192,240,.08)');
  lines(sx, xmin, xmax, true, 'rgba(159,192,240,.22)');
  lines(sy, ymin, ymax, false, 'rgba(159,192,240,.22)');
  ctx.restore();
  ctx.strokeStyle = 'rgba(234,243,255,.55)'; ctx.lineWidth = 1; ctx.strokeRect(L + .5, T + .5, R - L, B - T);
  for (let v = Math.ceil(xmin / sx - 1e-9) * sx; v <= xmax + 1e-9; v += sx) mono(ctx, String(+v.toFixed(6)), m.X(v), B + 15, 'center', 10);
  for (let v = Math.ceil(ymin / sy - 1e-9) * sy; v <= ymax + 1e-9; v += sy) mono(ctx, String(+v.toFixed(6)), L - 6, m.Y(v) + 3, 'right', 10);
  ctx.strokeStyle = INK; ctx.lineWidth = 1.6;
  if (xmin <= 0 && xmax >= 0) { ctx.beginPath(); ctx.moveTo(m.X(0), B); ctx.lineTo(m.X(0), T); ctx.stroke(); }
  if (ymin <= 0 && ymax >= 0) { ctx.beginPath(); ctx.moveTo(L, m.Y(0)); ctx.lineTo(R, m.Y(0)); ctx.stroke(); }
  if (xl) label(ctx, xl, R, h - 6, 'right', 12, MUT);
  if (yl) label(ctx, yl, L + 6, T + 16, 'left', 12, MUT);
}

export function drawSeries(canvas: HTMLCanvasElement, rows: Record<string, number>[], xk: string, yk: string, title: string, color = COLORS[0]) {
  const ctx = canvas.getContext('2d')!;
  const w = canvas.width, h = canvas.height;
  ctx.setTransform(1, 0, 0, 1, 0, 0);
  const pts = rows.map((r) => [r[xk], r[yk]]).filter(([a, b]) => Number.isFinite(a) && Number.isFinite(b));
  let xmin = 0, xmax = 1, ymin = 0, ymax = 1;
  if (pts.length) {
    xmin = Math.min(...pts.map((p) => p[0])); xmax = Math.max(...pts.map((p) => p[0]));
    ymin = Math.min(0, ...pts.map((p) => p[1])); ymax = Math.max(...pts.map((p) => p[1]));
    if (xmax === xmin) xmax = xmin + 1;
    if (ymax === ymin) ymax = ymin + 1;
  }
  const m = mapper(w, h, xmin, xmax, ymin, ymax, 30);
  axes(ctx, m, w, h, xmin, xmax, ymin, ymax, xk, '');
  hand(ctx, title, 36, 20, 'left', 17, COLORS[1]);
  ctx.strokeStyle = color; ctx.lineWidth = 2.5; ctx.lineJoin = 'round'; ctx.beginPath();
  pts.forEach(([a, b], i) => (i ? ctx.lineTo(m.X(a), m.Y(b)) : ctx.moveTo(m.X(a), m.Y(b))));
  ctx.stroke();
  if (pts.length) { const [a, b] = pts[pts.length - 1]; ctx.fillStyle = color; ctx.beginPath(); ctx.arc(m.X(a), m.Y(b), 4, 0, 7); ctx.fill(); }
}

export function arrow(ctx: CanvasRenderingContext2D, x0: number, y0: number, x1: number, y1: number, color = INK, w = 2, head = 9) {
  const len = Math.hypot(x1 - x0, y1 - y0);
  if (len < 2) return;
  const a = Math.atan2(y1 - y0, x1 - x0), hh = Math.min(head, len * 0.6);
  ctx.strokeStyle = color; ctx.fillStyle = color; ctx.lineWidth = w; ctx.lineCap = 'round'; ctx.setLineDash([]);
  ctx.beginPath(); ctx.moveTo(x0, y0); ctx.lineTo(x1 - Math.cos(a) * hh * 0.8, y1 - Math.sin(a) * hh * 0.8); ctx.stroke();
  ctx.beginPath(); ctx.moveTo(x1, y1); ctx.lineTo(x1 - hh * Math.cos(a - 0.42), y1 - hh * Math.sin(a - 0.42)); ctx.lineTo(x1 - hh * Math.cos(a + 0.42), y1 - hh * Math.sin(a + 0.42)); ctx.closePath(); ctx.fill();
}

/** Cota de dibujo técnico: líneas de extensión + flecha doble + valor. */
export function dim(ctx: CanvasRenderingContext2D, x0: number, y0: number, x1: number, y1: number, text: string, o: { color?: string; off?: number; size?: number } = {}) {
  const c = o.color ?? INK, off = o.off ?? 24;
  const dx = x1 - x0, dy = y1 - y0, L = Math.hypot(dx, dy) || 1, nx = -dy / L, ny = dx / L;
  const ax = x0 + nx * off, ay = y0 + ny * off, bx = x1 + nx * off, by = y1 + ny * off;
  ctx.strokeStyle = c; ctx.lineWidth = 1; ctx.setLineDash([]);
  ctx.beginPath(); ctx.moveTo(x0 + nx * 4, y0 + ny * 4); ctx.lineTo(ax + nx * 6, ay + ny * 6); ctx.moveTo(x1 + nx * 4, y1 + ny * 4); ctx.lineTo(bx + nx * 6, by + ny * 6); ctx.stroke();
  const mx = (ax + bx) / 2, my = (ay + by) / 2;
  arrow(ctx, mx, my, ax, ay, c, 1.2, 7); arrow(ctx, mx, my, bx, by, c, 1.2, 7);
  mono(ctx, text, mx + nx * 12, my + ny * 12 + 4, 'center', o.size ?? 12, c);
}

/** Anotación manuscrita con línea guía. */
export function callout(ctx: CanvasRenderingContext2D, px: number, py: number, tx: number, ty: number, text: string, color = PEN, size = 18) {
  ctx.strokeStyle = color; ctx.fillStyle = color; ctx.lineWidth = 1.2; ctx.setLineDash([]);
  ctx.beginPath(); ctx.arc(px, py, 3, 0, 7); ctx.fill();
  const left = tx >= px;
  hand(ctx, text, tx, ty - 5, left ? 'left' : 'right', size, color);
  const wd = ctx.measureText(text).width;
  ctx.beginPath(); ctx.moveTo(px, py); ctx.lineTo(tx, ty); ctx.lineTo(left ? tx + wd : tx - wd, ty); ctx.stroke();
}

export function ground(ctx: CanvasRenderingContext2D, x0: number, x1: number, y: number, color = INK) {
  ctx.strokeStyle = color; ctx.lineWidth = 2; ctx.setLineDash([]);
  ctx.beginPath(); ctx.moveTo(x0, y); ctx.lineTo(x1, y); ctx.stroke();
  ctx.lineWidth = 1; ctx.strokeStyle = 'rgba(234,243,255,.4)'; ctx.beginPath();
  for (let x = x0; x < x1; x += 12) { ctx.moveTo(x, y); ctx.lineTo(x - 8, y + 9); }
  ctx.stroke();
}

/** Fórmula química con subíndices: C3H8 → C₃H₈ (los coeficientes iniciales no se bajan). */
export function formulaText(ctx: CanvasRenderingContext2D, f: string, x: number, y: number, size = 16, color = INK, align: CanvasTextAlign = 'left') {
  const segs: { t: string; sub: boolean }[] = [];
  for (let i = 0; i < f.length; i++) {
    const c = f[i], prev = f[i - 1];
    segs.push({ t: c, sub: /\d/.test(c) && !!prev && /[A-Za-z)]|\d/.test(prev) && segs.length > 0 && (segs[segs.length - 1].sub || /[A-Za-z)]/.test(prev)) });
  }
  const big = `600 ${size}px ${SANS}`, small = `600 ${Math.round(size * 0.7)}px ${SANS}`;
  let total = 0;
  for (const s of segs) { ctx.font = s.sub ? small : big; total += ctx.measureText(s.t).width; }
  let cx = align === 'center' ? x - total / 2 : align === 'right' ? x - total : x;
  ctx.textAlign = 'left'; ctx.lineJoin = 'round';
  for (const s of segs) {
    ctx.font = s.sub ? small : big;
    const yy = s.sub ? y + size * 0.28 : y;
    ctx.lineWidth = 4; ctx.strokeStyle = BG; ctx.strokeText(s.t, cx, yy);
    ctx.fillStyle = color; ctx.fillText(s.t, cx, yy);
    cx += ctx.measureText(s.t).width;
  }
  return total;
}
