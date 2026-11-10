# Projeto Remotion | Reels SG-025 a SG-044 e posts SG-049/SG-050

Fonte editável (React + Remotion 4.0.542) do motion dos Reels do lote 10 a 13/11/2026 e dos posts adicionais de impressões prontas.

- `src/reel/`: motor de edição dos Reels. `Reel.tsx` monta apresentador (tela cheia, punch-in ancorado no rosto e janela circular nas cenas de motion, sem cobrir o rosto), gancho em texto, palavras-chave, cenas (`list`, `steps`, `compare`, `statement`, `strike`, `cta`), legendas Montserrat em uma linha e trilha Pixabay com fade. `types.ts` descreve o mapa fala → cena.
- `src/data/`: um arquivo por Reel (`SG-xxx.ts`) com corte inicial, legendas e mapa fala → motion. Gerados em 10/11/2026 por `scripts/gen.py` **sem transcrição**: o teleprompter do briefing é distribuído pela fala real usando só a detecção de pausas (`silencedetect`, análise; o áudio não é alterado) e a contagem de sílabas, com finais de frase ancorados em pausas reais. Legendas só nos Reels cujos finais de frase ficaram ancorados (SG-026, 031, 037, 043); nos demais (SG-025, 032, 038, 044) a fala é contínua demais para garantir a sincronia, então a legenda foi omitida e o motion tipográfico foi mantido.
- `src/stills/ImpressaoPronta.tsx`: post estático das fotos de `07 - IMPRESSÕES PRONTAS` (composições `SG-049-FEED` e `SG-050-FEED`).
- `scripts/transcrever.mjs`: legado. A transcrição foi proibida pelas regras de 10/11/2026 (PROMPT-UNICO-CLAUDE.md); não usar.
- `scripts/align.py`, `scripts/sents.py`, `scripts/gen.py`: alinhamento por pausas e geração dos mapas.

## Ativos não versionados
- Brand Kit (logotipos, faixa CMYK, fundo gradiente, ícones): copiar de `Meu Drive/02 - SUA GRÁFICA BH/IDENTIDADE VISUAL/SUA_GRAFICA_BH_BRANDKIT/` para `public/brand/` sem alteração.
- Fotos: `public/fotos/tags.jpg` e `cartao.jpg`, convertidas dos HEIC originais (cópias; os originais não são alterados).
- Trilhas: `public/music/`, baixadas do Pixabay (registro em `TRILHAS-PIXABAY.md`).
- Vídeos montados: `public/media/` (cópias dos brutos; nunca os originais).

## Uso
    npm install
    npx remotion still src/index.ts SG-049-FEED out/SG-049-FEED-01.png
    npx remotion render src/index.ts SG-025 out/SG-025-REEL-1080x1920.mp4 --codec h264

Fontes: Montserrat (legendas) e Inter (fonte oficial do Brand Kit), servidas localmente de `public/fonts/` (copiar de `node_modules/@fontsource/*/files/`).

Render sem acesso a remotion.media: `--browser-executable=<chromium local>`.
