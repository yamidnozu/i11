const puppeteer = require('puppeteer-core');
const fs = require('fs');
const path = require('path');

const CAPTURES_DIR = path.join(__dirname, '../docs/capturas');
if (!fs.existsSync(CAPTURES_DIR)) {
  fs.mkdirSync(CAPTURES_DIR, { recursive: true });
}

async function main() {
  const browser = await puppeteer.launch({
    executablePath: '/opt/google/chrome/chrome',
    args: ['--no-sandbox', '--disable-setuid-sandbox']
  });

  const page = await browser.newPage();

  // Test Mobile (390x844 - iPhone 12/13/14)
  await page.setViewport({ width: 390, height: 844, deviceScaleFactor: 2, isMobile: true, hasTouch: true });

  const routes = [
    { name: '01_inicio_bienvenida_mobile', hash: '#/' },
    { name: '02_diag_mobile', hash: '#/diag' },
    { name: '03_aprender_mobile', hash: '#/aprender' },
    { name: '04_practicar_mobile', hash: '#/practicar' },
    { name: '05_simulacro_mobile', hash: '#/simulacro' },
    { name: '06_panel_mobile', hash: '#/panel' },
    { name: '07_faq_mobile', hash: '#/faq' },
    { name: '08_sims_mobile', hash: '#/sims' },
    { name: '09_pregunta_mobile', hash: '#/pregunta/m-01' }
  ];

  for (const r of routes) {
    await page.goto(`http://127.0.0.1:5173/${r.hash}`, { waitUntil: 'networkidle0' });
    await new Promise(res => setTimeout(res, 600));
    await page.screenshot({ path: path.join(CAPTURES_DIR, `${r.name}.png`) });
    console.log(`Captured ${r.name}`);
  }

  // Trigger coachmarks on mobile home and capture
  await page.goto('http://127.0.0.1:5173/#/', { waitUntil: 'networkidle0' });
  await page.evaluate(() => {
    const btn = document.querySelector('.help-coachmark-btn');
    if (btn) btn.click();
  });
  await new Promise(res => setTimeout(res, 500));
  await page.screenshot({ path: path.join(CAPTURES_DIR, '10_coachmarks_inicio_mobile.png') });
  console.log('Captured 10_coachmarks_inicio_mobile');

  // Desktop (1280x800)
  await page.setViewport({ width: 1280, height: 800, deviceScaleFactor: 1 });
  const desktopRoutes = [
    { name: '11_inicio_desktop', hash: '#/' },
    { name: '12_aprender_desktop', hash: '#/aprender' },
    { name: '13_faq_desktop', hash: '#/faq' }
  ];

  for (const r of desktopRoutes) {
    await page.goto(`http://127.0.0.1:5173/${r.hash}`, { waitUntil: 'networkidle0' });
    await new Promise(res => setTimeout(res, 600));
    await page.screenshot({ path: path.join(CAPTURES_DIR, `${r.name}.png`) });
    console.log(`Captured ${r.name}`);
  }

  await browser.close();
  console.log('All captures done.');
}

main().catch(err => {
  console.error(err);
  process.exit(1);
});
