"""Gera notebooks, dados didáticos e README da Unidade 1.

O script usa apenas a biblioteca padrão para que a estrutura dos notebooks
possa ser reconstruída mesmo antes da instalação do Jupyter. Ele não gera o
HTML, os gabaritos, as referências, os revisores ou os pareceres.
"""

from __future__ import annotations

import csv
import json
from pathlib import Path
from textwrap import dedent


RAIZ = Path(__file__).resolve().parents[1]
UNIDADE = RAIZ / "unidade_01"
DADOS = UNIDADE / "dados"


def texto(conteudo: str) -> dict:
    return {
        "cell_type": "markdown",
        "metadata": {},
        "source": dedent(conteudo).strip().splitlines(keepends=True),
    }


def codigo(conteudo: str) -> dict:
    return {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": dedent(conteudo).strip().splitlines(keepends=True),
    }


def notebook(celulas: list[dict]) -> dict:
    return {
        "cells": celulas,
        "metadata": {
            "kernelspec": {
                "display_name": "Python 3",
                "language": "python",
                "name": "python3",
            },
            "language_info": {
                "name": "python",
                "version": "3",
                "mimetype": "text/x-python",
                "codemirror_mode": {"name": "ipython", "version": 3},
                "pygments_lexer": "ipython3",
                "nbconvert_exporter": "python",
                "file_extension": ".py",
            },
        },
        "nbformat": 4,
        "nbformat_minor": 5,
    }


def salvar_notebook(nome: str, celulas: list[dict]) -> None:
    caminho = UNIDADE / nome
    caminho.write_text(
        json.dumps(notebook(celulas), ensure_ascii=False, indent=1) + "\n",
        encoding="utf-8",
    )


def criar_dados() -> None:
    DADOS.mkdir(parents=True, exist_ok=True)
    registros = [
        ["D001", 1890, "Jornal Aurora", "editorial", "Capital", "progresso", 860],
        ["D002", 1891, "Jornal Aurora", "carta", "Interior", "trabalho", 420],
        ["D003", 1892, "Gazeta Popular", "notícia", "Capital", "educação", 610],
        ["D004", 1893, "Gazeta Popular", "editorial", "Capital", "progresso", 940],
        ["D005", 1894, "Correio do Vale", "carta", "Interior", "educação", 380],
        ["D006", 1895, "Correio do Vale", "notícia", "Interior", "trabalho", 550],
        ["D007", 1900, "Jornal Aurora", "notícia", "Capital", "educação", 720],
        ["D008", 1901, "Jornal Aurora", "editorial", "Capital", "trabalho", 1010],
        ["D009", 1902, "Gazeta Popular", "carta", "Interior", "progresso", 460],
        ["D010", 1903, "Gazeta Popular", "notícia", "Capital", "trabalho", 670],
        ["D011", 1904, "Correio do Vale", "editorial", "Interior", "educação", 890],
        ["D012", 1905, "Correio do Vale", "carta", "Interior", "progresso", 440],
    ]
    with (DADOS / "documentos_exemplo.csv").open(
        "w", encoding="utf-8", newline=""
    ) as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerow(
            ["id", "ano", "periodico", "genero", "local", "tema", "palavras"]
        )
        escritor.writerows(registros)

    metadados = {
        "titulo": "Coleção didática de periódicos",
        "natureza": "dados fictícios para fins de ensino",
        "descricao": (
            "Doze registros simulados inspirados em práticas de catalogação "
            "de periódicos, sem correspondência com documentos históricos reais."
        ),
        "cobertura_temporal": {"inicio": 1890, "fim": 1905},
        "campos": [
            {"nome": "id", "descricao": "identificador do documento"},
            {"nome": "ano", "descricao": "ano atribuído ao documento"},
            {"nome": "periodico", "descricao": "título fictício do periódico"},
            {"nome": "genero", "descricao": "gênero documental atribuído"},
            {"nome": "local", "descricao": "localidade em categoria ampla"},
            {"nome": "tema", "descricao": "tema dominante atribuído manualmente"},
            {"nome": "palavras", "descricao": "extensão simulada em palavras"},
        ],
        "limitacoes": [
            "coleção pequena e não representativa",
            "categorias simplificadas para fins didáticos",
            "ausência do texto integral de cada documento",
            "intervalos temporais descontínuos",
        ],
    }
    (DADOS / "metadados_exemplo.json").write_text(
        json.dumps(metadados, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    (DADOS / "texto_exemplo.txt").write_text(
        (
            "Nesta edição fictícia, o periódico debate a abertura de uma escola "
            "noturna. O texto associa instrução, trabalho e progresso, mas não "
            "registra as vozes das pessoas que frequentariam a instituição. "
            "Este fragmento foi criado exclusivamente para atividades didáticas.\n"
        ),
        encoding="utf-8",
    )


def guia() -> list[dict]:
    return [
        texto(
            """
            # Unidade 1 — Guia de estudo

            ## Como transformar uma questão das Humanidades em um problema computacional?

            **Problema orientador:** como representar computacionalmente um fenômeno
            histórico, social, linguístico ou cultural sem reduzir indevidamente sua
            complexidade?

            Esta unidade não parte da ferramenta. Ela parte de uma pergunta e examina
            as decisões necessárias para que fontes, conceitos e observações possam ser
            tratados computacionalmente. O objetivo não é eliminar a interpretação,
            mas tornar explícita a relação entre pergunta, dados, método e argumento.
            """
        ),
        texto(
            """
            ## Objetivos de aprendizagem

            Ao final do percurso, você deverá ser capaz de:

            1. distinguir cinco tipos de pergunta de pesquisa;
            2. operacionalizar conceitos sem confundi-los com seus indicadores;
            3. definir unidade de análise, população, amostra e corpus;
            4. reconhecer dados estruturados, semiestruturados e não estruturados;
            5. relacionar documentos, variáveis, categorias e metadados;
            6. avaliar o alcance e os limites de uma evidência computacional;
            7. formular a pergunta inicial do projeto da disciplina.
            """
        ),
        texto(
            """
            ## Percurso

            | Notebook | Questão central | Produto |
            |---|---|---|
            | 00 | Como a unidade está organizada? | Diagnóstico inicial |
            | 01 | Que tipo de pergunta estamos fazendo? | Pergunta reformulada |
            | 02 | Como representar conceitos e observações? | Mapa de operacionalização |
            | 03 | Que conjunto de dados sustenta a análise? | Ficha do corpus |
            | 04 | O projeto é coerente e viável? | Formulação inicial do projeto |

            Os exemplos usam uma **coleção inteiramente fictícia** de doze registros
            de periódicos. Ela serve para tornar as decisões visíveis; não permite
            conclusões históricas reais.
            """
        ),
        codigo(
            """
            # Verificação inicial do ambiente
            import sys
            from pathlib import Path

            print("Versão do Python:", sys.version.split()[0])
            print("Diretório atual:", Path.cwd())
            """
        ),
        texto(
            """
            ## Como trabalhar com os notebooks

            Execute as células na ordem. Leia a explicação antes de observar a saída.
            Escreva respostas discursivas nas células Markdown indicadas. Nas células
            Python, primeiro preveja o resultado, depois execute e interprete. Reinicie
            o kernel e execute tudo novamente antes de entregar.

            Um resultado numérico responde apenas à operação programada. Pergunte
            sempre: **que decisão tornou esse número possível, o que ele representa e
            o que ficou fora da representação?**
            """
        ),
        texto(
            """
            ## Carga e prioridades

            A carga da unidade é de oito horas:

            | Modalidade | Atividade | Tempo |
            |---|---|---:|
            | Preparação | Trechos de Alves (2016) | 30 min |
            | Aula 1 | Guia, Notebook 01 e início do 02 | 3 h 30 |
            | Preparação | Estudo de caso de Rodrigues (2020) | 40 min |
            | Aula 2 | Conclusão do 02, Notebook 03 e oficina | 3 h |
            | Revisão assíncrona | Quiz HTML | 20 min |

            São **essenciais**: a pergunta reformulada, o mapa de operacionalização,
            a ficha do corpus e a síntese da oficina. Leituras complementares e
            extensões dos exercícios podem ser feitas após a unidade.
            """
        ),
        texto(
            """
            ## Leituras essenciais

            - ALVES, Daniel (2016), “As Humanidades Digitais como uma comunidade
              de práticas”, especialmente a introdução.
            - RODRIGUES, Aldair (2020), “Humanidades digitais e diáspora africana”,
              como estudo de caso para a segunda aula.

            As referências completas e os links estão em `referencias.md`.
            """
        ),
        texto(
            """
            ## Diagnóstico inicial

            Responda diretamente nesta célula Markdown. Não há respostas certas.

            **Tema de interesse:**
            Escreva aqui.

            **Experiência com Python:**
            Escreva aqui.

            **Tipos de fonte com que gostaria de trabalhar:**
            Escreva aqui.

            **Maior dúvida sobre a transformação de uma questão em dados:**
            Escreva aqui.
            """
        ),
        texto(
            """
            ## Produto e avaliação

            O produto final será uma formulação inicial, não uma promessa definitiva.
            Ela deverá apresentar: fenômeno, contexto, pergunta, tipo de pergunta,
            unidade de análise, recorte, fontes possíveis, operacionalizações,
            evidências esperadas e limitações.

            A avaliação valoriza a **coerência entre as escolhas** e a capacidade de
            reconhecer limites. Uma pergunta modesta e bem delimitada é preferível a
            uma pergunta grandiosa que os dados não podem sustentar.
            """
        ),
        texto(
            """
            ## Antes de continuar

            Escreva em uma frase:

            > Quero compreender __________ no contexto __________, observando
            > inicialmente __________.

            Guarde essa frase. Ela será revista nos quatro notebooks seguintes.
            """
        ),
    ]


def perguntas() -> list[dict]:
    return [
        texto(
            """
            # Perguntas e problemas computacionais

            ## Retomada

            Antes de continuar:

            1. Que fenômeno você registrou no guia?
            2. Que fonte permitiria observar apenas uma parte dele?

            ## 1. Humanidades Digitais e pesquisa orientada por dados

            Humanidades Digitais não são apenas a aplicação de ferramentas digitais
            a objetos tradicionais. Elas incluem práticas de construção de acervos,
            modelagem, análise, visualização, crítica de infraestruturas e reflexão
            sobre como tecnologias participam da produção do conhecimento.

            Não há uma definição única e neutra do campo. Alves (2016) propõe
            compreendê-lo como comunidade de práticas; Burdick et al. (2012) destacam
            formas de produção de conhecimento que incluem modelagem, curadoria,
            visualização e construção. No Brasil, Ferla, Lima e Feitler (2020)
            mostram como condições institucionais e pedagógicas situadas afetam sua
            realização.

            Uma pesquisa orientada por dados articula:

            - uma questão substantiva;
            - fontes produzidas em contextos específicos;
            - uma forma explícita de representação;
            - operações que geram resultados;
            - interpretação situada e crítica.

            Dados não são o fenômeno em estado puro. Drucker (2011) propõe o termo
            *capta* para enfatizar que registros são tomados e construídos. Lavin
            (2021) concorda com a crítica à neutralidade, mas defende “dados situados”
            em vez de abandonar o termo *data*. A divergência é produtiva: ambos
            exigem que seleção, descrição e transformação sejam explicitadas.
            """
        ),
        texto(
            """
            ## 2. Cinco tipos de pergunta

            - **Descritiva:** caracteriza ocorrências ou distribuições.
              Ex.: quais temas aparecem nos editoriais da coleção?
            - **Comparativa:** procura diferenças ou semelhanças.
              Ex.: os temas diferem entre Capital e Interior?
            - **Associativa:** investiga se características variam juntas.
              Ex.: gênero documental e tema aparecem associados?
            - **Explicativa:** pergunta por mecanismos ou fatores relacionados a um
              resultado, exigindo uma teoria e cautela causal.
              Ex.: que condições ajudam a explicar mudanças no debate educacional?
            - **Preditiva:** busca estimar um resultado desconhecido a partir de
              características disponíveis.
              Ex.: metadados permitem prever o gênero de um documento?

            Uma mesma temática comporta perguntas diferentes. O verbo usado oferece
            pistas, mas o tipo depende da finalidade lógica da investigação.
            """
        ),
        texto(
            """
            ### Como ler o primeiro experimento

            `pd.DataFrame(perguntas)` transforma uma lista de registros em uma tabela.
            Cada dicionário vira uma linha; as chaves viram colunas. Antes de executar,
            preveja quantas linhas e colunas aparecerão.

            O objetivo não é aprender toda a sintaxe de `pandas`, mas observar que uma
            tipologia pode ser registrada e consultada — e que o código não justifica
            as categorias por nós.
            """
        ),
        codigo(
            """
            import pandas as pd

            perguntas = [
                {
                    "pergunta": "Quais temas aparecem nos documentos?",
                    "tipo": "descritiva",
                    "operacao_inicial": "contar ocorrências por tema",
                },
                {
                    "pergunta": "Os temas diferem entre Capital e Interior?",
                    "tipo": "comparativa",
                    "operacao_inicial": "comparar distribuições",
                },
                {
                    "pergunta": "Gênero documental e tema variam juntos?",
                    "tipo": "associativa",
                    "operacao_inicial": "cruzar categorias",
                },
                {
                    "pergunta": "Que processos explicam a mudança do debate?",
                    "tipo": "explicativa",
                    "operacao_inicial": "formular e confrontar explicações",
                },
                {
                    "pergunta": "É possível estimar o gênero pelos metadados?",
                    "tipo": "preditiva",
                    "operacao_inicial": "treinar e avaliar uma previsão",
                },
            ]

            tabela_perguntas = pd.DataFrame(perguntas)
            tabela_perguntas
            """
        ),
        texto(
            """
            Na célula seguinte, a expressão entre colchetes produz uma sequência de
            valores verdadeiros e falsos. Ela mantém somente as linhas cujo tipo é
            “comparativa”. Preveja o número de linhas antes de executar.
            """
        ),
        codigo(
            """
            # Filtrar uma categoria é simples; justificar a categoria é parte da pesquisa.
            tabela_perguntas[tabela_perguntas["tipo"] == "comparativa"]
            """
        ),
        texto(
            """
            ## 3. Da questão humanística à tarefa computacional

            Compare três níveis:

            1. **Questão ampla:** como ideias de progresso participaram da vida social?
            2. **Pergunta delimitada:** como o tema “progresso” aparece nos gêneros
               editoriais de três periódicos entre 1890 e 1905?
            3. **Tarefa computacional:** selecionar editoriais, contar a categoria
               temática atribuída e comparar períodos.

            A tarefa não substitui a pergunta. Uma contagem pode indicar um padrão;
            compreender seu sentido demanda retornar aos documentos, às condições de
            produção, às categorias adotadas e à historiografia pertinente.
            """
        ),
        texto(
            """
            ### Exemplo completo

            **Questão ampla:** Como ideias de progresso participaram da vida social?

            **Pergunta delimitada:** Como o tema “progresso” aparece em editoriais de
            três periódicos da coleção didática entre 1890 e 1905?

            **Tarefa computacional:** Selecionar editoriais, contar temas atribuídos e
            comparar períodos.

            **Interpretação necessária:** Reler os documentos selecionados e
            contextualizar os diferentes sentidos de “progresso”.

            Observe que apenas a terceira formulação descreve uma operação. As demais
            registram o problema substantivo e o trabalho interpretativo.
            """
        ),
        texto(
            """
            ## 4. Tratabilidade não significa importância

            Uma pergunta é computacionalmente tratável quando há uma relação plausível
            entre o que ela pergunta e operações realizáveis sobre dados disponíveis.
            Isso não significa que:

            - toda pergunta deva ser quantificada;
            - o que é fácil de contar seja o mais relevante;
            - categorias sejam neutras;
            - correlação produza explicação;
            - previsão produza compreensão;
            - fontes digitalizadas representem todas as experiências.

            A formulação deve equilibrar relevância humanística, viabilidade empírica e
            responsabilidade interpretativa.
            """
        ),
        texto(
            """
            ### Checklist de revisão

            Releia sua pergunta e marque:

            - [ ] o fenômeno de interesse está explícito;
            - [ ] o contexto está informado;
            - [ ] é possível identificar o que será observado;
            - [ ] há ao menos uma fonte plausível;
            - [ ] o recorte é compatível com o tempo da disciplina;
            - [ ] a pergunta não promete mais do que os dados podem sustentar.

            Este checklist apoia uma decisão argumentativa. Ele não pode decidir
            automaticamente se uma pergunta é relevante ou teoricamente adequada.
            """
        ),
        texto(
            """
            ## Atividade guiada — classifique com justificativa

            Para cada pergunta abaixo, indique o tipo predominante e justifique:

            1. Quais personagens falam mais em um conjunto de romances?
            2. A presença de personagens femininas difere entre dois períodos?
            3. A posição social de uma personagem está relacionada ao número de falas?
            4. Que convenções literárias ajudam a explicar essas diferenças?
            5. É possível prever o período do romance por características do vocabulário?

            Depois, preencha a seção seguinte.
            """
        ),
        texto(
            """
            ### Minhas classificações

            1. **Tipo:** Escreva aqui.
               **Justificativa:** Escreva aqui.
            2. **Tipo:** Escreva aqui.
               **Justificativa:** Escreva aqui.
            3. **Tipo:** Escreva aqui.
               **Justificativa:** Escreva aqui.
            4. **Tipo:** Escreva aqui.
               **Justificativa:** Escreva aqui.
            5. **Tipo:** Escreva aqui.
               **Justificativa:** Escreva aqui.
            """
        ),
        texto(
            """
            ### Casos limítrofes

            Uma investigação pode ter etapas de tipos diferentes. Considere:

            > Quais mudanças no vocabulário distinguem dois períodos e que processos
            > históricos ajudam a explicá-las?

            A comparação produz o padrão inicial; a explicação exige teoria, contexto
            e confronto de mecanismos. Indique qual tipo é predominante, quais são as
            etapas secundárias e como a pergunta mudaria se o objetivo fosse prever o
            período de um documento.
            """
        ),
        texto(
            """
            ## Atividade autônoma — produto parcial

            Reformule seu interesse em três níveis:

            - questão humanística ampla;
            - pergunta delimitada, com fenômeno, contexto e recorte;
            - tarefa computacional inicial.

            Em seguida, registre o que a tarefa **não** será capaz de responder.
            """
        ),
        texto(
            """
            ### Meu produto parcial

            **Questão ampla:**
            Escreva aqui.

            **Pergunta delimitada:**
            Escreva aqui.

            **Tipo predominante e justificativa:**
            Escreva aqui.

            **Tarefa computacional inicial:**
            Escreva aqui.

            **O que essa tarefa deixa de fora:**
            Escreva aqui.
            """
        ),
        texto(
            """
            ## Referências e leituras

            - ALVES, Daniel (2016). “As Humanidades Digitais como uma comunidade de
              práticas”.
            - BURDICK, Anne et al. (2012). *Digital_Humanities*.
            - DRUCKER, Johanna (2011). “Humanities Approaches to Graphical Display”.
            - LAVIN, Matthew (2021). “Why Digital Humanists Should Emphasize Situated
              Data over Capta”.
            - FERLA, Luis A.; LIMA, Luís F.; FEITLER, Bruno (2020).
              “Novidades no front”.

            Dados completos e links: `referencias.md`.
            """
        ),
        texto(
            """
            ## Síntese

            A boa formulação não nasce da simples tradução de uma pergunta em código.
            Ela nasce de um ciclo: formular, representar, testar a viabilidade, examinar
            as perdas e reformular. No próximo notebook, estudaremos o centro desse
            processo: a operacionalização.
            """
        ),
    ]


def operacionalizacao() -> list[dict]:
    return [
        texto(
            """
            # Representação e operacionalização

            ## Retomada

            1. Qual foi a pergunta delimitada no Notebook 01?
            2. Que palavra ou expressão dessa pergunta ainda precisa ser definida?

            ## 1. Do conceito ao registro

            Conceitos como modernização, identidade, prestígio, violência ou
            participação política não aparecem prontos em uma planilha. Para analisá-los,
            construímos relações entre:

            - **conceito teórico:** ideia que orienta a investigação;
            - **dimensão:** aspecto particular do conceito;
            - **indicador:** evidência observável escolhida;
            - **variável:** campo em que registramos valores;
            - **categoria ou valor:** forma assumida por uma observação.

            **Operacionalizar** é construir e justificar essas relações. O indicador
            aponta para o conceito, mas não é idêntico a ele. A crítica de Drucker
            (2011) ajuda a perceber que a representação não apenas descreve o objeto:
            ela produz uma forma particular de torná-lo observável.
            """
        ),
        texto(
            """
            ### Exemplo de mapa de operacionalização

            | Conceito | Dimensão | Indicador | Variável | Limitação |
            |---|---|---|---|---|
            | Centralidade do tema educação | Presença no documento | Tema dominante atribuído | `tema` | Um único tema apaga ambiguidades |
            | Centralidade do tema educação | Extensão da discussão | Palavras no trecho pertinente | `palavras_sobre_educacao` | Extensão não equivale a importância |

            A tabela serve para documentar uma decisão conceitual. Ela não precisa ser
            criada em Python, pois ainda não contém observações a serem processadas.
            """
        ),
        texto(
            """
            ## 2. Unidade de análise

            A unidade de análise é a entidade sobre a qual fazemos afirmações: pessoa,
            documento, parágrafo, evento, instituição, município, imagem ou relação.

            Ela não deve ser confundida com:

            - **fonte:** material do qual extraímos informação;
            - **unidade de observação:** onde uma medida é efetivamente registrada;
            - **nível de agregação:** escala em que resumimos resultados.

            Um jornal pode ser a fonte, cada artigo a unidade de análise e cada parágrafo
            a unidade de observação. Trocar de unidade altera o significado das medidas.
            """
        ),
        texto(
            """
            ### Como ler o experimento

            A lista `registros` contém três observações. `pd.DataFrame(registros)`
            organiza essas observações em linhas e os campos em colunas.
            `len(documentos)` conta linhas, não jornais, autores ou temas. Antes de
            executar, identifique o que cada linha representa.
            """
        ),
        codigo(
            """
            import pandas as pd

            registros = [
                {"id": "D001", "ano": 1890, "genero": "editorial", "tema": "progresso"},
                {"id": "D002", "ano": 1891, "genero": "carta", "tema": "trabalho"},
                {"id": "D003", "ano": 1892, "genero": "notícia", "tema": "educação"},
            ]
            documentos = pd.DataFrame(registros)

            print("Número de unidades de análise:", len(documentos))
            print("Unidade representada por cada linha: documento")
            documentos
            """
        ),
        texto(
            """
            ## 3. Variáveis, categorias, documentos e metadados

            Em uma tabela, linhas frequentemente representam unidades e colunas
            representam variáveis. Algumas variáveis expressam quantidades; outras,
            categorias ou identificadores.

            Um **documento** é um objeto de pesquisa, não apenas uma sequência de
            caracteres. Seu suporte, autoria, circulação, gênero e proveniência
            participam da interpretação.

            **Metadados** são dados que descrevem, identificam, contextualizam ou
            administram outros dados e documentos. Eles podem ser parte da própria
            análise — por exemplo, data, autoria, local e gênero documental.
            """
        ),
        texto(
            """
            ### Exemplos de campos e papéis

            | Campo | Papel | Exemplo |
            |---|---|---|
            | `id` | Identificador | D001 |
            | `ano` | Variável temporal | 1890 |
            | `genero` | Categoria documental | editorial |
            | `tema` | Categoria analítica | progresso |
            | `texto` | Conteúdo documental | trecho integral |
            | `arquivo_origem` | Metadado de proveniência | caixa_03.pdf |

            A tabela documenta o esquema. O código passa a ser relevante quando há
            registros concretos a inspecionar, transformar ou comparar.
            """
        ),
        texto(
            """
            ## 4. Categorias são decisões

            Categorizar significa produzir equivalências e diferenças. Antes de usar
            uma categoria, pergunte:

            1. ela vem da fonte, de uma instituição ou do pesquisador?
            2. as definições são explícitas?
            3. casos ambíguos podem ser registrados?
            4. as categorias mudaram historicamente?
            5. quem ou o que se torna invisível?

            Categorias históricas podem reproduzir classificações discriminatórias.
            Preservá-las para análise não significa adotá-las sem crítica; transformá-las
            também exige documentação. D'Ignazio e Klein (2020) mostram que decidir o
            que e como contar envolve relações de poder, trabalho e experiências que
            podem desaparecer das estruturas formais.
            """
        ),
        texto(
            """
            No experimento seguinte, compare duas decisões. `value_counts()` conta
            valores exclusivos. A segunda série preserva listas, mas ainda não define
            como cada tema contribuirá para uma contagem. Preveja qual informação se
            perde na primeira representação.
            """
        ),
        codigo(
            """
            # Duas representações do mesmo conjunto produzem perguntas diferentes.
            temas_exclusivos = pd.Series(
                ["educação", "trabalho", "educação"],
                name="um tema dominante por documento",
            )
            temas_multiplos = pd.Series(
                [["educação", "progresso"], ["trabalho"], ["educação", "trabalho"]],
                name="múltiplos temas por documento",
            )

            print("Contagem exclusiva:")
            print(temas_exclusivos.value_counts())
            print("\\nRepresentação com múltiplos temas:")
            print(temas_multiplos)
            """
        ),
        texto(
            """
            A primeira representação facilita uma contagem, mas força exclusividade. A
            segunda preserva coexistências, porém demanda regras para comparar documentos.
            Nenhuma estrutura é naturalmente correta: a escolha depende da pergunta, da
            teoria, das fontes e da qualidade da anotação.
            """
        ),
        texto(
            """
            ## 5. Validade da representação

            Uma operacionalização deve ser examinada em pelo menos quatro dimensões:

            - **validade conceitual:** o indicador corresponde ao conceito?
            - **confiabilidade:** a regra seria aplicada de modo consistente?
            - **cobertura:** casos relevantes conseguem aparecer?
            - **rastreabilidade:** é possível reconstruir como o valor foi produzido?

            Precisão numérica não compensa uma definição conceitual inadequada.
            """
        ),
        texto(
            """
            ### Exemplo de avaliação

            - **Conceito:** presença temática.
            - **Indicador:** tema dominante anotado.
            - **Regra:** atribuir uma categoria após a leitura integral.
            - **Fonte:** documento digitalizado.
            - **Limitação:** discordâncias e temas secundários não aparecem.

            A avaliação depende de justificativa teórica, leitura das fontes e
            comparação entre alternativas; uma função Python apenas verificaria se os
            campos foram preenchidos, não se a operacionalização é válida.

            Rawson e Muñoz (2019) lembram que transformações aparentemente técnicas
            também constroem modelos e autoridades sobre os dados. Registrar a regra é
            parte da produção de conhecimento.
            """
        ),
        texto(
            """
            ## Atividade — mapa de operacionalização

            Escolha um conceito central de sua pergunta. Proponha ao menos duas
            operacionalizações. Compare o que cada uma permite observar e o que perde.
            """
        ),
        texto(
            """
            ### Meu mapa de operacionalização

            Preencha a tabela diretamente nesta célula:

            | Conceito | Dimensão | Indicador | Unidade de análise | Variável ou categoria | Fonte | Regra | Limitação |
            |---|---|---|---|---|---|---|---|
            | Escreva | Escreva | Escreva | Escreva | Escreva | Escreva | Escreva | Escreva |
            | Mesmo conceito | Alternativa | Indicador alternativo | Escreva | Escreva | Escreva | Escreva | Escreva |

            Compare as duas linhas em um pequeno parágrafo:

            Escreva aqui.
            """
        ),
        texto(
            """
            ## Referências e leituras

            - D'IGNAZIO, Catherine; KLEIN, Lauren F. (2020). *Data Feminism*.
            - DRUCKER, Johanna (2011). “Humanities Approaches to Graphical Display”.
            - RAWSON, Katie; MUÑOZ, Trevor (2019). “Against Cleaning”.

            Dados completos e links: `referencias.md`.
            """
        ),
        texto(
            """
            ## Reflexão e síntese

            - O que aconteceria se a unidade fosse alterada?
            - Sua categoria existe nas fontes ou foi criada para analisá-las?
            - Como casos ambíguos serão registrados?
            - Que interpretação seria indevida a partir do indicador?

            Operacionalizar é argumentar sobre a relação entre teoria e observação.
            O próximo notebook acrescenta outra decisão: quais registros formarão o
            conjunto analisado.
            """
        ),
    ]


def corpus() -> list[dict]:
    return [
        texto(
            """
            # Dados, corpus e evidências

            ## Retomada

            1. Qual é sua unidade de análise?
            2. Que indicador você propôs e de qual fonte ele seria extraído?

            ## 1. População, amostra e corpus

            - **População:** conjunto de unidades sobre o qual se deseja formular uma
              afirmação.
            - **Amostra:** subconjunto observado segundo algum procedimento de seleção.
            - **Corpus:** conjunto de materiais reunidos e delimitados para análise,
              comum em estudos documentais, linguísticos e culturais.

            Os termos não são intercambiáveis. Nem todo corpus é uma amostra
            probabilística. Uma coleção digital disponível pode resultar de preservação,
            catalogação, direitos autorais, digitalização e mecanismos de busca; sua
            existência não garante representatividade.
            """
        ),
        texto(
            """
            ### Como ler a importação

            `pd.read_csv(...)` lê o arquivo tabular e cria um `DataFrame`. O caminho é
            relativo à pasta da unidade, para que o exemplo funcione em outros
            computadores. Antes de executar, preveja o número de linhas a partir da
            descrição da coleção.
            """
        ),
        codigo(
            """
            import json
            from pathlib import Path
            import pandas as pd

            PASTA_DADOS = Path("dados")
            if not PASTA_DADOS.exists():
                PASTA_DADOS = Path("unidade_01/dados")

            documentos = pd.read_csv(PASTA_DADOS / "documentos_exemplo.csv")
            documentos
            """
        ),
        texto(
            """
            ## 2. Critérios de inclusão e exclusão

            Um corpus deve ser definido por regras justificáveis e reproduzíveis:

            - período;
            - local;
            - autoria ou instituição;
            - gênero documental;
            - idioma;
            - disponibilidade e qualidade;
            - pertinência temática;
            - condições éticas e legais.

            Disponibilidade pode ser uma condição prática, mas não deve ser ocultada
            como se fosse uma propriedade teórica do fenômeno.
            """
        ),
        texto(
            """
            `between(1890, 1895)` testa o intervalo para cada linha; a condição entre
            colchetes seleciona os registros verdadeiros. O segundo filtro compara a
            coluna `genero` com “editorial”. Os dois corpus respondem a critérios
            diferentes, portanto sustentam afirmações diferentes.
            """
        ),
        codigo(
            """
            # Corpus A: todos os documentos entre 1890 e 1895.
            corpus_a = documentos[documentos["ano"].between(1890, 1895)].copy()

            # Corpus B: apenas editoriais, em todo o período disponível.
            corpus_b = documentos[documentos["genero"] == "editorial"].copy()

            print("Corpus A:", len(corpus_a), "documentos")
            print("Corpus B:", len(corpus_b), "documentos")
            """
        ),
        codigo(
            """
            comparacao = pd.DataFrame({
                "colecao_completa": documentos["tema"].value_counts(),
                "corpus_1890_1895": corpus_a["tema"].value_counts(),
                "apenas_editoriais": corpus_b["tema"].value_counts(),
            }).fillna(0).astype(int)
            comparacao
            """
        ),
        texto(
            """
            A distribuição muda quando muda o critério. Isso não demonstra que um
            corpus seja “tendencioso” e o outro “neutro”; demonstra que toda conclusão
            precisa declarar a qual conjunto se refere e por que ele foi constituído.
            """
        ),
        texto(
            """
            ## Estudo de caso brasileiro — população escravizada de Mariana

            Rodrigues (2020) examina a construção de uma base sobre a população
            escravizada de Mariana no século XVIII. O caso mostra que transpor fontes
            produzidas sob a escravidão para uma base não é simples digitalização:
            categorias, nomes, marcas corporais, proveniência e ausências envolvem
            decisões éticas e metodológicas em um país racialmente desigual.

            Após a leitura orientada, identifique:

            1. qual problema histórico orienta a base;
            2. quem produziu as fontes originais e com quais finalidades;
            3. quem modela, financia e mantém os dados;
            4. que categorias podem reproduzir violência documental;
            5. como preservar rastreabilidade sem naturalizar classificações;
            6. que usos públicos ou acadêmicos exigem cautela.

            Compare o estudo real à coleção fictícia: quais problemas foram
            simplificados no exemplo didático?
            """
        ),
        texto(
            """
            ## 3. Três formas de organização dos dados

            - **Estruturados:** seguem esquema explícito, como uma tabela com colunas.
            - **Semiestruturados:** possuem marcas e hierarquias flexíveis, como JSON ou
              XML.
            - **Não estruturados:** não apresentam previamente uma tabela de campos,
              como texto corrido, áudio e muitas imagens.

            “Não estruturado” não significa sem forma ou sem contexto. Um texto possui
            estrutura linguística e documental; a expressão indica que essa estrutura
            não está previamente organizada como campos regulares para computação.
            """
        ),
        codigo(
            """
            # CSV: estrutura tabular
            print(documentos.dtypes)

            # JSON: chaves, listas e objetos aninhados
            with (PASTA_DADOS / "metadados_exemplo.json").open(encoding="utf-8") as arquivo:
                metadados = json.load(arquivo)
            print("\\nTítulo da coleção:", metadados["titulo"])
            print("Cobertura:", metadados["cobertura_temporal"])

            # TXT: conteúdo textual a ser interpretado ou transformado
            texto_documento = (PASTA_DADOS / "texto_exemplo.txt").read_text(encoding="utf-8")
            print("\\nTexto:", texto_documento)
            """
        ),
        texto(
            """
            ## 4. Documentos e metadados

            O conteúdo do documento e seus metadados respondem a perguntas distintas.
            Buscar “educação” no texto não equivale a usar uma categoria temática
            atribuída por catalogação. O primeiro procedimento depende da palavra
            registrada; o segundo depende de uma interpretação e de uma regra.

            Metadados também têm história: podem conter erros, lacunas, vocabulários
            institucionais e revisões posteriores. Devem ser avaliados como fontes.
            """
        ),
        codigo(
            """
            print("Campos documentados:")
            for campo in metadados["campos"]:
                print(f"- {campo['nome']}: {campo['descricao']}")

            print("\\nLimitações declaradas:")
            for limite in metadados["limitacoes"]:
                print(f"- {limite}")
            """
        ),
        texto(
            """
            ## 5. Evidência computacional e interpretação humanística

            Uma evidência computacional é um resultado produzido por operações
            explícitas sobre uma representação: contagem, correspondência, medida,
            classificação ou visualização. Seu alcance depende de toda a cadeia:

            **fonte → seleção → digitalização → descrição → transformação → operação
            → resultado → interpretação**

            Resultados podem revelar padrões difíceis de perceber por leitura individual,
            orientar casos para leitura aprofundada e testar a extensão de uma impressão.
            Ainda assim, não falam sozinhos. D'Ignazio e Klein (2020) enfatizam que
            números dependem de contexto, teoria e relações de poder.

            O desenho é iterativo:

            **pergunta → amostragem → leitura → modelagem → resultado → releitura
            → reformulação**
            """
        ),
        codigo(
            """
            contagem_local = documentos["local"].value_counts()
            contagem_local
            """
        ),
        texto(
            """
            A saída anterior permite afirmar quantos registros de cada categoria local
            existem **nesta coleção didática**. Ela não permite concluir como era a
            produção jornalística de uma região, porque não conhecemos a população,
            o processo de preservação nem a cobertura documental necessária.

            Uma interpretação responsável explicita o sujeito da frase: “na coleção
            analisada”, e não “na sociedade”.
            """
        ),
        texto(
            """
            ## 6. Limites da quantificação e da automação

            A quantificação pode:

            - tornar padrões comparáveis;
            - revelar exceções e lacunas;
            - dar escala a uma investigação.

            Mas também pode:

            - produzir falsa precisão;
            - estabilizar categorias contestáveis;
            - privilegiar o que sobreviveu e foi digitalizado;
            - apagar ambiguidade, silêncio e contexto;
            - ampliar vieses por meio da automação.

            Automatizar uma regra aumenta sua velocidade e alcance, não sua validade.
            Erros sistemáticos podem ser reproduzidos em grande escala.
            """
        ),
        texto(
            """
            A função seguinte resume um corpus. Cada chave nomeia uma informação e
            cada expressão calcula seu valor. `nunique()` conta valores distintos;
            `sorted(...unique())` organiza as categorias. A função descreve o conjunto,
            mas não avalia sua qualidade ou representatividade.
            """
        ),
        codigo(
            """
            def resumo_corpus(tabela, nome):
                return pd.Series({
                    "nome": nome,
                    "numero_de_documentos": len(tabela),
                    "primeiro_ano": int(tabela["ano"].min()),
                    "ultimo_ano": int(tabela["ano"].max()),
                    "periodicos": tabela["periodico"].nunique(),
                    "generos": ", ".join(sorted(tabela["genero"].unique())),
                })

            resumo_corpus(corpus_a, "Documentos de 1890 a 1895")
            """
        ),
        texto(
            """
            ## Atividade — ficha do corpus

            Delimite um corpus inicial e responda:

            1. qual população ou universo de interesse orienta a pergunta?
            2. o conjunto disponível é amostra, corpus ou coleção de conveniência?
            3. quais são os critérios de inclusão e exclusão?
            4. quais formatos e metadados existem?
            5. que grupos, vozes ou períodos podem estar ausentes?
            6. a que conjunto uma conclusão poderá se referir?
            7. quem produziu, classificou, financiou e mantém os dados?
            """
        ),
        texto(
            """
            ### Minha ficha do corpus

            **Universo de interesse:**
            Escreva aqui.

            **O conjunto é amostra, corpus ou coleção de conveniência? Por quê?**
            Escreva aqui.

            **Unidade de análise:**
            Escreva aqui.

            **Critérios de inclusão e exclusão:**
            Escreva aqui.

            **Formatos e metadados necessários:**
            Escreva aqui.

            **Ausências e silêncios documentais:**
            Escreva aqui.

            **Alcance possível das conclusões:**
            Escreva aqui.

            **Instituições, trabalho e autoridade sobre os dados:**
            Escreva aqui.
            """
        ),
        texto(
            """
            ## Referências e leituras

            - D'IGNAZIO, Catherine; KLEIN, Lauren F. (2020). *Data Feminism*,
              capítulo “The Numbers Don't Speak for Themselves”.
            - RAWSON, Katie; MUÑOZ, Trevor (2019). “Against Cleaning”.
            - RODRIGUES, Aldair (2020). “Humanidades digitais e diáspora africana”.

            Dados completos e links: `referencias.md`.
            """
        ),
        texto(
            """
            ## Síntese

            O corpus não é um recipiente neutro. Ele materializa decisões de pesquisa
            e processos anteriores de produção, preservação e acesso. No próximo
            notebook, pergunta, operacionalização e corpus serão reunidos em uma
            proposta inicial coerente.
            """
        ),
    ]


def oficina() -> list[dict]:
    return [
        texto(
            """
            # Oficina — formulação inicial do projeto

            Este notebook produz o trabalho da Unidade 1. Edite as células Markdown
            indicadas e escreva com liberdade. O objetivo é construir uma versão
            inicial que possa ser revista à medida que novas fontes e métodos forem
            estudados.

            Não há código neste notebook: formular, justificar e interpretar são
            atividades de escrita. Os experimentos computacionais dos notebooks
            anteriores devem informar suas decisões, não substituir sua argumentação.

            Recupere os três produtos parciais. Em cada seção, registre o que foi
            mantido, o que mudou e por quê. Revisar uma decisão diante de nova evidência
            é parte do trabalho acadêmico.
            """
        ),
        texto(
            """
            ## Identificação

            **Nome:**
            Escreva aqui.

            **Título provisório:**
            Escreva aqui.

            **Fenômeno histórico, social, linguístico ou cultural:**
            Escreva aqui.

            **Contexto espacial, temporal e institucional:**
            Escreva aqui.
            """
        ),
        texto(
            """
            ## 1. Da motivação à pergunta

            Descreva por que o fenômeno importa antes de escrever uma pergunta. Depois,
            formule uma versão ampla e uma versão delimitada. Evite começar por
            “aplicar uma técnica”; o método será escolhido em função da pergunta.
            """
        ),
        texto(
            """
            ### Minha formulação

            **Motivação humanística:**
            Escreva aqui.

            **Conceito central e autores de referência:**
            Escreva aqui. Indique ao menos duas leituras pertinentes e explique o que
            cada uma contribui para definir o problema.

            **Questão ampla:**
            Escreva aqui.

            **Pergunta delimitada:**
            Escreva aqui.

            **Tipo predominante da pergunta e justificativa:**
            Escreva aqui.

            **Tarefa computacional inicial possível:**
            Escreva aqui.

            **O que mudou em relação ao produto do Notebook 01 e por quê?**
            Escreva aqui.
            """
        ),
        texto(
            """
            ## 2. Unidade, população e corpus

            Declare sobre o que serão feitas as afirmações. Em seguida, diferencie o
            universo de interesse do conjunto que poderá ser efetivamente observado.
            """
        ),
        texto(
            """
            ### Minha delimitação

            **Unidade de análise:**
            Escreva aqui.

            **Fontes possíveis:**
            Escreva aqui.

            **População ou universo de interesse:**
            Escreva aqui.

            **Amostra, corpus ou coleção efetivamente disponível:**
            Escreva aqui.

            **Recortes temporal e espacial:**
            Escreva aqui.

            **Critérios de inclusão e exclusão:**
            Escreva aqui.

            **O que mudou em relação à ficha do Notebook 03 e por quê?**
            Escreva aqui.
            """
        ),
        texto(
            """
            ## 3. Operacionalização

            Liste os conceitos essenciais. Para cada um, descreva dimensão, indicador,
            variável ou categoria, fonte da observação, regra e limitação. Inclua ao
            menos duas alternativas para o conceito central.
            """
        ),
        texto(
            """
            ### Meu mapa de operacionalização

            | Conceito | Dimensão | Indicador | Variável ou categoria | Fonte | Regra | Limitação |
            |---|---|---|---|---|---|---|
            | Conceito central | Escreva | Escreva | Escreva | Escreva | Escreva | Escreva |
            | Mesmo conceito | Alternativa | Indicador alternativo | Escreva | Escreva | Escreva | Escreva |

            **Por que uma alternativa parece mais adequada à pergunta?**
            Escreva aqui.

            **O que mudou em relação ao mapa do Notebook 02 e por quê?**
            Escreva aqui.
            """
        ),
        texto(
            """
            ## 4. Dados e metadados necessários

            Antecipe como as unidades poderão ser representadas. Diferencie conteúdo
            documental de metadados e indique a proveniência necessária para auditar
            as decisões.
            """
        ),
        texto(
            """
            ### Esquema inicial

            | Campo | Papel | Tipo esperado | Origem | Exemplo |
            |---|---|---|---|---|
            | identificador | metadado | texto | Escreva | DOC001 |
            | Escreva | documento, metadado, variável ou categoria | Escreva | Escreva | Escreva |

            Acrescente quantas linhas forem necessárias. Neste momento, a tabela é uma
            especificação; na Unidade 2 ela orientará a construção dos dados reais.
            """
        ),
        texto(
            """
            ## 5. Evidência e interpretação

            Complete a cadeia lógica:

            - se observarmos determinado padrão...
            - ele constituirá evidência de quê?
            - que leituras alternativas existem?
            - quais documentos precisarão ser relidos?
            - que conhecimento de contexto será necessário?
            """
        ),
        texto(
            """
            ### Minha cadeia de evidência

            **Operação prevista:**
            Escreva aqui.

            **Resultado possível:**
            Escreva aqui.

            **De que esse resultado poderia ser evidência?**
            Escreva aqui.

            **O que ele não demonstraria diretamente?**
            Escreva aqui.

            **Interpretações alternativas:**
            Escreva aqui.

            **Casos ou documentos que precisariam ser relidos:**
            Escreva aqui.

            **Conhecimento contextual necessário:**
            Escreva aqui.
            """
        ),
        texto(
            """
            ## 6. Limites, vieses e ética

            Considere limites em toda a cadeia: produção das fontes, preservação,
            acesso, seleção, digitalização, categorias, operações e comunicação.
            Pessoas representadas nos dados podem não ter escolhido participar da
            pesquisa. Dados públicos não são automaticamente isentos de risco.
            """
        ),
        texto(
            """
            ### Minha avaliação crítica

            | Dimensão | Risco ou limitação | Estratégia de redução ou documentação |
            |---|---|---|
            | Seleção | Escreva | Escreva |
            | Representação | Escreva | Escreva |
            | Automação | Escreva | Escreva |
            | Ética | Escreva | Escreva |
            | Interpretação | Escreva | Escreva |
            """
        ),
        texto(
            """
            ## 7. Rubrica de autoavaliação

            Atribua:

            - 0 — ausente;
            - 1 — presente, mas pouco definido;
            - 2 — definido e coerente;
            - 3 — definido, coerente e criticamente justificado.
            """
        ),
        texto(
            """
            ### Minha autoavaliação

            | Critério | Pontuação (0–3) | O que ainda precisa ser revisto |
            |---|---:|---|
            | Relevância humanística |  | Escreva |
            | Fundamentação bibliográfica |  | Escreva |
            | Delimitação da pergunta |  | Escreva |
            | Unidade de análise |  | Escreva |
            | Viabilidade dos dados |  | Escreva |
            | Operacionalização |  | Escreva |
            | Cadeia de evidência |  | Escreva |
            | Limites e ética |  | Escreva |

            **Síntese da autoavaliação:**
            Escreva aqui. A pontuação ajuda a localizar lacunas, mas não substitui a
            justificativa escrita.
            """
        ),
        texto(
            """
            ## 8. Síntese para entrega

            Escreva um parágrafo autocontido que apresente a proposta. Ele deve poder
            ser compreendido por alguém que não acompanhou suas anotações anteriores.
            """
        ),
        texto(
            """
            ### Minha entrega

            **Pergunta final da unidade:**
            Escreva aqui.

            **Resumo:**
            Pretendo investigar... A unidade de análise será... O corpus inicial
            incluirá... O conceito central será observado por... Os resultados poderão
            oferecer evidência sobre... Os principais limites são...

            **Próxima decisão necessária:**
            Escreva aqui.
            """
        ),
        texto(
            """
            ## 9. Referências utilizadas

            Liste somente obras efetivamente mobilizadas na proposta e indique onde
            cada uma fundamenta um conceito, uma escolha ou uma crítica.

            1. Escreva aqui.
            2. Escreva aqui.

            A bibliografia geral da unidade está em `referencias.md`.
            """
        ),
        texto(
            """
            ## Revisão entre pares

            Peça a uma colega ou a um colega que responda:

            1. consigo identificar exatamente o que será observado?
            2. os dados propostos podem responder à pergunta?
            3. conceito e indicador estão diferenciados?
            4. o alcance da conclusão está claro?
            5. qual escolha precisa de maior justificativa?

            Revise a formulação após receber o comentário. A pergunta resultante encerra
            a Unidade 1 e orientará a construção da base na Unidade 2.
            """
        ),
    ]


def criar_readme() -> None:
    conteudo = """\
# Unidade 1 — Questões das Humanidades e problemas computacionais

Esta pasta contém o material teórico-prático da primeira unidade da disciplina
**Computação Aplicada a Problemas em Humanidades Digitais**.

## Ordem de estudo

1. `00_guia_da_unidade.ipynb`
2. `01_perguntas_e_problemas_computacionais.ipynb`
3. `02_representacao_e_operacionalizacao.ipynb`
4. `03_dados_corpus_e_evidencias.ipynb`
5. `04_oficina_projeto_de_pesquisa.ipynb`
6. `exercicios_unidade_01.html`
7. `referencias.md`

## Dependências

- Python 3
- pandas
- JupyterLab, Jupyter Notebook ou VS Code com extensão Jupyter

Os exemplos não dependem de acesso à internet. Os dados da pasta `dados` são
fictícios e foram criados exclusivamente para fins didáticos; não devem ser
utilizados para produzir afirmações históricas.

O arquivo `exercicios_unidade_01.html` contém 18 questões de múltipla escolha
com correção, explicações e revisão por tópico. Ele pode ser aberto diretamente
em um navegador e funciona sem servidor ou acesso à internet.

## Carga e modalidade

| Modalidade | Material | Tempo |
|---|---|---:|
| Preparação | Alves (2016) e diagnóstico | 30 min |
| Aula 1 | Notebooks 00, 01 e início do 02 | 3 h 30 |
| Preparação | Rodrigues (2020) | 40 min |
| Aula 2 | Conclusão do 02, Notebook 03 e oficina | 3 h |
| Revisão assíncrona | Exercício HTML | 20 min |

As leituras complementares e extensões não integram a carga essencial.

## Material do docente

A pasta `gabaritos` contém respostas objetivas, respostas-modelo e rubricas.
Como grande parte da unidade envolve formulação e interpretação, os modelos das
atividades abertas são referências de coerência, não respostas únicas.

A pasta separa organizacionalmente o material, mas não restringe o acesso de
quem possui o repositório.

## Revisão antes da oferta

A pasta `revisores` define uma banca de revisão com seis especialidades:
nível acadêmico, didática, alinhamento, Humanidades Digitais, referências e
qualidade técnica/acessibilidade. Ela também contém matriz de avaliação e modelo
de parecer.

Os pareceres executados ficam em `revisores/pareceres`. Após alterações
acadêmicas ou didáticas, uma nova rodada deve registrar explicitamente quais
achados foram resolvidos. A Rodada 2 aprovou a unidade com ajustes. Uma
avaliação extraordinária posterior identificou ajuste alto na classificação das
perguntas; o teste manual com leitor de tela também permanece pendente.

## Execução

A partir da raiz do repositório:

```bash
python3 -m pip install -r requirements.txt
jupyter lab unidade_01
```

Também é possível abrir os arquivos individualmente no VS Code. Execute as
células na ordem. Nas atividades de escrita, entre no modo de edição das células
Markdown e substitua `Escreva aqui` por suas respostas. As células Python são
experimentos: execute-as, altere os parâmetros quando solicitado e interprete
os resultados no texto.

## Produto da unidade

O último notebook conduz à formulação inicial da pergunta de pesquisa, incluindo
unidade de análise, corpus, operacionalização, evidências esperadas e limites.
"""
    (UNIDADE / "README.md").write_text(dedent(conteudo), encoding="utf-8")


def main() -> None:
    UNIDADE.mkdir(parents=True, exist_ok=True)
    criar_dados()
    criar_readme()
    salvar_notebook("00_guia_da_unidade.ipynb", guia())
    salvar_notebook(
        "01_perguntas_e_problemas_computacionais.ipynb", perguntas()
    )
    salvar_notebook(
        "02_representacao_e_operacionalizacao.ipynb", operacionalizacao()
    )
    salvar_notebook("03_dados_corpus_e_evidencias.ipynb", corpus())
    salvar_notebook("04_oficina_projeto_de_pesquisa.ipynb", oficina())
    print(f"Notebooks, dados e README reconstruídos em: {UNIDADE}")


if __name__ == "__main__":
    main()
