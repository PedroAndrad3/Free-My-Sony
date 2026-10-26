# Publicar o projeto no GitHub

Destino proposto: conta `PedroAndrad3`, repositório público `sony-kd55x705g-codex`.

Esta preparação local não confirma a criação do repositório remoto. A publicação externa foi interrompida pela revisão automática por causa da restrição de trabalhar somente com arquivos locais; é necessário esclarecer a autorização para publicar o código e a documentação.

## Conteúdo público

Código Python, testes sintéticos, documentação revisada, licença MIT, guia de contribuição e configuração do GitHub Actions. O firmware e os relatórios brutos continuam locais. Os arquivos `.gitkeep` apenas mantêm as pastas vazias no Git.

## Reprodução local

No Windows, com Python instalado:

```powershell
py -3 -m unittest discover -s tests -v
```

Se `py -3` informar que não há Python instalado, use o caminho completo de um Python 3.9+ disponível, seguido dos mesmos argumentos. Não é necessário instalar bibliotecas.

Se o ambiente restringir a pasta temporária padrão, configure uma pasta local antes dos testes:

```powershell
New-Item -ItemType Directory -Force .tmp | Out-Null
$env:TEMP = (Resolve-Path .tmp).Path
$env:TMP = $env:TEMP
py -3 -m unittest discover -s tests -v
```

## Publicação após autorização

1. No GitHub, crie um repositório público vazio chamado `sony-kd55x705g-codex` na conta `PedroAndrad3`. Não adicione README, licença ou `.gitignore` pelo site, pois eles já existem localmente.
2. Revise o que será publicado:

```powershell
git ls-files
git status --short
git log -1 --oneline
git check-ignore firmware/sony_tvupdate_2017_7931_bff_auth.zip reports/firmware_inventory.json reports/firmware_report.md
```

3. Depois de criar o remoto e conferir os arquivos, conecte e envie a branch:

```powershell
git remote add origin https://github.com/PedroAndrad3/sony-kd55x705g-codex.git
git push -u origin main
```

Se já existir um remoto `origin`, confira `git remote -v` antes de alterar qualquer configuração. Autentique-se pelo fluxo normal do GitHub, sem colocar tokens ou senhas em comandos ou arquivos do projeto.

Nesta pasta, o Git detectou que o proprietário do diretório é diferente do usuário atual. Para os comandos locais desta preparação, foi usada a opção temporária `git -c safe.directory=C:/st/sony-kd55x705g-codex ...`, exclusivamente para este repositório recém-criado. Se ocorrer a mesma mensagem ao publicar esta cópia, acrescente essa opção aos comandos Git acima. Nenhuma exceção global foi configurada.

4. Abra a página do repositório, confirme os arquivos e acompanhe a primeira execução na aba Actions. A execução local dos testes não confirma o resultado do CI remoto.

Descrição sugerida: “Investigação estática e offline do firmware da Sony KD-55X705G, com ferramentas Python, testes sintéticos e evidências em português.”
