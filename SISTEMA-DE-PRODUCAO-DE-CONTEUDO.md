# Sistema de produção de conteúdo | SUA GRÁFICA BH

**Critérios obrigatórios de ponta a ponta:** consultar `AUDITORIA-DE-PROCESSO-E-GATES.md` para pesquisa, estratégia, roteiro, briefing, edição, QA, distribuição e mensuração. Em conflito, aplicar a hierarquia de `AGENTS.md`.

## Objetivo
Criar conteúdo que atraia empreendedores e potenciais clientes para a SUA GRÁFICA BH. O processo deve ser simples para João: receber um lote completo de conteúdos, gravar apenas os vídeos previstos, salvar a prancha visual no Drive e enviar os brutos. Claude fica responsável pela produção das artes finais, edição dos vídeos, revisão e agendamento/distribuição dos materiais aptos.

## Fontes oficiais e responsabilidades
- **CRM oficial** (`ABauerlab/crm-sua-grafica-bh`): fonte de verdade para identidade visual, catálogo ativo, especificações e informações comerciais.
- **Este repositório**: fonte de verdade para estratégia editorial, pesquisa, pautas, roteiros, referências, briefings, padrões de edição e aprendizados.
- **Google Drive**: armazenamento dos arquivos brutos, projetos de edição, exports finais e referências.
- **ChatGPT:** pesquisa, estratégia, pautas, roteiros, copy, briefings, prancha visual e auditoria/correção quando solicitado.
- **João:** define escopo, grava e envia os brutos e decide autorizações/questões comerciais que dependam dele.
- **Claude Code:** pesquisa e audita lacunas quando necessário; preserva briefings completos e corrige os incompletos dentro do escopo; produz artes, edita vídeos, revisa e distribui pelo Postiz.
- **Postiz:** publicação orgânica nos canais conectados da marca: Instagram, Facebook e Threads.

Não adicionar n8n, banco de dados, servidores de renderização ou outros serviços ao fluxo enquanto as integrações já disponíveis no Claude forem suficientes.

## Fluxo operacional
1. **Pesquisa e estratégia:** pesquisar oportunidades, dores, tendências e referências; definir o mix de vídeos, carrosséis, posts estáticos e Stories conforme o objetivo.
2. **Planejamento:** escrever roteiros, copy, estrutura slide a slide, CTAs, legendas e briefings de produção.
3. **Direção visual:** ChatGPT gera uma prancha visual de referência para o lote que inclua artes. João salva a imagem em `Meu Drive/02 - SUA GRÁFICA BH/CONTEÚDOS/05 - REFERÊNCIAS/`, com os IDs no nome do arquivo.
4. **Registro:** atribuir ID sequencial `SG-XXX`, criar um arquivo individual por conteúdo em `conteudos/` e atualizar `CALENDARIO.md`.
5. **Gravação:** João grava somente os conteúdos que exigem vídeo e usa o ID no nome de cada arquivo.
6. **Upload:** João envia os brutos para `Meu Drive/02 - SUA GRÁFICA BH/CONTEÚDOS/01 - VÍDEOS BRUTOS/`.
7. **Comando ao Claude:** João envia o comando único com os IDs exatos do lote.
8. **Produção:** Claude consulta cada briefing, confere a prancha visual e o Brand Kit, produz as artes finais e edita os vídeos cuja correspondência por ID seja clara.
9. **Revisão:** Claude abre cada arte e cada slide; reproduz cada vídeo; confere qualidade, textos, identidade, catálogo, direitos e adequação aos canais.
10. **Distribuição:** os materiais aptos são agendados/distribuídos pelo Postiz conforme calendário e canais que estiverem efetivamente conectados. Adaptar legenda, CTA e formato por canal.
11. **Registro:** Claude registra status, data, canal, links/IDs e pendências no calendário e no arquivo individual, quando tiver acesso.
12. **Aprendizado:** resultados disponíveis orientam os próximos temas, ganchos, formatos e prioridades.

## Pesquisa e integridade
- Separar evidência, interpretação e hipótese.
- Concorrentes são referências de mercado, nunca fonte oficial sobre produtos ou condições da SUA GRÁFICA BH.
- Não inventar fontes, links, autores, datas ou métricas.
- Encontrar a origem de um vídeo não significa ter autorização para reutilização comercial.
- Respeitar licenças, autorizações, créditos e identificadores de terceiros.

## Regras para roteiros
- Entregar o texto falado isolado, pronto para teleprompter.
- Não misturar falas com indicações de cena, pausas ou notas técnicas.
- Usar linguagem brasileira, natural e conversada.
- Criar gancho imediato, preferencialmente nos primeiros 1–2 segundos.
- Variar temas, ângulos, formatos e objetivos.
- Não forçar venda em toda pauta.
- Confirmar no CRM qualquer produto, preço, prazo, especificação, disponibilidade ou condição comercial citada.
- Não prometer viralização, vendas ou resultados garantidos.

## Formato de entrega do ChatGPT
Para cada conteúdo, entregar briefing individual com ID, formato, objetivo, público, etapa do funil, hipótese, conceito, gancho, conteúdo final, CTA, legendas por canal, fontes e instrução de execução.

- **Vídeo:** incluir roteiro e teleprompter isolado (somente falas), ficha de gravação e briefing de edição.
- **Carrossel:** incluir copy completa de cada slide, função narrativa e direção visual por página.
- **Post estático:** incluir texto final, hierarquia e direção de arte.
- **Stories:** incluir sequência, texto, CTA e direção visual.
- **Prancha visual:** gerar uma por lote que contenha artes, mapear os quadros aos IDs e orientar João a colocá-la na pasta `CONTEÚDOS/05 - REFERÊNCIAS/` do Drive.

## Google Drive
Raiz: `Meu Drive/02 - SUA GRÁFICA BH/CONTEÚDOS/`
- `01 - VÍDEOS BRUTOS/`: gravações originais; nunca apagar ou sobrescrever.
- `02 - EM EDIÇÃO/`: projetos e versões em andamento.
- `03 - APROVADOS/`: exports finais revisados.
- `04 - PUBLICADOS/`: cópias finais e materiais publicados.
- `05 - REFERÊNCIAS/`: referências e assets autorizados/licenciados.

Não renomear, mover ou apagar pastas existentes sem autorização. Se uma integração não permitir determinada ação, informar e usar a alternativa disponível sem alegar sucesso.

## Nomenclatura
Usar o mesmo ID em todas as etapas:
- Roteiro: `conteudos/SG-XXX-titulo-curto.md`
- Bruto: `SG-XXX - TÍTULO DO VÍDEO.mp4`
- Projeto: `SG-XXX - TÍTULO DO VÍDEO`
- Export: `SG-XXX - TÍTULO DO VÍDEO - FINAL.mp4`
- Carrossel: `SG-XXX-SLIDE-01.png`, `SG-XXX-SLIDE-02.png` etc.
- Post estático: `SG-XXX-ARTE-FINAL.png`
- Story: `SG-XXX-STORY-01.png`, `SG-XXX-STORY-02.png` etc.
- Capa/thumbnail: `SG-XXX-CAPA.png`
- Prancha visual do lote: `SG-XXX-SG-YYY-DIRECAO-VISUAL.png` (usar o primeiro e o último ID do lote).

O ID é permanente. Títulos podem mudar sem alterar o ID. Takes adicionais recebem sufixos `-take-02`, `-take-03`.

## Comando padrão e execução em lote
O comando reutilizável oficial está em `PROMPT-UNICO-CLAUDE.md`. João informa os IDs SG exatos do lote depois de colocar os brutos e a prancha visual no Drive.

Claude executa somente os briefings desses IDs: produz carrosséis slide a slide, posts estáticos, Stories e capas; edita vídeos com bruto correspondente; revisa, organiza e agenda/distribui os itens aptos pelo Postiz. O comando autoriza execução sem aprovação individual para cada peça que passar integralmente pelo controle de qualidade.

- Não criar pauta, copy, roteiro ou conteúdo substituto quando o briefing já está completo.
- Não processar conteúdos fora dos IDs informados.
- Não produzir nem publicar material sem briefing, confirmação comercial ou direitos resolvidos.
- Verificar o histórico do Postiz para evitar duplicidade.
- Se uma peça falhar, pausar somente aquele ID e continuar os demais aptos.
- Se o Postiz falhar em um canal, registrar a falha daquele canal. Não declarar publicação concluída sem confirmação.
- Agendar conforme calendário e briefing; não inventar data/horário como se fossem dados comprovados.
- Não aguardar 24 horas com o processo aberto para Trial Reels; registrar status e tratar a avaliação posterior como etapa separada.
## Controle de qualidade
- Briefing, prancha, bruto e arquivos finais correspondem aos mesmos IDs.
- Textos revisados em português do Brasil, com legibilidade em celular.
- Hierarquia, composição, contraste, margens seguras e identidade visual respeitados.
- Cada slide de carrossel é arquivo próprio e foi revisado na ordem correta.
- Cada vídeo foi reproduzido; áudio, cortes, legendas e enquadramento conferidos.
- Informações comerciais confirmadas no CRM.
- Direitos e créditos preservados.
- CTA, legenda e formato adequados a cada canal.
- Exports finais conferidos antes da distribuição.

## Status
IDEIA → PESQUISA → BRIEFING PRONTO → PRONTO PARA GRAVAR / PRONTO PARA PRODUZIR → GRAVADO → EM PRODUÇÃO → PRONTO PARA PUBLICAR → AGENDADO → PUBLICADO → ANALISADO.

Estados adicionais: PRANCHA VISUAL PENDENTE, PENDENTE DE ARQUIVO, PENDENTE DE DIREITOS, PENDENTE DE CATÁLOGO, PENDENTE DE RECURSO TRIAL REEL, ERRO DE PRODUÇÃO e ERRO DE AGENDAMENTO.


## Regra de escopo e economia de execução
O planejamento, pesquisa, copy, roteiros e direção criativa podem ser produzidos pelo ChatGPT ou auditados/corrigidos por Claude conforme a tarefa. Briefing completo e aprovado deve ser preservado; briefing incompleto, repetido, contraditório ou comercialmente não confirmado deve ser corrigido antes da produção, dentro da autorização. Claude executa os IDs informados, produz, revisa e distribui pelo Postiz conforme AGENTS.md. Se faltar arquivo ou autorização essencial, pausa somente o ID afetado.

A prancha visual gerada no ChatGPT precisa ser transferida por João para a pasta sincronizada do Drive indicada neste documento; não presumir que um arquivo desta conversa aparece automaticamente no ambiente do Claude.


## Regra obrigatória de CTA nos vídeos

Todo vídeo com fala de apresentador ou narração precisa ter CTA falado como última fala do roteiro/teleprompter. A chamada também deve aparecer no briefing individual, na legenda e, quando fizer sentido, na tela durante o encerramento. Nunca deixar o CTA somente na legenda ou em lettering.

A ação deve ser escolhida conforme o objetivo:
- Perfil em fase de crescimento/descoberta: seguir o perfil.
- Conteúdo educativo ou de referência: salvar ou compartilhar.
- Conteúdo de conversa/comunidade: comentar ou responder uma pergunta.
- Conteúdo com intenção comercial e produto confirmado: solicitar orçamento pelo canal oficial.

Usar apenas uma ação principal por vídeo, com frase natural, curta e sem tom insistente. Variar os CTAs ao longo do calendário. Não prometer produto, preço ou condição sem confirmação no CRM. Vídeos sem fala podem usar CTA visual, sem forçar narração.
