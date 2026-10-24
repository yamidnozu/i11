import { h } from './dom';
import { renderQuestion, dots } from './question';
import { hero } from './hero';
import { radar } from './radar';
import { ico } from './icons';
import { rich } from './tex';
import { go, query } from './nav';
import { QUESTIONS, LESSONS } from '../content';
import { AREAS, AREA_IDS, type AreaId } from '../adaptive/areas';
import { eap, pickItem, type Resp } from '../adaptive/irt';
import { areaScore, areaSE, globalScore, globalSE } from '../adaptive/score';
import { NIVELES, nivelIndex } from '../content/niveles';
import { nivelesPanel } from './niveles';
import { record, itemOf, summary, load, save, hasAccess, dueCards, syncSoon, day, touch } from '../state/store';
import { listSims, getSim } from '../core/registry';
import { mountSim } from '../core/engine';
import { drawThumb } from '../core/thumb';
import type { SimConfig } from '../core/types';
import type { Question } from '../content/schema';

export const DISCLAIMER = 'Plataforma independiente: no es oficial del ICFES. Los puntajes son estimaciones orientativas, no resultados oficiales.';
export const rnd = () => Math.random();
export const mcs = (a?: AreaId) => QUESTIONS.filter((q) => q.tipo !== 'reto' && (!a || q.area === a));
export const icon = (n: string, s = 26) => h('span', { html: ico(n, s) });
const SUBS: Record<string, string> = { fisica: 'Física', quimica: 'Química', biologia: 'Biología' };
const grupo = (s: SimConfig) => (s.subarea ? SUBS[s.subarea] ?? s.subarea : AREAS[s.area].nombre);
const sheetNo = (s: SimConfig) => String(listSims().findIndex((x) => x.id === s.id) + 1).padStart(2, '0');
export const head = (title: string, lede?: string, extra?: Node | null) => h('div', { class: 'pagehead' }, h('h1', {}, title), lede ? h('p', { class: 'lede' }, lede) : null, extra);
export const ruler = (total: number, done: number) => h('div', { class: 'ruler', role: 'img', 'aria-label': `${done} de ${total}` }, ...Array.from({ length: total }, (_, i) => h('i', { class: i < done ? 'on' : i === done ? 'now' : '' })));

/* ───────── Miniaturas de las láminas (se dibujan de a una por cuadro) ───────── */
const thumbQueue: [SimConfig, HTMLCanvasElement][] = [];
let pumping = false;
function pump() {
  if (pumping) return;
  pumping = true;
  const step = () => {
    const it = thumbQueue.shift();
    if (!it) { pumping = false; return; }
    if (it[1].isConnected) { try { drawThumb(it[0], it[1]); } catch { /* miniatura opcional */ } }
    requestAnimationFrame(step);
  };
  requestAnimationFrame(step);
}
function plate(s: SimConfig): HTMLElement {
  const c = h('canvas', { 'aria-hidden': 'true' });
  thumbQueue.push([s, c]); pump();
  document.fonts?.ready.then(() => { thumbQueue.push([s, c]); pump(); });
  const sum = (s.learn?.resumen ?? '').replace(/\$/g, '');
  return h('a', { class: 'plate', href: `#/sim/${s.id}` },
    h('div', { class: 'plate-fig' }, c),
    h('div', { class: 'plate-body' }, h('span', { class: 'plate-no' }, grupo(s)), h('h3', {}, s.title), h('p', {}, sum.length > 130 ? sum.slice(0, sum.lastIndexOf(' ', 128)) + '…' : sum),
      h('div', { class: 'plate-meta' }, dots(s.nivel), h('span', {}, `~${s.tiempoMin} min`))));
}

export function gate(content: () => HTMLElement): HTMLElement {
  if (hasAccess()) return content();
  return h('div', { class: 'box lock' }, icon('lock', 30), h('h2', {}, 'Contenido de pago'), h('p', {}, 'El diagnóstico y los laboratorios son gratis. La práctica adaptativa, las lecciones completas y los simulacros requieren el acceso de 12 meses (COP 29.900).'), h('a', { class: 'btn primary', href: '#/pago' }, 'Obtener acceso'));
}

export function home(): HTMLElement {
  const s = summary(), sims = listSims();
  const paths: [string, string, string, string][] = [
    ['#/diag', 'target', 'Diagnóstico gratis', '15 preguntas rápidas para conocer tu nivel (~10 min).'],
    ['#/practica', 'pencil', 'Práctica adaptativa', 'Preguntas a tu medida y repaso espaciado de lo que se te olvida.'],
    ['#/simulacro', 'clock', 'Simulacro cronometrado', 'Sin ayudas, con puntaje estimado por área.'],
    ['#/panel', 'chart', 'Mi progreso', s.global ? `Estimado actual: ${s.global} de 500.` : 'Racha, radar de áreas y recomendaciones.'],
    ['#/lecciones', 'book', 'Lecciones', 'Cada tema visto desde cinco ángulos distintos.'],
    ['#/contenido', 'book', 'Todo el contenido', 'Simulacros, laboratorios, lecciones y todas las preguntas, gratis y sin orden fijo.'],
    ['#/extras', 'ruler', 'Actividades', 'Lectura, inglés, ciudadanía y línea de tiempo.'],
  ];
  return h('div', {},
    h('section', { class: 'hero' },
      h('div', {}, h('h1', {}, 'Aprende el Saber 11 probando tú mismo'),
        h('p', { class: 'lede' }, 'Once laboratorios donde cambias un valor y ves por qué cambia el resultado. Cada uno explica la idea, resuelve un ejemplo contigo y te pide predecir antes de mostrarte la respuesta.'),
        h('div', { class: 'cta' }, h('a', { class: 'btn primary', href: '#/diag' }, 'Hacer el diagnóstico gratis (~10 min)'), h('a', { class: 'btn', href: '#/sims' }, 'Ver los laboratorios')),
        h('p', { class: 'fine' }, DISCLAIMER)),
      hero()),
    h('ul', { class: 'method' },
      ...[['01', 'Mira', 'Cada concepto se dibuja con sus cotas y vectores, no se queda en una fórmula.'], ['02', 'Predice', 'Antes de cada experimento eliges qué crees que pasará. Equivocarse enseña más que acertar a ciegas.'], ['03', 'Resuelve', 'El paso a paso usa los números que tienes en pantalla, así que puedes verificar a mano.']]
        .map(([n, t, d]) => h('li', {}, h('h3', {}, h('span', {}, n), t), h('p', {}, d)))),
    h('div', { class: 'sectionhead' }, h('h2', {}, 'Laboratorios'), h('a', { href: '#/sims' }, `Ver las ${sims.length}`)),
    h('div', { class: 'plates', style: 'margin-bottom:46px' }, ...sims.slice(0, 6).map(plate)),
    h('div', { class: 'sectionhead' }, h('h2', {}, 'Después, a practicar')),
    h('div', { class: 'paths' }, ...paths.map(([href, ic, t, d]) => h('a', { class: 'path', href }, icon(ic), h('b', {}, t), h('span', {}, d)))));
}

export function simsList(): HTMLElement {
  const sims = listSims(), groups = ['Todas', ...new Set(sims.map(grupo))];
  let sel = 'Todas';
  const grid = h('div', { class: 'plates' });
  const chips = h('div', { class: 'chips filters', role: 'group', 'aria-label': 'Filtrar por materia' });
  const draw = () => {
    chips.replaceChildren(...groups.map((g) => h('button', { class: 'chip', type: 'button', 'aria-pressed': String(g === sel), onclick: () => { sel = g; draw(); } }, g)));
    grid.replaceChildren(...sims.filter((s) => sel === 'Todas' || grupo(s) === sel).map(plate));
  };
  draw();
  return h('div', {}, head('Laboratorios', 'Elige uno. Todas se pueden usar gratis: tocan los conceptos que más se preguntan en Matemáticas y Ciencias Naturales.'), chips, grid);
}

export function simPage(id: string): HTMLElement {
  const s = getSim(id);
  if (!s) return h('div', {}, head('Laboratorio no encontrado'), h('a', { class: 'btn', href: '#/sims' }, 'Volver a los laboratorios'));
  const sims = listSims(), nx = sims[(sims.findIndex((x) => x.id === s.id) + 1) % sims.length];
  const host = h('div');
  const page = h('div', {},
    h('div', { class: 'pagehead' }, h('a', { class: 'crumb', href: '#/sims' }, '← Todos los laboratorios'), h('h1', {}, s.title),
      s.learn ? h('p', { class: 'lede', html: rich(s.learn.resumen) }) : null,
      h('div', { class: 'meta' }, h('span', { class: 'sheetno' }, `Laboratorio ${sheetNo(s)}`), h('span', { class: 'tag', style: 'margin:0' }, grupo(s)), dots(s.nivel), h('span', {}, `~${s.tiempoMin} min`))),
    host,
    h('div', { class: 'row between', style: 'margin-top:34px' }, h('a', { class: 'btn', href: '#/sims' }, 'Todos los laboratorios'), h('a', { class: 'btn primary', href: `#/sim/${nx.id}` }, `Siguiente: ${nx.title.split(':')[0]}`)));
  touch('sim:' + s.id);
  mountSim(s, host, { sheet: sheetNo(s) });
  return page;
}

export function lessons(id?: string): HTMLElement {
  return gate(() => {
    if (!id) return h('div', {}, head('Lecciones', 'Cada tema se explica desde cinco ángulos: la calle, un dato real, un gráfico, la versión formal y el error típico.'), h('div', { class: 'lessonlist' }, ...LESSONS.map((l) => h('a', { class: 'path', href: `#/leccion/${l.id}` }, icon('book'), h('b', {}, l.titulo), h('span', {}, AREAS[l.area].nombre)))));
    const l = LESSONS.find((x) => x.id === id);
    if (!l) return h('div', {}, head('Lección no encontrada'), h('a', { class: 'btn', href: '#/lecciones' }, 'Volver'));
    const names: Record<string, string> = { cotidiano: 'En la calle', dato_real: 'Con datos reales', grafico_tabla: 'En un gráfico o tabla', formal: 'La versión formal', error_tipico: 'El error típico' };
    touch('les:' + l.id);
    const host = h('div');
    if (l.sim) { const s = getSim(l.sim.id); if (s) mountSim(s, host); }
    return h('div', {}, h('div', { class: 'pagehead' }, h('a', { class: 'crumb', href: '#/lecciones' }, '← Lecciones'), h('h1', {}, l.titulo)),
      ...l.ejemplos.map((e, i) => h('article', { class: 'view-card' }, h('span', { class: 'sheetno' }, `Vista ${i + 1} · ${names[e.angulo] ?? e.angulo}`), h('h3', { style: 'margin-top:10px' }, e.titulo), h('p', {}, e.texto))),
      h('h2', { style: 'margin-top:34px' }, 'Pruébalo tú'), host, h('div', { class: 'box trick' }, h('span', { class: 'hand' }, 'Truco'), h('p', { style: 'margin:6px 0 0' }, l.truco)));
  });
}

/* ───────── Resultados por área ───────── */
export function resultView(): HTMLElement {
  const s = summary();
  const rows = AREA_IDS.map((a) => {
    const v = s.sc[a], A = AREAS[a], lvl = v === undefined ? '—' : NIVELES[a][nivelIndex(a, Math.round(v))].nombre;
    return h('div', { class: 'arow' }, h('b', {}, A.nombre, h('small', {}, v === undefined ? 'sin datos todavía' : lvl)), h('div', { class: 'bar', role: 'img', 'aria-label': `${A.nombre}: ${v ?? 0} de 100` }, h('i', { style: `width:${v ?? 0}%` }), h('u', { style: `left:${A.mu}%`, title: 'Media nacional' })), h('span', { class: 'num' }, v === undefined ? '—' : `${v} ± ${Math.round(s.se[a]!)}`));
  });
  return h('div', {},
    s.global === null ? null : h('div', { class: 'bigscore' }, h('b', {}, String(s.global)), h('span', {}, `de 500 · estimado ± ${Math.round(s.gse)}`)),
    h('div', { class: 'panelgrid' }, h('figure', { class: 'radar' }, h('div', { html: radar(s.sc) }), h('figcaption', {}, 'Relleno: tu puntaje (0–100). Línea punteada: media nacional.')),
      h('div', {}, h('h2', {}, 'Por área'), ...rows, h('p', { class: 'fine', style: 'margin-top:10px' }, 'La marca vertical de cada barra es la media nacional.'))),
    nivelesPanel(s.sc),
    h('p', { class: 'fine' }, DISCLAIMER));
}

/** Diagnóstico adaptativo: gratis. Round-robin por área, ítem de máxima información (top-3 aleatorio). */
export function diagnostic(): HTMLElement {
  const root = h('div'), MAX = 15;
  const resp: Record<string, Resp[]> = {};
  const used = new Set<string>();
  let n = 0;
  function next() {
    root.replaceChildren();
    if (n >= MAX) return finish();
    const area = AREA_IDS[n % AREA_IDS.length];
    const pool = mcs(area).filter((q) => !used.has(q.id)).map((q) => ({ q, item: itemOf(q) }));
    const th = resp[area]?.length ? eap(resp[area]).theta : 0;
    const pick = pickItem(th, pool, rnd) ?? pickItem(0, mcs().filter((q) => !used.has(q.id)).map((q) => ({ q, item: itemOf(q) })), rnd);
    if (!pick) return finish();
    used.add(pick.q.id);
    const sh = h('p', { class: 'sighint', role: 'status' }, 'Elige una respuesta para continuar');
    root.append(head('Diagnóstico'), h('div', { class: 'progline' }, ruler(MAX, n), h('span', {}, `${n + 1} / ${MAX}`)),
      sh, renderQuestion(pick.q, (ok) => { sh.remove(); (resp[pick.q.area] ??= []).push({ item: pick.item, correct: ok }); record(pick.q, ok, 'diag'); syncSoon(); n++; root.append(h('button', { class: 'btn primary next', type: 'button', onclick: next }, n >= MAX ? 'Ver resultado' : 'Siguiente')); }));
  }
  function finish() {
    root.replaceChildren(
      head('Tu diagnóstico', 'Así queda tu radar con lo que respondiste. Entre más preguntas respondas, más precisa será la estimación.'),
      h('div', { class: 'box diag-done-hero', style: 'background:color-mix(in srgb,var(--acc) 12%,var(--panel));border:1.5px solid var(--acc);margin-bottom:1.5rem;text-align:center' },
        h('h2', { style: 'margin:0 0 .4rem;font-size:1.35rem' }, '¡Diagnóstico completado! 🎉'),
        h('p', { style: 'margin:0 0 1rem;color:var(--mut)' }, 'Ya identificamos tus fortalezas y tu ruta de estudio personalizada.'),
        h('div', { class: 'row center', style: 'gap:10px' },
          h('a', { class: 'btn primary big', href: '#/' }, 'Ir a mi ruta de estudio →'),
          h('a', { class: 'btn', href: '#/panel' }, 'Ver mi progreso')
        )
      ),
      resultView(),
      h('div', { class: 'row', style: 'margin-top:1.5rem' },
        h('a', { class: 'btn primary', href: '#/' }, 'Ver mi ruta de estudio'),
        h('a', { class: 'btn', href: '#/panel' }, 'Ver mi progreso')
      )
    );
  }
  root.append(head('Diagnóstico inicial', 'Queremos conocer tu punto de partida. Responde con calma: si no sabes alguna, elige la que te parezca más lógica.'),
    h('div', { class: 'box diag-intro-box' },
      h('div', { style: 'display:flex;align-items:center;gap:12px;margin-bottom:12px' },
        h('span', { style: 'font-size:2rem' }, '🎯'),
        h('div', {},
          h('b', { style: 'font-size:1.15rem' }, '15 preguntas rápidas · 3 por área'),
          h('p', { class: 'fine', style: 'margin:0' }, 'Matemáticas, Lectura, Sociales, Ciencias e Inglés (~10 min)'))
      ),
      h('p', {}, 'Sin presiones: no es una nota para el colegio. Es para saber qué temas ya dominas y cuáles conviene repasar primero en tu ruta.'),
      h('div', { style: 'margin-top:16px' },
        h('button', { class: 'btn primary big', type: 'button', onclick: next }, '¡Comenzar diagnóstico! →')
      ),
      h('p', { class: 'fine', style: 'margin-top:12px' }, 'Con teclado: teclas A, B, C o D para responder y Enter para avanzar.')
    )
  );
  return root;
}

export function practice(): HTMLElement {
  return gate(() => {
    const root = h('div');
    const seen = new Set<string>();
    function next() {
      root.replaceChildren(head('Práctica adaptativa'));
      const due = dueCards().map((id) => QUESTIONS.find((q) => q.id === id)).filter((q): q is Question => !!q);
      let q: Question | undefined = due.find((x) => !seen.has(x.id));
      if (!q) {
        const s = summary();
        const weakest = [...AREA_IDS].sort((a, b) => (s.sc[a] ?? 0) - (s.sc[b] ?? 0))[0];
        const th = (s.sc[weakest] ?? AREAS[weakest].mu) - AREAS[weakest].mu;
        const pool = mcs(weakest).filter((x) => !seen.has(x.id));
        q = pickItem(th / AREAS[weakest].sigma, pool.map((x) => ({ x, item: itemOf(x) })), rnd)?.x ?? QUESTIONS.find((x) => !seen.has(x.id));
      }
      if (!q) { root.append(h('div', { class: 'box' }, h('p', {}, 'Completaste todo el banco disponible. Vuelve mañana para repasar lo que toque.'), h('a', { class: 'btn', href: '#/panel' }, 'Ver mi panel'))); return; }
      seen.add(q.id);
      root.append(h('p', { class: 'fine' }, `Repasos pendientes hoy: ${due.length}`)); const sh = h('p', { class: 'sighint', role: 'status' }, 'Elige una respuesta para continuar'); root.append(sh); root.append(renderQuestion(q, (ok) => { sh.remove(); record(q!, ok, 'prac'); syncSoon(); root.append(h('button', { class: 'btn primary next', type: 'button', onclick: next }, 'Siguiente')); }));
    }
    next();
    return root;
  });
}

export function panel(): HTMLElement {
  const d = load(), s = summary();
  const weakest = [...AREA_IDS].filter((a) => s.sc[a] !== undefined).sort((a, b) => s.sc[a]! - s.sc[b]!)[0];
  const text = `Resumen Saber 11 (estimado, no oficial): ${AREA_IDS.map((a) => `${AREAS[a].nombre} ${s.sc[a] ?? '—'}`).join(', ')}. Racha: ${d.streak.count} días.`;
  const left = h('p', { class: 'mono', style: 'color:var(--acc)' });
  const paintLeft = () => { left.textContent = d.examDay ? (d.examDay >= day() ? `Faltan ${d.examDay - day()} días para el examen.` : 'La fecha ya pasó.') : ''; };
  paintLeft();
  return h('div', {}, head('Mi progreso', 'Aquí ves cómo vas: tu puntaje estimado, qué áreas te faltan y qué repasar. Vuelve cuando termines una práctica.'),
    d.answers.length === 0 ? h('div', { class: 'box trick' }, h('b', {}, 'Aún no tienes datos'), h('p', { style: 'margin:.4rem 0 .8rem' }, 'Haz el diagnóstico (unos 20 minutos) y aquí verás tu puntaje estimado, tus áreas más fuertes y qué repasar.'), h('a', { class: 'btn primary', href: '#/diag' }, 'Hacer el diagnóstico')) : h('div', { class: 'stats' }, h('div', { class: 'stat' }, h('b', {}, String(d.streak.count)), h('span', {}, `días de racha · ${d.streak.freezes} congeladores`)), h('div', { class: 'stat' }, h('b', {}, String(d.answers.length)), h('span', {}, 'preguntas respondidas')), h('div', { class: 'stat' }, h('b', {}, String(dueCards().length)), h('span', {}, 'repasos para hoy'))),
    ...(d.answers.length === 0 ? [] : [resultView()]),
    weakest ? h('div', { class: 'box trick' }, h('span', { class: 'hand' }, 'Recomendación'), h('p', { style: 'margin:6px 0 0' }, `Practica ${AREAS[weakest].nombre}: es tu área más baja ahora.`)) : null,
    h('div', { class: 'box' }, h('label', { for: 'exam' }, h('b', {}, 'Fecha del examen (opcional)')), h('p', { class: 'fine', style: 'margin:.2rem 0' }, 'Con ella, la pantalla Hoy te cuenta cuántos días faltan.'), h('div', { style: 'max-width:260px;margin:8px 0' }, h('input', { id: 'exam', type: 'date', value: d.examDay ? new Date(d.examDay * 86400000).toISOString().slice(0, 10) : '', onchange: (e: Event) => { const v = (e.target as HTMLInputElement).value; d.examDay = v ? Math.floor(Date.parse(v) / 86400000) : undefined; save(); paintLeft(); } })), left),
    h('div', { class: 'box' }, h('h2', { style: 'font-size:1.3rem' }, 'Para tu profe o tu familia'), h('p', {}, 'Copia este resumen y envíalo por WhatsApp o correo para que te acompañen:'), h('textarea', { readonly: true, rows: 3, class: 'share', 'aria-label': 'Resumen para compartir' }, text), h('button', { class: 'btn', type: 'button', onclick: () => navigator.clipboard?.writeText(text) }, 'Copiar resumen')));
}

export async function payPage(): Promise<HTMLElement> {
  const root = h('div');
  const consent = h('input', { type: 'checkbox', id: 'cons' }) as HTMLInputElement;
  const minor = h('input', { type: 'checkbox', id: 'minor' }) as HTMLInputElement;
  const msg = h('p', { role: 'status', class: 'bad' });
  root.append(head('Plataforma personalizada por 12 meses', 'Todo el contenido es gratis para siempre. Premium solo cambia los colores de la plataforma.'),
    h('div', { class: 'box' }, h('div', { class: 'price' }, 'COP 29.900'),
      h('ul', { class: 'include' }, ...['Seis paletas de color para toda la plataforma, en modo claro y oscuro', 'Las preguntas, lecciones, laboratorios y simulacros siguen siendo gratis', 'Tu paleta se guarda en este dispositivo'].map((t) => h('li', {}, t))),
      h('label', { class: 'check', for: 'minor' }, minor, h('span', {}, 'Soy menor de edad y mi acudiente autoriza este pago y el tratamiento de mis datos.')),
      h('label', { class: 'check', for: 'cons' }, consent, h('span', {}, 'Acepto la política de tratamiento de datos y los términos. Tengo derecho de retracto de 5 días hábiles.')),
      h('button', { class: 'btn primary', type: 'button', onclick: async () => {
        if (!consent.checked) { msg.textContent = 'Debes aceptar los términos para continuar.'; return; }
        try {
          const r = await fetch('/api/pay/checkout', { method: 'POST', headers: { 'content-type': 'application/json' }, body: JSON.stringify({ uid: load().uid, minor: minor.checked, guardianConsent: minor.checked }) });
          const c = await r.json();
          if (!r.ok) { msg.textContent = c.error ?? 'No se pudo iniciar el pago.'; return; }
          const u = new URL('https://checkout.wompi.co/p/');
          u.search = new URLSearchParams({ 'public-key': c.publicKey, currency: c.currency, 'amount-in-cents': String(c.amountInCents), reference: c.reference, 'signature:integrity': c.signature, 'redirect-url': c.redirectUrl }).toString();
          location.href = u.toString();
        } catch { msg.textContent = 'No se pudo iniciar el pago (¿sin conexión?).'; }
      } }, 'Pagar con Wompi'), msg),
    h('p', { class: 'fine' }, 'Pago seguro con Wompi. ' + DISCLAIMER));
  return root;
}
export async function payResult(): Promise<HTMLElement> {
  const id = query().get('id') ?? new URLSearchParams(location.search).get('id');
  const out = h('div', {}, head('Resultado del pago'));
  if (!id) { out.append(h('p', {}, 'No encontramos la transacción.')); return out; }
  try {
    const r = await (await fetch(`/api/pay/status?id=${encodeURIComponent(id)}`)).json();
    if (r.status === 'APPROVED') { load().paid = true; save(); out.append(h('div', { class: 'box' }, h('p', { class: 'ok' }, 'Pago aprobado. Ya puedes elegir tus paletas por 12 meses.'), h('a', { class: 'btn primary', href: '#/practica' }, 'Empezar a practicar'))); }
    else out.append(h('p', {}, `Estado: ${r.status ?? 'desconocido'}. Si ya pagaste, se actualizará en unos minutos.`));
  } catch { out.append(h('p', {}, 'No pudimos verificar el pago ahora. Intenta de nuevo en un momento.')); }
  return out;
}
export { go };
