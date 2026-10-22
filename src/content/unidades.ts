import type { AreaId } from '../adaptive/areas';
import { QUESTIONS, LESSONS, UNIDADES_ALL } from './index';
import { getSim } from '../core/registry';
import type { Unidad } from './schema';

export type { Unidad };
export const UNIDADES: Unidad[] = UNIDADES_ALL;
export const unidadesDe = (a: AreaId) => UNIDADES.filter((u) => u.area === a);
export const unidad = (id: string) => UNIDADES.find((u) => u.id === id);
export const preguntasDe = (u: Unidad) => u.preguntas.map((id) => QUESTIONS.find((q) => q.id === id)).filter((q) => !!q) as typeof QUESTIONS;
export const tieneSim = (u: Unidad) => !!u.sim && !!getSim(u.sim);
export const tieneLeccion = (u: Unidad) => !!u.leccion && LESSONS.some((l) => l.id === u.leccion);
