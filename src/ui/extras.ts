import { h } from './dom';

/** Actividades interactivas ligeras: lectura (marcar evidencia), inglés (voz), tutela (escenarios), línea de tiempo. */
export function extras(): HTMLElement {
  return h('div', {}, h('div', { class: 'pagehead' }, h('h1', {}, 'Actividades'), h('p', { class: 'lede' }, 'Ejercicios cortos de lectura, inglés, ciudadanía e historia. Sin cronómetro: aquí se explora.')), reader(), english(), tutela(), timeline());
}

function reader(): HTMLElement {
  const sents = ['Las bibliotecas de barrio prestan libros.', 'También sirven para estudiar y hacer trámites digitales.', 'Por eso, medir su valor solo por préstamos es engañoso.', 'Algunas abren hasta tarde.'];
  const main = 2; const msg = h('p', { role: 'status' });
  return h('section', { class: 'activity' }, h('h2', {}, 'Lectura crítica: encuentra la tesis'), h('p', {}, 'Toca la oración que expresa la idea central del autor.'),
    ...sents.map((s, i) => h('button', { class: 'sent', type: 'button', onclick: (e: Event) => { const ok = i === main; (e.currentTarget as HTMLElement).classList.add(ok ? 'right' : 'wrong'); msg.textContent = ok ? 'Sí: «Por eso» marca la conclusión.' : 'Es un dato de apoyo; busca la conclusión.'; msg.className = ok ? 'ok' : 'bad'; } }, s)), msg);
}

function english(): HTMLElement {
  const phrase = 'If it rains tomorrow, we will stay at home.';
  const out = h('p', { role: 'status' });
  const speak = () => { if ('speechSynthesis' in window) { const u = new SpeechSynthesisUtterance(phrase); u.lang = 'en-US'; speechSynthesis.speak(u); } else out.textContent = 'Tu navegador no tiene voz; lee la frase en voz alta.'; };
  const listen = () => {
    const SR = (window as any).SpeechRecognition || (window as any).webkitSpeechRecognition;
    if (!SR) { out.textContent = 'Reconocimiento de voz no disponible: repite la frase y compárala con el audio.'; return; }
    const r = new SR(); r.lang = 'en-US'; r.onresult = (e: any) => { const t: string = e.results[0][0].transcript; out.textContent = `Dijiste: «${t}» — ${t.toLowerCase().replace(/[^a-z ]/g, '') === phrase.toLowerCase().replace(/[^a-z ]/g, '') ? '¡Perfecto!' : 'casi, inténtalo otra vez'}`; }; r.onerror = () => { out.textContent = 'No se pudo usar el micrófono.'; }; r.start();
  };
  return h('section', { class: 'activity' }, h('h2', {}, 'Inglés: escucha y repite'), h('p', { class: 'mono' }, phrase), h('div', { class: 'row' }, h('button', { class: 'btn', type: 'button', onclick: speak }, 'Escuchar'), h('button', { class: 'btn', type: 'button', onclick: listen }, 'Repetir')), out);
}

function tutela(): HTMLElement {
  const cases = [
    { t: 'Una EPS niega un medicamento que el médico ordenó y la persona corre riesgo.', a: true, why: 'Salud en conexidad con la vida: la tutela es el mecanismo rápido.' },
    { t: 'Quieres que el Congreso derogue una ley que no te gusta.', a: false, why: 'Eso se discute en el Congreso o con una demanda de inconstitucionalidad, no con tutela.' },
    { t: 'Una entidad no responde en 15 días un derecho de petición.', a: true, why: 'El derecho de petición es fundamental (art. 23).' },
  ];
  return h('section', { class: 'activity' }, h('h2', {}, '¿Procede la tutela?'), ...cases.map((c) => { const m = h('p', { role: 'status' }); return h('div', { style: 'margin-bottom:16px' }, h('p', {}, c.t), h('div', { class: 'row' }, h('button', { class: 'btn sm', type: 'button', onclick: () => { m.textContent = (c.a ? 'Sí procede. ' : 'No: sí procede. ') + c.why; m.className = c.a ? 'ok' : 'bad'; } }, 'Sí procede'), h('button', { class: 'btn sm', type: 'button', onclick: () => { m.textContent = (!c.a ? 'Correcto, no procede. ' : 'No: sí procede. ') + c.why; m.className = !c.a ? 'ok' : 'bad'; } }, 'No procede')), m); }));
}

function timeline(): HTMLElement {
  const correct = ['Grito de Independencia (1810)', 'Constitución de 1886', 'Frente Nacional (1958–1974)', 'Constitución de 1991'];
  const order = [correct[3], correct[0], correct[2], correct[1]];
  const box = h('div'); const msg = h('p', { role: 'status' });
  const draw = () => { box.replaceChildren(...order.map((t, i) => h('div', { class: 'row', style: 'margin:6px 0' }, h('span', { style: 'flex:1;min-width:200px' }, t), h('button', { class: 'btn sm sq', type: 'button', 'aria-label': `Subir ${t}`, onclick: () => { if (i) { [order[i - 1], order[i]] = [order[i], order[i - 1]]; draw(); } } }, '↑'), h('button', { class: 'btn sm sq', type: 'button', 'aria-label': `Bajar ${t}`, onclick: () => { if (i < 3) { [order[i + 1], order[i]] = [order[i], order[i + 1]]; draw(); } } }, '↓')))); };
  draw();
  return h('section', { class: 'activity' }, h('h2', {}, 'Ordena la línea de tiempo'), box, h('button', { class: 'btn primary', type: 'button', onclick: () => { const ok = order.join('|') === correct.join('|'); msg.textContent = ok ? 'Orden correcto.' : 'Aún no: revisa las fechas.'; msg.className = ok ? 'ok' : 'bad'; } }, 'Comprobar'), msg);
}
