"""Gera os materiais didáticos da Unidade 1 em formato Jupyter Notebook.

O script usa apenas a biblioteca padrão para que a estrutura dos notebooks
possa ser reconstruída mesmo antes da instalação do Jupyter.
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
            Quando uma célula contiver uma variável com seu nome ou sua pergunta,
            substitua o exemplo por sua resposta. Reinicie o kernel e execute tudo
            novamente antes de entregar.

            Um resultado numérico responde apenas à operação programada. Pergunte
            sempre: **que decisão tornou esse número possível, o que ele representa e
            o que ficou fora da representação?**
            """
        ),
        codigo(
            """
            # Diagnóstico: edite as respostas. Não há resposta certa.
            diagnostico = {
                "tema_de_interesse": "Ex.: memória pública e monumentos",
                "experiencia_com_python": "nenhuma / inicial / intermediária",
                "tipo_de_fonte": "Ex.: jornais, entrevistas, imagens, legislação",
                "maior_duvida": "Ex.: como transformar meu tema em dados?",
            }

            for item, resposta in diagnostico.items():
                print(f"{item}: {resposta}")
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

            ## 1. Humanidades Digitais e pesquisa orientada por dados

            Humanidades Digitais não são apenas a aplicação de ferramentas digitais
            a objetos tradicionais. Elas incluem práticas de construção de acervos,
            modelagem, análise, visualização, crítica de infraestruturas e reflexão
            sobre como tecnologias participam da produção do conhecimento.

            Uma pesquisa orientada por dados articula:

            - uma questão substantiva;
            - fontes produzidas em contextos específicos;
            - uma forma explícita de representação;
            - operações que geram resultados;
            - interpretação situada e crítica.

            Dados não são o fenômeno em estado puro. São registros selecionados,
            descritos e transformados segundo decisões humanas e institucionais.
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
        codigo(
            """
            niveis = {
                "questao_ampla": "Como ideias de progresso participaram da vida social?",
                "pergunta_delimitada": (
                    "Como o tema 'progresso' aparece em editoriais de três periódicos "
                    "da coleção didática entre 1890 e 1905?"
                ),
                "tarefa_computacional": (
                    "Selecionar editoriais, contar temas atribuídos e comparar períodos."
                ),
                "interpretacao_necessaria": (
                    "Reler os documentos e contextualizar o sentido de 'progresso'."
                ),
            }

            for nivel, formulacao in niveis.items():
                print(f"{nivel}:\\n  {formulacao}\\n")
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
        codigo(
            """
            # Uma pequena função para revisar, e não decidir automaticamente, uma pergunta.
            def checklist_pergunta(pergunta, contexto, unidade, fonte, periodo):
                itens = {
                    "pergunta preenchida": bool(pergunta.strip()),
                    "contexto informado": bool(contexto.strip()),
                    "unidade de análise indicada": bool(unidade.strip()),
                    "fonte possível indicada": bool(fonte.strip()),
                    "recorte temporal indicado": bool(periodo.strip()),
                }
                return pd.Series(itens, name="atende?")

            checklist_pergunta(
                pergunta="Como varia o tema educação entre gêneros documentais?",
                contexto="Três periódicos da coleção didática",
                unidade="Documento",
                fonte="Registros catalográficos e textos",
                periodo="1890–1905",
            )
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

            Depois, edite e execute a célula seguinte.
            """
        ),
        codigo(
            """
            minhas_classificacoes = [
                {"numero": 1, "tipo": "descritiva", "justificativa": "Caracteriza a coleção."},
                {"numero": 2, "tipo": "comparativa", "justificativa": "Compara períodos."},
                {"numero": 3, "tipo": "associativa", "justificativa": "Relaciona características."},
                {"numero": 4, "tipo": "explicativa", "justificativa": "Busca mecanismos."},
                {"numero": 5, "tipo": "preditiva", "justificativa": "Estima uma classe desconhecida."},
            ]
            pd.DataFrame(minhas_classificacoes)
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
        codigo(
            """
            meu_produto_parcial = {
                "questao_ampla": "Edite aqui",
                "pergunta_delimitada": "Edite aqui",
                "tipo_predominante": "Edite aqui",
                "tarefa_computacional": "Edite aqui",
                "o_que_fica_de_fora": "Edite aqui",
            }
            pd.Series(meu_produto_parcial, name="formulação")
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
            aponta para o conceito, mas não é idêntico a ele.
            """
        ),
        codigo(
            """
            import pandas as pd

            mapa_exemplo = pd.DataFrame([
                {
                    "conceito": "centralidade do tema educação",
                    "dimensão": "presença no documento",
                    "indicador": "tema dominante atribuído",
                    "variável": "tema",
                    "valores": "educação, trabalho, progresso",
                    "limitação": "um único tema apaga ambiguidades",
                },
                {
                    "conceito": "centralidade do tema educação",
                    "dimensão": "extensão da discussão",
                    "indicador": "número de palavras do trecho pertinente",
                    "variável": "palavras_sobre_educacao",
                    "valores": "inteiros não negativos",
                    "limitação": "extensão não equivale a importância",
                },
            ])
            mapa_exemplo
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
        codigo(
            """
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
        codigo(
            """
            classificacao_campos = pd.DataFrame([
                {"campo": "id", "papel": "identificador", "exemplo": "D001"},
                {"campo": "ano", "papel": "variável temporal", "exemplo": 1890},
                {"campo": "genero", "papel": "categoria documental", "exemplo": "editorial"},
                {"campo": "tema", "papel": "categoria analítica", "exemplo": "progresso"},
                {"campo": "texto", "papel": "conteúdo documental", "exemplo": "trecho integral"},
                {"campo": "arquivo_origem", "papel": "metadado de proveniência", "exemplo": "caixa_03.pdf"},
            ])
            classificacao_campos
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
            também exige documentação.
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
        codigo(
            """
            def avaliar_operacionalizacao(conceito, indicador, regra, fonte, limitacao):
                campos = {
                    "conceito explícito": conceito,
                    "indicador observável": indicador,
                    "regra de registro": regra,
                    "fonte da observação": fonte,
                    "limitação reconhecida": limitacao,
                }
                return pd.Series(campos, name="descrição")

            avaliar_operacionalizacao(
                conceito="presença temática",
                indicador="tema dominante anotado",
                regra="atribuir uma categoria após leitura integral",
                fonte="documento digitalizado",
                limitacao="discordâncias e temas secundários não aparecem",
            )
            """
        ),
        texto(
            """
            ## Atividade — mapa de operacionalização

            Escolha um conceito central de sua pergunta. Proponha ao menos duas
            operacionalizações. Compare o que cada uma permite observar e o que perde.
            """
        ),
        codigo(
            """
            meu_mapa = pd.DataFrame([
                {
                    "conceito": "Edite aqui",
                    "dimensão": "Edite aqui",
                    "indicador": "Edite aqui",
                    "unidade_de_analise": "Edite aqui",
                    "variavel": "Edite aqui",
                    "valores_ou_categorias": "Edite aqui",
                    "fonte": "Edite aqui",
                    "regra": "Edite aqui",
                    "limitacao": "Edite aqui",
                },
                {
                    "conceito": "Mesmo conceito",
                    "dimensão": "Outra dimensão",
                    "indicador": "Indicador alternativo",
                    "unidade_de_analise": "Edite aqui",
                    "variavel": "Edite aqui",
                    "valores_ou_categorias": "Edite aqui",
                    "fonte": "Edite aqui",
                    "regra": "Edite aqui",
                    "limitacao": "Edite aqui",
                },
            ])
            meu_mapa
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
            Ainda assim, não falam sozinhos.
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
            """
        ),
        codigo(
            """
            minha_ficha = pd.Series({
                "universo_de_interesse": "Edite aqui",
                "tipo_do_conjunto": "amostra / corpus / coleção de conveniência",
                "unidade_de_analise": "Edite aqui",
                "criterios_de_inclusao": "Edite aqui",
                "criterios_de_exclusao": "Edite aqui",
                "formatos": "Edite aqui",
                "metadados_necessarios": "Edite aqui",
                "ausencias_e_silencios": "Edite aqui",
                "alcance_da_conclusao": "Edite aqui",
            }, name="ficha do corpus")
            minha_ficha
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

            Este notebook produz o trabalho da Unidade 1. Substitua os exemplos por
            suas respostas. O objetivo é construir uma versão inicial que possa ser
            revista à medida que novas fontes e métodos forem estudados.
            """
        ),
        codigo(
            """
            import pandas as pd

            projeto = {
                "nome": "Seu nome",
                "titulo_provisorio": "Título provisório do projeto",
                "fenomeno": "Fenômeno histórico, social, linguístico ou cultural",
                "contexto": "Contexto espacial, temporal e institucional",
            }
            pd.Series(projeto, name="identificação")
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
        codigo(
            """
            formulacao = {
                "motivacao_humanistica": "Edite aqui",
                "questao_ampla": "Edite aqui",
                "pergunta_delimitada": "Edite aqui",
                "tipo_predominante": (
                    "descritiva / comparativa / associativa / explicativa / preditiva"
                ),
                "justificativa_do_tipo": "Edite aqui",
                "tarefa_computacional_inicial": "Edite aqui",
            }
            pd.Series(formulacao, name="pergunta")
            """
        ),
        texto(
            """
            ## 2. Unidade, população e corpus

            Declare sobre o que serão feitas as afirmações. Em seguida, diferencie o
            universo de interesse do conjunto que poderá ser efetivamente observado.
            """
        ),
        codigo(
            """
            delimitacao = {
                "unidade_de_analise": "Edite aqui",
                "fonte": "Edite aqui",
                "populacao_ou_universo": "Edite aqui",
                "amostra_ou_corpus": "Edite aqui",
                "recorte_temporal": "Edite aqui",
                "recorte_espacial": "Edite aqui",
                "criterios_de_inclusao": "Edite aqui",
                "criterios_de_exclusao": "Edite aqui",
            }
            pd.Series(delimitacao, name="delimitação")
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
        codigo(
            """
            operacionalizacao = pd.DataFrame([
                {
                    "conceito": "Conceito central",
                    "dimensao": "Edite aqui",
                    "indicador": "Edite aqui",
                    "variavel_ou_categoria": "Edite aqui",
                    "fonte": "Edite aqui",
                    "regra": "Edite aqui",
                    "limitacao": "Edite aqui",
                },
                {
                    "conceito": "Conceito central",
                    "dimensao": "Alternativa",
                    "indicador": "Indicador alternativo",
                    "variavel_ou_categoria": "Edite aqui",
                    "fonte": "Edite aqui",
                    "regra": "Edite aqui",
                    "limitacao": "Edite aqui",
                },
            ])
            operacionalizacao
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
        codigo(
            """
            esquema_inicial = pd.DataFrame([
                {
                    "campo": "identificador",
                    "papel": "metadado",
                    "tipo": "texto",
                    "origem": "Edite aqui",
                    "exemplo": "DOC001",
                },
                {
                    "campo": "Edite aqui",
                    "papel": "documento / metadado / variável / categoria",
                    "tipo": "texto / número / data / booleano",
                    "origem": "Edite aqui",
                    "exemplo": "Edite aqui",
                },
            ])
            esquema_inicial
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
        codigo(
            """
            cadeia_de_evidencia = {
                "operacao_prevista": "Ex.: comparar frequências entre períodos",
                "resultado_possivel": "Ex.: aumento de uma categoria",
                "evidencia_para": "Edite aqui",
                "nao_evidencia_diretamente": "Edite aqui",
                "interpretacoes_alternativas": "Edite aqui",
                "retorno_qualitativo": "Documentos ou casos que deverão ser relidos",
                "contexto_necessario": "Edite aqui",
            }
            pd.Series(cadeia_de_evidencia, name="cadeia de evidência")
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
        codigo(
            """
            avaliacao_critica = pd.DataFrame([
                {"dimensao": "seleção", "risco": "Edite aqui", "estrategia": "Edite aqui"},
                {"dimensao": "representação", "risco": "Edite aqui", "estrategia": "Edite aqui"},
                {"dimensao": "automação", "risco": "Edite aqui", "estrategia": "Edite aqui"},
                {"dimensao": "ética", "risco": "Edite aqui", "estrategia": "Edite aqui"},
                {"dimensao": "interpretação", "risco": "Edite aqui", "estrategia": "Edite aqui"},
            ])
            avaliacao_critica
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
        codigo(
            """
            rubrica = pd.DataFrame([
                {"criterio": "relevância humanística", "pontuacao": 0, "comentario": "Edite"},
                {"criterio": "delimitação da pergunta", "pontuacao": 0, "comentario": "Edite"},
                {"criterio": "unidade de análise", "pontuacao": 0, "comentario": "Edite"},
                {"criterio": "viabilidade dos dados", "pontuacao": 0, "comentario": "Edite"},
                {"criterio": "operacionalização", "pontuacao": 0, "comentario": "Edite"},
                {"criterio": "cadeia de evidência", "pontuacao": 0, "comentario": "Edite"},
                {"criterio": "limites e ética", "pontuacao": 0, "comentario": "Edite"},
            ])

            total = int(rubrica["pontuacao"].sum())
            maximo = len(rubrica) * 3
            print(f"Pontuação de autoavaliação: {total}/{maximo}")
            rubrica
            """
        ),
        texto(
            """
            ## 8. Síntese para entrega

            Escreva um parágrafo autocontido que apresente a proposta. Ele deve poder
            ser compreendido por alguém que não acompanhou suas anotações anteriores.
            """
        ),
        codigo(
            """
            sintese = {
                "pergunta_final_da_unidade": "Edite aqui",
                "resumo": (
                    "Pretendo investigar... A unidade de análise será... O corpus "
                    "inicial incluirá... O conceito central será observado por... "
                    "Os resultados poderão oferecer evidência sobre... Os principais "
                    "limites são..."
                ),
                "proxima_decisao_necessaria": "Edite aqui",
            }
            pd.Series(sintese, name="entrega")
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

## Dependências

- Python 3
- pandas
- JupyterLab, Jupyter Notebook ou VS Code com extensão Jupyter

Os exemplos não dependem de acesso à internet. Os dados da pasta `dados` são
fictícios e foram criados exclusivamente para fins didáticos; não devem ser
utilizados para produzir afirmações históricas.

## Execução

A partir da raiz do repositório:

```bash
python3 -m pip install -r requirements.txt
jupyter lab unidade_01
```

Também é possível abrir os arquivos individualmente no VS Code. Execute as
células na ordem. As atividades possuem valores como `Edite aqui`; substitua-os
pelas respostas do projeto.

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
    print(f"Unidade criada em: {UNIDADE}")


if __name__ == "__main__":
    main()
