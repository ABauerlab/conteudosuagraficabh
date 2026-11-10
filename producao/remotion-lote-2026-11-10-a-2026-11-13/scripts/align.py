"""Alinhamento de legendas ao bruto SEM transcrição.

Usa apenas a detecção de pausas (silencedetect, análise; o áudio não é alterado)
e a contagem aproximada de sílabas do teleprompter. Gera blocos de legenda de
uma linha e relata o quanto os finais de frase previstos coincidem com pausas
reais (métrica de confiança). Se a confiança for baixa, a legenda do trecho é
omitida, conforme PROMPT-UNICO-CLAUDE.md.
"""
import json, re, subprocess, sys, unicodedata

VOW = 'aeiouáéíóúâêôãõày'


def sil(s):
    w = unicodedata.normalize('NFC', s.lower())
    w = re.sub(r'[^a-záéíóúâêôãõàçü]', '', w)
    if not w:
        return 0
    # grupos vocálicos ~ sílabas (ditongos contam 1)
    g = re.findall(r'[aeiouáéíóúâêôãõàü]+', w)
    n = 0
    for x in g:
        n += 1 if len(x) <= 2 else 2
    return max(1, n)


def pauses(path, db=-30, d=0.12):
    out = subprocess.run(['ffmpeg', '-v', 'info', '-i', path, '-af', f'silencedetect=noise={db}dB:d={d}', '-vn', '-f', 'null', '-'],
                         capture_output=True, text=True).stderr
    st = [float(x) for x in re.findall(r'silence_start: ([0-9.]+)', out)]
    en = [float(x) for x in re.findall(r'silence_end: ([0-9.]+)', out)]
    dur = float(re.search(r'Duration: (\d+):(\d+):([0-9.]+)', out).group(3)) + 60 * int(re.search(r'Duration: (\d+):(\d+)', out).group(2))
    ps = list(zip(st, en + [dur] * (len(st) - len(en))))
    return ps, dur


def chunks(sentence, maxc=26):
    words = sentence.split()
    out, cur = [], []
    for w in words:
        cand = ' '.join(cur + [w])
        if cur and len(cand) > maxc:
            out.append(' '.join(cur)); cur = [w]
        else:
            cur.append(w)
        if re.search(r'[,:;?]$', w) and len(' '.join(cur)) >= 12:
            out.append(' '.join(cur)); cur = []
    if cur:
        out.append(' '.join(cur))
    # evita sobra de uma palavra curta
    if len(out) > 1 and len(out[-1]) < 8:
        out[-2] = out[-2] + ' ' + out[-1]; out.pop()
    return out


def anchor(items, sentences, ps, dur, speech, at, S, total):
    """Ancora finais de frase em pausas reais (programação dinâmica monotônica)."""
    import math
    # tempo proporcional do fim de cada frase
    acc=0; tau=[]
    for si in range(len(sentences)-1):
        acc=sum(i['syl'] for i in items if i['sent']<=si)
        tau.append(at(acc/S*total))
    P=[(s,e) for s,e in ps if s>0.3 and e<dur-0.3]
    n,m=len(tau),len(P)
    INF=1e9; PEN=1.0
    # dp[i][j]: melhor custo usando frases[:i] e pausas[:j]
    dp=[[INF]*(m+1) for _ in range(n+1)]; bk={}
    for j in range(m+1): dp[0][j]=0
    for i in range(1,n+1):
        for j in range(0,m+1):
            # frase i-1 sem âncora
            best=dp[i-1][j]+PEN; arg=('skip',j)
            if j>0:
                # usa pausa j-1
                c=abs((P[j-1][0]+P[j-1][1])/2-tau[i-1])
                if c<3.0:
                    for jj in range(j):
                        v=dp[i-1][jj]+c
                        if v<best: best=v; arg=('use',jj)
                # ou ignora a pausa j-1
                if dp[i][j-1]<best: best=dp[i][j-1]; arg=('ign',j-1)
            dp[i][j]=best; bk[(i,j)]=arg
    i,j=n,m; anchors={}
    while i>0:
        a=bk[(i,j)]
        if a[0]=='skip': i-=1
        elif a[0]=='ign': j=a[1]
        else: anchors[i-1]=P[j-1]; i-=1; j=a[1]
    return anchors, tau


def align(path, sentences):
    ps, dur = pauses(path)
    # intervalos de fala = complemento das pausas
    speech, t = [], 0.0
    for s, e in ps:
        if s - t > 0.05:
            speech.append((t, s))
        t = max(t, e)
    if dur - t > 0.05:
        speech.append((t, dur))
    total = sum(b - a for a, b in speech)

    def at(x):  # tempo de fala acumulado -> tempo real
        acc = 0.0
        for a, b in speech:
            if acc + (b - a) >= x:
                return a + (x - acc)
            acc += b - a
        return speech[-1][1]

    items = []
    for si, s in enumerate(sentences):
        for c in chunks(s):
            items.append({'text': c, 'sent': si, 'syl': sum(sil(w) for w in c.split())})
    S = sum(i['syl'] for i in items)
    acc = 0
    for it in items:
        it['start'] = at(acc / S * total)
        acc += it['syl']
        it['end'] = at(acc / S * total)
    anchors, tau = anchor(items, sentences, ps, dur, speech, at, S, total)
    # pontos de controle (tempo previsto -> tempo real)
    first = speech[0][0]; last = speech[-1][1]
    ctrl = [(first, first)] + sorted((tau[k], anchors[k][0]) for k in anchors) + [(last, last)]
    def remap(x):
        for (a0, b0), (a1, b1) in zip(ctrl, ctrl[1:]):
            if a0 <= x <= a1 and a1 > a0:
                return b0 + (x - a0) * (b1 - b0) / (a1 - a0)
        return x
    for it in items:
        it['start'] = remap(it['start']); it['end'] = remap(it['end'])
    for k, (s, e) in anchors.items():
        nxt = [i for i in items if i['sent'] == k + 1]
        if nxt: nxt[0]['start'] = e
    unanch = [k for k in range(len(sentences) - 1) if k not in anchors]
    # encaixe nas pausas: início de bloco vai para o fim da pausa próxima (±0.45 s)
    ends = [e for s, e in ps if e > 0.05]
    starts = [s for s, e in ps]
    for it in items:
        near = [e for e in ends if abs(e - it['start']) < 0.45]
        if near:
            it['start'] = min(near, key=lambda e: abs(e - it['start']))
        nearS = [s for s in starts if abs(s - it['end']) < 0.45]
        if nearS:
            it['end'] = min(nearS, key=lambda s: abs(s - it['end']))
    for a, b in zip(items, items[1:]):
        if b['start'] < a['end']:
            m = (a['end'] + b['start']) / 2
            a['end'] = b['start'] = m
        elif b['start'] - a['end'] < 0.35:
            a['end'] = b['start']
    # confiança: fim previsto de cada frase vs pausa mais próxima
    errs = []
    for si in range(len(sentences)):
        e = max(i['end'] for i in items if i['sent'] == si)
        if si < len(sentences) - 1:
            errs.append(round(min(abs(s - e) for s in starts), 2) if starts else 9)
    rate = S / total
    return {'unanchored': unanch, 'anchors': anchors, 'items': items, 'pauses': ps, 'dur': dur, 'speech': speech, 'rate': rate, 'sentErr': errs}


if __name__ == '__main__':
    path = sys.argv[1]
    sents = json.load(open(sys.argv[2]))
    r = align(path, sents)
    print('dur %.2f  sil/s %.2f  err %s  sem ancora %s/%d' % (r['dur'], r['rate'], r['sentErr'], r['unanchored'], len(sents)-1))
    for i in r['items']:
        print('%6.2f %6.2f  %s' % (i['start'], i['end'], i['text']))
