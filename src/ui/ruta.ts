import { h } from './dom';
import { renderQuestion } from './question';
import { hero } from './hero';
import { go, query } from './nav';
import { head, ruler, gate, icon, mcs, rnd, DISCLAIMER } from './pages';
import { AREAS, AREA_IDS, type AreaId } from '../adaptive/areas';
import { pickItem } from '../adaptive/irt';
import { QUESTIONS, SIMULACROS_ALL } from '../content';
import { UNIDADES, unidad, unidadesDe, preguntasDe, tieneSim, tieneLeccion, type Unidad } from '../content/unidades';
import { simulacroTarjetas } from './simulacro';
import { summary, load, record, itemOf, dueCards, syncSoon, hasAccess, seen, day } from '../state/store';
import type { Question } from '../content/schema';

/* ───────── Estado de cada unidad, calculado a partir de las respuestas ───────── */
export interface Estado { total: number; hechas: number; ok: number; lab: boolean; lec: boolean; nivel: 'nueva' | 'curso' | 'dominada' }
export function estado(u: Unidad): Estado {
  const ult = new Map<string, boolean>();
  for (const a of load().answers) if (u.preguntas.includes(a.qid)) ult.set(a.qid, a.ok);
  const ok = [...ult.values()].filter(Boolean).length, hechas = ult.size, total = u.preguntas.length;
  const lab = !!u.sim && seen('sim:' + u.sim), lec = !!u.leccion && seen('les:' + u.leccion);
  const nivel = hechas === total && ok / total >= 0.8 ? 'dominada' : hechas || lab || lec ? 'curso' : 'nueva';
  return { total, hechas, ok, lab, lec, nivel };
}
const ETQ = { nueva: 'Sin empezar', curso: 'En curso', dominada: 'Dominada' } as const;
const aviso = () => h('p', { class: 'fine' }, DISCLAIMER);

/** Siguiente unidad que conviene estudiar: la del área más baja que todavía no domina. */
export function recomendada(): Unidad | undefined {
  const s = summary();
  const orden = [...AREA_IDS].sort((a, b) => (s.sc[a] ?? AREAS[a].mu - 1) - (s.sc[b] ?? AREAS[b].mu - 1));
  for (const a of orden) { const u = unidadesDe(a).find((x) => estado(x).nivel !== 'dominada'); if (u) return u; }
  return undefined;
}
const diagHecho = () => load().answers.some((a) => a.mode === 'diag');

/* ───────── Hoy ───────── */
export function hoy(): HTMLElement {
  return diagHecho() ? tablero() : bienvenida();
}

function bienvenida(): HTMLElement {
  const paso = (n: string, t: string, d: string, extra?: Node) => h('li', {}, h('span', { class: 'n' }, n), h('div', {}, h('b', {}, t), h('p', {}, d), extra ?? null));
  return h('div', {},
    h('section', { class: 'hero' },
      h('div', {}, h('h1', {}, 'Tu ruta al Saber 11'),
        h('p', { class: 'lede' }, 'Empiezas con un diagnóstico rápido de 15 preguntas (~10 min). Con eso te armamos una ruta personalizada: qué temas estudiar primero, cada uno con laboratorio, explicación y preguntas guiadas.'),
        h('div', { class: 'cta' }, h('a', { class: 'btn primary big', href: '#/diag' }, 'Empezar el diagnóstico (gratis) →'), h('a', { class: 'btn', href: '#/aprender' }, 'Prefiero explorar los temas')),
        aviso()),
      hero()),
    h('h2', { class: 'secth' }, 'Así funciona'),
    h('ol', { class: 'pasos3' },
      paso('1', 'Diagnóstico rápido (~10 min)', '15 preguntas adaptativas que miden tu nivel real en las 5 áreas obligatorias sin notas de juicio.'),
      paso('2', 'Tu ruta personalizada', 'Comienzas por tu área con mayor oportunidad de mejora: laboratorio interactivo, lección conceptual y práctica con el profe.'),
      paso('3', 'Práctica y simulacros', 'Sesiones cortas de 8 preguntas para mantener tu racha y simulacros completos cronometrados tipo examen real.')),
    h('h2', { class: 'secth' }, 'Preguntas frecuentes'),
    h('div', { class: 'faq-preview', style: 'display:grid;gap:10px;margin-bottom:1rem' },
      h('details', { class: 'box' },
        h('summary', { style: 'cursor:pointer;font-weight:600' }, '¿Qué es Saber 11 Interactivo?'),
        h('p', { class: 'fine', style: 'margin-top:8px' }, 'Plataforma web educativa gratuita con laboratorios de física y matemáticas, diagnóstico adaptativo de 15 preguntas y simulacros cronometrados tipo examen real.')
      ),
      h('details', { class: 'box' },
        h('summary', { style: 'cursor:pointer;font-weight:600' }, '¿Es 100% gratis?'),
        h('p', { class: 'fine', style: 'margin-top:8px' }, 'Sí. Todo el contenido pedagógico (diagnóstico, laboratorios, lecciones, práctica adaptativa y simulacros) es totalmente gratuito.')
      ),
      h('details', { class: 'box' },
        h('summary', { style: 'cursor:pointer;font-weight:600' }, '¿Cuáles son las 5 áreas obligatorias evaluadas?'),
        h('p', { class: 'fine', style: 'margin-top:8px' }, 'Matemáticas, Lectura Crítica, Sociales y Ciudadanas, Ciencias Naturales e Inglés.')
      ),
      h('details', { class: 'box' },
        h('summary', { style: 'cursor:pointer;font-weight:600' }, '¿Cómo prepararse de forma efectiva?'),
        h('p', { class: 'fine', style: 'margin-top:8px' }, 'Haz el diagnóstico de 10 min, estudia primero tus áreas más débiles en los laboratorios y entrena 15 minutos diarios.')
      )
    ),
    h('p', { style: 'margin-bottom:1.5rem' }, h('a', { class: 'btn sm', href: '#/faq' }, 'Ver todas las preguntas frecuentes (FAQ) →')),
    h('p', { class: 'fine' }, '¿Prefieres ver todo antes de empezar? Abre el ', h('a', { href: '#/mapa' }, 'mapa de la plataforma'), ' o consulta las ', h('a', { href: '#/faq' }, 'preguntas frecuentes (FAQ)'), '.'));
}

function tablero(): HTMLElement {
  const d = load(), s = summary(), due = dueCards().length, rec = recomendada();
  const falta = d.examDay ? d.examDay - day() : null;
  const items: { t: string; sub: string; href: string; ic: string }[] = [];
  if (due) items.push({ t: `Repasar ${due} ${due === 1 ? 'pregunta' : 'preguntas'}`, sub: 'Lo que estás a punto de olvidar', href: '#/sesion?modo=repaso', ic: 'reset' });
  if (rec) items.push({ t: rec.titulo, sub: `${AREAS[rec.area].nombre} · tu siguiente tema (~${rec.min} min)`, href: `#/unidad/${rec.id}`, ic: 'book' });
  items.push({ t: 'Práctica mixta de 8 preguntas', sub: 'Adaptada a tu nivel (~15 min)', href: '#/sesion', ic: 'pencil' });
  const principal = items[0];
  return h('div', {},
    h('div', { class: 'hoyhead' },
      h('div', {}, h('h1', {}, 'Hoy'), h('p', { class: 'lede' }, d.streak.count ? (d.streak.count === 1 ? 'Llevas 1 día seguido. Sigue con tu ruta.' : `Llevas ${d.streak.count} días seguidos. Sigue con tu ruta.`) : 'Estudia un rato hoy y empieza tu racha.')),
      h('div', { class: 'chips3' },
        h('div', { class: 'stat' }, h('b', {}, s.global === null ? '—' : String(s.global)), h('span', {}, 'puntaje estimado de 500')),
        h('div', { class: 'stat' }, h('b', {}, String(d.streak.count)), h('span', {}, 'racha en días')),
        h('a', { class: 'stat', href: '#/panel' }, h('b', {}, falta === null ? '+' : falta >= 0 ? String(falta) : '0'), h('span', {}, falta === null ? 'fecha del examen' : 'días para el examen')))),
    h('section', { class: 'hoycard' },
      h('h2', {}, 'Tu sesión de hoy'),
      h('ol', { class: 'plan' }, ...items.map((it, i) => h('li', {}, h('a', { href: it.href }, icon(it.ic, 22), h('span', {}, h('b', {}, it.t), h('small', {}, it.sub)), h('i', { class: 'go' }, i === 0 ? 'Ahora' : '→'))))),
      h('a', { class: 'btn primary big', href: principal.href }, 'Continuar')),
    h('h2', { class: 'secth' }, 'Ir directo a…'),
    h('div', { class: 'chips' }, h('a', { class: 'chip', href: '#/sims' }, 'Laboratorios'), h('a', { class: 'chip', href: '#/simulacro' }, 'Simulacros'), h('a', { class: 'chip', href: '#/practicar' }, 'Practicar una materia'), h('a', { class: 'chip', href: '#/contenido' }, 'Todo el contenido'), h('a', { class: 'chip', href: '#/mapa' }, 'Mapa de la plataforma')),
    h('h2', { class: 'secth' }, 'Tu nivel por área'),
    h('div', { class: 'areas' }, ...AREA_IDS.map((a) => {
      const v = s.sc[a], us = unidadesDe(a), dom = us.filter((u) => estado(u).nivel === 'dominada').length;
      return h('a', { class: 'area', href: `#/aprender?area=${a}` }, h('b', {}, AREAS[a].nombre), h('div', { class: 'bar' }, h('i', { style: `width:${v ?? 0}%` }), h('u', { style: `left:${AREAS[a].mu}%`, title: 'Media nacional' })), h('span', {}, v === undefined ? 'sin datos' : `${v}/100`), h('small', {}, `${dom} de ${us.length} temas dominados`));
    })),
    aviso());
}

/* ───────── Aprender ───────── */
export function aprender(): HTMLElement {
  const sel = query().get('area') as AreaId | null;
  const areas = sel && AREAS[sel] ? [sel] : AREA_IDS;
  // Las preguntas oficiales solo llegan a QUESTIONS cuando VITE_ICFES=1;
  // por eso esta biblioteca desaparece por completo en el build publicado normal.
  const oficiales = QUESTIONS.filter((q) => q.origen === 'icfes');
  const banco = oficiales.length ? h('section', { class: 'official-bank' },
    h('div', { class: 'sectionhead' }, h('h2', {}, 'Preguntas oficiales'), h('span', { class: 'tag' }, `${oficiales.length} preguntas · ${UNIDADES.filter((u) => u.id.startsWith('u-icfes-')).length} rutas · ${SIMULACROS_ALL.filter((s) => s.id.startsWith('sim-icfes-')).length} simulacros`)),
    h('p', { class: 'fine' }, 'Abre un área y entra a cualquier pregunta para ver su explicación pedagógica completa.'),
    ...areas.filter((a) => oficiales.some((q) => q.area === a)).map((a) => {
      const qs = oficiales.filter((q) => q.area === a);
      return h('details', { class: 'official-area' }, h('summary', {}, h('b', {}, AREAS[a].nombre), h('small', {}, `${qs.length} preguntas`)),
        h('div', { class: 'official-question-list' }, ...qs.map((q) => h('a', { class: 'path', href: `#/pregunta/${q.id}` },
          h('b', {}, q.id.toUpperCase()), h('span', {}, q.enunciado.replace(/\s+/g, ' ').slice(0, 180) + (q.enunciado.length > 180 ? '…' : ''))))));
    })) : null;
  const chips = h('div', { class: 'chips filters area-chips-scroll', role: 'group', 'aria-label': 'Filtrar por área' },
    h('a', { class: 'chip', href: '#/aprender', 'aria-pressed': String(!sel) }, 'Todas'), ...AREA_IDS.map((a) => h('a', { class: 'chip', href: `#/aprender?area=${a}`, 'aria-pressed': String(sel === a) }, AREAS[a].nombre)));
  const rec = recomendada();
  return h('div', {},
    head('Aprender', 'Elige un tema y estúdialo en tres pasos: míralo en el laboratorio, léelo y practícalo con preguntas. Si no sabes cuál, empieza por el recomendado.'),
    rec && !sel ? h('a', { class: 'startcard', href: `#/unidad/${rec.id}` }, h('small', {}, 'Tu siguiente tema'), h('b', {}, rec.titulo), h('span', {}, `${AREAS[rec.area].nombre} · unos ${rec.min} minutos`), h('i', { class: 'go' }, 'Empezar →')) : null,
    chips,
    banco,
    ...areas.map((a) => {
      const us = unidadesDe(a), hechos = us.filter((u) => estado(u).nivel === 'dominada').length;
      return h('details', { class: 'areasec', open: !!sel || (rec ? rec.area === a : a === areas[0]) || (!sel && a === 'matematicas') },
        h('summary', {}, h('h2', {}, AREAS[a].nombre), h('small', {}, `${hechos} de ${us.length} dominados`), h('span', { class: 'areabar', 'aria-hidden': 'true' }, h('i', { style: `width:${Math.round(100 * hechos / Math.max(1, us.length))}%` }))),
        h('div', { class: 'unitgrid' }, ...us.map((u) => tarjeta(u, rec?.id === u.id))));
    }),
    h('p', { class: 'fine' }, 'También puedes ', h('a', { href: '#/sims' }, 'ver todos los laboratorios'), ' sueltos.'));
}

function tarjeta(u: Unidad, recomendado: boolean): HTMLElement {
  const e = estado(u);
  return h('a', { class: `unit n-${e.nivel}`, href: `#/unidad/${u.id}` },
    h('div', { class: 'ubadges' }, recomendado ? h('span', { class: 'rec' }, 'Recomendado') : null, e.nivel === 'nueva' ? null : h('span', { class: `est ${e.nivel}` }, ETQ[e.nivel])),
    h('h3', {}, u.titulo), h('p', {}, u.resumen),
    h('div', { class: 'usteps' }, tieneSim(u) ? h('span', { class: e.lab ? 'ok' : '' }, 'Laboratorio') : null, tieneLeccion(u) ? h('span', { class: e.lec ? 'ok' : '' }, 'Lección') : null, h('span', { class: e.hechas === e.total ? 'ok' : '' }, `${e.hechas}/${e.total} preguntas`)),
    h('div', { class: 'bar thin' }, h('i', { style: `width:${(e.ok / e.total) * 100}%` })));
}

/* ───────── Unidad ───────── */
export function unidadPage(id: string, modo?: string): HTMLElement {
  const u = unidad(id);
  if (!u) return h('div', {}, head('Tema no encontrado'), h('a', { class: 'btn', href: '#/aprender' }, 'Volver a Aprender'));
  if (modo === 'practica') return gate(() => sesion({ titulo: u.titulo, volver: `#/unidad/${u.id}`, preguntas: preguntasDe(u) }));
  const e = estado(u), pasos: { n: string; t: string; d: string; hecho: boolean; href: string; cta: string; lock?: boolean }[] = [];
  if (tieneSim(u)) pasos.push({ n: 'Míralo', t: 'Laboratorio', d: 'Mueve los valores y mira qué cambia. Te pide predecir antes de mostrarte la respuesta.', hecho: e.lab, href: `#/sim/${u.sim}`, cta: e.lab ? 'Volver a verlo' : 'Abrir el laboratorio' });
  if (tieneLeccion(u)) pasos.push({ n: 'Léelo', t: 'Lección', d: 'El tema visto desde cinco ángulos: la calle, un dato real, un gráfico, la versión formal y el error típico.', hecho: e.lec, href: `#/leccion/${u.leccion}`, cta: e.lec ? 'Releer' : 'Leer la lección', lock: !hasAccess() });
  pasos.push({ n: 'Practícalo', t: `Preguntas (${e.hechas}/${e.total})`, d: 'Primero la intentas tú. Si no logras avanzar, el profe te explica con voz, ejemplos y el porqué de cada opción.', hecho: e.hechas === e.total && e.ok / e.total >= 0.8, href: `#/unidad/${u.id}/practica`, cta: e.hechas ? 'Practicar otra vez' : 'Empezar a practicar', lock: !hasAccess() });
  const sig = pasos.find((p) => !p.hecho);
  return h('div', {},
    h('div', { class: 'pagehead' }, h('a', { class: 'crumb', href: `#/aprender?area=${u.area}` }, `← ${AREAS[u.area].nombre}`), h('h1', {}, u.titulo), h('p', { class: 'lede' }, u.resumen), e.nivel === 'nueva' ? null : h('span', { class: `est ${e.nivel}` }, ETQ[e.nivel])),
    h('ol', { class: 'ustages' }, ...pasos.map((p, i) => h('li', { class: `${p.hecho ? 'done' : ''} ${p === sig ? 'now' : ''}` },
      h('span', { class: 'mk' }, p.hecho ? '✓' : String(i + 1)),
      h('div', {}, h('small', {}, p.n), h('b', {}, p.t), h('p', {}, p.d), h('a', { class: `btn ${p === sig ? 'primary' : ''}`, href: p.href }, (p.lock ? '🔒 ' : '') + p.cta))))),
    sig ? null : h('div', { class: 'box trick' }, h('span', { class: 'hand' }, '¡Tema dominado!'), h('p', { style: 'margin:6px 0 0' }, 'Pasa al siguiente tema desde Aprender, o haz una práctica mixta para que no se te olvide.'), h('a', { class: 'btn primary', href: '#/aprender' }, 'Elegir otro tema')));
}

/* ───────── Practicar (menú) ───────── */
export function practicar(): HTMLElement {
  const due = dueCards().length;
  const op = (href: string, ic: string, t: string, d: string, tag?: string) => h('a', { class: 'path card-path', href },
    h('div', { class: 'path-icon-box' }, icon(ic, 22)),
    h('div', { class: 'path-body' },
      h('div', { class: 'path-title-row' },
        h('b', {}, t),
        tag ? h('em', { class: 'tag2' }, tag) : null
      ),
      h('span', { class: 'path-desc' }, d)
    ),
    h('span', { class: 'path-arrow' }, '→')
  );
  return h('div', {}, head('Practicar', 'Aquí pones a prueba lo aprendido: práctica según tu nivel, simulacros cronometrados o el diagnóstico. Si apenas empiezas, hazlo primero.'),
    h('div', { class: 'paths prac-paths' },
      op('#/sesion', 'pencil', 'Sesión de práctica adaptativa', '8 preguntas adaptadas a tu nivel (~15 min) con resumen final.', due ? `${due} repasos pendientes` : 'Recomendado'),
      op('#/simulacro', 'clock', 'Simulacros tipo examen', 'Pruebas completas como el examen real: tiempo por sección, sin ayudas y con puntaje estimado.'),
      op('#/diag', 'target', 'Repetir el diagnóstico', '15 preguntas rápidas (~10 min) para actualizar tu nivel en cada área.'),
      op('#/contenido', 'book', 'Todo el contenido', 'Entra directo a cualquier simulacro, laboratorio, lección o pregunta, sin seguir la ruta.'),
      op('#/extras', 'ruler', 'Actividades de entrenamiento', 'Lectura, inglés, ciudadanía y línea de tiempo para practicar sueltos.')),
    h('h2', { class: 'secth' }, 'Practicar una sola materia'),
    h('p', { class: 'fine' }, 'Elige un área para resolver preguntas enfocadas exclusivamente en esa prueba:'),
    h('div', { class: 'chips filters area-chips-scroll' }, ...AREA_IDS.map((a) => h('a', { class: 'chip', href: `#/sesion?area=${a}` }, `🎯 ${AREAS[a].nombre}`))),
    h('h2', { class: 'secth' }, 'Simulacros disponibles'), simulacroTarjetas());
}

/* ───────── Sesión de preguntas con resumen ───────── */
interface SesionOpts { titulo: string; volver: string; preguntas?: Question[]; total?: number; repaso?: boolean; area?: AreaId }
export function sesion(o: SesionOpts): HTMLElement {
  const root = h('div'), res: { q: Question; ok: boolean }[] = [], visto = new Set<string>();
  const total = o.preguntas?.length ?? o.total ?? 8;
  let n = 0;
  const elegir = (): Question | undefined => {
    if (o.preguntas) return o.preguntas[n];
    const due = dueCards().map((id) => QUESTIONS.find((q) => q.id === id)).filter((q): q is Question => !!q && !visto.has(q.id));
    if (due.length && (!o.area || due[0].area === o.area)) return due[0];
    const s = summary(), orden = [...AREA_IDS].sort((a, b) => (s.sc[a] ?? 0) - (s.sc[b] ?? 0));
    const area = o.area ?? orden[n % 3];
    const th = ((s.sc[area] ?? AREAS[area].mu) - AREAS[area].mu) / AREAS[area].sigma;
    return pickItem(th, mcs(area).filter((x) => !visto.has(x.id)).map((x) => ({ x, item: itemOf(x) })), rnd)?.x ?? mcs().find((x) => !visto.has(x.id));
  };
  function paso() {
    const q = elegir();
    if (!q || n >= total) return fin();
    visto.add(q.id);
    const sig = h('button', { class: 'btn', type: 'button', disabled: true, onclick: () => { n++; paso(); } }, n + 1 >= total ? 'Ver resumen' : 'Siguiente') as HTMLButtonElement;
    const barra = h('div', { class: 'sesionbar' }, h('a', { class: 'btn sm', href: o.volver }, '✕ Salir'), h('div', { class: 'sinfo' }, h('b', {}, o.titulo), ruler(total, n), h('span', {}, `Pregunta ${n + 1} de ${total}`)), sig);
    const hint = h('p', { class: 'sighint', role: 'status' }, 'Elige una respuesta para continuar') as HTMLElement;
    let hecha = false;
    const listo = (ok: boolean, nota?: string) => { if (hecha) return; hecha = true; res.push({ q, ok }); record(q, ok, 'prac'); syncSoon(); sig.disabled = false; sig.classList.add('primary'); hint.textContent = nota ?? ''; hint.hidden = !nota; };
    const alVer = () => { if (!hecha) listo(false, 'Viste la solución: esta pregunta volverá en tus repasos. Toca el botón de arriba para seguir.'); };
    document.addEventListener('hoja:fin', alVer, { once: true });
    root.replaceChildren(barra, hint, renderQuestion(q, (ok) => { listo(ok); sig.focus({ preventScroll: true }); }));
  }
  function fin() {
    const ok = res.filter((r) => r.ok).length, mal = res.filter((r) => !r.ok);
    root.replaceChildren(head('Sesión completada', `${o.titulo}`),
      h('div', { class: 'bigscore' }, h('b', {}, `${ok}/${res.length}`), h('span', {}, ok === res.length ? '¡Perfecto!' : ok / Math.max(1, res.length) >= 0.6 ? 'Buen trabajo' : 'Vale la pena repasar')),
      ...(mal.length ? [h('div', { class: 'box' }, h('h2', { style: 'font-size:1.2rem' }, 'Para repasar'), h('ul', {}, ...mal.map((r) => h('li', {}, AREAS[r.q.area].nombre, ': ', h('span', { html: r.q.enunciado.slice(0, 90) + '…' })))), h('p', { class: 'fine' }, 'Estas preguntas volverán en tus repasos automáticamente.'))] : []),
      h('div', { class: 'row' }, h('a', { class: 'btn primary', href: '#/' }, 'Volver a Hoy'), h('button', { class: 'btn', type: 'button', onclick: () => go(location.hash.slice(1) || '/sesion') }, 'Otra sesión'), h('a', { class: 'btn', href: o.volver }, o.volver === '#/' ? 'Inicio' : 'Volver al tema')));
  }
  paso();
  return root;
}
export function sesionGeneral(repaso = false): HTMLElement {
  const a = query().get('area') as AreaId | null, area = a && AREAS[a] ? a : undefined;
  return gate(() => sesion({ titulo: repaso ? 'Repaso' : area ? `Práctica de ${AREAS[area].nombre}` : 'Práctica mixta', volver: '#/practicar', total: 8, repaso, area }));
}
void UNIDADES;
