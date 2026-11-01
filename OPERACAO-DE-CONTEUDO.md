# Operação de conteúdo | SUA GRÁFICA BH

## Objetivo
Manter uma rotina simples: ChatGPT pesquisa, planeja e entrega lotes multimodais com roteiros, artes e direção visual; João grava os vídeos e coloca os brutos e a prancha visual no Drive; Claude produz as artes finais, edita os vídeos, revisa e agenda/distribui os materiais aptos pelo Postiz.

Não criar etapas, serviços ou ferramentas adicionais quando as integrações já disponíveis no ambiente do Claude forem suficientes.

## Papéis
- **ChatGPT:** pesquisa, estratégia editorial, roteiros, copy, briefings de todas as peças, prancha visual e organização do repositório.
- **João:** grava os roteiros e envia os vídeos para a pasta de brutos. Quando solicitar o processamento em lote, autoriza a edição e a publicação dos conteúdos que passarem no controle de qualidade.
- **Claude Code:** consulta este repositório, o CRM e o Brand Kit; localiza os brutos e a prancha visual no Drive; produz artes finais, edita, revisa e agenda/distribui pelo Postiz.
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
8. **Produção:** Claude cria as artes finais, carrosséis slide a slide, Stories e capas previstas; edita os vídeos com bruto correspondente. Não refaz pesquisa, estratégia, copy ou roteiro já concluídos.
9. **Revisão:** Claude abre e confere cada arte/slide e reproduz cada vídeo, verificando textos, áudio, imagem, formato, catálogo, direitos e identidade visual.
10. **Distribuição:** Claude agenda/publica os materiais aptos via Postiz conforme calendário e canais efetivamente conectados. Legendas, CTA e formato devem ser adaptados por canal.
11. **Registro:** Claude registra status, data, canal, links/IDs e pendências no calendário e nos arquivos individuais, quando tiver acesso de escrita.

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
O comando reutilizável oficial está em `PROMPT-UNICO-CLAUDE.md`. João deve informar os IDs SG exatos do lote. Claude executa apenas esses briefings, produz artes finais, edita vídeos com bruto correspondente, revisa, organiza e agenda/distribui conforme os calendários e canais conectados. Não refaz pesquisa, estratégia, copy ou roteiro. Para Trial Reels, nunca manter a execução aberta aguardando 24 horas; registrar o status e tratar a avaliação/graduação como etapa posterior, somente se o recurso estiver confirmado.

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
