"""Valida a estrutura e executa as células de código da Unidade 1."""

from __future__ import annotations

import json
import os
import re
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
        "finalidade e estrutura da pergunta": "estrutura analítica",
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


def validar_exercicios_html() -> None:
    caminho = UNIDADE / "exercicios_unidade_01.html"
    conteudo = caminho.read_text(encoding="utf-8")
    assert "<!doctype html>" in conteudo.lower()
    assert not re.search(r'(?:src|href)="https?://', conteudo), (
        "o exercício deve funcionar sem recursos externos"
    )
    assert len(re.findall(r"^\s+enunciado:", conteudo, flags=re.MULTILINE)) == 18
    assert len(re.findall(r"^\s+correta:", conteudo, flags=re.MULTILINE)) == 18
    assert "<noscript>" in conteudo
    assert "exercicios_unidade_01_texto.md" in conteudo

    topicos = [
        "Humanidades Digitais",
        "Finalidade e estrutura da pergunta",
        "Operacionalização",
        "Unidade de análise",
        "População, amostra e corpus",
        "Variáveis, categorias e metadados",
        "Formatos de dados",
        "Evidência e interpretação",
        "Limites da quantificação",
        "Limites da automação",
    ]
    ausentes = [topico for topico in topicos if f'topico: "{topico}"' not in conteudo]
    assert not ausentes, f"tópicos ausentes no HTML: {', '.join(ausentes)}"

    versao_textual = (UNIDADE / "exercicios_unidade_01_texto.md").read_text(
        encoding="utf-8"
    )
    assert len(re.findall(r"^## Questão \d+", versao_textual, re.MULTILINE)) == 18


def validar_referencias() -> None:
    referencias = (UNIDADE / "referencias.md").read_text(encoding="utf-8")
    autores = [
        "ALVES, Daniel",
        "DRUCKER, Johanna",
        "LAVIN, Matthew",
        "D'IGNAZIO, Catherine",
        "RODRIGUES, Aldair",
        "FERLA, Luis Antonio",
        "SHMUELI, Galit",
        "DREW, Clifford",
    ]
    ausentes = [autor for autor in autores if autor not in referencias]
    assert not ausentes, f"autores ausentes: {', '.join(ausentes)}"
    assert referencias.count("https://") >= 8
    titulo_alves = (
        "As Humanidades Digitais como uma comunidade de práticas dentro "
        "do formalismo académico: dos exemplos internacionais ao caso português"
    )
    assert titulo_alves in " ".join(referencias.split())
    titulo_rodrigues = (
        "Humanidades digitais e diáspora africana: questões éticas e "
        "metodológicas na elaboração de uma base de dados sobre a população "
        "escravizada de Mariana (século XVIII)"
    )
    assert titulo_rodrigues in " ".join(referencias.split())

    for nome in [
        "01_perguntas_e_problemas_computacionais.ipynb",
        "02_representacao_e_operacionalizacao.ipynb",
        "03_dados_corpus_e_evidencias.ipynb",
    ]:
        conteudo = (UNIDADE / nome).read_text(encoding="utf-8")
        assert "Referências e leituras" in conteudo, f"{nome} sem leituras"

    oficina = (UNIDADE / "04_oficina_projeto_de_pesquisa.ipynb").read_text(
        encoding="utf-8"
    )
    assert "Conceito central e autores de referência" in oficina
    assert "Referências utilizadas" in oficina

    guia = json.loads(
        (UNIDADE / "00_guia_da_unidade.ipynb").read_text(encoding="utf-8")
    )
    conteudo_guia = "\n".join(
        fonte_da_celula(celula) for celula in guia["cells"]
    )
    assert "Atividade em dupla — compreender o interesse do colega" in conteudo_guia
    assert conteudo_guia.index("## Atividade individual — diagnóstico inicial") < conteudo_guia.index(
        "## Atividade em dupla"
    ) < conteudo_guia.index("## Produto e avaliação")

    dinamicas_esperadas = {
        "00_guia_da_unidade.ipynb": [
            "Modalidade:** individual",
            "Atividade em dupla — compreender o interesse do colega",
        ],
        "01_perguntas_e_problemas_computacionais.ipynb": [
            "Experimento guiado — organizar e consultar perguntas",
            "Modalidade:** trios",
            "Atividade em trio e plenária — casos limítrofes",
            "Atividade autônoma — produto parcial",
        ],
        "02_representacao_e_operacionalizacao.ipynb": [
            "produção individual seguida de comparação em dupla",
        ],
        "03_dados_corpus_e_evidencias.ipynb": [
            "produção individual seguida de revisão em dupla",
        ],
        "04_oficina_projeto_de_pesquisa.ipynb": [
            "Modalidade:** elaboração individual",
            "Atividade — revisão entre pares",
            "dois turnos",
            "Parecer recebido",
            "Mudanças realizadas e justificativa",
        ],
    }
    for nome, marcadores in dinamicas_esperadas.items():
        documento = json.loads((UNIDADE / nome).read_text(encoding="utf-8"))
        conteudo = "\n".join(
            fonte_da_celula(celula) for celula in documento["cells"]
        )
        ausentes = [marcador for marcador in marcadores if marcador not in conteudo]
        assert not ausentes, f"{nome} sem dinâmica: {', '.join(ausentes)}"

    caminho_notebook_01 = UNIDADE / "01_perguntas_e_problemas_computacionais.ipynb"
    documento_notebook_01 = json.loads(caminho_notebook_01.read_text(encoding="utf-8"))
    notebook_01 = "\n".join(
        fonte_da_celula(celula) for celula in documento_notebook_01["cells"]
    )
    assert '"finalidade"' in notebook_01 and '"estrutura"' in notebook_01
    assert "Shmueli (2010)" in notebook_01
    assert titulo_alves in " ".join(notebook_01.split())

    for nome in [
        "00_guia_da_unidade.ipynb",
        "03_dados_corpus_e_evidencias.ipynb",
    ]:
        documento = json.loads((UNIDADE / nome).read_text(encoding="utf-8"))
        conteudo = " ".join(
            fonte_da_celula(celula) for celula in documento["cells"]
        )
        assert titulo_rodrigues in " ".join(conteudo.split())

    materiais_ativos = [
        RAIZ / "notes" / "contexto_disciplina.md",
        RAIZ / "notes" / "plano_unidade_01.md",
        UNIDADE / "00_guia_da_unidade.ipynb",
        UNIDADE / "01_perguntas_e_problemas_computacionais.ipynb",
        UNIDADE / "04_oficina_projeto_de_pesquisa.ipynb",
        UNIDADE / "exercicios_unidade_01.html",
        *sorted((UNIDADE / "gabaritos").glob("*.md")),
    ]
    formulacao_antiga = "cinco tipos de pergunta"
    ocorrencias = [
        str(caminho.relative_to(RAIZ))
        for caminho in materiais_ativos
        if formulacao_antiga in caminho.read_text(encoding="utf-8").lower()
    ]
    assert not ocorrencias, (
        "formulação antiga encontrada em materiais ativos: "
        + ", ".join(ocorrencias)
    )

    assert "Finalidade predominante e justificativa" in oficina
    assert "Estrutura analítica inicial" in oficina


def validar_gabaritos() -> None:
    pasta = UNIDADE / "gabaritos"
    esperados = {
        "README.md",
        "gabarito_01_perguntas.md",
        "gabarito_02_operacionalizacao.md",
        "gabarito_03_corpus.md",
        "gabarito_04_oficina.md",
        "gabarito_exercicios_multipla_escolha.md",
    }
    encontrados = {caminho.name for caminho in pasta.glob("*.md")}
    assert encontrados == esperados, (
        f"gabaritos divergentes: esperados {sorted(esperados)}, "
        f"encontrados {sorted(encontrados)}"
    )

    chave = (pasta / "gabarito_exercicios_multipla_escolha.md").read_text(
        encoding="utf-8"
    )
    respostas_chave = re.findall(
        r"^\|\s*\d+\s*\|\s*([A-D])\s*\|", chave, re.MULTILINE
    )
    assert len(respostas_chave) == 18, "a chave deve conter 18 respostas"

    html = (UNIDADE / "exercicios_unidade_01.html").read_text(encoding="utf-8")
    respostas_html = [
        chr(65 + int(indice))
        for indice in re.findall(r"^\s+correta:\s*(\d+),?$", html, re.MULTILINE)
    ]
    assert respostas_chave == respostas_html, (
        "a chave do gabarito não corresponde às respostas do exercício HTML"
    )

    oficina = (pasta / "gabarito_04_oficina.md").read_text(encoding="utf-8")
    criterios = [
        "Relevância humanística",
        "Delimitação",
        "Unidade de análise",
        "Dados e corpus",
        "Operacionalização",
        "Cadeia de evidência",
        "Limites e ética",
    ]
    ausentes = [criterio for criterio in criterios if criterio not in oficina]
    assert not ausentes, f"critérios ausentes da rubrica: {', '.join(ausentes)}"


def validar_revisores() -> None:
    pasta = UNIDADE / "revisores"
    esperados = {
        "README.md",
        "00_coordenacao_da_revisao.md",
        "01_revisor_nivel_academico.md",
        "02_revisor_didatica.md",
        "03_revisor_alinhamento.md",
        "04_revisor_humanidades_digitais.md",
        "05_revisor_referencias.md",
        "06_revisor_tecnico_acessibilidade.md",
        "matriz_de_avaliacao.md",
        "modelo_de_parecer.md",
    }
    encontrados = {caminho.name for caminho in pasta.glob("*.md")}
    assert encontrados == esperados, (
        f"revisores divergentes: esperados {sorted(esperados)}, "
        f"encontrados {sorted(encontrados)}"
    )

    conteudo = "\n".join(
        caminho.read_text(encoding="utf-8") for caminho in sorted(pasta.glob("*.md"))
    )
    criterios = [
        "nível de mestrado",
        "progressão didática",
        "alinhamento",
        "Humanidades Digitais",
        "referências acadêmicas",
        "acessibilidade",
        "Bloqueante",
        "Evidência",
    ]
    ausentes = [criterio for criterio in criterios if criterio not in conteudo]
    assert not ausentes, f"critérios ausentes dos revisores: {', '.join(ausentes)}"

    pasta_pareceres = pasta / "pareceres"
    pareceres_esperados = {
        "README.md",
        "01_parecer_nivel_academico.md",
        "02_parecer_didatica.md",
        "03_parecer_alinhamento.md",
        "04_parecer_humanidades_digitais.md",
        "05_parecer_referencias.md",
        "06_parecer_tecnico_acessibilidade.md",
        "parecer_consolidado.md",
    }
    pareceres_encontrados = {
        caminho.name for caminho in pasta_pareceres.glob("*.md")
    }
    assert pareceres_encontrados == pareceres_esperados, (
        f"pareceres divergentes: esperados {sorted(pareceres_esperados)}, "
        f"encontrados {sorted(pareceres_encontrados)}"
    )

    consolidado = (pasta_pareceres / "parecer_consolidado.md").read_text(
        encoding="utf-8"
    )
    assert "revisão obrigatória" in consolidado.lower()
    assert "64%" in consolidado

    pasta_rodada_2 = pasta_pareceres / "rodada_02"
    rodada_2_esperados = {
        "README.md",
        "01_nivel_academico.md",
        "02_didatica.md",
        "03_alinhamento.md",
        "04_humanidades_digitais.md",
        "05_referencias.md",
        "06_tecnico_acessibilidade.md",
        "avaliacao_tipologia_perguntas.md",
        "parecer_consolidado.md",
    }
    rodada_2_encontrados = {
        caminho.name for caminho in pasta_rodada_2.glob("*.md")
    }
    assert rodada_2_encontrados == rodada_2_esperados
    consolidado_2 = (pasta_rodada_2 / "parecer_consolidado.md").read_text(
        encoding="utf-8"
    )
    assert "Aprovada com ajuste" in consolidado_2
    assert "87%" in consolidado_2

    pasta_rodada_3 = pasta_pareceres / "rodada_03"
    rodada_3_esperados = {
        "README.md",
        "01_nivel_academico.md",
        "02_didatica.md",
        "03_alinhamento.md",
        "05_referencias.md",
        "parecer_consolidado.md",
    }
    rodada_3_encontrados = {
        caminho.name for caminho in pasta_rodada_3.glob("*.md")
    }
    assert rodada_3_encontrados == rodada_3_esperados
    consolidado_3 = (pasta_rodada_3 / "parecer_consolidado.md").read_text(
        encoding="utf-8"
    )
    assert "Aprovada" in consolidado_3
    assert "100%" in consolidado_3


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
    print("OK presença textual: 9/9 tópicos da ementa")
    validar_referencias()
    print("OK referências: bibliografia consolidada e leituras nos notebooks")
    validar_exercicios_html()
    print(
        "OK exercícios: 18 questões, 10 tópicos, HTML offline e versão textual"
    )
    validar_gabaritos()
    print("OK gabaritos: 5 arquivos de respostas e 1 guia docente")
    validar_revisores()
    print(
        "OK revisores: 6 especialidades, coordenação, matriz, modelo e "
        "3 rodadas de pareceres executadas"
    )
    print(
        f"OK total: {len(notebooks)} notebooks, "
        f"{total_textos} células de texto, {total_codigos} de código"
    )


if __name__ == "__main__":
    main()
