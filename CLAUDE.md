# Instruções para o Claude

Este repositório é o acervo de roupas da Andressa e serve para gerar prompts de looks
para o ChatGPT criar imagens. Converse sempre em português.

## Ao receber um pedido de looks
1. Leia `guarda-roupa/pecas.md` e use **somente** peças cadastradas (prefira ✅; ❓ só se ainda não houver peças ✅ suficientes, e avise).
2. Leia os `README.md` de `looks/` para não repetir combinações já feitas e para seguir os looks marcados com ⭐.
3. Parta de `prompts/modelo-base.md` (grade de 15 ou look único) e descreva cada peça com cor, tecido e modelagem do catálogo.
4. Salve o prompt em `prompts/AAAA-MM-DD-<tema>.md` e mostre o bloco pronto para copiar na resposta.
5. Foco: trabalho (escritório). Considere clima/ocasião se ela informar.

## Ao cadastrar peças
- Adicione na tabela da categoria certa em `guarda-roupa/pecas.md`, com o próximo código livre.
- Se ela mandar foto, descreva a peça a partir da foto.

## Ao receber uma imagem gerada
- Crie `looks/AAAA-MM-<tema>/` com a imagem e um `README.md` listando os looks (modelo: `looks/2026-11-saia-creme-camadas/`).
- Linke a coleção no `README.md` da raiz.

Faça commit e push depois de cada alteração.
