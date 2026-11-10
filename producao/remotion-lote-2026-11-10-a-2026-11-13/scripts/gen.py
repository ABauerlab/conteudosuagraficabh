"""Gera src/data/SG-xxx.ts (mapa fala -> motion) a partir do alinhamento por pausas.

Cada beat é ancorado a um trecho do teleprompter (T = início do trecho), então o
motion acompanha a fala sem transcrição. Legendas só nos Reels com sincronia
ancorada em pausas reais (ver CAPTIONS)."""
import json, re, sys
sys.path.insert(0, '/home/claude/work')
from align import align

PROJ = '/home/claude/conteudosuagraficabh/producao/remotion-lote-2026-11-10-a-2026-11-13'
RAW = '/home/claude/work/raw/SG-{}.mp4'
CAPTIONS = {'026', '031', '037', '043'}  # finais de frase ancorados em pausas reais
MUSIC = ['kulakovka-corporate-background-609167.mp3', 'the_mountain-corporate-background-576564.mp3',
         'alex-morgan-light-airy-soft-daylight-578475.mp3']


class Tl:
    def __init__(self, id):
        self.id = id
        self.sents = json.load(open(f'/home/claude/work/sents-{id}.json'))
        self.r = align(RAW.format(id), self.sents)
        self.items = self.r['items']
        sp = self.r['speech']
        self.start = max(0.0, sp[0][0] - 0.12)
        self.end = sp[-1][1] + 0.25
        self.full = ' '.join(self.sents)
        # índice de caracteres de cada bloco no texto completo
        pos = 0
        for it in self.items:
            i = self.full.find(it['text'], pos)
            it['c0'] = i; it['c1'] = i + len(it['text']); pos = it['c1']

    def T(self, phrase, after=0):
        i = self.full.find(phrase, after)
        if i < 0:
            raise ValueError(f'{self.id}: trecho não encontrado: {phrase}')
        for it in self.items:
            if it['c0'] <= i < it['c1'] + 1:
                f = (i - it['c0']) / max(1, it['c1'] - it['c0'])
                return round(it['start'] + f * (it['end'] - it['start']) - self.start, 2)
        raise ValueError(phrase)

    def E(self, phrase):
        """fim do bloco que contém o fim do trecho"""
        i = self.full.find(phrase) + len(phrase) - 1
        for it in self.items:
            if it['c0'] <= i < it['c1'] + 1:
                return round(it['end'] - self.start, 2)
        raise ValueError(phrase)


def ts(obj):
    return json.dumps(obj, ensure_ascii=False, indent=1)


def build(id, plan, n):
    tl = Tl(id)
    beats = plan(tl)
    dur = round(tl.end - tl.start, 2)
    # nada compete com o gancho: palavras e zooms só depois que ele sai
    hk = max(b['to'] for b in beats if b['kind'] == 'hook')
    for b in beats:
        if b['kind'] in ('word', 'zoom') and b['from'] < hk + 0.15:
            b['from'] = round(hk + 0.15, 2)
        if b['kind'] == 'panel' and b['from'] < hk + 0.5:
            b['from'] = round(hk + 0.5, 2)
    # palavras-chave não invadem cenas de motion (mesma área da janela do apresentador)
    pan = [b for b in beats if b['kind'] == 'panel']
    for b in beats:
        if b['kind'] != 'word':
            continue
        for p in pan:
            if p['from'] - 0.4 < b['to'] and b['from'] < p['from']:
                b['to'] = round(p['from'] - 0.4, 2)
            if p['from'] <= b['from'] < p['to'] + 0.4:
                b['from'] = round(p['to'] + 0.4, 2)
    beats = [b for b in beats if b['kind'] not in ('word', 'zoom') or b['to'] - b['from'] >= 0.6]
    # painéis não se sobrepõem
    panels = sorted([b for b in beats if b['kind'] == 'panel'], key=lambda b: b['from'])
    for a, b in zip(panels, panels[1:]):
        if a['to'] > b['from'] - 0.75:
            a['to'] = round(b['from'] - 0.75, 2)
    caps = []
    if id in CAPTIONS:
        for it in tl.items:
            caps.append({'text': it['text'], 'start': round(it['start'] - tl.start, 2), 'end': round(it['end'] - tl.start, 2)})
    data = {
        'id': f'SG-{id}', 'video': f'SG-{id}.mp4', 'start': round(tl.start, 2), 'duration': dur, 'tail': 1.2,
        'face': {'x': 540, 'y': 900}, 'captions': caps, 'beats': beats,
        'music': {'file': MUSIC[n % 3], 'volume': 0.07},
    }
    open(f'{PROJ}/src/data/SG-{id}.ts', 'w').write(
        "import type {ReelData} from '../reel/types';\n// Gerado por gen.py: tempos em segundos após o corte inicial.\n"
        f"export const SG{id}: ReelData = {ts(data)};\n")
    return tl, data


def it(text, at):
    return {'text': text, 'at': at}


# ---------------- Planos de edição por Reel ----------------
def p025(t):
    return [
        {'kind': 'hook', 'from': 0, 'to': 2.6, 'lines': ['Profissional não é', 'sinônimo de complicada.'], 'mark': 'complicada.'},
        {'kind': 'panel', 'variant': 'strike', 'theme': 'claro', 'from': t.T('um monte') - 0.2, 'to': t.E('Ela precisa ser clara.') + 0.3,
         'title': 'Não precisa de:', 'items': [it('efeitos', t.T('efeitos')), it('fontes diferentes', t.T('fontes')),
                                                it('elementos sofisticados', t.T('elementos')), it('clareza.', t.T('Ela precisa'))]},
        {'kind': 'panel', 'variant': 'list', 'theme': 'escuro', 'from': t.T('O título') - 0.2, 'to': t.E('entender a mensagem.'),
         'title': 'Comunicação clara', 'items': [it('Título fácil de achar', t.T('O título')), it('Texto confortável de ler', t.T('o texto')),
                                                 it('Imagens que explicam', t.T('e as imagens'))]},
        {'kind': 'zoom', 'from': t.T('Também'), 'to': t.E('com intenção.'), 'scale': 1.12},
        {'kind': 'word', 'from': t.T('cores com'), 'to': t.E('com intenção.') + 0.2, 'text': 'Com intenção', 'color': '#00A6D6'},
        {'kind': 'panel', 'variant': 'statement', 'theme': 'claro', 'from': t.T('Quando cada') - 0.2, 'to': t.E('mais confiança.'),
         'items': [it('Cada elemento,', t.T('Quando cada')), it('uma função.', t.T('uma função')), it('Mais confiança.', t.T('transmite'))]},
        {'kind': 'word', 'from': t.T('Na próxima'), 'to': t.E('não ajuda a mensagem.'), 'text': 'Tire 1 elemento', 'color': '#E6007E'},
        {'kind': 'zoom', 'from': t.T('Às vezes'), 'to': t.E('o que faltava.'), 'scale': 1.16},
        {'kind': 'word', 'from': t.T('simplificar'), 'to': t.E('o que faltava.') + 0.1, 'text': 'Simplificar'},
        {'kind': 'panel', 'variant': 'cta', 'theme': 'escuro', 'from': t.T('Compartilhe') - 0.1, 'to': 99, 'icon': 'icone_atendimento_colorido.png',
         'items': [it('Compartilhe com um empreendedor', t.T('Compartilhe'))]},
    ]


def p026(t):
    return [
        {'kind': 'hook', 'from': 0, 'to': 2.6, 'lines': ['Não adianta chamar atenção', 'e esconder o próximo passo.'], 'mark': 'passo.'},
        {'kind': 'word', 'from': t.T('atenção de'), 'to': t.E('Ótimo.'), 'text': 'Atenção ✓', 'color': '#00A6D6'},
        {'kind': 'word', 'from': t.T('Mas e depois'), 'to': t.E('Mas e depois?') + 0.2, 'text': 'E depois?', 'color': '#E6007E'},
        {'kind': 'zoom', 'from': t.T('A pessoa sabe'), 'to': t.E('falar com você?'), 'scale': 1.18},
        {'kind': 'panel', 'variant': 'list', 'theme': 'escuro', 'from': t.T('Em muita') - 0.2, 'to': t.E('mensagem principal.'),
         'title': 'Contato escondido fica:', 'items': [it('Perdido', t.T('perdido')), it('Pequeno', t.T('pequeno')), it('Longe da mensagem', t.T('ou distante'))]},
        {'kind': 'panel', 'variant': 'steps', 'theme': 'claro', 'from': t.T('Pense no caminho') - 0.2, 'to': t.E('continuar a conversa.'),
         'title': 'O caminho completo', 'items': [it('Entende o que você oferece', t.T('a pessoa entende')), it('Vê se faz sentido', t.T('identifica')),
                                                  it('Encontra como continuar', t.T('e encontra'))]},
        {'kind': 'word', 'from': t.T('confira se'), 'to': t.T('e se o contato') - 0.1, 'text': 'Próximo passo visível'},
        {'kind': 'word', 'from': t.T('e se o contato'), 'to': t.E('contato está correto.') + 0.1, 'text': 'Contato correto', 'color': '#00A6D6'},
        {'kind': 'zoom', 'from': t.T('Clareza também'), 'to': t.E('vida do cliente.'), 'scale': 1.14},
        {'kind': 'panel', 'variant': 'cta', 'theme': 'claro', 'from': t.T('Siga a SUA') - 0.1, 'to': 99, 'icon': 'icone_qualidade_colorido.png',
         'items': [it('Siga a SUA GRÁFICA BH', t.T('Siga a SUA'))]},
    ]


def p031(t):
    return [
        {'kind': 'hook', 'from': 0, 'to': 2.6, 'lines': ['A mesma mensagem não', 'funciona igual', 'para todo mundo.'], 'mark': 'todo'},
        {'kind': 'panel', 'variant': 'list', 'theme': 'claro', 'from': t.T('um restaurante') - 0.3, 'to': t.E('outras empresas.'),
         'title': 'Cada público lê diferente', 'items': [it('Restaurante', t.T('restaurante')), it('Loja', t.T('uma loja')),
                                                         it('Profissional liberal', t.T('um profissional')), it('Empresa que vende a empresas', t.T('ou uma empresa'))]},
        {'kind': 'panel', 'variant': 'statement', 'theme': 'escuro', 'from': t.T('O público muda') - 0.2, 'to': t.E('também muda.'),
         'items': [it('Público muda.', t.T('O público muda')), it('Linguagem muda.', t.T('a linguagem')), it('Destaque muda.', t.T('e a informação'))]},
        {'kind': 'word', 'from': t.T('Antes de criar'), 'to': t.T('quem vai ver') - 0.15, 'text': 'Antes de criar'},
        {'kind': 'panel', 'variant': 'steps', 'theme': 'claro', 'from': t.T('quem vai ver') - 0.2, 'to': t.E('faça depois?'),
         'title': '4 perguntas', 'items': [it('Quem vai ver?', t.T('quem vai ver')), it('O que já sabe?', t.T('O que essa')),
                                           it('Qual a dúvida?', t.T('Qual dúvida')), it('O que deve fazer depois?', t.T('E o que eu'))]},
        {'kind': 'panel', 'variant': 'compare', 'theme': 'escuro', 'from': t.T('Quando você conhece') - 0.2, 'to': t.E('para quem compra.'),
         'title': 'Conhecer o público muda o foco',
         'left': {'label': 'Antes', 'items': [it('Agradar a própria empresa', t.T('para de criar'))]},
         'right': {'label': 'Depois', 'items': [it('Fazer sentido para quem compra', t.T('e começa'))]}},
        {'kind': 'panel', 'variant': 'cta', 'theme': 'claro', 'from': t.T('Marca alguém') - 0.1, 'to': 99, 'icon': 'icone_atendimento_colorido.png',
         'items': [it('Marca alguém que empreende', t.T('Marca alguém'))]},
    ]


def p032(t):
    return [
        {'kind': 'hook', 'from': 0, 'to': 2.6, 'lines': ['Publicar não significa', 'que a mensagem chegou.'], 'mark': 'chegou.'},
        {'kind': 'panel', 'variant': 'compare', 'theme': 'claro', 'from': t.T('Divulgar é') - 0.2, 'to': t.E('aquilo significa.'),
         'title': 'Não é a mesma coisa',
         'left': {'label': 'Divulgar', 'items': [it('Colocar na frente das pessoas', t.T('colocar'))]},
         'right': {'label': 'Comunicar', 'items': [it('Fazer entender o que significa', t.T('Comunicar é'))]}},
        {'kind': 'zoom', 'from': t.T('Você pode publicar'), 'to': t.T('o que sua empresa') - 0.1, 'scale': 1.14},
        {'kind': 'word', 'from': t.T('todos os dias'), 'to': t.T('o que sua empresa') - 0.1, 'text': 'Todo dia, e dúvidas', 'color': '#E6007E'},
        {'kind': 'panel', 'variant': 'list', 'theme': 'escuro', 'from': t.T('o que sua empresa') - 0.15, 'to': t.E('prestar atenção?'),
         'title': 'As dúvidas que ficam', 'items': [it('O que sua empresa faz?', t.T('o que sua empresa')), it('Para quem trabalha?', t.T('para quem')),
                                                    it('Por que prestar atenção?', t.T('e por que'))]},
        {'kind': 'panel', 'variant': 'steps', 'theme': 'claro', 'from': t.T('Uma boa comunicação') - 0.2, 'to': t.E('próximo passo.'),
         'title': 'Boa comunicação', 'items': [it('Uma ideia por vez', t.T('escolhe')), it('Com clareza', t.T('apresenta')), it('Com próximo passo', t.T('e indica'))]},
        {'kind': 'panel', 'variant': 'strike', 'theme': 'escuro', 'from': t.T('Então, antes') - 0.2, 'to': t.E('nesta semana.'),
         'title': 'Troque a pergunta', 'items': [it('Quantas artes postar?', t.T('quantas artes')), it('Que mensagem passar?', t.T('pergunte qual'))]},
        {'kind': 'panel', 'variant': 'cta', 'theme': 'claro', 'from': t.T('Salve para') - 0.1, 'to': 99, 'icon': 'icone_orcamento_colorido.png',
         'items': [it('Salve para o seu planejamento', t.T('Salve para'))]},
    ]


def p037(t):
    return [
        {'kind': 'hook', 'from': 0, 'to': 2.6, 'lines': ['A criação começa antes', 'de abrir o programa.'], 'mark': 'antes'},
        {'kind': 'word', 'from': t.T('Teve uma ideia'), 'to': t.E('ideia de campanha?') + 0.1, 'text': 'Teve uma ideia?', 'color': '#00A6D6'},
        {'kind': 'panel', 'variant': 'steps', 'theme': 'claro', 'from': t.T('Antes de abrir') - 0.2, 'to': t.E('mensagem principal.'),
         'title': 'Antes do editor, anote', 'items': [it('Objetivo', t.T('o objetivo')), it('Público', t.T('o público')), it('Mensagem principal', t.T('e a mensagem'))]},
        {'kind': 'zoom', 'from': t.T('Depois pense'), 'to': t.E('vai aparecer.'), 'scale': 1.12},
        {'kind': 'word', 'from': t.T('no formato'), 'to': t.E('vai aparecer.'), 'text': 'Formato + local'},
        {'kind': 'panel', 'variant': 'compare', 'theme': 'escuro', 'from': t.T('O que funciona') - 0.2, 'to': t.E('material físico.'),
         'title': 'Cada lugar, um formato',
         'left': {'label': 'Tela', 'items': [it('Funciona de um jeito', t.T('O que funciona'))]},
         'right': {'label': 'Impresso', 'items': [it('Pode pedir outra organização', t.T('outra organização'))]}},
        {'kind': 'panel', 'variant': 'list', 'theme': 'claro', 'from': t.T('Só então') - 0.2, 'to': t.E('elementos visuais.'),
         'title': 'Só então escolha', 'items': [it('Imagens', t.T('imagens')), it('Textos', t.T('textos')), it('Elementos visuais', t.T('e elementos'))]},
        {'kind': 'zoom', 'from': t.T('E finalize'), 'to': t.E('conhece a campanha.'), 'scale': 1.16},
        {'kind': 'word', 'from': t.T('com o olhar'), 'to': t.E('conhece a campanha.'), 'text': 'Olhar de fora', 'color': '#E6007E'},
        {'kind': 'panel', 'variant': 'strike', 'theme': 'escuro', 'from': t.T('Esse processo') - 0.2, 'to': t.E('motivou o pedido.'),
         'items': [it('Arte só bonita', t.T('uma arte bonita')), it('Arte que resolve', t.T('que não resolve'))]},
        {'kind': 'panel', 'variant': 'cta', 'theme': 'claro', 'from': t.T('Siga o perfil') - 0.1, 'to': 99, 'icon': 'icone_impressao_colorido.png',
         'items': [it('Siga para mais dicas práticas', t.T('Siga o perfil'))]},
    ]


def p038(t):
    return [
        {'kind': 'hook', 'from': 0, 'to': 2.6, 'lines': ['O menor orçamento', 'nem sempre responde', 'à necessidade certa.'], 'mark': 'certa.'},
        {'kind': 'zoom', 'from': t.T('não olhe'), 'to': t.E('valor final.'), 'scale': 1.14},
        {'kind': 'word', 'from': t.T('não olhe'), 'to': t.E('valor final.') + 0.1, 'text': 'Não só o valor', 'color': '#E6007E'},
        {'kind': 'panel', 'variant': 'list', 'theme': 'claro', 'from': t.T('Confira se você') - 0.2, 'to': t.E('condição de entrega.'),
         'title': 'Compare o mesmo', 'items': [it('Quantidade', t.T('mesma quantidade')), it('Especificação e material', t.T('especificação')),
                                                it('Acabamento e prazo', t.T('acabamento')), it('Condição de entrega', t.T('e condição'))]},
        {'kind': 'word', 'from': t.T('Se um desses'), 'to': t.E('a mesma coisa.'), 'text': 'Mesma coisa?', 'color': '#00A6D6'},
        {'kind': 'panel', 'variant': 'list', 'theme': 'escuro', 'from': t.T('Também confira') - 0.2, 'to': t.E('você precisa.'),
         'title': 'Confira também', 'items': [it('Arte correta', t.T('a arte está')), it('Resultado para o seu uso', t.T('e se o resultado'))]},
        {'kind': 'panel', 'variant': 'strike', 'theme': 'claro', 'from': t.T('Não é sobre') - 0.2, 'to': t.E('com informação.'),
         'items': [it('Escolher a mais cara', t.T('Não é sobre')), it('Decidir com informação', t.T('decidir com'))]},
        {'kind': 'panel', 'variant': 'cta', 'theme': 'escuro', 'from': t.T('Compartilhe') - 0.1, 'to': 99, 'icon': 'icone_orcamento_colorido.png',
         'items': [it('Compartilhe com quem cota materiais', t.T('Compartilhe'))]},
    ]


def p043(t):
    return [
        {'kind': 'hook', 'from': 0, 'to': 2.6, 'lines': ['Muitos erros se evitam', 'com uma aprovação', 'bem feita.'], 'mark': 'aprovação'},
        {'kind': 'panel', 'variant': 'statement', 'theme': 'escuro', 'from': t.T('Sabe quando') - 0.2, 'to': t.E('sido enviada?'),
         'items': [it('Telefone.', t.T('telefone')), it('Nome.', t.T('nome,')), it('Texto.', t.T('texto ou')), it('De novo?', t.T('que já tinha'))]},
        {'kind': 'panel', 'variant': 'list', 'theme': 'claro', 'from': t.T('Muitas vezes') - 0.2, 'to': t.E('com pressa.'),
         'title': 'O retrabalho começa com', 'items': [it('Pedido incompleto', t.T('o pedido')), it('Aprovação com pressa', t.T('ou porque a'))]},
        {'kind': 'panel', 'variant': 'steps', 'theme': 'escuro', 'from': t.T('Antes de aprovar') - 0.2, 'to': t.E('realmente a final.'),
         'title': 'Antes de aprovar', 'items': [it('Confira tudo', t.T('confira o')), it('Peça outra revisão', t.T('peça para')),
                                                it('Valide a versão final', t.T('e valide'))]},
        {'kind': 'zoom', 'from': t.T('E se algo'), 'to': t.E('antes de seguir.'), 'scale': 1.15},
        {'kind': 'word', 'from': t.T('comunique'), 'to': t.E('antes de seguir.') + 0.1, 'text': 'Mudou? Avise', 'color': '#E6007E'},
        {'kind': 'word', 'from': t.T('mas reduz'), 'to': t.E('ser evitados.'), 'text': 'Menos retrabalho', 'color': '#00A6D6'},
        {'kind': 'panel', 'variant': 'cta', 'theme': 'claro', 'from': t.T('Salve e use') - 0.1, 'to': 99, 'icon': 'icone_qualidade_colorido.png',
         'items': [it('Salve para a próxima aprovação', t.T('Salve e use'))]},
    ]


def p044(t):
    return [
        {'kind': 'hook', 'from': 0, 'to': 2.6, 'lines': ['O negócio cresce.', 'A comunicação acompanha?'], 'mark': 'acompanha?'},
        {'kind': 'zoom', 'from': t.T('a comunicação improvisada'), 'to': t.E('um problema.'), 'scale': 1.14},
        {'kind': 'word', 'from': t.T('improvisada'), 'to': t.E('um problema.') + 0.1, 'text': 'Improviso = problema', 'color': '#E6007E'},
        {'kind': 'panel', 'variant': 'list', 'theme': 'escuro', 'from': t.T('Cada pessoa') - 0.2, 'to': t.E('encontra a marca.'),
         'title': 'Sem padrão', 'items': [it('Cada pessoa fala de um jeito', t.T('Cada pessoa')), it('Cada material, um padrão', t.T('cada material')),
                                          it('Cliente recebe versões diferentes', t.T('e o cliente'))]},
        {'kind': 'panel', 'variant': 'steps', 'theme': 'claro', 'from': t.T('O primeiro passo') - 0.2, 'to': t.E('ser adaptados.'),
         'title': 'Documente o básico', 'items': [it('Identidade visual', t.T('identidade visual')), it('Tom de voz', t.T('tom de voz')),
                                                  it('Informações oficiais', t.T('informações oficiais')), it('Modelos adaptáveis', t.T('e modelos'))]},
        {'kind': 'zoom', 'from': t.T('Assim, a empresa'), 'to': t.E('nova campanha.'), 'scale': 1.12},
        {'kind': 'word', 'from': t.T('consistência'), 'to': t.E('nova campanha.'), 'text': 'Consistência', 'color': '#00A6D6'},
        {'kind': 'panel', 'variant': 'cta', 'theme': 'escuro', 'from': t.T('Se você está') - 0.1, 'to': 99, 'icon': 'icone_impressao_colorido.png',
         'items': [it('Acompanhe a SUA GRÁFICA BH', t.T('acompanhe a'))]},
    ]


PLANS = {'025': p025, '026': p026, '031': p031, '032': p032, '037': p037, '038': p038, '043': p043, '044': p044}

if __name__ == '__main__':
    ids = sys.argv[1:] or list(PLANS)
    for n, id in enumerate(PLANS):
        if id not in ids:
            continue
        tl, d = build(id, PLANS[id], n)
        for b in d['beats']:
            if b['to'] == 99:
                b['to'] = d['duration'] + d['tail']
        # reescreve com o fim real do CTA
        open(f"{PROJ}/src/data/SG-{id}.ts", 'w').write(
            "import type {ReelData} from '../reel/types';\n// Gerado por gen.py (alinhamento por pausas, sem transcrição). Tempos em segundos após o corte inicial.\n"
            f"export const SG{id}: ReelData = {ts(d)};\n")
        print(id, 'start', d['start'], 'dur', d['duration'], 'beats', len(d['beats']), 'caps', len(d['captions']))
    idx = "import type {ReelData} from '../reel/types';\n" + ''.join(f"import {{SG{i}}} from './SG-{i}';\n" for i in PLANS) + \
          'export const reels: ReelData[] = [' + ', '.join(f'SG{i}' for i in PLANS) + '];\n'
    open(f'{PROJ}/src/data/index.ts', 'w').write(idx)
