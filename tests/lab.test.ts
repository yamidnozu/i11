import { describe, it, expect } from 'vitest';
import { LABS_JSON, LAB_WARNINGS, compileLab } from '../src/lab';
import { evNum, tpl, compile } from '../src/lab/expr';
import { BASE_CODIGO, ALL_SIMS } from '../src/sims';
import { validateLab } from '../src/lab/schema';
import { runHeadless as simulate } from '../src/core/thumb';

describe('expresiones', () => {
  it('aritmética y funciones', () => { expect(evNum('2+3*4^2', {})).toBe(50); expect(evNum('hypot(3,4)+max(1,7)', {})).toBe(12); expect(evNum('si(x>2,10,20)', { x: 3 })).toBe(10); });
  it('no permite código', () => { expect(() => compile('constructor')).toThrow(); expect(() => compile('a.__proto__')).toThrow(); expect(() => compile('alert(1);')).toThrow(); });
  it('plantillas con coma decimal', () => { expect(tpl('x = #{a|1} m', { a: 3.14159 })).toBe('x = 3,1 m'); expect(tpl('\\frac{1}{2}=#{0.5}', {})).toBe('\\frac{1}{2}=0,5'); });
});
describe('laboratorios en JSON', () => {
  it('no hay avisos y todos son válidos', () => { expect(LAB_WARNINGS).toEqual([]); for (const j of LABS_JSON) expect(validateLab(j), j.id).toEqual([]); });
  it('detecta errores', () => { const e = validateLab({ id: 'x', escena: { capas: [{ t: 'dragon' }] } } as never); expect(e.length).toBeGreaterThan(3); });
  it('cada laboratorio JSON iguala al hecho en código (mismas medidas)', () => {
    for (const j of LABS_JSON) {
      const cod = BASE_CODIGO.find((b) => b.id === j.id); if (!cod) continue;
      const nuevo = compileLab(j);
      const casos: Record<string, number | boolean>[] = [{}, { v0: 10, theta: 30, g: 10 }, { v0: 35, theta: 60, g: 1.62 }, { v0: 20, theta: 45, drag: true }, { v0: 40, theta: 10, drag: true }, { v0: 5, theta: 89, g: 9.8 }, { v0: 20, theta: 0 }];
      for (const c of casos) {
        const p = Object.fromEntries([...cod.params.map((q) => [q.key, q.default]), ...Object.entries(c)]);
        const a = simulate(cod, p).measures, b = simulate(nuevo, p).measures;
        for (const k of Object.keys(a)) expect(b[k], `${j.id} ${JSON.stringify(c)} ${k}`).toBeCloseTo(a[k], 2);
      }
    }
  });
  it('los experimentos de cada JSON se cumplen numéricamente', () => {
    for (const j of LABS_JSON) { const s = compileLab(j); for (const x of s.experiments ?? []) {
      const p0 = { ...Object.fromEntries(s.params.map((q) => [q.key, q.default])), ...x.setup }, p1 = { ...p0, ...(x.cambio ?? {}) };
      if (x.check) expect(x.check(simulate(s, p0).measures, simulate(s, p1).measures), `${j.id}/${x.id}`).toBe(true); } }
  });
  it('los retos tienen solución y la explicación se genera', () => { expect(ALL_SIMS.length).toBeGreaterThanOrEqual(11); for (const j of LABS_JSON) { const s = compileLab(j); const p = Object.fromEntries(s.params.map((q) => [q.key, q.default])); const m = simulate(s, p).measures; expect(s.solution?.(p, m).length ?? 1).toBeGreaterThan(0); expect(s.insight?.(p, m) ?? 'x').toBeTruthy(); } });
});
