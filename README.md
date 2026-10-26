# Free My Sony — Sony KD-55X705G

Investigação aberta de firmware: [PedroAndrad3/Free-My-Sony](https://github.com/PedroAndrad3/Free-My-Sony).

Projeto de **engenharia reversa exploratória, somente leitura** do firmware oficial Sony 7.931, com foco em avaliar realisticamente a possibilidade de executar aplicativos adicionais em uma Smart TV Sony **sem Android**.

**Estado do projeto:** ferramenta inicial de inventário criada e testada com amostras sintéticas. **O ZIP oficial esperado ainda não foi recebido nem analisado.** Nada neste projeto prova que seja possível instalar streamings diretamente na TV.

Este projeto reúne ferramentas e documentação em português para quem quiser reproduzir a investigação, aprender com os resultados ou contribuir com evidências. Não possui vínculo com a Sony. Uma conclusão de que não há instalação nativa suportada também é um resultado útil.

Na preparação local para publicação em 26/10/2026, o ZIP esperado não estava presente. Havia um arquivo `.pkg` em `firmware/`, sem análise ou procedência validada nesta etapa. Nenhum pacote de firmware faz parte do conteúdo versionado.

## Testar sem firmware

Com Python 3.9 ou superior, os testes criam amostras sintéticas temporárias e não precisam de TV, firmware ou dependências externas:

```powershell
py -3 -m unittest discover -s tests -v
```

Em Linux/macOS, use `python3 -m unittest discover -s tests -v`. O workflow de GitHub Actions está configurado para executar esses testes em Windows e Linux.

## Iniciar no Windows

1. Extraia este projeto em uma pasta (ex.: `C:\SonyX705G-Codex`).
2. Baixe o firmware do site oficial da Sony: <https://www.sony.com.br/electronics/support/lcd-tvs-xg70xx_x70xxg-series/kd-43x705g/software/00273647>. Confirme que sua TV aparece na lista de modelos. Não atualize a TV: só precisamos do ZIP no computador.
3. Coloque o arquivo `sony_tvupdate_2017_7931_bff_auth.zip` na pasta `firmware`.
4. Abra PowerShell na pasta do projeto e rode:

```powershell
py -3 src\firmware_inspector.py --input firmware\sony_tvupdate_2017_7931_bff_auth.zip
py -3 -m unittest discover -s tests -v
```

Os resultados serão gravados em `reports\firmware_inventory.json` e `reports\firmware_report.md`. O programa não extrai, executa ou envia firmware à TV. Python 3.9+ recomendado, sem dependências externas.

5. Abra a mesma pasta no **Codex para desktop**, **Codex CLI** ou extensão **Codex para VS Code**. Cole o texto de `PROMPT_INICIAL_CODEX.md` na conversa do Codex. O Codex encontrará também o arquivo `AGENTS.md` com instruções persistentes.

## Contexto técnico já confirmado pela pessoa proprietária

- Modelo: Sony KD-55X705G; versão de software: `v7.931-4.000-0103`.
- Linux ARMv7 inferido do navegador. Identificação do navegador: Opera 36 / Chromium 49 (User-Agent, não uma auditoria de componentes).
- Página HTML/JavaScript executa no navegador; vídeos de teste MP4/H.264/AAC e HLS reproduziram.
- Sites de streaming comerciais testados não reproduziram; YouTube via navegador informou versão antiga.
- Testes anteriores relataram um serviço DLNA MediaRenderer. Endereços, portas e capturas da rede pessoal foram omitidos da documentação pública.
- O DLNA não oferece, por si, instalação de aplicativos.

## Hipóteses a testar, NÃO fatos

- O pacote ZIP pode conter payload compactado, assinado e/ou criptografado; é preciso identificar o formato real.
- O firmware pode incluir mecanismo interno de aplicativos restrito a componentes pré-instalados.
- Conseguir instalar software nativo não garantiria funcionamento de streamings por requisitos DRM, codecs, certificados e suporte das plataformas.

## Fontes

- Sony — firmware oficial 7.931 e modelos aplicáveis: <https://www.sony.com.br/electronics/support/lcd-tvs-xg70xx_x70xxg-series/kd-43x705g/software/00273647>
- Sony — componentes de código aberto do modelo: <https://oss.sony.net/Products/Linux/TV/KD-55X705G.html>

## Segurança e limites

Apenas analisar arquivos **offline**. Não atualizar, regravar, desmontar ou modificar a TV; não explorar falhas de rede; não procurar chaves DRM nem tentar burlar controle de acesso. Não publicar o ZIP da Sony em um repositório. Inspeção estática de componentes públicos é o escopo autorizado.

## Contribuir e acompanhar

- Consulte [o registro de evidências](docs/EVIDENCIAS.md) e [o plano](PLANO.md) antes de propor uma conclusão.
- Use Issues para dúvidas, referências e resultados reproduzíveis; veja [CONTRIBUTING.md](CONTRIBUTING.md).
- Envie melhorias nas ferramentas e testes por pull request, usando somente amostras sintéticas.
- Não anexe firmware, payloads, dados pessoais, capturas de rede ou relatórios brutos. Os relatórios gerados permanecem locais em `reports/`; registre apenas conclusões revisadas e sem dados privados na documentação.

Para publicar esta cópia, consulte [docs/PUBLICACAO.md](docs/PUBLICACAO.md).

## Licença

O código e a documentação deste projeto estão sob a [licença MIT](LICENSE). Essa licença não abrange firmware, marcas ou componentes de terceiros, que não são distribuídos aqui.
