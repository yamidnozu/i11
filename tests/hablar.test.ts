import { describe, it, expect } from 'vitest';
import { hablar } from '../src/ui/hablar';
import { enPalabras } from '../src/ui/numeros';
describe('hablar', () => {
  it('lee cantidades con unidades', () => {
    expect(hablar('rapidez de 20 m/s y 30° con g = 10 m/s²')).toBe('rapidez de veinte metros por segundo y treinta grados con g igual a diez metros por segundo al cuadrado');
    expect(hablar('cuesta $4.000 y 12 V')).toBe('cuesta cuatro mil pesos y doce voltios');
  });
  it('lee números grandes y decimales como se dicen', () => {
    expect(hablar('1.000 pesos')).toBe('mil pesos');
    expect(hablar('100.000 y 96.000 y 120.000')).toBe('cien mil y noventa y seis mil y ciento veinte mil');
    expect(hablar('R = 0,082 y 273,15 K')).toBe('R igual a cero coma cero ochenta y dos y doscientos setenta y tres coma quince kelvin');
    expect(hablar('en 1810 y 1991')).toBe('en mil ochocientos diez y mil novecientos noventa y uno');
    expect(hablar('1 kilómetro, 21.000 pesos, 1.000.000')).toBe('un kilómetro, veintiún mil pesos, un millón');
    expect(enPalabras(2000)).toBe('dos mil');
    expect(hablar('{{She goes 20 times}}')).toBe('{{She goes 20 times}}');
  });
  it('lee fórmulas en LaTeX', () => {
    expect(hablar('$R=\\frac{v_0^2\\,\\sin(2\\theta)}{g}$')).toContain('R igual a v sub cero al cuadrado seno de dos theta sobre g');
    expect(hablar('$x=\\frac{1}{2}\\cdot3\\cdot4^2=24\\ \\text{m}$')).toBe('x igual a uno sobre dos por tres por cuatro al cuadrado igual a veinticuatro metros');
    expect(hablar('$(x-1)(x-3)=0$')).toBe('x menos uno por x menos tres igual a cero');
  });
  it('lee fórmulas químicas y subíndices', () => {
    expect(hablar('C₃H₈ + 5 O₂ → 3 CO₂')).toBe('C tres H ocho más cinco O dos entonces tres C O dos');
    expect(hablar('v₀ y x²')).toBe('v sub cero y x al cuadrado');
  });
  it('no deja restos de código ni cifras', () => { for (const s of ['$P(\\text{roja})=\\frac{3}{3+5}=\\frac{3}{8}$', '$x^*=\\frac{\\gamma}{\\delta}$', '$\\bar{x}=\\frac{12}{4}=3$', '$f(x)=x^2-4x+3$', 'Entre 1810 y 1886 → cambia', 'Son 4.000 + 1.000 × 7 = 11.000']) { const r = hablar(s); expect(r).not.toMatch(/[\\${}^_]/); expect(r).not.toMatch(/\d/); } });
});
