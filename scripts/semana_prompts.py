"""Gera os prompts das imagens da semana (3 opções por dia) a partir de semanas/<data>.json."""
import json, re, sys
plan = json.load(open(sys.argv[1]))
cat = {}
for l in open('guarda-roupa/pecas.md'):
    m = re.match(r'\| ([A-Z]{3}-\d\d) \| ([^|]*)\| ([^|]*)\| ([^|]*)\|', l)
    if m: cat[m[1]] = f"{m[2].strip()} {m[3].strip().lower()} ({m[4].strip()[:160]})"
SAP = {"SAP-02":"slingback marrom café de couro croco, bico fino, salto médio fino","SAP-03":"tênis branco de couro com logo V preto na lateral",
"SAP-04":"tênis retrô de camurça caramelo com faixa off-white","SAP-05":"sapato preto de bico fino com salto médio bloco",
"SAP-06":"bota marrom de couro de cano baixo","SAP-07":"bota preta de couro de cano baixo","SAP-08":"sapatilha slingback marrom clara sem salto",
"SAP-09":"tênis Adidas Samba branco com 3 listras pretas e sola caramelo","SAP-10":"slingback prata metalizado, bico quadrado, salto médio bloco"}
desc = lambda c: SAP.get(c) or re.sub(r'\*\*', '', cat.get(c, c))
head = open('prompts/2026-11-09-sueter-chevron-kookai-street-style.md').read().split('Prompt pronto para colar:')[1].split('PEÇA FIXA')[0].strip()
looks = [(d, o) for d in plan["dias"] for o in d["opcoes"]]
for k in range(0, len(looks), 6):
    grupo = looks[k:k+6]
    h = head if len(grupo) == 6 else head.replace("grade de 6 fotos (2 linhas × 3 colunas)", f"grade de {len(grupo)} fotos lado a lado (1 linha × {len(grupo)} colunas, cada foto vertical)")
    linhas = []
    for i, (d, o) in enumerate(grupo, 1):
        clima = f"{d['max']} °C" + (", dia chuvoso, calçada molhada" if d["chuva"] else "")
        pcs = "; ".join(desc(c) for c in o["pecas"]) + ("; " + "; ".join(o.get("extras", [])) if o.get("extras") else "")
        linhas.append(f"{i}. \"{d['dia']} · {o['nome']}\" ({clima}): {pcs}.")
    txt = f"# Semana {plan['inicio']} — parte {k//6+1}\n\nPrompt pronto para colar:\n\n{h}\n\nLOOKS (cada foto um look; peça larga só ela é larga, o resto ajustado; camisa larga nunca por dentro):\n" + "\n".join(linhas) + "\n\nRoupas, bolsas e sapatos exatamente como descritos. Sem texto, sem legendas, sem logotipos.\n"
    open(f"prompts/semana-{plan['inicio']}-parte{k//6+1}.md", "w").write(txt)
    print(f"prompts/semana-{plan['inicio']}-parte{k//6+1}.md", len(grupo))
