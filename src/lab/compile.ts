import type { SimConfig, Params, Challenge, M, Extra } from '../core/types';
import { rk4, bisect } from '../math/rk4';
import { ev, evNum, tpl, type Scope } from './expr';
import { drawScene } from './scene';
import type { LabJSON } from './schema';

/** Convierte un laboratorio escrito en JSON en un SimConfig que el motor ya sabe ejecutar. */
export function compileLab(j: LabJSON): SimConfig {
  const f = j.fisica, modo = f.integracion ?? (f.ecuaciones ? 'rk4' : 'formula');
  const base = (p: Params): Scope => {
    const sc: Scope = { ...(j.constantes ?? {}) };
    for (const [k, v] of Object.entries(p)) sc[k] = typeof v === 'boolean' ? v : +v;
    for (const [k, e] of Object.entries(j.derivadas ?? {})) sc[k] = ev(e, sc);
    return sc;
  };
  const keys = Object.keys(f.ecuaciones ?? {});
  const evalState = (sc: Scope, src: Record<string, string>, t: number) => { const o: Record<string, any> = { t }; const s2: Scope = { ...sc, t }; for (const [k, e] of Object.entries(src)) { o[k] = evNum(e, s2); s2[k] = o[k]; } return o; };
  const dur = (sc: Scope) => (f.duracion ? evNum(f.duracion, sc) : Infinity);

  const logic: SimConfig['logic'] = {
    init: (p) => {
      const sc = base(p);
      if (modo === 'formula') return { ...evalState(sc, f.estadoT!, 0), done: false };
      const o: Record<string, any> = { t: 0, done: false }; const s2 = { ...sc };
      for (const [k, e] of Object.entries(f.estado ?? {})) { o[k] = evNum(e, s2); s2[k] = o[k]; }
      return o;
    },
    step: (s: any, p, dt) => {
      if (s.done) return s;
      const sc = base(p), T = dur(sc);
      if (modo === 'formula') { const t = Math.min(s.t + dt, T); return { ...evalState(sc, f.estadoT!, t), done: t >= T - 1e-12 }; }
      const fn = (t: number, y: number[]) => { const s2: Scope = { ...sc, t }; keys.forEach((k, i) => { s2[k] = y[i]; }); return keys.map((k) => evNum(f.ecuaciones![k], s2)); };
      const y0 = keys.map((k) => s[k]), adv = (hh: number) => rk4(fn, s.t, y0, hh);
      const mk = (y: number[], hh: number, done: boolean) => { const o: Record<string, any> = { ...s, t: s.t + hh, done }; keys.forEach((k, i) => { o[k] = y[i]; }); return o; };
      let hh = dt, n = adv(hh);
      const hitT = s.t + hh >= T - 1e-12;
      if (hitT) { hh = T - s.t; return mk(adv(hh), hh, true); }
      if (f.evento) {
        const at = (y: number[], t: number) => { const s2: Scope = { ...sc, t }; keys.forEach((k, i) => { s2[k] = y[i]; }); return !!ev(f.evento!, s2); };
        if (at(n, s.t + hh)) {
          const ya = at(y0, s.t);
          hh = ya ? 0 : bisect((q) => (at(adv(q), s.t + q) ? -1 : 1), 0, dt);
          n = hh === 0 ? [...y0] : adv(hh);
          const o = mk(n, hh, true); for (const [k, v] of Object.entries(f.ajustar ?? {})) o[k] = v; return o;
        }
      }
      return mk(n, hh, false);
    },
    done: (s: any) => !!s.done,
    sample: (s: any) => { const o: Record<string, number> = {}; for (const k of f.muestras ?? ['t', ...Object.keys(f.estado ?? f.estadoT ?? {})]) o[k] = +s[k]; return o; },
    measures: (traj: any[], p) => {
      const sc: Scope = { ...base(p), traj, last: traj[traj.length - 1], first: traj[0] }; const m: M = {};
      for (const [k, e] of Object.entries(f.medidas)) m[k] = evNum(e, sc); return m;
    },
  };
  if (j.modo === 'estatico') { delete (logic as any).step; delete (logic as any).done; }

  const retos: Challenge[] = j.retos.map((r) => ({ id: r.id, prompt: r.texto, fixed: r.fijos, checks: r.criterios.map((c) => ({ measure: c.medida, target: c.objetivo, tol: c.tol })), hint: r.pista }));
  const ctxOf = (p: Params, m: M): Scope => ({ ...base(p), m });
  const extra: Partial<Extra> = {
    learn: j.aprende, presets: j.presets, readouts: j.lectura,
    experiments: j.experimentos?.map((x) => ({ id: x.id, titulo: x.titulo, setup: x.setup as Params, cambio: x.cambio as Params | undefined, pregunta: x.pregunta, opciones: x.opciones, correcta: x.correcta, explicacion: x.explicacion, check: x.verifica ? (a: M, d: M) => !!ev(x.verifica!, { antes: a, despues: d }) : undefined })),
    solution: j.solucion ? (p, m) => { const sc = ctxOf(p, m); return j.solucion!.filter((s) => !s.si || ev(s.si, sc)).map((s) => ({ t: tpl(s.t, sc), tex: tpl(s.tex, sc), nota: s.nota ? tpl(s.nota, sc) : undefined })); } : undefined,
    compare: j.comparar ? (p, m) => { const sc = ctxOf(p, m); return j.comparar!.map((c) => ({ label: c.label, teoria: evNum(c.teoria, sc), sim: evNum(c.sim, sc), nota: c.nota && ev(c.nota.si, sc) ? tpl(c.nota.txt, sc) : undefined })); } : undefined,
    insight: j.insight ? (p, m) => { const sc = ctxOf(p, m); return j.insight!.map((g) => g.find((x) => ev(x.si, sc))).filter(Boolean).map((x) => tpl(x!.txt, sc)).join(' '); } : undefined,
  };
  return {
    id: j.id, title: j.titulo, area: j.area, subarea: j.subarea, competencia: j.competencia, evidencias: j.evidencias, nivel: j.nivel, tiempoMin: j.tiempoMin,
    mode: j.modo === 'estatico' ? 'static' : 'dynamic',
    params: j.params.map((q) => ({ key: q.key, label: q.label, type: q.tipo, min: q.min, max: q.max, step: q.paso, default: q.def, unit: q.unidad, options: q.opciones, hint: q.hint })),
    logic, graphs: j.graficas?.map((g) => ({ id: g.id, x: g.x, y: g.y, title: g.titulo })), measureLabels: j.etiquetasMedidas, challenges: retos,
    describe: j.descripcion ? (m, p) => tpl(j.descripcion!, ctxOf(p, m)) : undefined,
    ...extra,
    render: { width: j.escena.ancho, height: j.escena.alto, view: (v) => drawScene(j, base, v) },
  } as SimConfig;
}
