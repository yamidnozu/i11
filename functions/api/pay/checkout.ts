import { integritySignature } from '../../_lib/wompi';
import { json, PRICE_CENTS_DEFAULT, type Env } from '../../_lib/env';

/** El servidor decide el monto y la referencia; el cliente nunca los fija. */
export const onRequestPost: PagesFunction<Env> = async ({ request, env }) => {
  const body = (await request.json().catch(() => ({}))) as { uid?: string; email?: string; guardianConsent?: boolean; minor?: boolean };
  if (!body.uid || !/^[\w-]{8,64}$/.test(body.uid)) return json({ error: 'uid inválido' }, 400);
  if (body.minor && !body.guardianConsent) return json({ error: 'Se requiere autorización del acudiente' }, 400);
  const amount = Number(env.PRICE_CENTS ?? PRICE_CENTS_DEFAULT);
  const reference = `S11-${crypto.randomUUID()}`;
  await env.DB.prepare('INSERT INTO orders (reference,uid,amount_cents,status,created_at) VALUES (?,?,?,?,?)').bind(reference, body.uid, amount, 'PENDING', Date.now()).run();
  if (body.minor) await env.DB.prepare('INSERT INTO consents (uid,kind,created_at) VALUES (?,?,?)').bind(body.uid, 'guardian_payment', Date.now()).run();
  const signature = await integritySignature(reference, amount, 'COP', env.WOMPI_INTEGRITY_SECRET);
  return json({ publicKey: env.WOMPI_PUBLIC_KEY, currency: 'COP', amountInCents: amount, reference, signature, redirectUrl: `${env.SITE_URL}/#/pago/resultado` });
};
