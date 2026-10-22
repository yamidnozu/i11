import type { Extra, SimConfig } from './types';

/** Une la lógica base de un simulador con su capa pedagógica y visual. */
export function enrich<S>(sim: SimConfig<S>, x: Extra<S>): SimConfig<S> {
  return {
    ...sim,
    learn: x.learn, presets: x.presets, experiments: x.experiments, solution: x.solution,
    compare: x.compare, insight: x.insight, ambient: x.ambient, readouts: x.readouts,
    params: sim.params.map((d) => ({ ...d, hint: x.paramHints?.[d.key] ?? d.hint, ...(x.paramOverrides?.[d.key] ?? {}) })),
    render: { ...sim.render, ...(x.size ?? {}), view: x.view ?? sim.render.view },
  };
}
