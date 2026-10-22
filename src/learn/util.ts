export const rad = (d: number) => (d * Math.PI) / 180;
export const deg = (r: number) => (r * 180) / Math.PI;
/** Número con coma decimal (es-CO) para textos y fórmulas. */
export const n = (x: number, d = 2) => (Number.isFinite(x) ? (+x.toFixed(d)).toString().replace('.', ',') : '—');
export const near = (a: number, b: number, tol: number) => Math.abs(a - b) <= tol;
