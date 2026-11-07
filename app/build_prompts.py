"""Copia os prompts de prompts/*.md para dentro de app/index.html (aba Prompts).

Uso (na raiz do repositório):  python3 app/build_prompts.py
Ordem: a lista "Prompts prontos" do README.md, do mais novo para o mais antigo.
Um prompt fica marcado como "já gerado" quando algum looks/*/README.md aponta para ele.
"""
import glob, json, os, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
readme = open(os.path.join(ROOT, "README.md"), encoding="utf-8").read()
ordem = re.findall(r"\]\((prompts/[^)]+\.md)\)", readme)[::-1]
gerados = "".join(open(f, encoding="utf-8").read() for f in glob.glob(os.path.join(ROOT, "looks/*/README.md")))

itens = []
for rel in ordem:
    caminho = os.path.join(ROOT, rel)
    if not os.path.exists(caminho):
        continue
    md = open(caminho, encoding="utf-8").read()
    if "street style" not in md.lower():
        continue  # só os prompts no estilo atual
    titulo = re.search(r"^# (.+)$", md, re.M).group(1).strip()
    if "Prompt pronto para colar:" in md:
        texto = md.split("Prompt pronto para colar:", 1)[1].strip()
    else:
        m = re.search(r"```\n(.*?)```", md, re.S)
        if not m:
            continue
        texto = m.group(1).strip()
    itens.append({
        "titulo": titulo,
        "arquivo": os.path.basename(rel),
        "gerado": os.path.basename(rel) in gerados,
        "texto": texto,
    })

html_path = os.path.join(ROOT, "app/index.html")
html = open(html_path, encoding="utf-8").read()
novo = "/*PROMPTS*/" + json.dumps(itens, ensure_ascii=False) + "/*FIM-PROMPTS*/"
html, n = re.subn(r"/\*PROMPTS\*/.*?/\*FIM-PROMPTS\*/", lambda _: novo, html, flags=re.S)
assert n == 1, "marcador /*PROMPTS*/ não encontrado em app/index.html"
open(html_path, "w", encoding="utf-8").write(html)
print(f"{len(itens)} prompts copiados para a página")
