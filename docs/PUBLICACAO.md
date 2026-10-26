# Publicar o projeto no GitHub

Repositório público criado pela pessoa proprietária: [PedroAndrad3/Free-My-Sony](https://github.com/PedroAndrad3/Free-My-Sony).

A pessoa proprietária autorizou explicitamente a publicação dos arquivos revisados de código e documentação. A análise de firmware continua restrita a arquivos locais; firmware, relatórios brutos e dados privados não fazem parte da publicação.

## Estado da publicação

O envio inicial da branch `main` foi confirmado no commit `66007fb`. A árvore pública contém os 18 arquivos revisados; `firmware/` e `reports/` contêm somente `.gitkeep`. A pasta local está conectada ao remoto `origin` com acompanhamento de `origin/main`.

A [primeira execução dos testes](https://github.com/PedroAndrad3/Free-My-Sony/actions/runs/40367696110) passou nas quatro combinações de Windows/Linux e Python 3.9/3.13. Esse resultado se refere ao commit `66007fb`; atualizações posteriores podem ser acompanhadas na aba Actions.

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

## Publicação e atualizações

1. O destino é `PedroAndrad3/Free-My-Sony`. Para uma nova cópia de trabalho, clone esse repositório. Para a pasta original do projeto, conecte o remoto conforme o passo 3.
2. Revise o que será publicado:

```powershell
git ls-files
git status --short
git log -1 --oneline
git check-ignore firmware/sony_tvupdate_2017_7931_bff_auth.zip reports/firmware_inventory.json reports/firmware_report.md
```

3. Na pasta original, se ainda não houver remoto, conecte-o e envie a branch:

```powershell
git remote add origin https://github.com/PedroAndrad3/Free-My-Sony.git
git push -u origin main
```

Se já existir um remoto `origin`, confira `git remote -v` antes de alterar qualquer configuração. Autentique-se pelo fluxo normal do GitHub, sem colocar tokens ou senhas em comandos ou arquivos do projeto.

Nesta pasta, o Git detectou que o proprietário do diretório é diferente do usuário atual. Para os comandos locais desta preparação, foi usada a opção temporária `git -c safe.directory=C:/st/sony-kd55x705g-codex ...`, exclusivamente para este repositório recém-criado. Se ocorrer a mesma mensagem ao publicar esta cópia, acrescente essa opção aos comandos Git acima. Nenhuma exceção global foi configurada.

4. Abra a página do repositório, confirme os arquivos e acompanhe a primeira execução na aba Actions. A execução local dos testes não confirma o resultado do CI remoto.

Descrição sugerida: “Investigação estática e offline do firmware da Sony KD-55X705G, com ferramentas Python, testes sintéticos e evidências em português.”
