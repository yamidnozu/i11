/** Elo con incertidumbre: K(n)=K0/(1+αn). Útil por evidencia entre diagnósticos. */
export const K0 = 0.4, ALPHA = 0.05;
export const B0: Record<number, number> = { 1: -1.5, 2: -0.5, 3: 0.5, 4: 1.5 };
export const pCorrect = (th: number, b: number, c: number) => c + (1 - c) / (1 + Math.exp(-(th - b)));
export function eloUpdate(th: number, n: number, b: number, c: number, correct: boolean) {
  const k = K0 / (1 + ALPHA * n);
  return { theta: th + k * ((correct ? 1 : 0) - pCorrect(th, b, c)), n: n + 1 };
}
