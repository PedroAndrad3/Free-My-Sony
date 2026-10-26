# Primeira tarefa para o Codex

Estou investigando minha Sony KD-55X705G (Linux, firmware 7.931) para avaliar se é possível instalar aplicativos de streaming adicionais **sem Android TV**. Os testes de navegação, MP4/HLS e UPnP estão documentados neste projeto. Leia integralmente `AGENTS.md`, `README.md`, `docs/EVIDENCIAS.md` e `PLANO.md`.

**Sua missão nesta etapa:** executar uma investigação de firmware exclusivamente offline e somente leitura.

1. Inspecione a estrutura do repositório e rode os testes existentes.
2. Se existir `firmware/sony_tvupdate_2017_7931_bff_auth.zip`, execute o inspetor e examine o inventário. Se o arquivo não estiver presente, não invente resultados nem finja que analisou o firmware; sinalize sua ausência e melhore/teste as ferramentas usando arquivos sintéticos.
3. Identifique os contêineres internos com evidências: magic bytes, tamanho, assinatura, compactação, possível criptografia, formato de partição/sistema de arquivos. Não inferir criptografia apenas pela entropia.
4. Proponha próximos passos de análise estática não destrutiva para compreender runtime do navegador, mecanismos oficiais de atualização e formato de apps. **Não** altere a TV, não crie imagens de instalação ou payloads e não tente burlar DRM ou assinaturas.
5. Gere um relatório claro em português com: achados confirmados, hipóteses, limites, riscos e recomendação sobre a viabilidade de instalar serviços de streaming nativamente.
6. Registre alterações e rode os testes. Sempre peça aprovação antes de instalar novas dependências ou acessar rede externa.

Priorize precisão sobre entusiasmo: concluir que não é viável é aceitável se a evidência apontar isso.
