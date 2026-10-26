# Plano de investigação

## Fase 0 — concluída: caracterização não invasiva

- [x] Modelo, firmware e navegador declarados.
- [x] HTML/JavaScript, MP4 e HLS funcionais em servidor local.
- [x] Streamings comerciais via VEWD não funcionaram.
- [x] DLNA MediaRenderer relatado em testes anteriores; os serviços observados são de mídia, não instalação. Dados da rede pessoal omitidos.

## Fase 1 — preparada: inspeção do firmware offline

- [x] Criar ferramenta com inventário ZIP, assinaturas iniciais, hash SHA-256, amostra de entropia.
- [x] Criar testes sintéticos.
- [ ] Receber o ZIP de firmware oficial 7.931, sem enviá-lo ao GitHub.
- [ ] Executar inventário real e documentar tamanho, hashes e membros.
- [ ] Identificar (ou registrar como não identificado) formato do payload interno.

## Fase 2 — somente após a fase 1

- [ ] Ler documentação dos componentes OSS Sony relevantes ao modelo.
- [ ] Determinar se é possível inspecionar metadados de volumes/partições sem executar código.
- [ ] Procurar apenas sinais não sensíveis de arquitetura: sistema de arquivos, componente VEWD/Opera, framework UI, serviço de instalação.
- [ ] Classificar bloqueios: assinatura, criptografia, falta de runtime, ausência de SDK e compatibilidade DRM.

## Fase 3 — decisão de engenharia

- [ ] Avaliar evidência de um mecanismo de instalação de terceiros; documentar certeza e risco.
- [ ] Comparar alternativa web personalizada, DLNA/espelhamento e dispositivo HDMI externo.
- [ ] Concluir de modo honesto se instalar streaming comercial é viável.

**Fora do escopo:** modificar firmware, criar imagem de flash, burlar proteções de conteúdo, explorar portas de rede, alterar armazenamento da TV.

## Colaboração pública

- [x] Preparar README, licença MIT, guia de contribuição e modelos de Issues.
- [x] Configurar workflow de testes sintéticos para Windows e Linux, sem firmware.
- [x] Remover endereços e detalhes da rede pessoal da documentação pública e ampliar exclusões do Git.
- [x] Reproduzir os quatro testes existentes com o Python do runtime do aplicativo e uma pasta temporária local.
- [x] Repositório público `PedroAndrad3/Free-My-Sony` criado pela pessoa proprietária; publicação de código e documentação autorizada explicitamente.
- [x] Publicar o código e a documentação revisados no repositório.
- [x] Confirmar a execução dos testes no GitHub Actions após a publicação: quatro combinações aprovadas em Windows/Linux e Python 3.9/3.13, no commit `66007fb`.
