# Pipeline audiovisual, legendas, motion e entrega final

**Status:** norma operacional complementar e prevalente para produção/fechamento de Reels e lotes. Atualizada em 26/11/2026 após auditoria de contradições da main e pesquisa de ferramentas.

## 1. Objetivo e hierarquia

Este documento fecha quatro lacunas operacionais: sincronização de legendas com fala real, liberdade para motion full-screen sem o apresentador, execução verificável de Impressões Prontas e empacotamento plano para transferência ao Postiz.

Ler junto de `DIRECAO-AUDIOVISUAL-PROFISSIONAL.md`, `PADROES-DE-EDICAO.md`, `PRODUCAO-DE-VIDEOS.md`, `AGENTS.md` e do briefing individual. Em caso de conflito com proibições antigas de ASR/Whisper ou obrigação de manter o apresentador sempre visível, esta norma prevalece, respeitando a integridade da faixa original.

## 2. Pesquisa de stack e decisão técnica

Pesquisa consultada em 26/11/2026:

| Ferramenta/skill | Uso indicado | Decisão |
|---|---|---|
| Remotion + `remotion-dev/skills` | Composições programáticas React, cenas reutilizáveis, componentes, render e preview | ESSENCIAL como motor quando o projeto e a licença forem adequados |
| HyperFrames + GSAP | Composição HTML determinística, timelines, animação avançada e render via Chrome/FFmpeg | ESSENCIAL como alternativa/stack complementar; escolher por projeto, não duplicar sem motivo |
| `iart-ai/motion-design-skills` | Princípios de animação, direção de arte, composição, cor e timing | RECOMENDADA; instalar apenas módulos necessários |
| `charlie947/motion-graphics-skills` | Storyboards, launch films, explainer, motion effects e gráficos | RECOMENDADA para avaliação prática de módulos relevantes |
| `Barty-Bart/motion-graphics` | B-roll/motion, separação de objetos e explainers | COMPLEMENTAR; `motion-broll` só após conferir como usa transcript e nunca passar a faixa original para processamento |
| FFmpeg/FFprobe | Inspeção de mídia, extração temporária para análise, mux, composição e export | ESSENCIAL |
| WhisperX ou alinhador equivalente | ASR e alinhamento forçado para timestamps de palavras | RECOMENDADA para alinhamento local, após validar suporte ao pt-BR, hardware e licença |

Fontes de pesquisa:
- Remotion Agent Skills: https://www.remotion.dev/docs/ai/skills
- Remotion CLI skills: https://www.remotion.dev/docs/cli/skills
- Remotion licença: https://www.remotion.dev/docs/license/pricing e https://www.remotion.dev/docs/license/faq
- HyperFrames introdução: https://hyperframes.app/docs/1-startup/1-introduction
- HyperFrames Quickstart: https://hyperframes.app/docs/1-startup/2-quickstart
- HyperFrames CLI/QA: https://github.com/heygen-com/hyperframes/blob/main/skills/hyperframes-cli/references/lint-validate-inspect.md
- GSAP Timeline: https://gsap.com/docs/v3/GSAP/Timeline/
- iart motion design skills: https://github.com/iart-ai/motion-design-skills
- iart motion skills hub: https://github.com/iart-ai/motion-skills
- Charlie motion graphics skills: https://github.com/charlie947/motion-graphics-skills
- Barty motion graphics: https://github.com/Barty-Bart/motion-graphics
- WhisperX: https://github.com/m-bain/whisperX

### Observações de licença e manutenção

- Remotion informa licença gratuita para indivíduos e organizações com até 3 pessoas, sujeita aos termos; entidades que não se qualificam precisam da licença de empresa. Verificar elegibilidade da organização antes de uso comercial continuado. Não presumir que o fato de a ferramenta ser open source torna qualquer uso empresarial gratuito.
- HyperFrames é framework open source e usa HTML, GSAP e FFmpeg. Confirmar a licença da versão instalada e de cada asset/dependência.
- Repositórios de skills independentes podem mudar rapidamente. Conferir a data do último commit, LICENSE, scripts e SKILL.md no momento da instalação.
- Não instalar um pack inteiro se apenas uma skill for necessária. Não instalar plugins de sound design, captions automáticas, voiceover ou áudio reativo que exijam processamento da faixa original.
- Esta auditoria documental não instalou ferramentas no ambiente local de Claude Code. Instalação precisa ser feita e comprovada no ambiente de execução.

### Direção de arquitetura

1. Usar Remotion como primeira opção para cenas programáticas com React e componentes reutilizáveis, se licença e ambiente estiverem regulares.
2. Usar HyperFrames/HTML+GSAP quando timelines HTML, composição de camadas e inspeção visual forem mais adequadas.
3. Não manter dois projetos completos para a mesma peça sem razão técnica. Escolher um motor principal por Reel.
4. Usar FFmpeg/FFprobe como utilitário de inspeção, extração temporária de áudio, mux e export, não como substituto de direção criativa.
5. Usar skills de motion design como repertório de princípios e workflows, não como templates a aplicar mecanicamente.

## 3. Sincronização correta das legendas

### Princípio

O teleprompter aprovado determina o texto esperado. A gravação real determina o tempo e confirma o que foi efetivamente dito. ASR não é a fonte final do texto: é ferramenta para localizar palavras e timestamps.

### Pipeline obrigatório por RAW

1. Identificar o RAW por SG e confirmar visualmente que corresponde ao roteiro.
2. Guardar o RAW em local somente leitura ou calcular SHA-256 antes/depois para provar que não foi alterado.
3. Executar FFprobe para registrar duração, streams, codec, sample rate, frame rate e time base.
4. Extrair uma cópia temporária de áudio para análise, por exemplo WAV mono 16 kHz. Essa cópia é derivada descartável, não substitui o áudio original.
5. Executar ASR local e alinhamento forçado com ferramenta que suporte português brasileiro. WhisperX é uma opção candidata; validar modelo de alinhamento e idioma antes do lote.
6. Comparar transcrição reconhecida com o teleprompter aprovado. Não aceitar automaticamente texto reconhecido; detectar diferenças, omissões, repetições e palavras incertas.
7. Ouvir os trechos divergentes e ajustar timestamps manualmente. Se a palavra realmente falada diferir do teleprompter, não inventar: registrar e legendar somente a fala confirmada, preservando o sentido.
8. Gerar SRT/ASS com timestamps de entrada/saída reais. Dividir em blocos de uma linha, com velocidade de leitura confortável.
9. Aplicar Montserrat oficial e safe zones. Destacar palavras-chave sem sacrificar legibilidade.
10. Renderizar uma prévia, revisar começo/meio/fim e amostras em pontos de fala rápida, pausas e cortes.
11. Reproduzir o Reel inteiro em velocidade normal e validar sincronização.
12. Registrar ferramenta, versão/modelo, método, revisão humana e hash do RAW no manifesto de QA.

### Uso correto de FFmpeg

FFmpeg/FFprobe podem:
- inspecionar streams e metadados;
- extrair cópia temporária de áudio para ASR/alinhamento;
- extrair frames para inspeção visual;
- aplicar legendas como camada visual;
- compor cenas e exportar o vídeo;
- muxar a faixa original sem filtros, quando a arquitetura de edição permitir.

Não usar filtros de áudio, loudness normalization, denoise, EQ, compressor, limiter, pitch, time-stretch, voice isolation, restauração ou mixagem. Não substituir a faixa original pela cópia WAV de análise.

Quando a composição permitir, mapear a faixa original diretamente e usar cópia de áudio somente para análise. Se cortes de vídeo exigirem segmentação temporal da faixa, preservar segmentos originais sem filtros e sem alterar pitch/velocidade. Se a ferramenta não conseguir garantir isso, interromper apenas o Reel afetado e registrar a limitação em vez de processar o som silenciosamente.

### Critérios de aceite

- Texto correto segundo fala confirmada.
- Timestamps alinhados com início e fim reais das frases/palavras.
- Nenhuma legenda antecipa fala ou fica atrasada de forma perceptível.
- Sem palavras inventadas ou omitidas por erro do alinhador.
- Uma linha por vez, Montserrat, safe zones.
- Áudio original preservado.
- Vídeo completo reproduzido e conferido.

## 4. Direção do apresentador e motion full-screen

Não é obrigatório manter João visível durante toda a duração. O apresentador pode abrir a narrativa, reaparecer em pontos de autoridade e fechar com CTA; entre esses momentos, o vídeo pode migrar para motion/B-roll em tela cheia.

Cada bloco do storyboard deve escolher explicitamente um modo:
- PRESENTER: apresentador em plano íntegro, sem crop facial.
- FULLSCREEN_MOTION: cena gráfica independente, sem imagem do apresentador.
- BROLL_FULLSCREEN: mídia de apoio contextual em tela cheia.
- SPLIT/PIP: composição dividida quando melhora a explicação.

Regras:
- Não cortar testa, queixo ou laterais do rosto.
- Não usar o rosto como fundo obrigatório.
- Não colocar gráficos sobre olhos, nariz ou boca.
- Fazer transições intencionais para e da cena gráfica.
- Variar composição e ritmo; evitar uma sequência de talking head com textos soltos.
- Cada cena deve demonstrar a fala, não apenas repetir palavras.
- Usar motion complexo quando agrega clareza, surpresa ou demonstração; manter cenas simples quando a mensagem pede respiro.

## 5. Impressões Prontas: execução não opcional

A pasta oficial de entrada é:
`Meu Drive/02 - SUA GRÁFICA BH/CONTEÚDOS/07 - IMPRESSÕES PRONTAS/`

O ledger oficial é `REGISTRO-IMPRESSOES-PRONTAS.md`.

Em toda finalização de lote:
1. Listar/inventariar arquivos da pasta de entrada, excluindo totalmente `POSTADOS`.
2. Comparar cada arquivo com ledger por Drive ID, SHA-256 e/ou fingerprint visual.
3. Identificar conjuntos do mesmo trabalho (frente/verso, ângulos, detalhes e vídeos).
4. Verificar privacidade, autorização de exposição e fidelidade do produto.
5. Consultar CRM para qualquer especificação, prazo, preço, acabamento ou disponibilidade.
6. Escolher formato editorial mais adequado: estático, carrossel, Reel ou misto, respeitando compatibilidade do Postiz.
7. Criar ID SG global sequencial para cada conjunto editorial coerente e briefing individual no lote adequado.
8. Produzir, revisar e incluir no manifesto de entrega.
9. Não deixar arquivo elegível sem estado e motivo.
10. Mover originais para `POSTADOS` somente após publicação confirmada em todos os destinos previstos, seguindo o ledger.

Se Drive não estiver conectado, não alegar inventário concluído. Registrar bloqueio com caminho e continuar os demais itens possíveis.

## 6. Pasta plana de entrega ao Postiz

Ao concluir cada lote, criar a pasta plana definida em FLUXO-DE-ENTREGA-E-AGENDAMENTO-POSTIZ.md:

`Meu Drive/02 - SUA GRÁFICA BH/CONTEÚDOS/06 - PARA POSTIZ/LOTE-AAAA-MM-DD-a-AAAA-MM-DD/`

**A pasta deve ser plana:** todos os arquivos finais ficam diretamente na raiz. Não criar subpastas de Reels, Feed, Stories ou Impressões Prontas.

Incluir somente mídias finais aprovadas:
- MP4 final de cada Reel;
- capa independente de cada Reel;
- cada slide do Feed como arquivo individual e numerado;
- cada Story final;
- mídias finais das Impressões Prontas aprovadas;
- qualquer arquivo adicional estritamente necessário para publicação.

Excluir:
- RAWs;
- projetos-fonte;
- SRT/ASS intermediários;
- renders de teste;
- exports rejeitados;
- duplicatas;
- briefings e documentação;
- arquivos temporários.

### Nomenclatura

Exemplos:
- `SG-051_REEL_FINAL.mp4`
- `SG-051_REEL_CAPA.png`
- `SG-053_FEED_SLIDE-01.png`
- `SG-053_FEED_SLIDE-02.png`
- `SG-054_STORY_FINAL.png`

Para impressões prontas, usar o SG atribuído e sufixos de mídia/ordem. Nome deve ser único, estável e sem “final-final”.

### Manifesto fora da pasta plana

Manter manifesto de entrega no lote/repositório com ID SG, título, canal, tipo, arquivos exatos, ordem, status de aprovação, data prevista, origem da mídia, caminho do projeto-fonte e observações.

### Gate de entrega

- Confirmar pasta real no Drive.
- Confirmar todos os arquivos diretamente na raiz.
- Confirmar ausência de subpastas.
- Conferir quantidade e nomes únicos.
- Abrir os arquivos e validar formato/duração/resolução.
- Conferir sequência dos slides.
- Conferir manifesto contra a pasta.
- Confirmar que não há RAW/intermediário/duplicata.
- Só então marcar como PACOTE FINAL PRONTO PARA TRANSFERÊNCIA.

A pasta plana é o pacote para João fazer upload manual em lote na biblioteca Media do Postiz. Esse upload não agenda nem autoriza publicação. Claude só inicia o agendamento depois do comando explícito “Pode programar todos os conteúdos”, conforme FLUXO-DE-ENTREGA-E-AGENDAMENTO-POSTIZ.md.

## 7. Execução equilibrada

Classificar cada conteúdo:
- Nível 1: peça estática/demonstração simples com acabamento alto.
- Nível 2: motion explicativo, B-roll, tipografia cinética e múltiplas cenas.
- Nível 3: produção especial/cinematográfica com storyboard detalhado, composição avançada e animação sob medida.

O nível deve ser escolhido pelo objetivo e potencial editorial. Não simplificar um conteúdo que pede motion, nem acrescentar efeitos só para parecer sofisticado. O padrão é intenção, clareza, originalidade e acabamento.

## 8. QA e status

Renderizado não significa aprovado. Aprovado não significa agendado. Agendado não significa publicado.

Atualizar estado por SG e por destino com evidência. Continuar itens aptos mesmo quando outro estiver bloqueado. Não marcar pasta final pronta sem Drive real. Não arquivar originais antes da publicação confirmada.

## 9. Limites desta auditoria

A revisão do repositório e a pesquisa web não equivalem a instalar skills, renderizar vídeos, inspecionar arquivos RAW, acessar Brand Kit/Drive, executar QA audiovisual ou criar a pasta final. Essas tarefas dependem do ambiente de execução e dos conectores com acesso aos arquivos. Registrar execução somente quando houver evidência.
