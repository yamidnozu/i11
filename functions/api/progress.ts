import { json, type Env } from '../_lib/env';
/** Sincroniza progreso (documento JSON por uid). Datos mínimos; sin PII. */
export const onRequestGet: PagesFunction<Env> = async ({ request, env }) => {
  const uid = new URL(request.url).searchParams.get('uid') ?? '';
  const row = await env.DB.prepare('SELECT data,updated_at FROM progress WHERE uid=?').bind(uid).first<any>();
  return json(row ? { data: JSON.parse(row.data), updated_at: row.updated_at } : { data: null });
};
export const onRequestPut: PagesFunction<Env> = async ({ request, env }) => {
  const b = (await request.json().catch(() => null)) as { uid?: string; data?: unknown } | null;
  if (!b?.uid || !/^[\w-]{8,64}$/.test(b.uid) || !b.data) return json({ error: 'datos inválidos' }, 400);
  const s = JSON.stringify(b.data);
  if (s.length > 200_000) return json({ error: 'muy grande' }, 413);
  await env.DB.prepare('INSERT INTO progress (uid,data,updated_at) VALUES (?,?,?) ON CONFLICT(uid) DO UPDATE SET data=excluded.data, updated_at=excluded.updated_at').bind(b.uid, s, Date.now()).run();
  return json({ ok: true });
};
