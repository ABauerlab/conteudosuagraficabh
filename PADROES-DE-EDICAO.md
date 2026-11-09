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
- A fonte padrão gratuita é a biblioteca oficial do Pixabay, conforme a seção de licenciamento deste documento. Não comprar músicas, assinaturas ou serviços.
- Verificar a página individual da faixa e os termos vigentes para o uso comercial pretendido; registrar URL, autor, título, data e evidência de licença junto ao projeto.
- Não presumir que qualquer arquivo gratuito ou áudio em tendência pode ser reutilizado. Não usar reuploads, faixas sem origem comprovada ou áudio cuja licença não cubra o uso.
- Se não houver faixa adequada com licença verificável, documentar a exceção; não improvisar nem usar áudio de terceiros por conveniência.
- Mixar a música abaixo da voz, com ducking quando necessário. Voz sempre inteligível. Efeitos sonoros pontuais e discretos.

### Tratamento de áudio: melhorar sem degradar a gravação

O áudio original deve ser preservado. O objetivo do tratamento é aumentar clareza, inteligibilidade, consistência e conforto de escuta, mantendo a voz natural e fiel à gravação. **Não aplicar processamento por rotina se o original já estiver bom.**

1. Ouvir o bruto integralmente antes de editar, preferencialmente com fones e também em reprodução comum. Identificar ruído constante, eco/reverberação, vento, estalos, plosivas, sibilância, clipping, volume irregular e problemas de inteligibilidade.
2. Criar uma cópia de trabalho e manter o arquivo original intocado. Escolher somente os tratamentos necessários para os problemas realmente identificados.
3. Fazer limpeza de ruído de forma moderada. Redução agressiva, artefatos metálicos/robóticos, som subaquático, cortes de sílabas ou perda de ambiência são sinais de piora. Se isso ocorrer, reduzir ou remover o processamento.
4. Usar equalização corretiva sutil, quando necessária, para reduzir ressonâncias ou excesso de graves e melhorar a compreensão. Não alterar o timbre natural nem exagerar agudos/graves.
5. Aplicar compressão leve/moderada somente quando ajudar a controlar variações de volume. Evitar voz esmagada, bombeamento, respiração artificialmente elevada ou perda de dinâmica.
6. Usar de-esser, gate/expander, de-click, de-plosive e de-reverb apenas quando o defeito estiver presente e a ferramenta produzir melhora audível. Não cortar finais de palavras, respirações naturais ou consoantes.
7. Ajustar ganho e loudness de forma consistente com a plataforma e o material, preservando headroom e evitando clipping. Limiter é proteção final, não correção para áudio distorcido.
8. Mixar música e efeitos abaixo da voz. Automatizar/baixar a trilha nos trechos falados; a fala deve permanecer sempre inteligível, sem competir com a música ou os efeitos.
9. Fazer comparação A/B entre original e tratado em volume de reprodução equivalente. Conferir em fones, alto-falante comum e celular. O tratado deve ser claramente mais confortável/limpo sem soar artificial.
10. Se o processamento não melhorar de forma inequívoca, voltar à versão anterior ou manter o original. Não “forçar” tratamento para demonstrar trabalho.

**Não fazer:** denoise extremo, gate que corta sílabas, compressão excessiva, EQ agressivo, normalização que amplifica ruído, remoção artificial de respirações, alteração de pitch/timbre, clonagem de voz ou substituição da fala. Não usar serviços pagos ou enviar gravações a serviços externos sem autorização.

**Critério de aceite:** voz natural, compreensível e estável; sem clipping introduzido, artefatos perceptíveis ou cortes de fala; música/efeitos discretos; comparação antes/depois aprovada pela escuta crítica. Registrar no projeto o que foi tratado e manter o bruto preservado.


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
Um Reel só pode ser marcado como finalizado quando: (1) apresenta progressão visual e motion design relevante, não apenas legenda sobre o bruto; (2) os recursos visuais reforçam trechos específicos da fala; (3) há variação intencional de enquadramento, ritmo e composição; (4) trilha e efeitos têm licença confirmada ou exceção documentada; o tratamento de áudio melhora a clareza sem alterar a voz natural, sem artefatos e com comparação antes/depois; (5) legendas Montserrat, uma linha por vez, discretas, seguras e sincronizadas após revisão com áudio; (6) existe capa gráfica original independente do vídeo; (7) vídeo completo reproduzido e revisado; (8) projeto-fonte, assets e export final organizados. Se qualquer critério essencial falhar, manter EM REVISÃO, não aprovado nem pronto para distribuição.


## Documento mestre complementar e obrigatório
Para a direção completa de produção audiovisual, proteção do rosto, cinematografia, montagem, storytelling, motion design, áudio, capas, formatos, revisão, publicação e critérios de aceite, consultar `PADRAO-MESTRE-CONTEUDO-PROFISSIONAL.md`. As regras deste arquivo permanecem válidas; o documento mestre consolida e amplia o padrão. **Nunca cortar ou encobrir o rosto do apresentador.**

## Tempo mínimo de leitura do gancho na tela

- O texto do gancho inicial deve permanecer visível tempo suficiente para ser lido integralmente em velocidade normal, especialmente em celular. Não remover, trocar ou animar para fora antes de o espectador conseguir concluir a leitura.
- Usar **3 a 5 segundos como referência inicial**, ajustando para mais quando a frase for longa, tiver termos menos familiares ou exigir interpretação. O tempo é definido pela legibilidade real, não por uma duração rígida.
- Se o gancho não couber confortavelmente nesse intervalo, simplificar apenas a apresentação visual ou dividir o texto em blocos sequenciais sem alterar a promessa e o sentido do briefing. Cada bloco precisa ter tempo próprio de leitura.
- Não acelerar a entrada/saída, reduzir excessivamente o tamanho da fonte ou acumular elementos que prejudiquem a leitura.
- Revisar o início do vídeo em velocidade normal e em tela de celular, como alguém que vê o conteúdo pela primeira vez. Confirmar que o texto pode ser lido sem pausar ou voltar o vídeo.
- Se a fala começar simultaneamente, garantir que o texto continue legível sem competir com a fala ou encobrir o apresentador.
- **Critério de aceite:** gancho ilegível, exibido por tempo insuficiente ou removido antes da leitura completa mantém o Reel em EM REVISÃO e deve ser corrigido antes da distribuição.

## Direção semântica e comercial do motion design

Motion design precisa traduzir visualmente a fala, não apenas preencher a tela com animações. Antes de editar, montar um mapa simples por bloco de fala: fala exata → ideia principal → imagem/metáfora visual → elemento gráfico ou B-roll → entrada/saída e duração.

- Cada elemento precisa ilustrar, explicar, provar visualmente ou enfatizar exatamente o que está sendo dito naquele momento.
- Usar metáforas visuais somente quando forem imediatas e inequívocas para o público. Se o espectador precisar adivinhar a relação entre fala e gráfico, a solução não funciona.
- Evitar formas, quadrados coloridos, ícones, painéis, gráficos ou animações genéricas sem função narrativa. Não inserir elementos apenas para parecer que existe motion design.
- Manter coerência entre texto, fala, imagem, cor, movimento e ordem de leitura. Um elemento não pode sugerir uma ideia diferente da fala.
- Priorizar recursos comerciais: produto real, aplicação, resultado demonstrável, processo pertinente, comparação honesta, benefício confirmado, situação de uso e CTA.
- Criar storyboard/mapeamento visual antes da montagem. Revisar cada cena perguntando: O que está sendo falado? O que o público está vendo? A relação entre os dois fica clara imediatamente?
- Se não houver imagem de apoio fiel ao assunto, usar motion tipográfico/diagrama simples e semanticamente correto em vez de foto genérica ou animação decorativa.
- Critério de aceite: se o motion estiver desalinhado, aleatório, ambíguo ou sem relação evidente com a fala, manter EM REVISÃO e refazer a cena.

## Música gratuita e licenciamento
A estratégia padrão é utilizar a biblioteca oficial do Pixabay: https://pixabay.com/pt/music/. Antes de usar cada faixa, abrir a página individual, conferir os termos vigentes e verificar se o uso comercial pretendido é permitido. Registrar URL, título, autor, data de download e evidência de licença. Não usar reuploads ou faixas sem origem comprovada. Não comprar músicas, assinaturas ou serviços sem autorização. A licença não garante ausência de reivindicações automatizadas; guardar evidências e tratar qualquer reivindicação com verificação, nunca contestação automática. Se não houver faixa adequada e verificável, documentar a exceção.

## B-roll e fotografia de bancos de imagem: contexto obrigatório

Toda foto/vídeo de banco de imagens deve ter correspondência direta com a fala e com a cena. Não usar imagens bonitas, genéricas ou apenas relacionadas ao tema se não explicarem o que está sendo dito.

- Antes de pesquisar, escrever um microbrief de asset: fala/trecho que será ilustrado, objeto/ação exatos, ambiente, enquadramento, contexto brasileiro quando relevante, função narrativa e duração prevista na tela.
- Pesquisar por assunto + ação + contexto + enquadramento. Não buscar apenas termos amplos como gráfica; buscar a ação real descrita na fala.
- Conferir o arquivo real antes de inserir: o que aparece, o que está escrito, equipamentos, idioma, cenário, pessoas, marcas, uniformes e coerência com o contexto da SUA GRÁFICA BH.
- A imagem deve mostrar a ação/objeto correto. Não usar foto de impressão offset para ilustrar processo digital se a diferença for relevante; não usar embalagem genérica para afirmar um acabamento específico; não sugerir que uma instalação, máquina ou equipe retratada pertence à SUA GRÁFICA BH.
- Preferir imagens de produção brasileira e contexto local quando o assunto exigir. Evitar fotos com textos estrangeiros visíveis, máquinas ou processos incompatíveis e marcas de terceiros em destaque.
- Se não encontrar asset contextual, usar material próprio autorizado, criar um diagrama/motion fiel ou manter o apresentador em tela. Não preencher espaço com stock fora de contexto.
- Registrar URL, autor, plataforma, licença e data de obtenção. A licença ampla da Unsplash permite muitos usos comerciais, mas não libera automaticamente direitos de imagem de pessoas reconhecíveis, marcas/logos ou obras protegidas retratadas. Consultar https://unsplash.com/pt-br/licença e https://unsplash.com/terms; quando esses elementos aparecerem, verificar permissões adicionais ou escolher outra imagem.
- Critério de aceite: asset fora de contexto, contraditório ou que possa induzir o público a uma afirmação falsa deve ser removido e substituído.


## Diretriz permanente: aquisição inteligente, originalidade e autonomia de produção

### Objetivo comercial e crescimento de audiência
O objetivo central do conteúdo é **atrair potenciais clientes, conquistar seguidores qualificados e transformar confiança em pedidos pagos**. Não tratar seguidores e vendas como objetivos concorrentes: construir uma audiência que reconheça a marca, acompanhe porque recebe valor e escolha comprar quando surgir uma necessidade gráfica.

Planejar a jornada: **descoberta → identificação/valor → seguir o perfil → relacionamento e consideração → consulta ao catálogo/WhatsApp → orçamento → pedido pago → recompra/indicação**. Nem toda peça precisa pedir compra. Em conteúdos de descoberta, a ação principal pode ser seguir, compartilhar ou salvar; em conteúdos de consideração, comentar, visitar o perfil ou consultar uma solução; em conteúdos comerciais, iniciar conversa/orçamento pelo canal oficial. Fazer a venda de modo inteligente: ensinar, inspirar, demonstrar aplicações e resolver problemas reais antes de apresentar a oferta. CTA deve ser natural e coerente com a etapa, sem transformar todo post em propaganda direta.

Cada briefing novo deve explicitar: público específico, necessidade/desejo, etapa do funil, valor entregue, relação legítima com a gráfica/produto confirmado, motivo para seguir a SUA GRÁFICA BH e ação principal esperada. Explicar por que aquele conteúdo atrairia alguém que pode vir a comprar, sem forçar produto desconectado do assunto.

### Auditoria antirrepetição semântica obrigatória antes de cada novo lote
Antes de propor qualquer pauta, Claude deve consultar o histórico completo disponível de conteúdos planejados, gravados, produzidos, publicados e agendados, incluindo briefings, roteiros, calendário, banco de ganchos e análises de desempenho. Comparar não apenas palavras ou títulos, mas assunto/subassunto; dor, desejo ou pergunta; promessa/gancho; argumento central e informação entregue; exemplo, aplicação ou produto; conclusão e CTA; estrutura narrativa e formato.

**Não criar conteúdos que repitam a mesma ideia, ensinamento, argumento ou conclusão apenas trocando palavras, exemplos superficiais, gancho ou formato.** Reels, carrosséis e Stories também contam como repetição entre si. Uma mudança de copy não torna uma pauta original.

Manter um inventário/matriz de temas com ID SG, tema, ângulo, promessa, público, produto (se houver), etapa do funil, formato, CTA e status. Antes de aprovar a pauta, comparar semanticamente com o inventário e registrar: NOVA ABORDAGEM, APROFUNDAMENTO REAL ou REAPROVEITAMENTO ESTRATÉGICO. Reaproveitamento só é permitido quando houver motivo claro (atualização factual, nova prova, nova aplicação, evolução do tema ou novo estágio do funil) e diferença substantiva no valor entregue. Se a ideia já foi coberta e não há novidade real, descartar e criar outra pauta.

Auditar também repetição de CTA, ritmo, abertura e estrutura. Variar formatos sem sacrificar clareza. Não preencher calendário com versões disfarçadas da mesma pauta. Priorizar diversidade de necessidades, segmentos de clientes, ocasiões de compra e aplicações reais dos produtos ativos.

### Briefing do próximo lote: requisitos explícitos
Todo novo lote preparado para João gravar deve conter, em cada conteúdo: roteiro falado completo e natural; gancho e texto de tela com tempo de leitura; público e problema/desejo; objetivo de aquisição e etapa do funil; valor original entregue; motivo legítimo para seguir o perfil; relação com produto/serviço ativo no catálogo quando aplicável; CTA falado exato; direção de gravação e enquadramento; mapa de edição/motion por blocos de fala; assets/B-roll e contexto exato; referências e direitos; legenda por canal, hashtags e destino oficial; critério de aceite e arquivos esperados.

O lote deve vir acompanhado de auditoria antirrepetição, mapa do funil e síntese mostrando como as peças trabalham em conjunto para atrair seguidores qualificados e gerar oportunidades de venda. Não pedir a João que invente direção ou complete roteiro: entregar tudo pronto para gravar.

### Autonomia total de produção e revisão de Claude
João entrega os vídeos brutos e materiais disponíveis. A partir daí, Claude é responsável por localizar arquivos, conferir correspondências, editar, criar motion, selecionar B-roll contextual, tratar áudio, inserir trilha permitida, legendar, criar capas, finalizar artes, revisar, corrigir, organizar e agendar/distribuir conforme autorização do lote.

Claude deve fazer sua própria revisão profissional antes de apresentar o resultado. Assistir/reproduzir integralmente cada vídeo final em velocidade normal; revisar cada arte, slide, capa e Story em tamanho real e em visualização de celular; verificar áudio, ortografia, enquadramento, rosto, ritmo, coerência semântica, tempo de leitura do gancho, sincronização, licença, CTA, formato e destino. Corrigir os problemas encontrados e repetir a revisão. Não transferir ao João a tarefa de detectar erros que Claude consegue identificar.

Não entregar como final uma peça que ainda precise de ajustes evidentes. Não perguntar se João gostou antes de realizar o próprio controle de qualidade. A aprovação individual não é necessária quando a execução foi autorizada e todos os critérios objetivos foram cumpridos. Só escalar problemas que dependam de decisão, gravação, acesso ou autorização de João (bruto ausente/ininteligível, dado comercial sem confirmação, licença/permissão impossível de validar, falha de integração). Agrupar dúvidas indispensáveis em uma única mensagem objetiva; continuar os demais itens aptos.

Relatório final conciso e factual: itens concluídos, arquivos/caminhos, agendamentos confirmados, pendências externas e evidências do controle de qualidade. Distinguir produzido, revisado, aprovado, agendado e publicado.

### Política de trilha
A política detalhada de uso gratuito do Pixabay está consolidada em `## Música gratuita e licenciamento` neste documento. Não manter regras paralelas ou contratar serviços sem autorização.


## Motion design com fonte JavaScript/TypeScript obrigatória quando houver animação programática
Quando o motion gráfico for produzido programaticamente, a fonte principal deve ser um projeto editável em JavaScript/TypeScript, preferencialmente React + Remotion quando disponível no ambiente. Não entregar somente o MP4 renderizado, um conjunto de imagens ou um script FFmpeg opaco como substituto do projeto de motion.

- Construir cenas, composições, componentes, keyframes, transições, textos e elementos animados no código JS/TS; Remotion é a opção preferencial para composição e renderização por frames.
- Organizar o código por Reel/cena ou por componentes reutilizáveis, mantendo cada vídeo com identidade narrativa própria. Reutilizar componentes técnicos é permitido; repetir a mesma direção criativa mecanicamente não.
- O código deve refletir o mapa de motion aprovado: fala/trecho → ideia → elemento visual → movimento/entrada/saída → duração.
- Manter projeto-fonte, assets referenciados, configurações e instruções mínimas de execução junto aos arquivos de trabalho. Não incluir segredos, tokens, arquivos pesados desnecessários ou dependências sem autorização.
- Verificar o ambiente e as dependências antes de escolher a implementação. Não instalar pacotes pagos nem enviar mídia a serviços externos sem autorização.
- FFmpeg pode ser usado para montagem final, conformação, áudio e export, mas não substitui a fonte JS/TS das animações programáticas.
- Validar que o projeto abre/renderiza no ambiente disponível. Se Remotion não estiver disponível ou não for tecnicamente adequado, documentar a limitação e escolher alternativa editável em JS/TS; escalar somente se não houver caminho viável.
- QA deve conferir o render final e a correspondência com o código-fonte. Entregar caminhos reais do projeto e do vídeo exportado.
