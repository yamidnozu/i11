import { QUESTIONS, SIMULACROS_ALL, CONTENT_WARNINGS } from './index';
import type { Question } from './schema';
import { validateSimulacro, type SimulacroDef, type SeccionDef } from './schema';
import { AREAS, AREA_IDS } from '../adaptive/areas';

const mc = QUESTIONS.filter((q) => q.tipo !== 'reto');
const ids = new Set(mc.map((q) => q.id));

/** Simulacro por defecto: usa todo el banco, una sección por área (siempre disponible). */
const RAPIDO: SimulacroDef = {
  id: 'rapido', nombre: 'Simulacro rápido', descripcion: 'Todas las preguntas del banco, una sección por área.', nivel: 'Práctica',
  secciones: AREA_IDS.map((a) => ({ id: a, titulo: AREAS[a].nombre, area: a, minutos: Math.max(2, mc.filter((q) => q.area === a).length * 2), auto: { area: a, n: 999 } })).filter((c) => mc.some((q) => q.area === c.area)),
};

export const SIMULACROS: SimulacroDef[] = [...SIMULACROS_ALL, RAPIDO].filter((s, i, all) => {
  const e = validateSimulacro(s, ids);
  if (all.findIndex((x) => x.id === s.id) !== i) e.push(`simulacro ${s.id}: id repetido`);
  if (e.length) { CONTENT_WARNINGS.push(...e); console.warn('[contenido]', e.join('; ')); return false; }
  return true;
});
export const getSimulacro = (id: string) => SIMULACROS.find((s) => s.id === id);

export interface Armado { titulo: string; area?: SeccionDef['area']; minutos: number; ids: string[] }
const barajar = <T,>(a: T[]) => { const r = [...a]; for (let i = r.length - 1; i > 0; i--) { const j = Math.floor(Math.random() * (i + 1)); [r[i], r[j]] = [r[j], r[i]]; } return r; };

/** Convierte la definición en listas concretas de preguntas (elige al azar lo que sea auto). */
export function armar(s: SimulacroDef): Armado[] {
  const usadas = new Set<string>(s.secciones.flatMap((c) => c.preguntas ?? []));
  return s.secciones.map((c) => {
    let lista = (c.preguntas ?? []).filter((id) => ids.has(id));
    if (c.auto) {
      const a = c.auto, ex = new Set(a.excluir ?? []);
      const pool = mc.filter((q) => (!a.area || q.area === a.area) && (!a.nivel || a.nivel.includes(q.nivel)) && !ex.has(q.id) && !usadas.has(q.id) && !lista.includes(q.id));
      const pick = barajar(pool).slice(0, Math.max(0, a.n - lista.length)).map((q) => q.id);
      pick.forEach((id) => usadas.add(id)); lista = [...lista, ...pick];
    }
    return { titulo: c.titulo, area: c.area, minutos: c.minutos, ids: s.barajar === false ? lista : barajar(lista) };
  }).filter((c) => c.ids.length);
}
export interface PruebaArm { titulo: string; area?: SeccionDef['area']; ids: string[] }
export interface SesionArm { titulo: string; minutos: number; pruebas: PruebaArm[] }

/** Elige las preguntas de una prueba sin partir los bloques de contexto: un bloque entra completo o no entra. */
function elegirPrueba(c: SeccionDef, usadas: Set<string>, mezclar: boolean): string[] {
  const fijas = (c.preguntas ?? []).filter((id) => ids.has(id));
  fijas.forEach((id) => usadas.add(id));
  let lista = [...fijas];
  if (c.auto) {
    const a = c.auto, ex = new Set(a.excluir ?? []);
    const pool = mc.filter((q) => (!a.area || q.area === a.area) && (!a.nivel || a.nivel.includes(q.nivel)) && !ex.has(q.id) && !usadas.has(q.id));
    const grupos: Question[][] = [], porBloque = new Map<string, Question[]>();
    for (const q of pool) { if (q.bloque) { const g = porBloque.get(q.bloque); if (g) g.push(q); else { const n = [q]; porBloque.set(q.bloque, n); grupos.push(n); } } else grupos.push([q]); }
    const falta = Math.max(0, a.n - lista.length);
    const mez = mezclar ? barajar(grupos) : grupos;
    let n = 0;
    for (const g of mez) { if (n >= falta) break; if (n + g.length > falta && n > 0) continue; g.forEach((q) => { lista.push(q.id); usadas.add(q.id); }); n += g.length; }
  }
  // los de un mismo bloque quedan juntos, en el orden en que aparecieron
  const byId = new Map(mc.map((q) => [q.id, q] as const)), orden: string[] = [], vistos = new Set<string>();
  for (const id of lista) { const b = byId.get(id)?.bloque; if (!b) { orden.push(id); continue; } if (vistos.has(b)) continue; vistos.add(b); orden.push(...lista.filter((x) => byId.get(x)?.bloque === b)); }
  return orden;
}
/** Convierte un simulacro de modo «examen» en sesiones con sus pruebas ya sorteadas. */
export function armarExamen(s: SimulacroDef): SesionArm[] {
  const usadas = new Set<string>();
  return (s.sesiones ?? []).map((x) => ({ titulo: x.titulo, minutos: x.minutos, pruebas: x.pruebas.map((c) => ({ titulo: c.titulo, area: c.area, ids: elegirPrueba(c, usadas, s.barajar !== false) })).filter((c) => c.ids.length) })).filter((x) => x.pruebas.length);
}
/** Cuántas preguntas tendrá (aprox. si hay auto) y minutos totales. */
export function resumen(s0: SimulacroDef) {
  const s = comoExamen(s0);
  if (s.modo === 'examen') { const ses = armarExamen({ ...s, barajar: false }); return { preguntas: ses.reduce((t, x) => t + x.pruebas.reduce((u, p) => u + p.ids.length, 0), 0), minutos: (s.sesiones ?? []).reduce((t, x) => t + x.minutos, 0) }; }
  const n = armar({ ...s, barajar: false }).reduce((t, c) => t + c.ids.length, 0);
  return { preguntas: n, minutos: s.secciones.reduce((t, c) => t + c.minutos, 0) };
}

/** Los simulacros por secciones también se presentan como cuadernillo: una sesión con todas sus pruebas visibles. */
export function comoExamen(s: SimulacroDef): SimulacroDef {
  if (s.modo === 'examen') return s;
  return { ...s, modo: 'examen', sesiones: [{ titulo: s.nombre, minutos: s.secciones.reduce((t, c) => t + c.minutos, 0), pruebas: s.secciones }] };
}
