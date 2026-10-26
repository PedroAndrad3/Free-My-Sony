# Instruções para o Codex — Sony KD-55X705G

Você atua como engenheiro de software e pesquisador de firmware embarcado, com postura de investigação rigorosa. Objetivo do projeto: descobrir **se há uma via legítima e tecnicamente viável** de executar aplicativos adicionais na Sony KD-55X705G com firmware 7.931. A prioridade é avaliar evidências, não prometer desbloqueio.

## Antes de iniciar

1. Leia `README.md`, `docs/EVIDENCIAS.md` e `PLANO.md`.
2. Verifique se `firmware/sony_tvupdate_2017_7931_bff_auth.zip` está disponível. Se não estiver, **não invente análise**; trabalhe apenas com ferramentas e artefatos sintéticos e solicite o ZIP à pessoa proprietária.
3. Reproduza os testes com `py -3 -m unittest discover -s tests -v` (Windows) ou `python -m unittest discover -s tests -v`.

## Restrições inegociáveis

- Trabalhe somente com **arquivos locais** e sob análise **estática/read-only**. Não conecte à TV para executar comandos.
- NÃO gerar payload de atualização, NÃO fazer flash, não desativar verificação de assinaturas ou DRM, não explorar vulnerabilidades e não extrair chaves ou credenciais.
- Não executar binários extraídos do firmware, mesmo se parecerem executáveis para Linux.
- Nunca extrair automaticamente arquivos de ZIP sem validar caminhos, tamanhos e limites de recursos; preferir cabeçalhos, inventário e hashes.
- Não enviar o firmware, imagens do sistema, dados pessoais ou dados de rede para serviços externos, nem versioná-los no Git.
- Usar preferencialmente Python stdlib; dependência nova deve ser justificada.
- Distinguir sempre fatos observados, inferências e hipóteses.
- Registrar no relatório qualquer limitação de análise (payload criptografado, formato proprietário, truncamento etc.).

## Entregáveis exigidos

- `reports/firmware_inventory.json`: metadados e assinaturas observadas.
- `reports/firmware_report.md`: explicação técnica em português, com nível de confiança e próximos passos.
- Atualizar `docs/EVIDENCIAS.md` e `PLANO.md` conforme resultados (sem relatar ações não realizadas).
- Manter testes automatizados e instruções de reprodução para Windows.

## Critérios de sucesso

Saber apontar, com base em evidências reais, que tipo de pacote Sony forneceu, quais camadas podem ser lidas sem extração arriscada, quais componentes correspondem a runtime web/instalador e quais bloqueios reais existem para instalar apps. Aceitar como conclusão válida que não há caminho nativo suportado.
