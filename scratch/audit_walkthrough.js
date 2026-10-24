import puppeteer from 'puppeteer-core';
import fs from 'fs';
import path from 'path';

const CAPTURAS_DIR = path.resolve('docs/capturas');
if (!fs.existsSync(CAPTURAS_DIR)) fs.mkdirSync(CAPTURAS_DIR, { recursive: true });

async function runAudit() {
  const browser = await puppeteer.launch({
    executablePath: '/opt/google/chrome/chrome',
    args: ['--no-sandbox', '--disable-gpu'],
  });

  const findings = [];
  const consoleErrors = [];

  const page = await browser.newPage();
  page.on('console', msg => {
    if (msg.type() === 'error') {
      consoleErrors.push(`[Console Error] ${msg.text()}`);
    }
  });
  page.on('pageerror', err => {
    consoleErrors.push(`[Page Error] ${err.message}`);
  });

  // Helper to capture both viewports
  async function captureScreen(route, namePrefix) {
    // Mobile 390x844
    await page.setViewport({ width: 390, height: 844, deviceScaleFactor: 2 });
    await page.goto(`http://127.0.0.1:5173/#${route}`, { waitUntil: 'networkidle0' });
    await new Promise(r => setTimeout(r, 600));
    
    // Check horizontal overflow
    const overflowM = await page.evaluate(() => {
      return document.documentElement.scrollWidth > window.innerWidth;
    });

    const fileMobile = `${namePrefix}_mobile_390x844.png`;
    await page.screenshot({ path: path.join(CAPTURAS_DIR, fileMobile), fullPage: false });

    // Desktop 1280x800
    await page.setViewport({ width: 1280, height: 800, deviceScaleFactor: 2 });
    await page.goto(`http://127.0.0.1:5173/#${route}`, { waitUntil: 'networkidle0' });
    await new Promise(r => setTimeout(r, 600));
    
    const overflowD = await page.evaluate(() => {
      return document.documentElement.scrollWidth > window.innerWidth;
    });

    const fileDesktop = `${namePrefix}_desktop_1280x800.png`;
    await page.screenshot({ path: path.join(CAPTURAS_DIR, fileDesktop), fullPage: false });

    console.log(`Captured ${namePrefix}: mobile (overflow: ${overflowM}), desktop (overflow: ${overflowD})`);
    return { overflowM, overflowD, fileMobile, fileDesktop };
  }

  // 1. Initial State (Clean localStorage)
  await page.goto('http://127.0.0.1:5173/#/');
  await page.evaluate(() => localStorage.clear());

  // Screen 1: Home / Bienvenida (pre-diagnostic)
  const s1 = await captureScreen('/', '01_hoy_bienvenida');

  // Screen 2: Diagnostic start
  const s2 = await captureScreen('/diag', '02_diagnostico_inicio');

  // Let's answer 1 question in diagnostic on mobile to see response feedback
  await page.setViewport({ width: 390, height: 844, deviceScaleFactor: 2 });
  await page.goto('http://127.0.0.1:5173/#/diag', { waitUntil: 'networkidle0' });
  await new Promise(r => setTimeout(r, 500));
  
  // Click on first option button
  const optionClicked = await page.evaluate(() => {
    const btn = document.querySelector('.qopt');
    if (btn) {
      btn.click();
      return true;
    }
    return false;
  });
  await new Promise(r => setTimeout(r, 600));
  await page.screenshot({ path: path.join(CAPTURAS_DIR, '02b_diagnostico_respondida_mobile.png') });

  // Complete the 15 diagnostic questions to see the results screen and post-diagnostic Home!
  for (let q = 1; q <= 15; q++) {
    await page.evaluate(() => {
      const opt = document.querySelector('.qopt');
      if (opt) opt.click();
      const nextBtn = document.querySelector('.diag-next, button.primary, [data-act="next"]');
      if (nextBtn) nextBtn.click();
    });
    await new Promise(r => setTimeout(r, 400));
  }
  await new Promise(r => setTimeout(r, 800));
  await page.screenshot({ path: path.join(CAPTURAS_DIR, '02c_diagnostico_resultado_mobile.png') });

  // Screen 3: Home post-diagnostic
  const s3 = await captureScreen('/', '03_hoy_con_diagnostico');

  // Screen 4: Aprender
  const s4 = await captureScreen('/aprender', '04_aprender');

  // Screen 5: Unit page
  const s5 = await captureScreen('/unidad/u-proyectil', '05_unidad_proyectil');

  // Screen 6: Sims list
  const s6 = await captureScreen('/sims', '06_sims_lista');

  // Screen 7: Lab Proyectil
  const s7 = await captureScreen('/sim/fis.proyectil', '07_lab_proyectil');

  // Screen 8: Lab Ohm
  const s8 = await captureScreen('/sim/fis.ohm', '08_lab_ohm');

  // Screen 9: Lessons list & lesson
  const s9 = await captureScreen('/lecciones', '09_lecciones_lista');
  const s9b = await captureScreen('/leccion/cie-proyectil', '09b_leccion_detalle');

  // Screen 10: Question focus mode
  const s10 = await captureScreen('/pregunta/mat-001', '10_pregunta_foco');

  // Question answered state
  await page.setViewport({ width: 390, height: 844, deviceScaleFactor: 2 });
  await page.goto('http://127.0.0.1:5173/#/pregunta/mat-001', { waitUntil: 'networkidle0' });
  await new Promise(r => setTimeout(r, 500));
  await page.evaluate(() => {
    const opt = document.querySelectorAll('.qopt')[1]; // correct answer for mat-001 is index 1 ($11.000)
    if (opt) opt.click();
  });
  await new Promise(r => setTimeout(r, 800));
  await page.screenshot({ path: path.join(CAPTURAS_DIR, '10b_pregunta_respondida_mobile.png') });

  // Open Hoja pedagógica / explanation if available
  await page.evaluate(() => {
    const expBtn = document.querySelector('.btn-hoja, [data-act="hoja"], .btn-profe');
    if (expBtn) expBtn.click();
  });
  await new Promise(r => setTimeout(r, 800));
  await page.screenshot({ path: path.join(CAPTURAS_DIR, '10c_pregunta_hoja_mobile.png') });

  // Screen 11: Practicar
  const s11 = await captureScreen('/practicar', '11_practicar');

  // Screen 12: Practice session (sesion)
  const s12 = await captureScreen('/sesion', '12_sesion_practica');

  // Screen 13: Simulacros list
  const s13 = await captureScreen('/simulacro', '13_simulacros_lista');

  // Screen 14: Simulacro page (cuadernillo-ejemplo)
  const s14 = await captureScreen('/simulacro/cuadernillo-ejemplo', '14_simulacro_portada');

  // Screen 15: Progress / Panel
  const s15 = await captureScreen('/panel', '15_progreso_panel');

  // Screen 16: Mapa
  const s16 = await captureScreen('/mapa', '16_mapa_plataforma');

  // Screen 17: Extras / Actividades
  const s17 = await captureScreen('/extras', '17_actividades_extras');

  // Screen 18: Biblioteca / Todo el contenido
  const s18 = await captureScreen('/contenido', '18_biblioteca_contenido');

  console.log('\n--- Console Errors Captured ---');
  console.log(consoleErrors.length ? consoleErrors.join('\n') : 'No console errors detected!');

  await browser.close();
  console.log('Audit completed successfully!');
}

runAudit().catch(err => {
  console.error('Audit failed:', err);
  process.exit(1);
});
