import { AREAS, AREA_IDS, type AreaId } from '../adaptive/areas';

/** Radar de las cinco áreas en estilo plano: tu puntaje frente a la media nacional. */
export function radar(sc: Partial<Record<AreaId, number>>): string {
  const S = 460, C = S / 2, R = 150, n = AREA_IDS.length;
  const ang = (i: number) => -Math.PI / 2 + (i * 2 * Math.PI) / n;
  const pt = (i: number, v: number) => `${(C + Math.cos(ang(i)) * R * (v / 100)).toFixed(1)},${(C + Math.sin(ang(i)) * R * (v / 100)).toFixed(1)}`;
  const poly = (f: (a: AreaId) => number) => AREA_IDS.map((a, i) => pt(i, f(a))).join(' ');
  const rings = [25, 50, 75, 100].map((v) => `<polygon points="${poly(() => v)}" fill="none" stroke="currentColor" stroke-opacity="${v === 100 ? 0.55 : 0.22}" stroke-width="1"/>`).join('');
  const spokes = AREA_IDS.map((_, i) => `<line x1="${C}" y1="${C}" x2="${pt(i, 100).split(',')[0]}" y2="${pt(i, 100).split(',')[1]}" stroke="currentColor" stroke-opacity=".25"/>`).join('');
  const labels = AREA_IDS.map((a, i) => {
    const x = C + Math.cos(ang(i)) * (R + 30), y = C + Math.sin(ang(i)) * (R + 26), anchor = Math.cos(ang(i)) > 0.3 ? 'start' : Math.cos(ang(i)) < -0.3 ? 'end' : 'middle';
    const words = AREAS[a].nombre.split(' '), l1 = words.slice(0, Math.ceil(words.length / 2)).join(' '), l2 = words.slice(Math.ceil(words.length / 2)).join(' ');
    return `<text x="${x.toFixed(1)}" y="${y.toFixed(1)}" text-anchor="${anchor}" font-size="13" fill="currentColor" font-weight="600">${l1}${l2 ? `<tspan x="${x.toFixed(1)}" dy="15">${l2}</tspan>` : ''}</text>`;
  }).join('');
  const ticks = [25, 50, 75].map((v) => `<text x="${C + 4}" y="${(C - R * (v / 100) + 11).toFixed(1)}" font-size="10" fill="currentColor" fill-opacity=".6" font-family="IBM Plex Mono,monospace">${v}</text>`).join('');
  const has = AREA_IDS.some((a) => sc[a] !== undefined);
  const mine = has ? `<polygon points="${poly((a) => sc[a] ?? 0)}" fill="var(--acc)" fill-opacity=".22" stroke="var(--acc)" stroke-width="2.6" stroke-linejoin="round"/>` + AREA_IDS.map((a, i) => (sc[a] === undefined ? '' : `<circle cx="${pt(i, sc[a]!).split(',')[0]}" cy="${pt(i, sc[a]!).split(',')[1]}" r="5" fill="var(--acc)" stroke="var(--panel)" stroke-width="2"/>`)).join('') : `<text x="${C}" y="${C + 4}" text-anchor="middle" font-size="15" fill="currentColor" font-family="Newsreader,Georgia,serif" font-style="italic" font-weight="600">haz el diagnóstico para dibujar tu radar</text>`;
  return `<svg viewBox="0 0 ${S} ${S}" role="img" aria-label="Radar de puntajes por área frente a la media nacional" font-family="IBM Plex Sans,system-ui,sans-serif">${rings}${spokes}<polygon points="${poly((a) => AREAS[a].mu)}" fill="none" stroke="currentColor" stroke-opacity=".55" stroke-width="2" stroke-dasharray="6 5"/>${ticks}${mine}${labels}</svg>`;
}
