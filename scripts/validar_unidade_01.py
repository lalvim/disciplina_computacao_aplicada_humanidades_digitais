"""Valida a estrutura e executa as células de código da Unidade 1."""

from __future__ import annotations

import json
import os
from pathlib import Path


RAIZ = Path(__file__).resolve().parents[1]
UNIDADE = RAIZ / "unidade_01"


def fonte_da_celula(celula: dict) -> str:
    fonte = celula.get("source", "")
    return "".join(fonte) if isinstance(fonte, list) else fonte


def validar_notebook(caminho: Path) -> tuple[int, int]:
    with caminho.open(encoding="utf-8") as arquivo:
        documento = json.load(arquivo)

    assert documento["nbformat"] == 4
    assert isinstance(documento["cells"], list)
    assert documento["cells"], "notebook sem células"

    ambiente = {"__name__": "__main__"}
    codigos = 0
    textos = 0
    diretorio_anterior = Path.cwd()
    try:
        os.chdir(UNIDADE)
        for numero, celula in enumerate(documento["cells"], start=1):
            tipo = celula.get("cell_type")
            fonte = fonte_da_celula(celula)
            assert fonte.strip(), f"célula {numero} vazia"
            if tipo == "markdown":
                textos += 1
            elif tipo == "code":
                codigos += 1
                assert "Escreva aqui" not in fonte and "Edite aqui" not in fonte, (
                    f"célula {numero} usa Python como formulário"
                )
                exec(
                    compile(fonte, f"{caminho.name}:célula-{numero}", "exec"),
                    ambiente,
                )
            else:
                raise AssertionError(f"tipo desconhecido na célula {numero}: {tipo}")
    finally:
        os.chdir(diretorio_anterior)

    return textos, codigos


def validar_cobertura() -> None:
    termos = {
        "Humanidades Digitais": "humanidades digitais",
        "tipos de pergunta": "descritiva",
        "operacionalização": "operacionaliza",
        "unidade de análise": "unidade de análise",
        "população, amostra e corpus": "população",
        "variáveis e metadados": "metadados",
        "tipos de dados": "semiestruturados",
        "evidência computacional": "evidência computacional",
        "limites da automação": "limites da quantificação e da automação",
    }
    conteudo = ""
    for caminho in sorted(UNIDADE.glob("*.ipynb")):
        documento = json.loads(caminho.read_text(encoding="utf-8"))
        conteudo += "\n".join(fonte_da_celula(c) for c in documento["cells"]).lower()

    ausentes = [rotulo for rotulo, termo in termos.items() if termo not in conteudo]
    assert not ausentes, f"tópicos ausentes: {', '.join(ausentes)}"


def main() -> None:
    notebooks = sorted(UNIDADE.glob("*.ipynb"))
    assert len(notebooks) == 5, f"esperados 5 notebooks; encontrados {len(notebooks)}"

    total_textos = 0
    total_codigos = 0
    for caminho in notebooks:
        textos, codigos = validar_notebook(caminho)
        if caminho.name == "04_oficina_projeto_de_pesquisa.ipynb":
            assert codigos == 0, "a oficina deve ser integralmente discursiva"
        total_textos += textos
        total_codigos += codigos
        print(f"OK {caminho.name}: {textos} células de texto, {codigos} de código")

    validar_cobertura()
    print(f"OK cobertura: 9/9 tópicos da ementa")
    print(
        f"OK total: {len(notebooks)} notebooks, "
        f"{total_textos} células de texto, {total_codigos} de código"
    )


if __name__ == "__main__":
    main()
