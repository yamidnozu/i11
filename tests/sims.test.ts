import { describe, it, expect } from 'vitest';
import { simulateProjectile } from '../src/sims/projectile';
import { muaX, muaV } from '../src/sims/mrua';
import { solveCircuit } from '../src/sims/ohm';
import { thinLens } from '../src/sims/lens';
import { idealVolume, initGas, stepGas } from '../src/sims/gases';
import { registerAll } from '../src/sims';
import { evaluateChallenge } from '../src/core/engine';

describe('proyectil', () => {
  it('v0=20, 30°, g=10: R≈34,641, H=5, t=2', () => {
    const s = simulateProjectile(20, 30, 10);
    expect(s.x).toBeCloseTo(34.641016, 2); expect(s.ymax).toBeCloseTo(5, 2); expect(s.t).toBeCloseTo(2, 2);
  });
  it('ángulos complementarios, mismo alcance; 45° máximo', () => {
    expect(simulateProjectile(20, 30, 9.8).x).toBeCloseTo(simulateProjectile(20, 60, 9.8).x, 2);
    expect(simulateProjectile(20, 45, 9.8).x).toBeCloseTo(400 / 9.8, 2);
  });
  it('con aire el alcance es menor', () => expect(simulateProjectile(20, 45, 9.8, true).x).toBeLessThan(simulateProjectile(20, 45, 9.8).x));
});
describe('MRUA', () => { it('x0=2,v0=5,a=3,t=4', () => { expect(muaX(2, 5, 3, 4)).toBe(46); expect(muaV(5, 3, 4)).toBe(17); }); });
describe('Ohm', () => {
  it('12 V, 2 Ω + (6||3)', () => { const c = solveCircuit(12, 2, 6, 3); expect(c.Rt).toBeCloseTo(4); expect(c.I).toBeCloseTo(3); expect(c.Ptot).toBeCloseTo(36); expect(c.I2 + c.I3).toBeCloseTo(c.I); });
});
describe('lente', () => { it('f=10, do=15, h=4', () => { const l = thinLens(10, 15, 4); expect(l.d_i).toBeCloseTo(30); expect(l.M).toBeCloseTo(-2); expect(l.h_i).toBeCloseTo(-8); }); });
describe('gases', () => {
  it('V=nRT/P', () => expect(idealVolume(2, 273.15, 1)).toBeCloseTo(44.8279, 3));
  it('P·A/(N·T) ≈ 1', () => {
    let s = initGas(80, 300, 100);
    for (let i = 0; i < 120 * 40; i++) s = stepGas(s, 1 / 120);
    const r = (s.pressure * s.W * s.H) / (s.N * s.T);
    expect(r).toBeGreaterThan(0.85); expect(r).toBeLessThan(1.15);
  });
});
describe('registro y retos', () => {
  it('11 simuladores válidos', () => expect(registerAll().length).toBe(11));
  it('criterio de reto', () => expect(evaluateChallenge({ id: 'x', prompt: '', checks: [{ measure: 'a', target: 40, tol: 0.5 }] }, { a: 40.3 })).toBe(true));
});
