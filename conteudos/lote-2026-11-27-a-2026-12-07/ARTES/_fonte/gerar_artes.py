import re, sys, html, json, pathlib, asyncio
from playwright.async_api import async_playwright

LOTE = pathlib.Path('.')
ASSETS = pathlib.Path('/home/claude/work/assets')
OUT = pathlib.Path('/home/claude/work/out')

C = dict(cy='#00A6D6', ma='#E6007E', ye='#FFD500', bk='#171717', wh='#FFFFFF', ow='#F7F7F4')
# (background, text, accent, support text)
THEMES = [
    ('#171717', '#FFFFFF', '#FFD500', '#D9D9D9'),
    ('#FFD500', '#171717', '#E6007E', '#2b2b2b'),
    ('#00A6D6', '#FFFFFF', '#FFD500', '#F0FBFF'),
    ('#F7F7F4', '#171717', '#E6007E', '#3a3a3a'),
    ('#E6007E', '#FFFFFF', '#FFD500', '#FFE9F4'),
]

def esc(s):
    return html.escape(s, quote=False)

def md_inline(s):
    s = esc(s.strip())
    return re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', s)

def parse_feed(path):
    t = path.read_text(encoding='utf-8')
    sid = re.search(r'# (SG-\d+)', t).group(1)
    slides = []
    for m in re.finditer(r'### Slide (\d+) — (.+?)\n(.*?)(?=\n### Slide|\n## )', t, re.S):
        n, title, body = m.groups()
        tm = re.search(r'\*\*Texto final:\*\*\s*(.*?)(?=\n- \*\*Função)', body, re.S)
        slides.append(dict(n=int(n), name=title.strip(), text=tm.group(1).strip()))
    return sid, slides

def parse_story(path):
    t = path.read_text(encoding='utf-8')
    sid = re.search(r'# (SG-\d+)', t).group(1)
    title = re.search(r'\*\*Título:\*\*\s*(.+)', t).group(1).strip()
    ap = re.search(r'\*\*(?:Texto de apoio|Apoio):\*\*\s*(.*?)(?=\n\*\*CTA na tela)', t, re.S).group(1).strip()
    cta = re.search(r'\*\*CTA na tela:\*\*\s*(.+)', t).group(1).strip()
    return sid, dict(title=title, apoio=ap, cta=cta)

BASE_CSS = """
*{box-sizing:border-box;margin:0;padding:0}
html,body{width:%(w)dpx;height:%(h)dpx;overflow:hidden}
body{font-family:'Inter',sans-serif;background:%(bg)s;color:%(fg)s;position:relative}
.disp{font-family:'Inter Display','Inter',sans-serif}
.lab{font-weight:500;text-transform:uppercase;letter-spacing:.3em}
.faixa{position:absolute;left:0;right:0;height:16px;display:flex}
.faixa i{flex:1}
.faixa i:nth-child(1){background:#00A6D6}.faixa i:nth-child(2){background:#E6007E}.faixa i:nth-child(3){background:#FFD500}.faixa i:nth-child(4){background:#171717}
"""

def logo_for(bg):
    f = {'#FFD500':'logo_horiz_claro.svg','#F7F7F4':'logo_horiz_claro.svg','#00A6D6':'logo_horiz_branco.svg','#E6007E':'logo_horiz_branco.svg'}.get(bg,'logo_horiz_escuro.svg')
    return f'file:///home/claude/work/assets/{f}'

def faixa(top=None, bottom=None):
    pos = f'top:{top}px' if top is not None else f'bottom:{bottom}px'
    return f'<div class="faixa" style="{pos}"><i></i><i></i><i></i><i></i></div>'

def fit(text, base, width=912, k=0.62):
    mw = max(len(w) for w in re.split(r'\s+', text)) or 1
    return int(min(base, width / (mw * k)))

def fit_size_old(text, base, minimum, width_chars):
    n = len(text)
    s = base
    while s > minimum and n * s * 0.52 > width_chars * base * 0.52 * (base / s) * 1.0 and False:
        s -= 4
    return s

def slide_html(sid, s, total, idx):
    w, h = 1080, 1350
    bg, fg, ac, sup = THEMES[[0, 3, 1, 2, 4, 0, 3][idx % 7]]
    if s['n'] == 1:
        bg, fg, ac, sup = THEMES[0]
    if s['n'] == total:
        bg, fg, ac, sup = THEMES[0]
    lines = [l.strip() for l in s['text'].split('\n') if l.strip()]
    css = BASE_CSS % dict(w=w, h=h, bg=bg, fg=fg)
    header = f'<div class="lab" style="position:absolute;left:84px;top:84px;font-size:22px;color:{ac}">{s["n"]:02d} / {total:02d}</div>'
    symf = 'simbolo_branco.svg' if bg in ('#00A6D6','#E6007E') else 'simbolo_colorido.svg'
    sym = f'<img src="file:///home/claude/work/assets/{symf}" style="position:absolute;right:84px;top:64px;height:64px">'
    if bg == '#00A6D6': ac = '#FFFFFF'
    body = ''
    if s['n'] == 1:
        title = lines[0]
        sub = ' '.join(lines[1:])
        fs = fit(title, 150 if len(title) < 22 else (128 if len(title) < 34 else 104), k=0.68)
        body = f'''
        <img src="file:///home/claude/work/assets/logo_horiz_escuro.svg" style="position:absolute;left:84px;top:84px;height:48px">
        <div style="position:absolute;left:84px;right:84px;top:360px">
          <div class="disp" style="font-weight:900;font-size:{fs}px;line-height:.98;letter-spacing:-.01em;word-spacing:.06em;color:{fg}">{esc(title)}</div>
          <div style="width:140px;height:12px;background:{ac};margin:56px 0 44px"></div>
          <div style="font-weight:600;font-size:46px;line-height:1.25;color:{ac}">{esc(sub)}</div>
        </div>
        <div class="lab" style="position:absolute;left:84px;bottom:88px;font-size:22px;color:{sup}">Deslize para ver →</div>'''
        return css, body + faixa(bottom=0)
    if s['n'] == total:
        title = lines[0]
        sub = ' '.join(lines[1:])
        body = f'''
        {header}
        <div style="position:absolute;left:84px;right:84px;top:330px">
          <div class="disp" style="font-weight:900;font-size:{fit(title,132,k=0.6)}px;line-height:1;letter-spacing:-.01em;word-spacing:.06em">{esc(title)}</div>
          <div style="width:140px;height:12px;background:{ac};margin:52px 0 44px"></div>
          <div style="font-weight:600;font-size:50px;line-height:1.25;color:{ac}">{esc(sub)}</div>
        </div>
        <img src="file:///home/claude/work/assets/logo_horiz_escuro.svg" style="position:absolute;left:84px;bottom:96px;height:52px">'''
        return css, body + faixa(bottom=0)
    # content slide
    first = lines[0]
    m = re.match(r'^(\d+)\.\s*(.*)$', first)
    num = m.group(1) if m else None
    head = m.group(2) if m else first
    rest = lines[1:]
    fs = fit(head, 92 if len(head) < 48 else (80 if len(head) < 80 else (68 if len(head) < 120 else 58)), k=0.6)
    rest_html = ''.join(f'<p style="margin-top:30px">{esc(r)}</p>' for r in rest)
    num_html = f'<div class="disp" style="font-weight:900;font-size:300px;line-height:.8;color:{ac};letter-spacing:-.04em;margin-bottom:36px">{num}</div>' if num else f'<div style="width:120px;height:12px;background:{ac};margin-bottom:48px"></div>'
    body = f'''
    {header}{sym}
    <div style="position:absolute;left:84px;right:84px;top:250px;bottom:150px;display:flex;flex-direction:column;justify-content:center">
      {num_html}
      <div class="disp" style="font-weight:800;font-size:{fs}px;line-height:1.06;letter-spacing:-.005em;word-spacing:.05em">{esc(head)}</div>
      <div style="font-weight:500;font-size:44px;line-height:1.3;color:{sup}">{rest_html}</div>
    </div>'''
    return css, body + faixa(bottom=0)

def story_html(sid, st, idx):
    w, h = 1080, 1920
    bg, fg, ac, sup = THEMES[[0, 2, 0, 4, 0, 1, 3][idx % 7]]
    css = BASE_CSS % dict(w=w, h=h, bg=bg, fg=fg)
    # apoio items
    raw = [l.strip() for l in st['apoio'].split('\n') if l.strip()]
    items = []
    if len(raw) > 1:
        items = raw
    else:
        one = raw[0]
        parts = re.split(r'(?<=[?!.])\s+', one) if '?' in one and one.count('?') > 1 else [one]
        if len(parts) > 1:
            items = parts
        else:
            items = [one]
    title = st['title']
    fs = fit(title, 118 if len(title) < 26 else (100 if len(title) < 40 else 86), width=912, k=0.68)
    cards = ''
    if len(items) > 1:
        for i, it in enumerate(items):
            mm = re.match(r'^(\d+)\.\s*(.*)$', it)
            label = mm.group(1) if mm else str(i + 1)
            txt = mm.group(2) if mm else it
            col = [ac, '#00A6D6', '#E6007E', '#FFD500'][i % 4] if bg == '#171717' else fg
            cards += f'''<div style="display:flex;align-items:center;gap:36px;padding:34px 40px;border-radius:28px;background:{'rgba(255,255,255,.08)' if bg=='#171717' else 'rgba(255,255,255,.18)'};margin-bottom:26px">
              <div class="disp" style="font-weight:900;font-size:84px;line-height:1;color:{col};min-width:70px">{label}</div>
              <div style="font-weight:700;font-size:48px;line-height:1.2">{esc(txt)}</div></div>'''
    else:
        cards = f'<div style="font-weight:600;font-size:54px;line-height:1.3;color:{sup}">{esc(items[0])}</div>'
    body = f'''
    <img src="{logo_for(bg)}" style="position:absolute;left:84px;top:250px;height:44px">
    <div class="lab" style="position:absolute;right:84px;top:258px;font-size:20px;color:{fg}">Stories</div>
    <div style="position:absolute;left:84px;right:84px;top:420px;bottom:560px;display:flex;flex-direction:column;justify-content:center">
      <div style="width:120px;height:12px;background:{ac};margin-bottom:48px"></div>
      <div class="disp" style="font-weight:900;font-size:{fs}px;line-height:1.02;letter-spacing:-.005em;word-spacing:.08em;margin-bottom:64px">{esc(title)}</div>
      {cards}
    </div>
    <div style="position:absolute;left:84px;right:84px;bottom:340px;padding:34px 44px;border-radius:999px;background:{ac};color:{'#171717' if ac in ('#FFD500','#00A6D6') else '#FFFFFF'};font-weight:800;font-size:42px;text-align:center">{esc(st['cta'])}</div>'''
    return css, body + faixa(bottom=0)

PAGE = '<!doctype html><html><head><meta charset="utf-8"><style>%s</style></head><body>%s</body></html>'

async def render(items):
    async with async_playwright() as p:
        b = await p.chromium.launch(args=['--allow-file-access-from-files'])
        for path, w, h, css, body in items:
            page = await b.new_page(viewport={'width': w, 'height': h})
            tmp = pathlib.Path('/home/claude/work/tmp.html')
            tmp.write_text(PAGE % (css, body), encoding='utf-8')
            await page.goto('file://' + str(tmp))
            await page.wait_for_timeout(150)
            await page.screenshot(path=str(path), type='png')
            await page.close()
        await b.close()

def main(only=None):
    jobs = []
    for f in sorted((LOTE / 'FEED').glob('SG-*.md')):
        sid, slides = parse_feed(f)
        if only and sid not in only: continue
        d = OUT / sid; d.mkdir(parents=True, exist_ok=True)
        for i, s in enumerate(slides):
            css, body = slide_html(sid, s, len(slides), i)
            jobs.append((d / f'{sid}-FEED-{s["n"]:02d}.png', 1080, 1350, css, body))
    for i, f in enumerate(sorted((LOTE / 'STORIES').glob('SG-*.md'))):
        sid, st = parse_story(f)
        if only and sid not in only: continue
        d = OUT / sid; d.mkdir(parents=True, exist_ok=True)
        css, body = story_html(sid, st, i)
        jobs.append((d / f'{sid}-STORY-01.png', 1080, 1920, css, body))
    asyncio.run(render(jobs))
    print(len(jobs), 'arquivos')

if __name__ == '__main__':
    main(set(sys.argv[1:]) or None)
