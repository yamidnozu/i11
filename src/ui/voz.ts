/** Voz del profe: Web Speech API del dispositivo. Sin voz disponible, el ritmo se calcula por la longitud del texto. */
export interface VozCfg { on: boolean; rate: number; name: string; en: string; enRate: number }
const KEY = 'saber11.voz';
const load = (): VozCfg => { try { return { on: true, rate: 0.95, name: '', en: '', enRate: 0.85, ...JSON.parse(localStorage.getItem(KEY) ?? '{}') }; } catch { return { on: true, rate: 0.95, name: '', en: '', enRate: 0.85 }; } };
export const cfg: VozCfg = load();
export const guardar = () => { try { localStorage.setItem(KEY, JSON.stringify(cfg)); } catch { /* sin almacenamiento */ } };
const ss = (): SpeechSynthesis | null => (typeof speechSynthesis !== 'undefined' ? speechSynthesis : null);

export const voces = (l = 'es'): SpeechSynthesisVoice[] => (ss()?.getVoices() ?? []).filter((v) => new RegExp(`^${l}`, 'i').test(v.lang));
const PREF = ['es-CO', 'es-MX', 'es-US', 'es-419', 'es-AR', 'es-PE', 'es-CL', 'es-ES'];
export function mejorVoz(l = 'es'): SpeechSynthesisVoice | null {
  const vs = voces(l); if (!vs.length) return null;
  if (l !== 'es') { const by = cfg.en ? vs.find((v) => v.name === cfg.en) : null; if (by) return by; }
  if (l !== 'es') return [...vs].sort((a, b) => Number(/natural|neural|online|google/i.test(b.name)) + Number(/en[-_]US/i.test(b.lang)) - Number(/natural|neural|online|google/i.test(a.name)) - Number(/en[-_]US/i.test(a.lang)))[0];
  const by = vs.find((v) => v.name === cfg.name); if (by) return by;
  const score = (v: SpeechSynthesisVoice) => (/natural|neural|online|google/i.test(v.name) ? 20 : 0) + (PREF.length - Math.max(0, PREF.findIndex((p) => v.lang.replace('_', '-').toLowerCase() === p.toLowerCase())) ) + (PREF.some((p) => v.lang.replace('_', '-').toLowerCase() === p.toLowerCase()) ? 5 : 0);
  return [...vs].sort((a, b) => score(b) - score(a))[0];
}
export const hayVoz = () => !!ss() && voces().length > 0;
export function alCargar(f: () => void) { const s = ss(); if (s) s.addEventListener?.('voiceschanged', f); }

let pend: (() => void) | null = null;
export function cortar() { pend?.(); pend = null; ss()?.cancel(); }
export const pausarVoz = () => ss()?.pause();
export const seguirVoz = () => ss()?.resume();

export const hayVozEn = () => !!ss() && voces('en').length > 0;
const limpiaEn = (x: string) => x.replace(/_{2,}/g, ', blank, ').replace(/\s*[–—]\s*/g, ' to ').replace(/\s+/g, ' ').trim();
let aviso: HTMLElement | null = null;
/** Si el dispositivo no tiene voz en inglés, no se lee el inglés con voz en español: se avisa una vez. */
/** Pasos para instalar una voz en inglés según el dispositivo. */
export function guiaVozEn(): string {
  const ua = typeof navigator !== 'undefined' ? navigator.userAgent : '';
  const f = ' Después recarga la página.';
  if (/Android/i.test(ua)) return 'Instala una voz en inglés: Ajustes → Sistema → Idioma y entrada → Salida de texto a voz → Google → Instalar datos de voz → English.' + f;
  if (/iPhone|iPad|iPod/i.test(ua)) return 'Instala una voz en inglés: Ajustes → Accesibilidad → Contenido leído → Voces → Inglés.' + f;
  if (/Windows/i.test(ua)) return 'Instala una voz en inglés: Configuración → Hora e idioma → Voz → Agregar voces → English (United States).' + f;
  if (/Mac/i.test(ua)) return 'Instala una voz en inglés: Ajustes del Sistema → Accesibilidad → Contenido leído → Voz del sistema → Gestionar voces → English.' + f;
  return 'Tu dispositivo no tiene voz en inglés. Instala una en los ajustes de voz del sistema.' + f;
}
function avisoSinEn() {
  if (aviso?.isConnected || typeof document === 'undefined') return;
  aviso = document.createElement('div'); aviso.className = 'toast-en'; aviso.setAttribute('role', 'status');
  aviso.textContent = guiaVozEn();
  document.body.append(aviso); setTimeout(() => aviso?.remove(), 9000);
}
/** Dice una frase en inglés con voz inglesa (lo usan los botones de escuchar). */
export function hablaEn(texto: string, lento = false): Promise<void> {
  cortar();
  const s = ss(), v = mejorVoz('en');
  if (!s || !v) { avisoSinEn(); return Promise.resolve(); }
  return new Promise((res) => {
    const u = new SpeechSynthesisUtterance(limpiaEn(texto)); u.voice = v; u.lang = v.lang; u.rate = lento ? 0.6 : cfg.enRate; u.pitch = 1;
    const t = setTimeout(res, 15000); u.onend = u.onerror = () => { clearTimeout(t); res(); };
    s.speak(u);
  });
}

/** Dice un texto y resuelve cuando termina (o cuando se corta). Lo que va entre {{ }} se dice con voz en inglés; {{!frase}} se dice normal y luego despacio. */
export function decir(texto: string): Promise<void> {
  const est = Math.max(900, texto.replace(/[{}!]/g, '').length * 64) / cfg.rate;
  return new Promise((res) => {
    let vivo = true, t: ReturnType<typeof setTimeout>;
    const fin = () => { if (!vivo) return; vivo = false; if (pend === fin) pend = null; clearTimeout(t); res(); };
    pend = fin;
    const v = cfg.on ? mejorVoz() : null, s = ss();
    if (!v || !s) { t = setTimeout(fin, est); return; }
    t = setTimeout(fin, est * 3 + 6000);
    const cola: { txt: string; en: boolean; lento: boolean }[] = [];
    texto.split(/(\{\{.+?\}\})/).map((x) => x.trim()).filter(Boolean).forEach((x) => {
      if (!/^\{\{/.test(x)) { x.split(/(?<=[.!?;:])\s+/).filter(Boolean).forEach((fr) => cola.push({ txt: fr, en: false, lento: false })); return; }
      let e = x.slice(2, -2); const doble = e.startsWith('!'); if (doble) e = e.slice(1);
      cola.push({ txt: e, en: true, lento: false }); if (doble) cola.push({ txt: e, en: true, lento: true });
    });
    let i = 0;
    const sig = () => {
      if (!vivo) return; if (i >= cola.length) { fin(); return; }
      const c = cola[i++], vz = c.en ? mejorVoz('en') : v;
      if (!vz) { if (c.en) avisoSinEn(); setTimeout(sig, 400); return; }
      const u = new SpeechSynthesisUtterance(c.en ? limpiaEn(c.txt) : c.txt); u.voice = vz; u.lang = vz.lang; u.pitch = 1;
      u.rate = c.en ? (c.lento ? 0.6 : cfg.enRate) : cfg.rate;
      u.onerror = fin; u.onend = () => setTimeout(sig, c.en ? 320 : cola[i]?.en ? 180 : /[.!?]$/.test(c.txt) ? 260 : 140);
      s.speak(u);
    };
    sig();
  });
}

/** Toca una frase en inglés (.en) o su botón (.spk) para oírla. */
if (typeof document !== 'undefined') {
  const oir = (e: Event) => {
    const el = (e.target as HTMLElement | null)?.closest<HTMLElement>('[data-en]'); if (!el) return;
    e.preventDefault(); e.stopPropagation();
    void hablaEn(el.dataset.en ?? '', el.dataset.lento === '1');
  };
  document.addEventListener('click', oir, true);
  document.addEventListener('keydown', (e) => { if ((e.key === 'Enter' || e.key === ' ') && (e.target as HTMLElement | null)?.matches?.('[data-en]')) oir(e); }, true);
}

if (typeof addEventListener === 'function') { addEventListener('hashchange', cortar); addEventListener('pagehide', cortar); }
