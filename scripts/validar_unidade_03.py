"""Valida estrutura, execução e integridade da Unidade 3."""

from __future__ import annotations

import hashlib
import json
import os
import re
import struct
import xml.etree.ElementTree as ET
from pathlib import Path

import pandas as pd

RAIZ = Path(__file__).resolve().parents[1]
UNIDADE = RAIZ / "unidade_03"
BRUTOS = UNIDADE / "dados" / "brutos"


def fonte(celula: dict) -> str:
    valor = celula.get("source", "")
    return "".join(valor) if isinstance(valor, list) else valor


def hashes_brutos() -> dict[str, str]:
    return {p.name: hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(BRUTOS.iterdir()) if p.is_file()}


def executar(caminho: Path) -> tuple[int, int]:
    doc = json.loads(caminho.read_text(encoding="utf-8"))
    ambiente = {"__name__": "__main__"}
    textos = codigos = 0
    anterior = Path.cwd()
    try:
        os.chdir(UNIDADE)
        for n, celula in enumerate(doc["cells"], 1):
            conteudo = fonte(celula)
            assert conteudo.strip(), f"{caminho.name}: célula {n} vazia"
            if celula["cell_type"] == "markdown":
                textos += 1
            elif celula["cell_type"] == "code":
                codigos += 1
                assert "Escreva aqui" not in conteudo
                exec(compile(conteudo, f"{caminho.name}:{n}", "exec"), ambiente)
            else:
                raise AssertionError("tipo de célula inválido")
    finally:
        os.chdir(anterior)
    return textos, codigos


def validar_cobertura() -> None:
    conteudo = ""
    for caminho in sorted(UNIDADE.glob("*.ipynb")):
        doc = json.loads(caminho.read_text(encoding="utf-8"))
        conteudo += "\n".join(fonte(c) for c in doc["cells"]).lower()
    termos = {
        "estrutura tabular": "estrutura tabular", "formatos": "csv", "extração": "extração de pdf",
        "ocr": "ocr", "base pública": "base pública", "largo e longo": "largo e longo",
        "limpeza": "limpeza", "padronização": "padronizado", "duplicatas": "duplicata",
        "ausentes": "datas, códigos e ausências", "junções": "cardinalidade", "integração": "integrar textos",
        "notebooks": "notebooks: ordem",
    }
    ausentes = [r for r,t in termos.items() if t not in conteudo]
    assert not ausentes, f"conteúdos ausentes: {', '.join(ausentes)}"


def validar_arquivos() -> None:
    extensoes = {p.suffix.lower() for p in BRUTOS.iterdir() if p.is_file()}
    for extensao in [".csv", ".xlsx", ".json", ".xml", ".txt", ".pdf", ".png"]:
        assert extensao in extensoes, f"formato ausente: {extensao}"
    assert len(list((UNIDADE / "dados" / "derivados").glob("*.csv"))) == 3

    entradas_ocr = {
        "pagina_digitalizada.png",
        "pagina_digitalizada_degradada.png",
        "ocr_referencia.txt",
        "ocr_precomputado.txt",
        "ocr_precomputado_degradado.txt",
    }
    assert entradas_ocr.issubset({p.name for p in BRUTOS.iterdir()})
    referencia = (BRUTOS / "ocr_referencia.txt").read_text(encoding="utf-8").strip()
    limpa = (BRUTOS / "ocr_precomputado.txt").read_text(encoding="utf-8").strip()
    degradada = (BRUTOS / "ocr_precomputado_degradado.txt").read_text(encoding="utf-8").strip()
    assert limpa == referencia and degradada != referencia


def dimensoes_png(caminho: Path) -> tuple[int, int]:
    dados = caminho.read_bytes()
    assert dados[:8] == b"\x89PNG\r\n\x1a\n"
    return struct.unpack(">II", dados[16:24])


def validar_imagens() -> None:
    pasta = UNIDADE / "imagens"
    esperados = {
        "README.md",
        "00_abertura_conceitual.png",
        "00_percurso_unidade.svg",
        "01_pdf_texto_imagem_ocr.svg",
        "02_largo_longo.svg",
        "02_transformacao_rastreavel.svg",
        "03_cardinalidades.svg",
        "03_modelo_relacional_base.svg",
        "04_pacote_processavel.svg",
    }
    encontrados = {p.name for p in pasta.iterdir() if p.is_file()}
    assert encontrados == esperados, f"imagens divergentes: {encontrados ^ esperados}"

    referencias = []
    referencias_ocr = []
    for notebook in sorted(UNIDADE.glob("*.ipynb")):
        doc = json.loads(notebook.read_text(encoding="utf-8"))
        markdown = "\n".join(
            fonte(c) for c in doc["cells"] if c["cell_type"] == "markdown"
        )
        referencias.extend(re.findall(r"!\[([^]]+)\]\((imagens/[^)]+)\)", markdown))
        referencias_ocr.extend(
            re.findall(r"!\[([^]]+)\]\((dados/brutos/pagina_digitalizada[^)]+)\)", markdown)
        )

    assert len(referencias) == 8 and len({c for _, c in referencias}) == 8
    assert len(referencias_ocr) == 2 and len({c for _, c in referencias_ocr}) == 2
    for alt, relativo in referencias + referencias_ocr:
        assert len(alt.split()) >= 6, f"texto alternativo insuficiente: {relativo}"
        assert (UNIDADE / relativo).is_file(), f"imagem ausente: {relativo}"

    namespace = {"svg": "http://www.w3.org/2000/svg"}
    for caminho in sorted(pasta.glob("*.svg")):
        raiz = ET.parse(caminho).getroot()
        titulo = raiz.find("svg:title", namespace)
        descricao = raiz.find("svg:desc", namespace)
        assert titulo is not None and (titulo.text or "").strip()
        assert descricao is not None and len((descricao.text or "").split()) >= 8
        assert raiz.attrib.get("role") == "img"
        assert raiz.attrib.get("aria-labelledby") == "titulo descricao"

    largura, altura = dimensoes_png(pasta / "00_abertura_conceitual.png")
    assert largura >= 1200 and altura >= 500
    for nome in ["pagina_digitalizada.png", "pagina_digitalizada_degradada.png"]:
        largura, altura = dimensoes_png(BRUTOS / nome)
        assert largura >= 1200 and altura >= 200

    ficha = (pasta / "README.md").read_text(encoding="utf-8")
    for nome in esperados - {"README.md"}:
        assert nome in ficha, f"imagem sem documentação: {nome}"


def validar_resultados_semanticos() -> None:
    tabela = pd.read_csv(
        UNIDADE / "dados" / "intermediarios" / "catalogo_normalizado.csv",
        dtype={"id_documento": "string", "ano_documento": "Int64"},
    ).set_index("id_documento")
    datas = {
        "D001": "1890-01-05",
        "D002": "1891-02-06",
        "D004": "1893-03-12",
        "D006": "1900-08-20",
        "D006-copia": "1900-08-20",
        "D007": "1901-04-09",
    }
    for identificador, data in datas.items():
        assert tabela.loc[identificador, "data_normalizada"] == data
        assert tabela.loc[identificador, "precisao_data"] == "dia"
    assert pd.isna(tabela.loc["D003", "data_normalizada"])
    assert tabela.loc["D003", "ano_documento"] == 1892
    assert tabela.loc["D003", "precisao_data"] == "ano"
    assert pd.isna(tabela.loc["D005", "data_normalizada"])
    assert pd.isna(tabela.loc["D005", "ano_documento"])
    assert tabela.loc["D005", "precisao_data"] == "desconhecida"
    assert tabela["precisao_data"].value_counts().to_dict() == {
        "dia": 6,
        "ano": 1,
        "desconhecida": 1,
    }
    assert int(tabela["possivel_duplicata"].sum()) == 2

    derivada = pd.read_csv(
        UNIDADE / "dados" / "derivados" / "documentos_processaveis.csv",
        dtype={"id_documento": "string", "ano_documento": "Int64"},
    ).set_index("id_documento")
    assert derivada.loc["D002", "data_normalizada"] == "1891-02-06"
    assert derivada.loc["D003", "precisao_data"] == "ano"


def validar_exercicios() -> None:
    texto = (UNIDADE / "exercicios_unidade_03_texto.md").read_text(encoding="utf-8")
    numeros = [int(n) for n in re.findall(r"^## Questão (\d+)", texto, re.MULTILINE)]
    assert numeros == list(range(1, 19))
    assert len(re.findall(r"^- \[ \] \*\*[A-D]\.\*\*", texto, re.MULTILINE)) == 72
    chave = (UNIDADE / "gabaritos" / "gabarito_exercicios_multipla_escolha.md").read_text(encoding="utf-8")
    respostas = re.findall(r"^\|\s*\d+\s*\|\s*([A-D])\s*\|", chave, re.MULTILINE)
    assert len(respostas) == 18


def validar_referencias_revisores() -> None:
    refs = (UNIDADE / "referencias.md").read_text(encoding="utf-8")
    for termo in ["RAWSON", "WICKHAM", "VAN HOOLAND", "HILL", "PANDAS", "TESSERACT", "PYPDF", "IBGE"]:
        assert termo in refs
    assert refs.count("https://") >= 9
    revisores = UNIDADE / "revisores"
    assert len(list(revisores.glob("*.md"))) == 9
    assert len(list((revisores / "pareceres").glob("*.md"))) == 7
    consolidado = (revisores / "pareceres" / "parecer_consolidado.md").read_text(encoding="utf-8")
    assert "Parecer consolidado" in consolidado
    rodadas = sorted((revisores / "pareceres").glob("rodada_*"))
    assert rodadas and len(list(rodadas[-1].glob("*.md"))) == 7


def validar_gabaritos() -> None:
    pasta = UNIDADE / "gabaritos"
    esperados = {
        "README.md",
        "gabarito_00_guia.md",
        "gabarito_01_formatos_ocr.md",
        "gabarito_02_limpeza.md",
        "gabarito_03_integracao.md",
        "gabarito_04_oficina.md",
        "gabarito_exercicios_multipla_escolha.md",
    }
    encontrados = {p.name for p in pasta.glob("*.md")}
    assert encontrados == esperados, f"gabaritos divergentes: {encontrados ^ esperados}"

    marcadores = {
        "gabarito_00_guia.md": [
            "## Exemplo de resposta preenchida",
            "Transformação prevista",
            "## Por que este exemplo é adequado?",
        ],
        "gabarito_01_formatos_ocr.md": [
            "## Exemplo de inventário resolvido",
            "## Exemplo de interpretação",
            "catalogo_messy.csv",
            "0,094",
        ],
        "gabarito_02_limpeza.md": [
            "## Exemplo de resultado das datas",
            "## Exemplo de resolução — log de transformação",
            "D003 parcial",
        ],
        "gabarito_03_integracao.md": [
            "## Exemplo de resolução — plano de integração",
            "### 4. Exemplo de rastreamento até a fonte",
            "## Por que este exemplo é adequado?",
        ],
        "gabarito_04_oficina.md": [
            "## Exemplo de resolução completa",
            "### 7. Autoavaliação preenchida",
            "### 8. Exemplo de revisão por pares",
        ],
        "gabarito_exercicios_multipla_escolha.md": [
            "Justificativa-modelo",
            "## Exemplo de resposta justificada",
            "alternativas A, C e D",
        ],
    }
    for nome, termos in marcadores.items():
        conteudo = (pasta / nome).read_text(encoding="utf-8")
        ausentes = [termo for termo in termos if termo not in conteudo]
        assert not ausentes, f"{nome}: exemplos incompletos: {ausentes}"

    exercicios = (pasta / "gabarito_exercicios_multipla_escolha.md").read_text(encoding="utf-8")
    justificativas = re.findall(
        r"^\|\s*\d+\s*\|\s*[A-D]\s*\|\s*(.+?)\s*\|$", exercicios, re.MULTILINE
    )
    assert len(justificativas) == 18
    assert all(len(texto.split()) >= 8 for texto in justificativas)


def main() -> None:
    notebooks = sorted(UNIDADE.glob("*.ipynb"))
    assert len(notebooks) == 5
    antes = hashes_brutos()
    total_md = total_code = 0
    for caminho in notebooks:
        n_md, n_code = executar(caminho)
        if caminho.name == "04_oficina_base_processavel.ipynb": assert n_code == 0
        total_md += n_md; total_code += n_code
        print(f"OK {caminho.name}: {n_md} Markdown, {n_code} código")
    assert antes == hashes_brutos(), "dados brutos foram alterados"
    validar_cobertura()
    validar_arquivos()
    validar_imagens()
    validar_resultados_semanticos()
    validar_exercicios()
    validar_gabaritos()
    validar_referencias_revisores()
    print("OK cobertura: 13/13 conteúdos")
    print("OK imagens: 8 recursos didáticos e 2 entradas de OCR, acessíveis e documentados")
    print("OK datas, OCR, dados brutos preservados, 3 derivados, exercícios, gabaritos e revisão")
    print(f"OK total: {total_md} células Markdown, {total_code} de código")


if __name__ == "__main__": main()
