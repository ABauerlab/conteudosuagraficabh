import React from 'react';
import {Composition, Still} from 'remotion';
import {Reel} from './reel/Reel';
import {FPS, W, H} from './reel/theme';
import {reels} from './data';
import {ImpressaoPronta} from './stills/ImpressaoPronta';

export const RemotionRoot: React.FC = () => (
  <>
    {reels.map((r) => (
      <Composition
        key={r.id}
        id={r.id}
        component={Reel}
        width={W}
        height={H}
        fps={FPS}
        durationInFrames={Math.round((r.duration + r.tail) * FPS)}
        defaultProps={{data: r}}
      />
    ))}
    <Still
      id="SG-049-FEED"
      component={ImpressaoPronta}
      width={1080}
      height={1350}
      defaultProps={{
        foto: 'tags.jpg',
        posY: '72%',
        etiqueta: 'Impressão pronta · Tags',
        titulo: 'Frente com a marca. Verso com o tamanho.',
        destaque: 'Verso com o tamanho.',
        apoio: 'Tags que acabaram de sair da produção, prontas para acompanhar as peças.',
      }}
    />
    <Still
      id="SG-050-FEED"
      component={ImpressaoPronta}
      width={1080}
      height={1350}
      defaultProps={{
        foto: 'cartao.jpg',
        posY: '55%',
        etiqueta: 'Impressão pronta · Cartão de visita',
        titulo: 'Marca na frente. QR code e site no verso.',
        destaque: 'QR code e site no verso.',
        apoio: 'Cartões que acabaram de sair da produção, prontos para entregar ao cliente.',
      }}
    />
  </>
);
