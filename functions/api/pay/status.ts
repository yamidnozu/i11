import { applyTransaction } from '../../_lib/orders';
import { json, type Env } from '../../_lib/env';

/** Consulta a Wompi con la llave privada (la fuente de verdad es Wompi, no la URL de retorno). */
export const onRequestGet: PagesFunction<Env> = async ({ request, env }) => {
  const id = new URL(request.url).searchParams.get('id');
  if (!id || !/^[\w-]{4,64}$/.test(id)) return json({ error: 'id inválido' }, 400);
  const r = await fetch(`${env.WOMPI_API}/transactions/${id}`, { headers: { Authorization: `Bearer ${env.WOMPI_PRIVATE_KEY}` } });
  if (!r.ok) return json({ error: 'no se pudo consultar' }, 502);
  const tx = ((await r.json()) as any).data;
  const res = await applyTransaction(env, tx);
  return json({ status: tx.status, ...res });
};
