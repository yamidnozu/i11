import { describe, it, expect } from 'vitest';
import { QUESTIONS, BLOQUES, LESSONS, UNIDADES_ALL, CONTENT_WARNINGS } from '../src/content';
import { SIMULACROS, armar, armarExamen, resumen } from '../src/content/simulacros';
import { validateQuestion, validateSimulacro } from '../src/content/schema';

describe('contenido por JSON (content/questions, packs, simulacros)', () => {
  it('no hay avisos de contenido mal formado', () => { expect(CONTENT_WARNINGS).toEqual([]); });
  it('ids de pregunta únicos y válidas', () => {
    expect(new Set(QUESTIONS.map((q) => q.id)).size).toBe(QUESTIONS.length);
    expect(QUESTIONS.flatMap(validateQuestion)).toEqual([]);
  });
  it('cada unidad apunta a preguntas y lección existentes', () => {
    const ids = new Set(QUESTIONS.map((q) => q.id));
    for (const u of UNIDADES_ALL) {
      for (const q of u.preguntas) expect(ids.has(q), `${u.id}: ${q}`).toBe(true);
      if (u.leccion) expect(LESSONS.some((l) => l.id === u.leccion), `${u.id}: lección ${u.leccion}`).toBe(true);
    }
  });
  it('los simulacros son válidos y se pueden armar', () => {
    expect(SIMULACROS.length).toBeGreaterThanOrEqual(1);
    const ids = new Set(QUESTIONS.filter((q) => q.tipo !== 'reto').map((q) => q.id));
    for (const s of SIMULACROS) {
      expect(validateSimulacro(s, ids)).toEqual([]);
      const a = s.modo === 'examen' ? armarExamen(s).flatMap((x) => x.pruebas) : armar(s), todas = a.flatMap((c) => c.ids);
      expect(a.length, s.id).toBeGreaterThan(0);
      expect(new Set(todas).size, `${s.id}: preguntas repetidas`).toBe(todas.length);
      expect(resumen(s).preguntas).toBeGreaterThan(0);
    }
  });
  it('las figuras, bloques y opciones con dibujo del ejemplo son válidos y los bloques no se parten', () => {
    const ex = QUESTIONS.filter((q) => q.bloque);
    expect(ex.length).toBeGreaterThan(5);
    expect(BLOQUES.length).toBeGreaterThan(3);
    expect(QUESTIONS.some((q) => q.opcionesFig)).toBe(true);
    expect(QUESTIONS.some((q) => q.opciones.length > 4)).toBe(true);
    const ses = armarExamen(SIMULACROS.find((s) => s.id === 'cuadernillo-ejemplo')!);
    for (const p of ses.flatMap((x) => x.pruebas)) {
      const bl = p.ids.map((id) => QUESTIONS.find((q) => q.id === id)!.bloque).filter(Boolean);
      for (const b of new Set(bl)) { const i = bl.indexOf(b), n = bl.filter((x) => x === b).length; expect(bl.slice(i, i + n).every((x) => x === b), b).toBe(true); expect(n, b).toBe(QUESTIONS.filter((q) => q.bloque === b).length); }
    }
  });
  it('un simulacro mal formado se detecta', () => {
    const mal = { id: 'X', nombre: '', secciones: [{ titulo: 'a', minutos: 0, preguntas: ['zzz-999'] }] };
    expect(validateSimulacro(mal as never, new Set()).length).toBeGreaterThanOrEqual(3);
  });
});

import { NIVELES, nivelDe } from '../src/content/niveles';
import { AREA_IDS } from '../src/adaptive/areas';
describe('niveles de desempeño', () => {
  it('cada prueba tiene 4 niveles que cubren 0 a 100 sin huecos', () => {
    for (const a of AREA_IDS) { const n = NIVELES[a]; expect(n.length, a).toBe(4); expect(n[0].desde).toBe(0); expect(n[3].hasta).toBe(100); for (let i = 1; i < 4; i++) expect(n[i].desde, a).toBe(n[i - 1].hasta + 1); n.forEach((x) => expect(x.demuestra.length, a).toBeGreaterThan(0)); }
  });
  it('los límites caen en el nivel correcto', () => { expect(nivelDe('matematicas', 35).nombre).toBe('Nivel 1'); expect(nivelDe('matematicas', 36).nombre).toBe('Nivel 2'); expect(nivelDe('ingles', 58).nombre).toBe('A2'); expect(nivelDe('ingles', 71).nombre).toBe('B1'); });
});
