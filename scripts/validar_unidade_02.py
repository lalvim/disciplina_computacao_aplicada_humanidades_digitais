"""Valida estrutura, cobertura e execução da Unidade 2."""

from __future__ import annotations

import json
import os
import re
import struct
import xml.etree.ElementTree as ET
from pathlib import Path


RAIZ = Path(__file__).resolve().parents[1]
UNIDADE = RAIZ / "unidade_02"


def fonte(celula: dict) -> str:
    valor = celula.get("source", "")
    return "".join(valor) if isinstance(valor, list) else valor


def executar_notebook(caminho: Path) -> tuple[int, int]:
    documento = json.loads(caminho.read_text(encoding="utf-8"))
    assert documento["nbformat"] == 4
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
                raise AssertionError(f"tipo inválido: {celula['cell_type']}")
    finally:
        os.chdir(anterior)
    return textos, codigos


def validar_cobertura() -> None:
    conteudo = ""
    for caminho in sorted(UNIDADE.glob("*.ipynb")):
        documento = json.loads(caminho.read_text(encoding="utf-8"))
        conteudo += "\n".join(fonte(c) for c in documento["cells"]).lower()
    termos = {
        "população e corpus": "população de interesse",
        "inclusão e exclusão": "critérios de inclusão",
        "representatividade": "representatividade",
        "fontes": "fonte primária",
        "dados institucionais": "governamentais, institucionais",
        "metadados": "metadados",
        "dicionário": "dicionário de dados",
        "identificadores": "identificador",
        "proveniência": "proveniência",
        "viés": "viés de seleção",
        "silêncios": "silêncios documentais",
        "FAIR": "findable / encontrável",
        "CARE": "authority to control / autoridade para controlar",
        "datasheets": "datasheets for datasets",
        "ética e legal": "ética e questões legais",
    }
    ausentes = [rotulo for rotulo, termo in termos.items() if termo not in conteudo]
    assert not ausentes, f"conteúdos ausentes: {', '.join(ausentes)}"


def validar_dados() -> None:
    esperados = {
        "catalogo_fontes.csv",
        "dicionario_dados.csv",
        "proveniencia_catalogo.json",
    }
    encontrados = {p.name for p in (UNIDADE / "dados").iterdir() if p.is_file()}
    assert encontrados == esperados
    assert "inteiramente fictícios" in (
        UNIDADE / "00_guia_da_unidade.ipynb"
    ).read_text(encoding="utf-8")


def validar_imagens() -> None:
    pasta = UNIDADE / "imagens"
    esperados = {
        "README.md",
        "00_abertura_conceitual.png",
        "00_percurso_unidade.svg",
        "01_populacao_acessivel_corpus.svg",
        "01_papel_das_fontes.svg",
        "02_cadeia_ausencias.svg",
        "02_cobertura_catalogo_corpus.svg",
        "03_documentacao_proveniencia.svg",
        "04_fair_care_datasheets.svg",
        "05_protocolo_integrado.svg",
    }
    encontrados = {p.name for p in pasta.iterdir() if p.is_file()}
    assert encontrados == esperados, f"imagens divergentes: {encontrados ^ esperados}"

    referencias = []
    for notebook in sorted(UNIDADE.glob("*.ipynb")):
        documento = json.loads(notebook.read_text(encoding="utf-8"))
        markdown = "\n".join(
            fonte(celula)
            for celula in documento["cells"]
            if celula["cell_type"] == "markdown"
        )
        referencias.extend(re.findall(r"!\[([^]]+)\]\((imagens/[^)]+)\)", markdown))

    assert len(referencias) == 9
    caminhos = [caminho for _, caminho in referencias]
    assert len(set(caminhos)) == 9
    for alt, caminho in referencias:
        assert len(alt.split()) >= 6, f"texto alternativo insuficiente: {caminho}"
        assert (UNIDADE / caminho).is_file(), f"imagem ausente: {caminho}"

    namespace = {"svg": "http://www.w3.org/2000/svg"}
    for caminho in sorted(pasta.glob("*.svg")):
        raiz = ET.parse(caminho).getroot()
        titulo = raiz.find("svg:title", namespace)
        descricao = raiz.find("svg:desc", namespace)
        assert titulo is not None and (titulo.text or "").strip()
        assert descricao is not None and len((descricao.text or "").split()) >= 8
        assert raiz.attrib.get("role") == "img"
        assert "aria-labelledby" in raiz.attrib

    png = (pasta / "00_abertura_conceitual.png").read_bytes()
    assert png[:8] == b"\x89PNG\r\n\x1a\n"
    largura, altura = struct.unpack(">II", png[16:24])
    assert largura >= 1200 and altura >= 500

    ficha = (pasta / "README.md").read_text(encoding="utf-8")
    for nome in esperados - {"README.md"}:
        assert nome in ficha, f"imagem sem documentação: {nome}"


def validar_exercicios() -> None:
    texto = (UNIDADE / "exercicios_unidade_02_texto.md").read_text(encoding="utf-8")
    numeros = [int(n) for n in re.findall(r"^## Questão (\d+)", texto, re.MULTILINE)]
    assert numeros == list(range(1, 22))
    assert len(re.findall(r"^- \[ \] \*\*[A-D]\.\*\*", texto, re.MULTILINE)) == 84

    chave = (
        UNIDADE / "gabaritos" / "gabarito_exercicios_multipla_escolha.md"
    ).read_text(encoding="utf-8")
    respostas = re.findall(r"^\|\s*\d+\s*\|\s*([A-D])\s*\|", chave, re.MULTILINE)
    assert len(respostas) == 21


def validar_gabaritos() -> None:
    pasta = UNIDADE / "gabaritos"
    marcadores = {
        "gabarito_01_selecao.md": [
            "## Exemplo de resposta — protocolo de seleção",
            "C004, de 1900, deve ser incluído",
            "### Por que esta resposta é defensável?",
        ],
        "gabarito_02_cobertura.md": [
            "## Exemplo de resposta — matriz de cobertura",
            "Silêncios que a ampliação da coleta talvez não resolva",
            "### Por que esta resposta é defensável?",
        ],
        "gabarito_03_documentacao.md": [
            "## Exemplo de resposta — documentação do projeto",
            "### Exemplo de registro de proveniência",
            "### Por que esta resposta é defensável?",
        ],
        "gabarito_04_governanca_documentacao.md": [
            "## Resultado esperado da auditoria",
            "## Exemplo de resposta — ficha de governança e documentação",
            "### Por que esta resposta é defensável?",
        ],
        "gabarito_05_protocolo.md": [
            "## Exemplo de resposta — protocolo integrado da base",
            "### 8. Autoavaliação — exemplo",
            "### 9. Revisão por pares — exemplo",
        ],
        "gabarito_exercicios_multipla_escolha.md": [
            "## Exemplo de resposta justificada",
        ],
    }
    for nome, termos in marcadores.items():
        conteudo = (pasta / nome).read_text(encoding="utf-8")
        ausentes = [termo for termo in termos if termo not in conteudo]
        assert not ausentes, f"{nome}: exemplos incompletos: {ausentes}"


def validar_referencias_e_revisao() -> None:
    referencias = (UNIDADE / "referencias.md").read_text(encoding="utf-8")
    for termo in ["AMERICAN HISTORICAL ASSOCIATION", "GEBRU", "RODRIGUES", "TROUILLOT", "SCHWARTZ", "CARROLL", "WILKINSON", "ANPD", "LGPD", "W3C"]:
        assert termo in referencias, f"referência ausente: {termo}"
    assert referencias.count("https://") >= 8

    revisores = UNIDADE / "revisores"
    assert len(list(revisores.glob("*.md"))) == 9
    assert len(list((revisores / "pareceres").glob("*.md"))) == 7
    consolidado = (revisores / "pareceres" / "parecer_consolidado.md").read_text(
        encoding="utf-8"
    )
    assert "94%" in consolidado and "Aprovada" in consolidado


def validar_encadeamento() -> None:
    """Garante que os notebooks explicitem as dependências entre suas etapas."""
    marcadores = {
        "00_guia_da_unidade.ipynb": [
            "A pergunta orientadora fornece o fio condutor",
            "o diagnóstico torna visíveis suas hipóteses atuais",
            "siga para o Notebook 01",
        ],
        "01_fontes_populacao_e_selecao.ipynb": [
            "Este notebook inicia sua construção pela decisão",
            "A filtragem produz um corpus, mas também produz exclusões",
            "Leve seu protocolo de seleção ao Notebook 02",
        ],
        "02_cobertura_vieses_e_silencios.ipynb": [
            "O Notebook 01 produziu critérios e um corpus",
            "A matriz ajuda a decidir o que ampliar",
            "Leve a matriz ao Notebook 03",
        ],
        "03_metadados_identificadores_e_proveniencia.ipynb": [
            "Os notebooks anteriores definiram o corpus",
            "Dicionário, identificadores, validações e proveniência",
            "Leve essa documentação ao Notebook 04",
        ],
        "04_governanca_reuso_e_documentacao_de_bases.ipynb": [
            "Partiremos da documentação construída no Notebook 03",
            "Agora as três lentes podem ser reunidas",
            "Leve a ficha revisada para o Notebook 05",
        ],
        "05_oficina_protocolo_da_base.ipynb": [
            "A oficina integra os produtos dos Notebooks 01 a 04",
            "Toda seleção altera presenças e ausências",
            "Incorpore o parecer antes da entrega",
        ],
    }
    for nome, termos in marcadores.items():
        documento = json.loads((UNIDADE / nome).read_text(encoding="utf-8"))
        conteudo = " ".join(
            re.sub(r"\s+", " ", fonte(celula)).strip()
            for celula in documento["cells"]
        )
        ausentes = [termo for termo in termos if termo not in conteudo]
        assert not ausentes, f"{nome}: encadeamento incompleto: {ausentes}"


def main() -> None:
    notebooks = sorted(UNIDADE.glob("*.ipynb"))
    assert len(notebooks) == 6
    total_textos = total_codigos = 0
    for caminho in notebooks:
        textos, codigos = executar_notebook(caminho)
        if caminho.name == "05_oficina_protocolo_da_base.ipynb":
            assert codigos == 0
        total_textos += textos
        total_codigos += codigos
        print(f"OK {caminho.name}: {textos} Markdown, {codigos} código")
    validar_cobertura()
    validar_dados()
    validar_imagens()
    validar_exercicios()
    validar_gabaritos()
    validar_referencias_e_revisao()
    validar_encadeamento()
    print("OK cobertura: 15/15 conteúdos")
    print("OK imagens: 9 recursos locais, acessíveis e documentados")
    print("OK dados, exercícios, gabaritos com exemplos, referências e revisores")
    print("OK encadeamento: pontes internas e produtos entre os 6 notebooks")
    print(f"OK total: {total_textos} células Markdown, {total_codigos} de código")


if __name__ == "__main__":
    main()
