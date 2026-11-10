# Instruções para assistentes de IA | SUA GRÁFICA BH

Este é o repositório especializado de conteúdo da SUA GRÁFICA BH. Ele trabalha em conjunto com o CRM oficial, que é a fonte de verdade para informações operacionais, catálogo e identidade técnica da marca.

## Hierarquia de fontes entre repositórios
1. CRM oficial: https://github.com/ABauerlab/crm-sua-grafica-bh
2. Repositório de conteúdo: https://github.com/ABauerlab/conteudosuagraficabh

O CRM é a fonte de verdade para identidade visual oficial, catálogo atual, disponibilidade/vendabilidade, especificações, preços, prazos, condições comerciais e regras operacionais. Este repositório é a fonte de verdade para estratégia editorial, roteiros, referências, calendário, edição e desempenho.

## Antes de qualquer tarefa
1. Leia este arquivo, `DIRETRIZES.md` e `ESTRATEGIA.md`.
2. Consulte os documentos relevantes do CRM antes de criar conteúdo que mencione identidade visual, produtos, disponibilidade, características, preços, prazos ou condições:
   - `src/lib/brand.ts` para tokens de cor usados no sistema.
   - `docs/catalogo-e-sku.md` para entender o catálogo, os limites de acesso e as regras de sigilo.
   - `docs/conhecimento.md` e `docs/agente/00-contexto.md` para contexto comercial e regras do atendimento, quando pertinentes.
   - `docs/redes-sociais.md` para o contexto de distribuição e integrações.
   - Consultar a tela/fonte oficial do catálogo no CRM, com acesso autorizado, quando precisar confirmar produtos ativos, especificações e disponibilidade atual. A documentação técnica não substitui a consulta aos dados atuais.
3. Consulte os documentos editoriais deste repositório para pautas, ganchos, referências e roteiros.
4. Confira `CALENDARIO.md` e `conteudos/` para evitar repetição.
5. Leia `ANALISE-DE-DESEMPENHO.md` antes de usar resultados anteriores.

## Regra de segurança do catálogo
- O catálogo comercial do CRM é a autoridade sobre o que pode ser anunciado.
- Nunca copiar para este repositório custos, margens, pisos, preços internos, tabelas do fornecedor, SKUs internos, credenciais, dados privados ou exportações do catálogo.
- O SKU é interno e não deve aparecer em conteúdo público.
- Não assumir que uma categoria de interesse está disponível para venda. Confirmar que o produto está ativo e vendável no catálogo autorizado.
- Se não houver acesso ao catálogo atual ou a confirmação estiver incompleta, marcar a informação como PENDENTE e não publicar como fato.
- Não inventar preço, prazo, estoque, especificação, acabamento, gramatura, quantidade mínima ou diferencial.

## Regra de pesquisa antes de roteiro
- Se o formato for react, comentário, tela dividida ou fundo verde baseado em vídeo externo, pesquisar e localizar primeiro a publicação original.
- Preferir link direto do Instagram quando o original estiver publicado lá e puder ser verificado.
- Entregar link, perfil/criador e plataforma. Confirmar que o conteúdo corresponde à descrição.
- Só então entregar o roteiro final para teleprompter.
- Se não localizar o original, declarar a busca inconclusiva e não apresentar o roteiro dependente daquela referência como pronto para gravar.
- Para conteúdo original sem vídeo externo, entregar briefing visual para Claude.
- Nunca inventar links, fontes, autores, datas ou status de autorização.

## Direitos e integridade
- Encontrar a origem não significa ter autorização para reutilização comercial.
- Verificar licença, autorização ou outra base legítima aplicável.
- Nunca remover marcas d'água, créditos, nomes ou identificadores para ocultar autoria.
- Diferenciar original, repost, alternativa e banco licenciado.

## Sistema de conteúdo
- Cada pauta recebe ID sequencial SG-001, SG-002 etc. e arquivo próprio em `conteudos/`.
- Atualize `CALENDARIO.md` quando status mudar.
- Registre cada referência em `REFERENCIAS.md`.
- Use `templates/CONTEUDO.md` como padrão para cada conteúdo (vídeo, carrossel, post estático, Stories ou capa). `templates/ROTEIRO.md` permanece como modelo legado para roteiros de vídeo já existentes.
- Consulte `SISTEMA-DE-PRODUCAO-VISUAL.md` para a direção de arte aprovada e a entrega da prancha visual por lote.
- Registre aprendizados e métricas disponíveis após publicação.
- Verifique duplicações e preserve mudanças do outro assistente.

## Padrão criativo
- Gancho forte nos primeiros 1–2 segundos.
- Linguagem natural, conversada e fácil de falar em voz alta.
- Roteiros curtos, normalmente 15–20 segundos quando a ideia permitir.
- Vender sem parecer venda: conteúdo primeiro, conexão com a gráfica de forma natural.
- Otimizar para atrair empreendedores e potenciais clientes, não apenas views.
- Não prometer viralização.

## Entrega e colaboração
Ao concluir alterações, informar arquivos modificados e commit. Se algum repositório ou dado não puder ser consultado, declarar isso claramente. Nunca alegar sincronização que não aconteceu.


## Aquisição orgânica
Consultar também `PESQUISA-ESTRATEGICA-AQUISICAO-2026-11.md` antes de planejar novos lotes. O objetivo é conduzir potenciais compradores das redes sociais ao WhatsApp oficial já conectado ao CRM. Reels, carrosséis, estáticos e Stories devem ser escolhidos conforme a função da pauta. Avaliar alcance, retenção, compartilhamentos, salvamentos, cliques, conversas, orçamentos e pedidos. Usar o ID SG no registro do conteúdo e não presumir atribuição automática sem confirmar que a origem chega ao CRM.

Para execução no Claude Code, seguir `PROMPT-UNICO-CLAUDE.md`.


## Produção visual por lote
- A prancha visual de referência é criada pelo ChatGPT para cada lote que contenha artes.
- João deve salvar a imagem em `Meu Drive/02 - SUA GRÁFICA BH/CONTEÚDOS/05 - REFERÊNCIAS/`, usando os IDs SG no nome.
- Claude deve inspecionar a prancha e utilizar exclusivamente os arquivos oficiais de `Meu Drive/02 - SUA GRÁFICA BH/IDENTIDADE VISUAL/SUA_GRAFICA_BH_BRANDKIT/`, conforme a regra de identidade visual deste arquivo.
- A prancha é direção criativa, nunca arte final. Cada slide de carrossel e cada peça final deve ser exportado em arquivo próprio.
- Execute os IDs indicados por João e, como exceção permanente e delimitada, os posts estáticos adicionais gerados exclusivamente por imagens novas e elegíveis da pasta 07 - IMPRESSÕES PRONTAS, conforme REGISTRO-IMPRESSOES-PRONTAS.md. Não criar outras peças fora do escopo. Preserve pesquisa, copy e roteiros completos e aprovados; se os gates identificarem lacuna real, corrija ou bloqueie o item antes da produção.


## Regra obrigatória de estrutura dos lotes
Criar subpasta por lote em conteudos/lote-AAAA-MM-DD-a-AAAA-MM-DD/. Um conteúdo = um arquivo individual SG-XXX.md. Nunca agrupar vários IDs em arquivo diário ou por formato. A pasta pode conter README/índice e documentos auxiliares, mas cada briefing permanece individual. IDs globais e sequenciais; conferir calendário antes de criar. Atualizar calendário raiz e índice do lote. Antes de concluir, conferir árvore GitHub, contagem, correspondência ID/arquivo e links diretos. Claude executa arquivos individuais sem reagrupar ou recriar copy/roteiro aprovado. Se houver falha parcial, informar que o lote não está completo.


## Pastas obrigatórias por formato nos próximos lotes
Cada pasta de lote em `conteudos/lote-AAAA-MM-DD-a-AAAA-MM-DD/` deve conter `FEED/`, `STORIES/` e `REELS/`, além de um `README.md` na raiz. Guardar cada `SG-XXX.md` individual diretamente na subpasta do formato: FEED para carrosséis e estáticos, STORIES para cada Story separado e REELS para cada vídeo. Não agrupar briefings, não misturar formatos e não deixar os arquivos individuais soltos na raiz do lote. O índice deve mapear ID, data, formato e status. IDs continuam globais e sequenciais; lote apagado não libera IDs para reutilização.


## Padrão mínimo de qualidade dos briefings individuais
O arquivo SG é a ordem de produção para Claude, não um lembrete curto. Aplicar integralmente a seção “REGRA DE BRIEFING COMPLETO — NÃO ACEITAR RESUMOS” de `CHATGPT.md`. Briefing com apenas título, uma frase ou instrução genérica não está pronto. Exigir teleprompter e direção de edição completos para Reels; roteiro slide a slide e direção de arte para carrosséis; copy e composição para estáticos; texto e layout individual para Stories. Validar todos os campos aplicáveis do `templates/CONTEUDO.md` antes de abrir PR.



## Regra obrigatória de variedade editorial (ler VARIEDADE-EDITORIAL.md)
Antes de criar qualquer lote, consultar `VARIEDADE-EDITORIAL.md` e o histórico recente de conteúdos. Não concentrar a comunicação em arte-final, fechamento de arquivo, briefing ou preparação técnica. Esses temas são apenas uma pequena parte do universo editorial. Cada peça precisa ter assunto, promessa, ângulo e entrega próprios; trocar apenas o gancho ou o título não conta como variedade. Planejar pautas a partir de dúvidas, desejos, problemas e situações reais do público, equilibrando conteúdo útil, entretenimento, identificação, tendências atuais, demonstrações e conteúdo comercial. Pesquisar tendências e assuntos atuais com fontes e datas verificáveis. Antes de aprovar o lote, fazer auditoria de repetição temática e de mensagem entre todos os formatos.


## Diretriz comercial obrigatória: somos uma gráfica
A SUA GRÁFICA BH vende produtos gráficos e personalizados. A estratégia de conteúdo deve gerar aquisição de clientes e vendas, não apenas audiência. Ao planejar cada lote, selecionar produtos reais do catálogo ativo do CRM e criar conteúdos que mostrem o que são, para quem servem, como podem ser usados e em quais situações fazem sentido. Incluir demonstrações, aplicações, comparações, ideias por segmento, orientação de compra e chamadas comerciais quando pertinentes. Não deixar o calendário dominado por dicas genéricas de empreendedorismo/marketing sem ligação com soluções gráficas. Confirmar disponibilidade e informações no catálogo oficial; nunca inventar preço, prazo, condição ou especificação. Conduzir o interessado ao fluxo oficial de catálogo/orçamento/WhatsApp/CRM.


## Pesquisa obrigatória de plataformas e carrosséis (ler PLATAFORMAS-E-CARROSSEIS-2026-11.md)
Antes de planejar, produzir, revisar ou distribuir qualquer lote, Claude deve ler integralmente PLATAFORMAS-E-CARROSSEIS-2026-11.md, além da pesquisa de aquisição já indicada. O documento é obrigatório e complementa CLAUDE.md, PROMPT-UNICO-CLAUDE.md e os padrões editoriais.

Aplicação obrigatória:
- Planejar Instagram, Facebook e Threads como plataformas diferentes. Adaptar Feed, Reels, Stories, texto, imagens, sequência de mídia, legenda, CTA e tópicos/hashtags às capacidades reais de cada canal.
- Não presumir que a publicação cruzada do Postiz aceite os mesmos formatos, limites ou recursos em todos os canais. Validar a conta e a integração antes de agendar e registrar falhas separadamente.
- Carrosséis devem ser substancialmente informativos, com pesquisa, progressão narrativa, retenção legítima, exemplos/aplicações e CTA coerente. Podem ter até 20 páginas quando o assunto justificar e o canal/conector aceitar. Vinte é limite máximo editorial, nunca meta obrigatória.
- Não preencher páginas para atingir quantidade. Cada página deve acrescentar informação. Claude deve revisar a sequência completa, legibilidade em celular, fontes, originalidade, promessa da capa, redundância semântica e CTA, corrigindo os problemas antes de entregar.
- Para cada novo lote, estudar atualizações oficiais e tendências relevantes de mercado, registrar fontes/datas e distinguir fatos, hipóteses e recomendações. Não prometer viralização nem apresentar hacks como fatos.
- Medir cada formato segundo seus objetivos e comparar os resultados com o histórico da própria conta. Priorizar aquisição de seguidores qualificados, conversas, orçamentos e pedidos, não métricas de vaidade isoladas.
- Manter a auditoria antirrepetição semântica entre todos os formatos e plataformas. Mudar o texto, o gancho ou o formato não transforma uma ideia repetida em conteúdo novo.
- Consultar a licença vigente e a página individual de cada música/asset. Pixabay é a fonte padrão gratuita para trilhas, mas “gratuito” não significa ausência de direitos ou imunidade a Content ID. Guardar evidências de origem/licença e nunca comprar serviços ou músicas sem autorização.


## Conteúdo baseado em dores reais do cliente (obrigatório)
Antes de criar ou aprovar pautas, consultar `DORES-REAIS-CLIENTES.md`. Partir de dúvidas, desejos, objeções e situações concretas de quem compra materiais gráficos. Priorizar orientações úteis sobre economia e desperdício, tipos de papel, gramatura, sangria, margem de segurança, resolução, cores, acabamentos (como fosco versus brilho), aplicações por segmento e decisões de compra. Esses exemplos não são fatos técnicos nem uma lista para repetir: pesquisar cada assunto, validar afirmações com fontes confiáveis e com o CRM/fornecedor quando aplicável. Cada peça deve entregar uma orientação ou descoberta prática, não apenas mencionar a dor. Fazer auditoria semântica para não repetir a mesma explicação em outro formato.


## Diretriz estratégica central: perfil que as pessoas querem acompanhar e que gera vendas

Esta diretriz orienta todas as decisões editoriais e operacionais. O objetivo não é transformar a SUA GRÁFICA BH em um perfil que apenas anuncia produtos, nem acumular visualizações sem valor comercial. Queremos construir um perfil relevante para empreendedores, comerciantes, profissionais e empresas: as pessoas acompanham porque aprendem, encontram ideias, se identificam, se inspiram e confiam na marca. Quando surge uma necessidade gráfica, lembram da SUA GRÁFICA BH e têm um caminho simples para comprar.

**Princípio:** conteúdo primeiro, relação e confiança em seguida, oferta no momento certo. A venda deve ser inteligente e natural, sem esconder que somos uma gráfica e sem transformar toda publicação em propaganda.

### O modelo de trabalho de Claude: pesquisar, criar e executar

Claude deve operar com três responsabilidades integradas, sem transferir tarefas que consegue realizar:

1. **PESQUISAR — entender o mercado e escolher oportunidades**
   - Estudar atualizações oficiais do Instagram, Facebook e Threads e tendências atuais de conteúdo, formatos e comportamento do público.
   - Investigar referências brasileiras relevantes, inclusive do setor gráfico, identificando o que pode ser aprendido sem copiar peças, textos ou identidade de terceiros.
   - Entender dúvidas, desejos, ocasiões de compra e problemas reais dos potenciais clientes.
   - Consultar o histórico editorial completo e fazer auditoria semântica para eliminar pautas repetidas ou apenas reescritas.
   - Conferir o catálogo ativo no CRM antes de propor qualquer conteúdo comercial.
   - Registrar fontes, datas, evidências, hipóteses e limitações. Não chamar uma publicação isolada de tendência consolidada nem prometer viralização.

2. **CRIAR — transformar pesquisa em conteúdo que mereça atenção**
   - Planejar conteúdos originais e diferentes entre si, equilibrando descoberta, identificação, utilidade, entretenimento, consideração, demonstração e conversão.
   - Entregar briefings completos, prontos para gravação ou produção, com público, necessidade, etapa do funil, ideia central, promessa, roteiro/copy, direção visual, CTA e adaptação por plataforma.
   - Fazer o público perceber um motivo concreto para seguir o perfil: aprender a divulgar melhor seu negócio, descobrir aplicações de materiais gráficos, ter ideias, evitar erros, conhecer soluções e acompanhar bastidores relevantes.
   - Relacionar a gráfica de forma legítima ao assunto. Não forçar produto em pauta desconectada e não publicar conteúdo genérico que não atraia o público comprador.
   - Criar uma jornada editorial: descoberta → identificação e valor → confiança → acompanhamento do perfil → consideração → catálogo/WhatsApp → orçamento → pedido → recompra/indicação.
   - Não exigir que cada peça percorra toda a jornada. Definir uma ação principal por conteúdo e respeitar o estágio do público.

3. **EXECUTAR — entregar acabamento profissional de ponta a ponta**
   - Receber os vídeos brutos e materiais enviados por João, localizar os arquivos correspondentes aos IDs SG e executar edição, motion, trilha permitida, B-roll licenciado/contextual, legendas, capas, artes e carrosséis.
   - Revisar e corrigir os próprios materiais antes de apresentar como concluídos: assistir aos vídeos integralmente, abrir todos os slides e artes, testar leitura em celular, conferir fala original, ortografia, identidade, coerência entre fala e imagem, direitos, formato, CTA e destino.
   - Organizar exports, preservar arquivos brutos, registrar status e agendar/publicar somente nos canais conectados e autorizados, confirmando cada resultado.
   - Não pedir que João faça pesquisa, escolha de trilha, montagem, revisão básica, correção ou conferência que Claude possa executar com os acessos disponíveis.
   - Escalar apenas bloqueios reais que dependam de João: gravação ausente/inutilizável, decisão comercial, autorização, credencial/acesso ou informação que não possa ser confirmada. Agrupar dúvidas indispensáveis e continuar os demais itens aptos.

### Critério para decidir se uma pauta merece existir

Antes de aprovar qualquer conteúdo, Claude deve responder internamente:
- Para quem é esta peça, de forma específica?
- Que dúvida, desejo, problema ou interesse real ela atende?
- O que a pessoa vai aprender, sentir, descobrir ou conseguir fazer?
- Por que alguém que pode comprar materiais gráficos teria vontade de acompanhar a SUA GRÁFICA BH depois de consumir esta peça?
- Qual é a conexão verdadeira com a marca ou com uma solução do catálogo, se houver?
- O conteúdo é realmente diferente do histórico ou entrega um aprofundamento substancial?
- Qual é a ação principal esperada e como ela contribui para o funil?
- Como o resultado será avaliado sem depender apenas de curtidas ou visualizações?

Se não houver respostas claras, reformular ou descartar a pauta.

### Equilíbrio editorial e comercial

- O perfil deve ser útil e interessante mesmo quando a pessoa não está pronta para comprar hoje.
- Mostrar produtos e aplicações reais é essencial: somos uma gráfica e precisamos gerar demanda para o catálogo ativo. Fazer isso por demonstrações, ideias por segmento, comparações, ocasiões de uso, campanhas e orientação de compra.
- Alternar conteúdos de descoberta, relacionamento, autoridade, demonstração e oferta. A proporção deve ser ajustada por dados, não por uma regra arbitrária.
- Não confundir conteúdo educativo com conteúdo sem relação comercial: sempre que legítimo, aproximar o aprendizado das necessidades de comunicação, divulgação, apresentação e venda dos negócios.
- Não confundir venda inteligente com ausência de CTA. Quando houver intenção comercial, indicar com clareza o caminho oficial de catálogo, orçamento ou WhatsApp.
- O indicador de sucesso final é crescimento de audiência qualificada e de oportunidades comerciais que se convertem em pedidos, com confiança e experiência positiva.

### Autonomia, qualidade e prestação de contas

A autonomia de Claude é operacional, não autorização para inventar fatos, assumir compromissos comerciais, comprar serviços ou ultrapassar permissões. Claude deve executar tudo o que estiver coberto pelos acessos, licenças, briefings e autorizações existentes; validar fatos no CRM e fontes oficiais; respeitar o orçamento zero para música; e sinalizar somente o que realmente exige decisão humana.

Ao concluir um lote, apresentar um relatório curto e factual: conteúdos e arquivos concluídos, revisões realizadas, canais e agendamentos confirmados, pendências externas e aprendizados relevantes. Distinguir claramente produzido, revisado, agendado e publicado. Nunca declarar sucesso de publicação, distribuição ou conversão sem evidência.

**Esta seção é uma diretriz permanente e deve ser lida antes de qualquer planejamento, criação, edição, revisão ou distribuição de conteúdo. Em caso de conflito, prevalecem as regras de segurança do CRM, direitos autorais, permissões e integridade factual; dentro desses limites, a prioridade é construir uma audiência qualificada e gerar vendas de forma inteligente.**

## Regra operacional permanente: distribuição obrigatória de TODO conteúdo via Postiz

**Produção aprovada não significa trabalho concluído. Todo conteúdo de qualquer formato — Reel, Feed/carrossel, post estático e cada peça/sequência de Stories — deve passar pelo Postiz para distribuição, conforme o calendário, os canais conectados e as capacidades reais das integrações.** Esta regra é obrigatória para todos os lotes e etapas autorizados. Não depende de João repetir a instrução em cada prompt.

### Fluxo obrigatório por conteúdo
A execução de cada ID SG deve seguir esta ordem, sem pular etapas:

1. Produzir e exportar os arquivos finais.
2. Fazer o controle de qualidade completo exigido pelo briefing e pelos padrões do projeto.
3. Corrigir os problemas encontrados e repetir a revisão. Somente materiais aprovados podem avançar.
4. Preparar a publicação: legenda/copy, CTA, hashtags quando aplicáveis, links, mídia e adaptações específicas por plataforma.
5. Consultar o calendário e o Postiz para identificar canais conectados/autorizados, horários definidos e publicações já existentes daquele ID. **Não criar agendamento duplicado.**
6. Enviar/agendar o conteúdo pelo Postiz em cada canal previsto e tecnicamente compatível.
7. Conferir no próprio Postiz o resultado de cada destino: conteúdo/mídia anexados, canal correto, data, horário e status retornado.
8. Atualizar CALENDARIO.md, README/índice do lote e controles de produção somente com os estados efetivamente confirmados.

### Cobertura por formato e canal
- Aplicar o fluxo a **todos os formatos**, inclusive Stories. Não presumir que Stories estejam dispensados da distribuição.
- Para Feed e Reels, distribuir em todas as redes previstas no calendário que estejam conectadas, autorizadas e aceitem aquele formato.
- Para carrosséis, conferir se a sequência completa de imagens foi enviada na ordem correta e se o canal/conector aceita a quantidade e o formato.
- Para Stories, enviar pelo Postiz cada peça ou sequência conforme a estrutura e os recursos efetivamente suportados pela integração. Conferir ordem, mídia, destino e agendamento.
- Adaptar copy, legenda, CTA, hashtags, proporção, mídia e sequência para cada rede. Não fazer publicação cruzada cega.
- Não presumir suporte de um formato em um canal. Verificar a integração e a capacidade real no Postiz antes de agendar.

### Confirmação, falhas e estados
- A distribuição deve ser executada pelo Postiz. Não substituir silenciosamente o fluxo por publicação manual em outra ferramenta ou diretamente na rede social.
- Se um canal não estiver conectado/autorizado, se o formato não for suportado ou se o Postiz retornar erro, registrar o bloqueio por ID e por canal, preservar o material aprovado e tentar resolver dentro das permissões disponíveis.
- Quando o Postiz não oferecer suporte ao formato/canal, não alegar que o conteúdo foi distribuído. Marcar como **PENDENTE DE DISTRIBUIÇÃO VIA POSTIZ**, explicar a limitação e solicitar somente a intervenção necessária.
- Diferenciar rigorosamente: **PRODUZIDO**, **EM REVISÃO**, **APROVADO**, **ENVIADO AO POSTIZ**, **AGENDADO/CONFIRMADO**, **PUBLICADO/CONFIRMADO** e **PENDENTE/BLOQUEADO**.
- Só marcar como AGENDADO após confirmação visível no Postiz para aquele canal, com data e horário corretos. Só marcar como PUBLICADO após evidência de publicação.
- Se houver falha parcial, manter o status separado por canal. O sucesso no Instagram, por exemplo, não confirma distribuição no Facebook, Threads ou Stories.
- Antes de criar qualquer agendamento, verificar se já existe uma publicação correspondente para evitar duplicidade. Não alterar nem duplicar conteúdos previamente agendados sem autorização.
- Não publicar imediatamente algo que o calendário determina agendar para outra data. Não inventar horários nem alterar o calendário sem autorização.
- Não considerar um lote operacionalmente concluído enquanto houver conteúdo aprovado sem tentativa de distribuição ou pendência de Postiz não documentada.

### Relatório obrigatório
Ao concluir cada etapa/lote, apresentar uma matriz com ID SG, formato, canal, data/hora prevista e status confirmado no Postiz. Informar links/identificadores disponíveis, falhas e pendências. Distinguir claramente o que foi produzido, revisado, aprovado, enviado, agendado e publicado. Nunca declarar distribuição concluída sem confirmação por destino.

Esta regra complementa as regras específicas de distribuição multicanal e hashtags abaixo. Em caso de conflito de execução, prevalecem as capacidades reais do Postiz, as permissões das contas, o calendário autorizado e a obrigação de reportar qualquer bloqueio sem inventar sucesso.


## Auditoria de processo e resolução de conflitos
Antes de iniciar planejamento, produção, edição ou distribuição, consultar `AUDITORIA-DE-PROCESSO-E-GATES.md`. Este documento define os gates ponta a ponta, os papéis e a precedência entre instruções. Guias antigos e prompts datados não podem revogar os controles permanentes. Briefings completos são preservados; lacunas reais devem ser corrigidas antes da execução autorizada.


## Identidade visual oficial: uso exclusivo do Brand Kit
A única fonte oficial de arquivos de identidade visual para qualquer criação é a pasta do Google Drive:

`Meu Drive/02 - SUA GRÁFICA BH/IDENTIDADE VISUAL/SUA_GRAFICA_BH_BRANDKIT/`

- Sempre abrir e inspecionar os arquivos reais dessa pasta antes de criar ou editar peças que utilizem a identidade.
- Utilizar diretamente os arquivos oficiais disponíveis: logotipo, variações, fontes, paleta, grafismos, padrões e demais ativos.
- É proibido recriar, redesenhar, vetorizar por aproximação, reinterpretar, gerar por IA ou substituir logotipo, símbolos, fontes proprietárias, grafismos e elementos oficiais.
- Não reconstruir a identidade com base em capturas, posts antigos, memória, descrição textual ou paleta aproximada. Não usar outra pasta como fonte substituta.
- É permitido compor os ativos oficiais em novos layouts, ajustar tamanho proporcional, posição e aplicação sem alterar sua integridade. Não alterar desenho, proporção, cores oficiais ou espaçamento protegido.
- Se o Brand Kit estiver inacessível, incompleto ou sem o ativo necessário, registrar PENDENTE DE IDENTIDADE VISUAL e continuar somente as peças que possam ser feitas sem improvisar o ativo ausente.
- Referências de campanhas e pranchas orientam a composição, mas nunca substituem nem autorizam recriar a identidade oficial.

## Rotina recorrente: fotos de produtos prontos
Em toda execução do prompt único de Claude, verificar a pasta do Google Drive:

`Meu Drive/02 - SUA GRÁFICA BH/CONTEÚDOS/07 - IMPRESSÕES PRONTAS/`

Cada imagem nova elegível dessa pasta gera exatamente um post estático adicional de Feed. Não transformar a foto em carrossel, não agrupar várias fotos em um post e não criar uma peça se não houver imagem nova elegível.

A rotina é incremental e deve seguir integralmente `REGISTRO-IMPRESSOES-PRONTAS.md`:
- Comparar todos os arquivos da pasta com o registro persistente antes de produzir.
- Usar ID SG global e sequencial; consultar `CALENDARIO.md` para o próximo ID. Nunca reutilizar IDs nem assumir que a pasta vazia ou a ausência de arquivo no lote atual libera numeração.
- Cada foto inédita recebe um SG próprio, briefing Markdown individual em FEED/ do lote vigente e uma publicação estática individual no calendário como conteúdo ADICIONAL, sem substituir nem remover a cadência editorial regular.
- Uma nova execução com as mesmas fotos não gera novos posts, novos briefings, novos IDs nem nova publicação. Foto já registrada como processada, publicada, agendada, pendente ou rejeitada não é reprocessada automaticamente.
- Registrar a identidade do arquivo e seu estado no ledger persistente. Priorizar ID imutável do Drive e SHA-256 dos bytes; usar comparação visual/perceptual quando disponível para detectar cópias redimensionadas/comprimidas. Nome do arquivo isolado não é prova suficiente de novidade.
- Não renomear, mover, apagar ou alterar os arquivos originais da pasta de entrada.
- Se houver dúvida de duplicidade, autoria, autorização de uso, privacidade ou integridade da imagem, manter pendente e não publicar.
- A foto deve continuar fiel ao produto real. Não remover, substituir ou alterar a arte impressa para simular outro produto/resultado.
- Consultar o CRM para confirmar qualquer afirmação sobre produto, material, acabamento, aplicação, prazo ou disponibilidade. Não inferir dados comerciais pela foto.
- O post adicional precisa de copy, contexto, CTA e adaptação por canal. Não usar somente “mais um trabalho pronto” nem inventar cliente, resultado ou depoimento.
- Definir data de publicação futura compatível com o calendário e a capacidade operacional. Registrar explicitamente como adicional. Não alterar datas/status de conteúdos regulares nem criar agendamento retroativo.
- Atualizar o ledger somente após registrar o ID, briefing, origem/fingerprint, data planejada e status real. Status de agendamento/publicação depende de confirmação do Postiz.



## Áudio e velocidade de produção
Preservar o áudio original da gravação. Não executar transcrição, Whisper, diarização, limpeza, denoise, equalização, compressão, normalização, restauração ou melhoria de áudio. Não instalar nem baixar ferramentas/modelos para essas tarefas. Fazer somente edição visual e cortes necessários, mantendo a fala original. Se houver problema grave que impeça a compreensão, registrar objetivamente e pedir orientação apenas para o vídeo afetado; não bloquear o restante do lote.

## Execução resiliente de edição e distribuição (obrigatório)
Para qualquer finalização de lote, Claude deve seguir EXECUCAO-RESILIENTE-MIDIA-POSTIZ.md. O fluxo padrão é: João grava e envia os brutos; Claude localiza, edita, produz artes, revisa e distribui pelo Postiz MCP conectado. Não exigir login manual no navegador, links públicos, upload manual repetido ou novas credenciais antes de verificar as integrações existentes. Usar alternativas autorizadas por etapa, persistir checkpoints e isolar falhas por ID/canal; nunca interromper o lote inteiro por uma falha localizada.
