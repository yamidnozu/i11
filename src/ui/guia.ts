import { h } from './dom';
import { tex, rich, eqn } from './tex';
import { atomize, mx, type Atom } from './automath';
import type { Question, Marca, Rol, Tarea } from '../content/schema';
import type { Ficha } from './ficha';

const ROLES: { r: Rol; n: string; t: string }[] = [
  { r: 'dato', n: 'Dato', t: 'Un número o condición que ya te dan. Ej.: «tiene 40 estudiantes»' },
  { r: 'pide', n: 'Lo que preguntan', t: 'Lo que debes encontrar. Ej.: «¿cuántos faltan?»' },
  { r: 'trampa', n: 'Ojo', t: 'Un detalle que confunde. Ej.: unidades distintas (km y m)' },
  { r: 'clave', n: 'Palabra clave', t: 'La palabra que te dice qué tema o camino usar. Ej.: «promedio», «el doble»' },
];

/** Compara el subrayado del estudiante con las marcas esperadas. Puro, para poder probarlo. */
export function evaluarMarcas(text: string, marcas: Marca[], tags: Record<number, Rol>) {
  const atoms = atomize(text);
  const found: Marca[] = [], missed: Marca[] = [];
  const tokenRole = new Map<number, Rol>();
  for (const m of marcas) {
    const i = text.indexOf(m.frag); if (i < 0) continue;
    const j = i + m.frag.length;
    const idx = atoms.map((_, k) => k).filter((k) => !atoms[k].space && atoms[k].start < j && atoms[k].end > i);
    idx.forEach((k) => tokenRole.set(k, m.rol));
    const hit = idx.filter((k) => tags[k] === m.rol).length;
    (idx.length && hit / idx.length >= 0.6 ? found : missed).push(m);
  }
  const extra = Object.keys(tags).map(Number).filter((k) => tokenRole.get(k) !== tags[k]);
  return { found, missed, extra, atoms, tokenRole };
}

export function parseNum(s: string): number {
  let t = s.trim().replace(/\s/g, '').replace(/^\$/, '').replace('−', '-');
  if (/^-?\d{1,3}(\.\d{3})+$/.test(t)) t = t.replace(/\./g, ''); else t = t.replace(/\./g, t.includes(',') ? '' : '.').replace(',', '.');
  return Number(t);
}

export function perm(n: number, seed: string): number[] {
  let x = 2166136261 >>> 0; for (const c of seed) x = Math.imul(x ^ c.charCodeAt(0), 16777619) >>> 0;
  const a = Array.from({ length: n }, (_, i) => i);
  for (let i = n - 1; i > 0; i--) { x = (Math.imul(x, 1664525) + 1013904223) >>> 0; const j = x % (i + 1); [a[i], a[j]] = [a[j], a[i]]; }
  return a;
}
const shuffle = <T,>(a: T[]): T[] => { const r = a.map((x, i) => [x, (i * 7 + 3) % (a.length + 1) + (i % 2) * 0.5] as [T, number]).sort((x, y) => x[1] - y[1]).map((x) => x[0]); return r.every((x, i) => x === a[i]) ? [...r.slice(1), r[0]] : r; };

export function crearGuia(q: Question, st: HTMLElement, ficha: Ficha, ctl: { onMarks(): void; onDone(): void }): { el: HTMLElement; start(): void } | null {
  const hoja = q.hoja; if (!hoja) return null;
  const tareas: { titulo: string; build: (done: () => void) => HTMLElement }[] = [];
  const marcas = (hoja.marcas ?? []).filter((m) => q.enunciado.includes(m.frag));
  if (marcas.length) tareas.push({ titulo: 'Subraya lo importante', build: (done) => marcar(q, marcas, st, ficha, () => { ctl.onMarks(); done(); }) });
  for (const t of hoja.guia ?? []) tareas.push({ titulo: t.titulo, build: (done) => (t.k === 'asignar' ? asignar(t, done) : t.k === 'llenar' ? llenar(t, done) : ordenar(t, done)) });
  if (!tareas.length) return null;
  const el = h('div', { class: 'guia', 'aria-live': 'polite' });
  let i = 0;
  const next = () => {
    if (i >= tareas.length) { ctl.onDone(); return; }
    const t = tareas[i++];
    const card = h('div', { class: 'tarea in' }, h('div', { class: 'hand ph' }, `${i} de ${tareas.length} · ${t.titulo}`));
    el.append(card);
    card.append(t.build(() => { card.classList.add('hecha'); next(); }));
    if (i === 1 && tareas[0].titulo.startsWith('Subraya')) st.scrollIntoView?.({ block: 'center', behavior: 'smooth' }); else card.scrollIntoView?.({ block: 'nearest', behavior: 'smooth' });
  };
  return { el, start: () => { if (!i) next(); } };
}

/** Aviso flotante: dice a dónde fue lo marcado y lleva allí con un toque, sin mover el scroll solo. */
function avisar(ficha: Ficha): void {
  document.querySelector('.toastf')?.remove();
  const t = h('div', { class: 'toastf', role: 'status' }, h('span', {}, '✓ Anotado en «Mis datos»'), h('button', { type: 'button', class: 'btn sm', onclick: () => { ficha.el.scrollIntoView({ block: 'center', behavior: 'smooth' }); t.remove(); } }, 'Ver mi hoja'));
  document.body.append(t);
  setTimeout(() => t.remove(), 4200);
}

function marcar(q: Question, marcas: Marca[], st: HTMLElement, ficha: Ficha, done: () => void): HTMLElement {
  const atoms = atomize(q.enunciado);
  const tags: Record<number, Rol> = {};
  const got = new Set<Marca>();
  let role: Rol = 'dato', anchor = -1, over = -1, down = false, busy = false;
  const E = () => [...st.querySelectorAll<HTMLElement>('.a')];
  const ROLCLS = ROLES.map((r) => `u-${r.r}`);
  const paint = () => E().forEach((n, k) => {
    n.classList.remove(...ROLCLS, 'sel');
    const r = tags[k] ?? (atoms[k].space && tags[k - 1] && tags[k - 1] === tags[k + 1] ? tags[k - 1] : undefined);
    if (r) n.classList.add(`u-${r}`);
    if (down && anchor >= 0 && k >= Math.min(anchor, over) && k <= Math.max(anchor, over)) n.classList.add('sel');
  });
  const at = (e: PointerEvent) => { const el = (e.target as HTMLElement).closest?.('.a') ?? document.elementFromPoint(e.clientX, e.clientY)?.closest('.a'); return el ? Number((el as HTMLElement).dataset.k) : -1; };
  const range = (a: number, b: number) => atoms.map((_, k) => k).filter((k) => k >= Math.min(a, b) && k <= Math.max(a, b) && !atoms[k].space);
  const msg = h('p', { class: 'hand nota' }), cnt = h('span', { class: 'fine' });
  const upd = () => { cnt.textContent = `Llevas ${got.size} de ${marcas.length}`; };
  const down_ = (e: PointerEvent) => { if (busy) return; const k = at(e); if (k < 0) return; e.preventDefault(); down = true; anchor = over = k; paint(); };
  const move_ = (e: PointerEvent) => { if (!down) return; const k = at(e); if (k >= 0 && k !== over) { over = k; paint(); } };
  const rangeOf = (m: Marca) => { const i = q.enunciado.indexOf(m.frag), j = i + m.frag.length; return atoms.map((_, k) => k).filter((k) => !atoms[k].space && atoms[k].start < j && atoms[k].end > i); };
  async function up_() {
    if (!down) return; down = false;
    const idx = range(anchor, over); anchor = over = -1;
    const all = idx.every((k) => tags[k] === role);
    const before = idx.map((k) => tags[k]);
    idx.forEach((k) => (all ? delete tags[k] : (tags[k] = role))); paint();
    if (all) { msg.textContent = ''; return; }
    const ev = evaluarMarcas(q.enunciado, marcas, tags);
    const nuevas = ev.found.filter((m) => !got.has(m));
    const roza = marcas.some((m) => rangeOf(m).some((k) => idx.includes(k)));
    if (nuevas.length) {
      busy = true; msg.textContent = '';
      for (const m of nuevas) { got.add(m); const r = rangeOf(m); await ficha.llenar(m, E().filter((_, k) => r.includes(k))); }
      avisar(ficha); upd(); busy = false;
      if (got.size === marcas.length) finish();
    } else if (!roza) {
      msg.textContent = 'Esa parte no es lo principal. Prueba con otra.'; msg.className = 'hand nota bad';
      idx.forEach((k, i) => { if (before[i]) tags[k] = before[i]; else delete tags[k]; }); E().forEach((n, k) => { if (idx.includes(k)) n.classList.add('sobra'); });
      setTimeout(() => { E().forEach((n) => n.classList.remove('sobra')); paint(); }, 900);
    } else { msg.textContent = 'Casi lo logras: revisa el tipo de marca o cuánto subrayaste.'; msg.className = 'hand nota'; }
  }
  st.classList.add('marcando');
  st.addEventListener('pointerdown', down_); st.addEventListener('pointermove', move_); st.addEventListener('pointerup', up_); st.addEventListener('pointercancel', up_);
  let cerrada = false;
  function finish() { if (cerrada) return; cerrada = true; st.classList.remove('marcando'); st.removeEventListener('pointerdown', down_); st.removeEventListener('pointermove', move_); st.removeEventListener('pointerup', up_); st.removeEventListener('pointercancel', up_); msg.textContent = got.size === marcas.length ? '¡Subrayaste todo lo importante!' : ''; msg.className = 'hand nota ok'; bFin.hidden = true; bShow.hidden = true; out.append(h('button', { class: 'btn sm primary', type: 'button', onclick: done }, 'Seguir')); }
  const pal = h('div', { class: 'pal', role: 'radiogroup', 'aria-label': 'Tipo de marca' }, ...ROLES.map((r) => h('button', { class: `rb m-${r.r}${r.r === role ? ' on' : ''}`, type: 'button', title: r.t, role: 'radio', onclick: (e: Event) => { role = r.r; pal.querySelectorAll('.rb').forEach((b) => b.classList.remove('on')); (e.currentTarget as HTMLElement).classList.add('on'); } }, r.n)));
  const out = h('div', { class: 'fbk' });
  const bShow = h('button', { class: 'btn sm', type: 'button', onclick: async () => { busy = true; for (const m of marcas) if (!got.has(m)) { got.add(m); const r = rangeOf(m); r.forEach((k) => (tags[k] = m.rol)); paint(); await ficha.llenar(m, E().filter((_, k) => r.includes(k))); } upd(); busy = false; finish(); } }, 'Muéstrame lo que falta');
  const bFin = h('button', { class: 'btn sm', type: 'button', onclick: () => { const faltan = marcas.filter((m) => !got.has(m)); out.replaceChildren(h('p', { class: 'fine' }, `Te faltaron ${faltan.length}: `), ...faltan.map((m) => h('div', { class: `mk m-${m.rol}` }, h('span', { class: 'chip' }, ROLES.find((r) => r.r === m.rol)!.n), h('span', { html: mx(m.frag) }), m.nota ? h('span', { class: 'hand' }, m.nota) : null))); bShow.click(); } }, 'Ya terminé');
  upd();
  return h('div', {}, h('div', { class: 'como' }, h('p', {}, h('b', {}, 'Qué hacer: '), 'lee el enunciado de arriba. Con el dedo o el cursor, pinta una parte importante y luego toca qué es: un dato, lo que preguntan, un ojo o una palabra clave.'), h('p', {}, h('b', {}, 'Para qué sirve: '), 'así separas lo que te dan de lo que te piden antes de calcular. Es lo primero que se hace en un examen.'), h('details', { class: 'leydet', open: !window.matchMedia('(max-width: 999px)').matches }, h('summary', {}, 'Qué significa cada botón'), h('ul', { class: 'leyenda' }, ...ROLES.map((r) => h('li', {}, h('b', { class: `m-${r.r}` }, r.n), ' — ', r.t)))), h('p', { class: 'fine' }, 'Si aciertas, se anota solo en tu hoja. Si no logras avanzar, toca «Muéstrame lo que falta».')), pal, h('div', { class: 'row' }, cnt, bFin, bShow), msg, out);
}

function asignar(t: Extract<Tarea, { k: 'asignar' }>, done: () => void): HTMLElement {
  let left = t.items.length;
  const wrap = h('div', { class: 'asig' });
  for (const it of t.items) {
    const fb = h('div', { class: 'hand nota' });
    const order = perm(it.op.length, it.p);
    const chips = order.map((i) => it.op[i]).map((o, pos) => { const i = order[pos]; return h('button', { class: 'cp', type: 'button', html: mx(o), onclick: (e: Event) => {
      const b = e.currentTarget as HTMLButtonElement;
      if (i === it.ok) { chips.forEach((c) => ((c as HTMLButtonElement).disabled = true)); b.classList.add('right'); fb.textContent = it.why; fb.className = 'hand nota ok'; if (--left === 0) setTimeout(done, 900); }
      else { b.classList.add('wrong'); b.disabled = true; fb.textContent = 'Todavía no. Míralo de nuevo.'; fb.className = 'hand nota bad'; }
    } }); });
    wrap.append(h('div', { class: 'ait' }, h('div', { class: 'ap', html: rich(it.p) }), h('div', { class: 'cps' }, ...chips), fb));
  }
  return wrap;
}

function llenar(t: Extract<Tarea, { k: 'llenar' }>, done: () => void): HTMLElement {
  let tries = 0;
  const inp = h('input', { class: 'num', type: 'text', inputmode: 'decimal', 'aria-label': 'Tu resultado', placeholder: '?' }) as HTMLInputElement;
  const fb = h('div', { class: 'hand nota' });
  const fin = (ok: boolean) => { inp.disabled = true; (b as HTMLButtonElement).disabled = true; fb.textContent = (ok ? '¡Eso! ' : 'La respuesta es ' + t.resp + '. ') + t.why; fb.className = 'hand nota ' + (ok ? 'ok' : 'bad'); setTimeout(done, 1200); };
  const check = () => { const v = parseNum(inp.value); if (!Number.isFinite(v)) { fb.textContent = 'Escribe un número.'; fb.className = 'hand nota bad'; return; } if (Math.abs(v - t.resp) <= (t.tol ?? 1e-9)) fin(true); else if (++tries >= 3) fin(false); else { fb.textContent = t.pista ?? 'Revisa la cuenta y las unidades.'; fb.className = 'hand nota bad'; } };
  const b = h('button', { class: 'btn sm primary', type: 'button', onclick: check }, 'Comprobar');
  inp.addEventListener('keydown', (e) => { if (e.key === 'Enter') { e.preventDefault(); check(); } });
  return h('div', {}, h('div', { class: 'ln', html: eqn(t.antes) }), h('div', { class: 'row' }, inp, t.unidad ? h('span', { html: mx(t.unidad) }) : null, b), fb);
}

function ordenar(t: Extract<Tarea, { k: 'ordenar' }>, done: () => void): HTMLElement {
  const pool = shuffle(t.items); const pick: string[] = [];
  const seq = h('ol', { class: 'seq' }), fb = h('div', { class: 'hand nota' }), box = h('div', { class: 'cps' });
  const btns = pool.map((o) => h('button', { class: 'cp', type: 'button', html: mx(o), onclick: (e: Event) => {
    const b = e.currentTarget as HTMLButtonElement; b.disabled = true; pick.push(o); seq.append(h('li', { html: mx(o) }));
    if (pick.length === t.items.length) {
      if (pick.every((x, i) => x === t.items[i])) { fb.textContent = '¡En orden! ' + t.why; fb.className = 'hand nota ok'; setTimeout(done, 1200); }
      else { fb.textContent = 'Ese orden no es correcto. Inténtalo de nuevo.'; fb.className = 'hand nota bad'; pick.length = 0; seq.replaceChildren(); btns.forEach((x) => ((x as HTMLButtonElement).disabled = false)); }
    }
  } }));
  box.append(...btns);
  return h('div', {}, h('p', { class: 'fine' }, 'Toca en el orden correcto, de primero a último.'), box, seq, fb);
}
