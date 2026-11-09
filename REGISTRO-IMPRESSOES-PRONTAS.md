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

Primeira varredura em 09/11/2026 (lote SG-025 a SG-048): 2 arquivos, ambos PENDENTE DE AUTORIZAÇÃO. Nenhum ID SG consumido e nenhum post adicional criado.

Atualização 09/11/2026 (segunda execução): autorização do cliente confirmada por João em 09/11/2026 para os 2 arquivos. Status alterado para ELEGÍVEL; IDs SG-049 e SG-050 atribuídos após conferir que estavam livres em CALENDARIO.md, na árvore do repositório e em 03 - APROVADOS. Nenhum arquivo novo na pasta além destes dois.

| Drive file ID | Nome original | SHA-256 | Fingerprint visual | Primeira detecção | ID SG | Lote/briefing | Status | Data planejada | Postiz / observações |
|---|---|---|---|---|---|---|---|---|---|
| 1yY8TnfbeHEIWrQ4yn6Fb7D_QkigkI1pF | Tags (HEIC) | 33e644c2d2c82dd0e7a92b6c3fa900fe4af3d84d02cafde7d2b3617903a70ce0 | pHash c63f609b96640dba / dHash faea32e968f182c2 | 2026-11-09 | SG-049 | conteudos/lote-2026-11-04-a-2026-11-11/FEED/SG-049.md | APROVADA (histórico: PENDENTE DE AUTORIZAÇÃO → ELEGÍVEL em 09/11/2026 → BRIEFING CRIADO → APROVADA) | 12/11/2026 (ADICIONAL; horário pendente de definição) | Autorização do cliente confirmada por João em 09/11/2026. SHA-256 conferido de novo em 09/11/2026 (bytes idênticos). Post estático único 1080x1350 `SG-049-FEED-01.png` (03 - APROVADOS/SG-049/), foto real só recortada. Grupo TAGS confirmado no CRM. Postiz: ainda não agendado (aguardando horário). |
| 1avXOVIev7p62Y4GcYyNc93f8NnjG0b7V | Cartão de visita (HEIC) | c9cad4ba1065c2a9581ac1ebd53ebeb345d32a78fd61682f5dd1392b2fa56f08 | pHash bfe4c04d3c31e4e2 / dHash 15630d1f33335b19 | 2026-11-09 | SG-050 | conteudos/lote-2026-11-04-a-2026-11-11/FEED/SG-050.md | APROVADA (histórico: PENDENTE DE AUTORIZAÇÃO → ELEGÍVEL em 09/11/2026 → BRIEFING CRIADO → APROVADA) | 13/11/2026 (ADICIONAL; horário pendente de definição) | Autorização do cliente confirmada por João em 09/11/2026. SHA-256 conferido de novo em 09/11/2026 (bytes idênticos). QR code e endereço mantidos sem desfoque (publicação autorizada; arte impressa não alterada). Post estático único 1080x1350 `SG-050-FEED-01.png` (03 - APROVADOS/SG-050/). Grupo CARTÕES DE VISITA confirmado no CRM. Postiz: ainda não agendado (aguardando horário). |
