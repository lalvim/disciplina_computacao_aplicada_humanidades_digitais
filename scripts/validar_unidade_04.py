"""Valida a Unidade 4."""
import json,os,re
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
 return a,b
def main():
 ns=sorted(U.glob("*.ipynb")); assert len(ns)==5; texto=""; tm=tc=0
 for p in ns:
  a,b=run(p); tm+=a;tc+=b; print("OK",p.name,a,b); d=json.loads(p.read_text(encoding="utf-8")); texto+=" ".join(src(x) for x in d["cells"]).lower()
 if p.name=="04_oficina_relatorio_exploratorio.ipynb": assert b==0
 termos=["tipos de variáveis","frequências","mediana","quartis","variância","distribuição","valores extremos","contingência","tokenização","normalização","frequências absoluta e relativa","concordâncias","n-gramas","colocações","vocabulário","diversidade lexical","barras","histograma","boxplot","dispersão","série temporal"]
 assert all(t in texto for t in termos)
 h=(U/"exercicios_unidade_04.html").read_text(encoding="utf-8"); assert h.count('"enunciado":')==18 and "<noscript>" in h
 t=(U/"exercicios_unidade_04_texto.md").read_text(encoding="utf-8"); assert len(re.findall(r"^## Questão",t,re.M))==18
 chave=(U/"gabaritos/gabarito_exercicios_multipla_escolha.md").read_text(encoding="utf-8"); resp=re.findall(r"^\|\s*\d+\s*\|\s*([A-D])",chave,re.M); cor=[chr(65+int(x)) for x in re.findall(r'"correta":\s*(\d+)',h)]; assert resp==cor
 assert len(list((U/"revisores").glob("*.md")))==9 and len(list((U/"revisores/pareceres").glob("*.md")))==7
 print("OK 21/21 conteúdos; quiz, gabaritos e revisão; total",tm,tc)
if __name__=="__main__": main()
