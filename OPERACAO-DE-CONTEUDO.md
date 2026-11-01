# Operação de conteúdo | SUA GRÁFICA BH

## Objetivo
Manter uma rotina simples: ChatGPT pesquisa e cria roteiros, João grava e envia os brutos ao Drive, Claude edita e distribui os materiais finalizados pelo Postiz.

Não criar etapas, serviços ou ferramentas adicionais quando as integrações já disponíveis no ambiente do Claude forem suficientes.

## Papéis
- **ChatGPT:** pesquisa, estratégia editorial, roteiros, briefings e organização do repositório.
- **João:** grava os roteiros e envia os vídeos para a pasta de brutos. Quando solicitar o processamento em lote, autoriza a edição e a publicação dos conteúdos que passarem no controle de qualidade.
- **Claude Code:** consulta este repositório, localiza os brutos no Drive, edita, revisa e distribui pelo Postiz.
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
- Adaptar o conceito à identidade visual oficial da SUA GRÁFICA BH, criando peças originais. Não copiar a arte, o texto, o layout exato ou a identidade de terceiros.
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
1. Pesquisar oportunidades, tendências e referências brasileiras.
2. Confirmar no catálogo do CRM/Supabase que cada produto ou serviço abordado está ativo e disponível.
3. Criar roteiros, briefings e peças com referências documentadas.
4. João grava cada roteiro e identifica o arquivo com o mesmo ID: `SG-XXX - TÍTULO DO VÍDEO.mp4`.
5. João envia os arquivos para `01 - VÍDEOS BRUTOS/`.
6. Claude cruza os arquivos com os roteiros, edita todos os itens com correspondência clara e salva os exports finais em `03 - APROVADOS/`.
7. Claude reproduz e confere cada export, verifica legenda e CTA e distribui os conteúdos aptos pelo Postiz.
8. Claude registra o resultado no calendário e nos arquivos individuais, quando tiver acesso de escrita.

## Regra especial: Reels do Instagram como Trial Reel
Todo vídeo destinado ao Reels do Instagram deve seguir este fluxo:
1. Primeiro, publicar como **Trial Reel (Reel de teste)**, usando o recurso oficial do Instagram, quando essa opção estiver disponível e for compatível com a integração do Postiz.
2. Aguardar 24 horas completas após a publicação de teste.
3. Depois das 24 horas, compartilhar/publicar o mesmo Reel para todos, tornando-o público para a audiência geral, conforme o fluxo oficial disponível.
4. Registrar os horários reais da etapa de teste e da publicação geral.

**Verificação obrigatória:** antes de executar, Claude deve confirmar se o Postiz e a conexão atual com o Instagram permitem criar Trial Reels e depois compartilhar o mesmo Reel com todos. Não confundir agendamento comum ou publicação normal com Trial Reel. Se o recurso não estiver disponível na integração, não publicar o Reel normalmente como substituição e não simular a etapa de teste. Marcar como `PENDENTE DE RECURSO TRIAL REEL`, informar João e manter os demais canais/itens aptos em andamento. Não afirmar que aguardou 24 horas ou publicou para todos sem confirmação real.

## Comando padrão para Claude
“Claude, processe os conteúdos disponíveis conforme os roteiros e briefings deste repositório. Antes de produzir ou publicar qualquer peça que mencione produto, confirme a disponibilidade no catálogo atual do CRM/Supabase. Para Reels do Instagram, siga obrigatoriamente o fluxo Trial Reel, aguarde 24 horas completas e só então compartilhe com todos, desde que o recurso esteja realmente disponível no Postiz/Instagram. Se não estiver, deixe pendente e me informe; não substitua por publicação pública comum. Edite, revise, distribua os itens aptos nos canais conectados, preserve os brutos, evite duplicatas e registre as ações confirmadas. Não invente informações nem declare ações que não foram confirmadas.”

## Regras para processamento em lote
- Usar `SG-XXX` como identificador principal.
- Antes de editar, listar arquivos encontrados e identificar brutos sem roteiro, roteiros sem bruto e nomes ambíguos.
- Não interromper todo o lote por causa de um único arquivo com problema; processar os demais que estiverem aptos.
- Não inventar correspondências, falas, cenas, depoimentos ou dados comerciais.
- Não apagar ou sobrescrever os arquivos originais.
- Não publicar material que falhar na revisão, não tiver produto confirmado no catálogo ou tiver pendência de direitos.
- Verificar histórico do Postiz para evitar duplicidade.
- Se o Postiz falhar em um canal, registrar a falha e não afirmar que houve publicação naquele canal.

## Controle de qualidade
- Fala fiel à gravação e ao roteiro.
- Gancho claro e ritmo natural.
- Legendas corretas, legíveis e dentro da área segura.
- Áudio limpo, sem clipping; música licenciada e abaixo da voz.
- Cortes sem prejudicar o entendimento.
- Identidade visual e assets oficiais respeitados.
- Produtos e informações comerciais confirmados no CRM/Supabase.
- Direitos e licenças dos assets verificados.
- Export reproduzido e conferido antes da distribuição.

## Status
IDEIA → PESQUISA → ROTEIRO PRONTO → PRONTO PARA GRAVAR → GRAVADO → EM EDIÇÃO → FINALIZADO → AGENDADO → PUBLICADO → ANALISADO.

Estados adicionais: PENDENTE DE ROTEIRO, PENDENTE DE REFERÊNCIA, PENDENTE DE DIREITOS, PENDENTE DE CATÁLOGO, PENDENTE DE RECURSO TRIAL REEL, ERRO DE EDIÇÃO e ERRO DE PUBLICAÇÃO.
