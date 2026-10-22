type Child = Node | string | number | null | undefined | false | Child[];

export function h<K extends keyof HTMLElementTagNameMap>(
  tag: K,
  props: Record<string, any> = {},
  ...children: Child[]
): HTMLElementTagNameMap[K] {
  const e = document.createElement(tag);
  for (const [k, v] of Object.entries(props)) {
    if (v == null || v === false) continue;
    if (k === 'class') e.className = v;
    else if (k.startsWith('on') && typeof v === 'function') e.addEventListener(k.slice(2).toLowerCase(), v);
    else if (k === 'html') e.innerHTML = v;
    else if (v === true) e.setAttribute(k, '');
    else e.setAttribute(k, String(v));
  }
  const add = (c: Child) => {
    if (c == null || c === false) return;
    if (Array.isArray(c)) c.forEach(add);
    else e.append(c instanceof Node ? c : document.createTextNode(String(c)));
  };
  children.forEach(add);
  return e;
}

export const fmt = (v: number): string => {
  if (!Number.isFinite(v)) return '—';
  const s = Math.abs(v) >= 100 ? v.toFixed(1) : v.toFixed(3);
  return s.replace(/\.?0+$/, '').replace('.', ',');
};
