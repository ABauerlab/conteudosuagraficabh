# Operação de conteúdo em escala

## Objetivo
Permitir produção contínua de vídeos com baixa carga operacional para João: ChatGPT pesquisa e roteiriza, João grava e envia ao Drive, Claude localiza o roteiro e edita.

## Papéis
- **João:** aprova pautas quando necessário, grava os roteiros no teleprompter e envia arquivos brutos ao Google Drive.
- **ChatGPT:** pesquisa mercado, identifica oportunidades, seleciona pautas, cria roteiros e briefings e mantém os registros editoriais.
- **Claude Code:** consulta este repositório, encontra os brutos no Drive, edita, exporta e informa a entrega.
- **Google Drive:** armazenamento e passagem dos arquivos entre gravação, edição, aprovação e publicação.
- **Distribuição:** publicação orgânica e uso em campanhas pagas conforme decisão do responsável. Não presumir Postiz ou publicação automática.

## Pasta oficial do Drive
`Meu Drive/02 - SUA GRÁFICA BH/CONTEÚDOS/`

Subpastas:
1. `01 - VÍDEOS BRUTOS/` — arquivos originais gravados por João.
2. `02 - EM EDIÇÃO/` — projetos e versões de trabalho do Claude.
3. `03 - APROVADOS/` — exports finais aprovados.
4. `04 - PUBLICADOS/` — arquivos finais e/ou materiais publicados.
5. `05 - REFERÊNCIAS/` — referências e assets autorizados/licenciados.

Não apagar nem sobrescrever arquivos brutos. Se o conector não permitir movimentar arquivos, manter cópias e informar.

## Fluxo
1. Pesquisa de mercado obrigatória antes de cada lote de roteiros.
2. Seleção de pautas por relevância para o público e potencial de aquisição.
3. Criar roteiro curto, natural e pronto para teleprompter.
4. Criar arquivo individual `conteudos/SG-XXX-titulo-curto.md` e atualizar `CALENDARIO.md`.
5. João grava um vídeo por arquivo e usa o mesmo ID/título no nome: `SG-XXX - TÍTULO DO VÍDEO.mp4`.
6. João envia os arquivos para `01 - VÍDEOS BRUTOS/`.
7. João solicita ao Claude a edição da pasta.
8. Claude cruza os arquivos do Drive com os roteiros por ID, identifica divergências e consulta os briefings antes de editar.
9. Claude salva projetos/versões em `02 - EM EDIÇÃO/` e exports finais em `03 - APROVADOS/`. Não marca como aprovado sem validação de João.
10. Após aprovação, salvar cópia em `04 - PUBLICADOS/` quando necessário e registrar links, data e plataforma.
11. Registrar métricas e resultados comerciais disponíveis e alimentar a próxima rodada de pesquisa.

## Gravação em lote
- Preparar a lista de roteiros aprovados.
- Agrupar por cenário, enquadramento e formato para reduzir trocas.
- Entregar o texto falado isolado, sem instruções misturadas.
- Gravar takes curtos, um vídeo por arquivo.
- Usar sufixos `-take-02`, `-take-03` quando houver novas tomadas.
- João não precisa editar nem procurar assets.

## Handoff para Claude
Ao receber solicitação para editar a pasta:
- Ler `AGENTS.md`, `CLAUDE.md`, `SISTEMA-DE-PRODUCAO-DE-CONTEUDO.md`, `PADROES-DE-EDICAO.md` e os arquivos individuais correspondentes.
- Listar os arquivos encontrados e fazer correspondência por ID.
- Informar brutos sem roteiro, roteiros sem bruto e nomes ambíguos antes de prosseguir.
- Não inventar falas, cenas reais, depoimentos, resultados ou informações comerciais.
- Preservar os brutos.
- Entregar ID, bruto, status, caminho real do export e pendências.
- Não alegar que moveu, exportou ou editou se a ação não foi confirmada.

## Mensagem padrão
“Claude, edite os vídeos disponíveis em `Meu Drive/02 - SUA GRÁFICA BH/CONTEÚDOS/01 - VÍDEOS BRUTOS/`. Consulte o repositório `ABauerlab/conteudosuagraficabh`, encontre o roteiro de cada vídeo pelo ID/nome e siga o briefing e os padrões de edição. Antes de começar, informe arquivos sem correspondência. Salve projetos e versões em `02 - EM EDIÇÃO/`; não altere os brutos. Não invente falas nem informações comerciais.”

## Controle de qualidade
- Fala fiel à gravação e ao roteiro.
- Gancho claro nos primeiros segundos.
- Legendas revisadas, legíveis e dentro da área segura.
- Áudio limpo, sem clipping e música licenciada abaixo da voz.
- Sem cortes bruscos ou ritmo que prejudique compreensão.
- Assets oficiais e identidade respeitados.
- Direitos e créditos preservados.
- Export reproduzido e conferido.
- João aprova antes de marcar como aprovado/publicável.

## Status
IDEIA → PESQUISA → ROTEIRO PRONTO → PRONTO PARA GRAVAR → GRAVADO → EM EDIÇÃO → REVISÃO → APROVADO → PUBLICADO → ANALISADO.
Estados adicionais: PAUSADO, PENDENTE DE REFERÊNCIA, PENDENTE DE DIREITOS, PENDENTE DE CATÁLOGO.
