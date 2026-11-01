# Estrutura de conteúdos

Cada lote fica em uma subpasta `lote-AAAA-MM-DD-a-AAAA-MM-DD/`. Dentro de cada lote, separar obrigatoriamente os conteúdos por formato:

- `FEED/`: carrosséis e posts estáticos. Um arquivo Markdown por publicação.
- `STORIES/`: um arquivo Markdown por Story individual.
- `REELS/`: um arquivo Markdown por Reel.
- `README.md`: índice do lote, calendário resumido, totais, IDs e status.

Padrão de exemplo:

```text
conteudos/
└── lote-AAAA-MM-DD-a-AAAA-MM-DD/
    ├── README.md
    ├── FEED/
    │   ├── SG-049.md
    │   └── SG-052.md
    ├── STORIES/
    │   ├── SG-050.md
    │   └── SG-053.md
    └── REELS/
        └── SG-051.md
```

Um conteúdo = um ID SG = um arquivo Markdown individual, dentro da pasta correspondente ao formato. É proibido agrupar vários conteúdos em um arquivo diário, temático ou por faixa de IDs. IDs são sequenciais e globais dentro do ciclo editorial vigente. Se João autorizar explicitamente reiniciar a numeração, o próximo lote começa em SG-001. Não reiniciar por iniciativa própria. Atualizar `CALENDARIO.md` e o README do lote. Antes de declarar conclusão, conferir a árvore do GitHub, contagem, pastas e correspondência entre ID, formato e arquivo.
