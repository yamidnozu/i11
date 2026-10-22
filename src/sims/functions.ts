import { compile } from '../math/expr';
import { axes, mapper, label, COLORS } from '../render/plot';
import type { SimConfig, Params } from '../core/types';

export interface FState { fn: (x: number) => number; family: number; a: number; b: number; c: number; error?: string; roots: number[]; vx: number; vy: number; y0: number; expr: string }

function makeFn(p: Params): { fn: (x: number) => number; error?: string; expr: string } {
  const a = +p.a, b = +p.b, c = +p.c, fam = +p.family;
  const custom = String(p.custom ?? '').trim();
  if (custom) {
    try {
      const f = compile(custom, ['x', 'a', 'b', 'c']);
      return { fn: (x) => f({ x, a, b, c }), expr: `f(x) = ${custom}` };
    } catch (e) {
      return { fn: () => NaN, error: (e as Error).message, expr: '' };
    }
  }
  switch (fam) {
    case 1: return { fn: (x) => a * x + b, expr: `f(x) = ${a}x + ${b}` };
    case 2: return { fn: (x) => a * x * x + b * x + c, expr: `f(x) = ${a}x² + ${b}x + ${c}` };
    case 3: return { fn: (x) => a * Math.exp(b * x) + c, expr: `f(x) = ${a}·e^(${b}x) + ${c}` };
    default: return { fn: (x) => a * Math.sin(b * x) + c, expr: `f(x) = ${a}·sen(${b}x) + ${c}` };
  }
}

export function findRoots(fn: (x: number) => number, lo = -10, hi = 10, n = 2000): number[] {
  const out: number[] = [];
  let px = lo, py = fn(px);
  for (let i = 1; i <= n; i++) {
    const x = lo + ((hi - lo) * i) / n, y = fn(x);
    if (Number.isFinite(py) && Number.isFinite(y)) {
      if (py === 0) out.push(px);
      else if (py * y < 0) {
        let a = px, b = x;
        for (let k = 0; k < 60; k++) { const m = (a + b) / 2; if (fn(a) * fn(m) <= 0) b = m; else a = m; }
        out.push((a + b) / 2);
      }
    }
    px = x; py = y;
  }
  return [...new Set(out.map((r) => +r.toFixed(6)))];
}

const F = (p: Params): FState => {
  const { fn, error, expr } = makeFn(p);
  const a = +p.a, b = +p.b, c = +p.c, family = +p.family;
  const quad = family === 2 && !String(p.custom ?? '').trim() && a !== 0;
  const vx = quad ? -b / (2 * a) : NaN;
  return { fn, family, a, b, c, error, expr, roots: error ? [] : findRoots(fn), vx, vy: quad ? fn(vx) : NaN, y0: fn(0) };
};

export const functionsSim: SimConfig<FState> = {
  id: 'mat.funciones',
  title: 'Graficador de funciones con parámetros',
  area: 'matematicas',
  competencia: 'interpretacion_y_representacion',
  evidencias: ['MAT_E1.1', 'MAT_E1.2', 'MAT_E2.3'],
  nivel: 2, tiempoMin: 10, mode: 'static',
  params: [
    { key: 'family', label: 'Tipo de función', type: 'select', default: 2, options: [{ v: 1, l: 'Lineal ax+b' }, { v: 2, l: 'Cuadrática ax²+bx+c' }, { v: 3, l: 'Exponencial a·eᵇˣ+c' }, { v: 4, l: 'Trigonométrica a·sen(bx)+c' }] },
    { key: 'a', label: 'a', type: 'slider', min: -5, max: 5, step: 0.5, default: 1 },
    { key: 'b', label: 'b', type: 'slider', min: -5, max: 5, step: 0.5, default: -4 },
    { key: 'c', label: 'c', type: 'slider', min: -5, max: 5, step: 0.5, default: 3 },
    { key: 'custom', label: 'Función propia (usa x, a, b, c). Ej: 2x^2 - 3x + 1', type: 'text', default: '' },
  ],
  logic: {
    init: (p) => F(p),
    measures: (traj) => {
      const s = traj[0];
      return { intercepto_y: s.y0, num_raices: s.roots.length, raiz_1: s.roots[0] ?? NaN, raiz_2: s.roots[1] ?? NaN, vertice_x: s.vx, vertice_y: s.vy };
    },
  },
  measureLabels: { intercepto_y: 'Corte con el eje y', num_raices: 'Raíces en [−10, 10]', raiz_1: 'Raíz 1', raiz_2: 'Raíz 2', vertice_x: 'Vértice x', vertice_y: 'Vértice y' },
  challenges: [
    { id: 'ch1', prompt: 'Con la cuadrática, elige a, b y c para que el vértice esté en (2, −3).', fixed: { family: 2, custom: '' }, checks: [{ measure: 'vertice_x', target: 2, tol: 0.01 }, { measure: 'vertice_y', target: -3, tol: 0.01 }], hint: 'Vértice x = −b/(2a); luego ajusta c.' },
  ],
  table: (p) => {
    const s = F(p);
    return { cols: ['x', 'f(x)'], rows: Array.from({ length: 11 }, (_, i) => [i - 5, s.fn(i - 5)]) };
  },
  describe: (m, p) => `${F(p).expr}. Corte con y: ${m.intercepto_y}. Raíces: ${m.num_raices}`,
  render: {
    width: 700, height: 460,
    view({ ctx, w, h, state: s }) {
      const m = mapper(w, h, -10, 10, -10, 10, 36);
      axes(ctx, m, w, h, -10, 10, -10, 10, 'x', 'y');
      if (s.error) { label(ctx, `Error: ${s.error}`, 20, 40, 'left', 14, '#B91C1C'); return; }
      ctx.save(); ctx.beginPath(); ctx.rect(m.pad, m.pad, w - 2 * m.pad, h - 2 * m.pad); ctx.clip();
      ctx.strokeStyle = COLORS[0]; ctx.lineWidth = 3; ctx.beginPath();
      let pen = false;
      for (let i = 0; i <= 700; i++) {
        const x = -10 + (20 * i) / 700, y = s.fn(x);
        if (!Number.isFinite(y) || Math.abs(y) > 1e3) { pen = false; continue; }
        if (pen) ctx.lineTo(m.X(x), m.Y(y)); else { ctx.moveTo(m.X(x), m.Y(y)); pen = true; }
      }
      ctx.stroke(); ctx.restore();
      ctx.fillStyle = COLORS[1];
      for (const r of s.roots) { ctx.beginPath(); ctx.arc(m.X(r), m.Y(0), 5, 0, 7); ctx.fill(); }
      if (Number.isFinite(s.vx) && Math.abs(s.vy) < 12) { ctx.fillStyle = COLORS[2]; ctx.beginPath(); ctx.rect(m.X(s.vx) - 5, m.Y(s.vy) - 5, 10, 10); ctx.fill(); }
      label(ctx, s.expr, 10, 20, 'left', 14);
    },
  },
};
