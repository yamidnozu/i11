/** Al señalar un dato (número o palabra relevante), ilumina en dorado todos los lugares donde aparece o se refiere a lo mismo.
 *  Usa la CSS Custom Highlight API: no cambia el DOM (la hoja se escribe animada) y siempre lee el estado actual. */
import type { Marca } from '../content/schema';

const TOKEN = /\d+(?:[.,]\d+)*|\p{L}{4,}/gu;
const SALTAR = '.mtabs,.sn,.dots,.qmeta,sub,sup,.lvs,.toastf,.kbd,.ph,.sesionbar,script,style';
const VACIAS = new Set('para como pero este esta estos estas cada entre sobre desde hasta donde cuando tiene tienen hace hacen unos unas todo toda todos todas aqui ahora luego solo sola esto eso ese esa aquel que con sin por del los las una uno muy mas menos pide piden quiere dato datos falta parte forma tambien viene puede sirve queda cuanto cuantos cuanta cuantas cual cuales quien cuesta resulta texto lista dado dada hallar'.split(' '));

/** Misma cantidad escrita igual o distinto: «1.000» = «1000», «0,5» = «0.5». */
export function normaliza(t: string): string {
  if (/^\d{1,3}(\.\d{3})+(,\d+)?$/.test(t)) t = t.replace(/\./g, '');
  return t.replace(',', '.');
}
const sinTilde = (s: string) => s.toLowerCase().normalize('NFD').replace(/[̀-ͯ]/g, '');
const raiz = (w: string) => { let r = w.length > 5 ? w.replace(/(es|s)$/, '') : w.replace(/s$/, ''); if (r.length > 3) r = r.replace(/[aeo]$/, ''); return r; };
/** Clave comparable de una palabra o cantidad. */
export function clave(t: string): string { return /^\d/.test(t) ? `n:${normaliza(t)}` : `w:${raiz(sinTilde(t))}`; }

const NUMEROS = /\d+(?:[.,]\d+)*/g;
/** Unidad escrita en el enunciado → cómo se nombra en las explicaciones («12 V» ↔ «voltios»). */
const UNIDADES: Record<string, string> = { V: 'voltio', 'Ω': 'ohmio', A: 'amperio', km: 'kilometro', cm: 'centimetro', s: 'segundo', h: 'hora', K: 'kelvin', atm: 'atmosfera', kg: 'kilogramo', L: 'litro', '°': 'grado' };
const limpia = (t: string) => t.replace(/\\[a-zA-Z]+|[$\\{}_^]/g, ' ');
const palabras = (t: string): string[] => (limpia(t).replace(NUMEROS, ' ').match(/\p{L}{5,}/gu) ?? []).filter((w) => !VACIAS.has(sinTilde(w)));

export interface Concepto { ks: Set<string>; gen: Set<string> }
/** Grupos de sentido común: señalar «colores» abarca todo lo que sea un color. */
const GRUPOS: Record<string, string[]> = { colores: ['rojo', 'azul', 'verde', 'amarillo', 'negro', 'blanco', 'naranja', 'morado', 'gris', 'rosado', 'cafe', 'marron'] };
const POR_ROL: Record<string, string[]> = { dato: ['dato', 'datos'], pide: ['pide', 'piden', 'pregunta', 'preguntan', 'incognita'], trampa: ['ojo', 'trampa'], clave: ['clave'] };
const ENLACE = /^\s*(?:,|y|e|o)\s*$/i;

/** Cada dato del enunciado es un «concepto». Reglas, para no mezclar cosas distintas:
 *  – una marca con UNA cantidad: la cantidad, las palabras del propio fragmento («arranque») y su unidad nombrada («voltios»);
 *  – una marca con VARIAS cantidades: cada cantidad sola (no se arrastran unas a otras);
 *  – una marca sin cantidades (lo que preguntan, una clave): sus palabras y las de su nota («corriente», «amperios»).
 *  Además, lo «genérico» abarca a los datos que lo comparten:
 *  – «3 fichas rojas y 5 azules»: «fichas» sirve a las dos marcas aunque la segunda lo calle;
 *  – «colores» abarca «rojas» y «azules»; «datos» abarca todos los datos; «piden» lo que preguntan. */
export function conceptos(marcas: Marca[] = [], enunciado = ''): Concepto[] {
  const out: (Concepto & { m: Marca; u?: string })[] = [];
  for (const m of marcas) {
    const frag = limpia(m.frag), nums = frag.match(NUMEROS) ?? [];
    if (nums.length > 1) { for (const n of nums) out.push({ ks: new Set([clave(n)]), gen: new Set(), m }); continue; }
    const ks = new Set<string>(); let uni: string | undefined;
    if (nums.length === 1) {
      ks.add(clave(nums[0]));
      for (const w of palabras(m.frag)) ks.add(clave(w));
      const u = frag.match(/\d[\d.,]*\s*(Ω|km|cm|atm|kg|°|V|A|s|h|K|L)(?![\p{L}])/u)?.[1]; if (u && UNIDADES[u]) { uni = clave(UNIDADES[u]); ks.add(uni); }
    } else {
      const nota = (m.nota ?? '').trim().split(/\s+/);
      for (const w of [...palabras(m.frag), ...(nota.length <= 4 ? palabras(m.nota ?? '') : [])]) ks.add(clave(w)); // la nota larga es explicación, no el dato
    }
    if (ks.size) out.push({ ks, gen: new Set(), m, u: uni });
  }
  // Sustantivo compartido por coordinación: «3 fichas rojas y 5 azules».
  const cabeza = (c: Concepto & { m: Marca }): string | null => { const w = limpia(c.m.frag).match(/\d[\d.,]*\s+(?:de\s+)?(\p{L}{4,})/u)?.[1]; return w && !VACIAS.has(sinTilde(w)) ? clave(w) : null; };
  for (const a of out) {
    const na = cabeza(a), ia = enunciado.indexOf(a.m.frag); if (!na || ia < 0) continue;
    for (const b of out) {
      if (a === b || b.ks.has(na) || ![...b.ks].some((k) => k.startsWith('n:'))) continue;
      const ib = enunciado.indexOf(b.m.frag); if (ib < 0) continue;
      const gap = ib >= ia + a.m.frag.length ? enunciado.slice(ia + a.m.frag.length, ib) : null; // el sustantivo va en el primero y el segundo lo calla
      if (gap !== null && ENLACE.test(gap)) { a.gen.add(na); b.gen.add(na); }
    }
  }
  // Una unidad que comparten varios datos («10 cm» y «15 cm») los abarca a todos.
  for (const c of out) if (c.u && out.filter((o) => o.u === c.u).length > 1) c.gen.add(c.u);
  for (const c of out) {
    for (const [g, lista] of Object.entries(GRUPOS)) if (lista.some((w) => c.ks.has(clave(w)))) c.gen.add(clave(g));
    for (const w of POR_ROL[c.m.rol] ?? []) c.gen.add(clave(w));
  }
  return out;
}

type Reg = { set(k: string, v: unknown): void; delete(k: string): void };
const soporta = (): boolean => typeof CSS !== 'undefined' && 'highlights' in CSS && typeof (globalThis as { Highlight?: unknown }).Highlight === 'function';

export function vincularDatos(root: HTMLElement, marcas?: Marca[], enunciado = ''): void {
  if (!soporta()) return;
  const reg = (CSS as unknown as { highlights: Reg }).highlights;
  const Hl = (globalThis as unknown as { Highlight: new (...r: Range[]) => unknown }).Highlight;
  const grupos = conceptos(marcas, enunciado);
  const todas = new Set<string>(grupos.flatMap((g) => [...g.ks, ...g.gen]));
  let fijo: string | null = null, actual: string | null = null;

  /** Todas las claves que se iluminan junto con k.
   *  Un término general («fichas», «colores», «datos») abarca todos los datos que cubre; uno concreto («rojas», «3») solo el suyo. */
  const familia = (k: string): Set<string> => {
    const f = new Set<string>([k]);
    const abarcados = grupos.filter((g) => g.gen.has(k));
    if (abarcados.length) { for (const g of abarcados) g.ks.forEach((x) => f.add(x)); return f; }
    for (const g of grupos) if (g.ks.has(k)) g.ks.forEach((x) => { if (!g.gen.has(x)) f.add(x); });
    return f;
  };

  const textos = (): Text[] => {
    const w = document.createTreeWalker(root, NodeFilter.SHOW_TEXT, { acceptNode: (n) => (n.parentElement?.closest(SALTAR) ? NodeFilter.FILTER_REJECT : NodeFilter.FILTER_ACCEPT) });
    const r: Text[] = []; for (let n = w.nextNode(); n; n = w.nextNode()) r.push(n as Text);
    return r;
  };
  const rangos = (ok: (k: string) => boolean): Range[] => {
    const out: Range[] = [];
    for (const n of textos()) for (const m of n.data.matchAll(TOKEN)) {
      if (!ok(clave(m[0]))) continue;
      const r = document.createRange(); r.setStart(n, m.index!); r.setEnd(n, m.index! + m[0].length); out.push(r);
    }
    return out;
  };
  const pintar = (k: string | null) => {
    if (k === actual) return; actual = k;
    if (!k) { reg.delete('nl-on'); return; }
    const f = familia(k); reg.set('nl-on', new Hl(...rangos((x) => f.has(x))));
  };
  const pista = () => { const r = rangos((k) => todas.has(k)); if (r.length) reg.set('nl-all', new Hl(...r)); else reg.delete('nl-all'); };

  const bajo = (x: number, y: number): string | null => {
    const d = document as Document & { caretPositionFromPoint?: (x: number, y: number) => { offsetNode: Node; offset: number } | null; caretRangeFromPoint?: (x: number, y: number) => Range | null };
    let nodo: Node | null = null, off = 0;
    const cp = d.caretPositionFromPoint?.(x, y); if (cp) { nodo = cp.offsetNode; off = cp.offset; }
    else { const cr = d.caretRangeFromPoint?.(x, y); if (cr) { nodo = cr.startContainer; off = cr.startOffset; } }
    if (!nodo || nodo.nodeType !== 3 || !root.contains(nodo) || (nodo.parentElement?.closest(SALTAR))) return null;
    const t = (nodo as Text).data;
    for (const m of t.matchAll(TOKEN)) {
      const a = m.index!, b = a + m[0].length;
      if (off < a || off > b) continue;
      const k = clave(m[0]); if (!todas.has(k)) return null;
      const r = document.createRange(); r.setStart(nodo, a); r.setEnd(nodo, b);
      const q = r.getBoundingClientRect(); // el puntero debe estar realmente sobre el texto
      if (x >= q.left - 3 && x <= q.right + 3 && y >= q.top - 3 && y <= q.bottom + 3) return k;
    }
    return null;
  };

  root.addEventListener('pointermove', (e) => { if (e.pointerType === 'touch' || fijo) return; pintar(bajo(e.clientX, e.clientY)); });
  root.addEventListener('pointerleave', () => { if (!fijo) pintar(null); });
  root.addEventListener('click', (e) => {
    const k = bajo(e.clientX, e.clientY);
    if (!k || k === fijo) { fijo = null; actual = null; pintar(null); return; }
    fijo = k; actual = null; pintar(k);
  });
  let t = 0;
  new MutationObserver(() => { clearTimeout(t); t = window.setTimeout(() => { pista(); const k = fijo ?? actual; if (k) { actual = null; pintar(k); } }, 250); }).observe(root, { childList: true, subtree: true, characterData: true });
  pista();
}
