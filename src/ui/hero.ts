import { h } from './dom';
import { gridFill, ground, niceStep, label, mono, hand, arrow, dim, COLORS, INK, MUT, PEN } from '../render/plot';

const V0 = 20, G = 9.8;
const rad = (d: number) => (d * Math.PI) / 180;
const fl = (v: number, d = 1) => v.toFixed(d).replace('.', ',');

/** Lámina viva del inicio: arrastra el ángulo y mira por qué θ y 90°−θ llegan al mismo punto. */
export function hero(): HTMLElement {
  const W = 760, H = 430, dpr = Math.min(window.devicePixelRatio || 1, 2);
  const still = !!window.matchMedia?.('(prefers-reduced-motion: reduce)').matches;
  let theta = 38;
  const canvas = h('canvas', { width: W * dpr, height: H * dpr, role: 'img', 'aria-label': 'Trayectoria de un proyectil. Arrastra para cambiar el ángulo de lanzamiento.', style: `aspect-ratio:${W}/${H}` });
  const ctx = canvas.getContext('2d')!;
  const out = h('output', { for: 'hero-angle' });
  const slider = h('input', { id: 'hero-angle', type: 'range', min: '8', max: '82', step: '1', value: String(theta), 'aria-label': 'Ángulo de lanzamiento en grados' }) as HTMLInputElement;
  const set = (v: number) => { theta = Math.round(Math.min(82, Math.max(8, v))); slider.value = String(theta); paint(); };
  const paint = () => { out.textContent = `${theta}°`; slider.style.setProperty('--pct', `${((theta - 8) / 74) * 100}%`); if (still) draw(0.6); };
  slider.addEventListener('input', () => set(+slider.value));

  const x0 = 56, y0 = H - 66, xmax = (V0 * V0) / G * 1.06, sc = (W - x0 - 30) / xmax;
  const X = (x: number) => x0 + x * sc, Y = (y: number) => y0 - y * sc;
  const phys = (th: number) => { const vx = V0 * Math.cos(rad(th)), vy = V0 * Math.sin(rad(th)); return { vx, vy, T: (2 * vy) / G, R: (vx * 2 * vy) / G, Hm: (vy * vy) / (2 * G) }; };

  let drag = false;
  const aim = (e: PointerEvent) => {
    const r = canvas.getBoundingClientRect(), px = ((e.clientX - r.left) * W) / r.width, py = ((e.clientY - r.top) * H) / r.height;
    set((Math.atan2(y0 - py, Math.max(4, px - x0)) * 180) / Math.PI);
  };
  canvas.addEventListener('pointerdown', (e) => { drag = true; canvas.setPointerCapture(e.pointerId); aim(e); });
  canvas.addEventListener('pointermove', (e) => { if (drag) aim(e); });
  canvas.addEventListener('pointerup', () => (drag = false));

  function draw(tFixed?: number) {
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    gridFill(ctx, W, H, 20);
    ground(ctx, x0 - 20, W - 14, y0);
    const sx = niceStep(xmax, 6);
    ctx.strokeStyle = INK; ctx.lineWidth = 1.2;
    for (let x = 0; x <= xmax; x += sx) { ctx.beginPath(); ctx.moveTo(X(x), y0); ctx.lineTo(X(x), y0 + 5); ctx.stroke(); mono(ctx, `${x}`, X(x), y0 + 19, 'center', 10); }
    label(ctx, 'metros', W - 18, y0 + 19, 'right', 11, MUT);
    const A = phys(theta), B = phys(90 - theta), tt = tFixed ?? ((performance.now() / 1000) * 0.85) % (Math.max(A.T, B.T) + 0.9);
    const curve = (P: ReturnType<typeof phys>, color: string, dash: number[], lw: number) => {
      ctx.strokeStyle = color; ctx.lineWidth = lw; ctx.setLineDash(dash); ctx.beginPath();
      for (let i = 0; i <= 80; i++) { const t = (P.T * i) / 80; const x = P.vx * t, y = P.vy * t - 0.5 * G * t * t; i ? ctx.lineTo(X(x), Y(y)) : ctx.moveTo(X(x), Y(y)); }
      ctx.stroke(); ctx.setLineDash([]);
    };
    if (Math.abs(theta - 45) > 1.5) curve(B, COLORS[3], [7, 6], 2.2);
    curve(A, COLORS[0], [], 3.2);
    // ángulo
    ctx.strokeStyle = MUT; ctx.lineWidth = 1.3; ctx.beginPath(); ctx.arc(X(0), Y(0), 46, -rad(theta), 0); ctx.stroke();
    ctx.setLineDash([4, 4]); ctx.beginPath(); ctx.moveTo(X(0), Y(0)); ctx.lineTo(X(0) + 120 * Math.cos(rad(theta)), Y(0) - 120 * Math.sin(rad(theta))); ctx.stroke(); ctx.setLineDash([]);
    mono(ctx, `θ = ${theta}°`, X(0) + 54, Y(0) - 10, 'left', 14, INK);
    ctx.fillStyle = PEN; ctx.strokeStyle = INK; ctx.lineWidth = 2; ctx.beginPath(); ctx.arc(X(0) + 120 * Math.cos(rad(theta)), Y(0) - 120 * Math.sin(rad(theta)), 8, 0, 7); ctx.fill(); ctx.stroke();
    // alcance
    dim(ctx, X(0), y0, X(A.R), y0, `R = ${fl(A.R)} m`, { off: 44, color: COLORS[2] });
    if (Math.abs(theta - 45) > 1.5) { ctx.fillStyle = COLORS[3]; ctx.beginPath(); ctx.arc(X(B.R), Y(0), 5, 0, 7); ctx.fill(); hand(ctx, `${90 - theta}° llega al mismo punto`, X(B.R) - 8, Y(B.Hm) - 12, 'right', 19, COLORS[3]); }
    else hand(ctx, '45°: el mayor alcance', X(A.R / 2), Y(A.Hm) - 14, 'center', 20, PEN);
    // móviles
    const ball = (P: ReturnType<typeof phys>, c: string, r: number) => { const t = Math.min(tt, P.T); ctx.fillStyle = c; ctx.strokeStyle = INK; ctx.lineWidth = 1.6; ctx.beginPath(); ctx.arc(X(P.vx * t), Y(P.vy * t - 0.5 * G * t * t), r, 0, 7); ctx.fill(); ctx.stroke(); };
    if (Math.abs(theta - 45) > 1.5) ball(B, COLORS[3], 5.5);
    ball(A, PEN, 7);
    hand(ctx, 'arrastra el punto amarillo', W - 16, 30, 'right', 20, PEN);
    mono(ctx, `R = v₀² · sen 2θ / g`, 20, 30, 'left', 14, INK);
    mono(ctx, `v₀ = ${V0} m/s   g = 9,8 m/s²`, 20, 50, 'left', 12, MUT);
    void arrow;
  }
  paint();
  const fig = h('figure', { class: 'hero-fig' }, canvas, h('figcaption', {}, h('label', { for: 'hero-angle' }, 'Ángulo'), slider, out));
  if (!still) {
    let seen = false;
    const loop = () => { if (canvas.isConnected) seen = true; else if (seen) return; draw(); requestAnimationFrame(loop); };
    requestAnimationFrame(loop);
  } else draw(0.6);
  document.fonts?.ready.then(() => draw(still ? 0.6 : undefined));
  return fig;
}
