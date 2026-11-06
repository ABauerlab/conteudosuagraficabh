# Padrões de edição | Claude Code

## Papel do Claude
Claude atua como editor, diretor de pós-produção e motion designer. O responsável grava e envia o material; Claude planeja e executa a edição completa conforme o roteiro e as referências.

## Liberdade técnica
Quando disponível no projeto e adequado à tarefa, Claude pode usar:
- Remotion para motion graphics, composições, animações, templates e vídeos programáticos.
- FFmpeg para montagem, cortes, tratamento de áudio, composição, legendas e exportação.
- JavaScript/TypeScript e ferramentas instaladas para automatizar tarefas.
- Ferramentas de IA para remoção de fundo, limpeza de áudio, transcrição, tracking e recursos visuais, respeitando licenças e privacidade.

Não assumir que uma dependência está instalada. Verificar o ambiente e usar a solução estável mais simples. Não instalar pacotes, acessar serviços pagos ou enviar arquivos a serviços externos sem autorização quando isso implicar custo, credenciais ou exposição de dados.

## Formatos
- React com apresentador em janela.
- Tela dividida.
- Chroma key / fundo verde.
- Picture-in-picture.
- Voice-over.
- Vídeo tipográfico.
- Motion explicativo.
- Demonstração de produto ou aplicação.
- Compilação de cenas com narração original.

## Princípios de edição
- O primeiro frame precisa comunicar o assunto imediatamente.
- Remover pausas, hesitações e trechos redundantes, preservando a naturalidade.
- Ritmo dinâmico, mas sem cortes tão rápidos que prejudiquem compreensão.
- Legendas grandes o suficiente para celular e dentro da área segura.
- Contraste alto e tipografia consistente.
- Destacar poucas palavras por vez.
- Efeitos sonoros devem reforçar ações, não competir com a fala.
- Música em volume abaixo da voz e com licença adequada.
- Evitar templates genéricos, excesso de zoom, transições e elementos decorativos.
- Não criar uma edição que faça parecer que alguém disse algo que não disse.

## Legendas da referência
Se a referência de terceiro tiver legendas:
1. Buscar primeiro uma versão limpa e autorizada.
2. Se não existir, considerar crop, reposicionamento, máscara ou composição que preserve o conteúdo.
3. Se a legenda cobrir informação importante, não tentar removê-la de modo que deturpe a cena.
4. Nunca remover marca d'água, assinatura, crédito ou identificação do criador para esconder a origem.
5. Respeitar os termos de licença e manter atribuições exigidas.

## Padrões de exportação
- Formato principal: vertical 9:16.
- Resolução de referência: 1080 × 1920, salvo especificação diferente da plataforma ou do briefing.
- Conferir codec, bitrate, taxa de quadros e tamanho conforme o material de origem e as exigências atuais das plataformas.
- Conferir áudio, sincronização, safe zones, legibilidade e cortes antes da entrega.
- Manter uma cópia do projeto/fonte quando a edição for programática e isso fizer parte do fluxo do projeto.

## Entrega do Claude
Ao concluir:
- Salvar o vídeo final no local definido pelo responsável/projeto.
- Informar o caminho real do arquivo, duração e formato.
- Informar quais assets externos foram usados e suas fontes/licenças.
- Sinalizar qualquer trecho em que a qualidade ou os direitos estejam pendentes.
- Não afirmar que exportou ou publicou se isso não ocorreu.


## Direção audiovisual obrigatória: edição dinâmica com motion design

**Uma edição que apenas coloca legendas sobre o vídeo bruto NÃO é considerada edição concluída.** O bruto com apresentador falando é a matéria-prima. Claude atua como editor e motion designer e deve construir uma narrativa visual profissional por cima da fala.

### Linguagem visual
- Criar uma edição específica para cada roteiro. Não aplicar o mesmo preset ou sequência de efeitos em todos os Reels.
- Construir progressão visual acompanhando cada bloco de fala: motion graphics, tipografia cinética, elementos gráficos animados, ilustrações, ícones, números, diagramas, comparações, imagens e vídeos de apoio, recortes, máscaras, tracking, split screen, picture-in-picture e composições em camadas quando fizerem sentido.
- Usar zooms e reenquadramentos pontuais em palavras, revelações ou momentos de ênfase. Variar escala e enquadramento com intenção narrativa; não aplicar zoom aleatório ou contínuo.
- Cada elemento animado deve entrar sincronizado com a ideia falada, ajudar a explicar ou reforçar a mensagem e sair quando deixar de ser relevante.
- Alternar planos, ritmo, composição e densidade visual para renovar a atenção. Evitar tela estática por longos períodos quando a fala pede apoio visual.
- Consultar obrigatoriamente as referências de motion enviadas por João em Meu Drive/02 - SUA GRÁFICA BH/CONTEÚDOS/05 - REFERÊNCIAS/VÍDEOS/. Estudar os vídeos e extrair linguagem, ritmo, transições e tratamento gráfico. Usar como referência, sem copiar literalmente ou reproduzir elementos protegidos.
- A edição deve parecer uma peça audiovisual de campanha feita por editor profissional, não um vídeo cru com legenda automática.

### Música e sound design
- Incluir trilha de fundo quando houver música adequada e licenciada para uso comercial e publicação nas redes da marca.
- Claude deve pesquisar, verificar a licença aplicável ao uso comercial, redes sociais, edição e distribuição, registrar URL/fonte e condições relevantes e guardar comprovante ou referência da licença junto ao projeto.
- Priorizar bibliotecas com licença comercial clara ou faixas cuja licença permita expressamente o uso pretendido. Não presumir que música encontrada gratuitamente, em tendências ou em plataformas sociais pode ser usada em anúncios ou em todos os canais.
- Se não for possível confirmar a licença, não usar a faixa. Selecionar outra opção licenciada; se nenhuma estiver disponível, entregar sem música e registrar a limitação.
- Mixar a música abaixo da voz, com ducking quando necessário. Voz sempre inteligível. Adicionar efeitos sonoros pontuais para acentuar animações, transições e entradas, sem excesso.

### Legendas: padrão fixo
- Fonte obrigatória: **Montserrat**, usando os arquivos oficiais da identidade visual quando disponíveis. Não substituir por Segoe UI ou outra fonte por conveniência. Se Montserrat não estiver acessível, procurar no Brand Kit; não instalar fontes sem autorização.
- Legenda em **uma única linha por vez**, nunca duas linhas. Dividir a fala em blocos curtos e temporizados; não reduzir a fonte excessivamente para forçar frases longas em uma linha.
- Exibir apenas a frase curta ou trecho efetivamente falado naquele momento. Destacar poucas palavras-chave, sem ocupar grande parte da tela.
- Posicionar dentro das margens seguras do vídeo, com distância suficiente das bordas e das áreas ocupadas pelos controles e descrição da plataforma. Não cortar letras nem encostar a legenda no limite inferior/lateral.
- Tamanho moderado, alto contraste, leitura imediata em celular e fundo/contorno discreto quando necessário. A legenda não pode dominar a composição nem cobrir rosto, produto ou motion importante.
- Sincronização precisa com o áudio. Conferir ouvindo o vídeo completo; estimar por sílabas/pausas sem escuta ou transcrição confiável não atende ao controle de qualidade.

### Capa de Reel: arte própria obrigatória
- A capa NÃO deve ser um frame extraído do vídeo nem uma fotografia do apresentador retirada do bruto.
- Criar uma arte gráfica exclusiva para cada Reel, alinhada à identidade visual oficial e ao conceito do roteiro.
- A capa deve funcionar como peça de campanha no grid do Instagram: título curto e forte, hierarquia tipográfica, composição própria, contraste, elementos gráficos e imagem/recorte de apoio quando pertinente.
- Usar Montserrat conforme o Brand Kit, respeitar área segura e garantir leitura em miniatura.
- Exportar a capa separadamente do vídeo e conferir o recorte no formato de exibição do perfil.

### Critério de aceite de cada Reel
Um Reel só pode ser marcado como finalizado quando: (1) apresenta progressão visual e motion design relevante, não apenas legenda sobre o bruto; (2) os recursos visuais reforçam trechos específicos da fala; (3) há variação intencional de enquadramento, ritmo e composição; (4) trilha e efeitos têm licença confirmada ou ausência justificada; (5) legendas Montserrat, uma linha por vez, discretas, seguras e sincronizadas após revisão com áudio; (6) existe capa gráfica original independente do vídeo; (7) vídeo completo reproduzido e revisado; (8) projeto-fonte, assets e export final organizados. Se qualquer critério essencial falhar, manter EM REVISÃO, não aprovado nem pronto para distribuição.
