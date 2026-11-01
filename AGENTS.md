# Instruções para assistentes de IA | SUA GRÁFICA BH

Este é o repositório especializado de conteúdo da SUA GRÁFICA BH. Ele trabalha em conjunto com o CRM oficial, que é a fonte de verdade para informações operacionais, catálogo e identidade técnica da marca.

## Hierarquia de fontes entre repositórios
1. CRM oficial: https://github.com/ABauerlab/crm-sua-grafica-bh
2. Repositório de conteúdo: https://github.com/ABauerlab/conteudosuagraficabh

O CRM é a fonte de verdade para identidade visual oficial, catálogo atual, disponibilidade/vendabilidade, especificações, preços, prazos, condições comerciais e regras operacionais. Este repositório é a fonte de verdade para estratégia editorial, roteiros, referências, calendário, edição e desempenho.

## Antes de qualquer tarefa
1. Leia este arquivo, `DIRETRIZES.md` e `ESTRATEGIA.md`.
2. Consulte os documentos relevantes do CRM antes de criar conteúdo que mencione identidade visual, produtos, disponibilidade, características, preços, prazos ou condições:
   - `src/lib/brand.ts` para tokens de cor usados no sistema.
   - `docs/catalogo-e-sku.md` para entender o catálogo, os limites de acesso e as regras de sigilo.
   - `docs/conhecimento.md` e `docs/agente/00-contexto.md` para contexto comercial e regras do atendimento, quando pertinentes.
   - `docs/redes-sociais.md` para o contexto de distribuição e integrações.
   - Consultar a tela/fonte oficial do catálogo no CRM, com acesso autorizado, quando precisar confirmar produtos ativos, especificações e disponibilidade atual. A documentação técnica não substitui a consulta aos dados atuais.
3. Consulte os documentos editoriais deste repositório para pautas, ganchos, referências e roteiros.
4. Confira `CALENDARIO.md` e `conteudos/` para evitar repetição.
5. Leia `ANALISE-DE-DESEMPENHO.md` antes de usar resultados anteriores.

## Regra de segurança do catálogo
- O catálogo comercial do CRM é a autoridade sobre o que pode ser anunciado.
- Nunca copiar para este repositório custos, margens, pisos, preços internos, tabelas do fornecedor, SKUs internos, credenciais, dados privados ou exportações do catálogo.
- O SKU é interno e não deve aparecer em conteúdo público.
- Não assumir que uma categoria de interesse está disponível para venda. Confirmar que o produto está ativo e vendável no catálogo autorizado.
- Se não houver acesso ao catálogo atual ou a confirmação estiver incompleta, marcar a informação como PENDENTE e não publicar como fato.
- Não inventar preço, prazo, estoque, especificação, acabamento, gramatura, quantidade mínima ou diferencial.

## Regra de pesquisa antes de roteiro
- Se o formato for react, comentário, tela dividida ou fundo verde baseado em vídeo externo, pesquisar e localizar primeiro a publicação original.
- Preferir link direto do Instagram quando o original estiver publicado lá e puder ser verificado.
- Entregar link, perfil/criador e plataforma. Confirmar que o conteúdo corresponde à descrição.
- Só então entregar o roteiro final para teleprompter.
- Se não localizar o original, declarar a busca inconclusiva e não apresentar o roteiro dependente daquela referência como pronto para gravar.
- Para conteúdo original sem vídeo externo, entregar briefing visual para Claude.
- Nunca inventar links, fontes, autores, datas ou status de autorização.

## Direitos e integridade
- Encontrar a origem não significa ter autorização para reutilização comercial.
- Verificar licença, autorização ou outra base legítima aplicável.
- Nunca remover marcas d'água, créditos, nomes ou identificadores para ocultar autoria.
- Diferenciar original, repost, alternativa e banco licenciado.

## Sistema de conteúdo
- Cada pauta recebe ID sequencial SG-001, SG-002 etc. e arquivo próprio em `conteudos/`.
- Atualize `CALENDARIO.md` quando status mudar.
- Registre cada referência em `REFERENCIAS.md`.
- Use `templates/ROTEIRO.md` para cada vídeo.
- Registre aprendizados e métricas disponíveis após publicação.
- Verifique duplicações e preserve mudanças do outro assistente.

## Padrão criativo
- Gancho forte nos primeiros 1–2 segundos.
- Linguagem natural, conversada e fácil de falar em voz alta.
- Roteiros curtos, normalmente 15–20 segundos quando a ideia permitir.
- Vender sem parecer venda: conteúdo primeiro, conexão com a gráfica de forma natural.
- Otimizar para atrair empreendedores e potenciais clientes, não apenas views.
- Não prometer viralização.

## Entrega e colaboração
Ao concluir alterações, informar arquivos modificados e commit. Se algum repositório ou dado não puder ser consultado, declarar isso claramente. Nunca alegar sincronização que não aconteceu.
