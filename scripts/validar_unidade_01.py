"""Valida a estrutura e executa as células de código da Unidade 1."""

from __future__ import annotations

import json
import os
import re
import xml.etree.ElementTree as ET
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
            assert celula.get("id"), f"célula {numero} sem identificador nbformat"
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


def validar_imagens() -> None:
    pasta = UNIDADE / "imagens"
    esperados = {
        "README.md",
        "00_abertura_conceitual.png",
        "00_percurso_unidade.svg",
        "01_matriz_perguntas.svg",
        "01_questao_tarefa_interpretacao.svg",
        "02_ciclo_operacionalizacao.svg",
        "02_conceito_dimensoes.svg",
        "02_representacoes_temas.svg",
        "03_populacao_amostra_corpus.svg",
        "03_periodico_1890.jpg",
        "03_cadeia_evidencia.svg",
        "04_construcao_projeto.svg",
    }
    encontrados = {caminho.name for caminho in pasta.iterdir() if caminho.is_file()}
    assert encontrados == esperados, (
        f"imagens divergentes: esperadas {sorted(esperados)}, "
        f"encontradas {sorted(encontrados)}"
    )

    referencias: list[tuple[str, str, str]] = []
    for notebook in sorted(UNIDADE.glob("*.ipynb")):
        documento = json.loads(notebook.read_text(encoding="utf-8"))
        conteudo = "\n".join(
            fonte_da_celula(celula)
            for celula in documento["cells"]
            if celula.get("cell_type") == "markdown"
        )
        for alt, caminho in re.findall(r"!\[([^]]*)\]\(([^)]+)\)", conteudo):
            referencias.append((notebook.name, alt.strip(), caminho.strip()))

    assert len(referencias) == len(esperados) - 1, (
        f"esperadas {len(esperados) - 1} imagens nos notebooks; "
        f"encontradas {len(referencias)}"
    )
    for notebook, alt, caminho in referencias:
        assert alt, f"imagem sem texto alternativo em {notebook}"
        assert not caminho.startswith(("http://", "https://")), (
            f"imagem remota em {notebook}: {caminho}"
        )
        assert caminho.startswith("imagens/"), (
            f"caminho visual fora da pasta imagens em {notebook}: {caminho}"
        )
        assert (UNIDADE / caminho).is_file(), (
            f"imagem ausente em {notebook}: {caminho}"
        )

    usados = {Path(caminho).name for _, _, caminho in referencias}
    assert usados == esperados - {"README.md"}

    for caminho in sorted(pasta.glob("*.svg")):
        raiz = ET.parse(caminho).getroot()
        namespace = "{http://www.w3.org/2000/svg}"
        titulo = raiz.find(f"{namespace}title")
        descricao = raiz.find(f"{namespace}desc")
        assert titulo is not None and (titulo.text or "").strip(), (
            f"{caminho.name} sem title acessível"
        )
        assert descricao is not None and (descricao.text or "").strip(), (
            f"{caminho.name} sem desc acessível"
        )
        assert raiz.get("role") == "img", f"{caminho.name} sem role=img"

    assert (pasta / "00_abertura_conceitual.png").read_bytes().startswith(b"\x89PNG")
    assert (pasta / "03_periodico_1890.jpg").read_bytes().startswith(b"\xff\xd8")

    creditos = (pasta / "README.md").read_text(encoding="utf-8")
    for nome in esperados - {"README.md"}:
        assert nome in creditos, f"{nome} ausente dos créditos"
    assert "Acervo da Fundação Biblioteca Nacional" in creditos
    assert "domínio público" in creditos
    assert "não integra a coleção fictícia" in creditos
    assert "ilustração conceitual" in creditos.lower()


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
        "BABBIE, Earl",
        "ADCOCK, Robert",
        "KRIPPENDORFF, Klaus",
        "RILEY, Jenn",
        "BOWKER, Geoffrey",
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
    titulos_metodologicos = [
        "The Practice of Social Research",
        "Measurement Validity: A Shared Standard for Qualitative and Quantitative Research",
        "Content Analysis: An Introduction to Its Methodology",
        "Understanding Metadata: What Is Metadata, and What Is It For? A Primer",
        "Sorting Things Out: Classification and Its Consequences",
    ]
    referencias_normalizadas = " ".join(referencias.split())
    ausentes = [
        titulo
        for titulo in titulos_metodologicos
        if titulo not in referencias_normalizadas
    ]
    assert not ausentes, f"títulos metodológicos ausentes: {', '.join(ausentes)}"

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
    assert "Atividade em dupla" not in conteudo_guia
    assert conteudo_guia.index(
        "## Produto final da unidade e critérios de avaliação"
    ) < conteudo_guia.index("## Atividade individual — diagnóstico inicial")

    dinamicas_esperadas = {
        "00_guia_da_unidade.ipynb": [
            "Modalidade:** individual",
            "Esta é a única atividade do guia",
        ],
        "01_perguntas_e_problemas_computacionais.ipynb": [
            "uma questão substantiva:** por exemplo",
            "fontes produzidas em contextos específicos:** por exemplo",
            "uma forma explícita de representação:** por exemplo",
            "operações que geram resultados:** por exemplo",
            "interpretação situada e crítica:** por exemplo",
            "| Pergunta | Finalidade | Estrutura | Operação inicial |",
            "| Nível | Função | Exemplo |",
            "Interpretação humanística",
            "seu resultado não substitui a interpretação",
            "Modalidade:** trios",
            "Atividade em trio e plenária — casos limítrofes",
            "Atividade em dupla — compreender e delimitar o interesse do colega",
            "Quero compreender __________ no contexto __________",
            "Atividade autônoma — produto parcial",
        ],
        "02_representacao_e_operacionalizacao.ipynb": [
            "## Mapa do percurso",
            "pergunta → conceito e dimensão → indicador → unidade de análise",
            "variáveis, valores, documentos e metadados → categorias históricas e",
            "As etapas formam um ciclo",
            "síntese didática elaborada para a unidade",
            "Babbie (2021, cap. 5)",
            "Adcock e Collier (2001)",
            "Krippendorff (2019, cap. 5)",
            "Riley (2017)",
            "Bowker e Star (1999)",
            "Rodrigues (2020)",
            "## 1. Conceito e dimensão",
            "## 2. Indicador",
            "Exemplo — do conceito e da dimensão ao indicador",
            "## 3. Unidade de análise",
            "### Exemplo de estrutura tabular",
            "## 4. Variáveis, valores, documentos e metadados",
            "`genero` é a variável e `editorial`",
            "## 5. Categorias históricas e analíticas",
            "### O que são categorias históricas?",
            "Categoria presente na fonte",
            "Categoria institucional",
            "Categoria analítica",
            "`termo_na_fonte`",
            "`regra_de_correspondencia`",
            "## 6. Comparação de representações",
            "Experimento — uma decisão de representação altera a contagem",
            "documentos_temas.explode",
            "## 7. Validade da representação",
            "## 8. Mapa de operacionalização",
            "### Possibilidades de dimensão para o conceito do exemplo",
            "| Recorrência temporal | Com que regularidade o tema aparece na coleção? |",
            "| Protagonismo | Quem recebe voz ou capacidade de agir? |",
            "As dimensões não são universais nem intercambiáveis",
            "### Exemplo preenchido — duas alternativas para o mesmo conceito",
            "| Centralidade do tema educação | Presença temática | Tema dominante atribuído |",
            "Use o exemplo como modelo de encadeamento entre as colunas",
            "### De onde vêm os elementos do percurso?",
            "| 8. Mapa de operacionalização | Síntese didática desta unidade |",
            "os autores não empregam necessariamente os mesmos termos",
            "| Conceito | Dimensão | Indicador | Unidade de análise | Variável | Categorias ou valores | Fonte | Regra | Limitação |",
            "produção individual seguida de comparação em dupla",
        ],
        "03_dados_corpus_e_evidencias.ipynb": [
            "produção individual seguida de revisão em dupla",
            "| Arquivo do exemplo | Classificação neste notebook | Por quê? |",
            "| CSV (`documentos_exemplo.csv`) | Estruturado |",
            "| JSON (`metadados_exemplo.json`) | Semiestruturado |",
            "| TXT (`texto_exemplo.txt`) | Não estruturado |",
            "não uma propriedade absoluta da extensão do arquivo",
            "### Objetivo da seção",
            "| Dados registrados | valores `Capital` e `Interior` na coluna `local` |",
            "### A cadeia de produção da evidência",
            "| Operação | aplicação de `value_counts()` à coluna `local` |",
            "### Experimento — contar registros por categoria local",
            "### Como ler a saída",
            "A produção jornalística da Capital e do Interior era igual",
            "o Python ainda poderá produzir `6` e `6`",
        ],
        "04_oficina_projeto_de_pesquisa.ipynb": [
            "Modalidade:** elaboração individual",
            "| Conceito | Dimensão | Indicador | Variável | Categorias ou valores | Fonte | Regra | Limitação |",
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
        conteudo_normalizado = " ".join(conteudo.split())
        ausentes = [
            marcador
            for marcador in marcadores
            if " ".join(marcador.split()) not in conteudo_normalizado
        ]
        assert not ausentes, f"{nome} sem dinâmica: {', '.join(ausentes)}"

    caminho_notebook_01 = UNIDADE / "01_perguntas_e_problemas_computacionais.ipynb"
    documento_notebook_01 = json.loads(caminho_notebook_01.read_text(encoding="utf-8"))
    notebook_01 = "\n".join(
        fonte_da_celula(celula) for celula in documento_notebook_01["cells"]
    )
    assert "| Pergunta | Finalidade | Estrutura | Operação inicial |" in notebook_01
    assert "| Descritiva | Comparativa |" in notebook_01
    assert "| Explicativa | Comparativa e associativa |" in notebook_01
    assert "| Preditiva | Associativa |" in notebook_01
    assert "Shmueli (2010)" in notebook_01
    assert titulo_alves in " ".join(notebook_01.split())

    caminho_notebook_02 = UNIDADE / "02_representacao_e_operacionalizacao.ipynb"
    documento_notebook_02 = json.loads(caminho_notebook_02.read_text(encoding="utf-8"))
    notebook_02 = "\n".join(
        fonte_da_celula(celula) for celula in documento_notebook_02["cells"]
    )
    assert notebook_02.index("## 1. Conceito e dimensão") < notebook_02.index(
        "### Possibilidades de dimensão para o conceito do exemplo"
    ) < notebook_02.index("## 2. Indicador")
    assert "A última coluna apenas antecipa exemplos" in notebook_02

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
        "gabarito_00_guia.md",
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

    guia_gabaritos = (pasta / "README.md").read_text(encoding="utf-8")
    assert "## Cobertura das atividades" in guia_gabaritos
    assert "Notebook 00: diagnóstico inicial" in guia_gabaritos
    assert "Notebook 04: autoavaliação e revisão entre pares" in guia_gabaritos

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

    operacionalizacao = (
        pasta / "gabarito_02_operacionalizacao.md"
    ).read_text(encoding="utf-8")
    assert "| progresso | 0 | 1 |" in operacionalizacao
    assert "a soma é cinco" in operacionalizacao
    assert "Como usar as referências na resolução" in operacionalizacao
    assert "mapa de oito etapas do notebook é uma síntese didática" in operacionalizacao

    marcadores_detalhamento = {
        "gabarito_00_guia.md": [
            "Exemplo de resolução preenchida",
            "Exemplo de leitura docente e encaminhamento",
        ],
        "gabarito_01_perguntas.md": [
            "Checklist de revisão — exemplo resolvido",
            "Casos limítrofes — exemplo de resolução",
            "Revisão em dupla — exemplo preenchido",
            "Linha de raciocínio da resolução",
        ],
        "gabarito_02_operacionalizacao.md": [
            "Resolução das quatro perguntas do experimento",
            "Exemplo de tratamento de uma categoria histórica",
            "Exemplo de comparação e revisão em dupla",
        ],
        "gabarito_03_corpus.md": [
            "Como acompanhar a resolução",
            "Resumo programático do Corpus A",
            "Revisão em dupla — exemplo de resolução",
        ],
        "gabarito_04_oficina.md": [
            "Como acompanhar o exemplo de resolução",
            "Autoavaliação — exemplo de resolução",
            "Revisão entre pares — exemplo de resolução",
        ],
    }
    for nome, marcadores in marcadores_detalhamento.items():
        conteudo = (pasta / nome).read_text(encoding="utf-8")
        ausentes = [marcador for marcador in marcadores if marcador not in conteudo]
        assert not ausentes, f"{nome} sem exemplos detalhados: {', '.join(ausentes)}"

    multipla_escolha = (
        pasta / "gabarito_exercicios_multipla_escolha.md"
    ).read_text(encoding="utf-8")
    assert multipla_escolha.count("**Como resolver:**") == 18
    assert multipla_escolha.count("**Por que as demais estão incorretas:**") == 18


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
        if caminho.name == "02_representacao_e_operacionalizacao.ipynb":
            assert codigos == 1, (
                "o Notebook 02 deve manter apenas o experimento comparativo"
            )
        total_textos += textos
        total_codigos += codigos
        print(f"OK {caminho.name}: {textos} células de texto, {codigos} de código")

    validar_cobertura()
    print("OK presença textual: 9/9 tópicos da ementa")
    validar_referencias()
    print("OK referências: bibliografia consolidada e leituras nos notebooks")
    validar_imagens()
    print("OK imagens: arquivos locais, textos alternativos, créditos e SVGs acessíveis")
    validar_exercicios_html()
    print(
        "OK exercícios: 18 questões, 10 tópicos, HTML offline e versão textual"
    )
    validar_gabaritos()
    print("OK gabaritos: 6 arquivos de respostas e 1 guia docente")
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
