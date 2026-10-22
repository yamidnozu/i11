import { h, fmt } from '../ui/dom';
import { rich, tex } from '../ui/tex';
import { ico } from '../ui/icons';
import { drawSeries, COLORS } from '../render/plot';
import { defaults, runHeadless } from './thumb';
import type { Challenge, Experiment, M, ParamDef, ParamValue, Params, Preset, SimConfig } from './types';

export interface MountOpts {
  preset?: Params;
  challengeId?: string;
  onResult?: (ok: boolean, m: M) => void;
  sheet?: string;
  tab?: string;
  autoRun?: boolean;
}

const FIXED_DT = 1 / 120;

export function evaluateChallenge(ch: Challenge, m: M): boolean {
  return ch.checks.every((c) => Math.abs((m[c.measure] ?? NaN) - c.target) <= c.tol);
}

const lsGet = (k: string) => { try { return localStorage.getItem(k); } catch { return null; } };
const lsSet = (k: string, v: string) => { try { localStorage.setItem(k, v); } catch { /* sin almacenamiento */ } };
const cell = (k: string, v: string) => h('div', { class: 'cell' }, h('span', { class: 'k' }, k), h('span', { class: 'v' }, v));

/** Laboratorio interactivo: escenario, controles, explicación, experimentos con predicción y resolución en vivo. */
export function mountSim(cfg: SimConfig, root: HTMLElement, opts: MountOpts = {}) {
  root.replaceChildren();
  const dynamic = cfg.mode === 'dynamic';
  const params: Params = { ...defaults(cfg), ...(opts.preset ?? {}) };
  let challenge: Challenge | undefined = cfg.challenges.find((c) => c.id === opts.challengeId);
  if (challenge?.fixed) Object.assign(params, challenge.fixed);

  let state = cfg.logic.init(params);
  let traj: any[] = [state];
  let finished = !dynamic;
  let running = false, raf = 0, last = 0, acc = 0, stepCount = 0, frame = 0, speed = 1;
  let pointer: { x: number; y: number } | null = null;
  let autoT: ReturnType<typeof setTimeout> | undefined;
  let alive = true;
  let measures: M = {};
  let tab = opts.tab ?? 'controles';
  let activePreset: Preset | undefined;

  const dpr = Math.min(window.devicePixelRatio || 1, 2);
  const { width: W, height: H } = cfg.render;
  const canvas = h('canvas', { width: Math.round(W * dpr), height: Math.round(H * dpr), class: 'stage-canvas', role: 'img', 'aria-label': cfg.title, style: `aspect-ratio:${W}/${H}` });
  const ctx = canvas.getContext('2d')!;
  const status = h('div', { class: 'sr-only', 'aria-live': 'polite' });

  /* ---------- escenario ---------- */
  const btnPlay = h('button', { class: 'btn primary sm', type: 'button', onclick: () => (running ? pause() : run()) });
  const btnReset = h('button', { class: 'btn sm', type: 'button', onclick: () => resetSim(false), html: `${ico('reset', 16)}<span>Reiniciar</span>` });
  const segBtns = [0.5, 1, 2].map((s) => h('button', { class: 'seg', type: 'button', 'aria-pressed': String(s === 1), onclick: () => { speed = s; segBtns.forEach((b, i) => b.setAttribute('aria-pressed', String([0.5, 1, 2][i] === s))); } }, `${s}×`));
  const hud = dynamic ? h('div', { class: 'hud' }, btnPlay, btnReset, h('div', { class: 'segs', role: 'group', 'aria-label': 'Velocidad' }, ...segBtns)) : null;
  const cajetin = h('figcaption', { class: 'cajetin' }, cell('Hoja', opts.sheet ?? '—'), cell('Plano', cfg.title), cell('Nivel', `${cfg.nivel} de 4`), cell('Tiempo', `~${cfg.tiempoMin} min`));
  const readoutsEl = h('div', { class: 'readouts', role: 'group', 'aria-label': 'Medidas' });
  const insightP = h('p');
  const insightEl = h('div', { class: 'insight' }, h('span', { class: 'hand' }, 'Observa'), insightP);
  const graphBox = h('div', { class: 'graphs' });
  const graphCanvases = (cfg.graphs ?? []).map((g, i) => {
    const c = h('canvas', { width: 440, height: 240, role: 'img', 'aria-label': g.title });
    graphBox.append(h('figure', { class: 'graph' }, c));
    return { g, c, color: COLORS[i % COLORS.length] };
  });
  const tableBox = h('details', { class: 'datatable' }, h('summary', {}, 'Ver tabla de datos'));

  /* ---------- panel lateral ---------- */
  const tabDefs = [
    { id: 'controles', t: 'Controles', ok: true },
    { id: 'idea', t: 'Idea clave', ok: !!cfg.learn },
    { id: 'exp', t: 'Experimentos', ok: !!cfg.experiments?.length },
    { id: 'paso', t: 'Paso a paso', ok: !!cfg.solution },
    { id: 'retos', t: 'Retos', ok: cfg.challenges.length > 0 },
  ].filter((t) => t.ok);
  if (!tabDefs.some((t) => t.id === tab)) tab = 'controles';
  const uid = cfg.id.replace(/\./g, '-');
  const tabsEl = h('div', { class: 'tabs', role: 'tablist', 'aria-label': 'Panel del laboratorio' });
  const panes: Record<string, HTMLElement> = {};
  const tabBtns: Record<string, HTMLElement> = {};
  tabDefs.forEach((t, i) => {
    panes[t.id] = h('div', { class: 'pane', role: 'tabpanel', id: `pane-${uid}-${t.id}`, 'aria-labelledby': `tab-${uid}-${t.id}`, hidden: true });
    tabBtns[t.id] = h('button', {
      class: 'tab', type: 'button', role: 'tab', id: `tab-${uid}-${t.id}`, 'aria-controls': `pane-${uid}-${t.id}`, 'aria-selected': 'false',
      onclick: () => selectTab(t.id),
      onkeydown: (e: KeyboardEvent) => {
        const d = e.key === 'ArrowRight' ? 1 : e.key === 'ArrowLeft' ? -1 : 0;
        if (d) { const n = tabDefs[(i + d + tabDefs.length) % tabDefs.length].id; selectTab(n); tabBtns[n].focus(); }
      },
    }, t.t);
    tabsEl.append(tabBtns[t.id]);
  });

  function selectTab(id: string) {
    tab = id;
    for (const t of tabDefs) { panes[t.id].hidden = t.id !== id; tabBtns[t.id].setAttribute('aria-selected', String(t.id === id)); tabBtns[t.id].tabIndex = t.id === id ? 0 : -1; }
    if (id === 'paso') renderSolution();
    if (id === 'exp') renderExp();
    if (id === 'retos') renderChallenges();
  }

  /* ---------- controles ---------- */
  const presetBox = h('div', { class: 'presets' });
  const ctrlBox = h('div', { class: 'controls' });
  panes.controles.append(presetBox, ctrlBox, h('button', { class: 'btn sm ghost', type: 'button', onclick: () => { Object.assign(params, defaults(cfg)); challenge = undefined; activePreset = undefined; buildControls(); drawPresets(); onParams(); } }, 'Restablecer valores'));

  const set = (k: string, v: ParamValue) => { params[k] = v; onParams(); };
  const valText = (d: ParamDef, v: ParamValue) => `${typeof v === 'number' ? +v.toFixed(4) : v}${d.unit ? ' ' + d.unit : ''}`;

  function control(d: ParamDef): HTMLElement {
    const locked = !!challenge?.fixed && d.key in challenge.fixed;
    const id = `p-${uid}-${d.key}`;
    const hint = d.hint ? h('p', { class: 'hint' }, d.hint) : null;
    if (d.type === 'custom') return h('div', { class: 'ctl' }, d.build!({ params, set }));
    if (d.type === 'slider') {
      const min = d.min!, max = d.max!, step = d.step!;
      const out = h('output', { class: 'val', for: id }, valText(d, params[d.key]));
      const input = h('input', { id, type: 'range', min: String(min), max: String(max), step: String(step), value: String(params[d.key]), disabled: locked }) as HTMLInputElement;
      const paint = () => input.style.setProperty('--pct', `${((+input.value - min) / (max - min)) * 100}%`);
      paint();
      const apply = (v: number) => { const nv = Math.min(max, Math.max(min, +v.toFixed(6))); input.value = String(nv); paint(); out.textContent = valText(d, nv); set(d.key, nv); };
      input.addEventListener('input', () => apply(+input.value));
      const stepBtn = (dir: number, sym: string, name: string) => h('button', { class: 'btn sq', type: 'button', 'aria-label': `${name} ${d.label}`, disabled: locked, onclick: () => apply(+input.value + dir * step) }, sym);
      return h('div', { class: 'ctl' }, h('div', { class: 'ctl-top' }, h('label', { for: id }, d.label), out), h('div', { class: 'row slider' }, stepBtn(-1, '−', 'Disminuir'), input, stepBtn(1, '+', 'Aumentar')), hint);
    }
    if (d.type === 'select') {
      const sel = h('select', { id, disabled: locked, onchange: (e: Event) => set(d.key, +(e.target as HTMLSelectElement).value) }, d.options!.map((o) => h('option', { value: String(o.v), selected: o.v === params[d.key] }, o.l)));
      return h('div', { class: 'ctl' }, h('div', { class: 'ctl-top' }, h('label', { for: id }, d.label)), sel, hint);
    }
    if (d.type === 'toggle') {
      return h('div', { class: 'ctl' }, h('label', { class: 'switch' }, h('input', { id, type: 'checkbox', checked: !!params[d.key], disabled: locked, onchange: (e: Event) => set(d.key, (e.target as HTMLInputElement).checked) }), h('span', { class: 'track' }), h('span', { class: 'lbl' }, d.label)), hint);
    }
    const hasCustom = cfg.params.some((q) => q.type === 'custom');
    return h('div', { class: 'ctl' }, h('div', { class: 'ctl-top' }, h('label', { for: id }, d.label)), h('input', {
      id, type: 'text', value: String(params[d.key]), disabled: locked, spellcheck: 'false', autocomplete: 'off',
      oninput: (e: Event) => set(d.key, (e.target as HTMLInputElement).value),
      onchange: () => { if (hasCustom) buildControls(); },
    }), hint);
  }
  function buildControls() { ctrlBox.replaceChildren(...cfg.params.map(control)); }

  function drawPresets() {
    presetBox.replaceChildren();
    if (!cfg.presets?.length) return;
    presetBox.append(
      h('p', { class: 'sub' }, 'Casos reales y situaciones típicas'),
      h('div', { class: 'chips' }, ...cfg.presets.map((pr) => h('button', { class: 'chip', type: 'button', 'aria-pressed': String(activePreset?.id === pr.id), onclick: () => applyPreset(pr) }, pr.label))),
      ...(activePreset ? [h('p', { class: 'preset-desc', html: rich(activePreset.desc) })] : []),
    );
  }
  function applyPreset(pr: Preset) {
    Object.assign(params, defaults(cfg), pr.params);
    challenge = undefined; activePreset = pr;
    buildControls(); drawPresets(); onParams();
  }

  /* ---------- lectura de resultados ---------- */
  function computeMeasures() { try { measures = cfg.logic.measures(traj, params); } catch { measures = {}; } }
  function readoutKeys() { return cfg.readouts ?? Object.keys(measures).slice(0, 6); }
  function updateReadouts() {
    readoutsEl.replaceChildren(...readoutKeys().map((k) => h('div', { class: 'ro' }, h('span', { class: 'k' }, cfg.measureLabels?.[k] ?? k), h('span', { class: 'v' }, fmt(measures[k] ?? NaN)))));
  }
  function updateInsight() {
    const t = cfg.insight ? cfg.insight(params, measures) : '';
    insightEl.hidden = !t;
    insightP.innerHTML = rich(t);
  }
  function renderTable() {
    let t: { cols: string[]; rows: (number | string)[][] };
    if (cfg.table) t = cfg.table(params, traj);
    else if (cfg.graphs?.length) {
      const keys = [...new Set(cfg.graphs.flatMap((g) => [g.x, g.y]))];
      const samples = traj.map((s) => cfg.logic.sample?.(s) ?? {});
      const n = Math.max(1, Math.floor(samples.length / 12));
      t = { cols: keys, rows: samples.filter((_, i) => i % n === 0).slice(0, 14).map((r) => keys.map((k) => r[k] ?? NaN)) };
    } else t = { cols: ['Medida', 'Valor'], rows: Object.entries(measures).map(([k, v]) => [cfg.measureLabels?.[k] ?? k, v]) };
    tableBox.replaceChildren(h('summary', {}, 'Ver tabla de datos'), h('table', {}, h('thead', {}, h('tr', {}, t.cols.map((c) => h('th', { scope: 'col' }, c)))), h('tbody', {}, t.rows.map((r) => h('tr', {}, r.map((v) => h('td', {}, typeof v === 'number' ? fmt(v) : v)))))));
  }

  /* ---------- dibujo ---------- */
  function draw() {
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    cfg.render.view({ ctx, w: W, h: H, state, traj, p: params, measures, time: performance.now() / 1000, pointer });
  }
  function drawGraphs() {
    if (!graphCanvases.length || !cfg.logic.sample) return;
    const rows = traj.map((s) => cfg.logic.sample!(s));
    for (const { g, c, color } of graphCanvases) drawSeries(c, rows, g.x, g.y, g.title, color);
  }
  function refreshAll() {
    computeMeasures(); updateReadouts(); updateInsight(); renderTable();
    if (tab === 'paso') renderSolution();
    draw(); drawGraphs();
    if (finished && cfg.describe) status.textContent = cfg.describe(measures, params);
  }

  /* ---------- ejecución ---------- */
  const setPlayLabel = () => { btnPlay.innerHTML = running ? `${ico('pause', 16)}<span>Pausar</span>` : `${ico('play', 16)}<span>${finished && traj.length > 1 ? 'Repetir' : 'Simular'}</span>`; };
  function stop() { running = false; cancelAnimationFrame(raf); setPlayLabel(); }
  function pause() { stop(); }
  function resetSim(auto: boolean) {
    stop(); clearTimeout(autoT);
    state = cfg.logic.init(params); traj = [state]; finished = !dynamic; acc = 0; stepCount = 0;
    refreshAll(); setPlayLabel();
    if (auto && dynamic) scheduleRun();
  }
  function onParams() { resetSim(false); if (dynamic) scheduleRun(); }
  function scheduleRun() { clearTimeout(autoT); autoT = setTimeout(() => { if (alive && canvas.isConnected) run(); }, 180); }
  function tick(ts: number) {
    if (!running) return;
    if (!canvas.isConnected) { stop(); return; }
    acc += Math.min((ts - last) / 1000, 0.1) * speed; last = ts;
    let n = 0;
    while (acc >= FIXED_DT && n < 16 && !finished) {
      state = cfg.logic.step!(state, params, FIXED_DT);
      acc -= FIXED_DT; n++; stepCount++;
      if (stepCount % 2 === 0) traj.push(state);
      if (cfg.logic.done!(state, params)) { finished = true; traj.push(state); }
    }
    frame++;
    if (finished) { stop(); refreshAll(); renderExpIfOpen(); return; }
    if (frame % 5 === 0) { computeMeasures(); updateReadouts(); updateInsight(); drawGraphs(); }
    draw();
    raf = requestAnimationFrame(tick);
  }
  function run() {
    if (!dynamic) return;
    if (finished) { state = cfg.logic.init(params); traj = [state]; finished = false; acc = 0; stepCount = 0; }
    running = true; last = performance.now(); setPlayLabel();
    raf = requestAnimationFrame(tick);
  }

  canvas.addEventListener('pointermove', (e) => {
    const r = canvas.getBoundingClientRect();
    pointer = { x: ((e.clientX - r.left) * W) / r.width, y: ((e.clientY - r.top) * H) / r.height };
    if (!running) draw();
  });
  canvas.addEventListener('pointerleave', () => { pointer = null; if (!running) draw(); });

  /* ---------- idea clave ---------- */
  function buildIdea() {
    const L = cfg.learn;
    if (!L) return;
    panes.idea.append(
      h('section', {}, h('h3', {}, 'Al terminar podrás'), h('ul', { class: 'goals' }, L.objetivos.map((o) => h('li', { html: rich(o) })))),
      h('section', {}, h('h3', {}, 'La idea'), ...L.idea.map((p) => h('p', { html: rich(p) })),
        L.analogia ? h('aside', { class: 'margin-note' }, h('span', { class: 'hand' }, 'En la vida diaria'), h('p', { html: rich(L.analogia) })) : null),
      h('section', {}, h('h3', {}, 'Fórmulas'), ...L.formulas.map((f) => h('figure', { class: 'formula' },
        h('div', { class: 'big', html: tex(f.tex) }), h('figcaption', {}, f.nombre),
        h('dl', { class: 'vars' }, ...f.vars.flatMap(([s, d]) => [h('dt', { html: tex(s) }), h('dd', { html: rich(d) })]))))),
      h('section', {}, h('h3', {}, 'Ejemplos resueltos'), ...L.ejemplos.map((e) => h('article', { class: 'worked' }, h('h4', {}, e.titulo), h('p', { html: rich(e.texto) }), h('ol', {}, e.pasos.map((s) => h('li', { html: rich(s) })))))),
      h('section', {}, h('h3', {}, 'Ideas que suelen fallar'), h('ul', { class: 'myths' }, L.errores.map((e) => h('li', {}, h('p', { class: 'mito' }, h('span', { html: ico('cross', 16) }), h('span', { html: rich(e.mito) })), h('p', { class: 'real' }, h('span', { html: ico('check', 16) }), h('span', { html: rich(e.realidad) })))))),
      h('aside', { class: 'tip' }, h('span', { class: 'hand' }, 'Para el examen'), h('p', { html: rich(L.saber11) })),
    );
  }

  /* ---------- paso a paso ---------- */
  function renderSolution() {
    if (!cfg.solution) return;
    const steps = cfg.solution(params, measures);
    const pane = panes.paso;
    pane.replaceChildren(
      h('p', { class: 'lead' }, 'Resolución con los valores que tienes ahora en los controles. Cambia un control y los números se recalculan.'),
      h('ol', { class: 'steps' }, steps.map((s) => h('li', {}, h('h4', {}, s.t), h('div', { class: 'eq', html: tex(s.tex) }), s.nota ? h('p', { class: 'nota', html: rich(s.nota) }) : null))),
    );
    const rows = finished && cfg.compare ? cfg.compare(params, measures) : [];
    if (rows.length) {
      pane.append(h('section', { class: 'cmp' }, h('h3', {}, 'Teoría frente a simulación'), h('table', {}, h('thead', {}, h('tr', {}, ['Medida', 'Teoría', 'Simulación'].map((c) => h('th', { scope: 'col' }, c)))),
        h('tbody', {}, rows.map((r) => { const ok = Math.abs(r.teoria - r.sim) <= Math.max(0.01 * Math.abs(r.teoria), 1e-6); return h('tr', { class: ok ? 'ok' : '' }, h('td', {}, r.label), h('td', {}, fmt(r.teoria)), h('td', {}, fmt(r.sim), ok ? h('span', { class: 'tick', html: ico('check', 14) }) : null)); }))),
        rows.some((r) => r.nota) ? h('p', { class: 'nota' }, rows.find((r) => r.nota)!.nota) : null));
    } else if (dynamic && cfg.compare) pane.append(h('p', { class: 'nota' }, 'Cuando la simulación termine, aquí verás la comparación con la teoría.'));
  }

  /* ---------- experimentos ---------- */
  const doneKey = `saber11.exp.${cfg.id}`;
  let doneSet = new Set<string>();
  try { doneSet = new Set(JSON.parse(lsGet(doneKey) ?? '[]')); } catch { /* ignorar */ }
  let activeExp: string | undefined;
  const answers: Record<string, number> = {};
  const cache = new Map<string, { b: M; a?: M }>();
  const expParams = (e: Experiment, withChange: boolean): Params => ({ ...defaults(cfg), ...e.setup, ...(withChange ? e.cambio ?? {} : {}) });
  function applyExp(e: Experiment, withChange: boolean) { Object.assign(params, expParams(e, withChange)); challenge = undefined; buildControls(); onParams(); }
  function renderExpIfOpen() { if (tab === 'exp') renderExp(); }

  function compareTable(e: Experiment): HTMLElement {
    let c = cache.get(e.id);
    if (!c) { c = { b: runHeadless(cfg, expParams(e, false)).measures, a: e.cambio ? runHeadless(cfg, expParams(e, true)).measures : undefined }; cache.set(e.id, c); }
    const keys = readoutKeys().length ? (cfg.readouts ?? Object.keys(c.b)).filter((k) => Number.isFinite(c!.b[k])).slice(0, 6) : [];
    const head = c.a ? ['Medida', 'Antes', 'Después', 'Cambio'] : ['Medida', 'Resultado'];
    return h('table', { class: 'ba' }, h('thead', {}, h('tr', {}, head.map((t) => h('th', { scope: 'col' }, t)))), h('tbody', {}, keys.map((k) => {
      const b = c!.b[k], a = c!.a?.[k];
      return h('tr', {}, h('td', {}, cfg.measureLabels?.[k] ?? k), h('td', {}, fmt(b)),
        ...(a === undefined ? [] : [h('td', {}, fmt(a)), h('td', {}, Number.isFinite(a) && Math.abs(b) > 1e-9 ? `×${fmt(a / b)}` : '—')]));
    })));
  }

  function renderExp() {
    const pane = panes.exp;
    if (!pane) return;
    pane.replaceChildren(h('p', { class: 'lead' }, 'Haz una predicción, compárala con el resultado y lee por qué ocurre. Cada experimento prepara el montaje por ti.'));
    (cfg.experiments ?? []).forEach((e, i) => {
      const open = activeExp === e.id, ans = answers[e.id], isDone = doneSet.has(e.id);
      const head = h('button', {
        class: 'exp-head', type: 'button', 'aria-expanded': String(open),
        onclick: () => { activeExp = open ? undefined : e.id; if (!open) { delete answers[e.id]; applyExp(e, false); } renderExp(); },
      }, h('span', { class: 'n' }, String(i + 1)), h('span', { class: 't' }, e.titulo), isDone ? h('span', { class: 'done', html: `${ico('check', 16)}<span class="sr-only">Hecho</span>` }) : null);
      const card = h('article', { class: 'exp' + (open ? ' open' : '') + (isDone ? ' ok' : '') }, head);
      if (open) {
        const body = h('div', { class: 'exp-body' }, h('p', { class: 'q', html: rich(e.pregunta) }));
        body.append(h('div', { class: 'opts', role: 'radiogroup', 'aria-label': 'Opciones' }, e.opciones.map((o, k) =>
          h('button', { class: 'opt' + (ans !== undefined ? (k === e.correcta ? ' right' : k === ans ? ' wrong' : '') : ''), type: 'button', disabled: ans !== undefined, onclick: () => answerExp(e, k) }, h('b', {}, 'ABCD'[k]), h('span', { html: rich(o) })))));
        if (ans !== undefined) {
          body.append(h('p', { class: ans === e.correcta ? 'verdict ok' : 'verdict bad', role: 'status' }, ans === e.correcta ? 'Correcto.' : 'No es esa opción.'), h('p', { class: 'expl', html: rich(e.explicacion) }), compareTable(e),
            h('button', { class: 'btn sm', type: 'button', onclick: () => { delete answers[e.id]; applyExp(e, false); renderExp(); } }, 'Repetir experimento'));
        }
        card.append(body);
      }
      pane.append(card);
    });
  }
  function answerExp(e: Experiment, k: number) {
    answers[e.id] = k;
    if (k === e.correcta) { doneSet.add(e.id); lsSet(doneKey, JSON.stringify([...doneSet])); }
    if (e.cambio) applyExp(e, true);
    renderExp();
  }

  /* ---------- retos ---------- */
  function renderChallenges() {
    const pane = panes.retos;
    if (!pane) return;
    const sel = h('select', {
      id: `ch-${uid}`, 'aria-label': 'Elegir reto',
      onchange: (e: Event) => {
        const v = (e.target as HTMLSelectElement).value;
        challenge = cfg.challenges.find((c) => c.id === v);
        Object.assign(params, defaults(cfg)); if (challenge?.fixed) Object.assign(params, challenge.fixed);
        buildControls(); onParams(); renderChallenges();
      },
    }, h('option', { value: '' }, 'Sin reto (modo libre)'), cfg.challenges.map((c, i) => h('option', { value: c.id, selected: c.id === challenge?.id }, `Reto ${i + 1}`)));
    pane.replaceChildren(h('p', { class: 'lead' }, 'Cumple una meta numérica moviendo los controles. Algunos valores quedan fijos para que el reto tenga solución.'), sel);
    if (!challenge) return;
    const ch = challenge;
    const msg = h('p', { class: 'chmsg', role: 'status' });
    const hintEl = h('p', { class: 'nota' });
    pane.append(h('p', { class: 'prompt', html: rich(ch.prompt) }),
      h('div', { class: 'row' },
        h('button', { class: 'btn primary', type: 'button', onclick: () => {
          if (dynamic && !finished) { msg.textContent = 'Espera a que termine la simulación (o pulsa Simular) y vuelve a comprobar.'; return; }
          computeMeasures();
          const ok = evaluateChallenge(ch, measures);
          const detail = ch.checks.map((c) => `${cfg.measureLabels?.[c.measure] ?? c.measure}: ${fmt(measures[c.measure] ?? NaN)} (meta ${c.target} ± ${c.tol})`).join(' · ');
          msg.textContent = (ok ? 'Reto cumplido. ' : 'Todavía no. ') + detail;
          msg.className = 'chmsg ' + (ok ? 'ok' : 'bad');
          opts.onResult?.(ok, measures);
        } }, 'Comprobar reto'),
        ch.hint ? h('button', { class: 'btn', type: 'button', onclick: () => { hintEl.textContent = ch.hint!; } }, 'Ver pista') : null),
      msg, hintEl);
  }

  /* ---------- montaje ---------- */
  root.append(h('div', { class: 'lab' },
    h('section', { class: 'lab-stage' }, h('figure', { class: 'stage' }, canvas, hud, cajetin), readoutsEl, insightEl, status, graphBox, tableBox),
    h('aside', { class: 'lab-side' }, tabsEl, ...Object.values(panes)),
  ));
  buildControls(); drawPresets(); buildIdea();
  selectTab(tab);
  refreshAll(); setPlayLabel();
  document.fonts?.ready.then(() => { if (alive) { draw(); drawGraphs(); } });
  if (cfg.ambient) {
    let seen = false;
    const loop = () => { if (!alive) return; if (canvas.isConnected) seen = true; else if (seen) { alive = false; return; } if (!running) draw(); requestAnimationFrame(loop); };
    requestAnimationFrame(loop);
  }
  if (dynamic && opts.autoRun !== false) autoT = setTimeout(() => { if (alive && canvas.isConnected) run(); }, 700);

  return { destroy: () => { alive = false; stop(); clearTimeout(autoT); }, getMeasures: () => ({ ...measures }), params };
}
