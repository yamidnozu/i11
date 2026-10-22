import { describe, it, expect } from 'vitest';
import { compile } from '../src/math/expr';
import { balance, parseFormula } from '../src/math/chem';
import { nextRand } from '../src/math/rng';

describe('expr', () => {
  it('prioridad y multiplicación implícita', () => {
    expect(compile('2x^2 - 3x + 1', ['x'])({ x: 3 })).toBe(10);
    expect(compile('(x+1)(x-1)', ['x'])({ x: 4 })).toBe(15);
    expect(compile('-x^2', ['x'])({ x: 3 })).toBe(-9);
  });
  it('rechaza código', () => { expect(() => compile('alert(1)', ['x'])).toThrow(); expect(() => compile('x;y', ['x'])).toThrow(); });
});
describe('chem', () => {
  it('fórmulas con paréntesis', () => expect(parseFormula('Ca(OH)2')).toEqual({ Ca: 1, O: 2, H: 2 }));
  it('propano', () => expect(balance('C3H8 + O2 -> CO2 + H2O').coefs).toEqual([1, 5, 3, 4]));
  it('glucosa', () => expect(balance('Fe + O2 -> Fe2O3').coefs).toEqual([4, 3, 2]));
  it('KMnO4', () => expect(balance('KMnO4 + HCl -> KCl + MnCl2 + H2O + Cl2').coefs).toEqual([2, 16, 2, 2, 8, 5]));
  it('imposible', () => expect(balance('H2 -> O2').ok).toBe(false));
});
describe('rng', () => { it('determinista', () => expect(nextRand(7)).toEqual(nextRand(7))); });
