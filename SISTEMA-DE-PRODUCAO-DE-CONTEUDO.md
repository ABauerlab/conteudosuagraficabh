# Sistema de produção de conteúdo | SUA GRÁFICA BH

## Objetivo
Operar uma máquina contínua de conteúdo para aquisição de clientes, combinando pesquisa de mercado, roteiros fáceis de gravar, edição profissional e aprendizado por resultados. O objetivo não é acumular visualizações vazias nem prometer viralização: é atrair empreendedores e transformar atenção em conversas, orçamentos e vendas.

## Fontes oficiais e responsabilidades
- **CRM** (`ABauerlab/crm-sua-grafica-bh`): fonte de verdade para identidade técnica, catálogo ativo/vendável, especificações e informações comerciais.
- **Este repositório**: fonte de verdade para estratégia editorial, pesquisa, pautas, roteiros, referências, briefings de gravação/edição e aprendizados.
- **Google Drive**: área de transferência e armazenamento dos vídeos brutos, materiais em edição e entregas finais.
- **ChatGPT**: pesquisa de mercado, estratégia, seleção de pautas e roteiro para teleprompter.
- **João**: grava os textos aprovados e envia os arquivos para o Drive.
- **Claude Code**: consulta este repositório, localiza os brutos no Drive, edita e salva os resultados no Drive.
- **Distribuição**: publicação orgânica e uso em campanhas pagas conforme decisão do responsável. Não presumir publicação automática nem dependência do Postiz.

## Fluxo operacional ponta a ponta
1. **Pesquisa:** antes de cada lote, pesquisar mercado, tendências, formatos, concorrentes e dores do público. Guardar links, datas e evidências.
2. **Seleção:** escolher pautas com potencial de atenção e relevância comercial. Definir público, objetivo de aquisição, hipótese e CTA.
3. **Roteiro:** criar fala curta, natural e pronta para teleprompter. O texto de fala deve ficar separado de instruções, cenas e notas.
4. **Registro:** atribuir ID sequencial `SG-XXX`, criar arquivo individual em `conteudos/` e atualizar `CALENDARIO.md`.
5. **Gravação:** João grava cada roteiro em vídeo separado. Nomeia o arquivo com o ID e o título do roteiro.
6. **Upload:** envia o bruto para `Meu Drive/02 - SUA GRÁFICA BH/CONTEÚDOS/01 - VÍDEOS BRUTOS/`.
7. **Handoff:** João solicita ao Claude a edição da pasta. Claude cruza cada nome/ID com o roteiro correspondente no repositório.
8. **Edição:** Claude segue o briefing individual e `PADROES-DE-EDICAO.md`. Se houver ambiguidade, arquivo ausente ou divergência de fala, pergunta antes de inventar.
9. **Revisão:** Claude salva a versão para revisão, informa arquivos concluídos e pendências. João aprova.
10. **Arquivo final:** após aprovação, mover/salvar na pasta de aprovados e manter o bruto original.
11. **Distribuição:** publicar organicamente e, quando fizer sentido, testar em mídia paga. Registrar URL, data, plataforma e identificação da campanha.
12. **Aprendizado:** registrar métricas e resultados comerciais disponíveis. Usar os aprendizados na próxima pesquisa e nos próximos roteiros.

## Pesquisa de mercado obrigatória
Nenhum lote de roteiros deve ser criado sem uma pesquisa recente, adequada ao tema e ao público. A pesquisa deve considerar:
- Tendências de formatos, assuntos e linguagem em Reels/TikTok e outras plataformas relevantes.
- Conteúdos de concorrentes e criadores como referência de mercado, nunca como fonte de informação oficial da gráfica.
- Dores, dúvidas, objeções, desejos e linguagem real de empreendedores e pequenos negócios.
- Perguntas e comentários recorrentes do público, quando houver fonte acessível.
- Oportunidades de gancho, retenção, compartilhamento, visita ao perfil e geração de conversas.
- Sazonalidade e acontecimentos relevantes, quando aplicável.

### Registro mínimo de pesquisa
Para cada pauta ou lote, registrar:
- Data da pesquisa e período observado.
- Tema/oportunidade.
- Link direto da fonte, perfil/criador, plataforma e data da publicação quando disponíveis.
- Evidência observada (ex.: formato recorrente, pergunta, comentários, padrão criativo). Não inventar métricas.
- O que pode ser aprendido sem copiar a execução.
- Como adaptar de forma original para a SUA GRÁFICA BH.
- Hipótese a testar e indicador principal.

Separar explicitamente **evidência**, **interpretação** e **hipótese**. Não afirmar que um conteúdo é viral ou tendência com base em uma única publicação sem evidência suficiente. Não copiar roteiros, identidade ou peças de terceiros.

### Pesquisa de referência para reacts
Se o roteiro depender de vídeo externo, localizar e verificar a publicação original antes de liberar o teleprompter. Preferir link direto do Instagram quando o original estiver lá. Registrar autoria, plataforma, data e situação dos direitos. Encontrar a origem não equivale a ter autorização para reutilização comercial. Se a origem ou os direitos estiverem pendentes, não entregar o roteiro dependente como pronto para gravar.

## Regras para os roteiros
- A entrega principal ao João é **somente o texto falado**, pronto para copiar e colar no teleprompter.
- Não inserir indicações como [cena], [pausa], [mostrar produto] ou comentários editoriais dentro do texto falado.
- Usar frases curtas, linguagem brasileira, natural e conversada.
- Gancho imediato, preferencialmente nos primeiros 1–2 segundos.
- Preferir 15–30 segundos quando a ideia permitir; não sacrificar clareza para atingir duração fixa.
- Evitar introduções institucionais, clichês, exageros, clickbait e promessas.
- Não começar todos os vídeos apresentando a gráfica nem forçar venda em toda pauta.
- Variar ângulos, formatos, públicos e objetivos.
- O produto não precisa aparecer em todos os vídeos. Quando aparecer, confirmar disponibilidade e informação no CRM.
- Não inventar preço, prazo, estoque, especificação, quantidade mínima, acabamento ou diferencial.
- Não prometer viralização, vendas ou resultados garantidos.

## Formato de entrega do ChatGPT
Para cada vídeo, entregar duas partes visualmente separadas:
1. **FICHA DE PRODUÇÃO (fora do teleprompter):** ID, título/filename, objetivo, público, etapa de aquisição, hipótese, duração estimada, formato, CTA, legenda, fontes da pesquisa e briefing visual/técnico resumido.
2. **TEXTO PARA TELEPROMPTER:** bloco isolado contendo exclusivamente as falas, sem cabeçalhos, cenas, notas ou instruções dentro do texto.

A ficha é para organização e Claude. O bloco de teleprompter é para João gravar. Não misturar os dois.

## Google Drive: estrutura oficial
Pasta raiz informada pelo responsável:
`Meu Drive/02 - SUA GRÁFICA BH/CONTEÚDOS/`

Estrutura:
- `01 - VÍDEOS BRUTOS/`: gravações originais de João; não sobrescrever nem apagar.
- `02 - EM EDIÇÃO/`: arquivos de trabalho e versões em andamento.
- `03 - APROVADOS/`: exports revisados e aprovados.
- `04 - PUBLICADOS/`: cópias finais e/ou registro de publicações.
- `05 - REFERÊNCIAS/`: referências e assets autorizados/licenciados.

Se o Drive conectado não permitir mover arquivos, manter cópias e informar claramente. Nunca alegar upload, movimentação ou edição concluída sem confirmar.

## Padrão de nomenclatura
Usar o mesmo ID e título em todo o fluxo:
- Roteiro: `conteudos/SG-XXX-titulo-curto.md`
- Bruto: `SG-XXX - TÍTULO DO VÍDEO.mp4`
- Projeto/edição: `SG-XXX - TÍTULO DO VÍDEO`
- Export final: `SG-XXX - TÍTULO DO VÍDEO - FINAL.mp4`

O ID `SG-XXX` é o identificador primário. Títulos podem ser ajustados, mas o ID não muda. Um vídeo por arquivo; takes adicionais recebem sufixos `-take-02`, `-take-03`.

## Handoff padrão para Claude
Quando João disser “edite os vídeos da pasta de brutos”, Claude deve:
1. Ler `AGENTS.md`, `CLAUDE.md`, este documento, `PADROES-DE-EDICAO.md` e os arquivos individuais dos IDs encontrados.
2. Listar arquivos disponíveis no Drive e comparar com IDs/títulos do repositório.
3. Relatar arquivos sem roteiro correspondente, roteiros sem bruto e nomes ambíguos antes de editar.
4. Para cada bruto identificado, consultar roteiro, fala, objetivo, formato, referência, assets e restrições.
5. Editar mantendo o sentido e a integridade das falas. Não inventar cenas reais, depoimentos, resultados ou atributos comerciais.
6. Salvar versões de trabalho em `02 - EM EDIÇÃO/` e exports aprovados em `03 - APROVADOS/`. Não mover/apagar o bruto.
7. Entregar uma tabela simples com ID, arquivo bruto, status, arquivo final e pendências.
8. Atualizar o status no calendário e arquivo individual, se autorizado e possível no repositório. Não marcar como aprovado sem aprovação de João.

### Mensagem padrão de solicitação
“Claude, edite os vídeos disponíveis em `Meu Drive/02 - SUA GRÁFICA BH/CONTEÚDOS/01 - VÍDEOS BRUTOS/`. Consulte o repositório `ABauerlab/conteudosuagraficabh`, encontre o roteiro de cada vídeo pelo ID/nome e siga o briefing e os padrões de edição. Antes de começar, informe arquivos sem correspondência. Salve projetos e versões em `02 - EM EDIÇÃO/`; não altere os brutos. Não invente falas nem informações comerciais.”

## Métricas e aquisição
Avaliar conteúdo em duas dimensões complementares:

**Orgânico**
- Alcance e visualizações, com janela temporal registrada.
- Retenção, tempo médio e conclusão, quando disponíveis.
- Compartilhamentos, salvamentos e comentários.
- Visitas ao perfil, seguidores e cliques.

**Comercial / mídia paga**
- Cliques e CTR, quando disponíveis.
- Conversas iniciadas e leads qualificados.
- Pedidos de orçamento.
- Vendas atribuídas ou influenciadas.
- Investimento, CPA/CPL e retorno, quando houver dados confiáveis.

Visualizações não são sinônimo de aquisição. Um conteúdo de menor alcance que gera conversas qualificadas pode ser mais valioso. Registrar período, plataforma, campanha e fonte dos dados. Não atribuir venda a um vídeo sem evidência de origem; marcar atribuição como direta, assistida, estimada ou desconhecida.

## Ciclo de aprendizagem
Após cada lote:
1. Identificar padrões nos vídeos com melhor retenção.
2. Comparar ganchos, temas, formatos e públicos.
3. Ver quais geraram compartilhamentos e salvamentos.
4. Cruzar, quando possível, com visitas, conversas, orçamentos e vendas.
5. Formular novos testes específicos.
6. Atualizar `ANALISE-DE-DESEMPENHO.md`, banco de ganchos e calendário.
7. Não generalizar a partir de amostras pequenas; distinguir correlação de causalidade.

## Controle de qualidade
- Texto falado corresponde ao roteiro e ao áudio.
- Gancho aparece imediatamente.
- Legendas corretas, legíveis e dentro da área segura.
- Áudio claro, sem clipping; música licenciada e abaixo da voz.
- Ritmo e cortes preservam compreensão.
- Identidade visual e assets oficiais respeitados.
- Nenhuma informação comercial inventada.
- Direitos e créditos preservados.
- Export reproduzido e conferido antes de ser marcado como concluído.

## Status padronizados
IDEIA → PESQUISA → ROTEIRO PRONTO → PRONTO PARA GRAVAR → GRAVADO → EM EDIÇÃO → REVISÃO → APROVADO → PUBLICADO → ANALISADO.
Estados adicionais: PAUSADO, PENDENTE DE REFERÊNCIA, PENDENTE DE DIREITOS, PENDENTE DE CATÁLOGO.
