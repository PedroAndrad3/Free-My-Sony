# Como contribuir

Queremos descobrir o que as evidências permitem concluir sobre a Sony KD-55X705G com firmware 7.931. Não há promessa de desbloqueio ou de instalação de aplicativos.

## Antes de abrir uma Issue

Leia `README.md`, `docs/EVIDENCIAS.md`, `PLANO.md` e os limites de `AGENTS.md`. Separe fatos observados, inferências e hipóteses. Resultados negativos e formatos não identificados também são contribuições úteis.

Para relatar um achado, informe modelo, versão de firmware, método estático, comandos reproduzíveis e limitações. Cite a origem pública quando houver. Não generalize um resultado para outros modelos ou versões sem evidências.

Não envie ZIPs da Sony, imagens de sistema, binários extraídos, chaves, credenciais, fotos identificáveis, IPs reais, números de série, capturas de rede ou relatórios brutos. Revise também nomes de arquivos e caminhos locais. Prefira exemplos sintéticos e conclusões sanitizadas. Firmware deve ser obtido individualmente na fonte oficial e mantido fora do Git.

## Alterações no código

1. Faça um fork e crie uma branch para a alteração.
2. Use preferencialmente Python stdlib e mantenha compatibilidade com Python 3.9 ou superior.
3. Trabalhe somente com análise estática local. Não execute firmware nem conecte ferramentas à TV.
4. Para mudanças no inspetor, acrescente testes sintéticos que verifiquem o comportamento relevante.
5. Execute no PowerShell:

```powershell
py -3 -m unittest discover -s tests -v
git status --short
git diff --cached --stat
```

6. Abra um pull request explicando o problema, a mudança, como foi validada e as limitações.

Não inclua payloads de atualização, instruções de flash, exploração de falhas, bypass de assinaturas/DRM ou extração de segredos. Nunca extraia automaticamente arquivos de um ZIP sem validar caminhos, tamanhos e limites de recursos.

O `.gitignore` é uma proteção inicial, não um filtro de conteúdo: revise cada arquivo antes de publicá-lo. Não use `git add -f` para contornar as exclusões de firmware e relatórios privados.

## Documentação e licença

Mantenha os textos em português e registre apenas ações realizadas. Ao contribuir com código e documentação de sua autoria, use a licença MIT do projeto; não inclua material de terceiros sem autorização compatível.
