import { describe, it, expect } from 'vitest';
import { integritySignature, eventChecksum, verifyEvent, sha256Hex, timingSafeEqual } from '../functions/_lib/wompi';

describe('Wompi', () => {
  it('SHA-256 conocido', async () => expect(await sha256Hex('abc')).toBe('ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad'));
  it('firma de integridad = SHA256(ref+monto+moneda+secreto)', async () => {
    expect(await integritySignature('R1', 2990000, 'COP', 'sec')).toBe(await sha256Hex('R12990000COPsec'));
    expect(await integritySignature('R1', 2990000, 'COP', 'sec', '2030-01-01T00:00:00.000Z')).toBe(await sha256Hex('R12990000COP2030-01-01T00:00:00.000Zsec'));
  });
  const ev = { event: 'transaction.updated', data: { transaction: { id: 'T1', status: 'APPROVED', amount_in_cents: 2990000 } }, timestamp: 1530291411, signature: { properties: ['transaction.id', 'transaction.status', 'transaction.amount_in_cents'], checksum: '' } };
  it('checksum del evento y verificación', async () => {
    const ck = await sha256Hex('T1APPROVED2990000' + '1530291411' + 'evsec');
    expect(await eventChecksum(ev, 'evsec')).toBe(ck);
    expect(await verifyEvent({ ...ev, signature: { ...ev.signature, checksum: ck.toUpperCase() } }, 'evsec')).toBe(true);
    expect(await verifyEvent({ ...ev, signature: { ...ev.signature, checksum: ck } }, 'otro')).toBe(false);
    expect(await verifyEvent({ ...ev, data: { transaction: { ...ev.data.transaction, status: 'DECLINED' } }, signature: { ...ev.signature, checksum: ck } }, 'evsec')).toBe(false);
  });
  it('comparación segura', () => { expect(timingSafeEqual('aB', 'Ab')).toBe(true); expect(timingSafeEqual('a', 'ab')).toBe(false); });
});
