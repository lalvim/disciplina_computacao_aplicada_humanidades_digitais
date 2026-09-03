"""Elementos comuns para publicar os notebooks no Google Colab."""

from __future__ import annotations

from textwrap import dedent


REPOSITORIO_GITHUB = (
    "https://github.com/lalvim/"
    "disciplina_computacao_aplicada_humanidades_digitais.git"
)
COLAB_GITHUB = (
    "https://colab.research.google.com/github/lalvim/"
    "disciplina_computacao_aplicada_humanidades_digitais/blob/main"
)


def link_colab(unidade: str, notebook: str) -> str:
    """Retorna um link textual que funciona no GitHub e no Jupyter."""

    return (
        f"[▶ Abrir este notebook no Google Colab]"
        f"({COLAB_GITHUB}/{unidade}/{notebook})"
    )


def adicionar_link_na_abertura(
    celula: dict,
    unidade: str,
    notebook: str,
) -> dict:
    """Insere o link logo abaixo do título, preservando a célula original."""

    fonte_original = celula.get("source", [])
    linhas = (
        list(fonte_original)
        if isinstance(fonte_original, list)
        else fonte_original.splitlines(keepends=True)
    )
    assert linhas and linhas[0].lstrip().startswith("# ")
    nova = dict(celula)
    nova["source"] = [
        linhas[0],
        "\n",
        f"{link_colab(unidade, notebook)}\n",
        *linhas[1:],
    ]
    return nova


def tabela_links_colab(
    unidade: str,
    notebooks: tuple[tuple[str, str], ...],
) -> str:
    """Monta a tabela de navegação local e abertura direta no Colab."""

    linhas = [
        "| Material | Arquivo | Google Colab |",
        "|---|---|---|",
    ]
    for titulo, nome in notebooks:
        linhas.append(
            f"| {titulo} | [`{nome}`]({nome}) | "
            f"[Abrir no Colab]({COLAB_GITHUB}/{unidade}/{nome}) |"
        )
    return "\n".join(linhas)


def preparacao_colab(
    unidade: str,
    pacotes: tuple[tuple[str, str], ...] = (),
) -> str:
    """Gera a célula executável que prepara arquivos e dependências no Colab.

    Cada item de ``pacotes`` contém o módulo a procurar e a especificação que o
    pip deve instalar caso o módulo não esteja disponível.
    """

    verificacoes = repr(list(pacotes))
    return dedent(
        f'''
        # @title Preparação do ambiente — execute esta célula no Google Colab
        from pathlib import Path
        import importlib.util
        import os
        import subprocess
        import sys

        URL_REPOSITORIO = {REPOSITORIO_GITHUB!r}
        REPOSITORIO = Path(
            "/content/disciplina_computacao_aplicada_humanidades_digitais"
        )
        PASTA_UNIDADE = REPOSITORIO / {unidade!r}

        try:
            import google.colab  # type: ignore  # noqa: F401
            EM_COLAB = True
        except ImportError:
            EM_COLAB = False

        if EM_COLAB:
            if not (REPOSITORIO / ".git").exists():
                subprocess.run(
                    [
                        "git",
                        "clone",
                        "--depth",
                        "1",
                        "--branch",
                        "main",
                        URL_REPOSITORIO,
                        str(REPOSITORIO),
                    ],
                    check=True,
                )

            PACOTES_COLAB = {verificacoes}
            ausentes = [
                especificacao
                for modulo, especificacao in PACOTES_COLAB
                if importlib.util.find_spec(modulo) is None
            ]
            if ausentes:
                subprocess.run(
                    [sys.executable, "-m", "pip", "install", "-q", *ausentes],
                    check=True,
                )

            os.chdir(PASTA_UNIDADE)
            print("Ambiente preparado em:", Path.cwd())
        else:
            print("Ambiente local: nenhuma clonagem necessária.")
        '''
    ).strip()
