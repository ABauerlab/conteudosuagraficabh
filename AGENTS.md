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
- Claude deve inspecionar a prancha e as referências visuais originais em `Meu Drive/02 - SUA GRÁFICA BH/IDENTIDADE VISUAL/` antes de criar artes.
- A prancha é direção criativa, nunca arte final. Cada slide de carrossel e cada peça final deve ser exportado em arquivo próprio.
- Execute somente os IDs indicados pelo João; não recrie pesquisa, copy ou roteiros já completos no repositório.


## Regra obrigatória de estrutura dos lotes
Criar subpasta por lote em conteudos/lote-AAAA-MM-DD-a-AAAA-MM-DD/. Um conteúdo = um arquivo individual SG-XXX.md. Nunca agrupar vários IDs em arquivo diário ou por formato. A pasta pode conter README/índice e documentos auxiliares, mas cada briefing permanece individual. IDs globais e sequenciais; conferir calendário antes de criar. Atualizar calendário raiz e índice do lote. Antes de concluir, conferir árvore GitHub, contagem, correspondência ID/arquivo e links diretos. Claude executa arquivos individuais sem reagrupar ou recriar copy/roteiro aprovado. Se houver falha parcial, informar que o lote não está completo.


## Pastas obrigatórias por formato nos próximos lotes
Cada pasta de lote em `conteudos/lote-AAAA-MM-DD-a-AAAA-MM-DD/` deve conter `FEED/`, `STORIES/` e `REELS/`, além de um `README.md` na raiz. Guardar cada `SG-XXX.md` individual diretamente na subpasta do formato: FEED para carrosséis e estáticos, STORIES para cada Story separado e REELS para cada vídeo. Não agrupar briefings, não misturar formatos e não deixar os arquivos individuais soltos na raiz do lote. O índice deve mapear ID, data, formato e status. IDs continuam globais e sequenciais; lote apagado não libera IDs para reutilização.


## Padrão mínimo de qualidade dos briefings individuais
O arquivo SG é a ordem de produção para Claude, não um lembrete curto. Aplicar integralmente a seção “REGRA DE BRIEFING COMPLETO — NÃO ACEITAR RESUMOS” de `CHATGPT.md`. Briefing com apenas título, uma frase ou instrução genérica não está pronto. Exigir teleprompter e direção de edição completos para Reels; roteiro slide a slide e direção de arte para carrosséis; copy e composição para estáticos; texto e layout individual para Stories. Validar todos os campos aplicáveis do `templates/CONTEUDO.md` antes de abrir PR.


## Reinício autorizado da sequência de IDs
João autorizou reiniciar a numeração após apagar a pasta do lote anterior diretamente no repositório. O próximo lote começa em SG-001. Consultar `CALENDARIO.md` como fonte de verdade; não usar SG-049 como próximo ID. Manter um Markdown individual por conteúdo e separar os arquivos em FEED/, STORIES/ e REELS/. Não reiniciar novamente sem autorização.


## Regra obrigatória de variedade editorial (ler VARIEDADE-EDITORIAL.md)
Antes de criar qualquer lote, consultar `VARIEDADE-EDITORIAL.md` e o histórico recente de conteúdos. Não concentrar a comunicação em arte-final, fechamento de arquivo, briefing ou preparação técnica. Esses temas são apenas uma pequena parte do universo editorial. Cada peça precisa ter assunto, promessa, ângulo e entrega próprios; trocar apenas o gancho ou o título não conta como variedade. Planejar pautas a partir de dúvidas, desejos, problemas e situações reais do público, equilibrando conteúdo útil, entretenimento, identificação, tendências atuais, demonstrações e conteúdo comercial. Pesquisar tendências e assuntos atuais com fontes e datas verificáveis. Antes de aprovar o lote, fazer auditoria de repetição temática e de mensagem entre todos os formatos.
