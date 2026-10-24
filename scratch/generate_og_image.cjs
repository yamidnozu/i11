const puppeteer = require('puppeteer-core');
const fs = require('fs');

async function main() {
  const browser = await puppeteer.launch({
    executablePath: '/opt/google/chrome/chrome',
    args: ['--no-sandbox', '--disable-setuid-sandbox']
  });
  const page = await browser.newPage();
  await page.setViewport({ width: 1200, height: 630, deviceScaleFactor: 1 });

  const html = `
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body {
    width: 1200px;
    height: 630px;
    background: radial-gradient(circle at 85% 15%, #164654 0%, #0A0E14 65%);
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    color: #F3F5F7;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    padding: 70px 80px;
    overflow: hidden;
    position: relative;
  }
  .bg-grid {
    position: absolute;
    inset: 0;
    background-image: linear-gradient(rgba(255,255,255,0.03) 1px, transparent 1px),
                      linear-gradient(90deg, rgba(255,255,255,0.03) 1px, transparent 1px);
    background-size: 40px 40px;
    z-index: 1;
  }
  .content {
    position: relative;
    z-index: 2;
    max-width: 850px;
  }
  .brand-row {
    display: flex;
    align-items: center;
    gap: 16px;
    margin-bottom: 24px;
  }
  .logo-box {
    width: 56px;
    height: 56px;
    border-radius: 14px;
    background: #0E5A6B;
    display: flex;
    align-items: center;
    justify-content: center;
    box-shadow: 0 8px 24px rgba(14, 90, 107, 0.5);
  }
  .logo-svg {
    width: 36px;
    height: 36px;
    color: #FFF;
  }
  .brand-tag {
    font-size: 1.1rem;
    font-weight: 700;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    color: #2FD1B5;
  }
  h1 {
    font-size: 4rem;
    font-weight: 800;
    line-height: 1.08;
    margin-bottom: 20px;
    letter-spacing: -0.02em;
    background: linear-gradient(135deg, #FFFFFF 30%, #A5C8D0 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
  }
  p.lede {
    font-size: 1.5rem;
    line-height: 1.45;
    color: #9EAFBA;
    margin-bottom: 34px;
  }
  .badges {
    display: flex;
    gap: 14px;
  }
  .badge {
    padding: 10px 20px;
    background: rgba(255, 255, 255, 0.07);
    border: 1px solid rgba(255, 255, 255, 0.15);
    border-radius: 999px;
    font-size: 1.05rem;
    font-weight: 600;
    color: #E2E8F0;
  }
  .badge.highlight {
    background: rgba(47, 209, 181, 0.18);
    border-color: #2FD1B5;
    color: #2FD1B5;
  }
  .footer {
    position: relative;
    z-index: 2;
    display: flex;
    justify-content: space-between;
    align-items: flex-end;
    border-top: 1px solid rgba(255, 255, 255, 0.12);
    padding-top: 24px;
    font-size: 0.95rem;
    color: #718096;
  }
  .domain {
    font-size: 1.25rem;
    font-weight: 700;
    color: #FFF;
  }
</style>
</head>
<body>
  <div class="bg-grid"></div>
  <div class="content">
    <div class="brand-row">
      <div class="logo-box">
        <svg class="logo-svg" viewBox="0 0 40 40" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round">
          <path d="M5 33h30"/>
          <path d="M5 33Q19 -4 33 33"/>
          <path d="M5 33l15-9" stroke-dasharray="2 3.5"/>
          <circle cx="19" cy="12.5" r="3.2" fill="currentColor" stroke="none"/>
        </svg>
      </div>
      <span class="brand-tag">Laboratorio de Estudio Pre-Saber 11</span>
    </div>
    <h1>Aprende el Saber 11 probando tú mismo</h1>
    <p class="lede">11 laboratorios interactivos, diagnóstico adaptativo en 10 min, práctica por temas y simulacros tipo examen real.</p>
    <div class="badges">
      <span class="badge highlight">✓ 100% Gratuito</span>
      <span class="badge">Matemáticas · Lectura · Ciencias · Sociales · Inglés</span>
      <span class="badge">Plataforma Independiente</span>
    </div>
  </div>
  <div class="footer">
    <span class="domain">https://icfes.edevcore.com</span>
    <span>Preparación de alta calidad para estudiantes de grado 11 en Colombia</span>
  </div>
</body>
</html>
  `;

  await page.setContent(html);
  await page.screenshot({ path: 'public/og-image.png' });
  console.log('Saved public/og-image.png');
  await browser.close();
}

main().catch(err => {
  console.error(err);
  process.exit(1);
});
