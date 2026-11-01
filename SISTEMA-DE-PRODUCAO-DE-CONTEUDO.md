# Sistema de produção de conteúdo | SUA GRÁFICA BH

## Objetivo
Criar conteúdo que atraia empreendedores e potenciais clientes para a SUA GRÁFICA BH. O processo deve ser simples para João: receber um lote completo de conteúdos, gravar apenas os vídeos previstos, salvar a prancha visual no Drive e enviar os brutos. Claude fica responsável pela produção das artes finais, edição dos vídeos, revisão e agendamento/distribuição dos materiais aptos.

## Fontes oficiais e responsabilidades
- **CRM oficial** (`ABauerlab/crm-sua-grafica-bh`): fonte de verdade para identidade visual, catálogo ativo, especificações e informações comerciais.
- **Este repositório**: fonte de verdade para estratégia editorial, pesquisa, pautas, roteiros, referências, briefings, padrões de edição e aprendizados.
- **Google Drive**: armazenamento dos arquivos brutos, projetos de edição, exports finais e referências.
- **ChatGPT:** pesquisa, estratégia, seleção de pautas, roteiros, copy, briefings de todas as peças e prancha visual de referência por lote.
- **João:** grava os roteiros e envia os arquivos para a pasta de brutos.
- **Claude Code:** consulta este repositório e o Brand Kit, produz artes finais, edita os vídeos gravados, revisa os arquivos e agenda/distribui os itens aptos pelo Postiz.
- **Postiz:** publicação orgânica nos canais conectados da marca: Instagram, Facebook e Threads.

Não adicionar n8n, banco de dados, servidores de renderização ou outros serviços ao fluxo enquanto as integrações já disponíveis no Claude forem suficientes.

## Fluxo operacional
1. **Pesquisa e estratégia:** pesquisar oportunidades, dores, tendências e referências; definir o mix de vídeos, carrosséis, posts estáticos e Stories conforme o objetivo.
2. **Planejamento:** escrever roteiros, copy, estrutura slide a slide, CTAs, legendas e briefings de produção.
3. **Direção visual:** ChatGPT gera uma prancha visual de referência para o lote que inclua artes. João salva a imagem em `Meu Drive/02 - SUA GRÁFICA BH/CONTEÚDOS/05 - REFERÊNCIAS/`, com os IDs no nome do arquivo.
4. **Registro:** atribuir ID sequencial `SG-XXX`, criar um arquivo individual por conteúdo em `conteudos/` e atualizar `CALENDARIO.md`.
5. **Gravação:** João grava somente os conteúdos que exigem vídeo e usa o ID no nome de cada arquivo.
6. **Upload:** João envia os brutos para `Meu Drive/02 - SUA GRÁFICA BH/CONTEÚDOS/01 - VÍDEOS BRUTOS/`.
7. **Comando ao Claude:** João envia o comando único com os IDs exatos do lote.
8. **Produção:** Claude consulta cada briefing, confere a prancha visual e o Brand Kit, produz as artes finais e edita os vídeos cuja correspondência por ID seja clara.
9. **Revisão:** Claude abre cada arte e cada slide; reproduz cada vídeo; confere qualidade, textos, identidade, catálogo, direitos e adequação aos canais.
10. **Distribuição:** os materiais aptos são agendados/distribuídos pelo Postiz conforme calendário e canais que estiverem efetivamente conectados. Adaptar legenda, CTA e formato por canal.
11. **Registro:** Claude registra status, data, canal, links/IDs e pendências no calendário e no arquivo individual, quando tiver acesso.
12. **Aprendizado:** resultados disponíveis orientam os próximos temas, ganchos, formatos e prioridades.

## Pesquisa e integridade
- Separar evidência, interpretação e hipótese.
- Concorrentes são referências de mercado, nunca fonte oficial sobre produtos ou condições da SUA GRÁFICA BH.
- Não inventar fontes, links, autores, datas ou métricas.
- Encontrar a origem de um vídeo não significa ter autorização para reutilização comercial.
- Respeitar licenças, autorizações, créditos e identificadores de terceiros.

## Regras para roteiros
- Entregar o texto falado isolado, pronto para teleprompter.
- Não misturar falas com indicações de cena, pausas ou notas técnicas.
- Usar linguagem brasileira, natural e conversada.
- Criar gancho imediato, preferencialmente nos primeiros 1–2 segundos.
- Variar temas, ângulos, formatos e objetivos.
- Não forçar venda em toda pauta.
- Confirmar no CRM qualquer produto, preço, prazo, especificação, disponibilidade ou condição comercial citada.
- Não prometer viralização, vendas ou resultados garantidos.

## Formato de entrega do ChatGPT
Para cada conteúdo, entregar briefing individual com ID, formato, objetivo, público, etapa do funil, hipótese, conceito, gancho, conteúdo final, CTA, legendas por canal, fontes e instrução de execução.

- **Vídeo:** incluir roteiro e teleprompter isolado (somente falas), ficha de gravação e briefing de edição.
- **Carrossel:** incluir copy completa de cada slide, função narrativa e direção visual por página.
- **Post estático:** incluir texto final, hierarquia e direção de arte.
- **Stories:** incluir sequência, texto, CTA e direção visual.
- **Prancha visual:** gerar uma por lote que contenha artes, mapear os quadros aos IDs e orientar João a colocá-la na pasta `CONTEÚDOS/05 - REFERÊNCIAS/` do Drive.

## Google Drive
Raiz: `Meu Drive/02 - SUA GRÁFICA BH/CONTEÚDOS/`
- `01 - VÍDEOS BRUTOS/`: gravações originais; nunca apagar ou sobrescrever.
- `02 - EM EDIÇÃO/`: projetos e versões em andamento.
- `03 - APROVADOS/`: exports finais revisados.
- `04 - PUBLICADOS/`: cópias finais e materiais publicados.
- `05 - REFERÊNCIAS/`: referências e assets autorizados/licenciados.

Não renomear, mover ou apagar pastas existentes sem autorização. Se uma integração não permitir determinada ação, informar e usar a alternativa disponível sem alegar sucesso.

## Nomenclatura
Usar o mesmo ID em todas as etapas:
- Roteiro: `conteudos/SG-XXX-titulo-curto.md`
- Bruto: `SG-XXX - TÍTULO DO VÍDEO.mp4`
- Projeto: `SG-XXX - TÍTULO DO VÍDEO`
- Export: `SG-XXX - TÍTULO DO VÍDEO - FINAL.mp4`

O ID é permanente. Títulos podem mudar sem alterar o ID. Takes adicionais recebem sufixos `-take-02`, `-take-03`.

## Comando padrão e execução em lote
O comando reutilizável oficial está em `PROMPT-UNICO-CLAUDE.md`. João informa os IDs SG exatos do lote depois de colocar os brutos e a prancha visual no Drive.

Claude executa somente os briefings desses IDs: produz carrosséis slide a slide, posts estáticos, Stories e capas; edita vídeos com bruto correspondente; revisa, organiza e agenda/distribui os itens aptos pelo Postiz. O comando autoriza execução sem aprovação individual para cada peça que passar integralmente pelo controle de qualidade.

- Não criar pauta, copy, roteiro ou conteúdo substituto quando o briefing já está completo.
- Não processar conteúdos fora dos IDs informados.
- Não produzir nem publicar material sem briefing, confirmação comercial ou direitos resolvidos.
- Verificar o histórico do Postiz para evitar duplicidade.
- Se uma peça falhar, pausar somente aquele ID e continuar os demais aptos.
- Se o Postiz falhar em um canal, registrar a falha daquele canal. Não declarar publicação concluída sem confirmação.
- Agendar conforme calendário e briefing; não inventar data/horário como se fossem dados comprovados.
- Não aguardar 24 horas com o processo aberto para Trial Reels; registrar status e tratar a avaliação posterior como etapa separada.
## Controle de qualidade
- Fala fiel à gravação e ao roteiro.
- Gancho claro e ritmo que preserve entendimento.
- Legendas corretas, legíveis e dentro da área segura.
- Áudio limpo, sem clipping; música licenciada abaixo da voz.
- Cortes e transições sem prejudicar a compreensão.
- Identidade visual e assets oficiais respeitados.
- Informações comerciais confirmadas no CRM.
- Direitos e créditos preservados.
- Export reproduzido antes da distribuição.

## Status
IDEIA → PESQUISA → ROTEIRO PRONTO → PRONTO PARA GRAVAR → GRAVADO → EM EDIÇÃO → FINALIZADO → AGENDADO → PUBLICADO → ANALISADO.

Estados adicionais: PENDENTE DE ROTEIRO, PENDENTE DE REFERÊNCIA, PENDENTE DE DIREITOS, PENDENTE DE CATÁLOGO, ERRO DE EDIÇÃO e ERRO DE PUBLICAÇÃO.


## Regra de escopo e economia de execução
O planejamento, a pesquisa, a copy, os roteiros e a direção criativa já são responsabilidade do ChatGPT. Claude não deve recriar essas etapas quando houver briefing completo. Ele executa os IDs informados no comando, produz as artes finais, edita os vídeos gravados, faz o controle de qualidade e agenda/distribui os itens aptos. Se faltar um arquivo essencial, pausa somente aquele ID e não inventa conteúdo substituto.

A prancha visual gerada no ChatGPT precisa ser transferida por João para a pasta sincronizada do Drive indicada neste documento; não presumir que um arquivo desta conversa aparece automaticamente no ambiente do Claude.