import {loadFont as loadMontserrat} from '@remotion/google-fonts/Montserrat';
import {loadFont as loadInter} from '@remotion/google-fonts/Inter';

// Legendas: Montserrat (regra permanente de PADROES-DE-EDICAO.md).
export const {fontFamily: MONTSERRAT} = loadMontserrat('normal', {weights: ['600', '700', '800'], subsets: ['latin', 'latin-ext']});
// Motion e títulos: Inter, fonte oficial do Brand Kit (cores_e_fontes_tokens.json).
export const {fontFamily: INTER} = loadInter('normal', {weights: ['500', '600', '800', '900'], subsets: ['latin', 'latin-ext']});

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
