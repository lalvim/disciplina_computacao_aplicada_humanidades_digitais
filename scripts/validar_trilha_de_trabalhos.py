"""Valida os cadernos de entrega cumulativa do projeto integrador."""

from __future__ import annotations

import json
from pathlib import Path


RAIZ = Path(__file__).resolve().parents[1]
PASTA = RAIZ / "notes" / "trilha_de_trabalhos" / "notebooks_de_entrega"


def fonte(celula: dict) -> str:
    valor = celula.get("source", "")
    return "".join(valor) if isinstance(valor, list) else valor


def validar_exemplo(
    caminho: Path,
    identificador: str,
    minimo_codigos: int,
    minimo_imagens: int,
    marcadores: list[str],
) -> None:
    assert caminho.exists(), f"notebook não encontrado: {caminho.name}"
    documento = json.loads(caminho.read_text(encoding="utf-8"))
    texto = "\n".join(fonte(c) for c in documento["cells"])
    celulas_codigo = [c for c in documento["cells"] if c["cell_type"] == "code"]

    assert "# EXEMPLO PREENCHIDO" in texto
    assert identificador in texto
    for marcador in marcadores:
        assert marcador in texto, f"{caminho.name}: ausente {marcador}"
    assert len(celulas_codigo) >= minimo_codigos, (
        f"{caminho.name}: faltam demonstrações executáveis"
    )
    assert all(c.get("execution_count") is not None for c in celulas_codigo), (
        f"{caminho.name}: há células de código que ainda não foram executadas"
    )
    assert not any(
        saida.get("output_type") == "error"
        for c in celulas_codigo
        for saida in c.get("outputs", [])
    ), f"{caminho.name}: há saída de erro"
    imagens = [
        saida
        for c in celulas_codigo
        for saida in c.get("outputs", [])
        if "image/png" in saida.get("data", {})
    ]
    assert len(imagens) >= minimo_imagens, (
        f"{caminho.name}: gráficos não incorporados ao notebook"
    )
    for unidade in range(1, 15):
        assert f"## U{unidade:02d} —" in texto, (
            f"{caminho.name}: unidade U{unidade:02d} ausente"
        )
    print(
        f"OK {caminho.name}: {len(celulas_codigo)} células executadas, "
        f"{len(imagens)} imagens e percurso U01–U14"
    )


def main() -> None:
    notebooks = sorted(PASTA.glob("PI_U*.ipynb"))
    assert not notebooks, (
        "a pasta deve conter somente exemplos preenchidos; "
        f"encontrados {len(notebooks)} modelos de entrega"
    )

    exemplos = [
        (
            PASTA / "EXEMPLO_PREENCHIDO_projeto_integrador_U01_a_U14.ipynb",
            "PI-EXEMPLO-IMPRENSA",
            7,
            3,
            ["não representa uma pesquisa histórica real", "Análise do gráfico"],
        ),
        (
            PASTA / "EXEMPLO_PREENCHIDO_IBGE_DADOS_FICTICIOS_U01_a_U14.ipynb",
            "PI-EXEMPLO-IBGE-SINTETICO",
            8,
            4,
            ["Dados inteiramente fictícios", "não foi produzido pelo IBGE"],
        ),
    ]
    for caminho, identificador, codigos, imagens, marcadores in exemplos:
        validar_exemplo(caminho, identificador, codigos, imagens, marcadores)

    readme = (PASTA / "README.md").read_text(encoding="utf-8")
    for caminho, *_ in exemplos:
        assert caminho.name in readme, f"{caminho.name} ausente do índice"
    print("OK trilha: dois exemplos preenchidos e nenhum modelo vazio")


if __name__ == "__main__":
    main()
