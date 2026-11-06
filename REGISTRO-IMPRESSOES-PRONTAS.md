# Registro incremental | 07 - Impressões prontas

Este arquivo é o ledger persistente da rotina recorrente de posts estáticos adicionais. Claude deve consultá-lo **antes** de criar qualquer publicação a partir da pasta do Drive e atualizá-lo durante cada execução.

## Pasta de entrada oficial

`Meu Drive/02 - SUA GRÁFICA BH/CONTEÚDOS/07 - IMPRESSÕES PRONTAS/`

## Regra editorial

- Uma imagem nova elegível = um post estático individual.
- Nunca agrupar várias fotos em um post ou carrossel.
- Os posts são **adicionais** à cadência regular do lote; não substituem Reels, carrosséis ou Stories planejados.
- Se não houver imagem nova elegível, não criar post adicional.
- Não modificar, mover, renomear ou apagar o arquivo original.
- Cada publicação recebe um ID SG global, sequencial e não reutilizável, e um briefing individual em `FEED/SG-XXX.md` do lote vigente.
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

## Registro de cada arquivo

Manter uma linha por imagem, inclusive para itens bloqueados ou rejeitados. Não apagar linhas antigas.

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
| Observações | Pendência, motivo, licença/autorização ou correção necessária |

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

Adicionar cada post como linha própria na seção **Posts estáticos adicionais — impressões prontas** de `CALENDARIO.md` e no README do lote que contém seu briefing.

- Marcar explicitamente como adicional, sem substituir a grade regular.
- Usar somente datas futuras compatíveis com o calendário vigente e com espaço de publicação.
- Se o lote atual já terminou, inserir no próximo lote aberto/futuro, sem retroagir.
- Não inventar horário. Só registrar horário quando definido/confirmado.
- Atualizar o status somente após evidência real; agendamento e publicação exigem confirmação individual no Postiz.

## Ledger inicial

Nenhuma imagem foi inspecionada ou registrada por esta alteração documental. Claude deve fazer a primeira varredura da pasta de entrada na próxima execução e inserir cada arquivo encontrado nesta tabela.

| Drive file ID | Nome original | SHA-256 | Fingerprint visual | Primeira detecção | ID SG | Lote/briefing | Status | Data planejada | Postiz / observações |
|---|---|---|---|---|---|---|---|---|---|
