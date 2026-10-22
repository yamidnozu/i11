import { h } from './dom';
import { tex, rich, eqn } from './tex';
import { atomize, mx } from './automath';
import { crearPad } from './pad';
import { crearGuia } from './guia';
import { crearFicha, type Ficha } from './ficha';
import { crearDemo } from './demo';
import type { Question, Marca, Paso, Rol } from '../content/schema';
import { pintarEscena } from '../lab/scene';
import { ev } from '../lab/expr';

const L = 'ABCDEFGH';
const ROL: Record<Rol, string> = { dato: 'Dato', pide: 'Lo que preguntan', trampa: 'Ojo', clave: 'Palabra clave' };
const esc = (s: string) => s.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');

/** Enunciado con números tipografiados; cada palabra es un átomo que se puede subrayar, animar y arrastrar a la ficha. */
export function anotar(texto: string, marcas: Marca[] = []): HTMLElement {
  const atoms = atomize(texto);
  const rol: (Rol | '')[] = atoms.map(() => '');
  for (const m of marcas) {
    const i = texto.indexOf(m.frag); if (i < 0) continue;
    const j = i + m.frag.length;
    atoms.forEach((a, k) => { if (a.start < j && a.end > i && !rol[k]) rol[k] = m.rol; });
  }
  const out = atoms.map((a, k) => { let r = rol[k]; if (a.space) r = rol[k - 1] && rol[k - 1] === rol[k + 1] ? rol[k - 1] : ''; return `<span class="a${a.space ? ' sp' : ''}" data-k="${k}"${r ? ` data-r="${r}"` : ''}>${a.html}</span>`; }).join('');
  return h('span', { class: 'anot', html: out });
}

/** Gráfica de una cuadrática con puntos marcados (SVG en línea, sin librerías). */
function graficaSvg(coef: [number, number, number], xr: [number, number], pts: { x: number; y: number; l: string }[]): string {
  const [a, b, c] = coef, f = (x: number) => a * x * x + b * x + c;
  const W = 340, H = 230, M = 30, [x0, x1] = xr;
  const xs = Array.from({ length: 121 }, (_, i) => x0 + ((x1 - x0) * i) / 120);
  let y0 = Math.min(0, ...xs.map(f), ...pts.map((p) => p.y)), y1 = Math.max(0, ...xs.map(f), ...pts.map((p) => p.y));
  const pad = (y1 - y0) * 0.12 || 1; y0 -= pad; y1 += pad;
  const X = (x: number) => M + ((x - x0) / (x1 - x0)) * (W - 2 * M), Y = (y: number) => H - M - ((y - y0) / (y1 - y0)) * (H - 2 * M);
  const stepY = (y1 - y0) > 12 ? 2 : 1; let g = '', t = '';
  const raw = (x1 - x0) / 8, sx = raw <= 1 ? 1 : raw <= 2 ? 2 : raw <= 5 ? 5 : 10;
  for (let x = Math.ceil(x0 / sx) * sx; x <= x1; x += sx) { g += `<line class="gr" x1="${X(x)}" y1="${M / 2}" x2="${X(x)}" y2="${H - M / 2}"/>`; t += `<text class="tk" x="${X(x)}" y="${Y(0) + 14}" text-anchor="middle">${x}</text>`; }
  for (let y = Math.ceil(y0 / stepY) * stepY; y <= Math.floor(y1); y += stepY) { g += `<line class="gr" x1="${M / 2}" y1="${Y(y)}" x2="${W - M / 2}" y2="${Y(y)}"/>`; if (y !== 0) t += `<text class="tk" x="${X(0) - 6}" y="${Y(y) + 4}" text-anchor="end">${y}</text>`; }
  const d = xs.map((x, i) => `${i ? 'L' : 'M'}${X(x).toFixed(1)},${Y(f(x)).toFixed(1)}`).join('');
  const dots = pts.map((p) => `<circle class="pt" cx="${X(p.x)}" cy="${Y(p.y)}" r="6"/><text class="pl" x="${X(p.x)}" y="${Y(p.y) + (p.y === 0 ? 34 : -12)}" text-anchor="middle">${esc(p.l)}</text>`).join('');
  return `<svg class="gf" viewBox="0 0 ${W} ${H}" role="img" aria-label="Gráfica de la función">${g}<line class="ax" x1="${M / 2}" y1="${Y(0)}" x2="${W - M / 2}" y2="${Y(0)}"/><line class="ax" x1="${X(0)}" y1="${M / 2}" x2="${X(0)}" y2="${H - M / 2}"/><text class="ek" x="${W - M / 2}" y="${Y(0) - 6}" text-anchor="end">x</text><text class="ek" x="${X(0) + 6}" y="${M / 2 + 8}">y</text>${t}<path class="cv" d="${d}"/>${dots}</svg>`;
}

/** Paso «escena»: dibujo declarativo (JSON) con animación opcional. Usa las mismas piezas que los laboratorios. */
export function escenaCanvas(p: Pick<Extract<Paso, { k: 'escena' }>, 'ancho' | 'alto' | 'marco' | 'capas' | 'vars' | 'anim' | 'titulo'>): HTMLElement {
  const cv = document.createElement('canvas'); cv.width = p.ancho; cv.height = p.alto; cv.className = 'escv'; cv.setAttribute('role', 'img'); cv.setAttribute('aria-label', p.titulo ?? 'Ilustración');
  const ctx = cv.getContext('2d'); if (!ctx) return cv;
  const vars = (u: number) => { const sc: Record<string, unknown> = { u, t: u * (p.anim?.dur ?? 1) }; for (const [k, v] of Object.entries(p.vars ?? {})) sc[k] = ev(v, sc); return sc; };
  const pinta = (u: number) => { ctx.clearRect(0, 0, p.ancho, p.alto); ctx.fillStyle = '#121821'; ctx.fillRect(0, 0, p.ancho, p.alto); try { pintarEscena({ ancho: p.ancho, alto: p.alto, marco: p.marco, capas: p.capas }, vars(u), ctx, p.ancho, p.alto); } catch { /* escena mal formada: se muestra vacía */ } };
  pinta(1);
  const quieto = typeof matchMedia === 'function' && matchMedia('(prefers-reduced-motion: reduce)').matches;
  if (p.anim && !quieto && typeof requestAnimationFrame === 'function') {
    let t0 = 0, vivo = true, fuera = 0;
    const tick = (now: number) => { if (!cv.isConnected) { if (++fuera > 120) return; requestAnimationFrame(tick); return; } fuera = 0; if (!t0) t0 = now; const k = (now - t0) / (p.anim!.dur * 1000); const u = p.anim!.bucle ? k % 1 : Math.min(1, k); pinta(u); if (vivo && (p.anim!.bucle || k < 1)) requestAnimationFrame(tick); };
    requestAnimationFrame(tick);
  }
  return cv;
}

function pasoEl(p: Paso): HTMLElement {
  const head = (t?: string) => (t ? h('div', { class: 'hand ph' }, t) : null);
  switch (p.k) {
    case 'idea': return h('li', { class: 'paso' }, head(p.titulo), h('p', { html: rich(p.texto) }));
    case 'calc': return h('li', { class: 'paso' }, head(p.titulo), ...p.lineas.map((l) => h('div', { class: 'ln', html: eqn(l) })), p.nota ? h('div', { class: 'hand nota', html: rich(p.nota) }) : null);
    case 'tabla': return h('li', { class: 'paso' }, head(p.titulo), h('table', { class: 'ht' }, h('thead', {}, h('tr', {}, ...p.cols.map((c) => h('th', { html: rich(c) })))), h('tbody', {}, ...p.filas.map((f) => h('tr', {}, ...f.map((c) => h('td', { html: rich(c.replace(/^\*/, '')), class: c.startsWith('*') ? 'hit' : '' })))))));
    case 'ejemplo': return h('li', { class: 'paso' }, head(p.titulo), h('div', { class: 'two' }, h('div', { class: 'si' }, h('b', {}, 'Sí'), h('ul', {}, ...p.si.map((x) => h('li', { html: rich(x) })))), h('div', { class: 'no' }, h('b', {}, 'No'), h('ul', {}, ...p.no.map((x) => h('li', { html: rich(x) }))))));
    case 'linea': return h('li', { class: 'paso' }, head(p.titulo), h('ol', { class: 'tl' }, ...p.eventos.map((e) => h('li', { class: `ev ${e.rol}` }, h('b', { class: 'yr' }, e.anio), h('div', {}, h('strong', {}, e.t), h('span', {}, e.d))))));
    case 'traducir': return h('li', { class: 'paso' }, head(p.titulo), h('div', { class: 'trad' }, ...p.filas.map((f) => h('div', { class: `ln tr${f.rol ? ' m-' + f.rol : ''}` }, h('q', { html: rich(f.dice) }), h('span', { class: 'ar', 'aria-hidden': 'true' }, '→'), h('span', { class: 'es', html: eqn(f.escribo) })))), p.nota ? h('div', { class: 'hand nota', html: rich(p.nota) }) : null);
    case 'tanteo': return h('li', { class: 'paso' }, head(p.titulo), h('div', { class: 'busco', html: rich(p.busco) }), h('div', { class: 'tant' }, h('div', { class: 'tr0' }, ...p.cols.map((c) => h('span', { html: rich(c) }))), ...p.filas.map((f) => h('div', { class: `ln tr1 ${f.ok ? 'ok' : 'no'}` }, h('span', { html: rich(f.a) }), h('span', { html: rich(f.b) }), h('span', { html: rich(f.c) }), h('span', { class: 'mk2', 'aria-label': f.ok ? 'sirve' : 'no sirve' }, f.ok ? '✓' : '✕')))), p.nota ? h('div', { class: 'hand nota', html: rich(p.nota) }) : null);
    case 'puntos': return h('li', { class: 'paso' }, head(p.titulo), h('div', { class: 'grupos ln' }, ...p.grupos.map((g) => h('div', { class: `grp c-${g.c}` }, h('div', { class: 'dots', 'aria-hidden': 'true' }, ...Array.from({ length: g.n }, () => h('i', { class: 'dt' }))), h('span', { class: 'gl', html: `<b>${g.n}</b> ${esc(g.l)}` })))), ...(p.lineas ?? []).map((l) => h('div', { class: 'ln', html: eqn(l) })), p.nota ? h('div', { class: 'hand nota', html: rich(p.nota) }) : null);
    case 'grafica': return h('li', { class: 'paso' }, head(p.titulo), h('div', { class: 'ln gfw', html: graficaSvg(p.coef, p.x, p.puntos) }), p.nota ? h('div', { class: 'hand nota', html: rich(p.nota) }) : null);
    case 'barras': { const max = Math.max(...p.barras.map((b) => b.segs.reduce((s, x) => s + x.v, 0)), p.ref?.v ?? 0);
      return h('li', { class: 'paso' }, head(p.titulo), h('div', { class: 'brs' }, ...p.barras.map((b) => h('div', { class: 'ln br' }, h('div', { class: 'brl' }, h('span', { html: rich(b.l) }), h('b', { html: rich(b.e) })), h('div', { class: 'brt' }, ...b.segs.map((s) => h('i', { class: `sg c-${s.c}`, style: `width:${(s.v / max) * 100}%` })), p.ref ? h('u', { class: 'rf', style: `left:${(p.ref.v / max) * 100}%` }) : null))), p.ref ? h('div', { class: 'rfl', html: `┆ ${esc(p.ref.l)}` }) : null), p.nota ? h('div', { class: 'hand nota', html: rich(p.nota) }) : null); }
    case 'flujo': return h('li', { class: 'paso' }, head(p.titulo), h('div', { class: 'flj' }, ...p.nodos.flatMap((n, i) => [h('div', { class: 'ln nd' }, h('b', { html: rich(n.v) }), n.l ? h('span', { html: rich(n.l) }) : null), i < p.saltos.length ? h('div', { class: 'ln sl' }, h('i', {}, '↓'), h('span', { html: eqn(p.saltos[i]) })) : null])), p.nota ? h('div', { class: 'hand nota', html: rich(p.nota) }) : null);
    case 'escena': return h('li', { class: 'paso' }, head(p.titulo), h('div', { class: 'ln escf' }, escenaCanvas(p)), p.nota ? h('div', { class: 'hand nota', html: rich(p.nota) }) : null);
    case 'vida': return h('li', { class: 'paso vida' }, head(p.titulo ?? 'En la vida real'), h('p', { html: rich(p.texto) }));
    case 'glosa': { const full = p.frase.map((w) => w.en).join(' ');
      return h('li', { class: 'paso' }, head(p.titulo), h('div', { class: 'ln gls' }, ...p.frase.map((w) => h('button', { class: 'gw', type: 'button', 'data-en': w.en }, h('b', {}, w.en), h('span', { class: 'es', html: rich(w.es) }), ...(w.pron ? [h('small', { class: 'pr' }, w.pron)] : [])))), h('div', { class: 'ln glf' }, h('button', { class: 'oirb', type: 'button', 'data-en': full }, h('i', { class: 'spki' }), 'Oír la frase'), h('button', { class: 'oirb', type: 'button', 'data-en': full, 'data-lento': '1' }, h('i', { class: 'spki' }), 'Despacio')), h('div', { class: 'ln gd', html: '= ' + rich(p.dice) }), ...(p.nota ? [h('div', { class: 'hand nota', html: rich(p.nota) })] : [])); }
    case 'escucha': return h('li', { class: 'paso' }, head(p.titulo), h('div', { class: 'esc' }, ...p.frases.map((f) => h('div', { class: 'ln er' }, h('button', { class: 'oirb', type: 'button', 'data-en': f.en, 'aria-label': 'Oír' }, h('i', { class: 'spki' })), h('button', { class: 'oirb lento', type: 'button', 'data-en': f.en, 'data-lento': '1', 'aria-label': 'Oír despacio' }, '0.6×'), h('div', { class: 'et' }, h('b', { lang: 'en' }, f.en), h('span', { html: rich(f.es) }), ...(f.pron ? [h('small', { class: 'pr' }, f.pron)] : []))))), ...(p.nota ? [h('div', { class: 'hand nota', html: rich(p.nota) })] : []));
    case 'check': return h('li', { class: 'paso check' }, h('div', { class: 'hand ph' }, 'Verifica'), h('p', { html: rich(p.texto) }));
  }
}

function marcasEl(q: Question): HTMLElement | null {
  const ms = (q.hoja?.marcas ?? []).filter((m) => q.enunciado.includes(m.frag)).sort((a, b) => q.enunciado.indexOf(a.frag) - q.enunciado.indexOf(b.frag));
  if (!ms.length) return null;
  const modo = q.hoja!.modo;
  return h('li', { class: 'paso sin' }, h('div', { class: 'hand ph' }, modo === 'lectura' ? 'Lo importante del texto' : 'Lo importante del enunciado'), ...ms.map((m) => h('div', { class: `mk m-${m.rol}` }, h('span', { class: 'chip' }, ROL[m.rol]), h('q', { html: mx(m.frag) }), m.nota ? h('span', { class: 'hand' }, m.nota) : null)));
}

function descarteEl(q: Question): HTMLElement | null {
  const rows = q.opciones.map((o, i) => ({ o, i, d: q.distractores[i] })).filter((r) => r.i !== q.correcta && r.d);
  if (!rows.length) return null;
  return h('li', { class: 'paso sin' }, h('div', { class: 'hand ph' }, 'Por qué las otras tientan'), ...rows.map((r) => h('div', { class: 'ds' }, h('b', {}, L[r.i]), h('div', {}, h('strong', { html: mx(r.o) + '. ' }), h('em', { html: mx(r.d) })))));
}

export interface Entrada { el: HTMLElement; kind: 'marcas' | 'paso' | 'descarte' | 'check'; paso?: Paso; shown?: boolean }

/** Hoja de borrador: dibujo a mano libre, ficha viva, demostración, guía interactiva y resolución. */
export function enfoqueEl(q: Question): HTMLElement | null {
  const e = q.hoja?.enfoque; if (!e) return null;
  return h('div', { class: 'enfoque', hidden: true },
    h('div', { class: 'ef-h' }, h('span', { class: 'hand' }, '¿De qué tema es?')),
    h('div', { class: 'ef-tema', 'data-e': 'tema' }, h('b', {}, e.tema), h('span', { html: '. ' + rich(e.que) })),
    h('div', { class: 'ef-pistas', 'data-e': 'pistas' }, h('b', {}, '¿Cómo lo sé? Pistas del enunciado'), h('ul', {}, ...e.pistas.map((x) => h('li', { html: rich(x) })))),
    h('div', { class: 'ef-sub' }, '¿Por qué NO es de estos otros temas?'),
    ...e.no.map((x, i) => h('div', { class: 'ef-no', 'data-e': `no${i}` }, h('b', {}, 'No es ' + x.t.charAt(0).toLowerCase() + x.t.slice(1)), h('span', { html: '. ' + rich(x.p) }))),
    h('div', { class: 'ef-clave', 'data-e': 'clave' }, h('b', {}, 'Clave para reconocerlo la próxima vez'), h('span', { html: ': ' + rich(e.clave) })),
    h('div', { class: 'ef-plan', 'data-e': 'plan' }, h('b', {}, 'Cómo la resuelvo, paso a paso'), h('ol', {}, ...e.plan.map((x) => h('li', {}, h('div', { html: rich(x.t) }), ...(x.eq ?? []).map((q) => h('div', { class: 'ln eqln', html: eqn(q) })))))));
}

export function crearHoja(q: Question, guiada: boolean, st: HTMLElement): { el: HTMLElement; ficha: Ficha; todo(parcial?: boolean): void; detener(): void; ir(n: string): void } {
  const steps: Entrada[] = [];
  const hoja = q.hoja;
  if (guiada && hoja) {
    const m = marcasEl(q); if (m) steps.push({ el: m, kind: 'marcas' });
    for (const p of hoja.pasos) if (p.k !== 'check') steps.push({ el: pasoEl(p), kind: 'paso', paso: p });
    const d = descarteEl(q); if (d) steps.push({ el: d, kind: 'descarte' });
    const c = hoja.pasos.find((p) => p.k === 'check'); if (c) steps.push({ el: pasoEl(c), kind: 'check', paso: c });
  }
  let ctlIr: (n: string) => void = () => undefined;
  const ficha = crearFicha(q);
  const root = h('section', { class: 'hoja', 'aria-label': 'Hoja de borrador' });
  const list = h('ol', { class: 'pasos', 'aria-live': 'polite' });
  let head = false;
  const marks = () => root.closest('.qcard')?.classList.add('marks-on');
  const mostrar = (e: Entrada): HTMLElement => {
    if (!e.shown) { e.shown = true; if (!head) { head = true; list.append(h('li', { class: 'hand ph sol' }, 'Solución, paso a paso')); } e.el.classList.add('in'); list.append(e.el); }
    return e.el;
  };
  function todo(parcial?: boolean) { demo?.abortar(); if (ef) ef.hidden = false; marks(); if (parcial) return; ficha.llenarTodo(); for (const e of steps) mostrar(e); bRes.disabled = true; ctlIr('expl'); }
  root.addEventListener('click', (ev) => { const t = (ev.target as HTMLElement).closest('.enfoque>div[data-e], .paso'); if (t && root.closest('.qcard.play')) t.classList.toggle('open'); });
  const guia = guiada ? crearGuia(q, st, ficha, { onMarks: marks, onDone: () => todo() }) : null;
  const ef = guiada ? enfoqueEl(q) : null;
  const demo = guiada && hoja ? crearDemo(q, st, ficha, { entradas: steps, mostrar, todo, enfoque: ef ?? undefined, ir: (n) => ctlIr(n) }) : null;
  const bGuia = h('button', { class: 'btn primary', type: 'button', onclick: () => { guia?.start(); bGuia.hidden = true; } }, 'Empezar paso a paso') as HTMLButtonElement;
  const bRes = h('button', { class: 'btn sm', type: 'button', onclick: () => { todo(); } }, 'Ver la solución completa') as HTMLButtonElement;
  root.className = 'hoja mesa';
  root.setAttribute('aria-label', 'Mesa de estudio');
  if (!guiada) { root.append(crearPad()); return { el: root, ficha, todo, detener: () => undefined, ir: () => undefined }; }
  const panes: Record<string, HTMLElement> = {}, tabs: Record<string, HTMLButtonElement> = {};
  const ir = (n: string) => { root.dataset.pane = n; if (n === 'hoja') { for (const k of Object.keys(panes)) { panes[k].hidden = true; tabs[k].classList.remove('on'); tabs[k].setAttribute('aria-selected', 'false'); } return; } if (!panes[n]) return; for (const k of Object.keys(panes)) { const on = k === n; panes[k].hidden = !on; tabs[k].classList.toggle('on', on); tabs[k].setAttribute('aria-selected', String(on)); } };
  const tab = (id: string, label: string, sub: string, body: HTMLElement[]) => {
    tabs[id] = h('button', { class: 'mtab', type: 'button', role: 'tab', 'aria-selected': 'false', onclick: () => ir(id) }, h('b', {}, label), h('small', {}, sub)) as HTMLButtonElement;
    panes[id] = h('div', { class: 'mpane', role: 'tabpanel', hidden: true }, ...body);
  };
  if (ef) { ef.hidden = false; tab('tema', 'Empezar', 'De qué trata la pregunta', [h('p', { class: 'mhint' }, 'Úsala si no sabes por dónde empezar. Te cuento de qué tema es, en qué te fijas para reconocerlo y cómo se resuelve.'), ef]); }
  if (guia) tab('paso', 'Hazlo tú', 'Yo te guío, paso a paso', [h('p', { class: 'mhint' }, 'Úsala si quieres intentarlo. Vas paso a paso: primero marcas lo importante del enunciado y luego completas la solución. Si te equivocas, te explico por qué.'), bGuia, guia.el]);
  if (demo) tab('expl', 'Ver la solución', 'El profe la explica', [h('p', { class: 'mhint' }, 'Úsala si ya lo intentaste o si prefieres ver cómo se hace. El profe lo resuelve en voz alta. Si algo no te quedó claro, pasa a la siguiente explicación: cada una es más sencilla.'), demo.panel]);
  const borrador = h('section', { class: 'borr', 'aria-label': 'Tu borrador' }, h('h3', {}, 'Tu borrador'), h('p', { class: 'mhint' }, 'Aquí se va escribiendo la solución mientras avanzas, como en la hoja de un examen.'), ficha.el, list, bRes, h('details', { class: 'padd' }, h('summary', {}, 'Escribir a mano en la hoja'), crearPad()));
  const order = ['tema', 'paso', 'expl'].filter((k) => panes[k]);
  root.append(...(demo ? [h('div', { class: 'player' }, demo.subt, demo.bar)] : []), h('div', { class: 'mesa-h' }, h('h3', {}, '¿Cómo quieres que te ayude?'), h('p', { class: 'mhint' }, 'Elige una opción. Puedes cambiar cuando quieras: tu borrador de abajo se guarda. Truco: toca un dato (un número o una palabra subrayada) y verás en dorado dónde más aparece.')), h('div', { class: 'mtabs', role: 'tablist' }, ...order.map((k) => tabs[k])), ...order.map((k) => panes[k]), borrador, ...(demo ? [demo.pizarra] : []));
  ir(order[0]);
  ctlIr = ir;
  return { el: root, ficha, todo, detener: () => demo?.abortar(), ir: (n) => ctlIr(n) };
}
