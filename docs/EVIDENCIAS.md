# Registro de evidências — situação em 26/10/2026

## Confirmado pela usuária nos testes locais

| Evidência | Origem | Interpretação |
|---|---|---|
| Modelo KD-55X705G; software v7.931-4.000-0103 | Foto da TV | Identificação concreta do alvo |
| Navegador identifica Opera 36 / Chromium 49 e Linux ARMv7 | Página de diagnóstico local | Informações do User-Agent; requerem validação independente |
| HTML e JavaScript funcionam | Página local | Aplicações web simples possíveis |
| MP4 e HLS reproduziram | Página local | Reprodução de mídia básica possível, não atesta DRM |
| Streamings testados não reproduziram; YouTube acusou navegador antigo | Teste direto | Incompatibilidade com serviços web atuais, causas específicas ainda não isoladas |
| Serviço DLNA MediaRenderer relatado | Teste local anterior; dados da rede omitidos | Serviço UPnP de reprodução |
| XML informa RenderingControl, ConnectionManager e AVTransport | Leitura de XML anunciada pelo dispositivo | Não representa gerenciador/instalador de apps |
| Ausência de resposta em um conjunto limitado de testes TCP anteriores | Relato local; portas e endereços omitidos | Não demonstra ausência de serviços nem segurança da TV |

## Confirmado em documentação oficial pública

- Sony lista KD-55X705G entre modelos aplicáveis ao firmware 7.931 e informa nome do ZIP `sony_tvupdate_2017_7931_bff_auth.zip`, tamanho **294.094.077 bytes**, data **14/02/2023**.
  <https://www.sony.com.br/electronics/support/lcd-tvs-xg70xx_x70xxg-series/kd-43x705g/software/00273647>
- Sony disponibiliza código-fonte de alguns componentes de código aberto: <https://oss.sony.net/Products/Linux/TV/KD-55X705G.html>. Isso não equivale ao firmware completo ou a uma API de instalação.

## Não comprovado

- Acesso administrativo ou execução de código nativo no Linux.
- Possibilidade de instalar aplicativo próprio, loja de apps ou atualizar o navegador.
- Suporte a Widevine/PlayReady com licenças válidas ou certificação de streamings.
- Estrutura ou conteúdo do arquivo ZIP oficial (ainda não analisado pelo projeto).

**Disciplina:** ao acrescentar informação, anotar se é observação empírica, referência externa ou hipótese e fornecer comandos reproduzíveis.

## Preparação local para publicação — 26/10/2026

- Observação local: não existia repositório Git inicializado na pasta ao iniciar esta etapa.
- Observação local: o ZIP `sony_tvupdate_2017_7931_bff_auth.zip` estava ausente. Havia um arquivo `.pkg` em `firmware/`; ele não foi inspecionado, executado ou incluído no Git nesta etapa.
- Os relatos de testes na TV acima foram herdados da documentação; não foram repetidos nesta etapa. As referências oficiais acima também não foram consultadas novamente.
- Endereços e detalhes da rede pessoal foram removidos da documentação destinada à publicação. Firmware, relatórios locais, pacotes e capturas estão cobertos pelo `.gitignore`.
- A preparação para GitHub não constitui análise do firmware nem evidência de instalação de aplicativos. Ainda não há inventário ou relatório do ZIP real.
- Validação local: os quatro testes existentes passaram com o Python 3.12.14 do runtime do aplicativo e `TEMP`/`TMP` apontando para `.tmp/` no projeto. O comando `py -3` não encontrou instalação registrada nesta máquina; a primeira tentativa com o runtime esbarrou em permissões da pasta temporária padrão. Nenhuma dependência foi instalada.
- Publicação autorizada explicitamente pela pessoa proprietária. A API do GitHub confirmou o repositório público `PedroAndrad3/Free-My-Sony`, com branch padrão `main`, tamanho informado de zero e permissão de escrita da conta conectada. Essa consulta externa se limita à publicação autorizada; nenhum firmware foi enviado.
