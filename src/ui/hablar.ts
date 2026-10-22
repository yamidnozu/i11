import { numerosAPalabras } from './numeros';
import { EXPLICIT } from './tex';

/** Convierte texto con símbolos y LaTeX en texto para leer en voz alta (español). */
const DIG = ['cero', 'uno', 'dos', 'tres', 'cuatro', 'cinco', 'seis', 'siete', 'ocho', 'nueve'];
const SUB: Record<string, string> = { '₀': '0', '₁': '1', '₂': '2', '₃': '3', '₄': '4', '₅': '5', '₆': '6', '₇': '7', '₈': '8', '₉': '9', 'ᵢ': 'i', 'ₒ': 'o' };
const GR: Record<string, string> = { alpha: 'alfa', beta: 'beta', gamma: 'gamma', delta: 'delta', theta: 'theta', lambda: 'lambda', mu: 'mu', pi: 'pi', rho: 'ro', sigma: 'sigma', omega: 'omega', phi: 'fi', Delta: 'delta' };
const GRU: Record<string, string> = { α: 'alfa', β: 'beta', γ: 'gamma', δ: 'delta', θ: 'theta', λ: 'lambda', μ: 'mu', π: 'pi', σ: 'sigma', ω: 'omega', φ: 'fi' };
const UNITS: [string, string][] = [['atm·L/mol·K', 'atmósferas litro por mol kelvin'], ['m/s²', 'metros por segundo al cuadrado'], ['m/s', 'metros por segundo'], ['km/h', 'kilómetros por hora'], ['°C', 'grados Celsius'], ['cm', 'centímetros'], ['mm', 'milímetros'], ['km', 'kilómetros'], ['kg', 'kilogramos'], ['mol', 'moles'], ['atm', 'atmósferas'], ['Hz', 'hercios'], ['K', 'kelvin'], ['V', 'voltios'], ['A', 'amperios'], ['W', 'vatios'], ['N', 'newtons'], ['J', 'julios'], ['L', 'litros'], ['Ω', 'ohmios'], ['m', 'metros'], ['s', 'segundos'], ['g', 'gramos']];
const subWord = (x: string) => (/^\d$/.test(x) ? DIG[+x] : x);

function latex(s: string): string {
  s = s.replace(/\\[td]frac/g, '\\frac').replace(/\{,\}/g, ',').replace(/\\frac\s*([0-9A-Za-z])\s*([0-9A-Za-z])(?![0-9A-Za-z])/g, '\\frac{$1}{$2}').replace(/\\text\{([^{}]*)\}_\{?(\d+)\}?/g, (_, t, d) => ` ${t} ${[...d].map((c) => DIG[+c]).join(' ')} `).replace(/(?<![\\A-Za-z{])[nRTPVIQWFmgdxyabcAatv]{2,3}(?![A-Za-z}])/g, (m) => ` ${[...m].join(' ')} `).replace(/\//g, ' entre ').replace(/</g, ' menor que ').replace(/>/g, ' mayor que ').replace(/\\text\{\s*\}/g, ' ');
  s = s.replace(/\\[ ,;]|\\q?quad/g, ' ');
  for (let i = 0; i < 6; i++) s = s.replace(/\\frac\{([^{}]*)\}\{([^{}]*)\}/g, ' $1 sobre $2 ').replace(/\\sqrt\{([^{}]*)\}/g, ' raíz de $1 ').replace(/\\(?:text|mathrm)\{([^{}]*)\}/g, ' $1 ').replace(/\\(?:bar|overline)\{([^{}]*)\}/g, ' $1 barra ');
  s = s.replace(/\\frac(\d)\{([^{}]*)\}/g, ' $1 sobre $2 ');
  s = s.replace(/\^\{?\\circ\}?/g, ' grados ').replace(/\\circ/g, ' grados ').replace(/\^\{?\*\}?/g, ' asterisco ').replace(/\^\{?2\}?/g, ' al cuadrado ').replace(/\^\{?3\}?/g, ' al cubo ').replace(/\^\{([^{}]*)\}/g, ' elevado a $1 ').replace(/\^(\w)/g, ' elevado a $1 ');
  s = s.replace(/_\{([^{}]*)\}/g, (_, x) => ` sub ${[...x].map(subWord).join(' ')} `).replace(/_(\w)/g, (_, x) => ` sub ${subWord(x)} `);
  s = s.replace(/\\(cdot|times)(?![A-Za-z])/g, ' por ').replace(/\\div(?![A-Za-z])/g, ' entre ').replace(/\\approx(?![A-Za-z])/g, ' aproximadamente ').replace(/\\(?:Rightarrow|rightarrow|to)(?![A-Za-z])/g, ' entonces ').replace(/\\neq(?![A-Za-z])/g, ' distinto de ').replace(/\\leq?(?![A-Za-z])/g, ' menor o igual que ').replace(/\\geq?(?![A-Za-z])/g, ' mayor o igual que ').replace(/\\pm(?![A-Za-z])/g, ' más menos ')
    .replace(/\\sin(?![A-Za-z])/g, ' seno de ').replace(/\\cos(?![A-Za-z])/g, ' coseno de ').replace(/\\tan(?![A-Za-z])/g, ' tangente de ').replace(/\\ln(?![A-Za-z])/g, ' logaritmo natural de ').replace(/\\Omega(?![A-Za-z])/g, ' ohmios ').replace(/\\%/g, ' por ciento ')
    .replace(/\\([A-Za-z]+)/g, (_, n) => ` ${GR[n] ?? n} `);
  return s.replace(/-/g, ' menos ').replace(/[{}]/g, ' ').replace(/\)\s*\(/g, ' por ').replace(/[()]/g, ' ');
}

function unid(s: string): string {
  for (const [u, w] of UNITS) s = s.replace(new RegExp(`(\\d)\\s*${u.replace(/[.*+?^${}()|[\]\\/·]/g, '\\$&')}(?![A-Za-zÀ-ÿ²³])(?:\\^2|\\^\\{2\\})?`, 'g'), (m, d) => `${d} ${w}${/\^/.test(m) ? ' al cuadrado' : ''}`);
  return s;
}

function simbolos(s: string): string {
  s = unid(s.replace(/\$(\d[\d.]*)/g, '$1 pesos'));
  s = s.replace(/\b((?:[A-Z][a-z]?[₀-₉]*){2,}|[A-Z][a-z]?[₀-₉]+)(?![A-Za-zÀ-ÿ])/g, (m) => (/[₀-₉]/.test(m) || /^(?:[A-Z][a-z]?){2,}$/.test(m) && /^(CO|HO|NO|OH|CH|HCl|NaCl)$/.test(m) ? m.replace(/([A-Z][a-z]?)([₀-₉]*)/g, (_, e, d) => ` ${e} ${[...d].map((c) => DIG[+SUB[c]]).join(' ')} `) : m));
  s = s.replace(/([A-Za-zα-ωθ])([₀-₉ᵢₒ]+)/g, (_, v, d) => `${v} sub ${[...d].map((c) => subWord(SUB[c])).join(' ')} `).replace(/²/g, ' al cuadrado ').replace(/³/g, ' al cubo ');
  s = s.replace(/[α-ωθ]/g, (c) => ` ${GRU[c] ?? c} `);
  s = s.replace(/°/g, ' grados ').replace(/%/g, ' por ciento ').replace(/→|⇒/g, ' entonces ').replace(/↔/g, ' si y solo si ').replace(/≈/g, ' aproximadamente ').replace(/≠/g, ' distinto de ').replace(/≤/g, ' menor o igual que ').replace(/≥/g, ' mayor o igual que ')
    .replace(/[·×]/g, ' por ').replace(/÷/g, ' entre ').replace(/=/g, ' igual a ').replace(/\+/g, ' más ').replace(/[−–](?=\s?\d|\s?[a-zA-Z(])/g, (m, i, all) => (/\d$/.test(all.slice(Math.max(0, i - 2), i)) && /^\d{4}/.test(all.slice(i + 1)) ? ' a ' : ' menos '))
    .replace(/(\d)\/(\d)/g, '$1 sobre $2').replace(/(?<=\w)\/(?=\w)/g, ' o ');
  return s;
}

const DICT: [RegExp, string][] = [[/(?<![\w/])m\/s(?![\w/])/g, 'metros por segundo'], [/\bPunnett\b/g, 'Pánet'], [/\bOhm\b/g, 'Om'], [/\ba\. ?m\./gi, 'de la mañana'], [/\bp\. ?m\./gi, 'de la tarde'], [/(\d):(\d)/g, '$1 a $2'], [/\bpH\b/g, 'pe ache'], [/\bADN\b/g, 'a de ene'], [/\bICFES\b/g, 'Icfes'], [/\bSaber 11\b/g, 'Saber once']];
function hablarEs(t: string): string {
  const base = t.split(new RegExp(`(${EXPLICIT})`)).map((p, k) => (k % 2 ? simbolos(latex(unid(p.slice(1, -1).replace(/\\text\{([^{}]*)\}_\{?(\d+)\}?/g, (_: string, x: string, d: string) => ` ${[...x].join(' ')} ${[...d].map((c) => DIG[+c]).join(' ')} `).replace(/\\text\{([^{}]*)\}/g, ' $1 ').replace(/\bm\/s\b/g, ' metros por segundo ').replace(/\\[ ,;]/g, ' ').replace(/\{,\}/g, ',')))) : simbolos(p))).join(' ').replace(/\*\*/g, '').replace(/[«»]/g, '"');
  return DICT.reduce((x, [r, w]) => x.replace(r, w), base).replace(/\s+([.,;:!?])/g, '$1').replace(/\s+/g, ' ').trim();
}
/** Texto hablado. Lo que va entre {{ }} es inglés y se conserva tal cual para que la voz lo lea en inglés. */
export const hablar = (t: string): string => t.split(/(\{\{.+?\}\})/).map((p) => (/^\{\{/.test(p) ? p : numerosAPalabras(hablarEs(p)))).join(' ').replace(/\s+([.,;:!?])/g, '$1').replace(/\s+/g, ' ').trim();
