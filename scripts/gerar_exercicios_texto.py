"""Gera uma alternativa textual, sem respostas, para o exercício HTML."""

from __future__ import annotations

import re
from pathlib import Path


RAIZ = Path(__file__).resolve().parents[1]
HTML = RAIZ / "unidade_01" / "exercicios_unidade_01.html"
SAIDA = RAIZ / "unidade_01" / "exercicios_unidade_01_texto.md"


def extrair_questoes(conteudo: str) -> list[tuple[str, str, list[str]]]:
    padrao = re.compile(
        r"""\{\s*
        topico:\s*"([^"]+)",\s*
        enunciado:\s*"([^"]+)",\s*
        alternativas:\s*\[(.*?)\],\s*
        correta:\s*\d+,\s*
        explicacao:\s*"[^"]+"\s*
        \}""",
        re.DOTALL | re.VERBOSE,
    )
    questoes = []
    for topico, enunciado, bloco_alternativas in padrao.findall(conteudo):
        alternativas = re.findall(r'"([^"]+)"', bloco_alternativas)
        questoes.append((topico, enunciado, alternativas))
    return questoes


def main() -> None:
    questoes = extrair_questoes(HTML.read_text(encoding="utf-8"))
    if len(questoes) != 18:
        raise ValueError(f"Esperadas 18 questões; encontradas {len(questoes)}")

    linhas = [
        "# Exercícios da Unidade 1 — versão textual",
        "",
        "Esta versão contém as mesmas questões do exercício HTML, sem a correção",
        "interativa. Marque uma alternativa por questão e consulte o gabarito",
        "somente após concluir.",
        "",
    ]
    letras = "ABCD"
    for numero, (topico, enunciado, alternativas) in enumerate(questoes, start=1):
        linhas.extend(
            [
                f"## Questão {numero} — {topico}",
                "",
                enunciado,
                "",
            ]
        )
        for letra, alternativa in zip(letras, alternativas):
            linhas.append(f"- [ ] **{letra}.** {alternativa}")
        linhas.append("")

    SAIDA.write_text("\n".join(linhas), encoding="utf-8")
    print(f"Versão textual criada em: {SAIDA}")


if __name__ == "__main__":
    main()
