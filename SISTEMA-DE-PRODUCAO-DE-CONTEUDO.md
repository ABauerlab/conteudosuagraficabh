# Sistema de produção de conteúdo | SUA GRÁFICA BH

## Objetivo
Criar conteúdo que atraia empreendedores e potenciais clientes para a SUA GRÁFICA BH. O processo deve ser simples para João: receber roteiros prontos, gravar os vídeos e enviar os arquivos brutos. Claude fica responsável pela edição, revisão e distribuição dos materiais aptos.

## Fontes oficiais e responsabilidades
- **CRM oficial** (`ABauerlab/crm-sua-grafica-bh`): fonte de verdade para identidade visual, catálogo ativo, especificações e informações comerciais.
- **Este repositório**: fonte de verdade para estratégia editorial, pesquisa, pautas, roteiros, referências, briefings, padrões de edição e aprendizados.
- **Google Drive**: armazenamento dos arquivos brutos, projetos de edição, exports finais e referências.
- **ChatGPT:** pesquisa de mercado, estratégia, seleção de pautas e roteiros para teleprompter.
- **João:** grava os roteiros e envia os arquivos para a pasta de brutos.
- **Claude Code:** consulta este repositório, edita os vídeos gravados, revisa os exports e distribui pelo Postiz.
- **Postiz:** publicação orgânica nos canais conectados da marca: Instagram, Facebook e Threads.

Não adicionar n8n, banco de dados, servidores de renderização ou outros serviços ao fluxo enquanto as integrações já disponíveis no Claude forem suficientes.

## Fluxo operacional
1. **Pesquisa:** pesquisar tendências, formatos, concorrentes, dúvidas e dores do público. Registrar fontes, datas e evidências.
2. **Roteiro:** criar texto natural, curto e pronto para teleprompter, separado de cenas e instruções.
3. **Registro:** atribuir ID sequencial `SG-XXX`, criar arquivo em `conteudos/` e atualizar `CALENDARIO.md`.
4. **Gravação:** João grava cada roteiro em arquivo separado, usando o mesmo ID no nome.
5. **Upload:** João envia os vídeos para `Meu Drive/02 - SUA GRÁFICA BH/CONTEÚDOS/01 - VÍDEOS BRUTOS/`.
6. **Comando ao Claude:** João solicita o processamento de todos os vídeos da pasta de brutos.
7. **Correspondência:** Claude identifica cada vídeo pelo ID e localiza o roteiro/briefing correspondente. Itens ambíguos ou sem roteiro ficam pendentes.
8. **Edição:** Claude edita conforme o briefing e `PADROES-DE-EDICAO.md`, preservando o sentido das falas e os arquivos originais.
9. **Revisão:** Claude reproduz e confere cada export, incluindo áudio, imagem, cortes, legendas, ortografia, enquadramento e identidade visual.
10. **Distribuição:** os vídeos que passarem na revisão são distribuídos pelo Postiz nos canais conectados: Instagram, Facebook e Threads. Adaptar legenda, CTA e formato conforme cada canal.
11. **Registro:** Claude registra status, data, canal e links/IDs retornados pelo Postiz no calendário e no arquivo individual, quando tiver acesso de escrita.
12. **Aprendizado:** resultados disponíveis orientam os próximos temas, ganchos e formatos.

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
Para cada vídeo, entregar:
1. **Ficha de produção:** ID, título, objetivo, público, hipótese, duração estimada, formato, CTA, legenda, fontes e briefing para edição.
2. **Teleprompter:** bloco isolado contendo exclusivamente as falas.

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

## Comando padrão para Claude
“Claude, processe todos os vídeos disponíveis em `Meu Drive/02 - SUA GRÁFICA BH/CONTEÚDOS/01 - VÍDEOS BRUTOS/`. Consulte o repositório `ABauerlab/conteudosuagraficabh`, encontre o roteiro de cada vídeo pelo ID e siga integralmente as instruções, briefings e padrões de edição. Edite todos os vídeos que tiverem correspondência clara, revise e reproduza cada export para garantir a qualidade. Salve os arquivos finais em `03 - APROVADOS/`. Depois de conferir legenda, CTA e adequação por canal, distribua os conteúdos aprovados pelo Postiz nos canais conectados: Instagram, Facebook e Threads. Não publique duplicatas. Preserve todos os brutos. Registre o que foi editado, agendado ou publicado e informe pendências e falhas. Não invente informações nem declare ações que não foram confirmadas.”

## Execução em lote e publicação automática
- O comando de processamento em lote autoriza Claude a editar e publicar os vídeos que passarem integralmente pelo controle de qualidade, sem pedir aprovação individual de cada vídeo.
- Não publicar arquivos sem roteiro correspondente, com divergência material, com informação comercial pendente ou com problema de direitos.
- Não publicar exports que não tenham sido reproduzidos e conferidos.
- Verificar o histórico do Postiz para evitar duplicidade.
- Se um vídeo falhar, pausar somente aquele item e continuar os demais aptos.
- Se o Postiz falhar em um canal, registrar a falha daquele canal. Não declarar publicação concluída sem confirmação.
- Não criar automações ou infraestrutura externa para executar o fluxo; usar as integrações e ferramentas já conectadas ao Claude.

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
