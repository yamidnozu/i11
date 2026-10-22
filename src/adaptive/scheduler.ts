/** Repaso espaciado inspirado en FSRS (simplificado y documentado). */
export interface Card { S: number; due: number; last: number; reps: number }
export const RETENTION = 0.88, FACTOR = 19 / 81, DECAY = -0.5;
export const retrievability = (days: number, S: number) => Math.pow(1 + (FACTOR * days) / S, DECAY);
export const interval = (S: number, maxDays = 90) => Math.min(maxDays, Math.max(1, Math.round((S / FACTOR) * (Math.pow(RETENTION, 1 / DECAY) - 1))));

/** `now` y `examDay` en días. Rating: 1 fallo, 2 difícil, 3 bien, 4 fácil. */
export function review(card: Card | undefined, rating: 1 | 2 | 3 | 4, now: number, examDay?: number): Card {
  const maxD = examDay !== undefined ? Math.max(1, Math.min(90, examDay - 5 - now)) : 90;
  let S = card?.S ?? 1;
  if (!card) S = [0, 0.5, 1, 2, 4][rating];
  else if (rating === 1) S = Math.max(0.3, S * 0.4);
  else S = S * [0, 0, 1.2, 2.2, 3.2][rating] + 0.3;
  const iv = interval(S, maxD);
  return { S, last: now, due: now + iv, reps: (card?.reps ?? 0) + 1 };
}
