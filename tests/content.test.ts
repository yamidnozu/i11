import { describe, it, expect } from 'vitest';
import { readdirSync, readFileSync } from 'node:fs';
import { validateQuestion, validateLesson, type Question, type Lesson } from '../src/content/schema';
import { registerAll } from '../src/sims';
import { getSim } from '../src/core/registry';

const hojas = JSON.parse(readFileSync('content/hojas.json', 'utf8'));
const qs: Question[] = readdirSync('content/questions').flatMap((f) => JSON.parse(readFileSync(`content/questions/${f}`, 'utf8'))).map((q: Question) => (hojas[q.id] ? { ...q, hoja: hojas[q.id] } : q));
describe('banco de preguntas', () => {
  it('todas válidas e ids únicos', () => {
    expect(qs.flatMap(validateQuestion)).toEqual([]);
    expect(new Set(qs.map((q) => q.id)).size).toBe(qs.length);
  });
  it('las 5 áreas tienen preguntas', () => expect(new Set(qs.map((q) => q.area)).size).toBe(5));
  it('los simuladores y retos referenciados existen', () => {
    registerAll();
    for (const q of qs) if (q.sim) { const s = getSim(q.sim.id); expect(s, q.id).toBeTruthy(); if (q.sim.challengeId) expect(s!.challenges.some((c) => c.id === q.sim!.challengeId), q.id).toBe(true); }
  });
});
describe('lecciones', () => {
  it('5 ángulos y truco', () => {
    for (const f of readdirSync('content/lessons')) expect(validateLesson(JSON.parse(readFileSync(`content/lessons/${f}`, 'utf8')) as Lesson)).toEqual([]);
  });
});

import { tex } from '../src/ui/tex';
describe('hojas de resolución', () => {
  it('todas apuntan a preguntas existentes y sus fórmulas componen', () => {
    for (const id of Object.keys(hojas)) expect(qs.some((q) => q.id === id), id).toBe(true);
    for (const q of qs) for (const p of q.hoja?.pasos ?? []) if (p.k === 'calc') for (const l of p.lineas) { const o = tex(l); expect(o, `${q.id}: ${l}`).not.toMatch(/undefined|NaN|\\[a-z]+/); }
  });
  it('cada hoja tiene comprobación y al menos 3 pasos entre subrayado y cierre', () => {
    for (const q of qs) if (q.hoja) { expect(q.hoja.pasos.some((p) => p.k === 'check'), q.id).toBe(true); expect(q.hoja.pasos.length, q.id).toBeGreaterThanOrEqual(2); }
  });
});
import { evaluarMarcas, parseNum } from '../src/ui/guia';
import { atomize, mx } from '../src/ui/automath';
describe('guía interactiva', () => {
  it('subrayar exactamente las marcas da resultado perfecto, y no subrayar nada deja todo faltante', () => {
    for (const q of qs) {
      const ms = q.hoja?.marcas ?? []; if (!ms.length) continue;
      const atoms = atomize(q.enunciado); const tags: Record<number, any> = {};
      for (const m of ms) { const i = q.enunciado.indexOf(m.frag); atoms.forEach((a, k) => { if (!a.space && a.start < i + m.frag.length && a.end > i) tags[k] = m.rol; }); }
      const r = evaluarMarcas(q.enunciado, ms, tags);
      expect(r.missed, q.id).toEqual([]); expect(r.extra, q.id).toEqual([]);
      expect(evaluarMarcas(q.enunciado, ms, {}).found, q.id).toEqual([]);
    }
  });
  it('números en formato colombiano se leen bien', () => {
    expect(parseNum('11.000')).toBe(11000); expect(parseNum('0,375')).toBe(0.375); expect(parseNum('34,6')).toBe(34.6); expect(parseNum('-2')).toBe(-2); expect(parseNum('abc')).toBeNaN();
  });
  it('el texto de las tareas compone sin restos de comandos', () => {
    for (const q of qs) for (const t of q.hoja?.guia ?? []) {
      const txt: string[] = t.k === 'asignar' ? t.items.flatMap((i) => [i.p, i.why, ...i.op]) : t.k === 'llenar' ? [t.pista ?? '', t.why, t.unidad ?? ''] : [t.why, ...t.items];
      for (const s of txt) expect(mx(s), `${q.id}: ${s}`).not.toMatch(/\\[a-zA-Z]{2,}/);
      if (t.k === 'llenar') expect(tex(t.antes)).not.toMatch(/\\[a-zA-Z]{2,}/);
    }
  });
});
import { perm } from '../src/ui/guia';
describe('mezcla de opciones', () => {
  it('es permutación y no deja la correcta siempre primera', () => {
    let first = 0, total = 0;
    for (const q of qs) for (const t of q.hoja?.guia ?? []) if (t.k === 'asignar') for (const it of t.items) { const p = perm(it.op.length, it.p); expect([...p].sort()).toEqual(it.op.map((_, i) => i)); total++; if (p[0] === it.ok) first++; }
    expect(first / total).toBeLessThan(0.6);
  });
});
describe('marcas y fichas', () => {
  it('las marcas no se pisan entre sí y todas tienen campo para la ficha', () => {
    for (const q of qs) {
      const r = (q.hoja?.marcas ?? []).map((m) => [q.enunciado.indexOf(m.frag), q.enunciado.indexOf(m.frag) + m.frag.length, m.frag] as const);
      r.forEach(([a, b, f], i) => { expect(a, `${q.id}: ${f}`).toBeGreaterThanOrEqual(0); r.forEach(([c, d, g], j) => { if (i < j) expect(a < d && c < b, `${q.id}: «${f}» pisa «${g}»`).toBe(false); }); });
      for (const m of q.hoja?.marcas ?? []) { expect(m.campo, `${q.id}: ${m.frag}`).toBeTruthy(); expect(mx(m.campo!)).not.toMatch(/\\[a-zA-Z]{2,}/); }
    }
  });
});

import { QUESTIONS as QS, LESSONS as LS } from '../src/content';
import { hablar as hb } from '../src/ui/hablar';
describe('guiones', () => {
  for (const q of QS.filter((x) => x.hoja?.guion)) {
    it(`guion ${q.id}`, () => {
      const g = q.hoja!.guion!;
      for (const n of ['1', '2', '3'] as const) {
        expect(g[n].length).toBeGreaterThanOrEqual(3);
        for (const bt of g[n]) {
          expect(hb(bt.v ?? bt.t).replace(/\{\{.+?\}\}/g, '')).not.toMatch(/[\\$^{}]/);
          for (const a of (bt.a ?? '').split('|').filter(Boolean)) {
            const [c, ...r] = a.split(':'), arg = r.join(':');
            if (c === 'm') expect(q.hoja!.marcas!.some((m) => m.frag === arg), `${q.id} m:${arg}`).toBe(true);
            if (c === 'p') expect(q.hoja!.pasos[Number(arg)], `${q.id} p:${arg}`).toBeTruthy();
            if (c === 'o') expect('ABCDEFGH'.indexOf(arg[0])).toBeLessThan(q.opciones.length);
          }
        }
      }
      if (q.opciones.length) expect(g['2'].filter((x) => /^o:[A-H]:no/.test(x.a ?? '') || (x.a ?? '').includes('o:')).length).toBeGreaterThanOrEqual(1);
    });
  }
});

describe('auditoría: cobertura y lectura', () => {
  const con = QS.filter((x) => x.hoja);
  it('toda pregunta con hoja tiene guion de 3 niveles y enfoque', () => {
    for (const q of con) { expect(q.hoja!.guion, q.id).toBeTruthy(); expect(q.hoja!.enfoque?.tema, q.id).toBeTruthy(); expect(q.hoja!.enfoque!.no.length, q.id).toBeGreaterThanOrEqual(2); const en = q.hoja!.enfoque!; expect(en.que.length, q.id).toBeGreaterThan(40); expect(en.pistas.length, q.id).toBeGreaterThanOrEqual(2); expect(en.plan.length, q.id).toBeGreaterThanOrEqual(3); for (const x of en.no) expect(x.p, q.id).toMatch(/Pero/); const bad = /armo la regla|casos favorables|despejo|reemplazo en/i; expect(JSON.stringify(en), q.id).not.toMatch(bad); }
  });
  it('llaves {{ }} del inglés balanceadas', () => {
    for (const q of con) for (const n of ['1', '2', '3'] as const) for (const bt of q.hoja!.guion![n]) expect((bt.t.match(/\{\{/g) ?? []).length, `${q.id} ${bt.t}`).toBe((bt.t.match(/\}\}/g) ?? []).length);
  });
  it('el inglés se conserva para la voz en inglés', () => { expect(hb('Dice {{Monday–Friday}} y abre.')).toContain('{{Monday–Friday}}'); });
  it('en el nivel 2 se descarta cada opción incorrecta', () => {
    const faltan: string[] = []; for (const q of con) { const dichas = new Set(q.hoja!.guion!['2'].flatMap((x) => (x.a ?? '').split('|')).filter((a) => a.startsWith('o:') && a.endsWith(':no')).map((a) => a[2])); const malas = q.opciones.map((_, i) => 'ABCDEFGH'[i]).filter((_, i) => i !== q.correcta); for (const L of malas) if (!dichas.has(L)) faltan.push(`${q.id}:${L}`); } expect(faltan).toEqual([]);
  });
  it('lo hablado no deja restos de código', () => { for (const q of con) for (const n of ['1', '2', '3'] as const) for (const bt of q.hoja!.guion![n]) expect(hb(bt.t).replace(/\{\{.+?\}\}/g, '')).not.toMatch(/[\\$^_]|\bfrac\b/); });
});

describe('lo que dice el profe', () => {
  it('no deja ninguna cifra sin leer en palabras (ni en guion ni en enfoque)', () => {
    for (const q of QS) {
      const h = q.hoja; if (!h) continue;
      const textos: string[] = [];
      for (const n of ['1', '2', '3'] as const) for (const b of h.guion?.[n] ?? []) textos.push(b.t);
      if (h.enfoque) { const e = h.enfoque; textos.push(e.que, e.clave, ...e.pistas, ...e.plan.map((x) => x.t), ...e.no.map((x) => x.p)); }
      for (const t of textos) expect(hb(t).replace(/\{\{.+?\}\}/g, ''), q.id + ': ' + t).not.toMatch(/\d/);
    }
  });
});

describe('ecuaciones bien formadas', () => {
  it('ninguna fórmula explícita empieza por "=" o "≈" (se vería "= resultado" sin lado izquierdo)', () => {
    const malas: string[] = [];
    const ver = (x: unknown, ruta: string) => {
      if (typeof x === 'string') { for (const m of x.matchAll(/\$([^$]+)\$/g)) if (/^\s*(=|\\approx|\\Rightarrow|≈|⇒)/.test(m[1])) malas.push(`${ruta}: ${m[1].slice(0, 40)}`); }
      else if (Array.isArray(x)) x.forEach((v, i) => ver(v, `${ruta}[${i}]`));
      else if (x && typeof x === 'object') for (const [k, v] of Object.entries(x)) ver(v, `${ruta}.${k}`);
    };
    ver(QS, 'preguntas'); ver(LS, 'lecciones');
    for (const f of readdirSync('src/learn')) ver(readFileSync(`src/learn/${f}`, 'utf8').replace(/\\\\/g, '\\'), f);
    expect(malas).toEqual([]);
  });
});
