"""Valida conteúdo, execução, resultados e acessibilidade da Unidade 5."""

from __future__ import annotations

import json
import math
import os
import re
import struct
import xml.etree.ElementTree as ET
from pathlib import Path

import pandas as pd

from apoio_atividades import validar_identificadores_atividades

RAIZ = Path(__file__).resolve().parents[1]
UNIDADE = RAIZ / "unidade_05"


def fonte(celula: dict) -> str:
    valor = celula.get("source", "")
    return "".join(valor) if isinstance(valor, list) else valor


def executar(caminho: Path) -> tuple[int, int, dict]:
    documento = json.loads(caminho.read_text(encoding="utf-8"))
    assert documento["nbformat"] == 4 and documento["cells"]
    ambiente = {"__name__": "__main__"}
    textos = codigos = 0
    anterior = Path.cwd()
    try:
        os.chdir(UNIDADE)
        for numero, celula in enumerate(documento["cells"], 1):
            conteudo = fonte(celula)
            assert conteudo.strip(), f"{caminho.name}: célula {numero} vazia"
            if celula["cell_type"] == "markdown":
                textos += 1
            elif celula["cell_type"] == "code":
                codigos += 1
                assert "Escreva aqui" not in conteudo
                exec(compile(conteudo, f"{caminho.name}:{numero}", "exec"), ambiente)
            else:
                raise AssertionError(f"tipo inválido em {caminho.name}")
    finally:
        os.chdir(anterior)
    return textos, codigos, ambiente


def validar_conteudos(notebooks: list[Path]) -> None:
    conteudo = " ".join(
        fonte(celula).lower()
        for caminho in notebooks
        for celula in json.loads(caminho.read_text(encoding="utf-8"))["cells"]
    )
    termos = {
        "médias": "médias",
        "medianas": "medianas",
        "proporções": "proporções",
        "diferenças absolutas": "diferenças absolutas",
        "diferenças relativas": "absolutas e relativas",
        "variabilidade amostral": "variabilidade amostral",
        "intervalos de confiança": "intervalo de confiança",
        "testes de hipótese": "teste de permutação",
        "tamanho de efeito": "tamanho de efeito",
        "significância e relevância": "significância e relevância substantiva",
        "bag of words": "bag of words",
        "matriz documento-termo": "matriz documento-termo",
        "tf-idf": "tf-idf",
        "jaccard": "similaridade de jaccard",
        "cosseno": "similaridade de cosseno",
        "edição": "distância de edição",
        "autores/períodos/coleções": "comparar autores, períodos e coleções",
        "documentos semelhantes": "identificar documentos semelhantes",
        "versões": "comparação de versões",
        "questões críticas": "o que significa considerar dois textos semelhantes",
    }
    ausentes = [rotulo for rotulo, termo in termos.items() if termo not in conteudo]
    assert not ausentes, f"conteúdos ausentes: {ausentes}"


def validar_latex(notebooks: list[Path]) -> None:
    conteudo = "\n".join(
        fonte(celula)
        for caminho in notebooks
        for celula in json.loads(caminho.read_text(encoding="utf-8"))["cells"]
        if celula["cell_type"] == "markdown"
    )
    for controle in ["\x08", "\x0c", "\x0b"]:
        assert controle not in conteudo
    for caminho in notebooks:
        for celula in json.loads(caminho.read_text(encoding="utf-8"))["cells"]:
            if celula["cell_type"] == "markdown":
                texto = fonte(celula)
                assert texto.replace("$$", "").count("$") % 2 == 0, caminho.name
    formulas = [
        r"\Delta=\hat{\theta}_A-\hat{\theta}_B",
        r"\Delta_{rel}=\frac",
        r"d=\frac{\bar{x}_A",
        r"IC_{95\%}",
        r"\sum_{m=1}^{M}",
        r"X_{d,t}=c(t,d)",
        r"df(t)=\sum",
        r"tfidf(t,d)=",
        r"J(A,B)=\frac",
        r"\cos(\mathbf{x},\mathbf{y})",
        r"D_{i,j}=\min",
    ]
    ausentes = [f for f in formulas if f not in conteudo]
    assert not ausentes, f"fórmulas ausentes: {ausentes}"
    assert not re.search(r"^\\[\[\]]$", conteudo, re.MULTILINE)


def validar_resultados(ambientes: dict[str, dict]) -> None:
    est = ambientes["01_estimativas_e_tamanhos_de_efeito.ipynb"]
    esperado = est["medidas"].loc["Capital", "media_palavras"] - est["medidas"].loc["Interior", "media_palavras"]
    assert math.isclose(est["diferenca_absoluta"], esperado)
    assert len(est["a"]) == len(est["b"]) == 12
    assert not math.isclose(est["sensibilidade"].iloc[0], est["sensibilidade"].iloc[1])

    inf = ambientes["02_incerteza_e_testes_de_hipotese.ipynb"]
    assert len(inf["diferencas_bootstrap"]) == 4000
    assert len(inf["diferencas_nulas"]) == 5000
    assert inf["limite_inferior"] < inf["diferenca_observada"] < inf["limite_superior"]
    assert 0 <= inf["valor_p"] <= 1

    rep = ambientes["03_representacao_vetorial_de_textos.ipynb"]
    assert rep["matriz_contagens"].shape == (12, 53)
    assert (rep["frequencia_documento"] == rep["matriz_contagens"].gt(0).sum()).all()
    assert (rep["matriz_tfidf"] >= 0).all().all()
    assert not rep["contraste_periodos"].isna().any()

    sim = ambientes["04_similaridade_documentos_e_versoes.ipynb"]
    assert math.isclose(sim["jaccard"](["a", "b", "c"], ["b", "c", "d"]), 0.5)
    assert math.isclose(sim["cosseno"]([1, 0], [1, 0]), 1.0)
    assert sim["levenshtein"]("gato", "rato") == 1
    assert len(sim["tabela_edicao"]) == 3
    assert set(sim["ranking"].columns) == {"Jaccard", "cosseno contagens", "cosseno TF-IDF"}
    ordem_j = sim["ranking"]["Jaccard"].sort_values(ascending=False).index.tolist()
    ordem_c = sim["ranking"]["cosseno contagens"].sort_values(ascending=False).index.tolist()
    assert ordem_j != ordem_c, "o exemplo deve produzir sensibilidade à métrica"


def validar_dados() -> None:
    esperados = {"documentos.csv", "documentos_comparacao.csv", "versoes_textuais.csv", "proveniencia.json"}
    encontrados = {p.name for p in (UNIDADE / "dados").iterdir() if p.is_file()}
    assert encontrados == esperados
    original = pd.read_csv(UNIDADE / "dados" / "documentos.csv")
    derivado = pd.read_csv(UNIDADE / "dados" / "documentos_comparacao.csv")
    assert len(original) == 24 and len(derivado) == 12
    assert derivado["id_documento"].tolist() == original.head(12)["id_documento"].tolist()
    assert (derivado["texto"] != derivado["texto_comparacao"]).all()
    proveniencia = json.loads((UNIDADE / "dados" / "proveniencia.json").read_text(encoding="utf-8"))
    assert proveniencia["natureza"] == "dados inteiramente fictícios"


def validar_exercicios_e_gabaritos() -> None:
    exercicios = (UNIDADE / "exercicios_unidade_05_texto.md").read_text(encoding="utf-8")
    numeros = [int(n) for n in re.findall(r"^## Questão (\d+)", exercicios, re.MULTILINE)]
    assert numeros == list(range(1, 21))
    assert len(re.findall(r"^- \[ \] \*\*[A-D]\.\*\*", exercicios, re.MULTILINE)) == 80
    assert not list(UNIDADE.glob("*.html")) and not list(RAIZ.glob("scripts/*unidade_05*html*"))
    pasta = UNIDADE / "gabaritos"
    esperados = {
        "README.md", "gabarito_00_guia.md", "gabarito_01_estimativas.md", "gabarito_02_inferencia.md",
        "gabarito_03_representacao_textual.md", "gabarito_04_similaridade.md",
        "gabarito_05_oficina.md", "gabarito_exercicios_multipla_escolha.md",
    }
    assert {p.name for p in pasta.iterdir() if p.is_file()} == esperados
    chave = (pasta / "gabarito_exercicios_multipla_escolha.md").read_text(encoding="utf-8")
    assert len(re.findall(r"^\|\s*\d+\s*\|\s*[A-D]\s*\|", chave, re.MULTILINE)) == 20
    for nome in esperados - {"README.md"}:
        conteudo = (pasta / nome).read_text(encoding="utf-8")
        assert "Exemplo" in conteudo or "exemplo" in conteudo


def validar_imagens() -> None:
    pasta = UNIDADE / "imagens"
    esperados = {
        "README.md", "00_abertura_conceitual.png", "00_percurso_comparacao.svg",
        "01_diferenca_incerteza_relevancia.svg", "02_fluxo_bootstrap.svg",
        "02_distribuicao_nula.svg", "02_mapa_interpretacao.svg",
        "03_fluxo_matriz_documento_termo.svg", "03_anatomia_tfidf.svg",
        "04_escolha_metrica.svg", "04_distancia_edicao.svg",
        "04_vizinhos_documentais.svg", "05_cadeia_argumento.svg",
    }
    encontrados = {p.name for p in pasta.iterdir() if p.is_file()}
    assert encontrados == esperados, encontrados ^ esperados
    namespace = {"svg": "http://www.w3.org/2000/svg"}
    for caminho in pasta.glob("*.svg"):
        raiz = ET.parse(caminho).getroot()
        assert raiz.find("svg:title", namespace) is not None
        desc = raiz.find("svg:desc", namespace)
        assert desc is not None and len((desc.text or "").split()) >= 8
        assert raiz.attrib.get("role") == "img" and "aria-labelledby" in raiz.attrib
    png = (pasta / "00_abertura_conceitual.png").read_bytes()
    assert png[:8] == b"\x89PNG\r\n\x1a\n"
    largura, altura = struct.unpack(">II", png[16:24])
    assert largura >= 1200 and altura >= 500
    inventario = (pasta / "README.md").read_text(encoding="utf-8")
    notebooks = "\n".join(p.read_text(encoding="utf-8") for p in UNIDADE.glob("*.ipynb"))
    for nome in esperados - {"README.md"}:
        assert nome in inventario and nome in notebooks


def validar_referencias_revisores() -> None:
    referencias = (UNIDADE / "referencias.md").read_text(encoding="utf-8")
    for termo in ["WASSERSTEIN", "EFRON", "MANNING", "LEVENSHTEIN", "DRUCKER", "D'IGNAZIO", "JOCKERS", "UNDERWOOD"]:
        assert termo in referencias
    assert referencias.count("https://") >= 7
    revisores = UNIDADE / "revisores"
    assert len(list(revisores.glob("*.md"))) == 9
    assert len(list((revisores / "pareceres").glob("*.md"))) == 8
    consolidado = (revisores / "pareceres" / "parecer_consolidado.md").read_text(encoding="utf-8")
    assert "Aprovada com ajustes baixos" in consolidado and "Nenhum achado alto ou bloqueante" in consolidado


def validar_encadeamento() -> None:
    marcadores = {
        "00_guia_da_unidade.ipynb": ["A Unidade 4 descreveu padrões", "O diagnóstico torna visíveis", "Siga para o Notebook 01"],
        "01_estimativas_e_tamanhos_de_efeito.ipynb": ["uma única medida não deve apagar", "A etapa seguinte retorna aos registros", "Leve o quadro ao Notebook 02"],
        "02_incerteza_e_testes_de_hipotese.ipynb": ["O Notebook 01 estimou", "Um teste responde a outra pergunta", "No Notebook 03"],
        "03_representacao_vetorial_de_textos.ipynb": ["Para comparar documentos", "A matriz torna os documentos comparáveis", "Leve a matriz e suas regras"],
        "04_similaridade_documentos_e_versoes.ipynb": ["O Notebook 03 produziu", "Essa divergência é material analítico", "Leve o relatório à oficina"],
        "05_oficina_analise_comparativa.ipynb": ["Este notebook reúne os produtos", "A sensibilidade compara agregados", "Na Unidade 6"],
    }
    for nome, termos in marcadores.items():
        documento = json.loads((UNIDADE / nome).read_text(encoding="utf-8"))
        conteudo = " ".join(re.sub(r"\s+", " ", fonte(c)).strip() for c in documento["cells"])
        ausentes = [termo for termo in termos if termo not in conteudo]
        assert not ausentes, f"{nome}: {ausentes}"


def main() -> None:
    notebooks = sorted(UNIDADE.glob("*.ipynb"))
    assert len(notebooks) == 6
    ambientes = {}
    total_texto = total_codigo = 0
    for caminho in notebooks:
        a, b, ambiente = executar(caminho)
        ambientes[caminho.name] = ambiente
        total_texto += a
        total_codigo += b
        if caminho.name == "05_oficina_analise_comparativa.ipynb":
            assert b == 0
        print(f"OK {caminho.name}: {a} Markdown, {b} código")
    validar_conteudos(notebooks)
    validar_latex(notebooks)
    validar_resultados(ambientes)
    validar_dados()
    validar_exercicios_e_gabaritos()
    validar_identificadores_atividades(UNIDADE, 8)
    validar_imagens()
    validar_referencias_revisores()
    validar_encadeamento()
    print("OK conteúdo: 20/20 tópicos quantitativos, textuais e críticos")
    print("OK fórmulas e resultados: estimativas, reamostragem e métricas textuais")
    print("OK dados, 20 exercícios, 7 gabaritos com exemplos e ausência de HTML")
    print("OK atividades: U05-A01 a U05-A08 associadas aos gabaritos")
    print("OK imagens: 1 abertura e 11 SVGs acessíveis e documentados")
    print("OK revisão: seis pareceres, sem achados altos ou bloqueantes")
    print("OK encadeamento: produtos cumulativos nos 6 notebooks")
    print(f"OK total: {total_texto} células Markdown, {total_codigo} de código")


if __name__ == "__main__":
    main()
