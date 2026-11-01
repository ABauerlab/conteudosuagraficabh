# Operação de conteúdo | SUA GRÁFICA BH

## Objetivo
Manter uma rotina simples: ChatGPT pesquisa e cria roteiros, João grava e envia os brutos ao Drive, Claude edita e distribui os materiais finalizados pelo Postiz.

Não criar etapas, serviços ou ferramentas adicionais quando as integrações já disponíveis no ambiente do Claude forem suficientes.

## Papéis
- **ChatGPT:** pesquisa, estratégia editorial, roteiros, briefings e organização do repositório.
- **João:** grava os roteiros e envia os vídeos para a pasta de brutos. Quando solicitar o processamento em lote, autoriza a edição e a publicação dos conteúdos que passarem no controle de qualidade.
- **Claude Code:** consulta este repositório, localiza os brutos no Drive, edita, revisa, exporta e distribui pelo Postiz.
- **Google Drive:** armazenamento dos arquivos.
- **Postiz:** distribuição orgânica nos canais configurados: Instagram, Facebook e Threads.

## Pastas do Drive
Raiz: `Meu Drive/02 - SUA GRÁFICA BH/CONTEÚDOS/`
1. `01 - VÍDEOS BRUTOS/` — gravações originais de João.
2. `02 - EM EDIÇÃO/` — projetos e versões de trabalho.
3. `03 - APROVADOS/` — exports finais revisados.
4. `04 - PUBLICADOS/` — arquivos finais e materiais publicados.
5. `05 - REFERÊNCIAS/` — referências e assets autorizados/licenciados.

Não apagar nem sobrescrever brutos. Não alterar a estrutura de pastas sem autorização.

## Fluxo de trabalho
1. Pesquisar oportunidades e criar roteiros.
2. Criar um arquivo individual `conteudos/SG-XXX-titulo-curto.md` usando `templates/ROTEIRO.md`; atualizar `CALENDARIO.md`.
3. João grava cada roteiro e identifica o arquivo com o mesmo ID: `SG-XXX - TÍTULO DO VÍDEO.mp4`.
4. João envia os arquivos para `01 - VÍDEOS BRUTOS/`.
5. João envia ao Claude um único comando para processar os vídeos da pasta.
6. Claude cruza os arquivos com os roteiros, edita todos os itens com correspondência clara e salva os exports finais em `03 - APROVADOS/`.
7. Claude reproduz e confere cada export, verifica legenda e CTA e distribui os conteúdos aptos pelo Postiz para Instagram, Facebook e Threads.
8. Claude registra o resultado no calendário e nos arquivos individuais, quando tiver acesso de escrita.
9. Os resultados disponíveis são registrados para orientar os próximos conteúdos.

## Comando padrão para Claude
“Claude, processe todos os vídeos disponíveis em `Meu Drive/02 - SUA GRÁFICA BH/CONTEÚDOS/01 - VÍDEOS BRUTOS/`. Consulte o repositório `ABauerlab/conteudosuagraficabh`, encontre o roteiro de cada vídeo pelo ID e siga integralmente as instruções, briefings e padrões de edição. Edite todos os vídeos que tiverem correspondência clara, revise e reproduza cada export para garantir a qualidade. Salve os arquivos finais em `03 - APROVADOS/`. Depois de conferir legenda, CTA e adequação por canal, distribua os conteúdos aprovados pelo Postiz nos canais conectados: Instagram, Facebook e Threads. Não publique duplicatas. Preserve todos os brutos. Registre o que foi editado, agendado ou publicado e informe pendências e falhas. Não invente informações nem declare ações que não foram confirmadas.”

## Regras para processamento em lote
- Usar `SG-XXX` como identificador principal.
- Antes de editar, listar os arquivos encontrados e identificar brutos sem roteiro, roteiros sem bruto e nomes ambíguos.
- Não interromper todo o lote por causa de um único arquivo com problema; processar os demais que estiverem aptos.
- Não inventar correspondências, falas, cenas, depoimentos ou dados comerciais.
- Não apagar ou sobrescrever os arquivos originais.
- Não publicar material que falhar na revisão.
- Verificar histórico do Postiz para evitar duplicidade.
- Se o Postiz falhar em um canal, registrar a falha e não afirmar que houve publicação naquele canal.

## Controle de qualidade
- Fala fiel à gravação e ao roteiro.
- Gancho claro e ritmo natural.
- Legendas corretas, legíveis e dentro da área segura.
- Áudio limpo, sem clipping; música licenciada e abaixo da voz.
- Cortes sem prejudicar o entendimento.
- Identidade visual e assets oficiais respeitados.
- Informações comerciais confirmadas no CRM.
- Direitos e créditos preservados.
- Export reproduzido e conferido antes da distribuição.

## Status
IDEIA → PESQUISA → ROTEIRO PRONTO → PRONTO PARA GRAVAR → GRAVADO → EM EDIÇÃO → FINALIZADO → AGENDADO → PUBLICADO → ANALISADO.

Estados adicionais: PENDENTE DE ROTEIRO, PENDENTE DE REFERÊNCIA, PENDENTE DE DIREITOS, PENDENTE DE CATÁLOGO, ERRO DE EDIÇÃO e ERRO DE PUBLICAÇÃO.
