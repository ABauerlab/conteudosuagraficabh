import React from 'react';
import {AbsoluteFill, Img, staticFile} from 'remotion';
import {C, INTER} from '../reel/theme';

// Post estático adicional (rotina 07 - IMPRESSÕES PRONTAS): uma foto real = um post.
// A foto entra sem alteração de conteúdo (apenas recorte de enquadramento); identidade
// com logotipo oficial do Brand Kit, Inter e paleta oficial.
export type ImpressaoProps = {
  foto: string; // em public/fotos
  posY: string; // enquadramento vertical do recorte (object-position)
  etiqueta: string;
  titulo: string;
  destaque: string; // trecho do título realçado
  apoio: string;
};

export const ImpressaoPronta: React.FC<ImpressaoProps> = ({foto, posY, etiqueta, titulo, destaque, apoio}) => {
  const [antes, depois] = titulo.split(destaque);
  return (
    <AbsoluteFill style={{background: C.off, fontFamily: INTER}}>
      <div style={{position: 'absolute', left: 60, top: 60, width: 960, height: 900, borderRadius: 36, overflow: 'hidden', boxShadow: '0 18px 50px rgba(0,0,0,.18)'}}>
        <Img src={staticFile(`fotos/${foto}`)} style={{width: '100%', height: '100%', objectFit: 'cover', objectPosition: `50% ${posY}`}} />
        <div style={{position: 'absolute', left: 30, top: 30, background: C.amarelo, color: C.preto, fontWeight: 800, fontSize: 26, letterSpacing: '0.18em', padding: '12px 20px', borderRadius: 12, textTransform: 'uppercase'}}>
          Foto real
        </div>
      </div>
      <div style={{position: 'absolute', left: 70, top: 1000, display: 'flex', gap: 0}}>
        {[C.ciano, C.magenta, C.amarelo, C.preto].map((c) => (
          <i key={c} style={{display: 'block', width: 70, height: 10, background: c}} />
        ))}
      </div>
      <div style={{position: 'absolute', left: 70, top: 1028, fontWeight: 500, fontSize: 24, letterSpacing: '0.3em', textTransform: 'uppercase', color: C.preto}}>{etiqueta}</div>
      <div style={{position: 'absolute', left: 70, right: 70, top: 1068, fontWeight: 900, fontSize: 60, lineHeight: 1.04, letterSpacing: '-0.025em', color: C.preto}}>
        {antes}
        <span style={{background: C.magenta, color: C.branco, padding: '0 12px', borderRadius: 10, WebkitBoxDecorationBreak: 'clone', boxDecorationBreak: 'clone'}}>{destaque}</span>
        {depois}
      </div>
      <div style={{position: 'absolute', left: 70, right: 420, bottom: 64, fontWeight: 600, fontSize: 28, lineHeight: 1.25, color: '#3a3a3a'}}>{apoio}</div>
      <Img src={staticFile('brand/sua_grafica_bh_logo_horizontal_colorido_fundo_claro.png')} style={{position: 'absolute', right: 70, bottom: 70, width: 320}} />
    </AbsoluteFill>
  );
};
