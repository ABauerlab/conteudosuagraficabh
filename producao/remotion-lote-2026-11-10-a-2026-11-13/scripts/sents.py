import re,sys,json
B='/home/claude/conteudosuagraficabh/conteudos/lote-2026-11-04-a-2026-11-11/REELS/'
def sents(id):
    t=open(B+f'SG-{id}.md',encoding='utf-8').read()
    tp=t.split('## Teleprompter integral')[1].split('\n## ')[0]
    tp=' '.join(l.strip() for l in tp.strip().splitlines() if l.strip())
    return [s.strip() for s in re.split(r'(?<=[.?!])\s+',tp) if s.strip()]
if __name__=='__main__':
    for id in sys.argv[1:]:
        json.dump(sents(id),open(f'sents-{id}.json','w'),ensure_ascii=False)
