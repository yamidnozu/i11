import { describe, it, expect } from 'vitest';
import { eap, P3, fisher } from '../src/adaptive/irt';
import { areaScore, globalScore } from '../src/adaptive/score';
import { review, retrievability, interval } from '../src/adaptive/scheduler';
import { tick } from '../src/adaptive/streak';
import { eloUpdate } from '../src/adaptive/elo';

const it3 = (b: number) => ({ b, c: 0.25 });
describe('IRT', () => {
  it('P crece con theta y respeta el azar', () => { expect(P3(-9, it3(0))).toBeGreaterThan(0.25); expect(P3(-9, it3(0))).toBeLessThan(0.26); expect(P3(2, it3(0))).toBeGreaterThan(P3(0, it3(0))); });
  it('EAP sube con aciertos y baja con fallos', () => {
    const hi = eap([0, 0.5, 1, 1.5].map((b) => ({ item: it3(b), correct: true })));
    const lo = eap([0, 0.5, 1, 1.5].map((b) => ({ item: it3(b), correct: false })));
    expect(hi.theta).toBeGreaterThan(0.3); expect(lo.theta).toBeLessThan(-0.3);
  });
  it('SE baja con más datos', () => {
    const r = (n: number) => eap(Array.from({ length: n }, (_, i) => ({ item: it3((i % 5) - 2), correct: i % 2 === 0 })));
    expect(r(30).se).toBeLessThan(r(4).se);
  });
  it('Fisher máxima cerca de b', () => expect(fisher(0, it3(0))).toBeGreaterThan(fisher(0, it3(3))));
});
describe('puntajes', () => {
  it('rango', () => { expect(areaScore('matematicas', 10)).toBe(100); expect(areaScore('matematicas', -10)).toBe(0); });
  it('global ponderado 0-500', () => {
    expect(globalScore({ matematicas: 100, lectura_critica: 100, sociales: 100, ciencias: 100, ingles: 100 })).toBe(500);
    expect(globalScore({ matematicas: 50, lectura_critica: 50, sociales: 50, ciencias: 50 })).toBe(250);
  });
});
describe('repaso espaciado', () => {
  it('R(0)=1 y R(S) ≈ 0.9', () => { expect(retrievability(0, 5)).toBe(1); expect(retrievability(5, 5)).toBeCloseTo(0.9, 5); });
  it('intervalo crece con aciertos y respeta el examen', () => {
    let c = review(undefined, 3, 0);
    const i1 = c.due - c.last; c = review(c, 3, c.due); expect(c.due - c.last).toBeGreaterThanOrEqual(i1);
    const near = review(c, 4, 0, 20); expect(near.due).toBeLessThanOrEqual(15);
    expect(interval(1000)).toBe(90);
  });
  it('un fallo reduce la estabilidad', () => { const a = review(undefined, 4, 0), b = review(a, 1, 3); expect(b.S).toBeLessThan(a.S); });
});
describe('racha y Elo', () => {
  it('racha', () => {
    expect(tick({ count: 3, lastDay: 10, freezes: 0 }, 11).count).toBe(4);
    expect(tick({ count: 3, lastDay: 10, freezes: 1 }, 12)).toEqual({ count: 4, lastDay: 12, freezes: 0 });
    expect(tick({ count: 3, lastDay: 10, freezes: 0 }, 15).count).toBe(1);
  });
  it('Elo', () => { expect(eloUpdate(0, 0, 0, 0.25, true).theta).toBeGreaterThan(0); expect(eloUpdate(0, 0, 0, 0.25, false).theta).toBeLessThan(0); });
});
