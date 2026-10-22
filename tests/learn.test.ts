import { describe, it, expect } from 'vitest';
import { ALL_SIMS } from '../src/sims/index';
import { defaults, runHeadless } from '../src/core/thumb';
import { tex } from '../src/ui/tex';
import { analytic } from '../src/learn/projectile';

const bad = /NaN|undefined|Infinity|\[object/;

describe('capa pedagógica de los simuladores', () => {
  it('los 11 simuladores tienen contenido completo', () => {
    expect(ALL_SIMS.length).toBe(11);
    for (const s of ALL_SIMS as any[]) {
      expect(s.learn, s.id).toBeTruthy();
      expect(s.learn.formulas.length, s.id).toBeGreaterThan(1);
      expect(s.learn.ejemplos.length, s.id).toBeGreaterThan(1);
      expect(s.learn.errores.length, s.id).toBeGreaterThan(1);
      expect((s.presets ?? []).length, s.id).toBeGreaterThanOrEqual(3);
      expect((s.experiments ?? []).length, s.id).toBeGreaterThanOrEqual(3);
      expect(typeof s.solution, s.id).toBe('function');
    }
  });

  for (const s of ALL_SIMS as any[]) {
    describe(s.id, () => {
      const keys = new Set(s.params.map((d: any) => d.key));
      const inRange = (p: Record<string, any>) => {
        for (const [k, v] of Object.entries(p)) {
          expect(keys.has(k), `${s.id}: parámetro desconocido ${k}`).toBe(true);
          const d = s.params.find((x: any) => x.key === k);
          if (d.type === 'slider') { expect(v, `${s.id}.${k}`).toBeGreaterThanOrEqual(d.min); expect(v, `${s.id}.${k}`).toBeLessThanOrEqual(d.max); }
          if (d.type === 'select') expect(d.options.map((o: any) => o.v), `${s.id}.${k}`).toContain(v);
        }
      };
      it('presets válidos y resolubles', () => {
        for (const pr of s.presets) {
          inRange(pr.params);
          const p = { ...defaults(s), ...pr.params };
          const { measures } = runHeadless(s, p);
          const steps = s.solution(p, measures);
          expect(steps.length, pr.id).toBeGreaterThan(0);
          for (const st of steps) { expect(st.tex + (st.nota ?? ''), `${pr.id}: ${st.t}`).not.toMatch(bad); expect(() => tex(st.tex)).not.toThrow(); }
        }
      });
      it('experimentos: opción correcta válida y explicación verificada con la simulación', () => {
        for (const e of s.experiments) {
          expect(e.correcta, e.id).toBeGreaterThanOrEqual(0); expect(e.correcta, e.id).toBeLessThan(e.opciones.length);
          inRange(e.setup); if (e.cambio) inRange(e.cambio);
          if (e.check) {
            const before = runHeadless(s, { ...defaults(s), ...e.setup }).measures;
            const after = runHeadless(s, { ...defaults(s), ...e.setup, ...(e.cambio ?? {}) }).measures;
            expect(e.check(before, after), `${s.id}/${e.id} antes=${JSON.stringify(before)} después=${JSON.stringify(after)}`).toBe(true);
          }
        }
      });
      it('el texto matemático se compone sin errores', () => {
        const L = s.learn; const all = [L.resumen, ...L.objetivos, ...L.idea, L.analogia ?? '', L.saber11, ...L.formulas.map((f: any) => f.tex), ...L.ejemplos.flatMap((e: any) => [e.texto, ...e.pasos]), ...L.errores.flatMap((e: any) => [e.mito, e.realidad])];
        for (const t of all) expect(() => tex(t)).not.toThrow();
        for (const f of L.formulas) expect(f.tex + f.nombre).not.toMatch(bad);
      });
      it('compare e insight funcionan con los valores por defecto', () => {
        const p = defaults(s), { measures } = runHeadless(s, p);
        if (s.compare) for (const r of s.compare(p, measures)) { expect(Number.isFinite(r.teoria), r.label).toBe(true); expect(Number.isFinite(r.sim), r.label).toBe(true); }
        if (s.insight) expect(String(s.insight(p, measures))).not.toMatch(bad);
      });
    });
  }

  it('proyectil: teoría = simulación (sin aire)', () => {
    const s = (ALL_SIMS as any[]).find((x) => x.id === 'fis.proyectil');
    for (const [v0, th, g] of [[20, 30, 10], [25, 20, 9.8], [20, 45, 1.62]]) {
      const p = { ...defaults(s), v0, theta: th, g, drag: false };
      const m = runHeadless(s, p).measures, A = analytic(v0, th, g);
      expect(Math.abs(m.alcance - A.R) / A.R).toBeLessThan(0.01);
      expect(Math.abs(m.altura_max - A.H) / A.H).toBeLessThan(0.02);
    }
  });
});
