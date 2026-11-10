import React from 'react';
import {
  AbsoluteFill,
  Img,
  OffthreadVideo,
  Audio,
  interpolate,
  spring,
  staticFile,
  useCurrentFrame,
  useVideoConfig,
  Easing,
} from 'remotion';
import {C, FPS, H, INTER, MONTSERRAT, W} from './theme';
import type {Beat, Caption, PanelItem, ReelData} from './types';

const sec = (f: number) => f / FPS;

// Progresso suave de entrada/saída de um intervalo [from, to] (0..1).
function window01(t: number, from: number, to: number, ramp = 0.33) {
  if (t < from - ramp || t > to + ramp) return 0;
  const a = interpolate(t, [from - ramp, from], [0, 1], {extrapolateLeft: 'clamp', extrapolateRight: 'clamp', easing: Easing.out(Easing.cubic)});
  const b = interpolate(t, [to, to + ramp], [1, 0], {extrapolateLeft: 'clamp', extrapolateRight: 'clamp', easing: Easing.in(Easing.cubic)});
  return Math.min(a, b);
}

const PIP = {x: 330, y: 120, size: 420, k: 0.56};

/* ---------------- Apresentador ---------------- */
const Presenter: React.FC<{data: ReelData; t: number}> = ({data, t}) => {
  const panels = data.beats.filter((b) => b.kind === 'panel');
  const p = Math.max(0, ...panels.map((b) => window01(t, b.from, b.to, 0.35)));
  const zooms = data.beats.filter((b) => b.kind === 'zoom') as Extract<Beat, {kind: 'zoom'}>[];
  const z = 1 + Math.max(0, ...zooms.map((b) => window01(t, b.from, b.to, 0.25) * ((b.scale ?? 1.14) - 1)));
  // Leve deriva de câmera para o plano não ficar estático (máx. 2%).
  const drift = 1 + 0.02 * Math.sin(t / 6);

  const {x: fx, y: fy} = data.face;
  // Retângulo do contêiner: tela cheia -> janela.
  const cx = interpolate(p, [0, 1], [0, PIP.x]);
  const cy = interpolate(p, [0, 1], [0, PIP.y]);
  const cw = interpolate(p, [0, 1], [W, PIP.size]);
  const ch = interpolate(p, [0, 1], [H, PIP.size]);
  const radius = interpolate(p, [0, 1], [0, PIP.size / 2]);
  // Vídeo interno: escala e deslocamento para manter o rosto centrado na janela.
  const kFull = z * drift;
  const k = interpolate(p, [0, 1], [kFull, PIP.k]);
  const leftFull = fx - fx * kFull;
  const topFull = fy - fy * kFull;
  const left = interpolate(p, [0, 1], [leftFull, PIP.size / 2 - fx * PIP.k]);
  const top = interpolate(p, [0, 1], [topFull, PIP.size / 2 - fy * PIP.k]);

  return (
    <div
      style={{
        position: 'absolute',
        left: cx,
        top: cy,
        width: cw,
        height: ch,
        overflow: 'hidden',
        borderRadius: radius,
        boxShadow: p > 0.01 ? `0 0 0 ${10 * p}px ${C.branco}, 0 20px 60px rgba(0,0,0,${0.35 * p})` : undefined,
        zIndex: 5,
      }}
    >
      <OffthreadVideo
        src={staticFile(`media/${data.video}`)}
        startFrom={Math.round(data.start * FPS)}
        style={{position: 'absolute', left, top, width: W * k, height: H * k}}
      />
    </div>
  );
};

/* ---------------- Fundo das cenas ---------------- */
const PanelBg: React.FC<{t: number; data: ReelData}> = ({t, data}) => {
  const panels = data.beats.filter((b) => b.kind === 'panel') as Extract<Beat, {kind: 'panel'}>[];
  const active = panels.find((b) => t >= b.from - 0.35 && t <= b.to + 0.35);
  if (!active) return null;
  const o = window01(t, active.from, active.to, 0.35);
  const escuro = active.theme === 'escuro';
  return (
    <AbsoluteFill style={{opacity: o, zIndex: 2}}>
      {escuro ? (
        <Img src={staticFile('brand/elemento_05_fundo_gradiente_escuro.jpg')} style={{width: W, height: H, objectFit: 'cover'}} />
      ) : (
        <AbsoluteFill style={{background: C.off}} />
      )}
      <Img
        src={staticFile('brand/elemento_03_faixa_cmyk.png')}
        style={{position: 'absolute', left: 0, bottom: 0, width: W, height: 22}}
      />
    </AbsoluteFill>
  );
};

/* ---------------- Gancho ---------------- */
const Hook: React.FC<{b: Extract<Beat, {kind: 'hook'}>; t: number}> = ({b, t}) => {
  const {fps} = useVideoConfig();
  const o = window01(t, b.from, b.to, 0.2);
  if (o <= 0) return null;
  return (
    <div style={{position: 'absolute', left: 70, right: 70, top: 200, zIndex: 8, display: 'flex', flexDirection: 'column', alignItems: 'flex-start', gap: 14, opacity: o}}>
      {b.lines.map((line, i) => {
        const s = spring({frame: Math.round((t - b.from) * fps) - i * 5, fps, config: {damping: 14, stiffness: 140}});
        const words = line.split(' ');
        return (
          <div
            key={i}
            style={{
              transform: `translateY(${(1 - s) * 40}px)`,
              opacity: s,
              background: C.branco,
              color: C.preto,
              fontFamily: INTER,
              fontWeight: 900,
              fontSize: 58,
              letterSpacing: '-0.02em',
              lineHeight: 1.05,
              padding: '14px 26px',
              borderRadius: 16,
              boxShadow: '0 12px 40px rgba(0,0,0,.25)',
            }}
          >
            {words.map((w, j) => (
              <span key={j} style={{color: b.mark && w.toLowerCase().includes(b.mark.toLowerCase()) ? C.magenta : undefined}}>
                {w}
                {j < words.length - 1 ? ' ' : ''}
              </span>
            ))}
          </div>
        );
      })}
    </div>
  );
};

/* ---------------- Palavra-chave sobre o apresentador ---------------- */
const KeyWord: React.FC<{b: Extract<Beat, {kind: 'word'}>; t: number}> = ({b, t}) => {
  const {fps} = useVideoConfig();
  const o = window01(t, b.from, b.to, 0.15);
  if (o <= 0) return null;
  const s = spring({frame: Math.round((t - b.from) * fps), fps, config: {damping: 11, stiffness: 160}});
  const bg = b.color ?? C.amarelo;
  return (
    <div style={{position: 'absolute', left: 0, right: 0, top: b.y ?? 330, display: 'flex', justifyContent: 'center', zIndex: 8, opacity: o}}>
      <div
        style={{
          transform: `scale(${0.6 + 0.4 * s}) rotate(${(1 - s) * -4}deg)`,
          background: bg,
          color: bg === C.amarelo ? C.preto : C.branco,
          fontFamily: INTER,
          fontWeight: 900,
          fontSize: b.text.length > 14 ? 64 : 84,
          letterSpacing: '-0.02em',
          maxWidth: 940,
          textAlign: 'center',
          lineHeight: 1.05,
          padding: '12px 34px',
          borderRadius: 18,
          boxShadow: '0 14px 40px rgba(0,0,0,.3)',
          textTransform: 'uppercase',
        }}
      >
        {b.text}
      </div>
    </div>
  );
};

/* ---------------- Cenas de motion ---------------- */
const Item: React.FC<{it: PanelItem; t: number; idx: number; escuro: boolean; numbered?: boolean; accent: string}> = ({it, t, idx, escuro, numbered, accent}) => {
  const {fps} = useVideoConfig();
  const s = spring({frame: Math.round((t - it.at) * fps), fps, config: {damping: 15, stiffness: 150}});
  if (t < it.at - 0.05) return <div style={{height: 104}} />;
  return (
    <div style={{display: 'flex', alignItems: 'center', gap: 26, transform: `translateX(${(1 - s) * -60}px)`, opacity: s, marginBottom: 22}}>
      <div
        style={{
          width: 82,
          height: 82,
          flex: '0 0 82px',
          borderRadius: 41,
          background: accent,
          color: accent === C.amarelo ? C.preto : C.branco,
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'center',
          fontFamily: INTER,
          fontWeight: 900,
          fontSize: 42,
        }}
      >
        {it.icon ? <Img src={staticFile(`brand/${it.icon}`)} style={{width: 56, height: 56}} /> : numbered ? idx + 1 : '✓'}
      </div>
      <div style={{fontFamily: INTER, fontWeight: 800, fontSize: 52, lineHeight: 1.1, color: escuro ? C.branco : C.preto, letterSpacing: '-0.01em'}}>{it.text}</div>
    </div>
  );
};

const ACCENTS = [C.magenta, C.ciano, C.amarelo];

const Panel: React.FC<{b: Extract<Beat, {kind: 'panel'}>; t: number}> = ({b, t}) => {
  const {fps} = useVideoConfig();
  const o = window01(t, b.from, b.to, 0.3);
  if (o <= 0) return null;
  const escuro = b.theme === 'escuro';
  const txt = escuro ? C.branco : C.preto;
  const st = spring({frame: Math.round((t - b.from) * fps), fps, config: {damping: 16, stiffness: 120}});
  const title = b.title ? (
    <div style={{fontFamily: INTER, fontWeight: 900, fontSize: 70, lineHeight: 1.04, letterSpacing: '-0.025em', color: txt, marginBottom: 44, transform: `translateY(${(1 - st) * 30}px)`, opacity: st}}>
      {b.title}
    </div>
  ) : null;

  let body: React.ReactNode = null;
  if (b.variant === 'list' || b.variant === 'steps') {
    body = (b.items ?? []).map((it, i) => (
      <Item key={i} it={it} t={t} idx={i} escuro={escuro} numbered={b.variant === 'steps'} accent={ACCENTS[i % ACCENTS.length]} />
    ));
  } else if (b.variant === 'compare') {
    const col = (side: {label: string; items: PanelItem[]}, accent: string) => (
      <div style={{flex: 1, background: escuro ? 'rgba(255,255,255,.08)' : C.branco, borderRadius: 26, padding: 28, border: `5px solid ${accent}`}}>
        <div style={{fontFamily: INTER, fontWeight: 900, fontSize: 46, color: accent === C.amarelo ? txt : accent, marginBottom: 20, textTransform: 'uppercase'}}>{side.label}</div>
        {side.items.map((it, i) => {
          const s = spring({frame: Math.round((t - it.at) * fps), fps, config: {damping: 15}});
          return t < it.at - 0.05 ? null : (
            <div key={i} style={{fontFamily: INTER, fontWeight: 700, fontSize: 38, lineHeight: 1.15, color: txt, marginBottom: 16, opacity: s, transform: `translateY(${(1 - s) * 20}px)`}}>
              {it.text}
            </div>
          );
        })}
      </div>
    );
    body = (
      <div style={{display: 'flex', gap: 24}}>
        {b.left && col(b.left, C.cinza)}
        {b.right && col(b.right, C.magenta)}
      </div>
    );
  } else if (b.variant === 'statement' || b.variant === 'strike') {
    body = (
      <div>
        {(b.items ?? []).map((it, i) => {
          const s = spring({frame: Math.round((t - it.at) * fps), fps, config: {damping: 12, stiffness: 150}});
          if (t < it.at - 0.05) return null;
          const strike = b.variant === 'strike' && i < (b.items?.length ?? 0) - 1;
          const cut = interpolate(t, [it.at + 0.5, it.at + 0.85], [0, 1], {extrapolateLeft: 'clamp', extrapolateRight: 'clamp'});
          return (
            <div key={i} style={{position: 'relative', display: 'table', marginBottom: 18, transform: `scale(${0.7 + 0.3 * s})`, opacity: s, transformOrigin: 'left center'}}>
              <span
                style={{
                  fontFamily: INTER,
                  fontWeight: 900,
                  fontSize: 76,
                  letterSpacing: '-0.025em',
                  color: strike ? (escuro ? C.cinza : '#6b6b6b') : txt,
                  background: !strike && i === (b.items?.length ?? 0) - 1 ? C.amarelo : undefined,
                  padding: !strike && i === (b.items?.length ?? 0) - 1 ? '0 14px' : undefined,
                  borderRadius: 10,
                  ...(!strike && i === (b.items?.length ?? 0) - 1 ? {color: C.preto} : {}),
                }}
              >
                {it.text}
              </span>
              {strike ? (
                <div style={{position: 'absolute', left: 0, top: '52%', height: 10, width: `${cut * 100}%`, background: C.magenta, borderRadius: 5}} />
              ) : null}
            </div>
          );
        })}
      </div>
    );
  } else if (b.variant === 'cta') {
    const pulse = 1 + 0.03 * Math.sin((t - b.from) * 6);
    body = (
      <div style={{display: 'flex', flexDirection: 'column', alignItems: 'center', gap: 40}}>
        {b.icon ? <Img src={staticFile(`brand/${b.icon}`)} style={{width: 170, height: 170, transform: `scale(${st})`}} /> : null}
        <div
          style={{
            background: C.magenta,
            color: C.branco,
            fontFamily: INTER,
            fontWeight: 900,
            fontSize: 64,
            lineHeight: 1.1,
            textAlign: 'center',
            padding: '30px 44px',
            borderRadius: 26,
            transform: `scale(${st * pulse})`,
          }}
        >
          {(b.items ?? []).map((i) => i.text).join(' ')}
        </div>
        <Img src={staticFile(escuro ? 'brand/sua_grafica_bh_logo_horizontal_colorido_fundo_escuro.png' : 'brand/sua_grafica_bh_logo_horizontal_colorido_fundo_claro.png')} style={{width: 560, opacity: st}} />
      </div>
    );
  }

  return (
    <div style={{position: 'absolute', left: 80, right: 80, top: b.variant === 'cta' ? 700 : 640, zIndex: 6, opacity: o}}>
      {b.variant === 'cta' ? null : title}
      {b.variant === 'cta' && b.title ? (
        <div style={{fontFamily: INTER, fontWeight: 900, fontSize: 64, textAlign: 'center', color: txt, marginBottom: 36, letterSpacing: '-0.02em'}}>{b.title}</div>
      ) : null}
      {body}
    </div>
  );
};

/* ---------------- Legendas: Montserrat, uma linha ---------------- */
const Captions: React.FC<{caps: Caption[]; t: number}> = ({caps, t}) => {
  const c = caps.find((x) => t >= x.start && t < x.end);
  if (!c) return null;
  const local = t - c.start;
  const s = interpolate(local, [0, 0.12], [0.85, 1], {extrapolateRight: 'clamp'});
  const keys = (c.keys ?? []).map((k) => k.toLowerCase());
  const words = c.text.split(' ');
  return (
    <div style={{position: 'absolute', left: 60, right: 60, top: 1500, display: 'flex', justifyContent: 'center', zIndex: 20}}>
      <div
        style={{
          whiteSpace: 'nowrap',
          fontFamily: MONTSERRAT,
          fontWeight: 800,
          fontSize: 52,
          color: C.branco,
          background: 'rgba(23,23,23,.78)',
          padding: '10px 26px 12px',
          borderRadius: 14,
          transform: `scale(${s})`,
        }}
      >
        {words.map((w, i) => (
          <span key={i} style={{color: keys.includes(w.toLowerCase().replace(/[.,!?:;]/g, '')) ? C.amarelo : undefined}}>
            {w}
            {i < words.length - 1 ? ' ' : ''}
          </span>
        ))}
      </div>
    </div>
  );
};

/* ---------------- Assinatura discreta ---------------- */
const Signature: React.FC<{t: number; data: ReelData}> = ({t, data}) => {
  // Some durante cenas de motion, gancho e palavras-chave (mesma área superior).
  const panelOn = data.beats.some((b) => (b.kind === 'panel' || b.kind === 'hook' || b.kind === 'word') && t >= b.from - 0.3 && t <= b.to + 0.3);
  return (
    <Img
      src={staticFile('brand/sua_grafica_bh_logo_horizontal_colorido_fundo_claro.png')}
      style={{position: 'absolute', left: 70, top: 90, width: 260, zIndex: 9, opacity: panelOn ? 0 : 0.95, filter: 'drop-shadow(0 2px 6px rgba(0,0,0,.25))'}}
    />
  );
};

export const Reel: React.FC<{data: ReelData}> = ({data}) => {
  const frame = useCurrentFrame();
  const {durationInFrames} = useVideoConfig();
  const t = sec(frame);
  const total = sec(durationInFrames);
  const musicVol = (f: number) => {
    const tt = sec(f);
    const fadeIn = interpolate(tt, [0, 0.8], [0, 1], {extrapolateRight: 'clamp'});
    const fadeOut = interpolate(tt, [total - 1.6, total], [1, 0], {extrapolateLeft: 'clamp', extrapolateRight: 'clamp'});
    // Trilha sobe levemente só no encerramento sem fala.
    const tailUp = interpolate(tt, [data.duration, data.duration + 0.4], [1, 1.8], {extrapolateLeft: 'clamp', extrapolateRight: 'clamp'});
    return data.music.volume * fadeIn * fadeOut * tailUp;
  };

  return (
    <AbsoluteFill style={{background: C.preto}}>
      <Audio src={staticFile(`music/${data.music.file}`)} volume={musicVol} />
      <PanelBg t={t} data={data} />
      <Presenter data={data} t={t} />
      <Signature t={t} data={data} />
      {data.beats.map((b, i) =>
        b.kind === 'hook' ? <Hook key={i} b={b} t={t} /> : b.kind === 'word' ? <KeyWord key={i} b={b} t={t} /> : b.kind === 'panel' ? <Panel key={i} b={b} t={t} /> : null,
      )}
      <Captions caps={data.captions} t={t} />
    </AbsoluteFill>
  );
};
