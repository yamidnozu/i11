/** Navegación por hash que además funciona donde el hash no se puede escribir (vistas incrustadas). */
let cur = '/';
let suppress = false;
let onChange: () => void = () => {};

const norm = (p: string) => { const s = p.replace(/^#/, ''); return s.startsWith('/') ? s : '/' + s; };
export const current = () => cur.split('?')[0];
export const query = () => new URLSearchParams(cur.split('?')[1] ?? '');
export function go(path: string) {
  cur = norm(path);
  try { if (location.hash !== '#' + cur) { suppress = true; location.hash = cur; setTimeout(() => (suppress = false), 120); } } catch { /* sin acceso al hash */ }
  onChange();
}
export function initNav(cb: () => void) {
  onChange = cb;
  try { cur = norm(location.hash || '/'); } catch { cur = '/'; }
  addEventListener('hashchange', () => { if (suppress) { suppress = false; return; } try { cur = norm(location.hash || '/'); } catch { /* */ } cb(); });
  document.addEventListener('click', (e) => {
    const a = (e.target as HTMLElement).closest?.('a[href^="#/"]') as HTMLAnchorElement | null;
    if (!a || e.defaultPrevented || e.metaKey || e.ctrlKey || e.shiftKey || e.button !== 0 || a.target) return;
    e.preventDefault(); go(a.getAttribute('href')!);
  });
}
