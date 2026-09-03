"""Valida links e células de preparação para uso das Unidades 1–4 no Colab."""

from __future__ import annotations

import json
from pathlib import Path

from apoio_colab import COLAB_GITHUB


RAIZ = Path(__file__).resolve().parents[1]
DEPENDENTES_DO_REPOSITORIO = {
    "unidade_01": {"03_dados_corpus_e_evidencias.ipynb"},
    "unidade_02": {
        "00_guia_da_unidade.ipynb",
        "01_fontes_populacao_e_selecao.ipynb",
        "02_cobertura_vieses_e_silencios.ipynb",
        "03_metadados_identificadores_e_proveniencia.ipynb",
    },
    "unidade_03": {
        "00_guia_da_unidade.ipynb",
        "01_formatos_importacao_e_extracao.ipynb",
        "02_estrutura_limpeza_e_qualidade.ipynb",
        "03_juncoes_integracao_e_reprodutibilidade.ipynb",
    },
    "unidade_04": {
        "00_guia_da_unidade.ipynb",
        "01_exploracao_quantitativa.ipynb",
        "02_exploracao_textual.ipynb",
        "03_visualizacao_exploratoria.ipynb",
    },
}


def fonte(celula: dict) -> str:
    valor = celula.get("source", "")
    return "".join(valor) if isinstance(valor, list) else valor


def main() -> None:
    readme_raiz = (RAIZ / "README.md").read_text(encoding="utf-8")
    total = preparacoes = 0

    for unidade, dependentes in DEPENDENTES_DO_REPOSITORIO.items():
        pasta = RAIZ / unidade
        notebooks = sorted(pasta.glob("*.ipynb"))
        assert len(notebooks) == 5, f"{unidade}: esperados cinco notebooks"
        readme_unidade = (pasta / "README.md").read_text(encoding="utf-8")

        for caminho in notebooks:
            total += 1
            url = f"{COLAB_GITHUB}/{unidade}/{caminho.name}"
            documento = json.loads(caminho.read_text(encoding="utf-8"))
            fontes = [fonte(celula) for celula in documento["cells"]]

            assert sum(url in conteudo for conteudo in fontes) == 1, (
                f"{caminho}: link do Colab ausente ou duplicado"
            )
            assert url in readme_unidade, f"{caminho}: link ausente no README local"
            assert url in readme_raiz, f"{caminho}: link ausente no README principal"

            celulas_preparacao = [
                conteudo
                for conteudo in fontes
                if "# @title Preparação do ambiente" in conteudo
            ]
            esperado = caminho.name in dependentes
            assert len(celulas_preparacao) == int(esperado), (
                f"{caminho}: preparação incompatível com a dependência de arquivos"
            )
            if celulas_preparacao:
                preparacoes += 1
                codigo = celulas_preparacao[0]
                assert "git clone" not in codigo and "!git" not in codigo
                assert "subprocess.run" in codigo
                assert f"PASTA_UNIDADE = REPOSITORIO / {unidade!r}" in codigo
                compile(codigo, str(caminho), "exec")

    assert total == 20
    assert preparacoes == 13
    print(f"OK Colab: {total} links e {preparacoes} preparações seletivas")


if __name__ == "__main__":
    main()
