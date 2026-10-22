import { h } from './dom';
import type { Question } from '../content/schema';
import { AREAS } from '../adaptive/areas';
import { getSim } from '../core/registry';
import { mountSim } from '../core/engine';
import { anotar, crearHoja } from './hoja';
import { mx } from './automath';
import { rich } from './tex';
import { vincularDatos } from './vinculos';
import { figuraEl, bloqueEl } from './figura';
import { bloqueDe } from '../content';

const L = 'ABCDEFGH';
const decirEn = (s: string) => s.replace(/^(Choose the correct option|Complete|Sign):\s*/i, '').replace(/[«»]/g, '').replace(/\s+/g, ' ').trim();
const oirBar = (enun: string) => h('div', { class: 'oir' }, h('button', { class: 'oirb', type: 'button', 'data-en': decirEn(enun) }, h('i', { class: 'spki' }), 'Escuchar'), h('button', { class: 'oirb', type: 'button', 'data-en': decirEn(enun), 'data-lento': '1' }, h('i', { class: 'spki' }), 'Despacio'));
export const dots = (n: number) => h('span', { class: 'dots', role: 'img', 'aria-label': `Nivel ${n} de 4` }, ...[1, 2, 3, 4].map((i) => h('i', { class: i <= n ? 'on' : '' })));

/** Pregunta de opción múltiple o reto con simulador. `onDone(ok)` se llama una sola vez. Atajos: A–D o 1–4. */
export function renderQuestion(q: Question, onDone: (ok: boolean) => void, opts: { feedback?: boolean; ayuda?: 'siempre' | 'despues'; rango?: string; sinBloque?: boolean; revisar?: { elegida: number }; examen?: { elegida: number; onPick: (i: number) => void } } = {}): HTMLElement {
  const feedback = opts.feedback !== false;
  const sim = q.tipo === 'reto' && q.sim;
  const ayuda = opts.ayuda ?? 'despues';
  const st = anotar(q.enunciado, q.hoja?.marcas);
  const box = h('section', { class: 'qcard', 'data-kind': sim ? 'sim' : 'mc', ...(opts.examen || opts.revisar ? { 'data-libre': '1' } : {}), 'aria-labelledby': `q-${q.id}` });
  let done = false;
  const finish = (ok: boolean) => { if (done) return; done = true; onDone(ok); };
  const left = h('div', { class: 'qleft' }), right = h('div', { class: 'qright' });
  left.append(h('div', { class: 'qmeta' }, h('span', { class: 'tag' }, AREAS[q.area].nombre), dots(q.nivel), sim ? h('span', {}, 'Reto con laboratorio') : null), h('h2', { class: 'qtext', id: `q-${q.id}` }, st), ...(q.area === 'ingles' && !q.lectura ? [oirBar(q.enunciado)] : []));

  if (q.figuras?.length) left.querySelector('.qtext')!.after(...q.figuras.map((f) => figuraEl(f)));
  if (q.origen === 'icfes' && q.fuente) left.append(h('p', { class: 'qfuente' }, `Fuente: ${q.fuente}`));
  const bl = !opts.sinBloque ? bloqueDe(q) : undefined;
  if (bl) left.prepend(bloqueEl(bl, opts.rango));
  if (q.lectura) left.prepend(h('details', { class: 'lectura', open: true }, h('summary', {}, h('b', {}, q.lectura.titulo), h('small', {}, 'Léelo una vez; las preguntas de este texto lo usan')), h('div', { class: 'ltxt', html: rich(q.lectura.texto) })));
  box.append(left);
  if (q.tipo === 'reto' && q.sim) {
    const lab = getSim(q.sim.id)!;
    const host = h('div');
    box.append(host, h('div', { class: 'row', style: 'margin-top:14px' }, h('button', { class: 'btn', type: 'button', onclick: () => { finish(false); box.append(h('div', { class: 'fb bad' }, h('span', { class: 'hand' }, 'Solución'), h('p', {}, q.explicacion))); } }, 'No sé: ver la explicación')));
    mountSim(lab, host, { challengeId: q.sim.challengeId, onResult: (ok) => { if (ok) { finish(true); box.append(h('div', { class: 'fb ok' }, h('span', { class: 'hand' }, '¡Reto resuelto!'), h('p', {}, q.explicacion))); } } });
    return box;
  }
  const list = h('div', { class: 'opts', role: 'radiogroup', 'aria-label': 'Opciones' });
  const btns = q.opciones.map((o, i) => h('button', { class: 'opt', type: 'button', role: 'radio', 'aria-checked': 'false', onclick: () => choose(i) }, h('b', {}, L[i]), q.opcionesFig?.[i] ? h('span', { class: 'ofig' }, figuraEl(q.opcionesFig[i]!, { compacta: true }), o.length > 1 ? h('span', { html: mx(o) }) : null) : h('span', { html: mx(o) }), ...(q.area === 'ingles' ? [h('span', { class: 'spk', role: 'button', tabindex: '0', 'aria-label': 'Escuchar esta opción', 'data-en': o })] : [])));
  list.append(...btns);
  left.append(list);
  const hoja = crearHoja(q, feedback, st);
  right.append(hoja.el);
  if (q.hoja && feedback) { box.classList.add('dos'); box.append(right); }
  let pista: HTMLElement | null = null;
  if (q.hoja && feedback && ayuda === 'despues') {
    hoja.el.hidden = true; hoja.ficha.el.hidden = true; right.hidden = true;
    const abrir = () => { right.hidden = false; hoja.el.hidden = false; hoja.ficha.el.hidden = false; hoja.ir('tema'); pista?.remove(); right.scrollIntoView({ block: 'nearest', behavior: 'smooth' }); };
    pista = h('div', { class: 'tryfirst' }, h('p', {}, 'Inténtala tú primero. Piensa qué te piden y qué datos tienes.'), h('button', { class: 'btn sm', type: 'button', onclick: abrir }, 'Necesito ayuda'));
    list.after(pista);
  }
  function choose(i: number) {
    if (opts.examen) { btns.forEach((b, k) => { b.setAttribute('aria-checked', String(k === i)); b.classList.toggle('picked', k === i); }); opts.examen.onPick(i); return; }
    if (done) return;
    const ok = i === q.correcta;
    box.classList.add('resp');
    if (i < 0) { btns.forEach((b, k) => { (b as HTMLButtonElement).disabled = true; if (k === q.correcta) b.classList.add('right'); }); pista?.remove(); hoja.todo(true); right.hidden = false; hoja.el.hidden = false; hoja.ficha.el.hidden = false; left.append(h('div', { class: 'fb bad', role: 'status' }, h('span', { class: 'hand' }, 'La dejaste en blanco'), h('p', { html: rich(q.explicacion) }))); finish(false); return; }
    btns.forEach((b, k) => { (b as HTMLButtonElement).disabled = true; if (feedback && k === q.correcta) b.classList.add('right'); });
    btns[i].setAttribute('aria-checked', 'true');
    if (feedback) {
      pista?.remove(); const yaAbierta = !right.hidden; hoja.todo(true); right.hidden = false; hoja.el.hidden = false; hoja.ficha.el.hidden = false; if (!yaAbierta) hoja.ir('expl');
      btns[i].classList.add(ok ? 'right' : 'wrong');
      const why = !ok && q.distractores[i] ? h('p', { html: '<b>Por qué tienta:</b> ' + rich(q.distractores[i]) }) : null;
      left.append(h('div', { class: 'fb ' + (ok ? 'ok' : 'bad'), role: 'status' }, h('span', { class: 'hand' }, ok ? '¡Bien!' : 'Todavía no'), why, h('p', { html: rich(q.explicacion) }), q.hoja ? h('button', { class: 'btn sm', type: 'button', onclick: () => { hoja.ir('expl'); right.scrollIntoView({ block: 'start', behavior: 'smooth' }); } }, 'Que el profe me lo explique') : null));
      if (q.sim) { const s = getSim(q.sim.id); if (s) left.append(h('a', { class: 'btn sm', style: 'margin-top:12px', href: `#/sim/${s.id}` }, 'Verlo en el laboratorio')); }
    } else btns[i].classList.add('picked');
    finish(ok);
  }
  vincularDatos(box, q.hoja?.marcas, q.enunciado);
  if (opts.examen && opts.examen.elegida >= 0) { btns[opts.examen.elegida]?.setAttribute('aria-checked', 'true'); btns[opts.examen.elegida]?.classList.add('picked'); }
  if (opts.revisar) queueMicrotask(() => choose(opts.revisar!.elegida));
  return box;
}

/** Atajos globales: A–H / 1–8 eligen opción, Enter pasa a la siguiente. */
export function initKeys() {
  document.addEventListener('keydown', (e) => {
    const t = e.target as HTMLElement;
    if (e.metaKey || e.ctrlKey || e.altKey || /^(INPUT|TEXTAREA|SELECT)$/.test(t.tagName)) return;
    const q = document.querySelector('.qcard[data-kind="mc"]');
    if (!q) return;
    const k = e.key.toLowerCase(), idx = k.length === 1 && 'abcdefgh'.indexOf(k) >= 0 ? 'abcdefgh'.indexOf(k) : k.length === 1 && '12345678'.indexOf(k) >= 0 ? '12345678'.indexOf(k) : -1;
    if (idx >= 0) { const b = q.querySelectorAll<HTMLButtonElement>('.opt')[idx]; if (b && !b.disabled) { e.preventDefault(); b.click(); } return; }
    if (e.key === 'Enter') { const n = document.querySelector<HTMLButtonElement>('button.next'); if (n && t.tagName !== 'BUTTON') { e.preventDefault(); n.click(); } }
  });
}
