import { verifyEvent } from '../../_lib/wompi';
import { applyTransaction } from '../../_lib/orders';
import { json, type Env } from '../../_lib/env';

export const onRequestPost: PagesFunction<Env> = async ({ request, env }) => {
  const event: any = await request.json().catch(() => null);
  if (!event || !(await verifyEvent(event, env.WOMPI_EVENTS_SECRET, request.headers.get('X-Event-Checksum')))) return json({ error: 'firma inválida' }, 401);
  if (event.event === 'transaction.updated' && event.data?.transaction) await applyTransaction(env, event.data.transaction);
  return json({ ok: true });
};
