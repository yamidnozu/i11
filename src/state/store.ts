import { eap, type Item } from '../adaptive/irt';
import { B0 } from '../adaptive/elo';
import { areaScore, areaSE, globalScore, globalSE } from '../adaptive/score';
import { AREA_IDS, type AreaId } from '../adaptive/areas';
import { tick, type Streak } from '../adaptive/streak';
import { review, type Card } from '../adaptive/scheduler';
import type { Question } from '../content/schema';
import { QUESTIONS } from '../content';

export interface Answer { qid: string; ok: boolean; day: number; mode: 'diag' | 'prac' | 'sim' }
export interface Data { uid: string; answers: Answer[]; cards: Record<string, Card>; streak: Streak; examDay?: number; paid?: boolean; minor?: boolean; seen?: Record<string, number> }

const KEY = 'saber11.v1';
export const day = () => Math.floor(Date.now() / 86400000);
const mem: { d?: Data } = {};
const uid = () => 'u' + (crypto.randomUUID?.() ?? String(Math.random()).slice(2)).replace(/-/g, '').slice(0, 24);

export function load(): Data {
  if (mem.d) return mem.d;
  try { const s = localStorage.getItem(KEY); if (s) return (mem.d = JSON.parse(s)); } catch { /* sin almacenamiento */ }
  return (mem.d = { uid: uid(), answers: [], cards: {}, streak: { count: 0, lastDay: 0, freezes: 1 } });
}
export function save() { try { localStorage.setItem(KEY, JSON.stringify(mem.d)); } catch { /* ignorar */ } }

export const itemOf = (q: Question): Item => ({ b: B0[q.nivel], c: 1 / Math.max(2, q.opciones.length || 4) });

export function record(q: Question, ok: boolean, mode: Answer['mode']) {
  const d = load();
  d.answers.push({ qid: q.id, ok, day: day(), mode });
  d.streak = tick(d.streak, day());
  d.cards[q.id] = review(d.cards[q.id], ok ? 3 : 1, day(), d.examDay);
  save();
}

export function thetaOf(area: AreaId, modes?: Answer['mode'][]) {
  const rs = load().answers.filter((a) => (!modes || modes.includes(a.mode))).map((a) => ({ a, q: QUESTIONS.find((x) => x.id === a.qid)! })).filter((x) => x.q && x.q.area === area && x.q.tipo !== 'reto');
  if (!rs.length) return null;
  return { ...eap(rs.map((x) => ({ item: itemOf(x.q), correct: x.a.ok }))), n: rs.length };
}

export function summary() {
  const sc: Partial<Record<AreaId, number>> = {}, se: Partial<Record<AreaId, number>> = {}, n: Partial<Record<AreaId, number>> = {};
  for (const a of AREA_IDS) { const t = thetaOf(a); if (t) { sc[a] = areaScore(a, t.theta); se[a] = areaSE(a, t.se); n[a] = t.n; } }
  return { sc, se, n, global: globalScore(sc), gse: globalSE(se) };
}
export const touch = (k: string) => { const d = load(); (d.seen ??= {})[k] = day(); save(); };
export const seen = (k: string) => !!load().seen?.[k];
export const dueCards = () => Object.entries(load().cards).filter(([, c]) => c.due <= day()).map(([id]) => id);

/** El diagnóstico es gratis; el resto requiere acceso (o modo libre en desarrollo). */
export const FREE_MODE = (import.meta as any).env?.VITE_FREE_MODE === '1';
/** Todo el contenido es gratis para todos. */
export const hasAccess = () => true;
/** Lo único de pago: la plataforma personalizada con paletas de color. */
export const hasPremium = () => FREE_MODE || !!load().paid;
export async function refreshEntitlement() {
  try { const r = await fetch(`/api/entitlement?uid=${load().uid}`); if (r.ok) { load().paid = (await r.json()).active; save(); } } catch { /* offline */ }
}
let timer: any;
export function syncSoon() {
  clearTimeout(timer);
  timer = setTimeout(() => { fetch('/api/progress', { method: 'PUT', headers: { 'content-type': 'application/json' }, body: JSON.stringify({ uid: load().uid, data: { answers: load().answers.slice(-500), streak: load().streak } }) }).catch(() => {}); }, 3000);
}
