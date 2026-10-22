import type { SimConfig } from './types';

const reg = new Map<string, SimConfig>();

/** Valida un simulador declarativo antes de registrarlo. Devuelve lista de errores. */
export function validateConfig(c: SimConfig): string[] {
  const e: string[] = [];
  if (!/^[a-z]+\.[a-z0-9_]+$/.test(c.id)) e.push(`id inválido: ${c.id}`);
  if (!c.evidencias?.length) e.push('sin evidencias');
  if (c.nivel < 1 || c.nivel > 4) e.push('nivel fuera de 1..4');
  if (c.mode === 'dynamic' && !c.logic.step) e.push('modo dinámico requiere logic.step');
  if (c.mode === 'dynamic' && !c.logic.done) e.push('modo dinámico requiere logic.done');
  const keys = new Set(c.params.map((p) => p.key));
  if (keys.size !== c.params.length) e.push('claves de parámetros repetidas');
  for (const ch of c.challenges) {
    for (const k of Object.keys(ch.fixed ?? {})) if (!keys.has(k)) e.push(`reto ${ch.id}: parámetro fijo desconocido ${k}`);
    if (!ch.checks.length) e.push(`reto ${ch.id} sin criterios`);
  }
  for (const g of c.graphs ?? []) if (!c.logic.sample) e.push(`gráfica ${g.id} requiere logic.sample`);
  return e;
}

export function register(c: SimConfig): void {
  const errs = validateConfig(c);
  if (errs.length) throw new Error(`Simulador ${c.id} inválido: ${errs.join('; ')}`);
  if (reg.has(c.id)) throw new Error(`Simulador duplicado: ${c.id}`);
  reg.set(c.id, c);
}
export const getSim = (id: string) => reg.get(id);
export const listSims = () => [...reg.values()];
