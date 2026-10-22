import { h } from './dom';
import { mx } from './automath';
import { rich } from './tex';
import type { Question, Marca, Rol } from '../content/schema';

/** Velocidad de las animaciones (1 = normal). */
export const vel = { x: 1 };
export const reducido = () => typeof matchMedia !== 'undefined' && matchMedia('(prefers-reduced-motion: reduce)').matches;

const ORDEN: Rol[] = ['dato', 'pide', 'trampa', 'clave'];
const LAB: Record<string, Record<Rol, [string, string]>> = {
  calculo: { dato: ['Datos', 'Dato'], pide: ['Lo que preguntan', 'Piden'], trampa: ['Ojo', 'Ojo'], clave: ['Clave', 'Clave'] },
  lectura: { dato: ['Qué dice', 'Dice'], pide: ['Qué preguntan', 'Pregunta'], trampa: ['Ojo', 'Ojo'], clave: ['Idea clave', 'Clave'] },
  historia: { dato: ['Hechos y fuentes', 'Hecho'], pide: ['Qué preguntan', 'Piden'], trampa: ['Ojo', 'Ojo'], clave: ['Concepto clave', 'Clave'] },
  concepto: { dato: ['Datos', 'Dato'], pide: ['Qué preguntan', 'Piden'], trampa: ['Ojo', 'Ojo'], clave: ['Concepto', 'Clave'] },
};

export interface Ficha {
  el: HTMLElement;
  mostrar(): void;
  llenar(m: Marca, src: HTMLElement[], rapido?: boolean): Promise<void>;
  flash(ms: Marca[]): void;
  llenarTodo(): void;
  tiene(m: Marca): boolean;
}

/** Ficha "Mis datos": se va llenando con lo que sale del enunciado. */
export function crearFicha(q: Question): Ficha {
  const marcas = (q.hoja?.marcas ?? []).filter((m) => q.enunciado.includes(m.frag));
  const lab = LAB[q.hoja?.modo ?? 'calculo'];
  const el = h('section', { class: 'ficha', 'aria-label': 'Mis datos', 'aria-live': 'polite' }, h('div', { class: 'hand fh' }, 'Mis datos'));
  const body = h('div', { class: 'fgrid' }); el.append(body);
  const sec = new Map<Rol, HTMLElement>();
  for (const r of ORDEN) if (marcas.some((m) => m.rol === r)) {
    const rows = h('div', { class: 'frows' }, h('div', { class: 'fe' }, '—'));
    const box = h('div', { class: `fsec m-${r}` }, h('div', { class: 'ft' }, lab[r][0]), rows);
    sec.set(r, rows); body.append(box);
  }
  const rowOf = new Map<Marca, HTMLElement>();
  const nuevoRow = (m: Marca): HTMLElement => {
    const rows = sec.get(m.rol)!; rows.querySelector('.fe')?.remove();
    const row = h('div', { class: `frow m-${m.rol} nuevo` }, h('span', { class: 'chip' }, m.w ?? lab[m.rol][1]), h('span', { class: 'fv', html: m.campo ? rich(m.campo) : mx(m.frag) }), m.nota && m.nota.replace(/\s/g, '') !== (m.campo ?? '').replace(/\s/g, '') ? h('span', { class: 'hand fn' }, m.nota) : null);
    rows.append(row); rowOf.set(m, row); return row;
  };
  const aterriza = (row: HTMLElement) => { row.classList.remove('nuevo'); row.classList.add('lleno'); };
  return {
    el,
    mostrar: () => { el.classList.add('on'); },
    tiene: (m) => rowOf.has(m),
    async llenar(m, src, rapido) {
      if (rowOf.has(m) || !sec.has(m.rol)) return;
      el.classList.add('on');
      const row = nuevoRow(m);
      if (!rapido) { src[0]?.scrollIntoView?.({ block: 'nearest', behavior: 'auto' }); el.scrollIntoView?.({ block: 'nearest', behavior: 'auto' }); row.scrollIntoView?.({ block: 'nearest', behavior: 'auto' }); } // que se vea de dónde sale y adónde llega
      if (rapido || reducido() || !src.length || !row.animate) { aterriza(row); return; }
      const rs = src.map((e) => e.getBoundingClientRect());
      const L = Math.min(...rs.map((r) => r.left)), T = Math.min(...rs.map((r) => r.top)), R = Math.max(...rs.map((r) => r.right)), B = Math.max(...rs.map((r) => r.bottom));
      const fly = h('div', { class: `fly m-${m.rol}`, html: mx(m.frag) });
      Object.assign(fly.style, { left: L + 'px', top: T + 'px', minWidth: R - L + 'px', height: B - T + 'px' });
      document.body.append(fly);
      const tr = row.getBoundingClientRect();
      const dx = tr.left - L, dy = tr.top - T;
      try {
        await fly.animate([{ transform: 'translate(0,0) scale(1)', opacity: 1 }, { transform: `translate(${dx * 0.45}px,${dy * 0.45 - 46}px) scale(1.18)`, opacity: 1, offset: 0.45 }, { transform: `translate(${dx}px,${dy}px) scale(1)`, opacity: 0.95 }], { duration: 1300 / vel.x, easing: 'cubic-bezier(.4,0,.2,1)' }).finished;
      } catch { /* cancelada */ }
      fly.remove(); aterriza(row);
    },
    flash(ms) { for (const m of ms) { const r = rowOf.get(m); if (r) { r.classList.remove('flash'); void r.offsetWidth; r.classList.add('flash'); } } },
    llenarTodo() { el.classList.add('on'); for (const m of marcas) if (!rowOf.has(m)) aterriza(nuevoRow(m)); },
  };
}
