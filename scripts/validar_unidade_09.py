"""Valida a Unidade 9."""
from __future__ import annotations
import json, os, re, xml.etree.ElementTree as ET
from pathlib import Path
import pandas as pd
from apoio_atividades import validar_identificadores_atividades
RAIZ=Path(__file__).resolve().parents[1]; UNIDADE=RAIZ/"unidade_09"
def fonte(c):
    s=c.get("source",""); return "".join(s) if isinstance(s,list) else s
def executar(p):
    doc=json.loads(p.read_text(encoding="utf-8")); amb={"__name__":"__main__","display":print}; m=c=0; cwd=Path.cwd()
    try:
        os.chdir(UNIDADE)
        for i,cel in enumerate(doc["cells"],1):
            s=fonte(cel); assert s.strip()
            if cel["cell_type"]=="markdown": m+=1
            elif cel["cell_type"]=="code": c+=1; exec(compile(s,f"{p.name}:{i}","exec"),amb)
            else: raise AssertionError("célula inválida")
    finally: os.chdir(cwd)
    return m,c,amb
def main():
    nbs=sorted(UNIDADE.glob("*.ipynb")); assert [p.name for p in nbs]==["00_guia_da_unidade.ipynb","01_padronizacao_distancia_e_kmeans.ipynb","02_hierarquia_caracterizacao_e_estabilidade.ipynb","03_agrupamento_de_documentos.ipynb","04_modelagem_de_topicos_e_tempo.ipynb","05_oficina_agrupamentos_e_temas.ipynb"]
    texto="\n".join(fonte(c).lower() for p in nbs for c in json.loads(p.read_text(encoding="utf-8"))["cells"])
    termos=["aprendizado não supervisionado","padronizar","distância euclidiana","k-means","agrupamento hierárquico","dendrograma","silhueta","estabilidade","índice de rand ajustado","tf-idf","modelagem de tópicos","lda","mistura de tópicos","não adoção","mesmo relatório-notebook"]
    aus=[t for t in termos if t not in texto]; assert not aus,aus
    validar_identificadores_atividades(UNIDADE,8)
    ex=(UNIDADE/"exercicios_unidade_09_texto.md").read_text(encoding="utf-8"); assert [int(x) for x in re.findall(r"^## Questão (\d+)",ex,re.M)]==list(range(1,21))
    inst=pd.read_csv(UNIDADE/"dados"/"instituicoes_culturais.csv"); docs=pd.read_csv(UNIDADE/"dados"/"documentos_temas.csv"); assert len(inst)==120 and len(docs)==180 and inst.id_instituicao.is_unique
    prov=json.loads((UNIDADE/"dados"/"proveniencia.json").read_text(encoding="utf-8")); assert prov["natureza"]=="dados inteiramente fictícios"
    svgs=list((UNIDADE/"imagens").glob("*.svg")); assert len(svgs)==6; ns={"s":"http://www.w3.org/2000/svg"}
    for s in svgs:
        r=ET.parse(s).getroot(); assert r.find("s:title",ns) is not None and r.find("s:desc",ns) is not None and r.attrib.get("role")=="img"
    ambientes={}
    for p in nbs:
        m,c,a=executar(p); ambientes[p.name]=a; print(f"OK {p.name}: {m} Markdown, {c} código")
    km=ambientes["01_padronizacao_distancia_e_kmeans.ipynb"]; assert len(km["tabela_k"])==5 and km["dados"]["cluster_kmeans"].nunique()==3
    hi=ambientes["02_hierarquia_caracterizacao_e_estabilidade.ipynb"]; assert hi["dados"]["cluster_hierarquico"].nunique()==3 and len(hi["estabilidade"])==20
    tx=ambientes["03_agrupamento_de_documentos.ipynb"]; assert 0<=tx["silhueta_texto"]<=1 and len(tx["amostra_casos"])==6
    tp=ambientes["04_modelagem_de_topicos_e_tempo.ipynb"]; assert tp["mistura"].shape==(180,3) and len(tp["evolucao"])==3
    assert len(list((UNIDADE/"gabaritos").glob("gabarito_*.md")))==7
    print("OK Unidade 9: conteúdo, execução, dados, atividades e acessibilidade")
if __name__=="__main__": main()
