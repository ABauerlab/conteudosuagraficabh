# Execução resiliente de mídia e distribuição | SUA GRÁFICA BH

## Objetivo e contrato operacional

O fluxo oficial é simples: **João grava e envia os brutos; Claude localiza, edita, finaliza, produz as artes, faz QA e agenda pelo Postiz MCP conectado.** João não deve operar navegador, transferir manualmente arquivos entre serviços, gerar links públicos, instalar ferramentas ou fornecer credenciais novas quando os acessos existentes forem suficientes.

Este documento resolve falhas operacionais recorrentes. Ele não substitui os padrões criativos, de identidade, direitos ou qualidade; define como continuar o trabalho quando uma ferramenta falha.

## Princípios inegociáveis

1. **MCP conectado é o caminho primário.** Usar as ferramentas reais do Google Drive e Postiz MCP disponíveis no ambiente Claude. Descobrir seus nomes e schemas no início da execução; não presumir nomes de ferramentas.
2. **Não trocar MCP por navegador sem motivo.** Não pedir login manual, não depender de aba aberta, Ctrl+Shift+B, postMessage, DevTools ou sessão de navegador como fluxo normal. Navegador é contingência excepcional, não requisito do processo.
3. **Não pedir links públicos.** Brutos e exports devem permanecer privados. Não tornar o Drive público nem usar o GitHub público como CDN de mídia de cliente.
4. **Uma falha não para o lote.** Isolar a falha no ID/formato/canal afetado e continuar tudo que estiver apto.
5. **Não instalar dependência pesada como primeira tentativa.** Inspecionar o ambiente e reutilizar ferramentas e modelos já disponíveis.
6. **Não inventar sucesso.** Só marcar upload, agendamento ou publicação depois de confirmação retornada pelo Postiz e conferência do registro.
7. **Persistir checkpoints.** Cada etapa concluída deve ser registrada para que uma interrupção ou limite de execução não faça o trabalho recomeçar do zero.

## 1. Inicialização e descoberta das integrações

No início de cada lote:

1. Ler AGENTS.md, PROMPT-UNICO-CLAUDE.md, OPERACAO-DE-CONTEUDO.md, este documento e os padrões especializados do formato.
2. Verificar ferramentas MCP realmente conectadas no ambiente atual. Descobrir as ações de:
   - Google Drive: listar pasta, obter metadados, baixar/exportar arquivo e, se aplicável, enviar arquivo.
   - Postiz: listar publicações/fila, enviar mídia, criar/agendar publicação, consultar publicação e obter status/ID.
3. Verificar autenticação com uma operação somente de leitura e de baixo impacto. Nunca imprimir tokens, cookies, headers secretos ou valores de ambiente.
4. Registrar no estado do lote quais integrações responderam, quais ações estão disponíveis e qual método será usado.
5. Se uma ferramenta MCP estiver ausente, não fingir que está conectada. Procurar apenas alternativas já configuradas e autorizadas no ambiente. Não solicitar uma nova credencial antes de confirmar que a existente não pode ser reutilizada.

**Postiz:** o MCP conectado é a interface primária de distribuição. Usar o MCP para consultar fila, enviar mídia e agendar. Não substituir por navegador/API paralela só porque uma função de consulta falhou. Se o MCP não expuser uma ação necessária, verificar a documentação/implementação da integração e as credenciais já configuradas no ambiente; somente então registrar a lacuna específica.

## 2. Localização e download dos brutos no Google Drive

Localizar a pasta oficial de vídeos brutos e mapear arquivos por ID SG, nome, tamanho, MIME type, data e file ID. Não depender apenas do nome do arquivo; confirmar correspondência com briefing.

Ordem de acesso:

1. Google Drive MCP: listar a pasta e baixar o arquivo pelo file ID, usando a ação de download/exportação disponível.
2. Se o conector limitar o tamanho do download, verificar se ele oferece exportação por stream, download em partes, URL autenticada temporária ou outra ação própria. Não repetir a mesma tentativa que já falhou.
3. Verificar se a pasta do Drive está sincronizada/montada no ambiente local (Drive for desktop, volume ou diretório de trabalho já existente).
4. Verificar ferramentas de sincronização já instaladas e autenticadas (por exemplo, rclone ou cliente Google Drive), sem imprimir ou copiar credenciais. Usar somente a conta e o escopo já autorizados.
5. Se nenhuma rota autorizada funcionar, registrar o ID do arquivo, tamanho, limite exato e métodos testados. Pedir intervenção somente para aquele arquivo e continuar os demais.

**Proibido como solução padrão:** mudar permissão para “qualquer pessoa com o link”, copiar mídia para repositório público, solicitar upload manual repetido ou afirmar que o arquivo está indisponível só porque um conector tem limite de tamanho.

Preservar o original. Baixar para pasta de trabalho identificada por lote/SG, validar tamanho e, quando possível, checksum. Não sobrescrever nem mover o bruto original.

## 3. Transcrição e compatibilidade de CPU

Transcrição serve para conferir o que foi realmente falado e sincronizar legendas. Não pode virar bloqueio global de todo o lote.

Ordem de tentativa:

1. Reutilizar ferramenta/modelo de transcrição já instalado e funcional.
2. Detectar CPU e recursos suportados antes de escolher binário. Não presumir AVX2. Em processadores sem AVX2, selecionar build compatível com a arquitetura (por exemplo, baseline/SSE/AVX apropriado) ou compilar a ferramenta a partir do código-fonte oficial com flags compatíveis, se os compiladores já estiverem disponíveis.
3. Para Whisper local, começar por modelo multilíngue leve (tiny ou base) para validar o fluxo e o idioma; só aumentar o modelo se a qualidade estiver insuficiente. Não baixar automaticamente modelos gigantes (por exemplo, 1,5 GB) antes de testar uma opção menor.
4. Se o download do modelo for interrompido, retomar do ponto existente quando suportado; não apagar e reiniciar nem manter processos em espera indefinida.
5. Se a execução automática bloquear um binário baixado, não repetir downloads da mesma build. Preferir ferramenta já instalada ou build reproduzível a partir de fonte oficial. Validar origem e checksum quando fornecidos.
6. Se houver serviço de transcrição externo já autorizado e configurado, confirmar que o uso e o envio de gravações estão cobertos pela autorização existente. Não enviar vídeos privados a serviço novo nem criar conta/chave sem autorização.

Após transcrever, comparar a transcrição com o teleprompter/briefing e ouvir trechos relevantes. Corrigir nomes, números, negações, CTA e palavras que mudem o sentido. Não usar o roteiro como se fosse transcrição literal sem conferência.

Se nenhum método de transcrição funcionar:
- Continuar artes, carrosséis, Stories, organização e distribuição dos itens já aprovados.
- Para cada Reel, tentar revisão por reprodução/escuta em blocos menores com as ferramentas disponíveis.
- Não inventar fala nem sincronizar legenda por estimativa. Se não for possível confirmar o texto falado, marcar somente aquele Reel como PENDENTE DE TRANSCRIÇÃO, registrar o motivo e seguir os demais.
- Não transformar essa pendência localizada em motivo para interromper o lote inteiro.

## 4. Edição de vídeo e execução por etapas

Antes de instalar qualquer pacote, modelo ou binário:

1. Inventariar versões de Node, FFmpeg, Remotion, Python, codecs, fontes e ferramentas já disponíveis.
2. Abrir o projeto-fonte existente do lote e reutilizar componentes/configurações que funcionaram. Não recriar o motor de edição a cada execução.
3. Testar um Reel representativo em baixa resolução/trecho curto antes de renderizar todos.
4. Renderizar em lotes pequenos, salvar logs e validar saída antes de avançar.
5. Se Remotion falhar, diagnosticar a causa e corrigir; não trocar automaticamente por um fluxo opaco que descarte a fonte JS/TS.
6. Se um efeito, asset ou dependência não funcionar, substituir por solução visual equivalente e fiel à fala. Não inserir elementos genéricos apenas para preencher.
7. Tratar áudio conforme PADROES-DE-EDICAO.md: diagnóstico primeiro, processamento moderado, A/B em volume equivalente, preservar a voz natural e reverter o que piorar.

Não manter downloads ou renders longos sem checkpoint. Não deixar um processo em segundo plano sem registrar PID/saída, finalidade e forma de retomada.

## 5. Artes e arquivos finais

Produzir capas, carrosséis, Stories e estáticos a partir dos briefings e do Brand Kit oficial. Cada arquivo precisa ter ID SG e nome previsível.

Antes do upload:
- conferir dimensões, formato, peso, transparência quando aplicável e perfil de cor;
- abrir todas as imagens e revisar em tamanho real e escala de celular;
- conferir ortografia, contraste, margens, identidade, ordem dos slides, CTA e correspondência com o briefing;
- manter fontes editáveis e exports separados;
- não incluir marcas de clientes sem autorização registrada.

## 6. Distribuição obrigatória pelo Postiz MCP

A sequência padrão de distribuição é:

1. Consultar a fila/histórico pelo Postiz MCP para detectar duplicidade por ID, conteúdo, canal e janela de publicação.
2. Confirmar os destinos conectados e os formatos suportados em cada canal.
3. Enviar os arquivos finais pelo recurso de upload de mídia do Postiz MCP, preferindo arquivo local/bytes ou file path quando suportado.
4. Se o MCP aceitar somente URL, não presumir que o GitHub raw ou um link privado do Drive seja apropriado. Procurar o mecanismo oficial de upload de mídia do próprio Postiz ou a ação de upload exposta pela integração, autenticada pela sessão/credencial já conectada.
5. Criar/agendar cada publicação com mídia, legenda, canal, data e horário definidos no calendário.
6. Consultar novamente cada publicação e confirmar ID do Postiz, canal, formato, mídia, ordem, data/hora local e estado retornado.
7. Registrar separadamente cada destino. Uma publicação no Instagram não confirma Facebook ou Threads.

**Não usar como dependência:**
- navegador logado manualmente;
- ponte postMessage entre páginas;
- endpoint interno descoberto por tentativa sem documentação/validação;
- chave OpenAI de um agente de consulta como se fosse a chave da API de publicação;
- URL pública temporária criada apenas para contornar upload;
- upload por GitHub público de vídeos ou artes com dados de clientes.

Se a consulta da fila falhar, diferenciar:
- falha da ferramenta/agente de consulta;
- falha de autenticação do MCP;
- falha do endpoint de listagem;
- falha de upload;
- falha de criação/agendamento.

Tentar outra ação de leitura do próprio Postiz MCP ou consultar publicação individual pelos IDs já conhecidos. Não concluir que a publicação falhou só porque a busca da fila falhou. Não agendar às cegas quando não for possível verificar duplicidade; primeiro recuperar leitura por outro método autorizado. Nunca pedir chave nova sem comprovar que a autenticação existente está ausente/inválida.

## 7. Compatibilidade por canal

Não presumir que Instagram, Facebook e Threads aceitam os mesmos formatos ou recursos.

- Adaptar legenda, limite de caracteres, mídia, sequência, hashtags e CTA por canal.
- Stories: confirmar suporte real do canal/conector. Se Facebook Story não for oferecido, registrar apenas esse destino como PENDENTE DE RECURSO DE PLATAFORMA; não bloquear Instagram.
- Enquetes, stickers, música nativa e outros recursos interativos: não alegar que foram publicados se o Postiz não os suportar. Registrar a limitação por publicação.
- Threads: validar limite atual de texto e mídia; adaptar a copy, sem truncar silenciosamente.
- Carrosséis: confirmar ordem e quantidade de arquivos recebidos em cada canal.
- Publicação adicional (impressões prontas): seguir o ledger e a cadência aprovada; não inventar horários.

## 8. Checkpoints e retomada após interrupção

Manter um arquivo de estado por lote em execucao/ESTADO-LOTE-AAAA-MM-DD-a-AAAA-MM-DD.md (ou dentro da pasta do lote, se ela já existir). Atualizar após cada etapa significativa.

Campos mínimos:
- lote e IDs do escopo;
- branch e último commit;
- arquivos brutos encontrados/baixados e método;
- status de transcrição por Reel;
- status de edição/render por Reel;
- artes produzidas e QA;
- mídias enviadas ao Postiz e IDs/URLs retornados;
- publicações por canal com IDs, data/hora e estado;
- erros, tentativas realizadas e próximo passo exato;
- itens concluídos, pendentes e não iniciados.

Ao retomar:
1. Ler o estado e o último commit antes de agir.
2. Verificar se os arquivos e agendamentos já existem.
3. Reutilizar downloads, transcrições, renders e uploads válidos.
4. Não repetir uploads/agendamentos já confirmados.
5. Continuar do primeiro item incompleto.
6. Não recomeçar o lote por causa de limite de contexto, sessão ou ferramenta.

## 9. Quando pedir ajuda a João

Só escalar quando a ação realmente depender do responsável:
- gravação ausente, corrompida ou sem correspondência possível;
- decisão comercial ou autorização de uso de imagem/marca;
- acesso/credencial inexistente ou revogada, depois de verificar as conexões existentes;
- conflito de calendário que não possa ser resolvido pelas regras já aprovadas.

Não pedir login no navegador, link público, instalação de ferramenta, transcrição manual, escolha de trilha, revisão básica ou geração de chave se Claude puder resolver com os recursos conectados.

Se houver bloqueio real, informar o ID afetado, a evidência, o que já foi tentado, o impacto e a única ação necessária. Continuar o restante do lote.

## 10. Critério de conclusão

O lote só é concluído quando todos os IDs do escopo estão classificados e todas as etapas autorizadas foram executadas ou têm pendência individual documentada. Distinguir:
- produzido;
- editado;
- revisado/QA;
- aprovado;
- enviado ao Postiz;
- agendado;
- publicado.

O relatório final deve ser curto, com contagens, links/caminhos reais, IDs de agendamento, destinos confirmados e bloqueios restantes. Nunca chamar “agendado” de “publicado” nem “upload” de “agendamento”.
