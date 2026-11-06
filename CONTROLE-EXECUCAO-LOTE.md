# Controle de execução | Lote 06 a 13/11/2026 | Etapa 1 (06 a 08/11)

Atualizado em 06/11/2026. Branch de trabalho: `claude/gallant-johnson-jbnsz8`.
Arquivos em `producao/etapa-1/SG-XXX/` (repositório). Upload para o Drive (`02 - EM EDIÇÃO` e `03 - APROVADOS`) NÃO realizado: a ferramenta do Drive só aceita conteúdo via base64 no contexto, inviável para PNG/MP4.

## Resumo honesto
| Bloco | Total | Produzido | Agendado no Postiz | Pendente |
|---|---|---|---|---|
| Reels | 6 | 0 | 0 | 6 |
| Feed | 3 | 3 (15 slides) | 1 (SG-003) | 2 (SG-009, SG-015) |
| Stories | 9 | 9 | 3 (SG-004, 005, 006) | 6 |

"Agendado" = o Postiz retornou `postId` na criação. A fila não foi reconferida (não há ferramenta de listagem). Conferir na fila do Postiz antes das 12:00 UTC.

## Reels (6) | PENDENTE
Os 16 brutos existem no Drive (`01 - VÍDEOS BRUTOS`, IDs SG-001/002/007/008/013/014 presentes). Não foi possível editar: baixar um MP4 de ~40 MB pelo conector do Drive exigiria passar o arquivo em base64 pelo contexto, e o sandbox não acessa o Drive por rede. Também não há ferramenta para enviar vídeo ao Postiz.
Caminho mínimo: rodar a edição em ambiente com acesso direto ao Drive (Claude Code local do João) ou disponibilizar os brutos em uma URL/pasta acessível ao sandbox.
| ID | Data | Status |
|---|---|---|
| SG-001, SG-002 | 06/11 | PENDENTE, não editado, não agendado |
| SG-007, SG-008 | 07/11 | PENDENTE, não editado, não agendado |
| SG-013, SG-014 | 08/11 | PENDENTE, não editado, não agendado |

## Feed
Slides 1080x1350 individuais, copy fiel ao briefing, logo oficial (SVG do Brand Kit), paleta e Inter do `cores_e_fontes_tokens.json`. Sem fotografia (não há banco licenciado acessível); direção "foto de comércio" do slide 1 não atendida, substituída por composição gráfica CMYK.
| ID | Arquivos | Status |
|---|---|---|
| SG-003 | `producao/etapa-1/SG-003/SG-003-SLIDE-01..05.png` | Agendado: IG 06/11 12:30 BRT (`cmw4eaido0006rz8gz5gi3gq5`), FB 13:00 BRT (`cmw4eawix000arz8grq2tba9v`), Threads 14:30 BRT (`cmw4eawjr000brz8grn3pomrd`) |
| SG-009 | `.../SG-009/SG-009-SLIDE-01..05.png` | PRODUZIDO, NÃO AGENDADO (ver pendência A) |
| SG-015 | `.../SG-015/SG-015-SLIDE-01..05.png` | PRODUZIDO, NÃO AGENDADO (ver pendência A) |

## Stories (IG; Facebook Story não agendado, o Postiz não expõe Story para Facebook)
| ID | Arquivo | Status |
|---|---|---|
| SG-004 | `SG-004/SG-004-STORY-1080x1920.png` | Agendado IG 06/11 09:00 BRT (`cmw4eaomw0007rz8gp9xnrp7m`) |
| SG-005 | `SG-005/SG-005-STORY-1080x1920.png` | Agendado IG 06/11 14:00 BRT (`cmw4eaoni0008rz8gkhw6ua01`) |
| SG-006 | `SG-006/SG-006-STORY-1080x1920.png` | Agendado IG 06/11 20:00 BRT (`cmw4eaoob0009rz8gplzvvked`) |
| SG-010, 011, 012 | `SG-010..012/...png` | PRODUZIDO, NÃO AGENDADO (pendência A) |
| SG-016, 017, 018 | `SG-016..018/...png` | PRODUZIDO, NÃO AGENDADO (pendência A) |

## Pendências e decisões
- **A. Conteúdo repetido.** SG-009 e SG-015 têm slides idênticos aos do SG-003 (só muda o título da legenda, que não corresponde ao slide). Os Stories de 07 e 08/11 repetem os textos de SG-004/005/006. Não agendei para não publicar o mesmo conteúdo em 3 dias seguidos. Para liberar, basta João confirmar "agende mesmo assim" (ou enviar copy nova).
- **B. Enquete nativa** (SG-004/010/016): não existe via Postiz. A arte reserva a faixa inferior; adicionar o sticker de enquete no app, se desejado. Nenhum sticker falso foi desenhado.
- **C. Stories são publicados via Postiz como `post_type=story`.** Confirmar na primeira publicação (09:00 BRT) que saiu como Story.
- **D. Fotografia:** SG-006/012/018 pedem foto original/licenciada; entregues sem foto (gráfico). Substituir se João enviar foto.
- **E. Logo:** reconstruído do SVG oficial do Brand Kit; o símbolo ® minúsculo do original foi omitido. Conferir.
- **F. Catálogo/CRM:** nenhuma peça cita produto, preço ou prazo; consulta ao catálogo não necessária.
- **G. Mídia no Postiz** usa URLs `raw.githubusercontent.com` da branch de trabalho. Não apagar/renomear a branch antes da publicação (13:00 BRT 06/11 em diante só SG-003; Stories às 09:00/14:00/20:00).
- **H. Horários** são sugestão espaçada (sem dados confiáveis de insights), não dado de melhor desempenho. Janelas de 08:00 e 18:30 BRT reservadas aos Reels.
- **I. Revisão visual:** inspecionadas todas as 24 peças em folha de contato e as correções de layout reexportadas; não foi feita revisão pixel a pixel de cada arquivo em tela cheia.
