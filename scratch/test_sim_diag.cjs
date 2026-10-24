const puppeteer = require('puppeteer-core');

async function main() {
  const browser = await puppeteer.launch({
    executablePath: '/opt/google/chrome/chrome',
    args: ['--no-sandbox', '--disable-setuid-sandbox']
  });
  const page = await browser.newPage();
  await page.setViewport({ width: 390, height: 844, isMobile: true });

  // 1. Simulacros lista
  await page.goto('http://127.0.0.1:5173/#/simulacro', { waitUntil: 'networkidle0' });
  await page.screenshot({ path: 'docs/capturas/13_simulacros_lista_mobile_fixed.png' });
  console.log('Saved 13_simulacros_lista_mobile_fixed.png');

  // 2. Simulacro portada
  await page.goto('http://127.0.0.1:5173/#/simulacro/completo-1', { waitUntil: 'networkidle0' });
  await page.screenshot({ path: 'docs/capturas/14_simulacro_portada_mobile_fixed.png' });
  console.log('Saved 14_simulacro_portada_mobile_fixed.png');

  // 3. Diagnóstico entrada
  await page.goto('http://127.0.0.1:5173/#/diag', { waitUntil: 'networkidle0' });
  await page.screenshot({ path: 'docs/capturas/02_diagnostico_inicio_mobile_fixed.png' });
  console.log('Saved 02_diagnostico_inicio_mobile_fixed.png');

  await browser.close();
}

main().catch(err => {
  console.error(err);
  process.exit(1);
});
