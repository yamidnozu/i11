import { h } from './dom';
import { rich } from './tex';
import { escenaCanvas } from './hoja';
import type { Figura, Bloque } from '../content/schema';

/** Limpia un SVG escrito en el JSON: sin scripts, sin eventos, sin enlaces peligrosos. */
export function svgSeguro(src: string): string {
  const doc = new DOMParser().parseFromString(src, 'image/svg+xml');
  const svg = doc.documentElement;
  if (!svg || svg.nodeName.toLowerCase() !== 'svg' || doc.querySelector('parsererror')) return '';
  svg.querySelectorAll('script,foreignObject,iframe,object,embed').forEach((n) => n.remove());
  [svg, ...Array.from(svg.querySelectorAll('*'))].forEach((el) => Array.from(el.attributes).forEach((a) => { if (/^on/i.test(a.name) || /javascript:/i.test(a.value)) el.removeAttribute(a.name); }));
  svg.setAttribute('role', 'img'); svg.removeAttribute('width'); svg.removeAttribute('height');
  return new XMLSerializer().serializeToString(svg);
}

function ampliar(contenido: () => HTMLElement, alt: string) {
  const dlg = h('div', { class: 'zoomf', role: 'dialog', 'aria-modal': 'true', 'aria-label': alt, tabindex: '-1' }, h('button', { class: 'btn sm zx', type: 'button', onclick: () => dlg.remove() }, 'Cerrar'), h('div', { class: 'zbody' }, contenido()));
  dlg.addEventListener('click', (e) => { if (e.target === dlg) dlg.remove(); });
  dlg.addEventListener('keydown', (e) => { if ((e as KeyboardEvent).key === 'Escape') dlg.remove(); });
  document.body.append(dlg); dlg.focus();
}

function cuerpo(f: Figura): HTMLElement {
  switch (f.tipo) {
    case 'img': { const i = h('img', { src: f.src, alt: f.alt, loading: 'lazy', ...(f.ancho ? { style: `max-width:${f.ancho}px` } : {}) }); return i; }
    case 'svg': return h('div', { class: 'fsvg', html: svgSeguro(f.svg) });
    case 'escena': return escenaCanvas({ ...f, titulo: f.alt });
    case 'pendiente': return h('div', { class: 'fpend', role: 'img', 'aria-label': f.alt }, h('b', {}, 'Figura pendiente'), h('span', {}, f.pagina ? `Página ${f.pagina} del cuadernillo` : 'Aún sin cargar'), h('small', {}, f.alt));
    case 'tabla': return h('table', { class: 'ft' }, h('thead', {}, h('tr', {}, ...f.cols.map((c) => h('th', { html: rich(c) })))), h('tbody', {}, ...f.filas.map((r) => h('tr', {}, ...r.map((c) => h('td', { html: rich(c) }))))));
  }
}
/** Una figura del examen, con pie y botón para ampliar. */
export function figuraEl(f: Figura, opts: { compacta?: boolean } = {}): HTMLElement {
  const alt = (f as { alt?: string }).alt ?? 'Tabla de datos';
  return h('figure', { class: `fig fig-${f.tipo}${opts.compacta ? ' compacta' : ''}` }, h('div', { class: 'figc' }, cuerpo(f)), f.pie ? h('figcaption', { html: rich(f.pie) }) : null,
    opts.compacta ? null : h('button', { class: 'btn sm figz', type: 'button', 'aria-label': `Ampliar: ${alt}`, onclick: () => ampliar(() => cuerpo(f), alt) }, 'Ampliar'));
}

/** Contexto compartido: encabezado oficial, título, texto, figuras y fuente. `rango` = «4 A 6». */
export function bloqueEl(b: Bloque, rango?: string): HTMLElement {
  const enc = b.encabezado ?? 'DE ACUERDO CON LA SIGUIENTE INFORMACIÓN';
  return h('section', { class: 'bloque', 'aria-label': b.titulo ?? 'Contexto' },
    rango ? h('p', { class: 'benc' }, `RESPONDE LAS PREGUNTAS ${rango} ${enc}`) : h('p', { class: 'benc' }, enc),
    b.titulo ? h('h3', { class: 'btit' }, b.titulo) : null,
    b.texto ? h('div', { class: 'btxt' }, ...b.texto.split(/\n\s*\n/).map((par) => h('p', { html: rich(par).replace(/\n/g, '<br>') }))) : null,
    ...(b.figuras ?? []).map((f) => figuraEl(f)),
    b.fuente ? h('p', { class: 'bfue' }, b.fuente) : null);
}
