// Transcrição local (whisper.cpp, modelo medium, pt) com tempos por palavra.
// Uso: node scripts/transcrever.mjs <pasta-wav-16k> <pasta-saida> SG-025 SG-026 ...
import {transcribe, toCaptions} from '@remotion/install-whisper-cpp';
import fs from 'node:fs';
import path from 'node:path';

const [wavDir, outDir, ...ids] = process.argv.slice(2);
fs.mkdirSync(outDir, {recursive: true});
for (const id of ids) {
  const out = await transcribe({
    inputPath: path.join(wavDir, `${id}.wav`),
    whisperPath: path.join(process.cwd(), 'whisper.cpp'),
    whisperCppVersion: '1.5.5',
    model: 'medium',
    language: 'pt',
    tokenLevelTimestamps: true,
    splitOnWord: true,
    printOutput: false,
  });
  const {captions} = toCaptions({whisperCppOutput: out});
  const words = captions
    .map((c) => ({text: c.text.trim(), start: c.startMs / 1000, end: c.endMs / 1000}))
    .filter((w) => w.text.length > 0);
  fs.writeFileSync(path.join(outDir, `${id}.json`), JSON.stringify({id, text: out.transcription.map((s) => s.text).join(' ').trim(), words}, null, 1));
  console.log(id, words.length, 'palavras');
}
