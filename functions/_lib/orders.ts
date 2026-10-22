import type { Env } from './env';

/** Idempotente: solo pasa a APPROVED una vez y concede 12 meses de acceso. */
export async function applyTransaction(env: Env, tx: { id: string; reference: string; status: string; amount_in_cents: number }) {
  const ins = await env.DB.prepare('INSERT OR IGNORE INTO payment_events (tx_id,status,reference,created_at) VALUES (?,?,?,?)')
    .bind(tx.id, tx.status, tx.reference, Date.now()).run();
  const order = await env.DB.prepare('SELECT reference,uid,amount_cents,status FROM orders WHERE reference=?').bind(tx.reference).first<any>();
  if (!order) return { ok: false, reason: 'orden desconocida' };
  if (tx.amount_in_cents !== order.amount_cents) return { ok: false, reason: 'monto no coincide' };
  if (tx.status === 'APPROVED') {
    const upd = await env.DB.prepare("UPDATE orders SET status='APPROVED', tx_id=? WHERE reference=? AND status != 'APPROVED'").bind(tx.id, tx.reference).run();
    if (upd.meta.changes) {
      const until = Date.now() + 365 * 24 * 3600 * 1000;
      await env.DB.prepare('INSERT INTO entitlements (uid,until) VALUES (?,?) ON CONFLICT(uid) DO UPDATE SET until=MAX(until, excluded.until)').bind(order.uid, until).run();
    }
  } else if (['DECLINED', 'VOIDED', 'ERROR'].includes(tx.status)) {
    await env.DB.prepare("UPDATE orders SET status=? WHERE reference=? AND status='PENDING'").bind(tx.status, tx.reference).run();
  }
  return { ok: true, dup: !ins.meta.changes };
}
