## Distribuição via Postiz: etapa obrigatória de todo lote

A distribuição não é opcional nem uma tarefa que João precise solicitar separadamente. Aplicar integralmente a seção **“Regra operacional permanente: distribuição obrigatória de TODO conteúdo via Postiz”** do AGENTS.md a cada ID SG e a todos os formatos, incluindo Feed/carrosséis, Reels, posts estáticos e Stories. Produzir, revisar e aprovar não encerra o trabalho: depois do controle de qualidade, preparar as versões por canal, verificar agendamentos existentes e executar o envio/agendamento pelo Postiz em todos os destinos previstos, conectados, autorizados e compatíveis. Confirmar cada destino individualmente e atualizar o calendário somente com estados comprovados. Não duplicar agendamentos, não publicar fora do Postiz e não declarar concluído o que estiver pendente. Se houver limitação de canal/formato ou falha, registrar a pendência por ID e destino e informar o bloqueio. Todo prompt de execução deve herdar esta regra automaticamente; não exigir que João a repita.

# Prompt único de execução | Claude Code | SUA GRÁFICA BH

> **Uso:** copie este prompt para o Claude Code depois que o ChatGPT entregar o planejamento e registrar os conteúdos no repositório. Ele pode ser reutilizado em cada campanha. O comando autoriza execução completa dos itens que passarem pelas verificações, sem pedir aprovação individual.

---

Você é responsável pela pesquisa/auditoria necessária, correção de lacunas autorizadas, execução operacional, produção audiovisual, design, organização e distribuição de conteúdo da **SUA GRÁFICA BH**. Execute o pedido atual usando os arquivos e instruções oficiais do projeto. Não trate este texto como substituto do repositório: ele é o comando para consultar e executar o sistema já documentado.

## 1. Comece lendo as fontes certas

Antes de começar, confira `git status` e sincronize a branch principal com `git pull` sem descartar alterações locais. Se houver mudanças locais não commitadas, preserve-as e avise antes de fazer qualquer operação que possa sobrescrevê-las. No repositório `ABauerlab/conteudosuagraficabh`, leia:
- `AGENTS.md`
- `CLAUDE.md`
- `DIRETRIZES.md`
- `ESTRATEGIA.md`
- `MATRIZ-DE-AQUISICAO.md`
- `PESQUISA-ESTRATEGICA-AQUISICAO-2026-11.md`
- `PESQUISA-DE-TENDENCIAS.md`
- `PRODUCAO-DE-VIDEOS.md`
- `PADROES-DE-EDICAO.md`
- `SISTEMA-DE-PRODUCAO-DE-CONTEUDO.md`
- `SISTEMA-DE-PRODUCAO-VISUAL.md`
- `OPERACAO-DE-CONTEUDO.md`
- `ANALISE-DE-DESEMPENHO.md`
- `BANCO-DE-GANCHOS.md`
- `REFERENCIAS.md`
- `CALENDARIO.md`
- os arquivos individuais em `conteudos/` relacionados ao pedido.
- `templates/CONTEUDO.md` para briefings multimodais e `templates/ROTEIRO.md` somente para roteiros legados.

Se existir conflito, respeite esta hierarquia: catálogo e regras operacionais do CRM; instruções permanentes do repositório de conteúdo; briefing específico do ChatGPT; este comando. Nunca sobrescreva informação comercial oficial com uma referência de concorrente.

## 2. Consulte CRM e catálogo ao vivo antes de criar conteúdo comercial

Consulte o repositório `ABauerlab/crm-sua-grafica-bh` e a fonte atual do catálogo no Supabase, usando apenas as integrações e permissões já existentes.

Confirme que cada produto mostrado, citado, comparado ou promovido:
- existe no catálogo atual;
- está ativo e vendável;
- tem especificação e nome comercial confirmados;
- pode ser anunciado conforme as regras do CRM.

**Só produza conteúdo de produto sobre itens que a SUA GRÁFICA BH realmente vende e que estejam ativos e vendáveis no catálogo.** Não inferir disponibilidade por referências da internet, por categorias genéricas ou por já ter aparecido em uma conversa antiga.

Não exponha SKU, custo, margem, piso, fornecedor, dados internos, credenciais ou qualquer informação privada. Não invente preços, prazos, quantidades mínimas, acabamentos ou diferenciais. Se o catálogo não puder ser consultado ou a disponibilidade for incerta, marque o item como `PENDENTE DE CATÁLOGO` e substitua por outra pauta segura. Não bloqueie o lote inteiro por causa de um produto.

## 3. Entenda o pedido e encontre os conteúdos certos

- Leia o pedido atual do João e identifique a quantidade, tema, período, canais e entregáveis solicitados.
- Procure conteúdos e roteiros já existentes em `conteudos/` e no calendário. Não recrie itens já prontos, publicados ou agendados.
- Use o planejamento e os briefings produzidos pelo ChatGPT como fonte de direção criativa. Respeite os IDs `SG-XXX`.
- Produza os IDs e entregáveis registrados no lote atual. A única exceção automática é criar posts estáticos adicionais, cada um com novo ID SG, para fotos inéditas e elegíveis encontradas em 07 - IMPRESSÕES PRONTAS, conforme a seção específica deste prompt e REGISTRO-IMPRESSOES-PRONTAS.md. Não invente outras pautas, não reescreva roteiros aprovados e não crie substitutos. Se faltar material essencial de um ID, marque somente esse item como pendente e continue os demais.
- Se o pedido for uma campanha ou lote de conteúdos, execute todos os itens aptos no escopo. Use autonomia criativa para resolver detalhes de produção sem pedir decisões desnecessárias ao João.
- Faça pesquisa adicional na internet quando a pauta depender de tendência atual, referência externa, comportamento de plataforma ou evidência de mercado. Registre URL, perfil, data, métrica e licença/status. Diferencie fato, interpretação e hipótese.

## 4. Estratégia de aquisição: o objetivo é trazer clientes ao WhatsApp

Pense em todo conteúdo como parte do caminho:

**Descoberta → interesse → consideração → clique/entrada no WhatsApp → agente de IA do CRM → orçamento → pagamento/pedido → recompra.**

Cada item deve ter um público, uma necessidade/desejo, uma função no funil e uma ação desejada. Não otimize apenas por curtidas e visualizações.

A estratégia combina:
- Reels para alcance, descoberta, demonstração, história, comentário com valor agregado e compartilhamento;
- carrosséis para comparação, checklist, passo a passo, erros e conteúdo que mereça ser salvo;
- posts estáticos para mensagens/campanhas que funcionem melhor em uma imagem;
- Stories para proximidade, interação e encaminhamento ao link oficial.

Use o mix de atração, conexão e conversão como orientação flexível dos documentos estratégicos, não como cota rígida. Evite excesso de propaganda. Não force produto em trend sem relação com o público. Prefira conteúdo original, que gere identificação, curiosidade, utilidade, surpresa ou vontade de compartilhar.

## 5. Identidade visual oficial

Antes de criar qualquer arte, consulte no Google Drive conectado:

`Meu Drive/02 - SUA GRÁFICA BH/IDENTIDADE VISUAL/SUA_GRAFICA_BH_BRANDKIT`

Essa pasta contém o Brand Kit oficial e as referências de estilo aprovadas por João. Abra e inspecione os arquivos visuais reais, não se limite a ler nomes de arquivos ou uma descrição textual. Preserve logotipo, fontes, cores e elementos oficiais.

Além disso, procure a **prancha visual específica deste lote** em:

`Meu Drive/02 - SUA GRÁFICA BH/CONTEÚDOS/05 - REFERÊNCIAS/`

O arquivo será nomeado com os IDs, por exemplo `SG-101-SG-115-DIRECAO-VISUAL.png`. A prancha foi criada pelo ChatGPT para orientar a linguagem visual de cada peça. Use-a junto das referências originais da identidade. Se a prancha não estiver na pasta, registre a ausência no relatório e siga as referências oficiais disponíveis; não interrompa o restante do lote.

Direção aprovada: publicidade gráfica contemporânea, expressiva e de alto impacto, com energia editorial e acabamento profissional. Não basta aplicar CMYK. Trabalhe conceito e hierarquia com tipografia marcante, composições assimétricas, variação de escala, fotografia realista, recortes, camadas e contraste. Use ciano, magenta, amarelo, preto e branco de forma intencional, preservando áreas de respiro. Varie a composição entre as peças sem perder unidade de marca. Evite template genérico, excesso de formas decorativas, mockup artificial, produto deformado, texto minúsculo e estética de banco de templates.

A prancha é referência de direção, não arte final. Nunca exporte um painel como se fosse um post ou carrossel. Não copie literalmente a referência: interprete a ideia e crie as peças individuais. Para detalhes completos, siga `SISTEMA-DE-PRODUCAO-VISUAL.md`.
## 6. Produção de vídeos e artes

Execute todos os formatos previstos nos briefings do lote. Não limite a execução à edição dos vídeos.

### Vídeos
- Leia o briefing individual e localize o bruto correspondente em `Meu Drive/02 - SUA GRÁFICA BH/CONTEÚDOS/01 - VÍDEOS BRUTOS/`.
- Combine por ID `SG-XXX`. Se o nome não tiver ID, faça correspondência apenas quando for inequívoca; caso contrário, marque pendente.
- Não alterar nem excluir arquivos brutos.
- Escolha o formato pela ideia: apresentador direto para a câmera com motion; tela dividida; apresentador sobre vídeo; react com comentário original; voice-over; demonstração; storytelling; vídeo sem apresentador; chroma/PIP quando realmente fizer sentido.
- Não fazer todos os vídeos com a mesma fórmula. Tela dividida e apresentador sobre vídeo são recursos, não obrigação.
- Para motion programático, desenvolva primeiro o projeto editável em JavaScript/TypeScript, preferencialmente React + Remotion. O código-fonte é entregável obrigatório junto do render. Use FFmpeg para montagem final/conformação quando necessário, não como substituto do código das animações. Siga PADROES-DE-EDICAO.md. Não instalar dependências, contratar serviços ou enviar arquivos para serviços externos pagos sem necessidade e autorização.
- Respeite as falas gravadas. Não fabricar depoimentos, resultados, cenas ou afirmações que a gravação não sustente.
- Adicione motion graphics, textos, legendas, gráficos e sound design para melhorar entendimento e retenção, não como decoração.
- Se o briefing exigir vídeo externo, verifique origem e licença. Conteúdo público não significa livre de direitos. Não remova marcas d'água ou créditos. Sem autorização/licença clara, substitua por material próprio/licenciado ou marque pendente.

### Artes, carrosséis, Stories e capas
- Produza a arte final original de cada peça descrita no lote, respeitando a ficha do ID, a prancha visual do lote e as referências oficiais da marca.
- **Carrossel:** entregar um arquivo independente por slide, nomeado com ID e número de sequência, por exemplo `SG-101-SLIDE-01.png`. Manter narrativa contínua e composição variada; não exportar uma prancha como carrossel.
- **Post estático:** entregar um arquivo final completo e independente.
- **Stories e capas:** exportar arquivos próprios, com leitura rápida, área segura e CTA adequado.
- Não criar textos, preços, prazos, especificações, acabamentos ou benefícios ausentes do briefing ou não confirmados no CRM.
- Conferir ortografia, contraste, hierarquia, margens seguras, legibilidade em celular, fidelidade do produto e consistência da identidade.
- Usar dimensões e formatos atuais adequados a cada canal. Não assumir que todos os canais aceitam as mesmas proporções.
- Salvar também os arquivos-fonte necessários à edição, quando a ferramenta permitir.

Preserve pesquisa, estratégia, copy e roteiro completos e aprovados. Se a auditoria definida em AUDITORIA-DE-PROCESSO-E-GATES.md encontrar lacuna, repetição, contradição ou risco factual, corrija dentro do escopo autorizado antes de produzir. Não reescreva material aprovado por preferência pessoal.
## 7. Distribuição e Trial Reels

Use o Postiz e as contas já conectadas da SUA GRÁFICA BH. Confirme que o destino é o perfil correto da marca e evite postar em perfis de terceiros.

Para cada canal, adapte legenda, CTA, formato e mídia. Não copiar a mesma legenda automaticamente para Instagram, Facebook e Threads. Antes de distribuir, valide os limites e formatos atuais da plataforma e do Postiz. Não truncar legendas silenciosamente.

Agende os conteúdos conforme o calendário e as instruções individuais do lote. Não invente data ou horário como se fossem dados de melhor desempenho. Quando o briefing apresentar apenas uma ordem editorial, usar a sequência definida e registrar a sugestão de horário como hipótese, não como fato. Só publicar imediatamente quando o pedido ou briefing determinar isso.

### Regra de Reels do Instagram
A Meta informa que os insights do Trial Reel costumam ficar disponíveis aproximadamente 24 horas após o compartilhamento; isso não significa que o conteúdo se torne público automaticamente nesse momento. Também existe uma opção de compartilhamento automático baseada no desempenho observado durante as primeiras 72 horas. Consulte a orientação oficial atual antes de executar: https://about.fb.com/news/2024/12/trial-reels-try-content-non-followers-first-see-what-perfoms-best/.

A documentação do Postiz descreve os campos `is_trial_reel` e `graduation_strategy` (`MANUAL` ou `SS_PERFORMANCE`), mas a presença desses campos não garante que a conta e a integração conectadas permitam promover manualmente o mesmo Reel após a janela de análise. Consulte: https://postiz.com/codex/instagram.

Regras operacionais:
1. O Postiz documenta suporte a `is_trial_reel=true` e `graduation_strategy=MANUAL` ou `SS_PERFORMANCE`. Antes do primeiro uso na instalação self-hosted, confirmar a versão e os campos aceitos pela integração Instagram conectada.
2. Se disponível e previsto no briefing, publicar o Trial Reel via Postiz com `is_trial_reel=true` e `graduation_strategy=MANUAL` quando a decisão de compartilhar depois for humana.
3. Registrar ID, horário real, status e confirmação retornada pela ferramenta.
4. **Não deixar o Claude aguardando 24 horas nem manter a execução do lote aberta.** Finalizar as demais tarefas e registrar a revisão posterior.
5. Aproximadamente 24 horas depois, consultar as métricas. Se a decisão for compartilhar com seguidores, usar no Instagram a ação nativa **Compartilhar com todos / Share with everyone** no mesmo Trial Reel. Isso mantém a mesma publicação; não criar uma cópia.
6. Não publicar o mesmo vídeo como Reel normal no dia seguinte para depois apagar uma publicação. Isso divide os históricos e não transfere engajamento.
7. `SS_PERFORMANCE` é graduação automática decidida pelo Instagram, não um agendamento manual para exatamente 24 horas.
8. Se a integração não suportar Trial Reel, marcar `PENDENTE DE RECURSO TRIAL REEL` e não duplicar. Continuar os demais itens aptos.

Facebook e Threads podem ser agendados/publicados normalmente após revisão, conforme o calendário. Não aplicar a regra de Trial a esses canais.
## 8. Caminho para o WhatsApp e atribuição

- Use o link oficial de WhatsApp/site já configurado pela marca. Confira o endereço no site/CRM atual. Não invente telefone, URL ou destino.
- A CTA deve indicar claramente o próximo passo: consultar o link da bio/site e iniciar conversa pelo WhatsApp.
- Quando o link oficial permitir texto pré-preenchido, use o ID do conteúdo no texto, por exemplo: `Vim do conteúdo SG-XXX no Instagram e quero saber mais.`
- Não presumir que o CRM já armazena automaticamente essa origem. Verifique se o identificador aparece na conversa e se há campo/registro de origem existente.
- Não crie campos, tabelas, workflows, UTMs ou integrações novas sem autorização do João. Se não houver atribuição técnica, marque como `ORIGEM NÃO CONFIRMADA` e não invente conversões.
- O Postiz é ferramenta de publicação/agendamento, não presumir captura de DMs ou comentários. Priorizar o caminho oficial para o WhatsApp.
- Proteger dados pessoais: nunca expor prints, nomes, telefone, pedido ou conversa de cliente sem autorização.

## 9. Organização do Google Drive e repositório

Use as pastas existentes. Não mudar a estrutura sem autorização.

Conteúdo:
- `01 - VÍDEOS BRUTOS/`: originais de João; não editar por cima.
- `02 - EM EDIÇÃO/`: projetos e versões de trabalho.
- `03 - APROVADOS/`: exports finais verificados.
- `04 - PUBLICADOS/`: cópias finais e registro de material publicado.
- `05 - REFERÊNCIAS/`: referências autorizadas/licenciadas e a prancha visual do lote enviada por João.

Artes:
- `Meu Drive/02 - SUA GRÁFICA BH/06 - ARTES/01 - CARROSSÉIS/`
- `.../02 - POSTS ESTÁTICOS/`
- `.../03 - STORIES/`
- `.../04 - CAPAS E THUMBNAILS/`
- `.../05 - ARTES APROVADAS/`
- `.../06 - ARTES PUBLICADAS/`

Use os IDs `SG-XXX` em nomes de arquivos e subpastas. Organize por campanha/data quando ajudar a localizar. Salve os projetos-fonte necessários à edição. Mantenha a referência/licença de cada asset externo. A prancha visual do ChatGPT deve permanecer em `CONTEÚDOS/05 - REFERÊNCIAS/`; não misture esse arquivo com as artes finais.

Atualize o repositório `ABauerlab/conteudosuagraficabh` quando tiver permissão de escrita:
- status de cada item em `CALENDARIO.md`;
- referência nova em `REFERENCIAS.md`;
- roteiro/briefing individual em `conteudos/`;
- dados e aprendizados pós-publicação em `ANALISE-DE-DESEMPENHO.md` e no arquivo individual.
Não duplicar conteúdos nem sobrescrever mudanças sem verificar a versão atual.
## 10. Controle de qualidade obrigatório

Antes de qualquer publicação, confirmar:
- briefing e arquivo correspondem ao mesmo ID;
- produto, serviço e informações comerciais estão corretos e ativos no catálogo;
- direitos/licenças de todos os assets estão resolvidos;
- vídeo/arte está completo e no formato correto;
- arquivo final foi aberto e reproduzido; áudio, imagem, cortes e legendas conferidos;
- texto revisado em português do Brasil;
- CTA e destino corretos;
- identidade visual respeitada;
- post não existe já publicado/agendado;
- legenda específica do canal e dentro dos limites vigentes;
- etapa de Trial Reel configurada corretamente quando for Reel Instagram.

Se um item falhar, pausar apenas aquele item e continuar os demais que estejam aptos. Não pedir aprovação individual para item que passou por todas as verificações, pois este comando autoriza o lote. Dúvida de direitos, catálogo, dados comerciais, perfil de publicação ou falha não solucionável impede apenas aquele item.

## 11. O que significa concluir

Só marcar como criado, salvo, aprovado, agendado, Trial publicado, graduado ou publicado quando a ferramenta correspondente confirmar.

No relatório final, entregar:
1. Quantidade de conteúdos encontrados, produzidos, editados, agendados e publicados.
2. Lista por ID com tipo de peça, arquivos reais salvos e caminhos no Drive.
3. Links/IDs de publicação retornados pelo Postiz.
4. Status de Trial Reel e horário das etapas, sem simular o prazo.
5. Itens pendentes e motivo específico.
6. Métricas iniciais disponíveis e próxima data de revisão, quando houver.
7. Confirmação de que os brutos foram preservados e de que a prancha visual do lote foi localizada (ou estava ausente).

Se houver falha em integração, informar claramente e sugerir somente o passo manual mínimo. Não criar infraestrutura nova e não afirmar sucesso sem evidência.

**Execute agora o pedido e o lote atual. Use sua autonomia para tomar decisões criativas e operacionais dentro dessas regras.**


## Comando curto reutilizável

Após o João colocar os vídeos brutos e a prancha visual do lote nas pastas indicadas, use este comando para iniciar a execução:

> Claude, execute exclusivamente o lote de conteúdos **[INFORMAR IDs SG DO LOTE]** registrado no repositório `ABauerlab/conteudosuagraficabh`. Sincronize o repositório com segurança, leia integralmente `AGENTS.md`, `CLAUDE.md` e `PROMPT-UNICO-CLAUDE.md`, e consulte os briefings individuais desses IDs. Confira no Drive a prancha visual do lote em `CONTEÚDOS/05 - REFERÊNCIAS/`, o Brand Kit em `IDENTIDADE VISUAL/` e os brutos em `CONTEÚDOS/01 - VÍDEOS BRUTOS/`. Produza todas as artes finais (cada slide em arquivo separado), edite os vídeos com correspondência inequívoca por ID, revise, organize e agende pelo Postiz conforme calendário e instruções de cada conteúdo. Consulte o catálogo oficial antes de qualquer afirmação comercial. Preserve estratégia, copy e roteiros já registrados quando completos e aprovados; corrija lacunas reais identificadas pelos gates permanentes antes da produção. Não invente dados, não sobrescreva brutos, não publique duplicatas e não declare ações sem confirmação. Continue com os itens aptos mesmo que algum esteja pendente. Ao final, informe IDs, arquivos e caminhos reais, agendamentos confirmados, links/IDs de publicação e pendências.


## Regra obrigatória de CTA falado em vídeos

Antes de editar cada vídeo, verifique se o briefing inclui uma chamada para ação adequada ao objetivo. Em todo vídeo com apresentador ou narração, a última fala do teleprompter deve conter o CTA exato. CTA apenas na legenda ou na tela não atende ao requisito.

Preserve integralmente a fala final na edição, com áudio claro e tempo suficiente para compreensão. O elemento visual pode reforçar a mesma ação, nunca substituir a fala. Se o bruto não tiver a fala final prevista, registre o conteúdo como pendente de gravação complementar e não invente uma fala nem use voz sintética para simular João.

Escolha uma ação principal por vídeo: seguir o perfil, comentar, salvar, compartilhar ou solicitar orçamento. Para perfil novo, priorize CTA de seguir quando fizer sentido. Para conteúdo comercial, use orçamento/WhatsApp apenas quando a intenção comercial e o destino oficial estiverem confirmados. Evite repetir mecanicamente o mesmo CTA em todos os vídeos.


## Verificação da qualidade dos briefings antes da produção
Antes de iniciar, abra cada arquivo SG e valide se ele contém instruções específicas suficientes para Claude executar. Um título e uma frase de copy não constituem briefing. Se faltarem teleprompter, cenas, edição, textos na tela e assets para Reel; textos e direção slide a slide para carrossel; copy e layout para post estático; ou texto e composição para Story, sinalize “BRIEFING INCOMPLETO” e não improvise a criação editorial. A prancha visual complementa, mas nunca substitui o briefing escrito.



## 12. Regra de escopo por etapa e direção audiovisual obrigatória

**Escopo:** executar somente os IDs e a etapa expressamente solicitados por João no comando atual. Se o lote estiver dividido em Etapa 1 e Etapa 2, não iniciar, editar, exportar, agendar ou distribuir a Etapa 2 antes de João enviar o comando de continuidade. A existência de briefings ou arquivos no repositório não é autorização para executar todas as etapas. Antes de agir, identificar os IDs autorizados e o limite da etapa.

**Padrão dos Reels:** seguir integralmente a seção de direção audiovisual obrigatória em PADROES-DE-EDICAO.md. Vídeo bruto com legenda sobreposta não é edição final. Criar motion graphics e progressão visual por blocos de fala, com tipografia cinética, elementos animados, imagens/vídeos de apoio, composições, máscaras, tracking, split screen/PIP e zooms pontuais motivados pela narrativa. Variar a linguagem de cada Reel e estudar obrigatoriamente as referências de motion na pasta do Drive CONTEÚDOS/05 - REFERÊNCIAS/VÍDEOS/.

**Trilha:** usar música de fundo quando houver faixa cuja licença comercial e permissão para redes sociais/canais previstos tenham sido verificadas. Registrar fonte e licença. Não presumir que música gratuita ou em alta é liberada. Se não houver faixa licenciada confirmada, não usar e registrar a razão.

**Legendas:** Montserrat; uma única linha por vez; blocos curtos; tamanho moderado e discreto; dentro das margens seguras; sem cobrir rosto, produto ou elementos importantes; sincronização conferida ouvindo o vídeo completo. Não usar duas linhas nem substituir Montserrat por Segoe UI.

**Capas:** cada Reel exige capa gráfica original, criada como arte independente com a identidade oficial. Não usar frame ou foto extraída do vídeo como capa. Entregar arquivo próprio, legível em miniatura e revisado no recorte do grid.

**Não aprovar por quantidade:** não marcar como concluído só porque renderizou ou agendou. Aplicar todos os critérios de aceite em PADROES-DE-EDICAO.md. Se o vídeo estiver cru, com motion insuficiente, legenda fora do padrão ou capa baseada em frame, manter EM REVISÃO e corrigir antes de distribuir.


## Distribuição multicanal e hashtags obrigatórias para Feed e Reels

Para cada publicação de **Feed ou Reel**, distribuir em todas as redes sociais conectadas e autorizadas da SUA GRÁFICA BH, conforme o calendário e as capacidades reais do Postiz. Não limitar a publicação ao Instagram quando Facebook, Threads ou outros canais previstos estiverem conectados. Adaptar texto, CTA, formato e link ao contexto de cada rede; não copiar cegamente a mesma legenda quando o canal exigir adaptação. Confirmar cada destino e cada agendamento no Postiz. Se um canal não aceitar o formato, registrar a limitação e não declarar distribuição nele.

**Hashtags:** toda legenda de Feed e Reel deve conter de 3 a 5 hashtags, nunca mais de 5. Selecionar hashtags relevantes ao assunto, público, produto confirmado e intenção de busca/descoberta. Priorizar hashtags com alcance e uso atuais comprováveis, mas combinar:
- 1 ou 2 hashtags amplas do segmento, se ainda forem pertinentes;
- 1 ou 2 hashtags específicas do tema/produto/necessidade;
- 1 hashtag de marca ou campanha quando fizer sentido.

Antes de escolher, pesquisar sinais atuais de relevância e uso nas próprias plataformas ou fontes públicas confiáveis. Não afirmar que uma hashtag é “a de maior alcance” sem métrica verificável. Evitar hashtags genéricas, irrelevantes, repetidas mecanicamente em todas as publicações, banidas ou que possam atrair público desalinhado. Usar no máximo cinco hashtags no total por publicação e adaptar a seleção por canal e conteúdo. Não inventar volume de alcance nem prometer viralização: o objetivo é aumentar descoberta qualificada e potencial de compartilhamento, não garantir viralidade.

Stories não precisam receber hashtags automaticamente; seguir o briefing e priorizar interação e CTA.

Antes de agendar, verificar se a legenda final de cada Feed/Reel contém as hashtags selecionadas e se estão incluídas no texto efetivamente enviado ao Postiz. Não deixar hashtags apenas no arquivo de briefing ou no controle.


## Padrão mestre de qualidade obrigatório
Antes da execução, consulte `PADRAO-MESTRE-CONTEUDO-PROFISSIONAL.md` e aplique todos os requisitos pertinentes ao formato. Atenção especial à proteção integral do rosto do apresentador em todos os frames, direção cinematográfica, montagem narrativa, motion design sincronizado, tratamento de imagem e áudio, legendas Montserrat em uma linha, capas gráficas independentes, pacote completo de publicação multicanal, 3 a 5 hashtags em Feed/Reels, confirmação no Postiz e análise pós-publicação. O checklist do documento é critério de aceite, não sugestão. Não aprovar vídeo com rosto cortado/encoberto, edição apenas com legenda, capa baseada em frame ou publicação sem confirmação por canal.


## Correção obrigatória: tempo de leitura dos ganchos na tela

Em todos os Reels, dê tempo real para o público ler o gancho textual inicial. Use 3 a 5 segundos como referência, aumentando conforme o tamanho e a complexidade da frase. Não retire o texto antes da leitura completa. Se necessário, divida o gancho em blocos sequenciais, cada um com tempo suficiente, sem alterar sua promessa ou sentido. Não sacrifique legibilidade por animação rápida, fonte pequena ou ritmo acelerado. Revise em velocidade normal e em tela de celular, sem pausar: uma pessoa vendo pela primeira vez precisa conseguir ler e entender o gancho. Se não conseguir, corrija antes de aprovar ou agendar. Aplicar também aos ganchos já produzidos que forem revisados; não reabrir peças aprovadas sem relação com esta correção.

## Correções obrigatórias de direção criativa: motion, trilha e B-roll

Motion design com sentido: antes de editar, faça um mapa visual por trecho: fala exata → ideia → imagem/elemento que representa a ideia → motivo da escolha → duração e movimento. Cada elemento deve ilustrar ou explicar diretamente o que João está falando naquele momento. Não usar quadrados, formas, ícones, painéis ou animações genéricas apenas para preencher espaço. Manter grid, alinhamento, hierarquia, proporção, espaçamento e composição profissional. A linguagem deve ser publicitária/comercial e coerente com a identidade. Se a relação entre fala e imagem não for imediata, refaça a cena.

Trilha musical obrigatória: todo vídeo final deve ter música de fundo adequada à intenção e ao ritmo, mixada abaixo da voz. Não encerrar a edição sem trilha apenas por falta de licença. Use uma biblioteca com licença profissional que cubra uso comercial/de marca, trabalho para cliente, redes sociais e mídia paga quando aplicável. Avalie Artlist Pro/Business/Creator Pro ou equivalente, nunca presumindo que plano Social/pessoal cobre cliente ou anúncios. Não comprar/assinar sem autorização do João. Se a licença ainda não existir, registre BLOQUEIO DE LICENÇA MUSICAL, informe exatamente o acesso necessário e deixe o vídeo pendente de aprovação/distribuição. Registre faixa, autor, URL, fornecedor, plano, titular, canais e uso pago cobertos, data e comprovante. Ducking e mixagem são obrigatórios; voz sempre inteligível. Exceção sem trilha só com autorização expressa para aquele vídeo.

B-roll contextual: antes de buscar stock, defina qual fala será ilustrada, qual objeto/ação deve aparecer, em que ambiente/contexto e por que a imagem ajuda a entender. Pesquise por ação e contexto específicos, inspecione o arquivo real e confirme que ele representa fielmente a fala. Não use fotos genéricas, processos/equipamentos incompatíveis, textos estrangeiros ou marcas de terceiros em destaque. Não sugira que uma foto de banco seja da estrutura/equipe/clientes da gráfica. Se não houver asset adequado, use motion tipográfico/diagrama correto ou mantenha o apresentador em tela. Registre URL, autor, licença e data. Confira direitos adicionais de pessoas reconhecíveis, marcas/logos e obras retratadas, mesmo em bancos com licença comercial ampla.

Revisão obrigatória: assista ao vídeo inteiro em velocidade normal. Em cada trecho, confira se fala, motion, B-roll, trilha e composição contam a mesma história. Motion desalinhado, decorativo, sem hierarquia ou B-roll fora de contexto mantém o vídeo EM REVISÃO. Vídeo sem trilha licenciada permanece pendente, não aprovado nem agendado como final.


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


## 8. Rotina automática de impressões prontas (obrigatória em toda execução)

Verifique a pasta do Drive:

`Meu Drive/02 - SUA GRÁFICA BH/CONTEÚDOS/07 - IMPRESSÕES PRONTAS/`

Cada imagem nova e elegível deve virar **um post estático adicional individual**. Uma foto corresponde a uma publicação. Não agrupar fotos, não criar carrossel com elas e não substituir nenhum conteúdo regular do lote.

Procedimento obrigatório:
1. Listar todos os arquivos da pasta, incluindo subpastas somente se fizerem parte da organização real da entrada; não presumir.
2. Consultar `REGISTRO-IMPRESSOES-PRONTAS.md` antes de produzir.
3. Deduplicar por ID imutável do Drive e SHA-256 dos bytes. Quando disponível, comparar também hash perceptual/visual para detectar cópias renomeadas, redimensionadas ou comprimidas. Se a ferramenta não expuser bytes ou identificador estável, não declarar novidade com base apenas no nome: comparar visualmente e registrar a limitação.
4. Ignorar imagens já registradas, inclusive itens já produzidos, agendados, publicados, pendentes ou rejeitados. Só reabrir item pendente quando houver mudança concreta no arquivo, no acesso, na autorização ou na instrução do responsável.
5. Para cada nova foto elegível, alocar o próximo ID SG global livre, criar briefing individual em `FEED/SG-XXX.md` no lote vigente e incluir no calendário como **POST ESTÁTICO ADICIONAL — IMPRESSÕES PRONTAS**. Consultar a sequência real do calendário e do repositório; não reutilizar IDs. Se o lote vigente já estiver encerrado, incluir no próximo lote aberto/futuro, sem inserir datas retroativas.
6. Criar uma peça estática por foto. A foto do produto real é o elemento central; não alterar a arte impressa, não inventar acabamento, material, cliente, depoimento, resultado ou condição comercial. Não criar mockup que substitua a fotografia original.
7. Antes de publicar, conferir se a imagem contém dados pessoais, informações confidenciais, marca de cliente ou conteúdo cujo uso público dependa de autorização. Se a autorização não estiver coberta, registrar PENDENTE DE AUTORIZAÇÃO e não publicar.
8. Consultar o CRM para confirmar qualquer nome de produto, especificação, material, acabamento, aplicação, prazo ou disponibilidade mencionado. A imagem não é fonte suficiente para afirmação comercial.
9. Preparar legenda e CTA originais, com contexto verdadeiro e sem repetir a mesma copy em posts de fotos diferentes. Adaptar por canal.
10. Não mover, renomear, apagar, recortar de forma destrutiva ou modificar o original na pasta de entrada. Salvar derivados e artes finais nas pastas de produção/aprovados.
11. Registrar no ledger: ID SG, nome original, Drive file ID quando houver, SHA-256, fingerprint visual quando houver, data da primeira detecção, lote, status, destino dos arquivos, data planejada e confirmação Postiz. Atualizar o ledger em cada mudança de estado.
12. Se a pasta estiver vazia ou só contiver imagens já registradas, não criar post estático adicional e declarar no relatório: “nenhuma imagem nova elegível encontrada”.

Os posts adicionais entram na agenda como itens independentes e não alteram a cadência regular de Reels, carrosséis e Stories. Escolher datas futuras com espaço no calendário; não inventar horários e não agendar duas vezes.

## 9. Motion programático: código-fonte JavaScript/TypeScript obrigatório
Quando criar motion por código, construir as cenas e animações em JavaScript/TypeScript, preferencialmente React + Remotion, seguindo `PADROES-DE-EDICAO.md`. Entregar projeto editável, componentes, composição, configuração e assets necessários junto do vídeo renderizado. O código deve implementar o mapa visual fala → ideia → elemento → movimento → duração. FFmpeg pode finalizar vídeo e áudio, mas não substitui a fonte JS/TS do motion. Verificar dependências existentes e não instalar serviços/pacotes pagos sem autorização.
