import { h } from './dom';
import { atomize } from './automath';
import { rich } from './tex';
import { vel, reducido, type Ficha } from './ficha';
import { hablar } from './hablar';
import { cfg, guardar, decir, cortar, pausarVoz, seguirVoz, voces, hayVoz, hayVozEn, guiaVozEn, alCargar } from './voz';
import type { Question, Marca, Beat, NotaK, Paso, Enfoque } from '../content/schema';
import type { Entrada } from './hoja';

const esc = (s: string) => s.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
class Skip extends Error {}
const vis = (t: string) => t.replace(/\{\{!?(.+?)\}\}/g, '$1');
const PTR = '<svg viewBox="0 0 24 24" width="24" height="24"><path d="M3 2l15 9-6.5 1.6L9 19z" fill="#ffd24a" stroke="#07224f" stroke-width="1.5" stroke-linejoin="round"/></svg>';
const NOTA: Record<NotaK, string> = { ej: 'Ejemplo', contra: 'Caso contrario', ana: 'Piensa así', err: 'Error común', por: '¿Por qué?' };
const NIVELES = [{ n: '1', label: 'Resumido' }, { n: '2', label: 'Con explicación' }, { n: '3', label: 'Con ejemplos' }] as const;

/** Si una pregunta no tiene guion escrito, se arma uno corto con lo que ya existe. */
export function beatsAuto(q: Question): Beat[] {
  const hj = q.hoja!, out: Beat[] = [{ t: 'Vamos a leer el enunciado con calma.', a: 'leer' }];
  for (const m of hj.marcas ?? []) out.push({ t: `${m.nota ? m.nota[0].toUpperCase() + m.nota.slice(1) + '.' : 'Fíjate en esto.'} ${m.campo ?? ''}`.trim(), a: `m:${m.frag}` });
  hj.pasos.forEach((p, i) => { out.push({ t: p.k === 'idea' ? p.texto : p.k === 'check' ? p.texto : p.k === 'calc' ? (p.titulo ?? 'Hagamos la cuenta') + '.' : (p.titulo ?? 'Sigamos') + '.', a: `p:${i}` }); });
  return out;
}

const lc = (x: string) => x.charAt(0).toLowerCase() + x.slice(1);
/** Primero se ubica el tema: de qué es la pregunta, con qué podría confundirse y cómo se aborda. */
export function enfoqueBeats(e: Enfoque, n: string): Beat[] {
  const no = n === '1' ? e.no.slice(0, 1) : e.no;
  const pistas = n === '1' ? e.pistas.slice(0, 2) : e.pistas;
  return [
    { t: 'Antes de resolver nada, lo primero es saber de qué tema es la pregunta. Así sabemos por dónde empezar.', a: 'e:show' },
    { t: `Esta pregunta es de ${lc(e.tema)}. ${e.que}`, a: 'e:tema' },
    { t: `¿Cómo lo sé? Por estas pistas del enunciado: ${pistas.join('; ')}.`, a: 'e:pistas' },
    ...no.map((x, i) => ({ t: `Ojo, no es ${lc(x.t)}. ${x.p}`, a: `e:no${i}` })),
    ...(n === '1' ? [] : [{ t: `Una clave para reconocerlo rápido la próxima vez: ${e.clave}`, a: 'e:clave' }]),
    { t: 'Ahora sí, vamos paso a paso.', a: 'e:plan' },
    ...e.plan.map((x, i) => ({ t: `${['Primero', 'Segundo', 'Tercero', 'Cuarto', 'Quinto'][i] ?? 'Luego'}: ${x.t}`, a: `e:plan` })),
  ];
}

/** El profe: lee el enunciado con un cursor, habla, marca, llena la ficha, escribe en la hoja y comenta las opciones. */
export function crearDemo(q: Question, st: HTMLElement, ficha: Ficha, hoja: { entradas: Entrada[]; mostrar(e: Entrada): HTMLElement; todo(parcial?: boolean): void; enfoque?: HTMLElement; ir?(n: string): void }) {
  const guion = q.hoja?.guion;
  const niveles = NIVELES.filter((x) => (guion ? guion[x.n]?.length : x.n === '1'));
  const beatsDe = (n: string): Beat[] => {
    const base = guion ? guion[n as '1'] : beatsAuto(q), e = q.hoja?.enfoque;
    if (!e) return base;
    const rest = base[0]?.a === 'leer' ? base.slice(1) : base;
    return [{ t: 'Vamos a leer todo el enunciado, con calma.', a: 'leer' }, ...enfoqueBeats(e, n), ...rest];
  };
  let abort = false, paused = false, running = false, gen = 0, runId = 0, goto: number | null = null, nivel = '1', idx = 0;

  const cur = h('div', { class: 'dcur', 'aria-hidden': 'true' }, h('div', { class: 'ptr', html: PTR }));
  const subt = h('div', { class: 'subt', hidden: true, 'aria-live': 'polite' });
  const pizarra = h('div', { class: 'pizarra' });
  const trans = h('details', { class: 'trans', hidden: true }, h('summary', {}, 'Leer la explicación'));
  const card = () => st.closest('.qcard') as HTMLElement;

  // controles: pausa, volver 10 s, siguiente frase
  let t0 = 0, pausaIni = 0, pausado = 0;
  const ahora = () => performance.now() - t0 - pausado - (paused ? performance.now() - pausaIni : 0);
  const inicios: number[] = [];
  const pausa = (v?: boolean) => {
    const quiere = v ?? !paused; if (quiere === paused) return;
    if (quiere) pausaIni = performance.now(); else pausado += performance.now() - pausaIni;
    paused = quiere; bPause.textContent = paused ? '▶ Seguir' : '⏸ Pausa'; bPause.classList.toggle('primary', paused); paused ? pausarVoz() : seguirVoz();
  };
  /** Vuelve a la frase que empezó hace al menos 10 segundos de explicación (no cuenta el tiempo en pausa). */
  const atras10 = () => { const meta = ahora() - 10000; let j = 0; for (let k = idx; k >= 0; k--) if (inicios[k] !== undefined && inicios[k] <= meta) { j = k; break; } pausa(false); ir(j); };
  const bBack = h('button', { class: 'btn sm', type: 'button', 'aria-label': 'Volver 10 segundos', onclick: atras10 }, '⟲ 10 s');
  const bPause: HTMLButtonElement = h('button', { class: 'btn sm', type: 'button', onclick: () => pausa() }, '⏸ Pausa') as HTMLButtonElement;
  const bNext = h('button', { class: 'btn sm', type: 'button', 'aria-label': 'Frase siguiente', onclick: () => { pausa(false); ir(idx + 1); } }, '⏭ Siguiente');
  const bStop = h('button', { class: 'btn sm', type: 'button', onclick: () => hoja.todo() }, 'Ver solución');
  const bar = h('div', { class: 'dbar', hidden: true }, bBack, bPause, bNext, bStop);
  const onKey = (e: KeyboardEvent) => {
    if (!running) return;
    if (!st.isConnected) { document.removeEventListener('keydown', onKey); return; }
    const t = e.target as HTMLElement | null; if (t?.closest('input,select,textarea,button,summary,a,[contenteditable]')) return;
    if (e.key === ' ') { e.preventDefault(); pausa(); } else if (e.key === 'ArrowLeft') { e.preventDefault(); atras10(); } else if (e.key === 'ArrowRight') { e.preventDefault(); pausa(false); ir(idx + 1); }
  };
  document.addEventListener('keydown', onKey);
  const rate = h('select', { 'aria-label': 'Velocidad de la voz', onchange: (e: Event) => { cfg.rate = Number((e.target as HTMLSelectElement).value); guardar(); } }, ...[[0.75, 'Lenta'], [0.95, 'Normal'], [1.15, 'Rápida'], [1.4, 'Muy rápida']].map(([v, l]) => h('option', { value: String(v), selected: Math.abs(cfg.rate - (v as number)) < 0.05 }, l as string)));
  const bVoz = h('button', { class: 'btn sm', type: 'button', 'aria-pressed': String(cfg.on), onclick: () => { cfg.on = !cfg.on; guardar(); bVoz.textContent = cfg.on ? '🔊 Voz' : '🔇 Sin voz'; bVoz.setAttribute('aria-pressed', String(cfg.on)); if (!cfg.on) cortar(); } }, cfg.on ? '🔊 Voz' : '🔇 Sin voz');
  const selVoz = h('select', { 'aria-label': 'Elegir voz', hidden: true, onchange: (e: Event) => { cfg.name = (e.target as HTMLSelectElement).value; guardar(); } });
  const llenaVoces = () => { const vs = voces(); selVoz.replaceChildren(...vs.map((v) => h('option', { value: v.name, selected: v.name === cfg.name }, `${v.name.replace(/Microsoft |Google /g, '')} (${v.lang})`))); selVoz.hidden = vs.length < 2; sinVoz.hidden = hayVoz(); };
  const selEn = h('select', { 'aria-label': 'Voz en inglés', hidden: true, onchange: (e: Event) => { cfg.en = (e.target as HTMLSelectElement).value; guardar(); } });
  const rateEn = h('select', { 'aria-label': 'Velocidad del inglés', onchange: (e: Event) => { cfg.enRate = Number((e.target as HTMLSelectElement).value); guardar(); } }, ...[[0.65, 'Inglés muy lento'], [0.85, 'Inglés lento'], [1, 'Inglés normal']].map(([v, l]) => h('option', { value: String(v), selected: Math.abs(cfg.enRate - (v as number)) < 0.06 }, String(l))));
  const probarEn = h('button', { class: 'btn sm', type: 'button', 'data-en': 'Hello! This is how English sounds. She goes to school every day.' }, 'Probar inglés');
  const sinEn = h('span', { class: 'fine' }, guiaVozEn());
  const llenaEn = () => { const vs = voces('en'); selEn.replaceChildren(h('option', { value: '' }, 'Voz en inglés: automática'), ...vs.map((v) => h('option', { value: v.name, selected: v.name === cfg.en }, `${v.name.replace(/Microsoft |Google /g, '')} (${v.lang})`))); selEn.hidden = vs.length < 2; sinEn.hidden = hayVozEn(); };
  alCargar(llenaEn); setTimeout(llenaEn, 300);
  const sinVoz = h('span', { class: 'fine' }, 'Tu dispositivo no tiene voz en español: lee los subtítulos.');
  alCargar(llenaVoces); setTimeout(llenaVoces, 300);
  const SUBN: Record<string, string> = { '1': 'Solo lo esencial', '2': 'Explico cada paso y por qué las otras no', '3': 'Con ejemplos de la vida diaria' };
  const btns = niveles.map((x) => h('button', { class: 'lv', type: 'button', 'data-n': x.n, 'aria-pressed': 'false', onclick: () => start(x.n) }, h('b', {}, `${x.n} · ${x.label}`), h('small', {}, SUBN[x.n])));
  const panel = h('div', { class: 'profe' }, h('div', { class: 'lvs' }, ...btns), h('details', { class: 'aj' }, h('summary', {}, 'Voz y velocidad'), h('div', { class: 'row pv' }, bVoz, rate, selVoz, sinVoz), h('div', { class: 'row pv en' }, selEn, rateEn, probarEn, sinEn)), trans);

  // utilidades
  const wait = async (ms: number, g = gen) => { await new Promise((r) => setTimeout(r, reducido() ? 0 : ms / vel.x)); while (paused && !abort && g === gen) await new Promise((r) => setTimeout(r, 80)); if (abort) throw new Skip(); if (g !== gen) throw new Skip(); };
  function moveTo(el: HTMLElement, f = 0.5) { el.scrollIntoView?.({ block: 'nearest', inline: 'nearest', behavior: 'auto' }); const c = card().getBoundingClientRect(), r = el.getBoundingClientRect(); cur.style.transform = `translate(${r.left - c.left + r.width * f}px,${r.bottom - c.top - 2}px)`; }
  const atoms = atomize(q.enunciado);
  const ms = (q.hoja?.marcas ?? []).filter((m) => q.enunciado.includes(m.frag)).map((m) => { const i = q.enunciado.indexOf(m.frag), j = i + m.frag.length; return { m, idx: atoms.map((_, k) => k).filter((k) => !atoms[k].space && atoms[k].start < j && atoms[k].end > i) }; }).filter((x) => x.idx.length);
  const els = () => [...st.querySelectorAll<HTMLElement>('.a')];
  const nums = (s: string) => s.match(/\d+(?:[.,]\d+)?/g) ?? [];
  const usados = (line: string): Marca[] => { const L = line.replace(/\{,\}/g, ',').replace(/\\[a-zA-Z]+/g, ' '); return ms.filter((x) => x.m.rol === 'dato' && nums(x.m.frag).some((n) => new RegExp(`(?<![\\d.,])${n.replace('.', '\\.')}(?!\\d)`).test(L))).map((x) => x.m); };

  // acciones
  async function leer(g: number) { card().append(cur); cur.classList.add('on'); st.scrollIntoView({ block: 'center', behavior: reducido() ? 'auto' : 'smooth' }); await wait(500, g); const E = els(); for (let k = 0; k < atoms.length; k++) { if (atoms[k].space) continue; moveTo(E[k]); E[k].classList.add('rd'); await wait(70, g); E[k].classList.remove('rd'); } }
  async function marcar(frag: string, g: number) {
    const x = ms.find((y) => y.m.frag === frag); if (!x) return;
    card().append(cur); cur.classList.add('on'); st.scrollIntoView({ block: 'nearest', behavior: reducido() ? 'auto' : 'smooth' });
    const E = els(), a = x.idx[0], b = x.idx[x.idx.length - 1];
    if (ficha.tiene(x.m)) { ficha.flash([x.m]); for (let k = a; k <= b; k++) E[k].classList.add('rd'); await wait(900, g); for (let k = a; k <= b; k++) E[k].classList.remove('rd'); return; }
    moveTo(E[a], 0); await wait(350, g);
    for (let k = a; k <= b; k++) { E[k].classList.add(`u-${x.m.rol}`); if (!atoms[k].space) { moveTo(E[k], 1); await wait(110, g); } }
    await wait(300, g);
    await ficha.llenar(x.m, E.slice(a, b + 1).filter((_, k) => !atoms[a + k].space));
  }
  async function escribir(e: Entrada, g: number) {
    const era = e.shown; const sh = hoja.mostrar(e); sh.parentElement?.querySelectorAll('.act').forEach((x) => x.classList.remove('act')); sh.classList.add('act'); if (era) { sh.classList.add('done'); sh.scrollIntoView({ block: 'nearest', behavior: reducido() ? 'auto' : 'smooth' }); return; }
    const lns = [...sh.querySelectorAll<HTMLElement>('.ln')]; lns.forEach((l) => (l.style.clipPath = 'inset(0 100% 0 0)'));
    try {
      sh.scrollIntoView({ block: 'nearest', behavior: reducido() ? 'auto' : 'smooth' }); await wait(500, g);
      card().append(cur); cur.classList.add('on'); moveTo((sh.querySelector('.ph') as HTMLElement) ?? sh, 0.05); await wait(350, g);
      for (const ln of lns) {
        const u = e.paso?.k === 'calc' ? usados((e.paso as Extract<Paso, { k: 'calc' }>).lineas[lns.indexOf(ln)] ?? '') : []; if (u.length) { ficha.flash(u); await wait(600, g); }
        if (reducido() || !ln.animate) { ln.style.clipPath = ''; continue; }
        const tx = (ln.firstElementChild as HTMLElement) ?? ln; moveTo(tx, 0); await wait(80, g);
        const d = 1000 / vel.x; cur.style.transitionDuration = d / 1000 + 's'; moveTo(tx, 1);
        await ln.animate([{ clipPath: 'inset(0 100% 0 0)' }, { clipPath: 'inset(0 0 0 0)' }], { duration: d, easing: 'linear' }).finished; ln.style.clipPath = ''; cur.style.transitionDuration = '';
        await wait(300, g);
      }
    } finally { lns.forEach((l) => (l.style.clipPath = '')); cur.style.transitionDuration = ''; sh.classList.add('done'); }
  }
  const ops = () => [...card().querySelectorAll<HTMLElement>('.opt')];
  function opcion(L: string, v: string) { const o = ops()['ABCD'.indexOf(L)]; if (!o) return; o.classList.remove('hl-ok', 'hl-no'); o.classList.add(v === 'ok' ? 'hl-ok' : 'hl-no'); o.scrollIntoView({ block: 'nearest', behavior: reducido() ? 'auto' : 'smooth' }); }
  const limpiaOps = () => ops().forEach((o) => o.classList.remove('hl-ok', 'hl-no'));
  function nota(k: NotaK, t: string) { pizarra.append(h('div', { class: `pnota n-${k}` }, h('b', {}, NOTA[k]), h('span', { html: rich(vis(t)) }))); }

  const fase = (f: string) => { card().dataset.fase = f; };
  async function accion(b: Beat, g: number) {
    if (b.k) nota(b.k, b.t);
    for (const a of (b.a ?? '').split('|').filter(Boolean)) {
      const [c, ...r] = a.split(':'), arg = r.join(':');
      if (c === 'leer') { fase('leer'); hoja.ir?.('hoja'); await leer(g); }
      else if (c === 'e') { fase('tema'); hoja.ir?.('tema'); const ef = hoja.enfoque; if (ef) { ef.hidden = false; ef.querySelectorAll('.hi').forEach((x) => x.classList.remove('hi')); const t = arg === 'show' ? null : ef.querySelector(`[data-e="${arg}"]`); t?.classList.add('hi'); ef.classList.toggle('foco', !!t); ((t as HTMLElement | null) ?? ef).scrollIntoView({ block: 'nearest', behavior: reducido() ? 'auto' : 'smooth' }); await wait(400, g); } }
      else if (c === 'm') { fase('dato'); await marcar(arg, g); }
      else if (c === 'f') { const x = ms.find((y) => y.m.frag === arg); if (x) ficha.flash([x.m]); }
      else if (c === 'p') { fase('paso'); hoja.ir?.('hoja'); const p = q.hoja!.pasos[Number(arg)]; const e = hoja.entradas.find((y) => y.paso === p); if (e) await escribir(e, g); }
      else if (c === 'd') { fase('paso'); hoja.ir?.('hoja'); const e = hoja.entradas.find((y) => y.kind === 'descarte'); if (e) await escribir(e, g); }
      else if (c === 'o') { fase('opc'); const [L, v] = arg.split(':'); opcion(L, v); }
      else if (c === 'clr') limpiaOps();
    }
  }
  function pinta(i: number, total: number, b: Beat) { subt.hidden = false; subt.replaceChildren(h('span', { class: 'sn' }, `${i + 1}/${total}`), h('span', { html: rich(vis(b.t)) })); }
  function ir(i: number) { const n = beatsDe(nivel).length; goto = Math.max(0, Math.min(n, i)); gen++; cortar(); }
  async function run(id: number) {
    const beats = beatsDe(nivel);
    trans.hidden = false; trans.replaceChildren(h('summary', {}, 'Leer la explicación'), h('ol', {}, ...beats.map((b) => h('li', { html: rich(vis(b.t)) }))));
    idx = 0;
    while (idx < beats.length) {
      if (id !== runId) return;
      if (!st.isConnected) { cortar(); limpiar(); return; }
      const i = idx, b = beats[i], g = ++gen; inicios[i] = ahora(); pinta(i, beats.length, b);
      try { await Promise.all([decir(b.v ?? hablar(b.t)), accion(b, g).catch((e) => { if (!(e instanceof Skip)) throw e; })]); } catch (e) { if (!(e instanceof Skip)) throw e; }
      if (abort || id !== runId) return;
      if (!st.isConnected) { cortar(); limpiar(); return; }
      while (paused && !abort) await new Promise((r) => setTimeout(r, 80));
      if (goto !== null) { idx = goto; goto = null; continue; }
      if (g !== gen) { idx = i + 1; continue; }
      await new Promise((r) => setTimeout(r, reducido() ? 0 : 450 / cfg.rate)); idx = i + 1;
    }
    if (id === runId) fin();
  }
  function fin() {
    document.dispatchEvent(new CustomEvent('hoja:fin')); cur.remove(); bar.hidden = true; running = false; card()?.classList.remove('play'); delete card()?.dataset.fase; hoja.ir?.('expl'); btns.forEach((x) => ((x as HTMLButtonElement).disabled = false));
    const sig = niveles.find((x) => Number(x.n) > Number(nivel));
    subt.replaceChildren(h('span', {}, '¿Te quedó claro? '), ...(sig ? [h('button', { class: 'btn sm primary', type: 'button', onclick: () => start(sig.n) }, `No del todo: ${sig.n} · ${sig.label}`)] : []), h('button', { class: 'btn sm', type: 'button', onclick: () => { subt.hidden = true; } }, 'Sí, todo claro'));
  }
  function limpiar() { cortar(); cur.remove(); bar.hidden = true; card()?.classList.remove('play'); delete card()?.dataset.fase; st.querySelectorAll('.rd').forEach((e) => e.classList.remove('rd')); limpiaOps(); running = false; btns.forEach((x) => ((x as HTMLButtonElement).disabled = false)); }
  function start(n: string) {
    if (running) { abort = true; gen++; cortar(); }
    nivel = n; paused = false; t0 = performance.now(); pausado = 0; inicios.length = 0; bPause.textContent = '⏸ Pausa'; bPause.classList.remove('primary'); pizarra.replaceChildren(); limpiaOps(); card()?.classList.add('play');
    const id = ++runId;
    setTimeout(() => { if (id !== runId) return; abort = false; running = true; goto = null; bar.hidden = false; ficha.mostrar(); btns.forEach((x) => { const on = (x as HTMLElement).dataset.n === n; x.classList.toggle('on', on); x.setAttribute('aria-pressed', String(on)); }); run(id).catch((e) => { console.error(e); }); }, running ? 80 : 0);
  }
  return { panel, subt, bar, pizarra, start, abortar() { abort = true; runId++; gen++; limpiar(); subt.hidden = true; } };
}
