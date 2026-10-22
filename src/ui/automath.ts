import { tex, EXPLICIT } from './tex';
/** Parte un texto en átomos: números, unidades, fracciones, fórmulas y variables se tipografían como matemática. */
export interface Atom { raw: string; html: string; start: number; end: number; math: boolean; space: boolean }

const ESC = (s: string) => s.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
const SUBS = '₀₁₂₃₄₅₆₇₈₉ᵢₒ';
const SUBMAP: Record<string, string> = { '₀': '0', '₁': '1', '₂': '2', '₃': '3', '₄': '4', '₅': '5', '₆': '6', '₇': '7', '₈': '8', '₉': '9', 'ᵢ': 'i', 'ₒ': 'o' };
const GR: Record<string, string> = { α: '\\alpha', β: '\\beta', γ: '\\gamma', δ: '\\delta', θ: '\\theta', λ: '\\lambda', μ: '\\mu', π: '\\pi', ρ: '\\rho', σ: '\\sigma', ω: '\\omega', φ: '\\phi' };
const UNITS = 'm/s²|m/s|km/h|mol|atm|cm|mm|km|kg|Hz|°C|Ω|m|s|V|A|K|L|W|N|J|g';
const NUM = '(?<![\\w.,])[−-]?\\d{1,3}(?:\\.\\d{3})+(?:,\\d+)?|(?<![\\w.,])[−-]?\\d+(?:[.,]\\d+)?';
const OPN = `(?:\\d+/\\d+|${NUM})(?:\\s?(?:${UNITS})(?![A-Za-zÀ-ÿ²³]))?`;
const OPV = '(?<![A-Za-zÀ-ÿ\\d])[a-z](?![A-Za-zÀ-ÿ\\d])';
const OPR = '\\s?(?:[×÷·+=≈]|(?<=[\\w%°²\\s])−)\\s?';
const EXPR = `(?:${OPN}|(?<![A-Za-zÀ-ÿ\\d])[A-Za-z](?=\\s?=))(?:${OPR}(?:${OPN}|${OPV}))+`;
const EXPR_RE = new RegExp(`^(?:${EXPR})$`);
const RX = new RegExp([
  EXPLICIT,
  EXPR,
  `(?<![A-Za-z])(?=[A-Za-z${SUBS}]*[${SUBS}])(?:[A-Z][a-z]?[${SUBS}]*)+`,
  `[A-Za-zα-ωθ][${SUBS}²³]+`,
  `(?:${NUM})\\s?(?:${UNITS})(?![A-Za-zÀ-ÿ²³])`,
  `(?:${NUM})\\s?[%°]`,
  '\\d+/\\d+',
  NUM,
].map((p) => `(?:${p})`).join('|'), 'gu');

const tx = (s: string) => s.replace(/[α-ωθ]/g, (c) => (GR[c] ? GR[c] + ' ' : c)).replace(/[²³]/g, (c) => `^{${c === '²' ? 2 : 3}}`).replace(new RegExp(`[${SUBS}]+`, 'g'), (c) => `_{${[...c].map((x) => SUBMAP[x]).join('')}}`);

const OPT: Record<string, string> = { '×': '\\times', '÷': '÷', '·': '\\cdot', '+': '+', '=': '=', '≈': '\\approx', '−': '-' };
function toTex(m: string): string {
  if (m.startsWith('$')) return m.slice(1, -1);
  if (!/^\d+\/\d+$/.test(m) && EXPR_RE.test(m)) return m.split(/\s?([×÷·+=≈]|(?<=[\w%°²\s])−)\s?/).map((x, k) => (k % 2 ? `\\;${OPT[x]}\\;` : toTex(x.trim()))).join('');
  if (/^\d+\/\d+$/.test(m)) { const [a, b] = m.split('/'); return `\\frac{${a}}{${b}}`; }
  if (/^[A-Z]/.test(m) && new RegExp(`[${SUBS}]`).test(m) && /^(?:[A-Z][a-z]?[₀-₉ᵢₒ]*)+$/.test(m)) return (m.match(new RegExp(`[A-Z][a-z]?[${SUBS}]*`, 'g')) ?? []).map((e) => { const el = e.match(/^[A-Z][a-z]?/)![0]; const sb = e.slice(el.length); return `\\text{${el}}${sb ? `_{${[...sb].map((x) => SUBMAP[x]).join('')}}` : ''}`; }).join('');
  if (new RegExp(`^[A-Za-zα-ωθ][${SUBS}²³]+$`).test(m)) return tx(m);
  const q = m.match(new RegExp(`^(${NUM})\\s?(${UNITS})$`));
  if (q) { const u = q[2]; const sup = u.endsWith('²') ? '^{2}' : ''; return `${q[1]}\\,\\text{${u.replace('²', '')}}${sup}`; }
  if (/[%]$/.test(m)) return `${m.replace(/\s?%$/, '')}\\,\\%`;
  if (/°$/.test(m)) return `${m.replace(/\s?°$/, '')}^\\circ`;
  return m;
}

export function atomize(text: string): Atom[] {
  const out: Atom[] = [];
  const plain = (s: string, base: number) => {
    for (const w of s.match(/\s+|[^\s]+/g) ?? []) {
      const start = base + (out.length ? 0 : 0);
      void start;
      out.push({ raw: w, html: ESC(w), start: 0, end: 0, math: false, space: /^\s+$/.test(w) });
    }
  };
  let p = 0;
  const seg = (s: string) => { const first = out.length; plain(s, 0); let o = p; for (let k = first; k < out.length; k++) { out[k].start = o; o += out[k].raw.length; out[k].end = o; } };
  for (const m of text.matchAll(RX)) {
    const i = m.index!;
    if (i > p) { seg(text.slice(p, i)); p = i; }
    out.push({ raw: m[0], html: tex(toTex(m[0])), start: i, end: i + m[0].length, math: true, space: false });
    p = i + m[0].length;
  }
  if (p < text.length) seg(text.slice(p));
  return out;
}

export const mx = (text: string): string => atomize(text).map((a) => a.html).join('');

import { setAutoMath } from './tex';
setAutoMath(mx);
