import type { ViewCtx } from '../core/types';
import { gridFill, ground, mono, label, hand, arrow, dim, callout, niceStep, COLORS, INK, MUT, PEN } from '../render/plot';
import { ev, evNum, tpl, type Scope } from './expr';
import type { LabJSON, Capa } from './schema';

const COLOR_NOMBRE: Record<string, string> = { tinta: INK, suave: MUT, pluma: PEN, fondo: '#121821' };
const color = (c: unknown, sc: Scope, def = INK): string => {
  if (typeof c === 'number') return COLORS[c % COLORS.length];
  if (typeof c === 'string') { if (c in COLOR_NOMBRE) return COLOR_NOMBRE[c]; if (/^#|^rgb|^hsl/.test(c)) return c; const v = ev(c, sc); return typeof v === 'number' ? COLORS[v % COLORS.length] : String(v); }
  return def;
};

/** Dibuja la escena declarativa del JSON. Todo lo que cambia con el tiempo o los parámetros son expresiones. */
export function drawScene(lab: LabJSON, base: (p: ViewCtx<any>['p']) => Scope, v: ViewCtx<any>) {
  pintarEscena(lab.escena, { ...base(v.p), ...v.state, m: v.measures, time: v.time }, v.ctx, v.w, v.h, v.traj as Record<string, number>[]);
}
export type Escena = LabJSON['escena'];
/** Pinta una escena declarativa sobre un canvas (la usan los laboratorios y los pasos «escena» de las explicaciones). */
export function pintarEscena(E: Escena, sc0: Scope, ctx: CanvasRenderingContext2D, w: number, h: number, traj: Record<string, number>[] = []) {
  const mc = E.marco, v = { traj };
  const sc: Scope = { ...sc0, traj, w, h };
  const izq = mc?.izq ?? 40, der = mc?.der ?? 30, arr = mc?.arriba ?? 40, aba = mc?.abajo ?? 40, gy = h - aba;
  let xmin = 0, xmax = 1, ymin = 0, ymax = 1, sx = 1, sy = 1;
  if (mc) {
    xmin = evNum(mc.x[0], sc); xmax = evNum(mc.x[1], sc); ymin = evNum(mc.y[0], sc); ymax = evNum(mc.y[1], sc);
    sx = (w - izq - der) / (xmax - xmin); sy = (gy - arr) / (ymax - ymin);
    if (mc.escalaIgual) sx = sy = Math.min(sx, sy);
  }
  const X = (x: number) => izq + (x - xmin) * sx, Y = (y: number) => gy - (y - ymin) * sy;
  Object.assign(sc, { izq, der, arriba: arr, abajo: aba, gy, sx, sy, xmin, xmax, ymin, ymax, __f: { X: ([a]: number[]) => X(a), Y: ([a]: number[]) => Y(a) } });
  const N = (c: Capa, k: string, d = 0, s: Scope = sc) => (k in c ? evNum(c[k] as string | number, s) : d);
  const P = (c: Capa, kx = 'x', ky = 'y', s: Scope = sc): [number, number] => (c.px ? [N(c, kx, 0, s), N(c, ky, 0, s)] : [X(N(c, kx, 0, s)), Y(N(c, ky, 0, s))]);
  const dash = (c: Capa) => { ctx.setLineDash(Array.isArray(c.guion) ? (c.guion as number[]) : []); };

  for (const c of E.capas) {
    if (c.si !== undefined && !ev(c.si, sc)) continue;
    ctx.save();
    switch (c.t) {
      case 'cuadricula': gridFill(ctx, w, h, N(c, 'paso', 20)); break;
      case 'suelo': ground(ctx, N(c, 'x0', izq - 16), N(c, 'x1', w - der + 8), N(c, 'y', gy), color(c.color, sc)); break;
      case 'ejes': {
        ctx.strokeStyle = INK; ctx.lineWidth = 1.4;
        if (c.y !== false) { ctx.beginPath(); ctx.moveTo(izq, gy); ctx.lineTo(izq, arr - 10); ctx.stroke(); }
        const sxp = niceStep(xmax - xmin, 7), syp = niceStep(ymax - ymin, 5);
        if (c.x !== false) for (let x = Math.ceil(xmin / sxp) * sxp; x <= xmax; x += sxp) { ctx.beginPath(); ctx.moveTo(X(x), gy); ctx.lineTo(X(x), gy + 5); ctx.stroke(); mono(ctx, String(+x.toFixed(2)), X(x), gy + 19, 'center', 10); }
        if (c.y !== false) for (let y = Math.ceil((ymin + 1e-9) / syp) * syp; y <= ymax; y += syp) { if (y <= ymin + 1e-9) continue; ctx.beginPath(); ctx.moveTo(izq - 5, Y(y)); ctx.lineTo(izq, Y(y)); ctx.stroke(); mono(ctx, String(+y.toFixed(2)), izq - 9, Y(y) + 3, 'right', 10); }
        if (c.xl) label(ctx, String(c.xl), w - der, gy + 19, 'right', 12, MUT); if (c.yl) label(ctx, String(c.yl), izq + 8, arr - 2, 'left', 12, MUT);
        break;
      }
      case 'curva': {
        const pts = (v.traj as Record<string, number>[]);
        ctx.strokeStyle = color(c.color ?? 0, sc); ctx.lineWidth = N(c, 'grosor', 3); ctx.lineJoin = 'round'; dash(c); ctx.beginPath();
        pts.forEach((s, i) => { const s2 = { ...sc, ...s }; const [px, py] = P(c, 'x', 'y', s2); i ? ctx.lineTo(px, py) : ctx.moveTo(px, py); }); ctx.stroke(); break;
      }
      case 'funcion': {
        const n = N(c, 'n', 120), a = N(c, 'desde', xmin), b = N(c, 'hasta', xmax), vr = String(c.var ?? 'u');
        ctx.strokeStyle = color(c.color ?? 0, sc); ctx.lineWidth = N(c, 'grosor', 2); dash(c); ctx.beginPath();
        let ok = false;
        for (let i = 0; i <= n; i++) { const u = a + ((b - a) * i) / n, s2 = { ...sc, [vr]: u }; const xv = 'x' in c ? N(c, 'x', 0, s2) : u, yv = N(c, 'y', 0, s2); if (!Number.isFinite(yv)) { ok = false; continue; } const px = c.px ? xv : X(xv), py = c.px ? yv : Y(yv); ok ? ctx.lineTo(px, py) : ctx.moveTo(px, py); ok = true; }
        ctx.stroke(); break;
      }
      case 'marcas': {
        const cada = N(c, 'cada', 0.25), key = String(c.clave ?? 't'), r = N(c, 'r', 3.6), cada2 = N(c, 'etiquetaCada', 2);
        let last = -1;
        for (const s of v.traj as Record<string, number>[]) {
          const k = Math.floor(s[key] / cada + 1e-9); if (k === last) continue; last = k;
          const s2 = { ...sc, ...s, k }, [px, py] = P(c, 'x', 'y', s2);
          ctx.fillStyle = '#121821'; ctx.strokeStyle = INK; ctx.lineWidth = 1.4; ctx.beginPath(); ctx.arc(px, py, r, 0, 7); ctx.fill(); ctx.stroke();
          if (c.etiqueta && k > 0 && k % cada2 === 0) mono(ctx, tpl(String(c.etiqueta), s2), px, py - 10, 'center', 10);
        }
        break;
      }
      case 'circulo': { const [px, py] = P(c); ctx.beginPath(); ctx.arc(px, py, N(c, 'r', 6), 0, 7); if (c.relleno !== undefined) { ctx.fillStyle = color(c.relleno, sc); ctx.fill(); } if (c.borde !== false) { ctx.strokeStyle = color(c.colorBorde ?? 'tinta', sc); ctx.lineWidth = N(c, 'grosor', 2); ctx.stroke(); } break; }
      case 'rect': { const [px, py] = P(c), rw = N(c, 'w', 10), rh = N(c, 'h', 10); const cx = c.centro === false ? px : px - rw / 2, cy = c.centro === false ? py : py - rh / 2; if (c.relleno !== undefined) { ctx.fillStyle = color(c.relleno, sc); ctx.fillRect(cx, cy, rw, rh); } if (c.borde !== false) { ctx.strokeStyle = color(c.colorBorde ?? 'tinta', sc); ctx.lineWidth = N(c, 'grosor', 1.5); ctx.strokeRect(cx, cy, rw, rh); } break; }
      case 'linea': { const [a, b] = P(c, 'x0', 'y0'), [d, e] = P(c, 'x1', 'y1'); ctx.strokeStyle = color(c.color ?? 'suave', sc); ctx.lineWidth = N(c, 'grosor', 1.5); dash(c); ctx.beginPath(); ctx.moveTo(a, b); ctx.lineTo(d, e); ctx.stroke(); break; }
      case 'flecha': { const [px, py] = P(c); const dx = N(c, 'dx', 0), dy = N(c, 'dy', 0); arrow(ctx, px, py, px + dx, py - dy, color(c.color ?? 2, sc), N(c, 'grosor', 2.2), N(c, 'cabeza', 9)); break; }
      case 'texto': {
        const [px, py] = P(c), s = tpl(String(c.txt ?? ''), sc), al = (c.align as CanvasTextAlign) ?? 'left', tam = N(c, 'tam', 12), col = color(c.color ?? 'tinta', sc);
        (c.fuente === 'mono' ? mono : c.fuente === 'mano' ? hand : label)(ctx, s, px + N(c, 'dx', 0), py - N(c, 'dy', 0), al, tam, col); break;
      }
      case 'cota': { const [a, b] = P(c, 'x0', 'y0'), [d, e] = P(c, 'x1', 'y1'); dim(ctx, a, b, d, e, tpl(String(c.txt ?? ''), sc), { off: N(c, 'off', 30), color: color(c.color ?? 4, sc) }); break; }
      case 'llamada': { const [px, py] = P(c); callout(ctx, px, py, px + N(c, 'dx', 20), py - N(c, 'dy', 26), tpl(String(c.txt ?? ''), sc), color(c.color ?? 'pluma', sc)); break; }
      case 'arco': { const [px, py] = P(c); ctx.strokeStyle = color(c.color ?? 'suave', sc); ctx.lineWidth = N(c, 'grosor', 1.2); ctx.beginPath(); ctx.arc(px, py, N(c, 'r', 40), -(N(c, 'a1', 0) * Math.PI) / 180, -(N(c, 'a0', 0) * Math.PI) / 180); ctx.stroke(); break; }
    }
    ctx.restore();
  }
}
