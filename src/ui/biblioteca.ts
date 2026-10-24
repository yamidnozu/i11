import { h } from './dom';
import { renderQuestion } from './question';
import { QUESTIONS, LESSONS, BLOQUES } from '../content';
import { SIMULACROS, resumen } from '../content/simulacros';
import { listSims } from '../core/registry';
import { AREAS, AREA_IDS, type AreaId } from '../adaptive/areas';
import { head } from './pages';

const corto = (s: string) => s.replace(/\$[^$]*\$/g, '…').replace(/\s+/g, ' ').slice(0, 110);

/** Todo el contenido en un solo lugar: simulacros, laboratorios, lecciones y cada pregunta del banco. */
export function biblioteca(): HTMLElement {
  const root = h('div');
  let area: AreaId | 'todas' = 'todas', texto = '';
  const lista = h('div', { class: 'biblista' });
  const pinta = () => {
    const qs = QUESTIONS.filter((q) => q.tipo !== 'reto' || true).filter((q) => (area === 'todas' || q.area === area) && (!texto || (q.enunciado + ' ' + q.id).toLowerCase().includes(texto)));
    lista.replaceChildren(h('p', { class: 'fine' }, `${qs.length} ${qs.length === 1 ? 'pregunta' : 'preguntas'}`), ...qs.map((q) => h('a', { class: 'bibq', href: `#/pregunta/${q.id}` },
      h('b', {}, q.id), h('span', {}, corto(q.enunciado) || 'Pregunta con figura'), h('small', {}, `${AREAS[q.area].nombre} · nivel ${q.nivel}${q.bloque ? ' · con contexto' : ''}${q.figuras || q.opcionesFig ? ' · con figura' : ''}`))));
  };
  const tabs = h('div', { class: 'row exfil' }, ...(['todas', ...AREA_IDS] as const).map((a) => h('button', { class: 'btn sm', type: 'button', 'data-a': a, onclick: (e: Event) => { area = a; tabs.querySelectorAll('button').forEach((b) => b.classList.toggle('primary', b === e.currentTarget)); pinta(); } }, a === 'todas' ? 'Todas' : AREAS[a].nombre)));
  tabs.querySelector('button')!.classList.add('primary');
  const buscar = h('input', { type: 'search', class: 'bibbus', placeholder: 'Buscar en las preguntas', 'aria-label': 'Buscar en las preguntas' }) as HTMLInputElement;
  buscar.addEventListener('input', () => { texto = buscar.value.trim().toLowerCase(); pinta(); });
  const sims = listSims();
  const enlace = (href: string, t: string, d: string) => h('a', { class: 'simcard', href }, h('b', {}, t), h('span', { class: 'sd' }, d));
  pinta();
  root.append(head('Todo el contenido', 'Todo es gratis y está aquí: entra a lo que quieras, en el orden que quieras.'),
    h('h2', {}, 'Simulacros'), h('div', { class: 'simlist' }, ...SIMULACROS.map((s) => { const r = resumen(s); return enlace(`#/simulacro/${s.id}`, s.nombre, `${r.preguntas} preguntas · ${r.minutos} min${s.modo === 'examen' ? ' · formato cuadernillo' : ''}`); })),
    h('h2', {}, `Laboratorios (${sims.length})`), h('div', { class: 'simlist' }, ...sims.map((s) => enlace(`#/sim/${s.id}`, s.title, AREAS[s.area].nombre))),
    h('h2', {}, `Lecciones (${LESSONS.length})`), h('div', { class: 'simlist' }, ...LESSONS.map((l) => enlace(`#/leccion/${l.id}`, l.titulo, AREAS[l.area].nombre))),
    h('h2', {}, `Preguntas (${QUESTIONS.length}) y contextos (${BLOQUES.length})`), buscar, tabs, lista);
  return root;
}

/** Una sola pregunta del banco, con su contexto y toda la explicación del profe. */
export function preguntaSuelta(id: string): HTMLElement {
  const q = QUESTIONS.find((x) => x.id === id);
  if (!q) return h('div', {}, head('Pregunta no encontrada'), h('a', { class: 'btn', href: '#/contenido' }, 'Volver a Todo el contenido'));
  const prefijo = q.id.split('-')[0];
  const secuencia = QUESTIONS.filter((x) => x.origen === q.origen && x.area === q.area && (q.origen !== 'icfes' || x.id.split('-')[0] === prefijo));
  const indice = secuencia.findIndex((x) => x.id === q.id);
  const volver = q.origen === 'icfes' ? `#/aprender?area=${q.area}` : '#/contenido';
  const paginador = () => h('nav', { class: 'question-pager', 'aria-label': 'Navegación entre preguntas' },
    indice > 0 ? h('a', { class: 'btn sm', href: `#/pregunta/${secuencia[indice - 1].id}` }, '← Anterior') : h('span', { class: 'btn sm muted', 'aria-disabled': 'true' }, '← Anterior'),
    h('a', { class: 'question-pager-back', href: volver }, q.origen === 'icfes' ? 'Volver al banco de Aprender' : 'Volver a Todo el contenido'),
    h('span', { class: 'question-pager-count' }, `Pregunta ${indice + 1} de ${secuencia.length}`),
    indice >= 0 && indice < secuencia.length - 1 ? h('a', { class: 'btn sm primary', href: `#/pregunta/${secuencia[indice + 1].id}` }, 'Siguiente →') : h('span', { class: 'btn sm muted', 'aria-disabled': 'true' }, 'Siguiente →'));
  return h('div', {}, h('a', { class: 'crumb', href: volver }, q.origen === 'icfes' ? '← Aprender' : '← Todo el contenido'), paginador(), renderQuestion(q, () => undefined, { feedback: true, ayuda: 'siempre' }), paginador());
}
