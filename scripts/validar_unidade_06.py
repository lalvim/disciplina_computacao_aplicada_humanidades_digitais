"""Valida estrutura, conteúdo, execução e atividades da Unidade 6."""

from __future__ import annotations

import json
import os
import re
import xml.etree.ElementTree as ET
from pathlib import Path

import pandas as pd

from apoio_atividades import validar_identificadores_atividades


RAIZ = Path(__file__).resolve().parents[1]
UNIDADE = RAIZ / "unidade_06"


def fonte(celula: dict) -> str:
    valor = celula.get("source", "")
    return "".join(valor) if isinstance(valor, list) else valor


def executar(caminho: Path) -> tuple[int, int, dict]:
    documento = json.loads(caminho.read_text(encoding="utf-8"))
    assert documento["nbformat"] == 4 and documento["cells"]
    ambiente = {"__name__": "__main__", "display": print}
    markdown = codigo = 0
    cwd = Path.cwd()
    try:
        os.chdir(UNIDADE)
        for numero, celula in enumerate(documento["cells"], 1):
            conteudo = fonte(celula)
            assert conteudo.strip(), f"{caminho.name}: célula {numero} vazia"
            if celula["cell_type"] == "markdown":
                markdown += 1
            elif celula["cell_type"] == "code":
                codigo += 1
                exec(compile(conteudo, f"{caminho.name}:{numero}", "exec"), ambiente)
            else:
                raise AssertionError(f"tipo inválido em {caminho.name}")
    finally:
        os.chdir(cwd)
    return markdown, codigo, ambiente


def validar_conteudo(notebooks: list[Path]) -> None:
    texto = "\n".join(
        fonte(c).lower()
        for p in notebooks
        for c in json.loads(p.read_text(encoding="utf-8"))["cells"]
    )
    termos = [
        "tabela cruzada", "proporções condicionais", "v de cramér",
        "correlação de pearson", "spearman", "correlação não estabelece",
        "confundimento", "coocorrência", "matriz documento-entidade",
        "grafo bipartido", "nós e arestas", "grau", "força",
        "intermediação", "comunidades", "mesmo relatório-notebook",
    ]
    ausentes = [t for t in termos if t not in texto]
    assert not ausentes, f"conteúdos ausentes: {ausentes}"
    assert "u06-a01" in texto and "u06-a07" in texto


def validar_resultados(ambientes: dict[str, dict]) -> None:
    cat = ambientes["01_associacao_variaveis_categoricas.ipynb"]
    assert cat["tabela"].to_numpy().sum() == 80
    assert 0 <= cat["v_cramer"] <= 1
    assert cat["esperada"].shape == cat["observada"].shape

    cor = ambientes["02_correlacao_variaveis_numericas.ipynb"]
    assert -1 <= cor["pearson"] <= 1 and -1 <= cor["spearman"] <= 1
    assert -1 <= cor["pearson_circulacao"] <= 1
    assert len(cor["sem_extremo"]) == 79
    assert set(cor["por_local"].index) == {"Capital", "Interior"}

    coo = ambientes["03_coocorrencia_e_matrizes_relacionais.ipynb"]
    assert coo["incidencia"].shape[0] == 24
    assert (coo["matriz_coocorrencia"].values.diagonal() == 0).all()
    assert len(coo["arestas"]) > 10
    assert {"origem", "destino", "peso", "documentos"} == set(
        coo["fontes_arestas"].columns
    )
    assert coo["fontes_arestas"]["documentos"].str.len().gt(0).all()

    gra = ambientes["04_grafos_centralidade_e_comunidades.ipynb"]
    assert gra["grafo"].number_of_nodes() >= 10
    assert gra["grafo"].number_of_edges() >= 10
    assert not gra["metricas"].isna().any().any()
    assert len(gra["comunidades"]) >= 2
    assert gra["grafo_dirigido"].is_directed()
    assert gra["correspondencia_agregada"]["cartas"].sum() == gra["correspondencia"]["cartas"].sum()
    assert len(gra["correspondencia_agregada"]) == 6
    assert {"entrada", "saída", "cartas_enviadas", "cartas_recebidas"} == set(
        gra["graus_dirigidos"].columns
    )


def validar_arquivos() -> None:
    dados = {p.name for p in (UNIDADE / "dados").iterdir() if p.is_file()}
    assert dados == {
        "registros_associacao.csv", "documentos_entidades.csv",
        "correspondencia_direta.csv", "arestas_coocorrencia.csv", "proveniencia.json",
    }
    assert len(pd.read_csv(UNIDADE / "dados" / "registros_associacao.csv")) == 80
    assert len(pd.read_csv(UNIDADE / "dados" / "documentos_entidades.csv")) == 24
    prov = json.loads((UNIDADE / "dados" / "proveniencia.json").read_text(encoding="utf-8"))
    assert prov["natureza"] == "dados inteiramente fictícios"

    svgs = sorted((UNIDADE / "imagens").glob("*.svg"))
    assert len(svgs) == 6
    ns = {"svg": "http://www.w3.org/2000/svg"}
    for svg in svgs:
        raiz = ET.parse(svg).getroot()
        assert raiz.find("svg:title", ns) is not None
        assert raiz.find("svg:desc", ns) is not None
        assert raiz.attrib.get("role") == "img"


def validar_exercicios() -> None:
    texto = (UNIDADE / "exercicios_unidade_06_texto.md").read_text(encoding="utf-8")
    numeros = [int(x) for x in re.findall(r"^## Questão (\d+)", texto, re.MULTILINE)]
    assert numeros == list(range(1, 21))
    validar_identificadores_atividades(UNIDADE, 8)
    assert len(list((UNIDADE / "gabaritos").glob("gabarito_*.md"))) == 7


def main() -> None:
    notebooks = sorted(UNIDADE.glob("*.ipynb"))
    assert [p.name for p in notebooks] == [
        "00_guia_da_unidade.ipynb",
        "01_associacao_variaveis_categoricas.ipynb",
        "02_correlacao_variaveis_numericas.ipynb",
        "03_coocorrencia_e_matrizes_relacionais.ipynb",
        "04_grafos_centralidade_e_comunidades.ipynb",
        "05_oficina_associacao_ou_rede.ipynb",
    ]
    validar_conteudo(notebooks); validar_arquivos(); validar_exercicios()
    ambientes = {}
    for caminho in notebooks:
        markdown, codigo, ambiente = executar(caminho)
        ambientes[caminho.name] = ambiente
        print(f"OK {caminho.name}: {markdown} Markdown, {codigo} código")
    validar_resultados(ambientes)
    print("OK Unidade 6: conteúdo, execução, dados, atividades e acessibilidade")


if __name__ == "__main__":
    main()
