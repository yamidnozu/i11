export type AreaId = 'matematicas' | 'lectura_critica' | 'sociales' | 'ciencias' | 'ingles';

/** Medias/DE nacionales Cal. A 2024 y cortes de nivel (Informe Nacional 2024 / fichas ICFES). */
export const AREAS: Record<AreaId, { nombre: string; mu: number; sigma: number; peso: number; cortes: number[]; niveles: string[] }> = {
  matematicas: { nombre: 'Matemáticas', mu: 53, sigma: 13, peso: 3, cortes: [35, 50, 70], niveles: ['Nivel 1', 'Nivel 2', 'Nivel 3', 'Nivel 4'] },
  lectura_critica: { nombre: 'Lectura Crítica', mu: 54, sigma: 10, peso: 3, cortes: [35, 50, 65], niveles: ['Nivel 1', 'Nivel 2', 'Nivel 3', 'Nivel 4'] },
  sociales: { nombre: 'Sociales y Ciudadanas', mu: 49, sigma: 12, peso: 1, cortes: [40, 55, 70], niveles: ['Nivel 1', 'Nivel 2', 'Nivel 3', 'Nivel 4'] },
  ciencias: { nombre: 'Ciencias Naturales', mu: 51, sigma: 11, peso: 3, cortes: [40, 55, 70], niveles: ['Nivel 1', 'Nivel 2', 'Nivel 3', 'Nivel 4'] },
  ingles: { nombre: 'Inglés', mu: 52, sigma: 13, peso: 1, cortes: [36, 57, 70], niveles: ['Pre A1', 'A1', 'A2', 'B1'] },
};
export const AREA_IDS = Object.keys(AREAS) as AreaId[];
