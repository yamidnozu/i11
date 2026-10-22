import { h } from './dom';
import { AREAS, AREA_IDS, type AreaId } from '../adaptive/areas';
import { NIVELES, nivelIndex } from '../content/niveles';

/** «Tu nivel en cada prueba»: qué demuestras hoy y qué te falta para el siguiente (descriptores oficiales de niveles de desempeño). */
export function nivelesPanel(sc: Partial<Record<AreaId, number>>): HTMLElement | null {
  const areas = AREA_IDS.filter((a) => sc[a] !== undefined);
  if (!areas.length) return null;
  return h('section', { class: 'nivpan', 'aria-label': 'Tu nivel en cada prueba' }, h('h2', {}, 'Tu nivel en cada prueba'),
    h('p', { class: 'fine' }, 'Cada prueba tiene 4 niveles. Abre una para ver qué demuestras hoy y qué sigue para subir.'),
    ...areas.map((a) => {
      const v = Math.round(sc[a]!), i = nivelIndex(a, v), n = NIVELES[a][i], sig = NIVELES[a][i + 1];
      return h('details', { class: 'nivd' }, h('summary', {}, h('b', {}, AREAS[a].nombre), h('span', { class: 'tag' }, n.nombre), h('small', {}, `${v} de 100 · ${n.resumen}`)),
        h('div', { class: 'nivb' }, h('h3', {}, `Lo que ya demuestras (${n.nombre})`), h('ul', {}, ...n.demuestra.map((t) => h('li', {}, t))),
          sig ? h('div', {}, h('h3', {}, `Para llegar a ${sig.nombre} (desde ${sig.desde} puntos)`), h('p', { class: 'fine' }, sig.resumen), h('ul', {}, ...sig.demuestra.map((t) => h('li', {}, t)))) : h('p', { class: 'fine' }, 'Estás en el nivel más alto de esta prueba.')));
    }));
}
