"""Valida a Unidade 4."""
import json
import math
import os
import re
from pathlib import Path
R=Path(__file__).resolve().parents[1]; U=R/"unidade_04"
def src(c): return "".join(c["source"]) if isinstance(c["source"],list) else c["source"]
def run(p):
 d=json.loads(p.read_text(encoding="utf-8")); env={"__name__":"__main__"}; a=b=0; old=Path.cwd()
 try:
  os.chdir(U)
  for i,x in enumerate(d["cells"],1):
   s=src(x); assert s.strip()
   if x["cell_type"]=="markdown": a+=1
   else: b+=1; assert "Escreva aqui" not in s; exec(compile(s,f"{p.name}:{i}","exec"),env)
 finally: os.chdir(old)
 return a,b,env

def validar_latex(notebooks):
 texto = "\n".join(
  src(c)
  for p in notebooks
  for c in json.loads(p.read_text(encoding="utf-8"))["cells"]
  if c["cell_type"] == "markdown"
 )
 for controle in ["\x08", "\x0c", "\x0b"]:
  assert controle not in texto, "caractere de controle introduzido por LaTeX"
 for p in notebooks:
  for celula in json.loads(p.read_text(encoding="utf-8"))["cells"]:
   if celula["cell_type"] == "markdown":
    conteudo = src(celula)
    assert conteudo.replace("$$", "").count("$") % 2 == 0, (
     f"delimitador LaTeX inline sem par em {p.name}"
    )
 formulas = [
  r"f_k = \sum", r"\bar{x}=\frac", r"\widetilde{x}",
  r"s^2=\frac", r"IQR=Q_3-Q_1", r"L_{\mathrm{inferior}}",
  r"n_{ij}=\sum", r"p_{j\mid i}", r"f(w)=\sum",
  r"PMI(a,b)=", r"TTR(d)=", r"TTR_m(d)=", r"h_j=\sum",
  r"\bar{x}_t=\frac",
 ]
 ausentes = [formula for formula in formulas if formula not in texto]
 assert not ausentes, f"fórmulas LaTeX ausentes: {ausentes}"
 delimitadores = re.findall(r"^\$\$$", texto, re.MULTILINE)
 assert len(delimitadores) == 28
 assert not re.search(r"^\\[\[\]]$", texto, re.MULTILINE)
 assert r"\(" not in texto and r"\)" not in texto

def validar_resultados(ambientes):
 quantitativo = ambientes["01_exploracao_quantitativa.ipynb"]
 resumo = quantitativo["resumo"]
 assert resumo["variancia_amostral"] == quantitativo["x"].var(ddof=1)
 assert quantitativo["limite_inferior"] < quantitativo["limite_superior"]
 assert quantitativo["extremos"]["id_documento"].tolist() == ["D023"]
 somas_linha = quantitativo["proporcoes_por_genero"].sum(axis=1)
 assert all(abs(valor - 1) <= 0.002 for valor in somas_linha)

 textual = ambientes["02_exploracao_textual.ipynb"]
 esperado_bigramas = sum(max(len(tokens) - 1, 0) for tokens in textual["dados"]["tokens"])
 assert textual["total_bigramas"] == esperado_bigramas
 assert sum(textual["marginal_esquerda"].values()) == esperado_bigramas
 assert sum(textual["marginal_direita"].values()) == esperado_bigramas
 assert textual["tamanho_padrao"] == 19
 assert textual["diversidade"]["ttr_19"].notna().all()
 for _, linha in textual["tabela_frequencias"].iterrows():
  assert math.isclose(
   linha["relativa_todos_tokens"], linha["frequencia"] / textual["total_tokens"]
  )
  assert math.isclose(
   linha["relativa_tokens_conteudo"],
   linha["frequencia"] / textual["total_tokens_conteudo"],
  )
 assert {"id_documento", "contexto"}.issubset(
  textual["concordancias"](textual["dados"], "trabalho").columns
 )
 primeira = textual["tabela_colocacoes"].iloc[0]
 a, b = primeira["bigrama"].split()
 esperado_pmi = math.log2(
  primeira["frequencia"] * textual["total_bigramas"]
  / (textual["marginal_esquerda"][a] * textual["marginal_direita"][b])
 )
 assert math.isclose(primeira["pmi"], esperado_pmi)

def main():
 ns=sorted(U.glob("*.ipynb")); assert len(ns)==5; texto=""; tm=tc=0; ambientes={}
 for p in ns:
  a,b,env=run(p); ambientes[p.name]=env; tm+=a;tc+=b; print("OK",p.name,a,b); d=json.loads(p.read_text(encoding="utf-8")); texto+=" ".join(src(x) for x in d["cells"]).lower()
  if p.name=="04_oficina_relatorio_exploratorio.ipynb": assert b==0
 termos=["tipos de variáveis","frequências","mediana","quartis","variância","distribuição","valores extremos","contingência","tokenização","normalização","frequências absoluta e relativa","concordâncias","n-gramas","colocações","vocabulário","diversidade lexical","barras","histograma","boxplot","dispersão","série temporal"]
 assert all(t in texto for t in termos)
 h=(U/"exercicios_unidade_04.html").read_text(encoding="utf-8"); assert h.count('"enunciado":')==18 and "<noscript>" in h
 t=(U/"exercicios_unidade_04_texto.md").read_text(encoding="utf-8"); assert len(re.findall(r"^## Questão",t,re.M))==18
 chave=(U/"gabaritos/gabarito_exercicios_multipla_escolha.md").read_text(encoding="utf-8"); resp=re.findall(r"^\|\s*\d+\s*\|\s*([A-D])",chave,re.M); cor=[chr(65+int(x)) for x in re.findall(r'"correta":\s*(\d+)',h)]; assert resp==cor
 assert len(list((U/"revisores").glob("*.md")))==9 and len(list((U/"revisores/pareceres").glob("*.md")))==7
 validar_latex(ns); validar_resultados(ambientes)
 print("OK 14 fórmulas LaTeX e resultados quantitativos/textuais")
 print("OK 21/21 conteúdos; quiz, gabaritos e revisão; total",tm,tc)
if __name__=="__main__": main()
