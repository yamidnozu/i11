import { h } from './dom';
import { head, DISCLAIMER } from './pages';

interface FAQItem {
  q: string;
  a: string;
  bullets?: string[];
}

const FAQS: FAQItem[] = [
  {
    q: '¿Qué es Saber 11 Interactivo?',
    a: 'Es una plataforma web educativa gratuita diseñada para estudiantes de grados 10° y 11° en Colombia. Su objetivo es transformar la preparación para el examen de Estado Saber 11: en lugar de memorizar fórmulas o leer textos estáticos, experimentas directamente con laboratorios interactivos, diagnóstico adaptativo y simulacros tipo examen real.'
  },
  {
    q: '¿La plataforma es realmente 100% gratuita?',
    a: 'Sí. Todo el contenido pedagógico esencial es totalmente gratis: el diagnóstico adaptativo, los 11 laboratorios interactivos de física y matemáticas, las lecciones conceptuales, la práctica adaptativa con repetición espaciada y todos los simulacros completos.'
  },
  {
    q: '¿Esta plataforma es oficial del ICFES?',
    a: 'No. Es un proyecto educativo independiente de estudio y preparación. No está administrado, afiliado, autorizado ni respaldado por el Instituto Colombiano para la Evaluación de la Educación (ICFES). Todo el material pedagógico es original y se ofrece con propósitos estrictamente formativos.'
  },
  {
    q: '¿Cuáles son las 5 áreas obligatorias del examen Saber 11?',
    a: 'El examen oficial Saber 11 evalúa cinco áreas fundamentales:',
    bullets: [
      'Matemáticas: Álgebra, funciones, cálculo, geometría, medición, estadística y probabilidad (3 competencias: interpretación, formulación y argumentación).',
      'Lectura Crítica: Comprensión local, estructura global y reflexión crítica sobre textos continuos (ensayos, literatura) y discontinuos (infografías, cómics).',
      'Sociales y Ciudadanas: Constitución de 1991, deberes y derechos, mecanismos de participación, historia colombiana y análisis de perspectivas.',
      'Ciencias Naturales: Biología, Física, Química y la relación entre Ciencia, Tecnología y Sociedad (CTS).',
      'Inglés: Comprensión de avisos, vocabulario, conversaciones cotidianas y comprensión lectora en niveles A1 a B1 del MCER.'
    ]
  },
  {
    q: '¿Cómo recomiendan prepararse para el Saber 11 de forma efectiva?',
    a: 'Recomendamos un método activo en 5 etapas:',
    bullets: [
      '1. Diagnóstico inicial (~10 min): 15 preguntas rápidas para conocer tu punto de partida y fijar tu radar de áreas.',
      '2. Ruta priorizada (Aprender): Comienza por tu área con puntaje más bajo. En cada tema: mira la simulación, lee la lección y resuelve preguntas guiadas.',
      '3. Racha diaria (15 min al día): Sesiones cortas de práctica adaptativa con repetición espaciada para no olvidar lo aprendido.',
      '4. Simulacros cronometrados: Entrena la gestión del tiempo y la concentración con cuadernillos completos antes de la fecha real.',
      '5. Análisis del error: Revisa siempre por qué fallaste cada pregunta; comprender el distractor enseña más que acertar a ciegas.'
    ]
  },
  {
    q: '¿Cómo funcionan los laboratorios interactivos?',
    a: 'Cada laboratorio aborda un concepto central de física o matemáticas (proyectiles, ley de Ohm, resortes, caída libre). Puedes cambiar variables en tiempo real y observar el efecto de inmediato en el canvas. Antes de cada prueba se te pide predecir el resultado: equivocarse y ver por qué ocurre el fenómeno consolida el aprendizaje profundo.'
  },
  {
    q: '¿Se guardan mis progresos y respuestas?',
    a: 'Sí. Todo tu avance, racha de estudio, respuestas de simulacro y puntajes estimados se guardan localmente en tu dispositivo. Puedes volver en cualquier momento y continuar donde ibas.'
  }
];

export function faqPage(): HTMLElement {
  return h('div', { class: 'faq-page' },
    head('Preguntas Frecuentes (FAQ)', 'Todo lo que necesitas saber sobre la plataforma, el examen Saber 11 y cómo estudiar de forma inteligente.'),
    h('div', { class: 'faq-list', style: 'display:grid;gap:14px;margin-top:1.2rem' },
      ...FAQS.map((item, idx) => h('details', {
        class: 'box faq-item',
        open: idx < 2,
        style: 'border-radius:var(--r2);padding:16px 20px'
      },
        h('summary', { style: 'cursor:pointer;font-weight:700;font-size:1.08rem;color:var(--ink)' }, item.q),
        h('p', { style: 'margin:12px 0 6px;line-height:1.6;color:var(--ink)' }, item.a),
        item.bullets ? h('ul', { style: 'margin:8px 0 8px 18px;line-height:1.6;color:var(--mut)' },
          ...item.bullets.map((b) => h('li', { style: 'margin-bottom:6px' }, b))
        ) : null
      ))
    ),
    h('div', { class: 'box', style: 'margin-top:2rem;text-align:center;background:color-mix(in srgb,var(--acc) 8%,var(--panel));border:1px solid var(--acc)' },
      h('h3', { style: 'margin-bottom:8px' }, '¿Listo para empezar tu preparación?'),
      h('p', { style: 'color:var(--mut);margin-bottom:16px' }, 'Mide tu nivel en 10 minutos con nuestro diagnóstico adaptativo.'),
      h('div', { class: 'row center', style: 'gap:12px' },
        h('a', { class: 'btn primary big', href: '#/diag' }, 'Hacer diagnóstico gratis (~10 min) →'),
        h('a', { class: 'btn big', href: '#/' }, 'Ir al inicio')
      )
    ),
    h('p', { class: 'fine', style: 'margin-top:2rem' }, DISCLAIMER)
  );
}
