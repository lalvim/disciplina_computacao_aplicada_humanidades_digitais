from __future__ import annotations
import json,os,re,xml.etree.ElementTree as ET
from pathlib import Path
import pandas as pd
from apoio_atividades import validar_identificadores_atividades
R=Path(__file__).resolve().parents[1];U=R/"unidade_10"
def f(c):s=c.get("source","");return "".join(s) if isinstance(s,list) else s
def main():
 nbs=sorted(U.glob("*.ipynb"));assert len(nbs)==6
 validar_identificadores_atividades(U,8);ex=(U/"exercicios_unidade_10_texto.md").read_text();assert len(re.findall(r"^## Questão",ex,re.M))==20
 assert len(pd.read_csv(U/"dados"/"documentos.csv"))==12;assert len(pd.read_csv(U/"dados"/"autoridades.csv"))==12
 sv=list((U/"imagens").glob("*.svg"));assert len(sv)==6;ns={"s":"http://www.w3.org/2000/svg"}
 for p in sv:
  x=ET.parse(p).getroot();assert x.find("s:title",ns) is not None and x.find("s:desc",ns) is not None
 ambs={};cwd=Path.cwd()
 try:
  os.chdir(U)
  for p in nbs:
   a={"__name__":"__main__","display":print};m=c=0
   for i,cel in enumerate(json.loads(p.read_text())["cells"],1):
    s=f(cel)
    if cel["cell_type"]=="markdown":m+=1
    else:c+=1;exec(compile(s,f"{p.name}:{i}","exec"),a)
   ambs[p.name]=a;print("OK",p.name,m,c)
 finally:os.chdir(cwd)
 assert len(ambs["01_reconhecimento_de_entidades.ipynb"]["entidades"])>20
 assert ambs["04_avaliacao_validacao_e_rede.ipynb"]["f1"]<1
 print("OK Unidade 10")
if __name__=="__main__":main()
