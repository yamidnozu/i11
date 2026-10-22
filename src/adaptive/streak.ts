/** Racha diaria con "congeladores" (máx. 2; se gana uno cada 7 días de racha). */
export interface Streak { count: number; lastDay: number; freezes: number }
export function tick(s: Streak, today: number): Streak {
  if (s.lastDay === today) return s;
  const gap = today - s.lastDay;
  if (gap === 1) { const c = s.count + 1; return { count: c, lastDay: today, freezes: Math.min(2, s.freezes + (c % 7 === 0 ? 1 : 0)) }; }
  const missed = gap - 1;
  if (missed <= s.freezes) return { count: s.count + 1, lastDay: today, freezes: s.freezes - missed };
  return { count: 1, lastDay: today, freezes: s.freezes };
}
