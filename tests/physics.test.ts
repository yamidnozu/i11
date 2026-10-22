import { describe, it, expect } from 'vitest';
import { cross, gametes } from '../src/sims/punnett';
import { invariant, initLV, stepLV } from '../src/sims/lotka';
import { theoretical, rollMany, initProb } from '../src/sims/probability';
import { describeData } from '../src/sims/stats';
import { findRoots } from '../src/sims/functions';

describe('genética', () => {
  it('gametos', () => expect(gametes('AaBb').sort()).toEqual(['AB', 'Ab', 'aB', 'ab']));
  it('Aa×Aa = 3:1', () => { const c = cross('Aa', 'Aa'); expect(c.phenotypes).toEqual({ 'A_': 3, aa: 1 }); });
  it('AaBb×AaBb = 9:3:3:1', () => { const c = cross('AaBb', 'AaBb'); expect(Object.values(c.phenotypes).sort((a, b) => b - a)).toEqual([9, 3, 3, 1]); });
});
describe('Lotka-Volterra', () => {
  const q = { alpha: 1, beta: 0.1, delta: 0.02, gamma: 0.5 };
  it('el invariante se conserva', () => {
    let s = initLV(40, 9, q); const v0 = s.V;
    for (let i = 0; i < 4000; i++) s = stepLV(s, q, 0.01);
    expect(Math.abs(s.V - v0) / Math.abs(v0)).toBeLessThan(1e-4);
  });
  it('equilibrio (25,10) constante', () => { let s = initLV(25, 10, q); for (let i = 0; i < 1000; i++) s = stepLV(s, q, 0.01); expect(s.x).toBeCloseTo(25, 6); expect(s.y).toBeCloseTo(10, 6); });
  it('V(25,10)', () => expect(invariant(25, 10, q)).toBeCloseTo(0.02 * 25 - 0.5 * Math.log(25) + 0.1 * 10 - Math.log(10), 10));
});
describe('probabilidad', () => {
  it('suma de 2 dados suma 1', () => expect(theoretical(2).reduce((a, b) => a + b, 0)).toBeCloseTo(1, 12));
  it('LGN: más lanzamientos, menor desviación', () => {
    const a = rollMany(initProb(1), 60), b = rollMany(initProb(1), 60000);
    expect(b.maxDev).toBeLessThan(a.maxDev); expect(b.maxDev).toBeLessThan(0.01);
  });
});
describe('estadística', () => {
  it('2,3,3,4,8', () => { const d = describeData([2, 3, 3, 4, 8]); expect(d.mean).toBe(4); expect(d.median).toBe(3); expect(d.mode).toBe(3); expect(d.range).toBe(6); });
});
describe('funciones', () => { it('raíces de x²-4', () => expect(findRoots((x) => x * x - 4)).toEqual([-2, 2])); });
