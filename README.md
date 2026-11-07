# 👗 Acervo de Looks

Acervo das minhas roupas + prompts prontos para gerar looks novos no ChatGPT,
para não precisar pensar no que vestir de manhã para o trabalho.

## Abrir a página

👉 **[Looks do Dia](https://claude.ai/artifact/4aKopUPTGpFVxXRU8AG6q4)**: mural das peças e dos looks, sorteio do look do dia e montador de combinações com prompt pronto. O código fica em `app/`.

## Como funciona

```
1. Cadastro a peça   →  guarda-roupa/pecas.md
2. Peço ao Claude    →  "monta um prompt de looks com a saia X" (ou "looks para semana fria")
3. Claude gera o prompt e salva em prompts/
4. Colo o prompt no ChatGPT → ele gera a imagem com os looks
5. Salvo a imagem em looks/<pasta-da-coleção>/ e anoto os favoritos
6. De manhã: abro looks/, escolho um e pronto ✨
```

## Estrutura

| Pasta | O que tem |
|---|---|
| `guarda-roupa/pecas.md` | Catálogo de todas as minhas peças, com código (ex.: `SAI-01`) |
| `prompts/modelo-base.md` | Modelos de prompt (grade de 15 looks / look único) |
| `prompts/` | Prompts já gerados, um arquivo por pedido |
| `looks/` | Imagens geradas, organizadas por coleção, com a lista dos looks |

## Pedidos que funcionam bem

- "Cadastra essas peças: blazer preto de alfaiataria, calça pantalona bege..."
- "Gera um prompt de 15 looks novos usando só peças do acervo"
- "Prompt de 5 looks para a semana que vem, vai fazer frio"
- "Quero looks com a saia creme que eu ainda não fiz"
- "Look para reunião importante amanhã, com a camisa azul"

## Coleções

- [Saia creme em camadas — 15 looks](looks/2026-11-saia-creme-camadas/)

## Prompts prontos

- [Saia creme — 15 looks novos (rodada 2)](prompts/2026-11-07-saia-creme-15-looks-novos.md)
- [Jaqueta bomber preta — 15 looks](prompts/2026-11-07-jaqueta-bomber-preta-15-looks.md)
