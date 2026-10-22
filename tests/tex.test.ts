import { describe, it, expect } from 'vitest';
import { tex, rich } from '../src/ui/tex';
describe('tex', () => {
  it('fracción, subíndice, raíz y texto', () => {
    expect(tex('\\frac{a}{b}')).toContain('class="frac"');
    expect(tex('x_0')).toContain('<sub>');
    expect(tex('\\sqrt{x}')).toContain('class="sqrt"');
    expect(tex('\\text{m/s}')).toContain('m/s');
  });
  it('sub y sup juntos se apilan', () => expect(tex('x_0^2')).toContain('class="ss"'));
  it('griegas y símbolos', () => { expect(tex('\\theta')).toContain('θ'); expect(tex('a \\cdot b')).toContain('·'); });
  it('escapa HTML', () => expect(tex('<b>')).not.toContain('<b>'));
  it('rich mezcla texto y fórmulas', () => { const r = rich('Alcance $R=\\frac{1}{2}$ y **ojo** <x>'); expect(r).toContain('frac'); expect(r).toContain('<strong>ojo</strong>'); expect(r).toContain('&lt;x&gt;'); });
});

describe('a/b en línea se apila', () => {
  it('convierte 12/6 y d_i/d_o en fracción, pero no m/s dentro de \\text', async () => {
    const { tex } = await import('../src/ui/tex');
    expect(tex('I=12/6=2')).toContain('class="frac"');
    expect(tex('m=-d_i/d_o')).toContain('class="frac"');
    expect(tex('2\\cdot0{,}082/1')).toContain('class="frac"');
    expect(tex('20\\ \\text{m/s}')).not.toContain('class="frac"');
  });
});

describe('fórmulas pegadas y ecuaciones sin lado izquierdo', () => {
  it('funde "$6$ × $6$ = $36$" en una sola cuenta', () => {
    const h = rich('hay $6$ × $6$ = $36$ parejas');
    expect((h.match(/class="tex"/g) ?? []).length).toBe(1);
  });
});
