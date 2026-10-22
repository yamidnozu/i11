import type { AreaId } from '../adaptive/areas';
import { AREA_IDS } from '../adaptive/areas';
import { validaEscena } from '../lab/schema';

export type Rol = 'dato' | 'pide' | 'trampa' | 'clave';
export interface Marca { frag: string; rol: Rol; nota?: string; campo?: string; w?: string }
export interface Evento { anio: string; t: string; d: string; rol: 'antes' | 'hecho' | 'despues' }
export type Paso =
  | { k: 'idea'; titulo?: string; texto: string }
  | { k: 'calc'; titulo?: string; lineas: string[]; nota?: string }
  | { k: 'tabla'; titulo?: string; cols: string[]; filas: string[][] }
  | { k: 'ejemplo'; titulo?: string; si: string[]; no: string[] }
  | { k: 'linea'; titulo?: string; eventos: Evento[] }
  | { k: 'barras'; titulo?: string; barras: { l: string; e: string; segs: { v: number; c: 'azul' | 'verde' | 'rojo' | 'gris' | 'oro' }[] }[]; ref?: { v: number; l: string }; nota?: string }
  | { k: 'flujo'; titulo?: string; nodos: { v: string; l?: string }[]; saltos: string[]; nota?: string }
  | { k: 'vida'; titulo?: string; texto: string; icono?: string }
  | { k: 'glosa'; titulo?: string; frase: { en: string; es: string; pron?: string }[]; dice: string; nota?: string }
  | { k: 'escucha'; titulo?: string; frases: { en: string; es: string; pron?: string }[]; nota?: string }
  | { k: 'traducir'; titulo?: string; filas: { dice: string; escribo: string; rol?: Rol }[]; nota?: string }
  | { k: 'tanteo'; titulo?: string; busco: string; cols: [string, string, string]; filas: { a: string; b: string; c: string; ok?: boolean }[]; nota?: string }
  | { k: 'puntos'; titulo?: string; grupos: { n: number; l: string; c: 'rojo' | 'azul' | 'verde' | 'gris' }[]; lineas?: string[]; nota?: string }
  | { k: 'grafica'; titulo?: string; coef: [number, number, number]; x: [number, number]; puntos: { x: number; y: number; l: string }[]; nota?: string }
  | { k: 'escena'; titulo?: string; ancho: number; alto: number; marco?: { izq?: number; der?: number; arriba?: number; abajo?: number; x: [string | number, string | number]; y: [string | number, string | number]; escalaIgual?: boolean }; capas: { t: string; si?: string; [k: string]: unknown }[]; vars?: Record<string, string | number>; anim?: { dur: number; bucle?: boolean }; nota?: string }
  | { k: 'check'; texto: string };
export type Tarea =
  | { k: 'asignar'; titulo: string; items: { p: string; op: string[]; ok: number; why: string }[] }
  | { k: 'llenar'; titulo: string; antes: string; resp: number; tol?: number; unidad?: string; pista?: string; why: string }
  | { k: 'ordenar'; titulo: string; items: string[]; why: string };
export type NotaK = 'ej' | 'contra' | 'ana' | 'err' | 'por';
/** Una frase del profe: lo que dice (con $math$), y opcionalmente qué hace en pantalla. */
export interface Beat { t: string; v?: string; a?: string; k?: NotaK }
export type Guion = Record<'1' | '2' | '3', Beat[]>;
export interface Enfoque { tema: string; que: string; pistas: string[]; clave: string; no: { t: string; p: string }[]; plan: { t: string; eq?: string[] }[] }
export interface Hoja {
  enfoque?: Enfoque; modo: 'calculo' | 'lectura' | 'historia' | 'concepto'; marcas?: Marca[]; guia?: Tarea[]; guion?: Guion; pasos: Paso[] }
/** Escena dibujada con piezas JSON (la misma que usan los laboratorios y las explicaciones). */
export interface EscenaDef { ancho: number; alto: number; marco?: { izq?: number; der?: number; arriba?: number; abajo?: number; x: [string | number, string | number]; y: [string | number, string | number]; escalaIgual?: boolean }; capas: { t: string; si?: string; [k: string]: unknown }[]; vars?: Record<string, string | number>; anim?: { dur: number; bucle?: boolean } }
/** Una imagen del examen: archivo (img), SVG en línea, dibujo declarativo (escena) o tabla de datos. Siempre con texto alternativo. */
export type Figura =
  | { tipo: 'img'; src: string; alt: string; ancho?: number; pie?: string; recorteFuente?: { pagina: number; rect: [number, number, number, number] } }
  | { tipo: 'svg'; svg: string; alt: string; ancho?: number; pie?: string }
  | ({ tipo: 'escena'; alt: string; pie?: string } & EscenaDef)
  | { tipo: 'tabla'; cols: string[]; filas: string[][]; alt?: string; pie?: string }
  /** Hueco para una figura aún no cargada: cuando exista el archivo se cambia por tipo «img» o «svg». */
  | { tipo: 'pendiente'; pagina?: number; alt: string; pie?: string };
/** Contexto compartido por varias preguntas («Responde las preguntas X a Y de acuerdo con la siguiente información»). */
export interface Bloque { id: string; area: AreaId; encabezado?: string; titulo?: string; texto?: string; figuras?: Figura[]; fuente?: string }
export interface MarcoReferencia {
  version: number;
  origen: 'icfes' | 'propio' | 'licenciado';
  areas: Record<string, {
    nombre: string;
    fuentes?: string[];
    competencias: Array<{
      id: string;
      nombre: string;
      descripcion?: string;
      afirmaciones: Array<{ id: string; texto: string; evidencias: Array<{ id: string; texto: string }> }>;
    }>;
  }>;
}
export interface NivelesDesempeno {
  version: number;
  origen: 'icfes' | 'propio' | 'licenciado';
  areas: Record<string, { documento: string; fuente: string; niveles: Array<{ nivel: string; descriptores: string[]; revisar?: string }> }>;
}

export interface Question {
  id: string; area: AreaId; evidencia: string; nivel: 1 | 2 | 3 | 4;
  enunciado: string; opciones: string[]; correcta: number; explicacion: string; distractores: string[];
  bloque?: string; figuras?: Figura[]; opcionesFig?: (Figura | null)[]; afirmacion?: string; competencia?: string; parte?: string;
  /** Referencias estables a content/icfes/marco.json; solo se publican detrás del gate ICFES. */
  competenciaId?: string; afirmacionId?: string; evidenciaId?: string;
  hoja?: Hoja; lectura?: { id: string; titulo: string; texto: string }; origen: 'original' | 'icfes' | 'propio' | 'licenciado'; fuente?: string; revisar?: string[]; tipo?: 'mc' | 'reto'; sim?: { id: string; challengeId?: string };
}
export interface Lesson { id: string; titulo: string; area: AreaId; evidencias: string[]; sim?: { id: string }; ejemplos: { angulo: string; titulo: string; texto: string }[]; truco: string }

export const ANGULOS = ['cotidiano', 'dato_real', 'grafico_tabla', 'formal', 'error_tipico'];

export function validateQuestion(q: Question): string[] {
  const e: string[] = [];
  if (!/^[a-z]{3}-(i)?\d{3,4}$/.test(q.id)) e.push('id');
  if (!AREA_IDS.includes(q.area)) e.push('área');
  if (![1, 2, 3, 4].includes(q.nivel)) e.push('nivel');
  if (!q.enunciado || !q.explicacion) e.push('texto');
  if (!['original', 'icfes', 'propio', 'licenciado'].includes(q.origen)) e.push('origen');
  if ((q.origen === 'icfes' || q.origen === 'licenciado') && !q.fuente) e.push('contenido sin fuente (cita obligatoria)');
  if (q.tipo === 'reto') { if (!q.sim?.challengeId) e.push('reto sin challengeId'); return e.map((m) => `${q.id}: ${m}`); }
  if (q.opciones.length < 2 || q.opciones.length > 8) e.push('entre 2 y 8 opciones');
  if (q.opcionesFig && q.opcionesFig.length !== q.opciones.length) e.push('opcionesFig debe tener una entrada por opción (null si no hay figura)');
  for (const f of [...(q.figuras ?? []), ...(q.opcionesFig ?? [])]) if (f) e.push(...validaFigura(f));
  if (new Set(q.opciones).size !== q.opciones.length) e.push('opciones repetidas');
  if (!(q.correcta >= 0 && q.correcta < q.opciones.length)) e.push('correcta fuera de rango');
  if (q.distractores.length !== q.opciones.length) e.push('distractores');
  else q.distractores.forEach((d, i) => { if ((i === q.correcta) !== (d === '')) e.push(`distractor ${i}`); });
  for (const p of q.hoja?.pasos ?? []) if (p.k === 'escena') e.push(...validaEscena(p, 'paso escena: '));
  for (const m of q.hoja?.marcas ?? []) if (!q.enunciado.includes(m.frag)) e.push(`marca no está en el enunciado: ${m.frag}`);
  for (const t of q.hoja?.guia ?? []) {
    if (t.k === 'asignar') t.items.forEach((it, i) => { if (!(it.ok >= 0 && it.ok < it.op.length)) e.push(`guía: ok fuera de rango en ${i}`); if (it.op.length < 2) e.push('guía: pocas opciones'); });
    if (t.k === 'llenar' && !Number.isFinite(t.resp)) e.push('guía: resp no numérica');
    if (t.k === 'ordenar' && t.items.length < 3) e.push('guía: ordenar necesita 3+');
  }
  return e.map((m) => `${q.id}: ${m}`);
}
const SVG_MAL = /<\s*script|<\s*foreignObject|\son\w+\s*=|javascript:/i;
export function validaFigura(f: Figura): string[] {
  const e: string[] = [];
  if (f.tipo === 'img') { if (!f.src) e.push('figura img sin src'); if (!f.alt) e.push(`figura ${f.src}: falta alt`); }
  else if (f.tipo === 'svg') { if (!f.alt) e.push('figura svg: falta alt'); if (!/<svg[\s>]/i.test(f.svg ?? '')) e.push('figura svg: no tiene <svg>'); if (SVG_MAL.test(f.svg ?? '')) e.push('figura svg: contiene código no permitido'); }
  else if (f.tipo === 'escena') { if (!f.alt) e.push('figura escena: falta alt'); e.push(...validaEscena(f, 'figura: ')); }
  else if (f.tipo === 'tabla') { if (!f.cols?.length || !f.filas?.length) e.push('figura tabla vacía'); else f.filas.forEach((r, i) => { if (r.length !== f.cols.length) e.push(`figura tabla: la fila ${i + 1} no tiene ${f.cols.length} celdas`); }); }
  else if (f.tipo === 'pendiente') { if (!f.alt) e.push('figura pendiente: falta alt'); }
  else e.push('tipo de figura desconocido');
  return e;
}
export function validateBloque(b: Bloque): string[] {
  const e: string[] = [];
  if (!/^[a-z0-9][a-z0-9-]{1,40}$/.test(b.id ?? '')) e.push('id');
  if (!AREA_IDS.includes(b.area)) e.push('área');
  if (!b.texto && !b.figuras?.length) e.push('sin texto ni figuras');
  for (const f of b.figuras ?? []) e.push(...validaFigura(f));
  return e.map((m) => `bloque ${b.id}: ${m}`);
}
export function validateLesson(l: Lesson): string[] {
  const e: string[] = [];
  const got = new Set(l.ejemplos.map((x) => x.angulo));
  for (const a of ANGULOS) if (!got.has(a)) e.push(`${l.id}: falta ángulo ${a}`);
  if (!l.truco) e.push(`${l.id}: sin truco`);
  return e;
}

export interface Unidad { id: string; area: AreaId; titulo: string; resumen: string; preguntas: string[]; sim: string | null; leccion: string | null; min: number }
/** Una sección de un simulacro: preguntas fijas (ids) o elegidas al azar del banco (auto). */
export interface SeccionDef { id?: string; titulo: string; area?: AreaId; minutos: number; preguntas?: string[]; auto?: { area?: AreaId; n: number; nivel?: number[]; excluir?: string[] } }
/** Una sesión del examen real: un solo reloj y libertad para moverse entre todas sus pruebas. */
export interface SesionDef { titulo: string; minutos: number; pruebas: SeccionDef[] }
/** modo «secciones»: cada sección con su reloj (práctica). modo «examen»: sesiones con cuadernillo, hoja de respuestas y revisión final. */
export interface SimulacroDef { id: string; nombre: string; descripcion?: string; nivel?: string; barajar?: boolean; modo?: 'secciones' | 'examen'; secciones: SeccionDef[]; sesiones?: SesionDef[] }
/** Un paquete de contenido: cualquier JSON en content/packs/ con estas listas (todas opcionales). */
export interface Pack { id?: string; nombre?: string; version?: number; preguntas?: Question[]; bloques?: Bloque[]; lecciones?: Lesson[]; unidades?: Unidad[]; simulacros?: SimulacroDef[]; labs?: unknown[] }

export function validateSimulacro(s: SimulacroDef, ids: Set<string>): string[] {
  const e: string[] = [];
  if (!/^[a-z0-9][a-z0-9-]{1,40}$/.test(s.id ?? '')) e.push('id (minúsculas, números y guiones)');
  if (!s.nombre) e.push('nombre');
  const porSesion = s.modo === 'examen';
  const grupos: { d: string; c: SeccionDef }[] = porSesion ? (s.sesiones ?? []).flatMap((x, si) => x.pruebas.map((c, i) => ({ d: `sesión ${si + 1}, prueba ${i + 1}`, c }))) : (s.secciones ?? []).map((c, i) => ({ d: `sección ${i + 1}`, c }));
  if (porSesion) { if (!s.sesiones?.length) e.push('modo examen sin sesiones'); (s.sesiones ?? []).forEach((x, i) => { if (!x.titulo) e.push(`sesión ${i + 1}: sin título`); if (!(x.minutos > 0)) e.push(`sesión ${i + 1}: minutos`); if (!x.pruebas?.length) e.push(`sesión ${i + 1}: sin pruebas`); }); }
  else if (!Array.isArray(s.secciones) || !s.secciones.length) e.push('sin secciones');
  for (const { d, c } of grupos) {
    if (!c.titulo) e.push(`${d}: sin título`);
    if (!porSesion && !(c.minutos > 0)) e.push(`${d}: minutos`);
    if (c.area && !AREA_IDS.includes(c.area)) e.push(`${d}: área`);
    if (!c.preguntas?.length && !(c.auto && c.auto.n > 0)) e.push(`${d}: falta preguntas o auto.n`);
    for (const q of c.preguntas ?? []) if (!ids.has(q)) e.push(`${d}: pregunta inexistente ${q}`);
  }
  return e.map((m) => `simulacro ${s.id}: ${m}`);
}
