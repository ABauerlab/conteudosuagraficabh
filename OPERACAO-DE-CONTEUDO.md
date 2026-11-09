# Operação de conteúdo | SUA GRÁFICA BH

## Objetivo
Manter um fluxo integrado: ChatGPT e Claude podem pesquisar, planejar, criar e auditar conforme a tarefa. João grava e fornece materiais. Claude também pode corrigir estratégia, copy ou roteiro quando a auditoria encontrar lacunas; depois executa produção, QA e distribuição pelo Postiz. Aplicar os gates de AUDITORIA-DE-PROCESSO-E-GATES.md.

Não criar etapas, serviços ou ferramentas adicionais quando as integrações já disponíveis no ambiente do Claude forem suficientes.

## Papéis
- **ChatGPT:** pesquisa, estratégia, roteiros, copy, briefings, direção visual e organização do repositório; também audita e corrige quando solicitado.
- **João:** define escopo/etapas, grava e fornece materiais, e decide apenas questões comerciais, autorizações e acessos que dependam dele.
- **Claude Code:** pesquisa e audita lacunas quando necessário; consulta este repositório, o CRM e o Brand Kit; localiza brutos e referências; corrige briefings incompletos dentro da autorização; produz, edita, revisa e distribui pelo Postiz.
- **Google Drive:** armazenamento dos arquivos.
- **Postiz:** distribuição nos canais configurados: Instagram, Facebook e Threads.

## Fontes oficiais e regra de catálogo
- O CRM `ABauerlab/crm-sua-grafica-bh` e os dados comerciais no Supabase são a fonte de verdade para produtos ativos, disponibilidade, preços, especificações, prazos e condições.
- Antes de criar ou publicar qualquer conteúdo que mostre, mencione ou recomende um produto, Claude deve confirmar que ele está disponível para venda no catálogo/tabela comercial atual do CRM.
- **Só criar conteúdo sobre produtos e serviços que a SUA GRÁFICA BH realmente vende e que estejam ativos no catálogo.** Não presumir disponibilidade por encontrar o produto em referências externas.
- Se não conseguir consultar o catálogo/Supabase ou houver dúvida sobre a disponibilidade, marcar como `PENDENTE DE CATÁLOGO` e não publicar. Nunca inventar preço, prazo ou especificação.

## Pesquisa de mercado e referências
- Estudar conteúdos estáticos e vídeos de outras gráficas brasileiras que apresentem sinais verificáveis de alto desempenho, incluindo publicações com milhares de curtidas quando essa métrica estiver visível.
- Registrar link da publicação original, perfil, plataforma, data e métricas observadas. Diferenciar dados confirmados de estimativas.
- Identificar o que torna a peça eficaz: gancho, oferta, composição, fotografia, hierarquia, texto, formato e CTA.
- Acompanhar tendências de produtos, formatos e aplicações do mercado gráfico. Exemplo de pauta para investigar: **totem de mão**. Primeiro verificar se é uma tendência relevante no mercado brasileiro e, antes de criar qualquer conteúdo, confirmar no catálogo/Supabase se a gráfica vende esse item.
- Adaptar os conceitos à identidade visual oficial da SUA GRÁFICA BH, criando peças originais. Não copiar a arte, o texto, o layout exato ou a identidade de terceiros.
- Usar referências e materiais de terceiros somente quando houver licença, autorização ou permissão adequada para reutilização comercial. Preferir bancos de imagens/vídeos com licença comercial clara, materiais próprios ou assets autorizados.
- Para imagens e vídeos de gráficas, máquinas offset/digitais e processos de impressão, priorizar fontes brasileiras, contexto brasileiro e materiais em português do Brasil. Não usar materiais estrangeiros ou conteúdo com textos em outros idiomas.
- A expressão “sem direito autoral” não deve ser presumida: verificar a licença de cada arquivo e guardar a fonte e as condições de uso. Não remover marcas d'água nem créditos.

## Pastas do Drive
Raiz: `Meu Drive/02 - SUA GRÁFICA BH/CONTEÚDOS/`
1. `01 - VÍDEOS BRUTOS/` — gravações originais de João.
2. `02 - EM EDIÇÃO/` — projetos e versões de trabalho.
3. `03 - APROVADOS/` — exports finais revisados.
4. `04 - PUBLICADOS/` — arquivos finais e materiais publicados.
5. `05 - REFERÊNCIAS/` — referências e assets autorizados/licenciados.

Não apagar nem sobrescrever brutos. Não alterar a estrutura de pastas sem autorização.

## Fluxo de trabalho
1. **Pesquisa e estratégia:** identificar oportunidades, dores, tendências e referências brasileiras; escolher o mix de vídeos, carrosséis, estáticos e Stories conforme o objetivo.
2. **Planejamento:** entregar conteúdo final e briefing completo por ID SG, incluindo copy, roteiro, direção de gravação, direção de arte/edição, CTA e legendas por canal.
3. **Prancha visual:** gerar uma prancha por lote que inclua artes. João salva a imagem em `CONTEÚDOS/05 - REFERÊNCIAS/` com os IDs SG no nome.
4. **Gravação:** João grava os vídeos do lote, cada um identificado com o mesmo ID: `SG-XXX - TÍTULO DO VÍDEO.mp4`.
5. **Upload:** João envia os arquivos brutos para `01 - VÍDEOS BRUTOS/`.
6. **Comando ao Claude:** João informa os IDs exatos do lote usando o comando único de `PROMPT-UNICO-CLAUDE.md`.
7. **Correspondência:** Claude identifica cada briefing, prancha e bruto pelo ID. Itens ambíguos ou sem material essencial ficam pendentes.
8. **Auditoria e correção:** antes da produção, Claude confere estratégia, originalidade, roteiro, briefing, catálogo, direitos e referências. Preserva material completo/aprovado; corrige lacunas reais dentro do escopo autorizado.
9. **Produção e QA:** Claude produz as artes, carrosséis, Stories e capas; edita vídeos; reproduz cada vídeo e inspeciona cada arquivo em tamanho real e celular, corrigindo falhas.
10. **Distribuição:** Claude executa pelo Postiz a distribuição de todos os formatos em todos os destinos conectados, autorizados e compatíveis, com confirmação individual por canal conforme AGENTS.md.
11. **Registro:** Claude registra status, data, canal, links/IDs e pendências no calendário e nos arquivos individuais, quando tiver acesso de escrita.

## Conteúdo a partir de dores reais
Toda pesquisa, criação e revisão deve consultar `DORES-REAIS-CLIENTES.md`. Pautas devem responder a necessidades concretas de compradores de materiais gráficos, como economizar sem desperdiçar, escolher papéis, preparar sangria e margem de segurança, evitar erros de arquivo, entender cores e comparar fosco/brilho ou outros acabamentos disponíveis. Pesquisar e validar os fatos técnicos; não transformar exemplos em afirmações universais. Cada conteúdo deve entregar orientação prática e ser semanticamente diferente do histórico.



## Regra especial: Reels do Instagram como Trial Reel
A Meta informa que os insights de um Trial Reel costumam ficar disponíveis aproximadamente 24 horas após a publicação. A graduação manual (“share with everyone”) é uma ação posterior e não significa que o Reel será publicado automaticamente ao completar 24 horas. A Meta também oferece uma opção de graduação automática baseada no desempenho observado nos primeiros 72 horas. [Fonte oficial](https://about.fb.com/news/2024/12/trial-reels-try-content-non-followers-first-see-what-perfoms-best/).

O Postiz documenta os campos `is_trial_reel` e `graduation_strategy` (`MANUAL` ou `SS_PERFORMANCE`), mas isso, isoladamente, não comprova que a integração conectada permite promover manualmente o mesmo Reel depois. [Documentação Postiz](https://postiz.com/codex/instagram).

Regras operacionais:
1. O Postiz documenta suporte a `is_trial_reel=true` e `graduation_strategy=MANUAL` ou `SS_PERFORMANCE`. Antes do primeiro uso na instalação self-hosted, Claude deve confirmar a versão, os campos aceitos e o canal Instagram conectado.
2. Se disponível e previsto no briefing, agendar/publicar o Trial Reel via Postiz com `is_trial_reel=true` e `graduation_strategy=MANUAL` quando a decisão de compartilhar depois for humana.
3. Não deixar o Claude aguardando 24 horas nem manter a execução do lote aberta. Registrar ID, horário real e status do Trial Reel.
4. Aproximadamente 24 horas depois, consultar as métricas. Se a decisão for compartilhar com seguidores, abrir o mesmo Trial Reel no Instagram e usar a ação nativa **Compartilhar com todos / Share with everyone**. Essa etapa não deve criar outra publicação.
5. Não publicar uma cópia normal no dia seguinte para depois apagar uma delas. Isso divide os históricos, perde sinais e não transfere o engajamento entre posts.
6. `SS_PERFORMANCE` é uma opção de graduação automática decidida pelo Instagram, não um agendamento público manual para exatamente 24 horas.
7. Se o recurso ou a ação nativa não estiverem disponíveis, marcar `PENDENTE DE RECURSO TRIAL REEL`; não duplicar. Reaproveitar a ideia somente em outro momento, com variação criativa substancial, se fizer sentido.

Nunca afirmar que um Trial Reel foi graduado, que aguardou 24 horas ou que foi publicado para todos sem confirmação real.

## Comando padrão para Claude
O comando reutilizável oficial está em `PROMPT-UNICO-CLAUDE.md`. João deve informar os IDs SG exatos do lote. Claude audita os briefings antes de executar. Preserva os que estiverem completos e aprovados; corrige lacunas reais ou bloqueia apenas o ID afetado. Depois produz, revisa, organiza e distribui conforme AGENTS.md. Para Trial Reels, nunca manter a execução aberta aguardando 24 horas; registrar o status e tratar a avaliação/graduação como etapa posterior, somente se o recurso estiver confirmado.

## Regras para processamento em lote
- Usar `SG-XXX` como identificador principal em briefing, prancha, bruto, export e publicação.
- Conferir briefings, artes, prancha visual e brutos; identificar IDs sem material essencial, duplicações e correspondências ambíguas.
- Não interromper todo o lote por causa de um único item com problema; processar os demais que estiverem aptos.
- Não inventar correspondências, falas, cenas, depoimentos ou dados comerciais.
- Não apagar ou sobrescrever os arquivos originais.
- Não produzir nem distribuir material sem briefing, confirmação comercial quando aplicável ou direitos resolvidos.
- Agendar conforme calendário e canal efetivamente conectado; não inventar horários como se fossem dados comprovados.
- Verificar histórico do Postiz para evitar duplicidade.
- Se o Postiz falhar em um canal, registrar a falha e não afirmar que houve agendamento/publicação naquele canal.

## Controle de qualidade
- Roteiro e peça final correspondem ao mesmo ID.
- Texto revisado, legível em celular e fiel ao briefing.
- Hierarquia, contraste, margens seguras e identidade visual conferidos.
- Cada slide do carrossel foi aberto e revisado na ordem correta.
- Cada vídeo foi reproduzido; áudio, cortes, legendas e enquadramento conferidos.
- Produtos e informações comerciais confirmados no CRM/Supabase.
- Direitos e licenças dos assets verificados.
- CTA, legenda e formato adaptados ao canal.
- Arquivos finais conferidos antes do agendamento.

## Status
IDEIA → PESQUISANDO REFERÊNCIA → BRIEFING PRONTO → PRONTO PARA GRAVAR / PRONTO PARA PRODUZIR → GRAVADO → EM PRODUÇÃO → PRONTO PARA PUBLICAR → AGENDADO → PUBLICADO → ANALISADO.

Estados adicionais: PRANCHA VISUAL PENDENTE, PENDENTE DE ARQUIVO, PENDENTE DE DIREITOS, PENDENTE DE CATÁLOGO, PENDENTE DE RECURSO TRIAL REEL, ERRO DE PRODUÇÃO e ERRO DE AGENDAMENTO.


## Hashtags e distribuição multicanal: regra operacional

- **Feed e Reels:** toda legenda publicada deve incluir de 3 a 5 hashtags relevantes. Nunca ultrapassar cinco.
- Selecionar hashtags com base no assunto real do conteúdo, público-alvo, produto/serviço confirmado e intenção de descoberta. Combinar alcance amplo com especificidade; não usar listas genéricas copiadas para todas as peças.
- Verificar sinais atuais de uso e relevância nas plataformas ou fontes confiáveis. Não inventar volume, ranking ou alcance. Hashtags não garantem viralidade; são apenas um dos fatores de descoberta.
- Adaptar hashtags e legenda para Instagram, Facebook, Threads e demais canais conectados. Respeitar diferenças de formato e práticas de cada plataforma.
- **Distribuição:** Feed e Reels devem ser enviados a todos os canais conectados e autorizados que aceitem aquele formato, conforme calendário. Verificar no Postiz cada canal individualmente. Se o canal não aceitar o formato ou falhar, registrar a exceção sem declarar distribuição total.
- Não aplicar hashtags automaticamente a Stories; seguir briefing.
- No controle do lote, registrar a legenda final por canal ou, no mínimo, confirmar que cada legenda enviada contém as hashtags apropriadas.


## Padrão mestre de produção, distribuição e aprendizado
O fluxo operacional deve aplicar `PADRAO-MESTRE-CONTEUDO-PROFISSIONAL.md` do briefing à análise pós-publicação. Para cada Reel, validar proteção integral do rosto, narrativa, montagem, motion, áudio, legendas e capa. Para Feed/Stories, validar a função e a sequência próprias de cada formato. Distribuir Feed/Reels em todos os canais conectados elegíveis, com adaptações por plataforma, 3 a 5 hashtags relevantes em cada legenda e confirmação individual no Postiz. Após publicar, coletar métricas disponíveis de retenção, descoberta, interação e conversão para orientar os próximos lotes. Não inventar métricas nem prometer viralidade.

## Direção criativa audiovisual: coerência, música e imagens de apoio

- O motion deve traduzir a fala em imagem, não ser decoração. Antes da edição, mapear fala, ideia, elemento visual, motivo, duração e movimento por cena. Exigir alinhamento, hierarquia, grid e acabamento comercial.
- A fonte padrão gratuita para trilhas é o Pixabay, conforme `PADROES-DE-EDICAO.md`. Verificar a página individual e os termos vigentes de cada faixa, registrar evidências e nunca comprar músicas ou serviços sem autorização.
- Tratar o áudio original de forma moderada e não destrutiva: diagnosticar antes, preservar a voz natural, comparar antes/depois e reverter qualquer processamento que piore o resultado. Aplicar o procedimento detalhado de `PADROES-DE-EDICAO.md`.
- Fotos e vídeos de bancos devem representar a ação/contexto exatos da fala. Criar microbrief antes de pesquisar, inspecionar o asset e registrar origem/licença. Não usar stock genérico ou que sugira falsamente que a imagem é da empresa. Na Unsplash, conferir restrições e permissões adicionais para pessoas reconhecíveis, marcas e obras retratadas: https://unsplash.com/pt-br/licença e https://unsplash.com/terms.
- Na revisão, reproduzir o vídeo integralmente e verificar correspondência fala/imagem, qualidade do motion, trilha licenciada, inteligibilidade da voz e pertinência do B-roll. Falha crítica mantém EM REVISÃO.


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

### Estratégia de trilha sonora gratuita: Pixabay
Não comprar assinatura, licença paga, música, pacote ou serviço de áudio. A fonte padrão para trilhas é a biblioteca oficial de música do Pixabay: https://pixabay.com/pt/music/ . Usar somente faixas baixadas diretamente do site oficial e cuja página/termos vigentes permitam o uso comercial pretendido.

A licença Pixabay permite, em regra, uso comercial e adaptação sem atribuição obrigatória, desde que a música esteja incorporada a uma obra criativa maior e não seja redistribuída isoladamente. A licença não elimina direitos de terceiros eventualmente presentes, nem garante ausência de reivindicações automatizadas de Content ID. Consultar sempre os termos atuais: https://pixabay.com/service/license-summary/ e https://pixabay.com/service/faq/ .

Procedimento obrigatório por faixa:
1. Buscar música que combine com intenção, ritmo, público, fala e identidade do vídeo.
2. Abrir a página individual da faixa e verificar autor, título, duração, tags e informações disponíveis sobre licença/Content ID/restrições.
3. Baixar diretamente do Pixabay. Não usar reuploads, conversores, canais de terceiros ou arquivos sem origem comprovada.
4. Guardar no projeto o arquivo original, URL da página, nome/título, autor, data do download, cópia ou captura da página/licença vigente e IDs SG dos vídeos em que foi usado. Manter registro central de trilhas.
5. Usar a música sincronizada como parte da edição final, com voz inteligível, volume automatizado/ducking e sem clipping. Não publicar a faixa isolada nem disponibilizá-la como download independente.
6. Como o Pixabay informa que algumas faixas podem gerar reivindicações de Content ID, verificar página/FAQ e manter evidências. Se houver informação de Content ID ou histórico de reivindicação, preferir outra faixa quando possível. Não prometer que a faixa nunca terá reivindicação.
7. Se surgir reivindicação, não ignorar nem contestar automaticamente. Conferir faixa, uso e documentação; seguir procedimento oficial de disputa somente quando houver evidência suficiente de licença e uso permitido. Registrar ocorrência e substituir a música em publicações futuras se necessário.
8. Não usar trilha de origem, licença ou página individual incerta. Buscar outra opção no Pixabay. Não comprar nada nem recorrer a Artlist, Epidemic Sound ou biblioteca paga.

Trilha musical de fundo é requisito normal de acabamento dos vídeos. A falta de licença de uma biblioteca paga não é justificativa para deixar o vídeo sem música, pois a estratégia padrão é utilizar Pixabay conforme os controles acima. Exceção: se nenhuma faixa adequada puder ser validada para um vídeo específico, registrar a razão e pedir decisão apenas para aquele item; não inventar licença.


## Fonte única de identidade visual
A pasta oficial e exclusiva de ativos de marca é `Meu Drive/02 - SUA GRÁFICA BH/IDENTIDADE VISUAL/SUA_GRAFICA_BH_BRANDKIT/`. Abrir e inspecionar os arquivos reais antes de criar qualquer peça. Utilizar os ativos oficiais diretamente. É proibido recriar, redesenhar, vetorizar por aproximação, gerar por IA ou substituir logotipo, símbolo, fontes e grafismos. Não usar outra pasta, post antigo, memória ou descrição como fonte substituta. Se faltar um ativo, registrar pendência em vez de improvisar.


## Rotina recorrente de posts estáticos: 07 - IMPRESSÕES PRONTAS
Em toda execução do prompt, Claude deve verificar `Meu Drive/02 - SUA GRÁFICA BH/CONTEÚDOS/07 - IMPRESSÕES PRONTAS/`. Cada imagem inédita e elegível gera um post estático adicional individual (uma foto = uma publicação, nunca carrossel ou agrupamento). A rotina é incremental: consultar e atualizar `REGISTRO-IMPRESSOES-PRONTAS.md`, comparar ID do Drive, SHA-256 e similaridade visual quando disponível, e nunca republicar imagem já registrada. Se não houver imagem nova, não criar conteúdo estático adicional. Não renomear, mover, apagar ou alterar originais. Cada post recebe ID SG global sequencial, briefing individual em FEED/ e entrada própria no calendário como ADICIONAL, sem substituir a cadência regular. Confirmar privacidade, autorização de uso e catálogo antes de fazer afirmações. Manter pendências no ledger; não reprocessar automaticamente itens bloqueados.


## Comandos curtos de operação
João não precisa enviar novamente as regras de produção. Exemplos: `Finalize o lote de [datas/IDs].`; `Edite os vídeos [IDs].`; `Produza as artes [IDs].`; `Audite os briefings [IDs].` Claude deve interpretar o tipo de tarefa e seguir `PROMPT-UNICO-CLAUDE.md` como roteador, lendo os documentos especializados aplicáveis. `Finalize o lote` inclui QA, organização, Postiz e atualização dos registros; `Edite` limita-se aos IDs/formato solicitados e não autoriza distribuição por si só.
