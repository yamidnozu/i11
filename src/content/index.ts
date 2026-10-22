import type { Question, Lesson, Hoja, Guion, Enfoque, Pack, Unidad, SimulacroDef, Bloque } from './schema';
import { validateQuestion, validateLesson, validateBloque } from './schema';
import hojas from '../../content/hojas.json';
import guiones from '../../content/guiones.json';
import enfoques from '../../content/enfoques.json';
import unidadesBase from '../../content/unidades.json';
const qm = import.meta.glob('../../content/questions/*.json', { eager: true, import: 'default' }) as Record<string, Question[]>;
const lm = import.meta.glob('../../content/lessons/*.json', { eager: true, import: 'default' }) as Record<string, Lesson>;
const pm = { ...import.meta.glob('../../content/packs/**/*.json', { eager: true, import: 'default' }), ...import.meta.glob('../../content/icfes/**/preguntas.json', { eager: true, import: 'default' }) } as Record<string, Pack | Pack[]>;
const sm = import.meta.glob('../../content/simulacros/*.json', { eager: true, import: 'default' }) as Record<string, SimulacroDef | SimulacroDef[]>;
const bm = import.meta.glob('../../content/bloques/*.json', { eager: true, import: 'default' }) as Record<string, Bloque | Bloque[]>;
const H = hojas as unknown as Record<string, Hoja>;
const EN = enfoques as unknown as Record<string, Enfoque>;
const G = guiones as unknown as Record<string, Guion>;

/** Avisos de contenido mal formado: se omite lo inválido y la app sigue funcionando. */
export const CONTENT_WARNINGS: string[] = [];
const aviso = (m: string) => { CONTENT_WARNINGS.push(m); if (typeof console !== 'undefined') console.warn('[contenido]', m); };
const arr = <T>(x: T | T[] | undefined): T[] => (x === undefined ? [] : Array.isArray(x) ? x : [x]);

const packs: Pack[] = Object.values(pm).flatMap((x) => arr(x));
const base: Question[] = Object.values(qm).flat();
const vistos = new Set<string>();
function admitir(q: Question, origen: string): Question | null {
  if (vistos.has(q?.id)) { aviso(`${origen}: id repetido ${q?.id}`); return null; }
  const e = origen === 'banco' ? [] : validateQuestion(q);
  if (e.length) { aviso(`${origen}: ${e.join('; ')}`); return null; }
  vistos.add(q.id); return q;
}
const conExtras = (q: Question): Question => (q.hoja ? { ...q, hoja: { ...q.hoja, guion: q.hoja.guion ?? G[q.id], enfoque: q.hoja.enfoque ?? EN[q.id] } } : H[q.id] ? { ...q, hoja: { ...H[q.id], guion: G[q.id], enfoque: EN[q.id] } } : q);
export const QUESTIONS: Question[] = [
  ...base.map((q) => admitir(q, 'banco')),
  ...packs.flatMap((p) => (p.preguntas ?? []).map((q) => admitir(q, `paquete ${p.id ?? '?'}`))),
].filter((q): q is Question => !!q).map(conExtras);

const bls: Bloque[] = [...Object.values(bm).flatMap((x) => arr(x)), ...packs.flatMap((p) => p.bloques ?? [])];
export const BLOQUES: Bloque[] = bls.filter((b, i) => {
  if (bls.findIndex((x) => x.id === b.id) !== i) { aviso(`bloque repetido ${b.id}`); return false; }
  const e = validateBloque(b); if (e.length) { aviso(e.join('; ')); return false; } return true;
});
export const bloqueDe = (q: Question) => (q.bloque ? BLOQUES.find((b) => b.id === q.bloque) : undefined);
for (const q of QUESTIONS) if (q.bloque && !BLOQUES.some((b) => b.id === q.bloque)) aviso(`${q.id}: bloque inexistente ${q.bloque}`);

const lecs: Lesson[] = [...Object.values(lm), ...packs.flatMap((p) => p.lecciones ?? [])];
export const LESSONS: Lesson[] = lecs.filter((l, i) => {
  if (lecs.findIndex((x) => x.id === l.id) !== i) { aviso(`lección repetida ${l.id}`); return false; }
  const e = validateLesson(l); if (e.length) { aviso(e.join('; ')); return false; } return true;
});

const unis = [...(unidadesBase as unknown as Unidad[]), ...packs.flatMap((p) => p.unidades ?? [])];
export const UNIDADES_ALL: Unidad[] = unis.filter((u, i) => unis.findIndex((x) => x.id === u.id) === i);

export const SIMULACROS_ALL: SimulacroDef[] = [...Object.values(sm).flatMap((x) => arr(x)), ...packs.flatMap((p) => p.simulacros ?? [])];
export const byId = (id: string) => QUESTIONS.find((q) => q.id === id);
