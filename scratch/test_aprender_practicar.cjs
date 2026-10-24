const puppeteer = require('puppeteer-core');

async function main() {
  const browser = await puppeteer.launch({
    executablePath: '/opt/google/chrome/chrome',
    args: ['--no-sandbox', '--disable-setuid-sandbox']
  });
  const page = await browser.newPage();
  await page.setViewport({ width: 390, height: 844, isMobile: true });

  // 1. Aprender
  await page.goto('http://127.0.0.1:5173/#/aprender', { waitUntil: 'networkidle0' });
  await page.screenshot({ path: 'docs/capturas/04_aprender_mobile_fixed.png' });
  console.log('Saved 04_aprender_mobile_fixed.png');

  // 2. Practicar
  await page.goto('http://127.0.0.1:5173/#/practicar', { waitUntil: 'networkidle0' });
  await page.screenshot({ path: 'docs/capturas/11_practicar_mobile_fixed.png' });
  console.log('Saved 11_practicar_mobile_fixed.png');

  // 3. Panel
  await page.goto('http://127.0.0.1:5173/#/panel', { waitUntil: 'networkidle0' });
  await page.screenshot({ path: 'docs/capturas/15_progreso_panel_mobile_fixed.png' });
  console.log('Saved 15_progreso_panel_mobile_fixed.png');

  await browser.close();
}

main().catch(err => {
  console.error(err);
  process.exit(1);
});
