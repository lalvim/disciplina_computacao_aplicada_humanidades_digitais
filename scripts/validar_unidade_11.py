from __future__ import annotations
import json,os,re,xml.etree.ElementTree as ET
from pathlib import Path
import pandas as pd
from apoio_atividades import validar_identificadores_atividades
R=Path(__file__).resolve().parents[1];U=R/"unidade_11"
def f(c):s=c.get("source","");return "".join(s) if isinstance(s,list) else s
def main():
 nbs=sorted(U.glob("*.ipynb"));assert len(nbs)==6;validar_identificadores_atividades(U,8)
 assert len(re.findall(r"^## Questão",(U/"exercicios_unidade_11_texto.md").read_text(),re.M))==20
 assert len(pd.read_csv(U/"dados"/"serie_cultural.csv"))==61;assert len(pd.read_csv(U/"dados"/"territorios.csv"))==16
 ns={"s":"http://www.w3.org/2000/svg"};sv=list((U/"imagens").glob("*.svg"));assert len(sv)==6
 for p in sv:
  x=ET.parse(p).getroot();assert x.find("s:title",ns) is not None and x.find("s:desc",ns) is not None
 cwd=Path.cwd();ambs={}
 try:
  os.chdir(U)
  for p in nbs:
   a={"__name__":"__main__","display":print};m=c=0
   for i,z in enumerate(json.loads(p.read_text())["cells"],1):
    s=f(z)
    if z["cell_type"]=="markdown":m+=1;assert "\t" not in s
    else:c+=1;exec(compile(s,f"{p.name}:{i}","exec"),a)
   ambs[p.name]=a;print("OK",p.name,m,c)
 finally:os.chdir(cwd)
 assert "taxa_bruta" in ambs["04_distribuicao_espacial_e_taxas.ipynb"]["d"]
 print("OK Unidade 11")
if __name__=="__main__":main()
