# Registro incremental | 07 - Impressões prontas

Este arquivo é o ledger persistente da rotina recorrente de conteúdos adicionais produzidos a partir das mídias da pasta do Drive. Claude deve consultá-lo **antes** de criar qualquer publicação e atualizá-lo durante cada execução.

## Pasta de entrada oficial

`Meu Drive/02 - SUA GRÁFICA BH/CONTEÚDOS/07 - IMPRESSÕES PRONTAS/`

Pasta de arquivo após publicação confirmada:

`Meu Drive/02 - SUA GRÁFICA BH/CONTEÚDOS/07 - IMPRESSÕES PRONTAS/POSTADOS/`

A subpasta `POSTADOS` nunca deve ser incluída na varredura de novas mídias.

## Regra editorial e escolha do formato

- A pasta pode conter fotos, imagens de frente e verso, detalhes e vídeos do mesmo produto/trabalho.
- Inspecionar os arquivos e identificar relações entre eles antes de criar conteúdo. Nome, contexto visual e metadados são pistas, não prova isolada de relação.
- Frente e verso do mesmo item podem compor um carrossel.
- Fotos diferentes do mesmo trabalho podem compor carrossel quando cada mídia acrescentar ângulo, detalhe ou informação.
- Vídeo pode ser publicado sozinho como Reel/vídeo ou integrado a um carrossel com fotos e/ou outros vídeos, se o canal e o Postiz aceitarem essa combinação.
- Foto e vídeo do mesmo trabalho podem ser combinados em um conteúdo ou publicados separadamente, conforme narrativa e valor de cada mídia. Evitar duplicação desnecessária.
- Uma imagem isolada pode virar post estático quando esse for o melhor formato.
- Não agrupar materiais sem relação, não forçar carrossel e não criar automaticamente um post por arquivo.
- Um conjunto coerente pode gerar um único conteúdo SG com várias mídias. Cada arquivo de origem continua com registro individual no ledger para deduplicação e rastreabilidade.
- Os conteúdos são **adicionais** à cadência regular do lote; não substituem Reels, carrosséis ou Stories planejados.
- Se não houver mídia nova elegível, não criar conteúdo adicional.
- Não modificar, renomear ou apagar os arquivos originais. A movimentação para POSTADOS é permitida somente após publicação confirmada, conforme o protocolo abaixo.
- Cada conteúdo recebe um ID SG global, sequencial e não reutilizável, com briefing individual em `FEED/SG-XXX.md` ou `REELS/SG-XXX.md`, conforme o formato principal.
- Consultar `CALENDARIO.md` e a árvore completa do repositório para descobrir o próximo ID livre. O valor “próximo ID” no calendário é atualizado após cada novo registro. Não presumir que um lote encerrado libera IDs.

## Procedimento de detecção e deduplicação

Para cada arquivo encontrado:

1. Capturar o ID imutável do arquivo no Google Drive, se exposto pela integração.
2. Calcular SHA-256 dos bytes originais quando for possível baixar/ler o arquivo.
3. Quando disponível, calcular hash perceptual (pHash/dHash) ou comparar visualmente para detectar cópias redimensionadas, comprimidas, recortadas ou renomeadas.
4. Comparar esses identificadores com todos os registros abaixo e com os briefings/exports já existentes.
5. Tratar como já conhecido quando houver correspondência de Drive ID, SHA-256 ou forte correspondência visual. Em caso de dúvida, não criar outro post: registrar como PENDENTE DE DEDUPLICAÇÃO.
6. Nome de arquivo isolado, data de modificação isolada ou pasta vazia no repositório não comprovam que uma imagem é nova.
7. Se a integração não fornecer ID nem bytes, Claude deve fazer inspeção visual e registrar a limitação e o fingerprint alternativo utilizado. Não afirmar deduplicação criptográfica quando ela não ocorreu.

## Elegibilidade e proteção

Antes de criar o post, conferir:
- A foto representa um produto real finalizado, sem edição que altere ou falseie o produto.
- Não há dados pessoais, telefones, endereços, pedidos, documentos, informações confidenciais ou dados de cliente expostos.
- Marcas, artes e trabalhos identificáveis de clientes só podem ser publicados quando a autorização de exposição estiver coberta. Se não houver confirmação, registrar PENDENTE DE AUTORIZAÇÃO.
- Qualquer afirmação sobre nome do produto, material, acabamento, tamanho, aplicação, prazo, preço ou disponibilidade deve ser confirmada no CRM. A foto não comprova especificação nem disponibilidade atual.
- A legenda deve contextualizar o trabalho sem inventar cliente, depoimento, resultado, quantidade ou benefício.
- O post usa a identidade oficial exclusivamente a partir de `Meu Drive/02 - SUA GRÁFICA BH/IDENTIDADE VISUAL/SUA_GRAFICA_BH_BRANDKIT/`.

## Protocolo obrigatório de movimentação para POSTADOS

A pasta `POSTADOS` é o arquivo de mídias já publicadas e uma segunda barreira contra duplicidade. O ledger continua sendo o registro principal: mover um arquivo não substitui o controle por Drive ID, hash e histórico.

1. Na varredura, ler somente a pasta raiz `07 - IMPRESSÕES PRONTAS` e suas pastas de entrada pertinentes. Excluir `POSTADOS` e todo o seu conteúdo da descoberta de novos itens.
2. Antes de produzir, cruzar os arquivos da entrada com o ledger e com os briefings, exports e confirmações do Postiz.
3. Depois da publicação, confirmar cada destino previsto. Só considerar elegível para movimentação quando todos os destinos previstos estiverem com publicação efetivamente confirmada. Não mover por upload, rascunho, aprovação, agendamento ou confirmação parcial.
4. Atualizar o ledger com o status `PUBLICADA/CONFIRMADA`, IDs/links do Postiz por destino e movimentação `PENDENTE`; depois mover os arquivos originais correspondentes para `POSTADOS`, preservando nome e conteúdo.
5. Após mover, confirmar que cada arquivo está no destino, registrar seu Drive ID/localização de destino e marcar movimentação `CONCLUÍDA`.
6. Se a publicação estiver confirmada e o move falhar, manter `PUBLICADA/CONFIRMADA` e `movimentação PENDENTE`. Na próxima execução, não criar outra publicação; tentar somente finalizar a movimentação.
7. Se houver falha de publicação em algum destino, não mover o conjunto inteiro. Registrar os destinos confirmados e pendentes; retomar somente a distribuição que falta, sem duplicar nos destinos já confirmados.
8. Para conjuntos com várias fotos/vídeos, mover cada arquivo de origem associado ao SG somente após a confirmação completa da publicação daquele conteúdo. Registrar movimentação por arquivo para lidar com falhas parciais.
9. Se `POSTADOS` não existir, criá-la somente se o Drive MCP permitir. Se não houver permissão, manter o conteúdo publicado, registrar bloqueio de movimentação e não solicitar ações desnecessárias.
10. Nunca sobrescrever um arquivo de mesmo nome no destino. Em caso de colisão, verificar se é o mesmo Drive ID/arquivo; se for outro arquivo, preservar ambos e registrar a ocorrência sem renomear automaticamente.

## Registro de cada arquivo

Manter uma linha por arquivo de origem (imagem ou vídeo), inclusive para itens bloqueados ou rejeitados. Não apagar linhas antigas.

| Campo | O que registrar |
|---|---|
| Drive file ID | ID imutável do arquivo, quando disponível |
| Nome original | Nome exato na pasta de entrada |
| SHA-256 | Hash dos bytes originais, quando disponível |
| Fingerprint visual | pHash/dHash ou nota da comparação visual, quando disponível |
| Primeira detecção | Data/hora da primeira varredura |
| ID SG | ID atribuído; vazio apenas se ainda não elegível |
| Lote | Pasta do lote que recebeu o briefing |
| Briefing | Caminho do arquivo SG individual |
| Status | Estado atual conforme a lista abaixo |
| Data planejada | Data futura incluída no calendário, se definida |
| Postiz | Canal, identificador/link e confirmação por destino |
| Origem | Localização e ID imutável do arquivo na pasta de entrada |
| Destino POSTADOS | Localização e ID do arquivo após a movimentação |
| Movimentação | NÃO APLICÁVEL, PENDENTE, CONCLUÍDA ou BLOQUEADA |
| Observações | Pendência, motivo, licença/autorização ou correção necessária |

## Agrupamento e rastreabilidade de conjuntos

Manter uma linha para cada arquivo de origem, mesmo quando vários arquivos formarem um único conteúdo. Acrescentar aos registros, quando aplicável:
- **Grupo/conjunto:** identificador interno para relacionar frente/verso, fotos e vídeos do mesmo trabalho.
- **Conteúdo SG associado:** ID do conteúdo que utiliza o arquivo. Vários arquivos podem apontar para o mesmo ID SG.
- **Formato escolhido:** estático, carrossel de imagens, vídeo/Reel ou carrossel misto de fotos e vídeos.
- **Relação/ordem:** frente, verso, detalhe, ângulo, vídeo principal, vídeo complementar e ordem prevista.
- **Motivo da escolha:** por que o formato apresenta melhor o trabalho e quais limitações de canal/Postiz foram verificadas.

Não atribuir um SG separado para cada arquivo que integra o mesmo carrossel. A rastreabilidade é por arquivo; o briefing e a publicação são por conjunto editorial coerente.

## Estados permitidos

- `DETECTADA`: arquivo novo encontrado, ainda em triagem.
- `PENDENTE DE DEDUPLICAÇÃO`: identidade da imagem não pôde ser confirmada.
- `PENDENTE DE AUTORIZAÇÃO`: precisa de autorização de uso ou revisão de privacidade.
- `PENDENTE DE CATÁLOGO`: depende de informação comercial não confirmada.
- `ELEGÍVEL`: aprovada para briefing e produção.
- `BRIEFING CRIADO`: ID SG e briefing individual registrados.
- `EM PRODUÇÃO`
- `EM REVISÃO`
- `APROVADA`
- `ENVIADA AO POSTIZ`
- `AGENDADA/CONFIRMADA`
- `PUBLICADA/CONFIRMADA`
- `REJEITADA`: não usar, com justificativa documentada.

Itens pendentes ou rejeitados não devem ser recriados em execuções seguintes. Só reavaliar quando houver mudança concreta no arquivo, na autorização, no acesso ou instrução expressa do responsável.

## Como inserir no calendário

Adicionar cada conteúdo adicional como linha própria na seção de conteúdos adicionais — impressões prontas de `CALENDARIO.md` e no README do lote que contém seu briefing. Registrar o formato real (estático, carrossel, Reel/vídeo ou misto), sem presumir que todo item é post estático.

- Marcar explicitamente como adicional, sem substituir a grade regular.
- Usar somente datas futuras compatíveis com o calendário vigente e com espaço de publicação.
- Se o lote atual já terminou, inserir no próximo lote aberto/futuro, sem retroagir.
- Não inventar horário. Só registrar horário quando definido/confirmado.
- Atualizar o status somente após evidência real; agendamento e publicação exigem confirmação individual no Postiz.

## Ledger inicial

Nenhuma mídia foi inspecionada ou registrada por esta alteração documental. Claude deve fazer a próxima varredura da pasta de entrada, identificar arquivos relacionados e inserir cada arquivo encontrado nesta tabela, relacionando conjuntos quando aplicável.

| Drive file ID | Nome original | SHA-256 | Fingerprint visual | Primeira detecção | ID SG | Lote/briefing | Status | Data planejada | Postiz / observações | Origem | Destino POSTADOS | Movimentação |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
