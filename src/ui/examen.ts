import { h } from './dom';
import { renderQuestion } from './question';
import { radar } from './radar';
import { QUESTIONS, bloqueDe } from '../content';
import { bloqueEl } from './figura';
import { armarExamen, resumen, type SesionArm } from '../content/simulacros';
import type { SimulacroDef, Question } from '../content/schema';
import { AREAS, AREA_IDS, type AreaId } from '../adaptive/areas';
import { eap, type Resp } from '../adaptive/irt';
import { areaScore, areaSE, globalScore, globalSE } from '../adaptive/score';
import { record, itemOf, syncSoon } from '../state/store';
import { head, DISCLAIMER } from './pages';
import { crearPad } from './pad';
import { nivelesPanel } from './niveles';

const HKEY = 'saber11.simhist', SKEY = (id: string) => `saber11.sim.${id}`;
const lee = <T,>(k: string, d: T): T => { try { const s = localStorage.getItem(k); return s ? JSON.parse(s) as T : d; } catch { return d; } };
const escribe = (k: string, v: unknown) => { try { v === null ? localStorage.removeItem(k) : localStorage.setItem(k, JSON.stringify(v)); } catch { /* ignorar */ } };
const mmss = (ms: number) => { const t = Math.floor(ms / 1000), hh = Math.floor(t / 3600); return `${hh ? hh + ':' : ''}${String(Math.floor(t / 60) % 60).padStart(hh ? 2 : 1, '0')}:${String(t % 60).padStart(2, '0')}`; };
const LET = 'ABCDEFGH';
const qOf = (id: string) => QUESTIONS.find((q) => q.id === id)!;

interface Ex { id: string; ses: SesionArm[]; s: number; fase: 'pausa' | 'examen' | 'fin'; end: number; resp: Record<string, number>; marca: Record<string, 1>; cur: number; ent: number[] }

export function examenVista(def: SimulacroDef): HTMLElement {
  const root = h('div');
  let st: Ex | null = lee<Ex | null>(SKEY(def.id), null);
  if (st && !Array.isArray(st.ses)) st = null; // avance guardado con el formato anterior
  let tm: ReturnType<typeof setInterval> | undefined;
  const persist = () => escribe(SKEY(def.id), st);
  const plano = (S: SesionArm) => S.pruebas.flatMap((p, pi) => p.ids.map((id, k) => ({ id, pi, n: k + 1 })));

  const intro = () => {
    const r = resumen(def);
    root.replaceChildren(h('div', { class: 'pagehead' }, h('a', { class: 'crumb', href: '#/simulacro' }, '← Todos los simulacros'), h('h1', {}, def.nombre), def.descripcion ? h('p', { class: 'lede' }, def.descripcion) : null),
      ...armarExamen({ ...def, barajar: false }).map((x) => h('table', { class: 'simtab' }, h('caption', {}, `${x.titulo} · ${x.minutos} min en un solo reloj`), h('thead', {}, h('tr', {}, h('th', {}, 'Prueba'), h('th', {}, 'Preguntas'))),
        h('tbody', {}, ...x.pruebas.map((c) => h('tr', {}, h('td', {}, c.titulo), h('td', {}, String(c.ids.length))))))),
      h('p', { class: 'fine' }, `Total: ${r.preguntas} preguntas. Funciona como el cuadernillo real: dentro de cada sesión te mueves libremente entre preguntas, puedes cambiar respuestas y marcar las dudosas. Hay hoja de respuestas y hoja de operaciones. No hay ayudas ni correcciones hasta que entregues; al final tienes la revisión completa con explicación de cada pregunta. Tu avance se guarda.`),
      h('div', { class: 'row' }, h('button', { class: 'btn primary', type: 'button', onclick: empezar }, st ? 'Empezar de nuevo' : 'Empezar'), ...(st ? [h('button', { class: 'btn', type: 'button', onclick: run }, 'Continuar donde iba')] : [])));
  };
  function empezar() { st = { id: def.id, ses: armarExamen(def), s: 0, fase: 'pausa', end: 0, resp: {}, marca: {}, cur: 0, ent: [] }; persist(); run(); }

  function pausa() {
    const S = st!.ses[st!.s], n = plano(S).length;
    root.replaceChildren(head(st!.s === 0 ? 'Listo para empezar' : 'Descanso entre sesiones', st!.s === 0 ? 'Cuando empieces corre el tiempo de la sesión.' : 'Respira, toma agua. El reloj de la siguiente sesión corre cuando le des empezar.'),
      h('div', { class: 'box' }, h('b', {}, S.titulo), h('p', {}, `${n} preguntas · ${S.minutos} minutos`), h('ul', {}, ...S.pruebas.map((p) => h('li', {}, `${p.titulo}: ${p.ids.length}`)))),
      h('div', { class: 'row' }, h('button', { class: 'btn primary', type: 'button', onclick: () => { st!.fase = 'examen'; st!.end = Date.now() + S.minutos * 60000; st!.cur = 0; persist(); run(); } }, `Empezar ${S.titulo}`)));
  }

  function entregar(porTiempo: boolean) {
    clearInterval(tm);
    st!.ent.push(st!.s); st!.s++; st!.cur = 0; st!.end = 0; st!.fase = st!.s >= st!.ses.length ? 'fin' : 'pausa'; persist();
    if (porTiempo) root.replaceChildren(head('Se acabó el tiempo', 'Tus respuestas se entregaron tal como estaban.'), h('button', { class: 'btn primary', type: 'button', onclick: run }, 'Continuar'));
    else run();
  }

  function run() {
    clearInterval(tm);
    if (!st) return;
    if (st.fase === 'fin' || st.s >= st.ses.length) return fin();
    if (st.fase === 'pausa') return pausa();
    sesion();
  }

  function sesion(vista: 'q' | 'hoja' | 'ops' = 'q', foco?: string) {
    clearInterval(tm);
    const S = st!.ses[st!.s], P = plano(S);
    st!.cur = Math.min(st!.cur, P.length - 1);
    const clock = h('span', { class: 'clock', role: 'timer' });
    const tick = () => { if (!st || st.fase !== 'examen') { clearInterval(tm); return; } const left = Math.max(0, st!.end - Date.now()); clock.textContent = mmss(left); clock.classList.toggle('low', left < 600000); if (!left) entregar(true); };
    tm = setInterval(tick, 1000); tick();
    const ir = (k: number, v: 'q' | 'hoja' | 'ops' = 'q') => { st!.cur = k; persist(); sesion(v, v === 'q' ? P[k]?.id : undefined); };
    const contestadas = P.filter((x) => (st!.resp[x.id] ?? -1) >= 0).length;
    const bar = h('div', { class: 'row between exbar' }, h('div', {}, h('b', {}, S.titulo), h('small', {}, ` · ${contestadas} de ${P.length} contestadas`)), clock);
    const tabs = h('div', { class: 'row extabs' },
      h('button', { class: 'btn sm' + (vista === 'q' ? ' primary' : ''), type: 'button', onclick: () => ir(st!.cur) }, 'Cuadernillo'),
      h('button', { class: 'btn sm' + (vista === 'hoja' ? ' primary' : ''), type: 'button', onclick: () => ir(st!.cur, 'hoja') }, 'Hoja de respuestas'),
      h('button', { class: 'btn sm' + (vista === 'ops' ? ' primary' : ''), type: 'button', onclick: () => ir(st!.cur, 'ops') }, 'Hoja de operaciones'));
    const entregarBtn = h('button', { class: 'btn', type: 'button', onclick: () => confirmar() }, st!.s + 1 >= st!.ses.length ? 'Entregar y ver resultados' : 'Entregar esta sesión');
    function confirmar() {
      const sin = P.length - P.filter((x) => (st!.resp[x.id] ?? -1) >= 0).length;
      const dlg = h('div', { class: 'zoomf', role: 'dialog', 'aria-modal': 'true' }, h('div', { class: 'zbody' }, h('h3', {}, '¿Entregar la sesión?'), h('p', {}, sin ? `Te faltan ${sin} sin responder. Después de entregar no puedes volver a esta sesión.` : 'Ya respondiste todo. Después de entregar no puedes volver a esta sesión.'), h('div', { class: 'row' }, h('button', { class: 'btn primary', type: 'button', onclick: () => { dlg.remove(); entregar(false); } }, 'Sí, entregar'), h('button', { class: 'btn', type: 'button', onclick: () => dlg.remove() }, 'Seguir revisando'))));
      document.body.append(dlg);
    }
    const palette = h('nav', { class: 'expal', 'aria-label': 'Preguntas' }, ...S.pruebas.map((p, pi) => h('div', { class: 'expr' }, h('small', {}, p.titulo), h('div', { class: 'exbtns' }, ...P.filter((x) => x.pi === pi).map((x) => {
      const k = P.indexOf(x), cls = ['exn', (st!.resp[x.id] ?? -1) >= 0 ? 'on' : '', st!.marca[x.id] ? 'flag' : '', k === st!.cur && vista === 'q' ? 'cur' : ''].join(' ');
      return h('button', { class: cls, type: 'button', 'data-id': x.id, 'aria-label': `Pregunta ${x.n} de ${p.titulo}${(st!.resp[x.id] ?? -1) >= 0 ? ', contestada' : ', en blanco'}${st!.marca[x.id] ? ', marcada' : ''}`, onclick: () => ir(k) }, String(x.n));
    })))));
    let cuerpo: HTMLElement;
    if (vista === 'hoja') {
      cuerpo = h('div', { class: 'hojar' }, h('p', { class: 'fine' }, 'Así quedaría tu hoja de respuestas. Toca una burbuja para marcar o cambiar tu respuesta.'),
        ...S.pruebas.map((p, pi) => h('section', {}, h('h3', {}, p.titulo), h('div', { class: 'burb' }, ...P.filter((x) => x.pi === pi).map((x) => {
          const q = qOf(x.id);
          return h('div', { class: 'brow' }, h('b', {}, String(x.n)), ...q.opciones.map((_, i) => h('button', { class: 'bub' + (st!.resp[x.id] === i ? ' on' : ''), type: 'button', 'aria-label': `Pregunta ${x.n}, opción ${LET[i]}`, 'aria-pressed': String(st!.resp[x.id] === i), onclick: () => { st!.resp[x.id] = st!.resp[x.id] === i ? -1 : i; persist(); sesion('hoja'); } }, LET[i])));
        })))));
    } else if (vista === 'ops') {
      cuerpo = h('div', {}, h('p', { class: 'fine' }, 'Hoja de operaciones: úsala para cálculos y borradores. No se califica.'), crearPad());
    } else {
      const pi = P[st!.cur].pi, prueba = S.pruebas[pi], delPrueba = P.filter((y) => y.pi === pi);
      const selector = h('div', { class: 'row extabs' }, ...S.pruebas.map((p, k) => h('button', { class: 'btn sm' + (k === pi ? ' primary' : ''), type: 'button', onclick: () => ir(P.findIndex((y) => y.pi === k)) }, p.titulo)));
      const vistos = new Set<string>(), items: HTMLElement[] = [];
      for (const x of delPrueba) {
        const q: Question = qOf(x.id), marcada = !!st!.marca[x.id];
        if (q.bloque && !vistos.has(q.bloque)) {
          vistos.add(q.bloque); const g = delPrueba.filter((y) => qOf(y.id).bloque === q.bloque), bl = bloqueDe(q);
          if (bl) items.push(bloqueEl(bl, g.length > 1 ? `${g[0].n} A ${g[g.length - 1].n}` : undefined));
        }
        const card = renderQuestion(q, () => undefined, { feedback: false, sinBloque: true, examen: { elegida: st!.resp[x.id] ?? -1, onPick: (i) => { st!.resp[x.id] = i; persist(); const pb = palette.querySelector<HTMLElement>(`[data-id="${x.id}"]`); pb?.classList.toggle('on', i >= 0); } } });
        items.push(h('article', { class: 'exq', id: `pq-${x.id}` }, h('div', { class: 'row between' }, h('p', { class: 'qnum' }, h('b', {}, `Pregunta ${x.n}`)), h('div', { class: 'row' },
          h('button', { class: 'btn sm' + (marcada ? ' primary' : ''), type: 'button', 'aria-pressed': String(marcada), onclick: (e: Event) => { const on = !st!.marca[x.id]; if (on) st!.marca[x.id] = 1; else delete st!.marca[x.id]; persist(); const t = e.currentTarget as HTMLElement; t.classList.toggle('primary', on); t.setAttribute('aria-pressed', String(on)); t.textContent = on ? 'Marcada' : 'Marcar'; palette.querySelector(`[data-id="${x.id}"]`)?.classList.toggle('flag', on); } }, marcada ? 'Marcada' : 'Marcar'),
          h('button', { class: 'btn sm', type: 'button', onclick: () => { st!.resp[x.id] = -1; persist(); sesion('q', x.id); } }, 'Borrar'))), card));
      }
      cuerpo = h('div', {}, selector, h('p', { class: 'fine' }, `${prueba.titulo}: ${delPrueba.length} preguntas. Recorre el cuadernillo con el dedo o con la paleta; puedes cambiar tus respuestas hasta entregar.`), ...items);
      if (foco) requestAnimationFrame(() => { document.getElementById(`pq-${foco}`)?.scrollIntoView({ block: 'start' }); });
    }
    root.replaceChildren(bar, tabs, palette, cuerpo, h('div', { class: 'row' }, entregarBtn));
    root.scrollIntoView?.({ block: 'start' });
  }

  function evaluar() {
    const filas: { id: string; prueba: string; n: number; sesion: string }[] = [];
    st!.ses.forEach((S) => S.pruebas.forEach((p) => p.ids.forEach((id, k) => filas.push({ id, prueba: p.titulo, n: k + 1, sesion: S.titulo }))));
    return filas;
  }

  function fin() {
    clearInterval(tm);
    const filas = evaluar(), r = st!.resp;
    const per: Partial<Record<AreaId, Resp[]>> = {};
    for (const f of filas) { const q = qOf(f.id); (per[q.area] ??= []).push({ item: itemOf(q), correct: r[f.id] === q.correcta }); }
    const sc: Partial<Record<AreaId, number>> = {}, se: Partial<Record<AreaId, number>> = {};
    for (const a of AREA_IDS) if (per[a]) { const e = eap(per[a]!); sc[a] = areaScore(a, e.theta); se[a] = areaSE(a, e.se); }
    const g = globalScore(sc), ok = filas.filter((f) => r[f.id] === qOf(f.id).correcta).length;
    if (!st!.ent.includes(-1)) {
      const H = lee<Record<string, unknown[]>>(HKEY, {}); H[def.id] = [...(H[def.id] ?? []), { t: Date.now(), g, ok, n: filas.length }].slice(-12); escribe(HKEY, H);
      filas.forEach((f) => { const q = qOf(f.id); if ((r[f.id] ?? -1) >= 0) record(q, r[f.id] === q.correcta, 'sim'); }); st!.ent.push(-1); persist(); syncSoon();
    }
    const blancas = filas.filter((f) => (r[f.id] ?? -1) < 0).length;
    let filtro: 'todas' | 'mal' | 'blanco' | 'marca' = 'todas';
    const tabla = h('div'), detalle = h('div');
    const pintar = () => {
      const lista = filas.filter((f) => { const q = qOf(f.id), e = r[f.id] ?? -1; return filtro === 'todas' || (filtro === 'mal' && e >= 0 && e !== q.correcta) || (filtro === 'blanco' && e < 0) || (filtro === 'marca' && st!.marca[f.id]); });
      tabla.replaceChildren(h('div', { class: 'row exfil' }, ...([['todas', 'Todas'], ['mal', 'Incorrectas'], ['blanco', 'En blanco'], ['marca', 'Marcadas']] as const).map(([k, t]) => h('button', { class: 'btn sm' + (filtro === k ? ' primary' : ''), type: 'button', onclick: () => { filtro = k; pintar(); } }, t))),
        h('div', { class: 'tablewrap' }, h('table', { class: 'simtab revt' }, h('thead', {}, h('tr', {}, ['Pos.', 'Prueba', 'Afirmación', 'Tu respuesta', 'Correcta', ''].map((t) => h('th', {}, t)))),
          h('tbody', {}, ...lista.map((f) => { const q = qOf(f.id), e = r[f.id] ?? -1, bien = e === q.correcta; return h('tr', { class: e < 0 ? 'blank' : bien ? 'okr' : 'badr' }, h('td', {}, String(f.n)), h('td', {}, f.prueba), h('td', {}, q.afirmacion ?? q.competencia ?? '—'), h('td', {}, e < 0 ? 'Sin responder' : `${LET[e]}${bien ? ' ✓' : ' ✗'}`), h('td', {}, LET[q.correcta]), h('td', {}, h('button', { class: 'btn sm', type: 'button', onclick: () => abrir(f) }, 'Revisar'))); })))));
    };
    const abrir = (f: { id: string; n: number; prueba: string }) => {
      const q = qOf(f.id), P = filas.filter((y) => y.prueba === f.prueba), grupo = q.bloque ? P.filter((y) => qOf(y.id).bloque === q.bloque) : [];
      detalle.replaceChildren(h('div', { class: 'revq' }, h('p', { class: 'qnum' }, h('b', {}, `Pregunta ${f.n}`), h('small', {}, ` · ${f.prueba}`)), renderQuestion(q, () => undefined, { feedback: true, ayuda: 'siempre', rango: grupo.length > 1 ? `${grupo[0].n} A ${grupo[grupo.length - 1].n}` : undefined, revisar: { elegida: r[f.id] ?? -1 } }), h('button', { class: 'btn sm', type: 'button', onclick: () => detalle.replaceChildren() }, 'Cerrar revisión')));
      detalle.scrollIntoView?.({ block: 'start', behavior: 'smooth' });
    };
    pintar();
    const porPrueba = st!.ses.flatMap((S) => S.pruebas).map((p) => ({ p, ok: p.ids.filter((id) => r[id] === qOf(id).correcta).length }));
    root.replaceChildren(head(`Resultado: ${def.nombre}`),
      h('div', { class: 'panelgrid' }, h('figure', { class: 'radar' }, h('div', { html: radar(sc) }), h('figcaption', {}, 'Resultado frente a la media nacional.')),
        h('div', {}, ...AREA_IDS.filter((a) => per[a]).map((a) => h('div', { class: 'arow' }, h('b', {}, AREAS[a].nombre), h('div', { class: 'bar' }, h('i', { style: `width:${sc[a] ?? 0}%` }), h('u', { style: `left:${AREAS[a].mu}%` })), h('span', {}, `${sc[a] ?? 0}`))))),
      ...(g === null ? [] : [h('div', { class: 'bigscore' }, h('b', {}, String(g)), h('span', {}, `de 500 · estimado ± ${Math.round(globalSE(se))} · ${ok} de ${filas.length} correctas${blancas ? ` · ${blancas} en blanco` : ''}`))]),
      h('table', { class: 'simtab' }, h('thead', {}, h('tr', {}, h('th', {}, 'Prueba'), h('th', {}, 'Aciertos'))), h('tbody', {}, ...porPrueba.map((x) => h('tr', {}, h('td', {}, x.p.titulo), h('td', {}, `${x.ok} de ${x.p.ids.length}`))))),
      ...(nivelesPanel(sc) ? [nivelesPanel(sc)!] : []),
      h('h2', {}, 'Revisión completa'), h('p', { class: 'fine' }, 'Toca «Revisar» en cualquier pregunta para ver el enunciado, tu respuesta, la correcta y la explicación del profe.'), tabla, detalle,
      h('div', { class: 'row' }, h('button', { class: 'btn', type: 'button', onclick: () => { st = null; persist(); intro(); } }, 'Hacerlo otra vez'), h('a', { class: 'btn primary', href: '#/simulacro' }, 'Ver los simulacros')),
      h('p', { class: 'fine' }, DISCLAIMER));
  }

  intro();
  return root;
}
