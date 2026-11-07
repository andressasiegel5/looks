"""Gera a imagem de um prompt do acervo pela API de imagens da OpenAI.

Uso (na raiz do repositório):
    python3 scripts/gerar_imagem.py prompts/ARQUIVO.md looks/AAAA-MM-tema/grade-6-looks.png [--qualidade medium]

O texto enviado é o que vem depois de "Prompt pronto para colar:" no arquivo .md
(ou o primeiro bloco ``` se não houver essa marca).

A chave não fica no código: na sessão do Claude o proxy de rede injeta a chave salva
para api.openai.com. Fora dela, defina OPENAI_API_KEY.
"""
import argparse, base64, json, os, re, sys, urllib.request

ap = argparse.ArgumentParser()
ap.add_argument("prompt_md")
ap.add_argument("saida")
ap.add_argument("--modelo", default="gpt-image-2")
ap.add_argument("--tamanho", default="1536x1024", help="1536x1024 (grade 2x3), 1024x1536 (vertical) ou 1024x1024")
ap.add_argument("--qualidade", default="medium", choices=["low", "medium", "high"])
a = ap.parse_args()

md = open(a.prompt_md, encoding="utf-8").read()
if "Prompt pronto para colar:" in md:
    texto = md.split("Prompt pronto para colar:", 1)[1].strip()
else:
    m = re.search(r"```\n(.*?)```", md, re.S)
    if not m:
        sys.exit("Não achei o prompt no arquivo.")
    texto = m.group(1).strip()

req = urllib.request.Request(
    "https://api.openai.com/v1/images/generations",
    data=json.dumps({"model": a.modelo, "prompt": texto, "size": a.tamanho,
                     "quality": a.qualidade, "n": 1}).encode(),
    headers={"Content-Type": "application/json",
             "Authorization": "Bearer " + os.environ.get("OPENAI_API_KEY", "proxy-injected")},
)
try:
    with urllib.request.urlopen(req, timeout=300) as r:
        resp = json.load(r)
except urllib.error.HTTPError as e:
    sys.exit(f"Erro da API ({e.code}): {e.read().decode()[:500]}")

img = resp["data"][0]
dados = base64.b64decode(img["b64_json"]) if img.get("b64_json") else urllib.request.urlopen(img["url"]).read()
os.makedirs(os.path.dirname(a.saida) or ".", exist_ok=True)
open(a.saida, "wb").write(dados)
print("Imagem salva em", a.saida, "| uso:", json.dumps(resp.get("usage", {})))
