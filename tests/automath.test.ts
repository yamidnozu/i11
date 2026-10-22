import { describe, it, expect } from 'vitest';
import { atomize, mx } from '../src/ui/automath';
const m = (s: string) => atomize(s).filter((a) => a.math).map((a) => a.raw);
describe('automath', () => {
  it('detecta cantidades, fracciones, fórmulas y variables', () => {
    expect(m('rapidez de 20 m/s y ángulo de 30° (g = 10 m/s²)')).toEqual(['20 m/s', '30°', 'g = 10 m/s²']);
    expect(m('probabilidad 3/8 y 12 V')).toEqual(['3/8', '12 V']);
    expect(m('C₃H₈ + 5 O₂ → 3 CO₂')).toEqual(['C₃H₈', '5', 'O₂', '3', 'CO₂']);
    expect(m('en 1810 pagó $4.000 y 4,5 %')).toEqual(['1810', '4.000', '4,5 %']);
    expect(m('x² y v₀')).toEqual(['x²', 'v₀']);
  });
  it('conserva el texto: los offsets cubren la cadena completa', () => {
    const t = 'Un móvil de 3 m/s² recorre 24 m en 4 s.';
    const a = atomize(t);
    expect(a.map((x) => x.raw).join('')).toBe(t);
    a.forEach((x) => expect(t.slice(x.start, x.end)).toBe(x.raw));
  });
  it('no confunde palabras con unidades ni escapa mal', () => {
    expect(m('mil metros en un minuto')).toEqual([]);
    expect(mx('a < b')).toContain('&lt;');
    expect(mx('explícito $x^2$ ok')).toContain('class="tex"');
  });
});
describe('dinero con signo $', () => {
  it('no se confunde con matemática explícita', () => {
    expect(m('cobra $4.000 de arranque más $1.000 por km')).toEqual(['4.000', '1.000']);
    expect(mx('cobra $4.000 de arranque más $1.000')).toContain('$');
    expect(m('$100.000\\cdot1{,}2=120.000$ y $x^2$')).toEqual(['$100.000\\cdot1{,}2=120.000$', '$x^2$']);
  });
});
