# Instruções para o Claude

Este repositório é o acervo de roupas da Andressa e serve para gerar prompts de looks
para o ChatGPT criar imagens. Converse sempre em português.

## Perfil (sempre no prompt)
- Mulher magra e esguia, 1,68 m, ~56 kg, cintura fina, cabelo castanho acobreado (no prompt reforçar: "castanho médio com reflexos cobre, não preto nem castanho escuro"; o ChatGPT tende a escurecer). Sempre descrever o corpo da modelo assim.
- Peça oversized é estilo: dizer que **só aquela peça** é larga e o resto é do tamanho certo e ajustado.
- Preferir pose natural de "look do dia" (3/4, mão no bolso ou na cintura), não de frente rígida.
- Grades menores (9 looks, 3×3) saem com mais qualidade que 15.
- **Estilo que ela gosta**: street style de modelo fora do trabalho (referências: Hailey Bieber, Kendall Jenner). Foto andando na rua, não catálogo de estúdio. Não colocar nomes de celebridades no prompt; descrever a estética.
- Antes de errar de novo, veja `looks/_descartados/README.md`.

## Ao receber um pedido de looks
1. Leia `guarda-roupa/pecas.md`. **Só a peça âncora vem do acervo.** Não reutilize outras peças dela
   (nem a saia, nem a jaqueta, nem a listrada) a menos que ela peça. Proponha peças novas que combinem.
   Não repita tipos de peça das rodadas anteriores (veja `prompts/`): varie categorias, comprimentos,
   tecidos, acessórios e cabelo (coque, rabo baixo, solto liso).
   Repertório Kendall/Hailey: office siren (saia lápis + meia-calça fina + óculos de grau), baggy jeans
   arrastando + regata, peça jogada nos ombros sobre vestido de malha, minissaia + meia-calça opaca,
   camisa listrada azul, bermuda de alfaiataria longa, cinto de corrente, mini bolsa, óculos pequenos.
2. Leia os `README.md` de `looks/` para não repetir combinações já feitas e para seguir os looks marcados com ⭐.
3. Parta de `prompts/modelo-base.md`, modelo **C) Street style** (padrão) e descreva cada peça com cor, tecido e modelagem do catálogo.
4. Salve o prompt em `prompts/AAAA-MM-DD-<tema>.md` e mostre o bloco pronto para copiar na resposta.
5. **Sem sapatos no acervo por enquanto**: não escolha sapato; no prompt peça "sapato simples e discreto, em tom neutro".
6. **Proporção**: peça ampla em cima (ex.: JAQ-02) pede parte de baixo reta ou ajustada; nunca com peça de volume (ex.: SAI-01). Na página isso fica nas listas `AMPLAS` e `COM_VOLUME`.
7. Foco: trabalho (escritório). Considere clima/ocasião se ela informar.

## Ao cadastrar peças
- Adicione na tabela da categoria certa em `guarda-roupa/pecas.md`, com o próximo código livre.
- Se ela mandar foto, descreva a peça a partir da foto.

## Ao receber uma imagem gerada
- Crie `looks/AAAA-MM-<tema>/` com a imagem e um `README.md` listando os looks (modelo: `looks/2026-11-saia-creme-camadas/`).
- Linke a coleção no `README.md` da raiz.

Faça commit e push depois de cada alteração.

## Página "Looks do Dia" (app/)
- Publicada em https://claude.ai/artifact/4aKopUPTGpFVxXRU8AG6q4 a partir de `app/index.html` (imagens em `app/img/`).
- Os dados `PIECES` e `LOOKS` dentro de `app/index.html` espelham `guarda-roupa/pecas.md` e `looks/`. Ao cadastrar peça ou coleção nova, atualize os dois, gere os recortes em `app/img/` e republique no mesmo URL (Artifact com `url`, `root: app`).
- O banco da página guarda o que ela marca: coleção `looks` (`favorito`, `usos` = datas) e coleção `ideias` (combinações salvas para gerar, com `pecas` e `prompt`). Leia esses dados com ArtifactData antes de montar prompts novos.
