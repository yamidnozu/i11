import { describe, it, expect } from 'vitest';
import { mx } from '../src/ui/automath';
describe('expresiones aritméticas en texto', () => {
  it('tipografía toda la cuenta como una sola expresión', () => {
    const h = mx('Multiplico 7 × 1.000 = 7.000 y sumo 7.000 + 4.000 = 11.000.');
    expect((h.match(/class="tex"/g) ?? []).length).toBe(2);
    expect(h).toContain('×');
  });
  it('no toca frases normales ni listas', () => {
    expect(mx('Dos y tres, además de ocho')).toBe('Dos y tres, además de ocho');
    expect(mx('Datos 2, 3, 3, 4, 8').replace(/<[^>]+>/g, '')).not.toMatch(/[+=×]/);
  });
  it('variables con igual', () => { expect(mx('con g = 10 m/s²')).toContain('class="tex"'); });
});
