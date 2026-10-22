"""Valida estrutura, conteúdo, execução e atividades da Unidade 7."""

from __future__ import annotations

import json
import os
import re
import xml.etree.ElementTree as ET
from pathlib import Path

import pandas as pd

from apoio_atividades import validar_identificadores_atividades


RAIZ = Path(__file__).resolve().parents[1]
UNIDADE = RAIZ / "unidade_07"


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
        "variável de resposta", "variável explicativa", "regressão linear simples",
        "regressão múltipla", "categoria de referência", "controle estatístico",
        "interação", "resíduo", "alavancagem", "qualidade do ajuste", "regressão logística",
        "probabilidade", "chance", "razão de chances", "associação condicionada",
        "não demonstra causalidade", "mesmo relatório-notebook", "não adoção fundamentada",
    ]
    ausentes = [termo for termo in termos if termo not in texto]
    assert not ausentes, f"conteúdos ausentes: {ausentes}"
    assert "u07-a01" in texto and "u07-a07" in texto


def validar_resultados(ambientes: dict[str, dict]) -> None:
    simples = ambientes["01_regressao_linear_simples.ipynb"]["simples"]
    assert len(simples["previstos"]) == 150
    assert 0 < simples["r2"] < 1 and simples["rmse"] > 0

    multiplo = ambientes["02_regressao_multipla_e_categorias.ipynb"]
    assert multiplo["referencia"] == "Centro-Oeste"
    assert len(multiplo["com_regiao"]["coeficientes"]) == 9
    assert multiplo["cenarios"]["previsao"].notna().all()

    diag = ambientes["03_interacoes_residuos_e_qualidade.ipynb"]
    assert len(diag["modelo_interacao"]["coeficientes"]) == 4
    assert diag["diagnostico"].loc[diag["diagnostico"]["id_municipio"] == "M150", "residuo"].abs().iloc[0] > 2
    assert set(diag["sensibilidade"]["modelo"]) == {"todos os casos", "sem M150"}

    log = ambientes["04_regressao_logistica.ipynb"]
    assert ((log["probabilidades"] > 0) & (log["probabilidades"] < 1)).all()
    assert len(log["coeficientes_logisticos"]) == 5
    assert log["calibracao_descritiva"]["n"].sum() == 150


def validar_arquivos() -> None:
    assert {p.name for p in (UNIDADE / "dados").iterdir() if p.is_file()} == {
        "municipios_culturais.csv", "dicionario_dados.csv", "proveniencia.json"
    }
    dados = pd.read_csv(UNIDADE / "dados" / "municipios_culturais.csv")
    assert len(dados) == 150 and dados["id_municipio"].is_unique
    assert set(dados["biblioteca_publica"]) == {"sim", "não"}
    prov = json.loads((UNIDADE / "dados" / "proveniencia.json").read_text(encoding="utf-8"))
    assert prov["natureza"] == "dados inteiramente fictícios"
    assert "M150" in prov["caso_atipico"]

    svgs = sorted((UNIDADE / "imagens").glob("*.svg"))
    assert len(svgs) == 7
    ns = {"svg": "http://www.w3.org/2000/svg"}
    for svg in svgs:
        raiz = ET.parse(svg).getroot()
        assert raiz.find("svg:title", ns) is not None
        assert raiz.find("svg:desc", ns) is not None
        assert raiz.attrib.get("role") == "img"


def validar_exercicios() -> None:
    texto = (UNIDADE / "exercicios_unidade_07_texto.md").read_text(encoding="utf-8")
    numeros = [int(x) for x in re.findall(r"^## Questão (\d+)", texto, re.MULTILINE)]
    assert numeros == list(range(1, 21))
    validar_identificadores_atividades(UNIDADE, 8)
    assert len(list((UNIDADE / "gabaritos").glob("gabarito_*.md"))) == 7


def validar_latex(notebooks: list[Path]) -> None:
    controles = {"\x08", "\x0c", "\x07", "\r"}
    for caminho in notebooks:
        for celula in json.loads(caminho.read_text(encoding="utf-8"))["cells"]:
            if celula["cell_type"] == "markdown":
                texto = fonte(celula)
                assert not any(c in texto for c in controles), f"controle inválido em {caminho.name}"
                assert texto.count("$$") % 2 == 0, f"blocos LaTeX ímpares em {caminho.name}"


def main() -> None:
    notebooks = sorted(UNIDADE.glob("*.ipynb"))
    assert [p.name for p in notebooks] == [
        "00_guia_da_unidade.ipynb",
        "01_regressao_linear_simples.ipynb",
        "02_regressao_multipla_e_categorias.ipynb",
        "03_interacoes_residuos_e_qualidade.ipynb",
        "04_regressao_logistica.ipynb",
        "05_oficina_modelo_associativo.ipynb",
    ]
    validar_conteudo(notebooks)
    validar_latex(notebooks)
    validar_arquivos()
    validar_exercicios()
    ambientes = {}
    for caminho in notebooks:
        markdown, codigo, ambiente = executar(caminho)
        ambientes[caminho.name] = ambiente
        print(f"OK {caminho.name}: {markdown} Markdown, {codigo} código")
    validar_resultados(ambientes)
    print("OK Unidade 7: conteúdo, execução, dados, atividades e acessibilidade")


if __name__ == "__main__":
    main()
