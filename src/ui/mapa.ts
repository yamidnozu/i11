import { h } from './dom';
import { icon } from './pages';
import { QUESTIONS, LESSONS, SIMULACROS_ALL, UNIDADES_ALL } from '../content';
import { listSims } from '../core/registry';
import { AREAS, AREA_IDS } from '../adaptive/areas';
import { query } from './nav';
import { dueCards } from '../state/store';

type Dest = { t: string; href: string; n?: string };
interface Estacion { id: string; ic: string; t: string; para: string; dest: Dest[]; num?: string }

/** Las 10 cosas que alguien viene a hacer, cada una a un solo toque. */
export const QUIERO: { q: string; href: string; ic: string }[] = [
  { q: 'Entender de qué trata esto y por dónde empezar', href: '#/', ic: 'home' },
  { q: 'Saber en qué nivel estoy', href: '#/diag', ic: 'target' },
  { q: 'Tener 15 minutos y no saber qué hacer', href: '#/sesion', ic: 'pencil' },
  { q: 'Estudiar un tema que no entiendo', href: '#/aprender', ic: 'book' },
  { q: 'Practicar solo una materia', href: '#/practicar', ic: 'pencil' },
  { q: 'Estudiar casos clínicos de Odontología (Endodoncia)', href: '#/odontologia', ic: 'tooth' },
  { q: 'Hacer un simulacro como el examen real', href: '#/simulacro', ic: 'clock' },
  { q: 'Ver un laboratorio (cambiar valores y ver qué pasa)', href: '#/sims', ic: 'flask' },
  { q: 'Repasar lo que ya fallé u olvidé', href: '#/sesion?modo=repaso', ic: 'reset' },
  { q: 'Ver cuánto llevo y qué me falta', href: '#/panel', ic: 'chart' },
  { q: 'Buscar una pregunta o un tema concreto', href: '#/contenido', ic: 'book' },
];

function estaciones(): Estacion[] {
  const due = dueCards().length;
  return [
    { id: 'diag', num: '1', ic: 'target', t: 'Empieza', para: 'Sabes en qué nivel estás. Son 15 preguntas, unos 20 minutos.', dest: [{ t: 'Diagnóstico', href: '#/diag' }] },
    { id: 'aprender', num: '2', ic: 'book', t: 'Aprende', para: 'Estudia cada tema: míralo en un laboratorio, léelo y resuélvelo con el profe.', dest: [{ t: 'Temas', href: '#/aprender', n: `${UNIDADES_ALL.length}` }, { t: 'Laboratorios', href: '#/sims', n: `${listSims().length}` }, { t: 'Lecciones', href: '#/lecciones', n: `${LESSONS.length}` }] },
    { id: 'practicar', num: '3', ic: 'pencil', t: 'Practica', para: 'Preguntas a tu medida, por materia o mezcladas, y repaso de lo que se olvida.', dest: [{ t: 'Sesión mixta', href: '#/sesion' }, { t: 'Repaso', href: '#/sesion?modo=repaso', n: due ? `${due}` : undefined }, ...AREA_IDS.map((a) => ({ t: AREAS[a].nombre, href: `#/sesion?area=${a}` })), { t: 'Actividades', href: '#/extras' }] },
    { id: 'medir', num: '4', ic: 'clock', t: 'Mide', para: 'Pruebas completas con reloj y tu progreso por área.', dest: [{ t: 'Simulacros', href: '#/simulacro', n: `${SIMULACROS_ALL.length}` }, { t: 'Mi progreso', href: '#/panel' }] },
    { id: 'contenido', ic: 'book', t: 'Biblioteca', para: 'Todo el contenido sin orden fijo: busca y abre lo que quieras.', dest: [{ t: 'Todo el contenido', href: '#/contenido', n: `${QUESTIONS.length} preguntas` }] },
  ];
}

const donde = (desde: string): string => {
  if (/^\/(diag)/.test(desde)) return 'diag';
  if (/^\/(aprender|unidad|sims|sim|lecciones|leccion)/.test(desde)) return 'aprender';
  if (/^\/(practicar|sesion|practica|extras|odontologia)/.test(desde)) return 'practicar';
  if (/^\/(simulacro|panel)/.test(desde)) return 'medir';
  if (/^\/(contenido|pregunta)/.test(desde)) return 'contenido';
  return '';
};

export function mapa(): HTMLElement {
  const aqui = donde(query().get('desde') ?? '');
  return h('div', { class: 'mapa' },
    h('header', { class: 'head' }, h('h1', {}, 'Mapa'), h('p', { class: 'lede' }, 'Toda la plataforma en una pantalla. Todo es gratis; el orden de abajo es solo una sugerencia.')),
    h('h2', { class: 'secth' }, 'Quiero…'),
    h('ul', { class: 'quiero' }, ...QUIERO.map((x) => h('li', {}, h('a', { href: x.href }, icon(x.ic, 20), h('span', {}, x.q), h('i', { class: 'go', 'aria-hidden': 'true' }, '→'))))),
    h('h2', { class: 'secth' }, 'La ruta completa'),
    h('ol', { class: 'ruta' }, ...estaciones().map((e) => h('li', { class: `rta${aqui === e.id ? ' aqui' : ''}${e.num ? '' : ' libre'}`, ...(aqui === e.id ? { 'aria-current': 'location' } : {}) },
      h('span', { class: 'pt', 'aria-hidden': 'true' }, e.num ?? ''),
      h('div', { class: 'ec' },
        h('h3', {}, icon(e.ic, 20), e.t, aqui === e.id ? h('em', { class: 'tag2' }, 'Estás aquí') : null),
        h('p', {}, e.para),
        h('div', { class: 'chips' }, ...e.dest.map((d) => h('a', { class: 'chip', href: d.href }, d.t, d.n ? h('small', {}, ` ${d.n}`) : null))))))),
    h('p', { class: 'fine' }, 'Colores y acceso: ', h('a', { href: '#/pago' }, 'ver opciones'), '. El tema claro u oscuro se cambia con el botón de la luna, arriba.'));
}
