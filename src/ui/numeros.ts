/** Números en palabras (español de Colombia) para que la voz diga "cuatro mil" y no "cuatro cero cero cero". */
const U = ['cero', 'uno', 'dos', 'tres', 'cuatro', 'cinco', 'seis', 'siete', 'ocho', 'nueve', 'diez', 'once', 'doce', 'trece', 'catorce', 'quince', 'dieciséis', 'diecisiete', 'dieciocho', 'diecinueve', 'veinte', 'veintiuno', 'veintidós', 'veintitrés', 'veinticuatro', 'veinticinco', 'veintiséis', 'veintisiete', 'veintiocho', 'veintinueve'];
const D = ['', '', '', 'treinta', 'cuarenta', 'cincuenta', 'sesenta', 'setenta', 'ochenta', 'noventa'];
const C = ['', 'ciento', 'doscientos', 'trescientos', 'cuatrocientos', 'quinientos', 'seiscientos', 'setecientos', 'ochocientos', 'novecientos'];
const MASC = /^(metros?|kil[oó]metros?|segundos?|voltios?|amperios?|litros?|mol(es)?|grados?|pesos|dados?|puntos?|casos?|d[ií]as?|meses|a[nñ]os?|[aá]tomos?|gramos?|libros?|estudiantes?|resultados?|datos?|fichas?)$/i;
function bajo(n: number, apocope: boolean): string {
  if (n < 30) return n === 1 && apocope ? 'un' : n === 21 && apocope ? 'veintiún' : U[n];
  if (n < 100) { const d = Math.floor(n / 10), u = n % 10; return u ? `${D[d]} y ${bajo(u, apocope)}` : D[d]; }
  if (n === 100) return 'cien';
  const c = Math.floor(n / 100), r = n % 100;
  return r ? `${C[c]} ${bajo(r, apocope)}` : C[c];
}
export function enPalabras(n: number, apocope = false): string {
  if (n < 1000) return bajo(n, apocope);
  if (n < 1e6) { const m = Math.floor(n / 1000), r = n % 1000; return `${m === 1 ? 'mil' : `${bajo(m, true)} mil`}${r ? ' ' + bajo(r, apocope) : ''}`; }
  const m = Math.floor(n / 1e6), r = n % 1e6;
  return `${m === 1 ? 'un millón' : `${enPalabras(m, true)} millones`}${r ? ' ' + enPalabras(r, apocope) : ''}`;
}
const ENT = (s: string) => Number(s.replace(/\./g, ''));
/** Reemplaza cada número escrito con cifras (1.000, 4.500,50, 0,082, 273) por su lectura en palabras. */
export function numerosAPalabras(t: string): string {
  t = t.replace(/\d+(?:,\d+){2,}/g, (m) => m.replace(/,/g, ', ')); // lista: 2,3,3,4
  t = t.replace(/(?<![\p{L}\d.,_^])(\d{1,2})(?=[a-z](?![\p{L}\d]))/gu, (_, d: string) => enPalabras(Number(d)) + ' ');
  return t.replace(/(?<![\p{L}\d.,_^])(\d{1,3}(?:\.\d{3})+|\d+)(?:,(\d+))?(?![\p{L}\d_]|[.,]\d)(\s+[\p{L}]+)?/gu, (m, e: string, dec: string | undefined, sig: string | undefined) => {
    const n = ENT(e);
    if (n > 999999999) return m;
    const nombre = sig?.trim();
    const ap = !dec && !!nombre && MASC.test(nombre);
    let out = enPalabras(n, ap);
    if (dec) { const z = dec.match(/^0*/)![0].length; out += ' coma ' + Array(z).fill('cero').join(' ') + (dec.length > z ? (z ? ' ' : '') + enPalabras(Number(dec)) : ''); }
    return out + (sig ?? '');
  });
}
