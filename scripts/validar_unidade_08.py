"""Valida estrutura, execução, dados e atividades da Unidade 8."""

from __future__ import annotations

import json
import os
import re
import xml.etree.ElementTree as ET
from pathlib import Path

import pandas as pd

from apoio_atividades import validar_identificadores_atividades

RAIZ = Path(__file__).resolve().parents[1]
UNIDADE = RAIZ / "unidade_08"


def fonte(c: dict) -> str:
    s = c.get("source", ""); return "".join(s) if isinstance(s, list) else s


def executar(caminho: Path) -> tuple[int, int, dict]:
    doc = json.loads(caminho.read_text(encoding="utf-8")); ambiente = {"__name__": "__main__", "display": print}; md = cod = 0; cwd = Path.cwd()
    try:
        os.chdir(UNIDADE)
        for i, c in enumerate(doc["cells"], 1):
            texto = fonte(c); assert texto.strip(), f"{caminho.name}: célula {i} vazia"
            if c["cell_type"] == "markdown": md += 1
            elif c["cell_type"] == "code": cod += 1; exec(compile(texto, f"{caminho.name}:{i}", "exec"), ambiente)
            else: raise AssertionError("tipo de célula inválido")
    finally: os.chdir(cwd)
    return md, cod, ambiente


def main() -> None:
    notebooks = sorted(UNIDADE.glob("*.ipynb"))
    assert [p.name for p in notebooks] == ["00_guia_da_unidade.ipynb", "01_categorias_anotacao_e_concordancia.ipynb", "02_treinamento_teste_e_linha_de_base.ipynb", "03_modelos_metricas_e_erros.ipynb", "04_classificacao_textual_tfidf_e_embeddings.ipynb", "05_oficina_classificacao.ipynb"]
    texto = "\n".join(fonte(c).lower() for p in notebooks for c in json.loads(p.read_text(encoding="utf-8"))["cells"])
    termos = ["guia de anotação", "concordância", "treinamento", "teste", "linha de base", "regressão logística", "árvore", "tf-idf", "embeddings", "acurácia", "precisão", "revocação", "matriz de confusão", "desbalanceamento", "análise de erros", "grupos", "mesmo relatório-notebook", "não adoção"]
    assert not [t for t in termos if t not in texto]
    validar_identificadores_atividades(UNIDADE, 8)
    exercicios = (UNIDADE/"exercicios_unidade_08_texto.md").read_text(encoding="utf-8")
    assert [int(x) for x in re.findall(r"^## Questão (\d+)", exercicios, re.M)] == list(range(1, 21))
    dados = pd.read_csv(UNIDADE/"dados"/"documentos_classificacao.csv")
    assert len(dados) == 160 and dados["id_documento"].is_unique and set(dados["classe_alvo"]) == {"relevante", "não relevante"}
    assert len(pd.read_csv(UNIDADE/"dados"/"amostra_anotacao.csv")) == 32
    prov = json.loads((UNIDADE/"dados"/"proveniencia.json").read_text(encoding="utf-8")); assert prov["natureza"] == "dados inteiramente fictícios"
    svgs = list((UNIDADE/"imagens").glob("*.svg")); assert len(svgs) == 6; ns = {"s": "http://www.w3.org/2000/svg"}
    for arq in svgs:
        raiz = ET.parse(arq).getroot(); assert raiz.find("s:title", ns) is not None and raiz.find("s:desc", ns) is not None and raiz.attrib.get("role") == "img"
    ambientes = {}
    for p in notebooks:
        m, c, a = executar(p); ambientes[p.name] = a; print(f"OK {p.name}: {m} Markdown, {c} código")
    ano = ambientes["01_categorias_anotacao_e_concordancia.ipynb"]; assert .5 < ano["kappa"] < 1 and len(ano["discordancias"]) > 0
    div = ambientes["02_treinamento_teste_e_linha_de_base.ipynb"]; assert len(div["treino"]) == 120 and len(div["teste"]) == 40
    mod = ambientes["03_modelos_metricas_e_erros.ipynb"]; assert set(mod["tabela_metricas"].index) == {"logística", "árvore"} and mod["metricas_grupo"]["n"].sum() == 40
    txt = ambientes["04_classificacao_textual_tfidf_e_embeddings.ipynb"]; assert len(txt["previsto_texto"]) == 40 and (txt["metricas_texto"].between(0, 1)).all()
    assert len(list((UNIDADE/"gabaritos").glob("gabarito_*.md"))) == 7
    print("OK Unidade 8: conteúdo, execução, dados, atividades e acessibilidade")


if __name__ == "__main__": main()
