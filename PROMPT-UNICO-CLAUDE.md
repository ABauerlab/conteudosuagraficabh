# Comando operacional curto | Claude Code | SUA GRÁFICA BH

Este arquivo é a porta de entrada para executar tarefas. **O comando enviado por João define somente a tarefa, o escopo e os IDs. Todos os requisitos de pesquisa, estratégia, conteúdo, identidade, edição, QA, distribuição, segurança e organização estão documentados no repositório e devem ser consultados automaticamente.** Não exigir que João copie novamente essas regras em cada solicitação.

## Comandos que João pode usar
- `Finalize o lote de 10/11 a 13/11.`
- `Finalize o lote SG-025 a SG-048.`
- `Edite os vídeos SG-025, SG-026 e SG-031.`
- `Produza as artes dos IDs SG-027, SG-033 e SG-039.`
- `Audite e corrija os briefings SG-025 a SG-048.`
- `Crie o próximo lote para gravação, seguindo o calendário.`

## Como interpretar o comando
- **FINALIZAR LOTE:** auditar os IDs, corrigir lacunas justificadas, produzir todos os formatos do escopo, editar, fazer QA, organizar arquivos, distribuir via Postiz e atualizar registros. Executar também a rotina de impressões prontas descrita em `REGISTRO-IMPRESSOES-PRONTAS.md`.
- **EDITAR VÍDEOS/ARTES:** trabalhar somente nos IDs e formatos informados, seguindo os briefings e padrões. Não criar conteúdos novos nem alterar outros IDs. Não distribuir/publicar, salvo se João também solicitar finalização ou distribuição.
- **AUDITAR/CORRIGIR:** revisar somente o escopo indicado; corrigir falhas reais dentro da autorização, sem reescrever materiais aprovados por preferência.
- **CRIAR/PLANEJAR LOTE:** pesquisar dores reais, estratégia, catálogo, tendências e histórico; criar briefings completos e individuais, sem executar gravação ou publicação não solicitada.
- **DISTRIBUIR:** executar somente a distribuição dos conteúdos aprovados e indicados, após conferir Postiz, canais e duplicidade.

Se o período for informado sem IDs, consultar `CALENDARIO.md` e o README do lote para determinar o escopo. Se os IDs forem informados, eles delimitam o trabalho. Nunca presumir IDs, datas, horários, formatos ou autorização ausentes.

## Protocolo obrigatório antes de agir
1. Conferir `git status`, branch, alterações locais e estado remoto. Atualizar a referência de `main` com segurança; preservar trabalho existente e nunca sobrescrever alterações locais.
2. Ler integralmente `AGENTS.md`, `CLAUDE.md`, `DIRETRIZES.md`, `ESTRATEGIA.md` e `AUDITORIA-DE-PROCESSO-E-GATES.md`.
3. Ler os documentos especializados aplicáveis:
   - Criação: `DORES-REAIS-CLIENTES.md`, `VARIEDADE-EDITORIAL.md`, `MATRIZ-DE-AQUISICAO.md`, pesquisas estratégicas/tendências e `PLATAFORMAS-E-CARROSSEIS-2026-11.md`.
   - Vídeo/áudio: `PRODUCAO-DE-VIDEOS.md`, `PADROES-DE-EDICAO.md` e `PADRAO-MESTRE-CONTEUDO-PROFISSIONAL.md`.
   - Artes: `SISTEMA-DE-PRODUCAO-VISUAL.md` e os ativos oficiais do Brand Kit.
   - Operação: `OPERACAO-DE-CONTEUDO.md`, `CALENDARIO.md`, `REFERENCIAS.md`, `ANALISE-DE-DESEMPENHO.md` e `REGISTRO-IMPRESSOES-PRONTAS.md`, quando pertinentes.
4. Ler o README do lote e todos os briefings individuais SG do escopo. Consultar o histórico editorial necessário para evitar repetição.
5. Consultar o CRM oficial e o catálogo atual sempre que a tarefa envolver marca, produto, disponibilidade, características, preços, prazos, acabamentos ou condições.
6. Consultar e inspecionar os arquivos reais do Brand Kit oficial antes de criar peças com identidade. Nunca recriar ou aproximar ativos oficiais.

## Regras de execução
- O repositório é o manual operacional. Não pedir que João repita regras já documentadas.
- Pesquisar e criar a partir de dores reais: economia e desperdício, escolha de papel, gramatura, sangria, margem de segurança, resolução, cor, fosco versus brilho, acabamentos, aplicações por segmento, preparação de arquivos e decisões de compra. São exemplos de territórios, não pautas automáticas. Consultar `DORES-REAIS-CLIENTES.md` e validar afirmações técnicas em fontes confiáveis e no CRM quando aplicável.
- Nenhuma pauta pode ser aprovada só por trocar palavras, título, gancho ou formato. Comparar semanticamente com o histórico.
- Não inventar fatos, produtos, especificações, preços, prazos, benefícios, resultados, depoimentos, arquivos, licenças ou status.
- Preservar os originais e os IDs globais. Não sobrescrever brutos nem reutilizar IDs.
- Motion programático exige projeto-fonte editável em JavaScript/TypeScript, preferencialmente React + Remotion; FFmpeg não substitui a fonte de motion.
- Preservar o áudio original. Não executar transcrição nem processamento/melhoria de áudio. Não instalar ou baixar ferramentas para isso. Fazer cortes visuais e de ritmo sem alterar a fala.

- Música: seguir a estratégia gratuita Pixabay documentada; nunca contratar ou comprar sem autorização.
- Produzir, revisar e organizar todos os formatos incluídos no escopo. Distribuição só ocorre quando o comando pede finalização/distribuição e o conteúdo passou pelos gates.
- Em finalização de lote, aplicar Postiz a todos os formatos e destinos conectados, autorizados e compatíveis, confirmar individualmente e registrar falhas sem declarar sucesso.
- Não interromper o lote por falha isolada. Continuar os itens aptos e agrupar bloqueios indispensáveis.
- Fazer PR para `main`; não editar `main` diretamente. Revisar diff, validar arquivos e não declarar merge sem confirmação.

## Critério de encerramento
Relatar objetivamente: IDs auditados; correções; arquivos e caminhos reais; QA realizado; distribuição confirmada por canal quando solicitada; pendências por ID; alterações no repositório; branch, commit e PR. Distinguir produzido, revisado, aprovado, enviado, agendado e publicado.

**Regra central:** João envia um comando curto. Claude consulta o repositório, entende o escopo e executa todos os requisitos permanentes aplicáveis sem exigir um prompt extenso.


## Execução resiliente obrigatória
Antes de iniciar edição ou distribuição, ler EXECUCAO-RESILIENTE-MIDIA-POSTIZ.md. O fluxo normal é Drive MCP → edição/arte/QA → Postiz MCP conectado. Não pedir que João abra navegador ou faça login; não tornar arquivos públicos; não depender de postMessage, GitHub raw ou endpoints internos improvisados. Descobrir as ferramentas MCP disponíveis e usar as ações de upload/agendamento do Postiz. Se uma etapa falhar, seguir a árvore de alternativas documentada, salvar checkpoint e continuar os demais IDs. Falha de consulta da fila não equivale automaticamente a falha de publicação; distinguir listagem, autenticação, upload e agendamento. Não executar transcrição nem processamento de áudio. O áudio original permanece como gravado; não instalar ferramentas ou baixar modelos para essas tarefas.

## Prioridade de produção rápida
A finalização deve ser rápida e profissional, sem etapas técnicas desnecessárias. Reutilizar templates e componentes existentes; fazer cortes objetivos, ritmo, textos visuais e motion simples que agregue valor. Não criar pipeline novo nem animações complexas por obrigação. Não transcrever, gerar legendas automáticas, usar Whisper ou processar/melhorar áudio. Preservar a faixa original. Usar o roteiro fornecido somente quando corresponder claramente à fala; se houver dúvida, omitir a legenda. Não instalar ferramentas nem baixar modelos para áudio. Fazer QA objetivo e corrigir apenas problemas reais antes de enviar ao Postiz.
