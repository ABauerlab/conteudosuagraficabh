// Tipos do motor de edição dos Reels SUA GRÁFICA BH.
// Todos os tempos estão em segundos na linha do tempo da montagem (após cortes de pausas).

export type Word = {text: string; start: number; end: number};

export type Caption = {text: string; start: number; end: number; keys?: string[]};

export type PanelItem = {text: string; at: number; icon?: string};

export type Beat =
  // Gancho em texto (não falado), visível no início com João em tela cheia.
  | {kind: 'hook'; from: number; to: number; lines: string[]; mark?: string}
  // Punch-in motivado em palavra de ênfase; ancorado no rosto.
  | {kind: 'zoom'; from: number; to: number; scale?: number}
  // Palavra/expressão-chave sobre o apresentador (tipografia cinética).
  | {kind: 'word'; from: number; to: number; text: string; color?: string; y?: number}
  // Cena de motion em tela cheia; João vai para janela (rosto sempre visível).
  | {
      kind: 'panel';
      from: number;
      to: number;
      variant: 'list' | 'steps' | 'compare' | 'statement' | 'cta' | 'strike';
      title?: string;
      items?: PanelItem[];
      left?: {label: string; items: PanelItem[]};
      right?: {label: string; items: PanelItem[]};
      theme?: 'claro' | 'escuro';
      icon?: string;
    };

export type ReelData = {
  id: string;
  video: string; // arquivo em public/media (cópia de trabalho do bruto)
  start: number; // segundos cortados do início do bruto (silêncio antes da primeira fala)
  duration: number; // segundos da montagem
  tail: number; // segundos extras de encerramento
  face: {x: number; y: number}; // âncora do rosto no quadro 1080x1920
  captions: Caption[];
  beats: Beat[];
  music: {file: string; volume: number};
};
