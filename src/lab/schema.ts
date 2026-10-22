import type { AreaId } from '../adaptive/areas';
import type { Learn, Preset } from '../core/types';
import { checkExpr, checkTpl } from './expr';

export interface LabParam { key: string; label: string; tipo: 'slider' | 'select' | 'toggle'; min?: number; max?: number; paso?: number; def: number | boolean; unidad?: string; opciones?: { v: number; l: string }[]; hint?: string }
export interface Capa { t: string; si?: string; [k: string]: unknown }
export interface Fisica {
  /** 'rk4' integra ecuaciones diferenciales; 'formula' evalúa estadoT en cada instante t. */
  integracion?: 'rk4' | 'formula';
  estado?: Record<string, string | number>; ecuaciones?: Record<string, string>; estadoT?: Record<string, string>;
  duracion?: string; evento?: string; ajustar?: Record<string, number>; muestras?: string[]; medidas: Record<string, string>;
}
export interface LabJSON {
  id: string; titulo: string; area: AreaId; subarea?: string; competencia: string; evidencias: string[]; nivel: number; tiempoMin: number; modo: 'dinamico' | 'estatico';
  params: LabParam[]; constantes?: Record<string, number>; derivadas?: Record<string, string>; fisica: Fisica;
  graficas?: { id: string; x: string; y: string; titulo: string }[]; etiquetasMedidas?: Record<string, string>; lectura?: string[]; descripcion?: string;
  retos: { id: string; texto: string; fijos?: Record<string, number | boolean>; criterios: { medida: string; objetivo: number; tol: number }[]; pista?: string }[];
  escena: { ancho: number; alto: number; marco?: { izq?: number; der?: number; arriba?: number; abajo?: number; x: [string | number, string | number]; y: [string | number, string | number]; escalaIgual?: boolean }; capas: Capa[] };
  aprende?: Learn; presets?: Preset[];
  experimentos?: { id: string; titulo: string; setup: Record<string, number | boolean>; cambio?: Record<string, number | boolean>; pregunta: string; opciones: string[]; correcta: number; explicacion: string; verifica?: string }[];
  solucion?: { t: string; tex: string; nota?: string; si?: string }[];
  comparar?: { label: string; teoria: string; sim: string; nota?: { si: string; txt: string } }[];
  insight?: { si: string; txt: string }[][];
}

export const PRIMITIVAS = ['cuadricula', 'suelo', 'ejes', 'curva', 'funcion', 'marcas', 'circulo', 'rect', 'linea', 'flecha', 'texto', 'cota', 'llamada', 'arco'] as const;
const EXPR_CAMPOS = ['x', 'y', 'x0', 'y0', 'x1', 'y1', 'dx', 'dy', 'r', 'w', 'h', 'si', 'desde', 'hasta', 'a0', 'a1', 'cada', 'off', 'grosor', 'paso', 'n', 'tam'];
const TPL_CAMPOS = ['txt', 'etiqueta'];

export function validateLab(j: LabJSON): string[] {
  const e: string[] = [], id = j?.id ?? '?';
  const add = (m: string) => e.push(`laboratorio ${id}: ${m}`);
  if (!/^[a-z]+\.[a-z0-9_]+$/.test(j.id ?? '')) add('id (formato «area.nombre», ej. fis.proyectil)');
  for (const k of ['titulo', 'area', 'competencia'] as const) if (!j[k]) add(`falta ${k}`);
  if (!j.evidencias?.length) add('sin evidencias');
  if (!(j.nivel >= 1 && j.nivel <= 4)) add('nivel 1 a 4');
  if (!j.params?.length) add('sin params');
  const keys = new Set((j.params ?? []).map((p) => p.key));
  if (keys.size !== (j.params ?? []).length) add('params repetidos');
  for (const p of j.params ?? []) { if (p.tipo === 'slider' && !(p.min! < p.max!)) add(`param ${p.key}: min < max`); if (p.tipo === 'select' && !p.opciones?.length) add(`param ${p.key}: sin opciones`); }
  const chk = (src: unknown, donde: string) => { const m = checkExpr(src); if (m) add(`${donde}: ${m}`); };
  const chkT = (src: unknown, donde: string) => { if (typeof src === 'string') checkTpl(src).forEach((m) => add(`${donde}: ${m}`)); };
  for (const [k, v] of Object.entries(j.derivadas ?? {})) chk(v, `derivadas.${k}`);
  const f = j.fisica;
  if (!f) add('falta fisica'); else {
    const modo = f.integracion ?? (f.ecuaciones ? 'rk4' : 'formula');
    if (modo === 'rk4' && !(f.estado && f.ecuaciones)) add('rk4 necesita estado y ecuaciones');
    if (modo === 'rk4') for (const k of Object.keys(f.ecuaciones ?? {})) if (!(k in (f.estado ?? {}))) add(`ecuación de «${k}» sin valor inicial en estado`);
    if (modo === 'formula' && !f.estadoT) add('formula necesita estadoT');
    if (j.modo === 'dinamico' && !f.duracion && !f.evento) add('modo dinámico: falta duracion o evento (cuándo termina)');
    for (const k of ['estado', 'ecuaciones', 'estadoT'] as const) for (const [n, v] of Object.entries(f[k] ?? {})) chk(v, `fisica.${k}.${n}`);
    if (f.duracion) chk(f.duracion, 'fisica.duracion'); if (f.evento) chk(f.evento, 'fisica.evento');
    if (!Object.keys(f.medidas ?? {}).length) add('sin medidas');
    for (const [n, v] of Object.entries(f.medidas ?? {})) chk(v, `medidas.${n}`);
  }
  const med = new Set(Object.keys(f?.medidas ?? {}));
  for (const g of j.graficas ?? []) if (!g.id || !g.x || !g.y) add('gráfica incompleta');
  for (const r of j.retos ?? []) { if (!r.criterios?.length) add(`reto ${r.id}: sin criterios`); for (const c of r.criterios ?? []) if (!med.has(c.medida)) add(`reto ${r.id}: medida desconocida ${c.medida}`); for (const k of Object.keys(r.fijos ?? {})) if (!keys.has(k)) add(`reto ${r.id}: parámetro desconocido ${k}`); }
  for (const x of j.experimentos ?? []) { if (!(x.correcta >= 0 && x.correcta < x.opciones.length)) add(`experimento ${x.id}: correcta fuera de rango`); for (const k of [...Object.keys(x.setup ?? {}), ...Object.keys(x.cambio ?? {})]) if (!keys.has(k)) add(`experimento ${x.id}: parámetro desconocido ${k}`); if (x.verifica) chk(x.verifica, `experimento ${x.id}.verifica`); }
  for (const s of j.solucion ?? []) { chkT(s.tex, 'solucion.tex'); chkT(s.nota, 'solucion.nota'); chkT(s.t, 'solucion.t'); if (s.si) chk(s.si, 'solucion.si'); }
  for (const c of j.comparar ?? []) { chk(c.teoria, 'comparar.teoria'); chk(c.sim, 'comparar.sim'); }
  for (const g of j.insight ?? []) for (const x of g) { chk(x.si, 'insight.si'); chkT(x.txt, 'insight.txt'); }
  chkT(j.descripcion, 'descripcion');
  if (!j.escena?.capas?.length) add('escena sin capas');
  e.push(...validaEscena(j.escena, `laboratorio ${id}: `));
  return e;
}

/** Revisa una escena (de un laboratorio o de un paso «escena»): tipos de capa y expresiones. */
export function validaEscena(E: { marco?: LabJSON['escena']['marco']; capas: Capa[]; vars?: Record<string, string | number> } | undefined, pre = ''): string[] {
  const e: string[] = [], add = (m: string) => e.push(pre + m);
  if (!E?.capas?.length) { add('escena sin capas'); return e; }
  const chk = (src: unknown, donde: string) => { const m = checkExpr(src); if (m) add(`${donde}: ${m}`); };
  const mc = E.marco; if (mc) for (const v of [...mc.x, ...mc.y]) chk(v, 'escena.marco');
  for (const [k, v] of Object.entries(E.vars ?? {})) chk(v, `escena.vars.${k}`);
  E.capas.forEach((c, i) => {
    const d = `escena.capas[${i}] (${c.t})`;
    if (!(PRIMITIVAS as readonly string[]).includes(c.t)) { add(`${d}: tipo desconocido. Usa: ${PRIMITIVAS.join(', ')}`); return; }
    for (const k of EXPR_CAMPOS) if (k in c) chk(c[k], `${d}.${k}`);
    for (const k of TPL_CAMPOS) if (typeof c[k] === 'string') checkTpl(c[k] as string).forEach((m) => add(`${d}.${k}: ${m}`));
  });
  return e;
}
