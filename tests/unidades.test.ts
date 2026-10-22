import { describe, it, expect } from 'vitest';
import { UNIDADES, preguntasDe } from '../src/content/unidades';
import { QUESTIONS, LESSONS } from '../src/content';
import { registerAll } from '../src/sims';
import { getSim } from '../src/core/registry';

describe('unidades (ruta de estudio)', () => {
  registerAll();
  it('cada pregunta del banco pertenece a exactamente una unidad', () => {
    const cuenta = new Map<string, number>();
    for (const u of UNIDADES) for (const id of u.preguntas) cuenta.set(id, (cuenta.get(id) ?? 0) + 1);
    for (const q of QUESTIONS) expect(cuenta.get(q.id), q.id).toBe(1);
  });
  it('las preguntas, laboratorios y lecciones referenciados existen y son del área', () => {
    for (const u of UNIDADES) {
      expect(preguntasDe(u).length, u.id).toBe(u.preguntas.length);
      for (const q of preguntasDe(u)) expect(q.area, `${u.id}/${q.id}`).toBe(u.area);
      if (u.sim) expect(getSim(u.sim), u.sim).toBeTruthy();
      if (u.leccion) expect(LESSONS.some((l) => l.id === u.leccion), u.leccion!).toBe(true);
    }
  });
  it('ids únicos', () => { expect(new Set(UNIDADES.map((u) => u.id)).size).toBe(UNIDADES.length); });
});
