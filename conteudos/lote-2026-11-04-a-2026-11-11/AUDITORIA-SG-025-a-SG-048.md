# Auditoria e controle de execução | SG-025 a SG-048 (10 a 13/11/2026)

Execução: 09/11/2026, comando “Finalize o lote SG-025 a SG-048”. Escopo limitado a estes 24 IDs, mais a rotina de impressões prontas.

## Acessos verificados
| Recurso | Resultado |
|---|---|
| Brutos no Drive (`01 - VÍDEOS BRUTOS/02 - GRAVADOS/`) | Os 8 brutos existem: SG-025, SG-026 (nome com espaço: `SG-026 .mp4`), SG-031, SG-032, SG-037, SG-038, SG-043, SG-044, entre 38 e 42 MB cada. **Não puderam ser baixados**: o conector do Drive limita downloads a 10 MB, e o link direto exige login (arquivo privado). |
| Brand Kit oficial | Acessível. Usados: `LOGO_HORIZONTAL/sua_grafica_bh_logo_horizontal_colorido_fundo_claro.png` e `..._fundo_escuro.png` (SHA-256 2aab02bf… e 85436781…), `cores_e_fontes_tokens.json` (paleta e Inter). |
| Prancha visual do lote em `05 - REFERÊNCIAS/` | Nenhuma prancha com IDs SG-025 a SG-048 encontrada. Usados os ativos oficiais, conforme a regra de ausência de prancha. |
| CRM (Supabase) | Acessível. Grupos ativos e vendáveis confirmados em 09/11/2026: TAGS, CARDÁPIOS, CARTÕES FIDELIDADE, CALENDÁRIOS E FOLHINHAS 2027. Materiais citados nas artes constam do catálogo. Nenhum preço, prazo ou gramatura publicado. |
| Postiz | Integrações da SUA GRÁFICA BH conectadas: Instagram `cmvtp8ery0001qt7yhzygfbj3`, Facebook `cmvtp8x0j0003qt7yx77mreyp` e Threads `cmvtt2igw0001rz8gjexak5tp`. O agendamento exige URLs públicas de mídia, e esta sessão não tem rota para hospedá-las. A consulta da fila (`ask_postiz`) falha no servidor (chave OpenAI do Postiz ausente), então não foi possível checar duplicidade. A API pública (`/api/public/v1`) exige chave de API. |

## Gates por ID
| ID | Formato | Data | Gate 2 (repetição) | Gate 3 (briefing) | Correção aplicada | Produção | Distribuição |
|---|---|---|---|---|---|---|---|
| SG-025 | Reel | 10/11 | APROFUNDAMENTO REAL (vizinho de SG-007; ângulo próprio: simplificar) | OK após correção | Data, legenda 1 linha Montserrat, capa gráfica original, hashtags | Capa PRODUZIDA; vídeo PENDENTE DE ACESSO AO BRUTO | Bloqueada |
| SG-026 | Reel | 10/11 | NOVA ABORDAGEM | OK após correção | idem | idem | Bloqueada |
| SG-027 | Carrossel | 10/11 | Reprovado (copy idêntica a SG-003/SG-021) | Reescrito | Novo tema: cartão fidelidade, 7 slides | 7 slides PRODUZIDOS e revisados | Bloqueada |
| SG-028 a SG-030 | Stories | 10/11 | Reprovado (textos repetidos 4x no lote) | Reescritos | Sequência cartão fidelidade | 3 PRODUZIDOS e revisados | Bloqueada |
| SG-031 | Reel | 11/11 | NOVA ABORDAGEM | OK após correção | Data, legenda, capa, hashtags | Capa PRODUZIDA; vídeo PENDENTE | Bloqueada |
| SG-032 | Reel | 11/11 | NOVA ABORDAGEM | OK após correção | idem | idem | Bloqueada |
| SG-033 | Carrossel | 11/11 | Reprovado (copy idêntica) | Reescrito | Calendário 2027 como brinde, 7 slides | 7 slides PRODUZIDOS | Bloqueada |
| SG-034 a SG-036 | Stories | 11/11 | Reprovado | Reescritos | Sequência brindes 2027 | 3 PRODUZIDOS | Bloqueada |
| SG-037 | Reel | 12/11 | APROFUNDAMENTO REAL (vizinho de SG-002) | OK após correção | Data, legenda, capa, hashtags | Capa PRODUZIDA; vídeo PENDENTE | Bloqueada |
| SG-038 | Reel | 12/11 | NOVA ABORDAGEM (comparar orçamentos) | OK após correção | idem | idem | Bloqueada |
| SG-039 | Carrossel | 12/11 | Reprovado (copy idêntica; título repetia SG-002/SG-038) | Reescrito | Cardápio, 8 slides | 8 slides PRODUZIDOS | Bloqueada |
| SG-040 a SG-042 | Stories | 12/11 | Reprovado | Reescritos | Sequência cardápio | 3 PRODUZIDOS | Bloqueada |
| SG-043 | Reel | 13/11 | REAPROVEITAMENTO ESTRATÉGICO com ressalva: sobrepõe SG-020 (conferir antes de produzir). Diferença: foco no processo de aprovação e em outra pessoa revisando. Bruto já gravado; mantido. | OK após correção | Data, legenda, capa, hashtags | Capa PRODUZIDA; vídeo PENDENTE | Bloqueada |
| SG-044 | Reel | 13/11 | NOVA ABORDAGEM | OK após correção | idem | idem | Bloqueada |
| SG-045 | Carrossel | 13/11 | Reprovado (copy idêntica; título repetia SG-003/020/043) | Reescrito | Tag de roupa, 7 slides | 7 slides PRODUZIDOS | Bloqueada |
| SG-046 a SG-048 | Stories | 13/11 | Reprovado | Reescritos | Sequência tags | 3 PRODUZIDOS | Bloqueada |

Datas: os briefings indicavam 08 a 11/11, mas o calendário vigente (`CALENDARIO.md`) e o comando de João indicam 10 a 13/11. Os briefings foram alinhados ao calendário.

## Controle de qualidade das artes
- 49 PNGs: 8 capas 1080x1920, 29 slides 1080x1350 e 12 Stories 1080x1920. Dimensões conferidas com `identify`.
- Cada peça foi aberta em folha de contato e em simulação de celular. Problemas encontrados e corrigidos antes do export final: realce das capas cortava descendentes; texto de apoio pequeno demais para celular; ilustração sobreposta ao texto em SG-040, SG-041 e SG-045 (slides 2, 3, 4, 6 e 7).
- Copy conferida contra os briefings individuais. Logotipo oficial inserido sem alteração. Fonte Inter (oficial). Ilustrações vetoriais originais e genéricas, sem marcas de terceiros. Valores de cardápio aparecem como “R$ 00”.
- Stories: nenhum sticker de enquete foi desenhado. A enquete nativa só pode ser adicionada se o recurso estiver disponível na publicação.
- Capas de Reels: arte gráfica original. Quando o bruto estiver acessível, pode receber recorte de João, sem mudar o título.
- Fonte editável: `producao/artes-lote-2026-11-10-a-2026-11-13/` (`render.js` + `pecas.js`). Exports e SHA-256: `midia/exports/lote-2026-11-10-a-2026-11-13/`.

## Status por estado oficial
- PRODUZIDO e revisado (APROVADO no QA de Claude): artes dos 16 IDs de Feed/Stories e as 8 capas de Reels.
- PENDENTE DE ACESSO (bruto): edição dos 8 Reels.
- PENDENTE DE ACESSO (distribuição): os 24 IDs. Nada foi enviado ao Postiz, agendado ou publicado.
- Drive: os exports não foram copiados para `02 - EM EDIÇÃO/` nem para `03 - APROVADOS/`, porque o conector só aceita upload binário em base64 inline, inviável para estes arquivos. Estão no repositório.

## Para desbloquear
1. **Brutos:** adicionar os 8 MP4 ao repositório via Git LFS, em `midia/videos-brutos/` (rota já documentada no README da pasta), **ou** compartilhar temporariamente `02 - GRAVADOS` como “qualquer pessoa com o link”, para download direto.
2. **Postiz:** criar uma chave da API pública em Postiz (Configurações → API) e salvá-la como segredo de rede do ambiente para o host `postiz.bauerlab.com.br`, no header `Authorization` **sem** prefixo. Com ela é possível subir as mídias, checar duplicidade e agendar.

## Execução de 10/11/2026 (terceira execução): Reels e adicionais
Comando: “Finalize o lote SG-025 a SG-048”. Feed e Stories já estavam agendados desde 09/11 e foram preservados (nenhum reenvio). Uma sessão local paralela que rodava transcrição na pasta CONTEÚDOS foi sinalizada a João; a partir daí esta sessão assumiu o lote (decisão de João).

### Acessos
- Brutos: lidos pelo computador de João (Drive sincronizado), copiados para o ambiente sem alterar os originais. Os 8 brutos são HEVC 1080x1920, 32,6 a 35,5 s, tomada única, sem objetos de apoio (as ações de captação com folhas/post-its não foram gravadas; o apoio visual veio do motion).
- Brand Kit oficial: logotipos horizontais, faixa CMYK, fundo gradiente, canto de círculos e ícones coloridos, usados sem alteração.
- Postiz: integrações IG, FB e Threads da SUA GRÁFICA BH. A leitura da fila (`ask_postiz`) continua falhando no servidor; a duplicidade foi controlada pelos registros do repositório (nenhum Reel destes IDs havia sido enviado). Mídia por URL raw do GitHub (cópias de distribuição em `midia/exports/...`), rota autorizada por João em 10/11/2026.

### Edição dos 8 Reels
- Projeto-fonte React + Remotion (`producao/remotion-lote-2026-11-10-a-2026-11-13/`), um mapa fala → motion por Reel em `src/data/`, gerado por `scripts/gen.py`.
- **Sem transcrição e sem processamento de áudio** (PROMPT-UNICO-CLAUDE.md). O teleprompter foi distribuído pela fala real usando só a detecção de pausas e a contagem de sílabas; a taxa medida (6,1 a 6,9 sílabas/s em todos) é compatível com a leitura do roteiro integral. Corte apenas do silêncio inicial (0,3 a 0,6 s) e final; a fala, incluindo o CTA final, não foi cortada.
- Legendas Montserrat, uma linha: SG-026, 031, 037 e 043 (finais de frase ancorados em pausas reais). **Omitidas** em SG-025, 032, 038 e 044: fala contínua sem pausas suficientes para garantir a sincronia; o motion tipográfico foi mantido.
- Motion por bloco de fala: gancho em texto nos primeiros 2,6 s (acima do rosto), cenas de lista, passos, comparação, afirmação e risco (strike), palavras-chave, punch-ins motivados e cena de CTA com logotipo. O apresentador vai para janela circular nas cenas, rosto sempre visível.
- Trilha Pixabay a volume 0,07 sob a voz (registro em `TRILHAS-PIXABAY.md`). Duas das três faixas aparecem como “AI generated” no Pixabay; licença conferida em 09/11.
- Capas: as artes originais produzidas em 09/11 (não são frames do vídeo).

### QA realizado
- Cada export: 1080x1920, H.264/AAC, 30 fps, duração 33,1 a 36,0 s; nível médio de áudio igual ao do bruto (±0,1 dB), confirmando voz preservada e trilha abaixo dela.
- Folha de quadros a cada 1 s de cada Reel revisada. Problemas encontrados e corrigidos antes de aprovar: gancho sobreposto à primeira cena (SG-025/031), palavra-chave invadindo a transição para cena, itens de strike/afirmação colados na mesma linha, ganchos quebrando palavra no meio (SG-031/038/043) e palavra-chave longa saindo da tela (SG-044).
- **Limite declarado:** esta sessão não ouve áudio. Fala e CTA foram conferidos por métricas (pausas, taxa silábica, nível), não por escuta. Recomenda-se assistir a um Reel com som antes do primeiro horário.

### Distribuição confirmada (IDs retornados pelo Postiz)
Ver tabela em `CALENDARIO.md`. 24 publicações de Reels (8 IDs x IG, FB, Threads) e 6 dos adicionais SG-049/SG-050 (16:30 BRT de 12 e 13/11). SG-025 reencaixado para 10/11 21:00 BRT (00:00 UTC de 11/11), horário aprovado por João, porque o slot das 08:00 já tinha passado.

### Pendências
- Capas dos Reels não foram anexadas no Postiz (o conector não oferece campo de capa); escolher a capa manualmente no Instagram se desejado.
- Facebook Story continua sem suporte no conector (Stories só no Instagram).
- Leitura da fila do Postiz indisponível (chave OpenAI do agente de consulta ausente no servidor).
