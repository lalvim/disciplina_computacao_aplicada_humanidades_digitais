"""Valida estrutura, cobertura e execução da Unidade 2."""

from __future__ import annotations

import json
import os
import re
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


def validar_exercicios() -> None:
    html = (UNIDADE / "exercicios_unidade_02.html").read_text(encoding="utf-8")
    assert "<!doctype html>" in html.lower()
    assert "<noscript>" in html
    assert not re.search(r'(?:src|href)="https?://', html)
    assert len(re.findall(r'"enunciado":', html)) == 18
    assert len(re.findall(r'"correta":', html)) == 18
    texto = (UNIDADE / "exercicios_unidade_02_texto.md").read_text(encoding="utf-8")
    assert len(re.findall(r"^## Questão \d+", texto, re.MULTILINE)) == 18

    chave = (
        UNIDADE / "gabaritos" / "gabarito_exercicios_multipla_escolha.md"
    ).read_text(encoding="utf-8")
    respostas = re.findall(r"^\|\s*\d+\s*\|\s*([A-D])\s*\|", chave, re.MULTILINE)
    corretas = [
        chr(65 + int(i)) for i in re.findall(r'"correta":\s*(\d+)', html)
    ]
    assert len(respostas) == 18 and respostas == corretas


def validar_referencias_e_revisao() -> None:
    referencias = (UNIDADE / "referencias.md").read_text(encoding="utf-8")
    for termo in ["GEBRU", "RODRIGUES", "TROUILLOT", "SCHWARTZ", "CARROLL", "ANPD", "LGPD", "W3C"]:
        assert termo in referencias, f"referência ausente: {termo}"
    assert referencias.count("https://") >= 8

    revisores = UNIDADE / "revisores"
    assert len(list(revisores.glob("*.md"))) == 9
    assert len(list((revisores / "pareceres").glob("*.md"))) == 7
    consolidado = (revisores / "pareceres" / "parecer_consolidado.md").read_text(
        encoding="utf-8"
    )
    assert "94%" in consolidado and "Aprovada" in consolidado


def main() -> None:
    notebooks = sorted(UNIDADE.glob("*.ipynb"))
    assert len(notebooks) == 5
    total_textos = total_codigos = 0
    for caminho in notebooks:
        textos, codigos = executar_notebook(caminho)
        if caminho.name == "04_oficina_protocolo_da_base.ipynb":
            assert codigos == 0
        total_textos += textos
        total_codigos += codigos
        print(f"OK {caminho.name}: {textos} Markdown, {codigos} código")
    validar_cobertura()
    validar_dados()
    validar_exercicios()
    validar_referencias_e_revisao()
    print("OK cobertura: 12/12 conteúdos")
    print("OK dados, exercícios, gabaritos, referências e revisores")
    print(f"OK total: {total_textos} células Markdown, {total_codigos} de código")


if __name__ == "__main__":
    main()
