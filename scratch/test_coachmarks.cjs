const puppeteer = require('puppeteer-core');
const fs = require('fs');
const path = require('path');

const CAPTURE_DIR = path.resolve(__dirname, '../docs/capturas/coachmarks');
if (!fs.existsSync(CAPTURE_DIR)) {
  fs.mkdirSync(CAPTURE_DIR, { recursive: true });
}

async function run() {
  const browser = await puppeteer.launch({
    executablePath: '/opt/google/chrome/chrome',
    args: ['--no-sandbox', '--disable-setuid-sandbox', '--disable-dev-shm-usage', '--disable-gpu'],
    headless: 'new'
  });

  const screens = [
    { id: 'inicio', url: 'http://127.0.0.1:5173/#/' },
    { id: 'diag', url: 'http://127.0.0.1:5173/#/diag' },
    { id: 'pregunta', url: 'http://127.0.0.1:5173/#/pregunta/mat-001' },
    { id: 'aprender', url: 'http://127.0.0.1:5173/#/aprender' },
    { id: 'practicar', url: 'http://127.0.0.1:5173/#/practicar' },
    { id: 'simulacro', url: 'http://127.0.0.1:5173/#/simulacro' },
    { id: 'panel', url: 'http://127.0.0.1:5173/#/panel' }
  ];

  console.log('Testing Mobile (390x844)...');
  const pageMobile = await browser.newPage();
  await pageMobile.setViewport({ width: 390, height: 844, deviceScaleFactor: 2, isMobile: true, hasTouch: true });

  const results = [];

  for (const scr of screens) {
    console.log(`\nNavigating to ${scr.id} on Mobile...`);
    await pageMobile.goto(scr.url, { waitUntil: 'networkidle0' });
    await pageMobile.evaluate(() => {
      try { localStorage.clear(); } catch (e) {}
    });
    await pageMobile.reload({ waitUntil: 'networkidle0' });
    await new Promise((r) => setTimeout(r, 650));

    // Check if coachmark overlay appeared
    let overlay = await pageMobile.$('.coachmark-overlay');
    if (!overlay) {
      console.log(`Triggering help button for ${scr.id}...`);
      const helpBtn = await pageMobile.$('.help-coachmark-btn');
      if (helpBtn) await helpBtn.click();
      await new Promise((r) => setTimeout(r, 400));
      overlay = await pageMobile.$('.coachmark-overlay');
    }

    if (!overlay) {
      console.warn(`WARNING: Coachmark overlay did not appear for ${scr.id}`);
      results.push({ screen: scr.id, device: 'mobile', success: false, reason: 'No overlay' });
      continue;
    }

    // Capture step 1
    const fileStep1 = path.join(CAPTURE_DIR, `${scr.id}_mobile_paso1.png`);
    await pageMobile.screenshot({ path: fileStep1 });
    console.log(`Saved screenshot: ${fileStep1}`);

    // Check geometry: bubble bounds within viewport, non-clipping
    const bubbleGeo = await pageMobile.evaluate(() => {
      const b = document.querySelector('.coachmark-bubble');
      if (!b) return null;
      const r = b.getBoundingClientRect();
      const text = document.querySelector('.coachmark-text')?.textContent || '';
      const step = document.querySelector('.coachmark-step-count')?.textContent || '';
      return {
        left: r.left,
        top: r.top,
        right: r.right,
        bottom: r.bottom,
        width: r.width,
        height: r.height,
        vw: window.innerWidth,
        vh: window.innerHeight,
        text,
        step,
        wordCount: text.trim().split(/\s+/).length
      };
    });

    const clipped = bubbleGeo.left < 0 || bubbleGeo.right > bubbleGeo.vw || bubbleGeo.top < 0 || bubbleGeo.bottom > bubbleGeo.vh;
    console.log(`Geometry check for ${scr.id} mobile:`, {
      clipped,
      wordCount: bubbleGeo.wordCount,
      text: bubbleGeo.text,
      step: bubbleGeo.step
    });

    results.push({
      screen: scr.id,
      device: 'mobile',
      success: !clipped,
      stepCount: bubbleGeo.step,
      wordCount: bubbleGeo.wordCount,
      bubbleGeo
    });

    // Advance to next step
    const nextBtn = await pageMobile.$('.coachmark-next-btn');
    if (nextBtn) {
      await nextBtn.click();
      await new Promise((r) => setTimeout(r, 400));
      const fileStep2 = path.join(CAPTURE_DIR, `${scr.id}_mobile_paso2.png`);
      await pageMobile.screenshot({ path: fileStep2 });
      console.log(`Saved screenshot step 2: ${fileStep2}`);
    }
  }

  // Desktop (1280x800)
  console.log('\nTesting Desktop (1280x800)...');
  const pageDesk = await browser.newPage();
  await pageDesk.setViewport({ width: 1280, height: 800, deviceScaleFactor: 1 });

  for (const scr of screens) {
    console.log(`Navigating to ${scr.id} on Desktop...`);
    await pageDesk.goto(scr.url, { waitUntil: 'networkidle0' });
    await pageDesk.evaluate(() => {
      try { localStorage.clear(); } catch (e) {}
    });
    await pageDesk.reload({ waitUntil: 'networkidle0' });
    await new Promise((r) => setTimeout(r, 650));

    let overlay = await pageDesk.$('.coachmark-overlay');
    if (!overlay) {
      const helpBtn = await pageDesk.$('.help-coachmark-btn');
      if (helpBtn) await helpBtn.click();
      await new Promise((r) => setTimeout(r, 400));
      overlay = await pageDesk.$('.coachmark-overlay');
    }

    if (overlay) {
      const fileDesk = path.join(CAPTURE_DIR, `${scr.id}_desktop_paso1.png`);
      await pageDesk.screenshot({ path: fileDesk });
      console.log(`Saved screenshot desktop: ${fileDesk}`);
    }
  }

  // Test FAQ page
  console.log('\nTesting FAQ page (#/faq)...');
  await pageDesk.goto('http://127.0.0.1:5173/#/faq', { waitUntil: 'networkidle0' });
  const faqTitle = await pageDesk.title();
  const faqMetaDesc = await pageDesk.evaluate(() => document.querySelector('meta[name="description"]')?.content);
  console.log('FAQ Title:', faqTitle);
  console.log('FAQ Meta Description:', faqMetaDesc);
  const faqFile = path.join(CAPTURE_DIR, `faq_desktop.png`);
  await pageDesk.screenshot({ path: faqFile, fullPage: true });

  await pageMobile.goto('http://127.0.0.1:5173/#/faq', { waitUntil: 'networkidle0' });
  const faqMobileFile = path.join(CAPTURE_DIR, `faq_mobile.png`);
  await pageMobile.screenshot({ path: faqMobileFile, fullPage: true });

  await browser.close();

  console.log('\n--- EVALUATION SUMMARY ---');
  console.log(JSON.stringify(results, null, 2));
}

run().catch((err) => {
  console.error(err);
  process.exit(1);
});
