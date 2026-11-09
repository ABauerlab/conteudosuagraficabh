# Fonte editável das artes | SG-025 a SG-048

- `pecas.js`: copy e composição de cada peça, idêntica aos briefings individuais.
- `render.js`: renderiza em Chromium (Playwright) com Inter e o logotipo oficial do Brand Kit.

Uso, com os arquivos `logo_h_claro.png` e `logo_h_escuro.png` do Brand Kit em `<brandkit>`:

    NODE_PATH=$(npm root -g) node render.js <brandkit> <saida>

Exports aprovados no QA: `midia/exports/lote-2026-11-10-a-2026-11-13/` (com SHA256SUMS.txt).
O logotipo não fica versionado aqui: a fonte oficial é exclusivamente o Brand Kit no Drive.
