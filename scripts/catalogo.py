"""Gera fotos de catálogo (peça sozinha, fundo neutro) para as peças dela. Uso: python3 scripts/catalogo.py prompts|recortar"""
import json, re, sys, os
s = open('app/index.html').read()
pcs = re.findall(r'  P\("([A-Z]{3}-\d\d)","([a-z]+)","([^"]*)","([^"]*)","([^"]*)"(?:, (true|"[a-z]+"))?\)', s)
md = {}
for l in open('guarda-roupa/pecas.md'):
    m = re.match(r'\| ([A-Z]{3}-\d\d) \| ([^|]*)\| ([^|]*)\| ([^|]*)\| ([^|]*)\|', l)
    if m: md[m[1]] = (m[2].strip(), m[3].strip(), re.sub(r'\*\*', '', m[4].strip()), m[5].strip())
lista = [(c, cat) for c, cat, *_ , t in pcs if t == 'true' and c in md and '🎁' not in md[c][3]]
grupos = [lista[i:i+6] for i in range(0, len(lista), 6)]
os.makedirs('prompts/catalogo', exist_ok=True); os.makedirs('looks/_catalogo', exist_ok=True)
if sys.argv[1] == 'prompts':
    for g, grupo in enumerate(grupos, 1):
        linhas = []
        for i, (c, cat) in enumerate(grupo, 1):
            nome, cor, det, _ = md[c]
            como = "pendurada num cabide de madeira clara" if cat in ("top","terceira","vestido") else ("dobrada/pousada" if cat in ("acessorio","sapato") else "estendida reta, vista de frente")
            linhas.append(f"{i}. {nome} — cor {cor.lower()}; {det[:260]}. Mostrar {como}.")
        n = len(grupo); grade = "2 linhas × 3 colunas" if n > 3 else f"1 linha × {n} colunas"
        txt = f"Prompt pronto para colar:\n\nCrie uma única imagem com uma grade de {n} fotos ({grade}), separadas por finas linhas brancas, em estilo de foto de produto de e-commerce de moda minimalista: cada foto mostra UMA peça sozinha, sem pessoa, sem manequim, centralizada, ocupando bem o quadro, em fundo liso cinza-claro quente, luz suave de estúdio, sombra leve. Cores e texturas fiéis à descrição. Ordem da esquerda para a direita, de cima para baixo:\n" + "\n".join(linhas) + "\nSem texto, sem etiquetas, sem logotipos."
        open(f'prompts/catalogo/g{g:02d}.md', 'w').write(txt)
    json.dump(grupos, open('looks/_catalogo/grupos.json', 'w'))
    print(len(lista), 'peças em', len(grupos), 'grades')
else:
    from PIL import Image
    grupos = json.load(open('looks/_catalogo/grupos.json'))
    for g, grupo in enumerate(grupos, 1):
        f = f'looks/_catalogo/g{g:02d}.png'
        if not os.path.exists(f): continue
        im = Image.open(f).convert('RGB'); W, H = im.size; n = len(grupo)
        cols = 3 if n > 3 else n; rows = 2 if n > 3 else 1
        for i, (c, _) in enumerate(grupo):
            x, y = i % cols, i // cols
            t = im.crop((x*W//cols+6, y*H//rows+6, (x+1)*W//cols-6, (y+1)*H//rows-6))
            t.save(f'app/img/pecas/cat-{c}.jpg', quality=88)
    print('ok')
