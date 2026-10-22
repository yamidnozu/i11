import { h } from './dom';
import { renderQuestion } from './question';
import { radar } from './radar';
import { QUESTIONS } from '../content';
import { SIMULACROS, getSimulacro, armar, resumen, type Armado } from '../content/simulacros';
import type { SimulacroDef } from '../content/schema';
import { AREAS, AREA_IDS, type AreaId } from '../adaptive/areas';
import { eap, type Resp } from '../adaptive/irt';
import { areaScore, areaSE, globalScore, globalSE } from '../adaptive/score';
import { record, itemOf, syncSoon } from '../state/store';
import { examenVista } from './examen';
import { comoExamen } from '../content/simulacros';
import { gate, head, ruler, DISCLAIMER } from './pages';

const HKEY = 'saber11.simhist', SKEY = (id: string) => `saber11.sim.${id}`;
interface Hist { t: number; g: number | null; ok: number; n: number }
const lee = <T,>(k: string, d: T): T => { try { const s = localStorage.getItem(k); return s ? JSON.parse(s) as T : d; } catch { return d; } };
const escribe = (k: string, v: unknown) => { try { v === null ? localStorage.removeItem(k) : localStorage.setItem(k, JSON.stringify(v)); } catch { /* ignorar */ } };
const hist = (): Record<string, Hist[]> => lee(HKEY, {});
const mmss = (ms: number) => `${Math.floor(ms / 60000)}:${String(Math.floor(ms / 1000) % 60).padStart(2, '0')}`;

/** Lista de simulacros disponibles (el contenido sale de JSON: content/simulacros/ o content/packs/). */
export function simulacroTarjetas(): HTMLElement {
  const H = hist();
  return h('div', { class: 'simlist' }, ...SIMULACROS.map((s) => {
    const r = resumen(s), hs = H[s.id] ?? [], mejor = hs.reduce<number | null>((m, x) => (x.g !== null && (m === null || x.g > m) ? x.g : m), null);
    const enCurso = !!lee(SKEY(s.id), null), ex = s.modo === 'examen';
    return h('a', { class: 'simcard', href: `#/simulacro/${s.id}` },
      h('b', {}, s.nombre), s.descripcion ? h('span', { class: 'sd' }, s.descripcion) : null,
      h('span', { class: 'sm' }, ex ? `${r.preguntas} preguntas · ${s.sesiones?.length ?? 0} ${(s.sesiones?.length ?? 0) === 1 ? 'sesión' : 'sesiones'} · ${r.minutos} min` : `${r.preguntas} preguntas · ${s.secciones.length} ${s.secciones.length === 1 ? 'prueba' : 'pruebas'} · ${r.minutos} min`),
      h('span', { class: 'sb' }, enCurso ? 'En curso: continúa donde ibas' : mejor !== null ? `Tu mejor puntaje: ${mejor} de 500 (${hs.length} ${hs.length === 1 ? 'intento' : 'intentos'})` : 'Aún no lo has hecho'));
  }));
}
/** Lista de simulacros disponibles (el contenido sale de JSON: content/simulacros/ o content/packs/). */
export function simulacroLista(): HTMLElement {
  return h('div', {}, head('Simulacros', 'Cada simulacro es un cuadernillo: ves todas las preguntas de cada prueba, cambias respuestas, marcas dudas y al final revisas todo con explicación.'), simulacroTarjetas());
}

interface St { id: string; sec: Armado[]; s: number; i: number; ans: Record<string, boolean>; end: number; ini: number }

export function simulacroPagina(id: string): HTMLElement {
  const def = getSimulacro(id);
  if (!def) return h('div', {}, head('Simulacro no encontrado'), h('a', { class: 'btn', href: '#/simulacro' }, 'Ver los simulacros'));
  return gate(() => examenVista(comoExamen(def)));
}

function vista(def: SimulacroDef): HTMLElement {
  const root = h('div');
  let st: St | null = lee<St | null>(SKEY(def.id), null);
  const persist = () => escribe(SKEY(def.id), st);
  let tm: ReturnType<typeof setInterval> | undefined;

  const intro = () => {
    const r = resumen(def);
    root.replaceChildren(h('div', { class: 'pagehead' }, h('a', { class: 'crumb', href: '#/simulacro' }, '← Todos los simulacros'), h('h1', {}, def.nombre), def.descripcion ? h('p', { class: 'lede' }, def.descripcion) : null),
      h('table', { class: 'simtab' }, h('thead', {}, h('tr', {}, h('th', {}, 'Sección'), h('th', {}, 'Preguntas'), h('th', {}, 'Tiempo'))),
        h('tbody', {}, ...def.secciones.map((c) => h('tr', {}, h('td', {}, c.titulo), h('td', {}, String(c.preguntas?.length ?? Math.min(c.auto?.n ?? 0, QUESTIONS.filter((q) => q.tipo !== 'reto' && (!c.auto?.area || q.area === c.auto.area)).length))), h('td', {}, `${c.minutos} min`))))),
      h('p', { class: 'fine' }, `En total: ${r.preguntas} preguntas y ${r.minutos} minutos. Cada sección tiene su reloj y empieza cuando tú lo decides. Si se acaba el tiempo, pasas a la siguiente y lo que quedó sin responder cuenta como incorrecto. Si cierras la página, tu avance se guarda.`),
      h('div', { class: 'row' }, h('button', { class: 'btn primary', type: 'button', onclick: empezar }, st ? 'Empezar de nuevo' : 'Empezar'), ...(st ? [h('button', { class: 'btn', type: 'button', onclick: run }, 'Continuar donde iba')] : [])));
  };

  function empezar() { st = { id: def.id, sec: armar(def), s: 0, i: 0, ans: {}, end: 0, ini: Date.now() }; persist(); run(); }

  function pausa(titulo: string, extra: string) {
    clearInterval(tm);
    const S = st!.sec[st!.s];
    root.replaceChildren(head(titulo, extra), h('div', { class: 'box' }, h('b', {}, S.titulo), h('p', {}, `${S.ids.length} preguntas · ${S.minutos} minutos`)),
      h('div', { class: 'row' }, h('button', { class: 'btn primary', type: 'button', onclick: () => { st!.end = Date.now() + S.minutos * 60000; persist(); run(); } }, `Empezar ${S.titulo}`)));
  }
  function siguienteSeccion(porTiempo: boolean) {
    clearInterval(tm);
    const dejadas = st!.sec[st!.s].ids.filter((q) => !(q in st!.ans));
    dejadas.forEach((q) => { st!.ans[q] = false; });
    st!.s++; st!.i = 0; st!.end = 0; persist();
    if (st!.s >= st!.sec.length) return fin();
    run(porTiempo ? 'Se acabó el tiempo de la sección' : 'Sección terminada');
  }
  function run(aviso?: string) {
    clearInterval(tm);
    if (!st) return;
    if (st.s >= st.sec.length) return fin();
    const S = st.sec[st.s];
    if (!st.end) return pausa(aviso ?? (st.s === 0 ? 'Listo para empezar' : 'Sigue la siguiente sección'), st.s === 0 ? 'Cuando empieces, corre el tiempo de esta sección.' : 'Respira un momento. El tiempo de la siguiente sección corre cuando le des empezar.');
    if (st.i >= S.ids.length) return siguienteSeccion(false);
    const clock = h('span', { class: 'clock', 'aria-live': 'off' });
    const tick = () => { const left = Math.max(0, st!.end - Date.now()); clock.textContent = mmss(left); clock.classList.toggle('low', left < 60000); if (!left) { clearInterval(tm); siguienteSeccion(true); } };
    tm = setInterval(tick, 1000); tick();
    const q = QUESTIONS.find((x) => x.id === S.ids[st!.i])!;
    const sh = h('p', { class: 'sighint', role: 'status' }, 'Elige una respuesta para continuar');
    const ultimaDeSeccion = st.i + 1 >= S.ids.length, ultima = ultimaDeSeccion && st.s + 1 >= st.sec.length;
    root.replaceChildren(h('div', { class: 'row between' }, h('h1', {}, def.nombre), clock),
      h('p', { class: 'fine' }, `Sección ${st.s + 1} de ${st.sec.length}: ${S.titulo}`),
      h('div', { class: 'progline' }, ruler(S.ids.length, st.i), h('span', {}, `${st.i + 1} / ${S.ids.length}`)),
      sh, renderQuestion(q, (ok) => {
        sh.remove(); st!.ans[q.id] = ok; record(q, ok, 'sim'); st!.i++; persist();
        root.append(h('button', { class: 'btn primary next', type: 'button', onclick: () => run() }, ultima ? 'Terminar simulacro' : ultimaDeSeccion ? 'Terminar sección' : 'Siguiente'));
      }, { feedback: false }));
  }

  function fin() {
    clearInterval(tm);
    const todas = st!.sec.flatMap((c) => c.ids);
    const per: Partial<Record<AreaId, Resp[]>> = {};
    for (const qid of todas) { const q = QUESTIONS.find((x) => x.id === qid); if (q) (per[q.area] ??= []).push({ item: itemOf(q), correct: !!st!.ans[qid] }); }
    const sc: Partial<Record<AreaId, number>> = {}, se: Partial<Record<AreaId, number>> = {};
    for (const a of AREA_IDS) if (per[a]) { const e = eap(per[a]!); sc[a] = areaScore(a, e.theta); se[a] = areaSE(a, e.se); }
    const g = globalScore(sc), ok = todas.filter((q) => st!.ans[q]).length;
    const H = hist(), prev = H[def.id] ?? [];
    const antes = prev.length ? prev[prev.length - 1].g : null;
    H[def.id] = [...prev, { t: Date.now(), g, ok, n: todas.length }].slice(-12); escribe(HKEY, H);
    const secciones = st!.sec.map((c) => ({ c, ok: c.ids.filter((q) => st!.ans[q]).length }));
    root.replaceChildren(head(`Resultado: ${def.nombre}`),
      h('div', { class: 'panelgrid' }, h('figure', { class: 'radar' }, h('div', { html: radar(sc) }), h('figcaption', {}, 'Resultado de este simulacro frente a la media nacional.')),
        h('div', {}, ...AREA_IDS.filter((a) => per[a]).map((a) => h('div', { class: 'arow' }, h('b', {}, AREAS[a].nombre), h('div', { class: 'bar' }, h('i', { style: `width:${sc[a] ?? 0}%` }), h('u', { style: `left:${AREAS[a].mu}%` })), h('span', {}, `${sc[a] ?? 0}`))))),
      ...(g === null ? [] : [h('div', { class: 'bigscore' }, h('b', {}, String(g)), h('span', {}, `de 500 · estimado ± ${Math.round(globalSE(se))}${antes !== null ? ` · intento anterior: ${antes}` : ''}`))]),
      h('table', { class: 'simtab' }, h('thead', {}, h('tr', {}, h('th', {}, 'Sección'), h('th', {}, 'Aciertos'))), h('tbody', {}, ...secciones.map((x) => h('tr', {}, h('td', {}, x.c.titulo), h('td', {}, `${x.ok} de ${x.c.ids.length}`))))),
      h('div', { class: 'row' }, h('a', { class: 'btn primary', href: '#/simulacro' }, 'Ver los simulacros'), h('a', { class: 'btn', href: '#/panel' }, 'Ver mi progreso')),
      h('p', { class: 'fine' }, DISCLAIMER + ' Con pocas preguntas por área el margen es amplio.'));
    st = null; persist(); syncSoon();
  }

  intro();
  return root;
}
