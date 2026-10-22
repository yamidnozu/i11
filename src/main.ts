import './style.css';
import { h } from './ui/dom';
import { registerAll } from './sims';
import { biblioteca, preguntaSuelta } from './ui/biblioteca';
import { simulacroLista, simulacroPagina } from './ui/simulacro';
import * as P from './ui/pages';
import * as R from './ui/ruta';
import { extras } from './ui/extras';
import { mapa } from './ui/mapa';
import { UNIDADES_ALL, SIMULACROS_ALL } from './content';
import { listSims } from './core/registry';
import { initKeys } from './ui/question';
import { initNav, current, query } from './ui/nav';
import { ico } from './ui/icons';
import { refreshEntitlement, hasPremium } from './state/store';

registerAll();
const app = document.getElementById('app')!;
const NAV: [string, string, string, string][] = [
  ['/', 'Hoy', 'home', 'hoy'], ['/aprender', 'Aprender', 'book', 'aprender'], ['/practicar', 'Practicar', 'pencil', 'practicar'], ['/panel', 'Progreso', 'chart', 'panel'],
];
const DESC: Record<string, string> = { '/': 'Tu siguiente paso', '/aprender': 'Estudia un tema', '/practicar': 'Preguntas y simulacros', '/panel': 'Cómo vas' };
const TITLES: Record<string, string> = { aprender: 'Aprender', unidad: 'Tema', practicar: 'Practicar', sesion: 'Sesión', sims: 'Laboratorios', sim: 'Laboratorio', diag: 'Diagnóstico', lecciones: 'Lecciones', leccion: 'Lección', practica: 'Práctica', simulacro: 'Simulacro', contenido: 'Todo el contenido', mapa: 'Mapa', pregunta: 'Pregunta', panel: 'Mi progreso', extras: 'Actividades', pago: 'Acceso' };

const theme = () => document.documentElement.dataset.theme === 'oscuro' ? 'oscuro' : 'claro';
const themeBtn = h('button', { class: 'iconbtn', type: 'button', onclick: () => {
  const t = theme() === 'oscuro' ? 'claro' : 'oscuro';
  document.documentElement.dataset.theme = t;
  try { localStorage.setItem('saber11.theme', t); } catch { /* sin almacenamiento */ }
  paintTheme();

} });
const paintTheme = () => { themeBtn.innerHTML = ico(theme() === 'oscuro' ? 'sun' : 'moon', 20); themeBtn.setAttribute('aria-label', theme() === 'oscuro' ? 'Cambiar a tema claro' : 'Cambiar a tema oscuro'); };
paintTheme();

const PALETAS: { id: string; n: string; c: string }[] = [{ id: '', n: 'Océano', c: '#0E5A6B' }, { id: 'bosque', n: 'Bosque', c: '#2F7D4F' }, { id: 'uva', n: 'Uva', c: '#6B4BA6' }, { id: 'coral', n: 'Coral', c: '#C2492F' }, { id: 'dorado', n: 'Dorado', c: '#A87510' }, { id: 'grafito', n: 'Grafito', c: '#3D4852' }];
const pal = () => { try { return localStorage.getItem('saber11.paleta') ?? ''; } catch { return ''; } };
const aplicaPaleta = (id: string) => { if (id) document.documentElement.dataset.paleta = id; else delete document.documentElement.dataset.paleta; };
aplicaPaleta(hasPremium() ? pal() : '');
const palBtn = h('button', { class: 'iconbtn', type: 'button', 'aria-label': 'Elegir paleta de color', 'aria-haspopup': 'true', html: ico('palette', 20), title: 'Colores' });
const palMenu = h('div', { class: 'palmenu', hidden: true, role: 'menu' });
const pintaPal = () => palMenu.replaceChildren(h('p', { class: 'fine' }, hasPremium() ? 'Elige los colores de la plataforma.' : 'Colores premium: el contenido es gratis para todos.'), ...PALETAS.map((p) => { const lock = !!p.id && !hasPremium(); return h('button', { class: 'palopt', type: 'button', role: 'menuitem', 'aria-current': String(pal() === p.id), onclick: () => { if (lock) { palMenu.hidden = true; location.hash = '#/pago'; return; } try { localStorage.setItem('saber11.paleta', p.id); } catch { /* */ } aplicaPaleta(p.id); pintaPal(); } }, h('i', { style: `background:${p.c}` }), h('span', {}, p.n), lock ? h('small', {}, 'Premium') : null); }));
palBtn.addEventListener('click', () => { pintaPal(); palMenu.hidden = !palMenu.hidden; });
document.addEventListener('click', (e) => { if (!palMenu.hidden && !(e.target as HTMLElement).closest('.palwrap')) palMenu.hidden = true; });
const mapBtn = h('a', { class: 'iconbtn', href: '#/mapa', title: 'Mapa de la plataforma', 'aria-label': 'Mapa de la plataforma', html: ico('map', 20) }) as HTMLAnchorElement;
mapBtn.addEventListener('click', () => { const c = current(); if (c !== '/mapa') mapBtn.setAttribute('href', '#/mapa?desde=' + encodeURIComponent(c)); }, true);
const palWrap = h('div', { class: 'palwrap' }, palBtn, palMenu);

const logo = '<svg viewBox="0 0 40 40" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" aria-hidden="true"><path d="M5 33h30"/><path d="M5 33Q19 -4 33 33"/><path d="M5 33l15-9" stroke-dasharray="2 3.5"/><circle cx="19" cy="12.5" r="2.8" fill="currentColor" stroke="none"/></svg>';
const links = NAV.map(([href, t]) => h('a', { href: '#' + href, 'data-r': href, title: DESC[href] }, h('span', {}, t), h('small', {}, DESC[href])));
const dockLinks = NAV.map(([href, t, ic]) => h('a', { href: '#' + href, 'data-r': href, html: `${ico(ic, 22)}<span>${t}</span>` }));
document.getElementById('top')!.append(h('a', { class: 'brand', href: '#/', html: `${logo}<span>Saber 11<small>laboratorio de estudio</small></span>` }), h('nav', { class: 'topnav', 'aria-label': 'Principal' }, ...links), h('div', { class: 'tools' }, mapBtn, palWrap, themeBtn));
document.getElementById('dock')!.append(...dockLinks);

function mark(path: string) {
  const base = '/' + (path.split('/')[1] ?? '');
  const MAPA: Record<string, string> = { '/sim': '/aprender', '/sims': '/aprender', '/leccion': '/aprender', '/lecciones': '/aprender', '/unidad': '/aprender', '/diag': '/practicar', '/sesion': '/practicar', '/practica': '/practicar', '/simulacro': '/practicar', '/extras': '/practicar', '/contenido': '/practicar', '/pregunta': '/practicar', '/pago': '/panel' };
  const key = MAPA[base] ?? base;
  for (const a of [...links, ...dockLinks]) { if (a.getAttribute('data-r') === key) a.setAttribute('aria-current', 'page'); else a.removeAttribute('aria-current'); }
}

/** Modo enfoque: mientras se resuelve una pregunta, la pantalla no se desplaza; cada panel lleva su propio desplazamiento. */
new MutationObserver(() => document.body.classList.toggle('foco', !!app.querySelector('.qcard[data-kind="mc"]:not([data-libre])'))).observe(app, { childList: true, subtree: true });

/** Migas de pan: siempre se sabe dónde se está y cómo volver. */
function migas(name: string, rest: string[]): HTMLElement | null {
  const A: [string, string] = ['Aprender', '#/aprender'], P: [string, string] = ['Practicar', '#/practicar'];
  const id = rest[0] ?? '';
  let t: [string, string?][] = [];
  switch (name) {
    case 'unidad': t = [A, [UNIDADES_ALL.find((u) => u.id === id)?.titulo ?? 'Tema']]; break;
    case 'sims': t = [A, ['Laboratorios']]; break;
    case 'sim': t = [A, ['Laboratorios', '#/sims'], [listSims().find((x) => x.id === rest.join('/'))?.title ?? 'Laboratorio']]; break;
    case 'lecciones': t = [A, ['Lecciones']]; break;
    case 'leccion': t = [A, ['Lecciones', '#/lecciones'], ['Lección']]; break;
    case 'sesion': case 'practica': t = [P, [query().get('modo') === 'repaso' ? 'Repaso' : 'Sesión de práctica']]; break;
    case 'diag': t = [P, ['Diagnóstico']]; break;
    case 'extras': t = [P, ['Actividades']]; break;
    case 'simulacro': t = id ? [P, ['Simulacros', '#/simulacro'], [SIMULACROS_ALL.find((x) => x.id === id)?.nombre ?? 'Simulacro']] : [P, ['Simulacros']]; break;
    case 'contenido': t = [P, ['Todo el contenido']]; break;
    case 'pregunta': t = [P, ['Todo el contenido', '#/contenido'], ['Pregunta']]; break;
    case 'pago': t = [['Progreso', '#/panel'], ['Acceso']]; break;
    default: return null;
  }
  return h('nav', { class: 'crumb', 'aria-label': 'Dónde estás' }, h('a', { href: '#/' }, 'Hoy'), ...t.flatMap(([n, href]) => [h('span', { 'aria-hidden': 'true' }, '›'), href ? h('a', { href }, n) : h('b', { 'aria-current': 'page' }, n)]));
}
let token = 0;
async function route() {
  const me = ++token, path = current();
  const [, name = '', ...rest] = path.split('/');
  let view: HTMLElement | Promise<HTMLElement>;
  switch (name) {
    case 'diag': view = P.diagnostic(); break;
    case 'sims': view = P.simsList(); break;
    case 'sim': view = P.simPage(rest.join('/')); break;
    case 'lecciones': view = P.lessons(); break;
    case 'leccion': view = P.lessons(rest[0]); break;
    case 'aprender': view = R.aprender(); break;
    case 'unidad': view = R.unidadPage(rest[0], rest[1]); break;
    case 'mapa': view = mapa(); break;
    case 'contenido': view = biblioteca(); break;
    case 'pregunta': view = preguntaSuelta(rest[0]); break;
    case 'practicar': view = R.practicar(); break;
    case 'sesion': view = R.sesionGeneral(query().get('modo') === 'repaso'); break;
    case 'practica': view = R.sesionGeneral(); break;
    case 'simulacro': view = rest[0] ? simulacroPagina(rest[0]) : simulacroLista(); break;
    case 'panel': view = P.panel(); break;
    case 'extras': view = extras(); break;
    case 'pago': view = rest[0] === 'resultado' ? P.payResult() : P.payPage(); break;
    default: view = R.hoy();
  }
  const el = await view;
  if (me !== token) return;
  app.replaceChildren(h('div', { class: 'sheet' }, migas(name, rest), el));
  mark(path);
  document.title = (TITLES[name] ? TITLES[name] + ' · ' : '') + 'Saber 11';
  window.scrollTo(0, 0);
  app.focus({ preventScroll: true });
}
initNav(route);
initKeys();
route();
refreshEntitlement();
if ('serviceWorker' in navigator && location.protocol === 'https:') navigator.serviceWorker.register('/sw.js').catch(() => {});
