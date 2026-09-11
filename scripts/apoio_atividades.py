"""Validação compartilhada dos identificadores de atividades e gabaritos."""

from __future__ import annotations

import json
import re
from collections import Counter
from pathlib import Path


PADRAO_ID = re.compile(r"U\d{2}-A\d{2}")


def _texto_notebook(caminho: Path) -> str:
    documento = json.loads(caminho.read_text(encoding="utf-8"))
    return "\n".join(
        "".join(celula.get("source", ""))
        if isinstance(celula.get("source", ""), list)
        else celula.get("source", "")
        for celula in documento["cells"]
        if celula["cell_type"] == "markdown"
    )


def validar_identificadores_atividades(unidade: Path, quantidade: int) -> None:
    """Garante sequência, unicidade no material e associação aos gabaritos."""
    prefixo = f"U{int(unidade.name.split('_')[-1]):02d}"
    esperados = {f"{prefixo}-A{numero:02d}" for numero in range(1, quantidade + 1)}

    materiais = "\n".join(_texto_notebook(p) for p in sorted(unidade.glob("*.ipynb")))
    exercicios = sorted(unidade.glob("exercicios_unidade_*_texto.md"))
    assert len(exercicios) == 1
    materiais += "\n" + exercicios[0].read_text(encoding="utf-8")
    contagem_material = Counter(PADRAO_ID.findall(materiais))
    assert set(contagem_material) == esperados, (
        f"{unidade.name}: IDs no material divergentes: "
        f"{set(contagem_material) ^ esperados}"
    )
    repetidos = [identificador for identificador, n in contagem_material.items() if n != 1]
    assert not repetidos, f"{unidade.name}: IDs repetidos no material: {repetidos}"

    pasta_gabaritos = unidade / "gabaritos"
    indice = (pasta_gabaritos / "README.md").read_text(encoding="utf-8")
    ids_indice = PADRAO_ID.findall(indice)
    assert set(ids_indice) == esperados and len(ids_indice) == quantidade, (
        f"{unidade.name}: índice de gabaritos incompleto ou duplicado"
    )

    conteudo_gabaritos = "\n".join(
        caminho.read_text(encoding="utf-8")
        for caminho in sorted(pasta_gabaritos.glob("gabarito_*.md"))
    )
    contagem_gabaritos = Counter(PADRAO_ID.findall(conteudo_gabaritos))
    assert set(contagem_gabaritos) == esperados, (
        f"{unidade.name}: associações nos gabaritos divergentes: "
        f"{set(contagem_gabaritos) ^ esperados}"
    )
    repetidos = [identificador for identificador, n in contagem_gabaritos.items() if n != 1]
    assert not repetidos, f"{unidade.name}: ID associado a mais de um gabarito: {repetidos}"
