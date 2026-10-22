import type { M, Params, SimConfig } from './types';

export const defaults = (cfg: SimConfig): Params => Object.fromEntries(cfg.params.map((d) => [d.key, d.default]));

/** Ejecuta un simulador completo sin dibujar (para miniaturas, comparaciones antes/después y pruebas). */
export function runHeadless(cfg: SimConfig, p: Params, maxSteps = 12000) {
  let s = cfg.logic.init(p);
  const traj = [s];
  if (cfg.mode === 'dynamic') {
    for (let i = 0; i < maxSteps && !cfg.logic.done!(s, p); i++) {
      s = cfg.logic.step!(s, p, 1 / 120);
      if (i % 2 === 1) traj.push(s);
    }
    traj.push(s);
  }
  const measures: M = cfg.logic.measures(traj, p);
  return { state: s, traj, measures };
}

export function drawThumb(cfg: SimConfig, canvas: HTMLCanvasElement, p: Params = defaults(cfg)) {
  const { state, traj, measures } = runHeadless(cfg, p);
  const { width: w, height: h } = cfg.render;
  canvas.width = w; canvas.height = h;
  const ctx = canvas.getContext('2d')!;
  cfg.render.view({ ctx, w, h, state, traj, p, measures, time: 0, pointer: null });
}
