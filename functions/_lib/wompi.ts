/** Utilidades Wompi: firmas (Web Crypto, corre en Workers y Node ≥ 18). Sin secretos en código. */
const enc = new TextEncoder();
export async function sha256Hex(s: string): Promise<string> {
  const d = await crypto.subtle.digest('SHA-256', enc.encode(s));
  return [...new Uint8Array(d)].map((b) => b.toString(16).padStart(2, '0')).join('');
}

/** Firma de integridad del checkout: SHA256(<referencia><montoEnCentavos><moneda>[<expiración>]<secretoIntegridad>) */
export const integritySignature = (reference: string, amountCents: number, currency: string, integritySecret: string, expiration?: string) =>
  sha256Hex(`${reference}${amountCents}${currency}${expiration ?? ''}${integritySecret}`);

const getPath = (obj: any, path: string) => path.split('.').reduce((o, k) => (o == null ? undefined : o[k]), obj);

/** Checksum del evento: valores de signature.properties (resueltos en event.data) + timestamp + secreto de eventos. */
export async function eventChecksum(event: any, eventsSecret: string): Promise<string> {
  const props: string[] = event?.signature?.properties ?? [];
  const vals = props.map((p) => String(getPath(event.data, p) ?? '')).join('');
  return sha256Hex(`${vals}${event.timestamp}${eventsSecret}`);
}

export function timingSafeEqual(a: string, b: string): boolean {
  a = a.toLowerCase(); b = b.toLowerCase();
  if (a.length !== b.length) return false;
  let r = 0;
  for (let i = 0; i < a.length; i++) r |= a.charCodeAt(i) ^ b.charCodeAt(i);
  return r === 0;
}

export async function verifyEvent(event: any, eventsSecret: string, headerChecksum?: string | null): Promise<boolean> {
  const expected = await eventChecksum(event, eventsSecret);
  const given = event?.signature?.checksum ?? headerChecksum ?? '';
  return !!given && timingSafeEqual(expected, String(given));
}
