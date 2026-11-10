import {loadFont} from '@remotion/fonts';
import {staticFile} from 'remotion';

// Fontes servidas localmente (public/fonts, pacotes @fontsource, licença SIL OFL),
// para o render não depender de acesso ao Google Fonts.
const faces: Array<[string, string, string]> = [];
for (const w of ['600', '700', '800']) {
  for (const s of ['latin', 'latin-ext']) faces.push(['Montserrat', w, `fonts/montserrat-${s}-${w}-normal.woff2`]);
}
for (const w of ['500', '600', '800', '900']) {
  for (const s of ['latin', 'latin-ext']) faces.push(['Inter', w, `fonts/inter-${s}-${w}-normal.woff2`]);
}
for (const [family, weight, file] of faces) {
  loadFont({family, url: staticFile(file), weight, style: 'normal'});
}

// Legendas: Montserrat (regra permanente de PADROES-DE-EDICAO.md).
export const MONTSERRAT = 'Montserrat';
// Motion e títulos: Inter, fonte oficial do Brand Kit (cores_e_fontes_tokens.json).
export const INTER = 'Inter';

// Paleta oficial (Brand Kit: IDENTIDADE_VISUAL/cores_e_fontes_tokens.json).
export const C = {
  ciano: '#00A6D6',
  magenta: '#E6007E',
  amarelo: '#FFD500',
  preto: '#171717',
  branco: '#FFFFFF',
  off: '#F7F7F4',
  cinza: '#A7A7A7',
};

export const FPS = 30;
export const W = 1080;
export const H = 1920;
