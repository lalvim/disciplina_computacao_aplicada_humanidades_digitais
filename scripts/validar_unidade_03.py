"""Valida estrutura, execução e integridade da Unidade 3."""

from __future__ import annotations

import hashlib
import json
import os
import re
from pathlib import Path

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


def validar_exercicios() -> None:
    html = (UNIDADE / "exercicios_unidade_03.html").read_text(encoding="utf-8")
    assert "<!doctype html>" in html.lower() and "<noscript>" in html
    assert not re.search(r'(?:src|href)="https?://', html)
    assert len(re.findall(r'"enunciado":', html)) == 18
    texto = (UNIDADE / "exercicios_unidade_03_texto.md").read_text(encoding="utf-8")
    assert len(re.findall(r"^## Questão \d+", texto, re.MULTILINE)) == 18
    chave = (UNIDADE / "gabaritos" / "gabarito_exercicios_multipla_escolha.md").read_text(encoding="utf-8")
    respostas = re.findall(r"^\|\s*\d+\s*\|\s*([A-D])\s*\|", chave, re.MULTILINE)
    corretas = [chr(65 + int(i)) for i in re.findall(r'"correta":\s*(\d+)', html)]
    assert respostas == corretas and len(respostas) == 18


def validar_referencias_revisores() -> None:
    refs = (UNIDADE / "referencias.md").read_text(encoding="utf-8")
    for termo in ["RAWSON", "WICKHAM", "VAN HOOLAND", "HILL", "PANDAS", "TESSERACT", "PYPDF", "IBGE"]:
        assert termo in refs
    assert refs.count("https://") >= 9
    revisores = UNIDADE / "revisores"
    assert len(list(revisores.glob("*.md"))) == 9
    assert len(list((revisores / "pareceres").glob("*.md"))) == 7
    consolidado = (revisores / "pareceres" / "parecer_consolidado.md").read_text(encoding="utf-8")
    assert "92%" in consolidado and "Aprovada" in consolidado


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
    validar_cobertura(); validar_arquivos(); validar_exercicios(); validar_referencias_revisores()
    print("OK cobertura: 13/13 conteúdos")
    print("OK dados brutos preservados, 3 derivados, exercícios, gabaritos e revisão")
    print(f"OK total: {total_md} células Markdown, {total_code} de código")


if __name__ == "__main__": main()
