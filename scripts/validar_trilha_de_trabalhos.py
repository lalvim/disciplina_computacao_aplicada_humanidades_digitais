"""Valida os cadernos de entrega cumulativa do projeto integrador."""

from __future__ import annotations

import json
from pathlib import Path


RAIZ = Path(__file__).resolve().parents[1]
PASTA = RAIZ / "notes" / "trilha_de_trabalhos" / "notebooks_de_entrega"


def fonte(celula: dict) -> str:
    valor = celula.get("source", "")
    return "".join(valor) if isinstance(valor, list) else valor


def main() -> None:
    notebooks = sorted(PASTA.glob("PI_U*.ipynb"))
    assert not notebooks, (
        "a pasta deve conter somente o exemplo preenchido; "
        f"encontrados {len(notebooks)} modelos de entrega"
    )

    caminho_exemplo = PASTA / "EXEMPLO_PREENCHIDO_projeto_integrador_U01_a_U14.ipynb"
    assert caminho_exemplo.exists(), "notebook com o exemplo completo não encontrado"
    documento_exemplo = json.loads(caminho_exemplo.read_text(encoding="utf-8"))
    texto_exemplo = "\n".join(fonte(c) for c in documento_exemplo["cells"])
    celulas_codigo = [
        c for c in documento_exemplo["cells"] if c["cell_type"] == "code"
    ]
    assert "# EXEMPLO PREENCHIDO" in texto_exemplo
    assert "PI-EXEMPLO-IMPRENSA" in texto_exemplo
    assert "não representa uma pesquisa histórica real" in texto_exemplo
    assert len(celulas_codigo) >= 7, "faltam demonstrações executáveis no exemplo"
    assert all(c.get("execution_count") is not None for c in celulas_codigo), (
        "há células de código que ainda não foram executadas"
    )
    assert not any(
        saida.get("output_type") == "error"
        for c in celulas_codigo
        for saida in c.get("outputs", [])
    ), "o notebook contém saída de erro"
    imagens = [
        saida
        for c in celulas_codigo
        for saida in c.get("outputs", [])
        if "image/png" in saida.get("data", {})
    ]
    assert len(imagens) >= 3, "os três gráficos não estão incorporados ao notebook"
    assert "Análise dos resultados" in texto_exemplo
    assert "Análise do gráfico" in texto_exemplo
    assert "plt.show()" in texto_exemplo
    for unidade in range(1, 15):
        assert f"## U{unidade:02d} —" in texto_exemplo, (
            f"unidade U{unidade:02d} ausente do exemplo completo"
        )

    readme = (PASTA / "README.md").read_text(encoding="utf-8")
    assert caminho_exemplo.name in readme, "exemplo completo ausente do índice"
    print(
        f"OK {caminho_exemplo.name}: percurso fictício completo de U01 a U14"
    )
    print("OK trilha: somente o exemplo preenchido, com percurso de U01 a U14")


if __name__ == "__main__":
    main()
