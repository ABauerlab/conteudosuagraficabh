# Projeto Remotion | Reels SG-025 a SG-044 e posts SG-049/SG-050

Fonte editável (React + Remotion 4.0.542) do motion dos Reels do lote 10 a 13/11/2026 e dos posts adicionais de impressões prontas.

- `src/reel/`: motor de edição dos Reels. `Reel.tsx` monta apresentador (tela cheia, punch-in ancorado no rosto e janela circular nas cenas de motion, sem cobrir o rosto), gancho em texto, palavras-chave, cenas (`list`, `steps`, `compare`, `statement`, `strike`, `cta`), legendas Montserrat em uma linha e trilha Pixabay com fade. `types.ts` descreve o mapa fala → cena.
- `src/data/`: um arquivo por Reel com cortes, legendas sincronizadas e mapa de motion. **Vazio nesta versão**: a transcrição com tempos por palavra não pôde ser executada (ver auditoria do lote), então nenhum Reel foi montado.
- `src/stills/ImpressaoPronta.tsx`: post estático das fotos de `07 - IMPRESSÕES PRONTAS` (composições `SG-049-FEED` e `SG-050-FEED`).
- `scripts/transcrever.mjs`: transcrição local com whisper.cpp (modelo medium, pt).

## Ativos não versionados
- Brand Kit (logotipos, faixa CMYK, fundo gradiente, ícones): copiar de `Meu Drive/02 - SUA GRÁFICA BH/IDENTIDADE VISUAL/SUA_GRAFICA_BH_BRANDKIT/` para `public/brand/` sem alteração.
- Fotos: `public/fotos/tags.jpg` e `cartao.jpg`, convertidas dos HEIC originais (cópias; os originais não são alterados).
- Trilhas: `public/music/`, baixadas do Pixabay (registro em `TRILHAS-PIXABAY.md`).
- Vídeos montados: `public/media/` (cópias dos brutos; nunca os originais).

## Uso
    npm install
    npx remotion still src/index.ts SG-049-FEED out/SG-049-FEED-01.png
    npx remotion render src/index.ts SG-025 out/SG-025-REEL-1080x1920.mp4 --codec h264

Fontes: Montserrat (legendas) e Inter (fonte oficial do Brand Kit) via `@remotion/google-fonts`.
