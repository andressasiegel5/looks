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
4. Salve o prompt em `prompts/AAAA-MM-DD-<tema>.md` (texto após "Prompt pronto para colar:"), linke no README, rode
   `python3 app/build_prompts.py` (a aba Prompts foi removida do app a pedido dela; os prompts ficam só no repositório).
   Na resposta, mostre o prompt **dentro de um bloco de código** (```), que tem botão de copiar na conversa.
5. **Bolsas dela (BOL-01 a BOL-09)**: nos looks, use uma dessas bolsas (cor/estilo do catálogo), não invente outras.
6. **Sapatos dela (SAP-02 a SAP-07)**: escolha entre eles. Escritório: sapato preto de bico com salto bloco (SAP-05), slingback café croco (SAP-02), slingback prata (SAP-10) ou sapatilha slingback marrom clara (SAP-08, boa para dias quentes);
   frio: bota cano alto SAP-11 (salto alto; não em chuva forte), botas cano baixo marrom (SAP-06) ou preta (SAP-07); casual/sexta: tênis Veja branco (SAP-03), tênis Stella Larroude (SAP-04) ou Adidas Samba (SAP-09).
   O loafer SAP-01 está caindo do pé: não usar até ela avisar que resolveu.
6. **Proporção**: peça ampla em cima (ex.: JAQ-02) pede parte de baixo reta ou ajustada; nunca com peça de volume (ex.: SAI-01). Na página isso fica nas listas `AMPLAS` e `COM_VOLUME`.
7. Foco: trabalho (escritório). Considere clima/ocasião se ela informar.

## Ao cadastrar peças
- Adicione na tabela da categoria certa em `guarda-roupa/pecas.md`, com o próximo código livre.
- **CAS-03 (casaco Shoulder) é marrom acinzentado ESCURO**, não bege (os looks antigos saíram bege e foram removidos).
- **CAM-06 (camisa Max Mara) é muito larga e longa**: nunca por dentro; só aberta como terceira peça ou como vestido-camisa.
- Peças marcadas "🎁 vai doar"/"não usa mais" (JAQ-03 jaqueta de camurça, SAI-03 saia verde envelope) saíram do app e não entram em nenhum look.
- Peças marcadas "🏃 só exercício" (corta-ventos JAQ-10, JAQ-11) não entram em looks de trabalho; no app têm `tenho: "exercicio"`.
- Se ela mandar foto, descreva a peça a partir da foto. Fotos do armário: cadastre SÓ a peça em evidência (no centro/em foco);
  ignore as peças dos lados e não pergunte sobre elas.

## Ao receber uma imagem gerada
- Crie `looks/AAAA-MM-<tema>/` com a imagem e um `README.md` listando os looks (modelo: `looks/2026-11-saia-creme-camadas/`).
- Linke a coleção no `README.md` da raiz.

Faça commit e push depois de cada alteração.

## Página "Looks do Dia" (app/)
- Visual de app (mood → um look por vez, arrastar a foto ou ‹ ♡ ›, "meu armário"/"descobrir", "complete o look", barra preta embaixo).
- Moods são automáticos por palavras-chave (função `moodsOf`); "meu armário" = looks cujas roupas são todas dela (`tenho`), acessórios não contam.
- Publicada em https://claude.ai/artifact/4aKopUPTGpFVxXRU8AG6q4 a partir de `app/index.html` (imagens em `app/img/`).
- Limite de 512 arquivos por versão já atingido: imagens NOVAS (recortes e peças) vão para o armazenamento de assets
  (Artifact `asset: true`, `file_paths`) e o `/_blob/<id>` retornado entra no mapa `IMG` em `app/index.html`.
  Continue salvando os .jpg em `app/img/` no repositório, mas não os passe em `files`. Capabilities: `{db:{}, assets:{}, sample:{}}`.
- Os dados `PIECES` e `LOOKS` dentro de `app/index.html` espelham `guarda-roupa/pecas.md` e `looks/`. Ao cadastrar peça ou coleção nova, atualize os dois, gere os recortes em `app/img/` e republique no mesmo URL (Artifact com `url`, `root: app`).
- Aba looks tem "selecionar" (estilo Google Fotos): os looks que ela remove ganham `oculto: true` em `looks/<id>` no banco e somem do app.
  O botão "♡ wishlist" grava `wishlist: true`; a aba favoritos lista esses looks com as peças que faltam.
  Quando ela pedir para "remover de vez", leia com ArtifactData os docs com `oculto: true` e apague esses looks de `LOOKS` (e anote no README da coleção).
- O banco da página guarda o que ela marca: coleção `looks` (`favorito`, `usos` = datas) e coleção `ideias` (combinações salvas para gerar, com `pecas` e `prompt`). Leia esses dados com ArtifactData antes de montar prompts novos.

## Gerar imagens automaticamente (API da OpenAI)
- A chave está salva no ambiente para `api.openai.com` (o proxy injeta; nunca pedir a chave no chat).
- `python3 scripts/gerar_imagem.py prompts/ARQUIVO.md looks/AAAA-MM-tema/grade-6-looks.png`
  (modelo padrão gpt-image-2, 1536x1024, qualidade medium). Depois: recortar os 6 looks em `app/img/looks/`,
  criar o README da coleção, adicionar em `LOOKS`, rodar `build_prompts.py`, republicar e fazer commit.
- Cada geração custa dinheiro dela: gere uma vez; só repita se a imagem vier com erro claro.

## Modelo
- Ela testou gerar com o próprio rosto (foto de referência) e NÃO gostou do resultado. Use sempre a modelo
  descrita no Perfil (sem foto de referência). A opção `--ref` do script continua existindo, mas não use.

## Look da semana (pedido dela: "monta minha semana")
- No app: botão "📅 monta minha semana" na aba mood (capability `sample`; capabilities agora `{db:{}, assets:{}, sample:{}}`).
  O app NÃO acessa sites externos: a previsão vem do doc `clima/atual` no banco ({dias: {"AAAA-MM-DD": {max, min, chuva}}}).
  Quando ela pedir "atualiza o clima" (ou ao montar a semana), busque a previsão de Curitiba (WebSearch) e grave com ArtifactData. O resultado fica em `semana/atual` no banco.
- Peças favoritas: coleção `pecas` no banco (`pecas/<código>` com `favorito: true`), marcadas na aba peças (♡ marcar favoritas).
  Leia com ArtifactData. Monte os looks SÓ com as favoritas (+ bolsas BOL-xx dela).
- Cidade: **Curitiba**. Busque a previsão de seg a sex (WebSearch; o host api.open-meteo.com não responde neste ambiente).
- **O escritório é frio**: todo look precisa de uma camada por cima (blazer, cardigã, casaco, colete sobre camisa),
  mesmo em dia quente. Ex.: 24 °C → blusa/camiseta de manga curta + blazer ou cardigã que dá para tirar na rua.
  Dia com mín ≤ 10 °C ou máx ≤ 19 °C: precisa de suéter ou casaco quente (CAS-03, CAS-08); a capa CAS-06 é quente mas deixa os braços de fora: no frio só com blusa de manga longa por baixo; casaco-camisa CAS-04 e polo/manga curta sozinhos NÃO servem (função `climaOk` no app).
  Frio (máx ≤ 17 °C) → suéter + casaco/sobretudo, meia-calça se for saia. Chuva → calçado SÓ bota (SAP-06/07) ou tênis de couro (SAP-03 Veja, SAP-09 Samba), nunca sapato/sapatilha/slingback nem camurça (SAP-04); evitar SAI-01; preferir parka.
- **Fora do trabalho (🏠)**: jaquetas jeans JAQ-01, JAQ-04, JAQ-05; conjunto caramelo BLU-38 + CAL-06 (cozy, só casa/fim de semana) e os shorts CAL-08, CAL-09, CAL-10, CAL-11. Nunca em looks de trabalho nem na aba semana.
- **📦 A caminho**: lista `A_CAMINHO` no app (vazia: CAL-03/04/05 e SAI-01/02 chegaram em 13/11). Peça comprada que não chegou entra ali até ela avisar.
- **Peças que ela evita**: sobretudo rosa CAS-07 (💰 provável venda: não usar), parka CAS-02 e jeans CAL-14/CAL-15. Só em extremo (máx ≤ 12 °C ou chuva forte o dia todo).
- Não repetir a mesma peça principal na semana; variar saia/calça.
- Responder com tabela dia | previsão | look (códigos + nomes) e oferecer gerar a imagem (grade de 5, uma geração).

## Regerar look (botão no app)
- Ao abrir um look no app há "↻ regerar este look": o app (capability `sample`) sugere outra combinação com as peças dela.
  Se ela tocar "📸 quero a foto deste", grava em `pedidos` (`tipo: "regerar"`, `substitui: <id do look>`, `pecas`, `status: "novo"`).
- Quando ela disser "gera os pedidos": leia `pedidos` com status "novo" (ArtifactData), gere UMA imagem com até 6 pedidos,
  substitua a foto de cada look `substitui` (mesmo id, assim favoritos ficam), atualize `pecas` em LOOKS e marque o pedido `status: "feito"`.

## Aba "semana" (substitui o botão/modal; abas favoritos e peças estão escondidas da barra)
- **Ela pediu para NÃO gerar imagens novas sem pedir**: já há looks suficientes. Para a semana, escolha as 3 opções/dia entre os looks
  existentes em `LOOKS` (só peças dela, não ocultos, sem 🏠/🎁/parka/jeans, coerentes com o clima) e use a foto deles. Só gere se ela pedir.
- Toda semana: buscar a previsão de Curitiba (WebSearch ou print dela), montar `semanas/<segunda>.json`
  (5 dias × 3 opções, ids `wMMDD-<dia><opção>`, regras do look da semana), rodar `python3 scripts/semana_prompts.py semanas/<arquivo>.json`
  (gera 3 prompts: 6+6+3 looks), gerar as 3 imagens, recortar, subir como assets e trocar o JSON entre `/*SEMANA*/` e `/*FIMSEMANA*/`
  em `app/index.html` (com `img` = `/_blob/<id>` em cada opção). Também gravar `clima/atual`.
- A escolha dela por dia fica em `semana/<inicio>` (`escolhas: {iso: id}`, `trocas: {opção: lookId}`, `excluidos: [...]`).
  Botão "✕ não gostei, trocar" troca a opção por outro look existente (função `pickReplacement`, lista `SEM_FORA`); sem gerar imagem.
  Ao vetar peça nova, adicionar o código em `SEM_FORA`.

## Aba "hoje" (antiga semana)
- Mostra chips "hoje" e o próximo dia útil (`N_DIAS = 2`), 10 opções cada; fim de semana mostra só os próximos dias úteis.
- Toggle "🩹 pé machucado" (`state.soTenis`, localStorage): só looks sem salto/bota e sem saia lápis/curta; usar tênis (Veja ou Samba).
- (antes: só HOJE com até 10 opções; Peças não repetem mais de 2x nas opções.
- Dia quente (máx ≥ 24 °C): `climaOk` tira suéter, casaco, vestido-suéter, veludo, legging, flare de malha.

## Semana rolante
- A aba semana mostra só de hoje em diante e completa até 5 dias úteis (função `rolarSemana`): dias novos ganham 3 looks
  existentes escolhidos por `pickReplacement` (ids `auto-<iso>-N`), clima de `clima/atual` (sem previsão: 20°/12°, "previsão pendente").
- Mantenha `clima/atual` atualizado com os próximos dias (WebSearch) quando ela pedir clima ou semana.

## Fotos de catálogo das peças
- `python3 scripts/catalogo.py prompts` gera prompts (6 peças por grade, fundo neutro) a partir de `pecas.md`; gerar com `gerar_imagem.py`
  em `looks/_catalogo/gNN.png`; `python3 scripts/catalogo.py recortar` corta em `app/img/pecas/cat-<código>.jpg`.
- Subir como assets e pôr o `/_blob/` no mapa `CAT` em `app/index.html` (a foto real continua em `IMG`, aparece em "ver a foto real").
- Peça nova: gerar a foto de catálogo junto (cabe numa grade com outras).

## Looks usados
- Botões "👗 usei hoje" (aba semana) e "vou usar hoje" (ficha do look) gravam `usos: [datas]` em `looks/<id>`.
- Ao montar a semana / trocar opção: evitar looks usados nos últimos 21 dias (ler `looks` com ArtifactData).
- Uso por peças (quando a combinação não tem foto no app): coleção `usos/<data>` com `pecas: [códigos]`. Ler junto com `looks.usos`
  ao montar a semana e evitar repetir a mesma combinação (parte de cima + parte de baixo) por 21 dias.

## Ocasiões especiais
- Aba looks tem o seletor "✨ ocasiões especiais": looks cuja coleção começa com "✨" (`l.especial`). Eles NÃO aparecem no mood, nas listas de trabalho nem na aba hoje.
- Cada coleção especial tem fotos geradas de cabelo, brincos, maquiagem e colar em `GUIA_FOTOS[colecao]` (grades em `looks/<colecao>/guia/`) e um guia em `GUIAS[colecao]` (cabelo, brincos, colar, maquiagem, sapato, bolsa, frio, detalhes), mostrado na ficha do look.
- VES-06 (vestido longo de cetim preto frente-única, Zara) é peça de festa: está em `SEM_FORA`. Coleções de festa: ids `fN-0X`, constante com nome "✨ …".
