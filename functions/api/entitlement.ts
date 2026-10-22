import { json, type Env } from '../_lib/env';
export const onRequestGet: PagesFunction<Env> = async ({ request, env }) => {
  const uid = new URL(request.url).searchParams.get('uid') ?? '';
  const row = await env.DB.prepare('SELECT until FROM entitlements WHERE uid=?').bind(uid).first<{ until: number }>();
  return json({ active: !!row && row.until > Date.now(), until: row?.until ?? null });
};
