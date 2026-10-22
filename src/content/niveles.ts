import data from '../../content/niveles.json';
import type { AreaId } from '../adaptive/areas';

export interface NivelDef { nombre: string; desde: number; hasta: number; resumen: string; demuestra: string[] }
/** Niveles de desempeño por prueba (0 a 100), con lo que demuestra quien está en cada uno. Fuente: niveles de desempeño Saber 11 del ICFES. */
export const NIVELES: Record<AreaId, NivelDef[]> = data as unknown as Record<AreaId, NivelDef[]>;
export const nivelIndex = (a: AreaId, v: number) => Math.max(0, NIVELES[a].findIndex((n) => v >= n.desde && v <= n.hasta));
export const nivelDe = (a: AreaId, v: number) => NIVELES[a][nivelIndex(a, Math.round(v))];
export const siguienteNivel = (a: AreaId, v: number) => NIVELES[a][nivelIndex(a, Math.round(v)) + 1];
