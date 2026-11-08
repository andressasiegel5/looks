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

- [Blazer off-white (Amaro) — com as suas peças, 6 looks](looks/2026-11-blazer-offwhite-amaro/) ✨
- [Blazer de malha cinza (Zara) — com as suas peças, 5 looks](looks/2026-11-blazer-malha-cinza/) ✨
- [Vestido longo listrado (Viviane Furrier) — com as suas peças, 6 looks](looks/2026-11-vestido-longo-listrado/) ✨
- [Vestido letreiro (Lança Perfume) — com as suas peças, 6 looks](looks/2026-11-vestido-letreiro-lanca/) ✨
- [Casaco-camisa marrom — com as suas peças, 6 looks](looks/2026-11-casaco-camisa-marrom/) ✨
- [Vestido floral verde (Ralph Lauren) — com as suas peças, 6 looks](looks/2026-11-vestido-floral-verde/) ✨
- [Vestido de tricô marrom — com as suas peças, 6 looks](looks/2026-11-vestido-trico-marrom/) ✨
- [Vestido de lã cinza chumbo — com as suas peças, 6 looks](looks/2026-11-vestido-la-cinza/) ✨
- [Camisa-jaqueta de cotelê — com as suas peças, 6 looks](looks/2026-11-camisa-jaqueta-cotele/) ✨
- [Blazer pied-de-poule — com as suas peças, 6 looks](looks/2026-11-blazer-pied-de-poule/) ✨
- [Casaco de tricô com cachecol — com as suas peças, 6 looks](looks/2026-11-casaco-trico-cachecol/) ✨
- [Jaqueta jeans oversized — com as suas peças, 6 looks](looks/2026-11-jaqueta-jeans-oversized/) ✨
- [Jaqueta jeans branca — com as suas peças, 6 looks](looks/2026-11-jaqueta-jeans-branca/) ✨
- [Saia transpassada verde-menta — com as suas peças, 6 looks](looks/2026-11-saia-transpassada-verde/) ✨
- [Tech T-shirts gola redonda e V — com as suas peças, 6 looks](looks/2026-11-tech-tshirts-insider/) ✨
- [Regatas gola alta azul e oliva — com as suas peças, 6 looks](looks/2026-11-regatas-gola-alta-insider/) ✨
- [Jaqueta de camurça caramelo — com as suas peças, 6 looks](looks/2026-11-jaqueta-camurca-caramelo/) ✨
- [Suéter taupe — com as suas peças, 6 looks](looks/2026-11-sueter-taupe/) ✨
- [Camiseta gola alta cinza — com as suas peças, 6 looks](looks/2026-11-camiseta-gola-alta-cinza/) ✨
- [Parka preta — com as suas peças, 6 looks](looks/2026-11-parka-preta/) ✨
- [Camiseta preta com debrum — com as suas peças, 6 looks](looks/2026-11-camiseta-debrum-preta/) ✨
- [Calça marrom escuro — com as suas peças, 6 looks](looks/2026-11-calca-marrom/) ✨
- [Coletes preto curto e creme — com as suas peças, 6 looks](looks/2026-11-coletes-preto-e-creme/) ✨
- [Blusa de tricô marrom — com as suas peças, 6 looks](looks/2026-11-blusa-trico-marrom/) ✨
- [Calça de alfaiataria cinza mescla (H&M) — com as suas blusas, 6 looks](looks/2026-11-calca-cinza-hm/) ✨
- [Calça wide leg off-white (H&M) — com as suas blusas, 6 looks](looks/2026-11-calca-offwhite-hm/) ✨
- [Saia slip animal print — com as suas blusas, 6 looks](looks/2026-11-saia-slip-animal-print/) ✨
- [Blusa Wingsuit branca — street style, 6 looks](looks/2026-11-blusa-wingsuit-branca/) ✨
- [Blusa preta com renda — street style, 6 looks](looks/2026-11-blusa-renda-preta/) ✨
- [Polo de tricô com botões preta — street style, 6 looks](looks/2026-11-polo-botoes-preta/) ✨
- [Camisa acetinada preta — street style, 6 looks](looks/2026-11-camisa-acetinada-preta/) ✨
- [Polo de tricô Erica Candy — street style, 6 looks](looks/2026-11-polo-tricot-pistache/) ✨
- [Blazer preto trespassado — street style, 6 looks](looks/2026-11-blazer-preto-trespassado/) ✨
- [Camiseta listrada vermelha — rodada 2, peças variadas](looks/2026-11-camiseta-listrada-rodada-2/) ✨
- [Camiseta listrada vermelha — street style, 6 looks](looks/2026-11-camiseta-listrada-street/)
- [Jaqueta bomber preta — street style, 6 looks](looks/2026-11-jaqueta-bomber-street/) ✨
- [Saia creme em camadas — 15 looks](looks/2026-11-saia-creme-camadas/)

## Prompts prontos

- [Saia creme — 15 looks novos (rodada 2)](prompts/2026-11-07-saia-creme-15-looks-novos.md)
- [Jaqueta bomber preta — 9 looks (v2)](prompts/2026-11-07-jaqueta-bomber-preta-9-looks-v2.md)
- [Jaqueta bomber preta — street style (v3)](prompts/2026-11-07-jaqueta-bomber-preta-street-style-v3.md)
- [Camiseta listrada vermelha — street style](prompts/2026-11-07-camiseta-listrada-vermelha-street-style.md)
- [Camiseta listrada vermelha — rodada 2 (peças variadas)](prompts/2026-11-07-camiseta-listrada-rodada-2.md)
- [Blazer preto trespassado (Zara) — street style v2](prompts/2026-11-07-blazer-preto-trespassado-street-style.md)
- [Polo de tricô Erica Candy — street style](prompts/2026-11-07-polo-tricot-pistache-street-style.md)
- [Camisa acetinada preta (Shoulder) — street style](prompts/2026-11-07-camisa-acetinada-preta-street-style.md)
- [Polo de tricô com botões preta (Shoulder) — street style](prompts/2026-11-07-polo-botoes-preta-street-style.md)
- [Blusa preta com renda (Anne Fernandes) — street style](prompts/2026-11-07-blusa-renda-preta-street-style.md)
- [Blusa Wingsuit branca (Insider) — street style](prompts/2026-11-07-blusa-wingsuit-branca-street-style.md)
- [Saia slip animal print (H&M) — street style](prompts/2026-11-07-saia-slip-animal-print-street-style.md)
- [Calça wide leg off-white (H&M) — street style](prompts/2026-11-07-calca-offwhite-hm-street-style.md)
- [Calça de alfaiataria cinza mescla (H&M) — street style](prompts/2026-11-07-calca-cinza-hm-street-style.md)
- [Blusa slim de tricô marrom (Hering) — street style](prompts/2026-11-07-blusa-trico-marrom-street-style.md)
- [Coletes preto curto e creme — street style](prompts/2026-11-07-coletes-preto-e-creme-street-style.md)
- [Calça de alfaiataria marrom escuro — street style](prompts/2026-11-07-calca-marrom-street-style.md)
- [Camiseta preta com debrum (Morena Rosa) — street style](prompts/2026-11-08-camiseta-debrum-preta-street-style.md)
- [Parka preta com capuz de pelo (Amaro) — street style](prompts/2026-11-08-parka-preta-street-style.md)
- [Camiseta gola alta cinza (Zara) — street style](prompts/2026-11-08-camiseta-gola-alta-cinza-street-style.md)
- [Suéter Future Knit taupe (Insider) — street style](prompts/2026-11-08-sueter-taupe-street-style.md)
- [Jaqueta-camisa de camurça caramelo — street style](prompts/2026-11-08-jaqueta-camurca-caramelo-street-style.md)
- [Regatas gola alta Tech (Insider) azul e oliva — street style](prompts/2026-11-08-regatas-gola-alta-insider-street-style.md)
- [Tech T-shirts (Insider) gola redonda e gola V — street style](prompts/2026-11-08-tech-tshirts-insider-street-style.md)
- [Saia transpassada de linho verde-menta — street style](prompts/2026-11-08-saia-transpassada-verde-street-style.md)
- [Jaqueta jeans branca (Zara) — street style](prompts/2026-11-08-jaqueta-jeans-branca-street-style.md)
- [Jaqueta jeans oversized azul — street style](prompts/2026-11-08-jaqueta-jeans-oversized-street-style.md)
- [Casaco de tricô com cachecol bege (Shoulder) — street style](prompts/2026-11-09-casaco-trico-cachecol-street-style.md)
- [Blazer longo pied-de-poule — street style](prompts/2026-11-09-blazer-pied-de-poule-street-style.md)
- [Camisa-jaqueta de veludo cotelê (Zara) — street style](prompts/2026-11-09-camisa-jaqueta-cotele-street-style.md)
- [Vestido sem manga de lã cinza chumbo — street style](prompts/2026-11-09-vestido-la-cinza-street-style.md)
- [Vestido de tricô marrom gola alta — street style](prompts/2026-11-09-vestido-trico-marrom-street-style.md)
- [Vestido floral verde (Ralph Lauren) — street style](prompts/2026-11-09-vestido-floral-verde-street-style.md)
- [Casaco-camisa aveludado marrom — street style](prompts/2026-11-09-casaco-camisa-marrom-street-style.md)
- [Vestido letreiro preto (Lança Perfume) — street style](prompts/2026-11-09-vestido-letreiro-lanca-street-style.md)
- [Vestido longo listrado (Viviane Furrier) — street style](prompts/2026-11-09-vestido-longo-listrado-street-style.md)
- [Blazer de malha cinza (Zara) — street style](prompts/2026-11-09-blazer-malha-cinza-street-style.md)
- [Blazer off-white (Amaro) — street style](prompts/2026-11-09-blazer-offwhite-amaro-street-style.md)
