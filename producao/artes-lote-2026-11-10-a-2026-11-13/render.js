// Gerador das artes SG-025 a SG-048 (capas de Reels, carrosséis e Stories).
// Fonte editável: altere pecas.js e rode `node render.js <pasta-brandkit> <pasta-saida>`.
// Logotipo: arquivo oficial do Brand Kit, inserido sem alteração. Fonte oficial: Inter.
const fs = require('fs');
const path = require('path');
const { chromium } = require('playwright');
const { pecas } = require('./pecas');

const BRAND = process.argv[2];
const OUT = process.argv[3];
const logo = (v) => 'data:image/png;base64,' + fs.readFileSync(path.join(BRAND, v === 'escuro' ? 'logo_h_escuro.png' : 'logo_h_claro.png')).toString('base64');

const C = { ciano: '#00A6D6', magenta: '#E6007E', amarelo: '#FFD500', preto: '#171717', branco: '#FFFFFF', off: '#F7F7F4', cinza: '#A7A7A7' };
const esc = (s) => s.replace(/&/g, '&amp;').replace(/</g, '&lt;');

// Ilustrações vetoriais originais e genéricas (sem marcas de terceiros).
const ilu = {
  selos: (n = 10, cheios = 6, cor = C.magenta) => `<svg viewBox="0 0 700 300" width="100%"><rect x="4" y="4" width="692" height="292" rx="28" fill="#fff" stroke="${C.preto}" stroke-width="6"/>${Array.from({ length: n }, (_, i) => { const x = 85 + (i % 5) * 132, y = 95 + Math.floor(i / 5) * 115; return `<circle cx="${x}" cy="${y}" r="42" fill="${i < cheios ? cor : 'none'}" stroke="${C.preto}" stroke-width="5"/>${i < cheios ? `<path d="M${x - 16} ${y} l11 12 l22 -24" stroke="#fff" stroke-width="8" fill="none" stroke-linecap="round"/>` : ''}`; }).join('')}</svg>`,
  calendario: (cor = C.ciano, destaque = [5, 12, 19]) => `<svg viewBox="0 0 560 460" width="100%"><rect x="6" y="40" width="548" height="414" rx="26" fill="#fff" stroke="${C.preto}" stroke-width="6"/><rect x="6" y="40" width="548" height="90" rx="26" fill="${cor}"/><rect x="6" y="100" width="548" height="30" fill="${cor}"/><text x="280" y="102" font-family="Inter" font-weight="800" font-size="44" fill="#fff" text-anchor="middle">JULHO 2027</text>${[120, 220, 340, 440].map((x) => `<rect x="${x}" y="8" width="16" height="60" rx="8" fill="${C.preto}"/>`).join('')}${Array.from({ length: 28 }, (_, i) => { const x = 60 + (i % 7) * 74, y = 185 + Math.floor(i / 7) * 68; const d = destaque.includes(i + 1); return `${d ? `<circle cx="${x}" cy="${y - 12}" r="28" fill="${C.amarelo}"/>` : ''}<text x="${x}" y="${y}" font-family="Inter" font-weight="${d ? 800 : 500}" font-size="30" fill="${C.preto}" text-anchor="middle">${i + 1}</text>`; }).join('')}</svg>`,
  cardapio: (cor = C.magenta) => `<svg viewBox="0 0 520 640" width="100%"><rect x="6" y="6" width="508" height="628" rx="22" fill="#fff" stroke="${C.preto}" stroke-width="6"/><text x="260" y="82" font-family="Inter" font-weight="900" font-size="44" fill="${C.preto}" text-anchor="middle">CARDÁPIO</text>${['ENTRADAS', 'PRATOS', 'BEBIDAS'].map((t, k) => `<text x="50" y="${165 + k * 160}" font-family="Inter" font-weight="800" font-size="26" fill="${cor}" letter-spacing="4">${t}</text>${[0, 1].map((j) => `<rect x="50" y="${190 + k * 160 + j * 48}" width="${260 - j * 60}" height="16" rx="8" fill="${C.preto}" opacity=".8"/><text x="470" y="${205 + k * 160 + j * 48}" font-family="Inter" font-weight="700" font-size="24" fill="${C.preto}" text-anchor="end">R$ 00</text>`).join('')}`).join('')}</svg>`,
  tag: (cor = C.amarelo, verso = false) => `<svg viewBox="0 0 300 560" width="100%"><path d="M150 0 C150 40 150 40 150 60" stroke="${C.preto}" stroke-width="5" fill="none"/><path d="M40 70 L260 70 L260 540 L40 540 Z" fill="${verso ? '#fff' : cor}" stroke="${C.preto}" stroke-width="6" stroke-linejoin="round"/><circle cx="150" cy="118" r="18" fill="${C.off}" stroke="${C.preto}" stroke-width="5"/>${verso ? `<text x="150" y="220" font-family="Inter" font-weight="800" font-size="28" fill="${C.preto}" text-anchor="middle">TAMANHO</text>${['P', 'M', 'G', 'GG'].map((t, i) => `<rect x="${62 + i * 46}" y="245" width="38" height="38" rx="6" fill="none" stroke="${C.preto}" stroke-width="4"/><text x="${81 + i * 46}" y="273" font-family="Inter" font-weight="700" font-size="20" text-anchor="middle">${t}</text>`).join('')}<text x="150" y="350" font-family="Inter" font-weight="800" font-size="24" text-anchor="middle">CUIDADOS</text><rect x="70" y="370" width="160" height="12" rx="6" fill="${C.preto}" opacity=".6"/><rect x="90" y="394" width="120" height="12" rx="6" fill="${C.preto}" opacity=".6"/><rect x="100" y="440" width="100" height="70" rx="8" fill="none" stroke="${C.preto}" stroke-width="4"/><text x="150" y="485" font-family="Inter" font-weight="700" font-size="20" text-anchor="middle">@sualoja</text>` : `<text x="150" y="330" font-family="Inter" font-weight="900" font-size="54" fill="${C.preto}" text-anchor="middle">SUA</text><text x="150" y="390" font-family="Inter" font-weight="900" font-size="54" fill="${C.preto}" text-anchor="middle">MARCA</text>`}</svg>`,
  presente: (cor = C.magenta) => `<svg viewBox="0 0 400 380" width="100%"><rect x="30" y="140" width="340" height="230" rx="16" fill="${cor}" stroke="${C.preto}" stroke-width="6"/><rect x="10" y="90" width="380" height="70" rx="14" fill="${cor}" stroke="${C.preto}" stroke-width="6"/><rect x="175" y="90" width="50" height="280" fill="${C.amarelo}" stroke="${C.preto}" stroke-width="6"/><path d="M200 90 C140 10 80 50 130 90 M200 90 C260 10 320 50 270 90" stroke="${C.preto}" stroke-width="8" fill="none"/></svg>`,
};

function base(w, h, bg, corpo, opts = {}) {
  return `<!doctype html><html><head><meta charset="utf-8"><style>
  *{margin:0;padding:0;box-sizing:border-box}
  body{width:${w}px;height:${h}px;background:${bg};font-family:'Inter';color:${opts.txt || C.preto};overflow:hidden;position:relative}
  .disp{font-family:'Inter Display';font-weight:900;letter-spacing:-0.02em;line-height:1.02}
  .sub{font-weight:600;line-height:1.3}
  .eti{font-weight:500;text-transform:uppercase;letter-spacing:.3em;font-size:26px}
  .faixa{display:inline-block;padding:26px 36px;border-radius:18px;font-weight:800;font-size:44px;line-height:1.2}
  .cmyk{position:absolute;display:flex;gap:0}.cmyk i{display:block;width:120px;height:14px}
  </style></head><body>${corpo}</body></html>`;
}
const cmyk = (pos) => `<div class="cmyk" style="${pos}"><i style="background:${C.ciano}"></i><i style="background:${C.magenta}"></i><i style="background:${C.amarelo}"></i><i style="background:${C.preto}"></i></div>`;
const logoTag = (v, pos, w = 380) => `<img src="${logo(v)}" style="position:absolute;${pos};width:${w}px">`;

function htmlSlide(p, s, i, n) {
  const W = 1080, H = 1350;
  const escuro = s.bg === C.preto;
  const lv = escuro ? 'escuro' : 'claro';
  const linhas = s.texto.split('\n');
  const titulo = esc(linhas[0]);
  const apoio = linhas.slice(1).map(esc).join('<br>');
  if (s.tipo === 'capa') {
    return base(W, H, s.bg, `${cmyk('top:80px;left:80px')}
      <div class="eti" style="position:absolute;top:120px;left:80px;color:${escuro ? '#fff' : C.preto}">${esc(p.eti)}</div>
      <div class="disp" style="position:absolute;top:190px;left:80px;right:80px;font-size:${s.fs || 92}px;color:${escuro ? '#fff' : C.preto}">${titulo}</div>
      <div style="position:absolute;left:${s.iluLeft || 300}px;right:80px;bottom:150px">${s.ilu}</div>
      ${logoTag(lv, 'left:80px;bottom:70px', 320)}
      <div style="position:absolute;right:80px;bottom:72px;font-weight:700;font-size:28px;color:${escuro ? '#fff' : C.preto}">arraste →</div>`, { txt: escuro ? '#fff' : C.preto });
  }
  if (s.tipo === 'cta') {
    return base(W, H, s.bg, `${cmyk('top:80px;left:80px')}
      <div class="disp" style="position:absolute;top:170px;left:80px;right:80px;font-size:84px">${titulo}</div>
      <div style="position:absolute;top:${s.listaTop || 420}px;left:80px;right:80px">${(s.lista || []).map((t) => `<div style="display:flex;align-items:center;gap:22px;margin-bottom:22px;font-size:36px;font-weight:600"><span style="width:46px;height:46px;border-radius:50%;background:${p.cor};display:inline-flex;align-items:center;justify-content:center;color:#fff;font-weight:900;font-size:28px">✓</span>${esc(t)}</div>`).join('')}</div>
      <div class="faixa" style="position:absolute;left:80px;right:80px;bottom:220px;background:${p.cor};color:${p.cor === C.amarelo ? C.preto : '#fff'}">${apoio}</div>
      ${logoTag('claro', 'left:80px;bottom:90px', 420)}
      <div style="position:absolute;right:80px;bottom:100px;font-weight:600;font-size:26px">${i}/${n}</div>`);
  }
  return base(W, H, s.bg, `${cmyk('top:80px;left:80px')}
    <div class="eti" style="position:absolute;top:120px;left:80px;color:${p.cor === C.amarelo ? C.preto : p.cor}">${esc(p.eti)}</div>
    <div class="disp" style="position:absolute;top:180px;left:80px;right:80px;font-size:${s.fs || 76}px">${titulo}</div>
    <div class="sub" style="position:absolute;top:${s.apoioTop || 470}px;left:80px;right:80px;font-size:48px;color:#262626">${apoio}</div>
    <div style="position:absolute;left:${s.iluLeft || 260}px;right:${s.iluRight || 260}px;bottom:${s.iluBottom || 150}px">${s.ilu || ''}</div>
    ${logoTag('claro', 'left:80px;bottom:70px', 260)}
    <div style="position:absolute;right:80px;bottom:74px;font-weight:600;font-size:26px">${i}/${n}</div>`);
}

function htmlStory(st) {
  const W = 1080, H = 1920;
  const escuro = st.bg === C.preto || st.bg === C.magenta || st.bg === C.ciano;
  const txt = escuro ? '#fff' : C.preto;
  return base(W, H, st.bg, `
    ${cmyk('top:260px;left:90px')}
    <div class="eti" style="position:absolute;top:300px;left:90px;color:${txt}">${esc(st.eti)}</div>
    <div class="disp" style="position:absolute;top:370px;left:90px;right:90px;font-size:${st.fs || 96}px;color:${txt}">${esc(st.texto)}</div>
    <div style="position:absolute;left:${st.iluLeft || 260}px;right:${st.iluRight || 260}px;bottom:${st.iluBottom || 460}px">${st.ilu || ''}</div>
    ${st.cta ? `<div class="faixa" style="position:absolute;left:90px;right:90px;bottom:${st.ctaBottom || 560}px;background:${st.ctaCor};color:${st.ctaCor === C.amarelo ? C.preto : '#fff'};font-size:44px;text-align:center">${esc(st.cta)}</div>` : ''}
    ${logoTag(escuro ? 'escuro' : 'claro', 'left:90px;bottom:380px', 420)}`, { txt });
}

function htmlCapa(c) {
  const W = 1080, H = 1920;
  // Título e marca dentro da área central 4:5 (y 285 a 1635) para não cortar na grade do perfil.
  return base(W, H, c.bg, `
    <div style="position:absolute;inset:0;background:radial-gradient(circle at 85% 20%, ${c.cor}33 0, transparent 45%)"></div>
    ${cmyk('top:360px;left:90px')}
    <div class="eti" style="position:absolute;top:400px;left:90px;color:${c.bg === C.preto ? '#fff' : C.preto}">${esc(c.eti)}</div>
    <div class="disp" style="position:absolute;top:470px;left:90px;right:90px;line-height:1.16;font-size:${c.fs || 124}px;color:${c.bg === C.preto ? '#fff' : C.preto}">${c.titulo.split('|').map((t, k) => `<span style="${k === c.realce ? `background:${c.cor};color:${c.cor === C.amarelo ? C.preto : '#fff'};padding:2px 14px 8px;border-radius:10px;-webkit-box-decoration-break:clone` : ''}">${esc(t)}</span>`).join(' ')}</div>
    ${logoTag(c.bg === C.preto ? 'escuro' : 'claro', 'left:90px;top:1460px', 460)}`);
}

(async () => {
  fs.mkdirSync(OUT, { recursive: true });
  const b = await chromium.launch();
  const page = await b.newPage({ deviceScaleFactor: 1 });
  const shot = async (html, w, h, file) => {
    await page.setViewportSize({ width: w, height: h });
    await page.setContent(html, { waitUntil: 'load' });
    await page.evaluate(() => document.fonts.ready);
    const dir = path.join(OUT, file.slice(0, 6));
    fs.mkdirSync(dir, { recursive: true });
    await page.screenshot({ path: path.join(dir, file), type: 'png' });
  };
  const P = pecas(C, ilu);
  for (const c of P.capas) await shot(htmlCapa(c), 1080, 1920, `${c.id}-CAPA-1080x1920.png`);
  for (const p of P.carrosseis) for (const [k, s] of p.slides.entries()) await shot(htmlSlide(p, s, k + 1, p.slides.length), 1080, 1350, `${p.id}-SLIDE-${String(k + 1).padStart(2, '0')}.png`);
  for (const st of P.stories) await shot(htmlStory(st), 1080, 1920, `${st.id}-STORY.png`);
  await b.close();
  console.log('ok');
})();
