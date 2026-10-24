import { h } from './dom';

export interface CoachmarkStep {
  target: string;
  text: string;
  title?: string;
}

export interface CoachmarkGuide {
  id: string;
  name: string;
  steps: CoachmarkStep[];
}

export const GUIDES: Record<string, CoachmarkGuide> = {
  inicio: {
    id: 'inicio',
    name: 'Inicio',
    steps: [
      {
        target: 'a[href="#/diag"], .cta .btn.primary, .hoycard .btn.primary',
        text: 'Empieza aquí con 15 preguntas rápidas.'
      },
      {
        target: '.hero, .hero-vis, .plates, .plate, .hoycard, .pasos3',
        text: 'Experimenta con física y matemáticas interactivas.'
      },
      {
        target: '#dock, .topnav',
        text: 'Muévete entre Aprender, Practicar y tu Progreso.'
      }
    ]
  },
  diag: {
    id: 'diag',
    name: 'Diagnóstico',
    steps: [
      {
        target: '.diag-intro-box b, .diag-intro-box, .qtext, .progline',
        text: '15 preguntas rápidas para conocer tu punto de partida.'
      },
      {
        target: '.diag-intro-box button, .qcard .opt, .opt',
        text: 'Toca aquí para iniciar tu diagnóstico adaptativo.'
      },
      {
        target: '.diag-intro-box p:last-child, .btn.next, .sighint',
        text: 'Puedes responder con tu dedo o teclado.'
      }
    ]
  },
  pregunta: {
    id: 'pregunta',
    name: 'Pregunta',
    steps: [
      {
        target: '.qtext',
        text: 'Lee con atención el contexto del problema.'
      },
      {
        target: '.qcard .opt, .opt',
        text: 'Toca tu opción favorita para marcarla.'
      },
      {
        target: '.question-pager, .qact button, .anot-btn, .hintbox, .qcard',
        text: 'Pide la explicación del profe si tienes dudas.'
      }
    ]
  },
  aprender: {
    id: 'aprender',
    name: 'Aprender',
    steps: [
      {
        target: '.area-chips-scroll, .chips.filters',
        text: 'Desliza para elegir la materia que quieres estudiar.'
      },
      {
        target: '.startcard, .areasec, .sectionhead',
        text: 'Tu tema recomendado según tus áreas más débiles.'
      },
      {
        target: '.areasec summary, .unit, .official-area, .chips',
        text: 'Toca cualquier tema para ver laboratorio y preguntas.'
      }
    ]
  },
  practicar: {
    id: 'practicar',
    name: 'Practicar',
    steps: [
      {
        target: '.card-path:first-child, .paths a:first-child',
        text: 'Sesión de 8 preguntas a tu medida.'
      },
      {
        target: '.chips.filters, .chips',
        text: 'Entrena preguntas de una sola materia específica.'
      },
      {
        target: 'a[href="#/simulacro"], .card-path:nth-child(2), .simcard',
        text: 'Pruebas completas con tiempo como el examen real.'
      }
    ]
  },
  simulacro: {
    id: 'simulacro',
    name: 'Simulacros',
    steps: [
      {
        target: '.simcard, .exbar, .extabs',
        text: 'Elige un simulacro para medir tu puntaje.'
      },
      {
        target: '.sim-cta-pill, .clock, .timer',
        text: 'Toca Empezar para abrir el cuadernillo cronometrado.'
      },
      {
        target: '.simcard-footer, .sb, .exgrid, .exsheet, .simlist',
        text: 'Revisa tu historial y mejores puntajes aquí.'
      }
    ]
  },
  panel: {
    id: 'panel',
    name: 'Mi Progreso',
    steps: [
      {
        target: '.bigscore, .stats, .box.trick',
        text: 'Tu puntaje global proyectado y racha de estudio.'
      },
      {
        target: '.radar, .panelgrid, label[for="exam"], #exam',
        text: 'Descubre tus áreas más fuertes y por mejorar.'
      },
      {
        target: 'a[href*="whatsapp"], .share, .stat',
        text: 'Comparte tus avances con tu profe o familia.'
      }
    ]
  }
};

const KEY = (id: string) => `saber11.cm.${id}`;
let activeDismiss: (() => void) | null = null;

export function isCoachmarkSeen(screenId: string): boolean {
  try {
    return localStorage.getItem(KEY(screenId)) === '1';
  } catch {
    return false;
  }
}

export function markCoachmarkSeen(screenId: string): void {
  try {
    localStorage.setItem(KEY(screenId), '1');
  } catch {
    /* ignorar */
  }
}

export function clearCoachmark(screenId: string): void {
  try {
    localStorage.removeItem(KEY(screenId));
  } catch {
    /* ignorar */
  }
}

function findVisibleElement(selector: string): HTMLElement | null {
  const parts = selector.split(',').map((s) => s.trim());
  for (const sel of parts) {
    const list = document.querySelectorAll<HTMLElement>(sel);
    for (const el of list) {
      if (!el.isConnected) continue;
      const rect = el.getBoundingClientRect();
      const style = window.getComputedStyle(el);
      if (style.display === 'none' || style.visibility === 'hidden' || style.opacity === '0') continue;
      if (rect.width > 0 && rect.height > 0) {
        return el;
      }
    }
  }
  return null;
}

export function dismissActiveCoachmark(): void {
  if (activeDismiss) {
    activeDismiss();
    activeDismiss = null;
  }
}

/** Inicia el recorrido de coachmarks para una pantalla dada. */
export function startCoachmarks(screenId: string, force = false): void {
  dismissActiveCoachmark();

  const guide = GUIDES[screenId];
  if (!guide || (!force && isCoachmarkSeen(screenId))) return;

  // Filtrar pasos cuyos selectores coincidan con al menos un elemento visible en el DOM
  const availableSteps = guide.steps.map((st) => {
    const el = findVisibleElement(st.target);
    return el ? { step: st, el } : null;
  }).filter((x): x is { step: CoachmarkStep; el: HTMLElement } => x !== null);

  if (availableSteps.length === 0) return;

  let stepIdx = 0;

  // Elementos del overlay
  const overlay = h('div', { class: 'coachmark-overlay', role: 'dialog', 'aria-modal': 'true', 'aria-label': `Guía paso a paso: ${guide.name}` });
  const svg = document.createElementNS('http://www.w3.org/2000/svg', 'svg');
  svg.setAttribute('class', 'coachmark-svg');

  const maskId = `cm-mask-${Date.now()}`;
  svg.innerHTML = `
    <defs>
      <mask id="${maskId}">
        <rect width="100%" height="100%" fill="white" />
        <rect class="cm-hole" rx="8" ry="8" fill="black" />
      </mask>
    </defs>
    <rect width="100%" height="100%" fill="rgba(10, 14, 20, 0.78)" mask="url(#${maskId})" />
    <rect class="cm-ring" rx="8" ry="8" fill="none" stroke="var(--acc, #0E5A6B)" stroke-width="2.5" />
  `;

  const hole = svg.querySelector<SVGRectElement>('.cm-hole')!;
  const ring = svg.querySelector<SVGRectElement>('.cm-ring')!;

  const bubble = h('div', { class: 'coachmark-bubble' });
  const arrow = h('div', { class: 'coachmark-arrow' });
  const stepCount = h('span', { class: 'coachmark-step-count' });
  const skipBtn = h('button', { class: 'coachmark-skip-btn', type: 'button', 'aria-label': 'Saltar guía' }, 'Saltar');
  const textEl = h('p', { class: 'coachmark-text' });
  const nextBtn = h('button', { class: 'btn primary sm coachmark-next-btn', type: 'button' });

  skipBtn.onclick = () => dismiss(true);
  nextBtn.onclick = () => {
    if (stepIdx + 1 < availableSteps.length) {
      stepIdx++;
      renderStep();
    } else {
      dismiss(true);
    }
  };

  const onKeyDown = (e: KeyboardEvent) => {
    if (e.key === 'Escape') {
      dismiss(true);
    } else if (e.key === 'ArrowRight' || e.key === 'Enter') {
      nextBtn.click();
    }
  };
  window.addEventListener('keydown', onKeyDown);

  svg.onclick = () => dismiss(true);

  const bubbleHeader = h('div', { class: 'coachmark-header' }, stepCount, skipBtn);
  const bubbleFooter = h('div', { class: 'coachmark-footer' }, nextBtn);
  bubble.append(arrow, bubbleHeader, textEl, bubbleFooter);
  overlay.append(svg, bubble);
  document.body.append(overlay);

  function dismiss(markSeen: boolean) {
    if (markSeen) markCoachmarkSeen(screenId);
    overlay.remove();
    window.removeEventListener('keydown', onKeyDown);
    window.removeEventListener('resize', updatePos);
    window.removeEventListener('scroll', updatePos, true);
    if (activeDismiss === dismiss) activeDismiss = null;
  }
  activeDismiss = () => dismiss(false);

  function updatePos() {
    if (!overlay.isConnected) return;
    const currentItem = availableSteps[stepIdx];
    if (!currentItem || !currentItem.el.isConnected) return;

    const rect = currentItem.el.getBoundingClientRect();
    const vw = window.innerWidth, vh = window.innerHeight;

    // Actualizar orificio en la máscara SVG
    const pad = 6;
    const hx = Math.max(4, rect.left - pad);
    const hy = Math.max(4, rect.top - pad);
    const hw = Math.min(vw - 8, rect.width + pad * 2);
    const hh = rect.height + pad * 2;

    hole.setAttribute('x', String(hx));
    hole.setAttribute('y', String(hy));
    hole.setAttribute('width', String(hw));
    hole.setAttribute('height', String(hh));

    ring.setAttribute('x', String(hx));
    ring.setAttribute('y', String(hy));
    ring.setAttribute('width', String(hw));
    ring.setAttribute('height', String(hh));

    // Medidas de la burbuja
    const bw = Math.min(320, vw - 24);
    bubble.style.width = `${bw}px`;
    const bh = bubble.offsetHeight || 130;

    // Decidir posición vertical: arriba o abajo
    const spaceBelow = vh - rect.bottom;
    const spaceAbove = rect.top;
    const isBelow = spaceBelow >= bh + 16 || spaceAbove < bh + 16;

    let bTop: number;
    if (isBelow) {
      bTop = rect.bottom + 14;
      bubble.classList.remove('pos-top');
      bubble.classList.add('pos-bottom');
    } else {
      bTop = rect.top - bh - 14;
      bubble.classList.remove('pos-bottom');
      bubble.classList.add('pos-top');
    }

    // Clamp vertical para que nunca se salga de la pantalla
    bTop = Math.max(12, Math.min(vh - bh - 12, bTop));

    // Centrado horizontal relativo al target con clamp a márgenes
    let bLeft = rect.left + rect.width / 2 - bw / 2;
    bLeft = Math.max(12, Math.min(vw - bw - 12, bLeft));

    bubble.style.top = `${bTop}px`;
    bubble.style.left = `${bLeft}px`;

    // Flecha alineada con el centro del elemento
    const targetCenterX = rect.left + rect.width / 2;
    const arrowX = Math.max(14, Math.min(bw - 18, targetCenterX - bLeft));
    arrow.style.left = `${arrowX}px`;
  }

  function renderStep() {
    const currentItem = availableSteps[stepIdx];
    if (!currentItem) return;

    stepCount.textContent = `Paso ${stepIdx + 1} de ${availableSteps.length}`;
    textEl.textContent = currentItem.step.text;
    const isLast = stepIdx + 1 === availableSteps.length;
    nextBtn.textContent = isLast ? '¡Entendido! ✓' : 'Siguiente →';

    // Hacer scroll suave hacia el elemento si no tiene posición fija
    const pos = window.getComputedStyle(currentItem.el).position;
    if (pos !== 'fixed') {
      currentItem.el.scrollIntoView({ behavior: 'smooth', block: 'nearest', inline: 'nearest' });
    }

    requestAnimationFrame(() => {
      updatePos();
      setTimeout(updatePos, 80);
    });
  }

  window.addEventListener('resize', updatePos);
  window.addEventListener('scroll', updatePos, true);

  renderStep();
}

/** Verifica y lanza los coachmarks automáticamente tras montar la vista. */
export function checkCoachmarks(screenId: string, delay = 450): void {
  if (!screenId || !GUIDES[screenId] || isCoachmarkSeen(screenId)) return;
  setTimeout(() => {
    startCoachmarks(screenId, false);
  }, delay);
}
