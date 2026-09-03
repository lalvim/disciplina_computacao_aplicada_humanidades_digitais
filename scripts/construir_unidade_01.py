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

from apoio_colab import adicionar_link_na_abertura, preparacao_colab, tabela_links_colab


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
    for indice, celula in enumerate(celulas, start=1):
        celula.setdefault("id", f"celula-{indice:03d}")
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


def salvar_notebook(
    nome: str,
    celulas: list[dict],
    requer_repositorio: bool = False,
) -> None:
    publicadas = [adicionar_link_na_abertura(celulas[0], UNIDADE.name, nome)]
    if requer_repositorio:
        publicadas.append(codigo(preparacao_colab(UNIDADE.name)))
    publicadas.extend(celulas[1:])
    caminho = UNIDADE / nome
    caminho.write_text(
        json.dumps(notebook(publicadas), ensure_ascii=False, indent=1) + "\n",
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

            ![Ilustração conceitual em que fontes em papel passam por anotação e organização tabular, produzem redes e gráficos e retornam às fontes por uma seta de revisão.](imagens/00_abertura_conceitual.png)

            *Ilustração conceitual gerada para a unidade; não representa uma fonte
            histórica. A seta de retorno destaca que resultados levam à releitura e à
            revisão das decisões.*

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

            1. distinguir a finalidade e a estrutura analítica de uma pergunta;
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
            | 01 | Com que finalidade e estrutura perguntamos? | Pergunta reformulada |
            | 02 | Como representar conceitos e observações? | Mapa de operacionalização |
            | 03 | Que conjunto de dados sustenta a análise? | Ficha do corpus |
            | 04 | O projeto é coerente e viável? | Formulação inicial do projeto |

            ![Fluxo dos Notebooks 00 a 04: diagnóstico, pergunta reformulada, mapa de operacionalização, ficha do corpus e proposta inicial.](imagens/00_percurso_unidade.svg)

            *Cada notebook produz uma decisão ou um produto que alimenta o seguinte;
            as escolhas podem ser revistas ao longo do percurso.*

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

            - ALVES, Daniel (2016), “As Humanidades Digitais como uma comunidade de
              práticas dentro do formalismo académico: dos exemplos internacionais
              ao caso português”, especialmente a introdução.
            - RODRIGUES, Aldair (2020), “Humanidades digitais e diáspora africana:
              questões éticas e metodológicas na elaboração de uma base de dados
              sobre a população escravizada de Mariana (século XVIII)”, como estudo
              de caso para a segunda aula.

            As referências completas e os links estão em `referencias.md`.
            """
        ),
        texto(
            """
            ## Produto final da unidade e critérios de avaliação

            Ao final da unidade, cada estudante apresentará uma **proposta inicial de
            pesquisa orientada por dados**, consolidada no Notebook 04. Não se espera
            um artigo pronto, resultados definitivos ou um programa completo. O
            produto é um esboço argumentado que mostra como uma questão das
            Humanidades poderia ser investigada com apoio de dados e métodos
            computacionais.

            A proposta será construída progressivamente. Os Notebooks 01, 02 e 03
            geram produtos parciais sobre a pergunta, a representação do fenômeno e a
            composição do corpus. No Notebook 04, o estudante revisará e reunirá essas
            decisões em uma formulação coerente.

            O produto final deverá explicitar:

            - o fenômeno humanístico e seu contexto;
            - uma pergunta de pesquisa delimitada, sua finalidade e sua estrutura;
            - o recorte, a unidade de análise e as fontes ou o corpus possíveis;
            - como aspectos do fenômeno poderiam ser representados como dados;
            - quais operações computacionais poderiam produzir evidências pertinentes;
            - como essas evidências seriam interpretadas à luz do contexto e da
              bibliografia;
            - limitações, vieses e questões éticas da proposta.

            A avaliação não premiará a pergunta mais ambiciosa nem a maior quantidade
            de código. Ela considerará principalmente:

            1. **relevância humanística:** a proposta trata de um problema significativo
               para a área;
            2. **delimitação:** pergunta, contexto e recorte estão claramente definidos;
            3. **coerência:** fontes, unidade de análise, representação, operações e
               evidências são compatíveis com a pergunta;
            4. **fundamentação:** as decisões dialogam com conceitos e referências da
               unidade;
            5. **reflexividade:** limites, escolhas interpretativas, vieses e questões
               éticas são reconhecidos;
            6. **viabilidade:** a proposta pode ser investigada com os dados, o tempo e
               os recursos considerados.

            Uma pergunta modesta, bem delimitada e criticamente justificada é
            preferível a uma pergunta grandiosa que as fontes e os métodos não podem
            sustentar. A proposta poderá mudar nas unidades seguintes: revisar escolhas
            diante de novas evidências faz parte da pesquisa.
            """
        ),
        texto(
            """
            ## Atividade individual — diagnóstico inicial

            **Modalidade:** individual. **Tempo sugerido:** 10 minutos.

            Esta é a única atividade do guia. Responda diretamente nesta célula
            Markdown antes de iniciar o Notebook 01. Não há respostas certas nem
            necessidade de formular uma pergunta de pesquisa neste momento. O
            registro permitirá ao professor conhecer os interesses, as experiências e
            as dúvidas iniciais da turma.

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

            - **uma questão substantiva:** por exemplo, “como o tema do progresso
              aparece em diferentes gêneros de três periódicos entre 1890 e 1905?”;
            - **fontes produzidas em contextos específicos:** por exemplo, editoriais,
              notícias e cartas, considerando quem os escreveu, para qual público,
              sob quais convenções jornalísticas e por que foram preservados;
            - **uma forma explícita de representação:** por exemplo, registrar cada
              documento em uma linha com ano, periódico, gênero, local e tema. A
              categoria `tema` resulta de uma regra de anotação e não existe pronta no
              documento;
            - **operações que geram resultados:** por exemplo, selecionar o período,
              agrupar documentos por gênero, contar ocorrências da categoria
              “progresso” e localizar os registros que produziram cada contagem;
            - **interpretação situada e crítica:** por exemplo, tratar uma diferença
              entre gêneros como pista para releitura dos textos, considerando a
              cobertura da coleção, as categorias adotadas e as vozes ausentes, sem
              generalizar automaticamente para toda a imprensa do período.

            Os cinco exemplos formam uma única cadeia. Alterar a pergunta, excluir uma
            fonte, redefinir o tema ou escolher outra operação pode modificar o
            resultado e, portanto, a interpretação possível.

            Dados não são o fenômeno em estado puro. Drucker (2011) propõe o termo
            *capta* para enfatizar que registros são tomados e construídos. Lavin
            (2021) concorda com a crítica à neutralidade, mas defende “dados situados”
            em vez de abandonar o termo *data*. A divergência é produtiva: ambos
            exigem que seleção, descrição e transformação sejam explicitadas.
            """
        ),
        texto(
            """
            ## 2. Duas dimensões combináveis da pergunta

            Para evitar misturar categorias de níveis diferentes, a disciplina adota
            uma organização didática em duas dimensões. Ela não pretende ser uma
            taxonomia universal.

            **Finalidade predominante**

            - **Descritiva:** caracteriza ocorrências, distribuições ou padrões.
            - **Explicativa:** investiga mecanismos e condições relacionados a um
              resultado, com teoria e cautela causal.
            - **Preditiva:** estima um resultado desconhecido em novos casos.

            **Estrutura analítica inicial**

            - **Sem relação inicial:** caracteriza um conjunto sem confronto explícito.
            - **Comparativa:** confronta grupos, períodos, documentos ou contextos.
            - **Associativa:** examina como características variam em conjunto.

            As dimensões podem ser combinadas. “Os temas diferem entre Capital e
            Interior?” tem finalidade descritiva e estrutura comparativa. Comparações
            e associações também podem integrar uma investigação explicativa, mas não
            demonstram causalidade por si sós. A distinção entre explicar e prever é
            discutida por Shmueli (2010).

            ![Matriz com finalidades descritiva, explicativa e preditiva nas linhas e estruturas sem relação inicial, comparativa e associativa nas colunas.](imagens/01_matriz_perguntas.svg)

            *Leia a finalidade e a estrutura como dimensões diferentes. A posição na
            matriz não transforma comparação ou associação em explicação causal.*
            """
        ),
        texto(
            """
            | Pergunta | Finalidade | Estrutura | Operação inicial |
            |---|---|---|---|
            | Quais temas aparecem nos documentos? | Descritiva | Sem relação inicial | Contar ocorrências por tema |
            | Os temas diferem entre Capital e Interior? | Descritiva | Comparativa | Comparar distribuições |
            | Gênero documental e tema variam juntos? | Descritiva | Associativa | Cruzar categorias |
            | Que processos explicam a mudança do debate? | Explicativa | Comparativa e associativa | Formular e confrontar explicações |
            | É possível estimar o gênero pelos metadados? | Preditiva | Associativa | Treinar e avaliar uma previsão |
            """
        ),
        texto(
            """
            ## 3. Da questão humanística à tarefa computacional

            Uma pesquisa orientada por dados articula quatro níveis. Observe o mesmo
            exemplo em todo o percurso:

            | Nível | Função | Exemplo |
            |---|---|---|
            | Questão humanística ampla | Define o problema substantivo | Como ideias de progresso participaram da vida social? |
            | Pergunta delimitada | Estabelece fenômeno, contexto, fontes e recorte | Como o tema “progresso” aparece em editoriais de três periódicos da coleção didática entre 1890 e 1905? |
            | Tarefa computacional | Indica as operações que produzirão resultados | Selecionar editoriais, contar temas atribuídos e comparar períodos |
            | Interpretação humanística | Relaciona os resultados aos documentos, ao contexto e à bibliografia | Reler os documentos selecionados e contextualizar os diferentes sentidos de “progresso” |

            ![Quatro blocos conectam questão humanística ampla, pergunta delimitada, tarefa computacional e interpretação, com uma seta de retorno para releitura.](imagens/01_questao_tarefa_interpretacao.svg)

            *O fluxo possui retorno: resultados e releituras podem levar à revisão da
            pergunta, do recorte ou da representação.*

            Apenas a tarefa computacional descreve uma operação. Ela não substitui a
            pergunta, e seu resultado não substitui a interpretação. Uma contagem pode
            indicar um padrão; compreender seu sentido demanda retornar aos documentos,
            às condições de produção, às categorias adotadas e à historiografia
            pertinente.
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
            ### Atividade individual — checklist de revisão

            **Tempo sugerido:** 5 minutos. **Produto:** pergunta anotada com os itens
            que ainda exigem revisão.

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

            **Modalidade:** trios. **Tempo sugerido:** 15 minutos de trabalho e 10
            minutos de correção dialogada. **Produto:** cinco classificações com
            justificativas registradas na célula seguinte.

            Primeiro, cada integrante classifica ao menos uma pergunta. Depois, o trio
            compara as respostas e negocia uma versão conjunta. Divergências bem
            justificadas devem ser preservadas para a plenária.

            Para cada pergunta abaixo, indique separadamente a finalidade predominante
            e a estrutura analítica inicial. Justifique ambas:

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

            1. **Finalidade e estrutura:** Escreva aqui.
               **Justificativa:** Escreva aqui.
            2. **Finalidade e estrutura:** Escreva aqui.
               **Justificativa:** Escreva aqui.
            3. **Finalidade e estrutura:** Escreva aqui.
               **Justificativa:** Escreva aqui.
            4. **Finalidade e estrutura:** Escreva aqui.
               **Justificativa:** Escreva aqui.
            5. **Finalidade e estrutura:** Escreva aqui.
               **Justificativa:** Escreva aqui.
            """
        ),
        texto(
            """
            ### Atividade em trio e plenária — casos limítrofes

            **Tempo sugerido:** 10 minutos no trio e 5 minutos em plenária.
            **Produto:** classificação argumentada e uma reformulação preditiva.

            Uma investigação pode ter etapas de tipos diferentes. Considere:

            > Quais mudanças no vocabulário distinguem dois períodos e que processos
            > históricos ajudam a explicá-las?

            A estrutura comparativa produz o padrão inicial; a finalidade explicativa
            exige teoria, contexto e confronto de mecanismos. Indique a finalidade e
            as estruturas presentes, as etapas secundárias e como a pergunta mudaria
            se a finalidade fosse prever o período de um documento.
            """
        ),
        texto(
            """
            ## Atividade em dupla — compreender e delimitar o interesse do colega

            **Modalidade:** duplas. **Tempo sugerido:** 10 minutos.
            **Produto:** comentários do colega que serão usados na formulação
            individual da pergunta.

            Retome o tema e as fontes registrados no diagnóstico do Notebook 00.
            Prepare uma apresentação breve completando oralmente:

            > Quero compreender __________ no contexto __________, observando
            > inicialmente __________.

            Cada participante terá até dois minutos para apresentar sua ideia. O
            colega deverá ouvi-la usando os conceitos estudados neste notebook e
            identificar:

            1. **fenômeno de interesse:** o que está sendo investigado;
            2. **contexto e recorte:** onde, quando ou em que conjunto a investigação
               se situa;
            3. **fonte possível:** que documento ou registro poderia fornecer
               evidências;
            4. **ponto ainda amplo ou ambíguo:** o que precisa ser delimitado;
            5. **promessa excessiva:** o que talvez não possa ser sustentado pelas
               fontes ou por uma operação computacional.

            Não formule a pergunta pelo colega nem escolha uma técnica em seu lugar.
            Faça perguntas e ofereça comentários que o ajudem a justificar suas
            próprias decisões.

            ### Anotações da revisão em dupla

            **Como o colega compreendeu meu fenômeno e meu contexto:**
            Escreva aqui.

            **Fonte considerada plausível e justificativa:**
            Escreva aqui.

            **Ponto ainda amplo, ambíguo ou excessivo:**
            Escreva aqui.

            **Mudança que pretendo considerar na formulação individual:**
            Escreva aqui.
            """
        ),
        texto(
            """
            ## Atividade autônoma — produto parcial

            **Modalidade:** individual. **Tempo sugerido:** 15 minutos.
            **Produto:** primeira formulação documentada de sua pergunta, preenchida
            na célula seguinte.

            Use o diagnóstico inicial e os comentários recebidos na dupla como ponto
            de partida. Você não é obrigado a aceitar todas as sugestões: registre
            escolhas que consiga justificar.

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

            **Finalidade predominante e justificativa:**
            Escreva aqui.

            **Estrutura analítica inicial e justificativa:**
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
              práticas dentro do formalismo académico: dos exemplos internacionais
              ao caso português”.
            - BURDICK, Anne et al. (2012). *Digital_Humanities*.
            - DRUCKER, Johanna (2011). “Humanities Approaches to Graphical Display”.
            - LAVIN, Matthew (2021). “Why Digital Humanists Should Emphasize Situated
              Data over Capta”.
            - FERLA, Luis A.; LIMA, Luís F.; FEITLER, Bruno (2020).
              “Novidades no front”.
            - SHMUELI, Galit (2010). “To Explain or to Predict?”.
            - DREW, Clifford J.; HARDMAN, Michael L.; HOSP, John L. (2008).
              *Designing and Conducting Research in Education*, cap. 2.

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

            ## Mapa do percurso

            Este notebook responde à pergunta: **como transformar um conceito da
            pesquisa em registros analisáveis sem confundir a representação com o
            fenômeno?** O percurso será:

            > pergunta → conceito e dimensão → indicador → unidade de análise →
            > variáveis, valores, documentos e metadados → categorias históricas e
            > analíticas → comparação de representações → validade da representação → mapa de
            > operacionalização

            | Etapa | Pergunta orientadora | Para que serve |
            |---|---|---|
            | Conceito e dimensão | O que a expressão central da pergunta significa e qual aspecto será examinado? | Delimitar teoricamente o fenômeno |
            | Indicador | Que traço observável pode apontar para esse aspecto? | Construir a ponte entre conceito e fonte |
            | Unidade de análise | Sobre que entidade serão feitas as afirmações? | Definir o que constitui um caso da pesquisa |
            | Variáveis, valores, documentos e metadados | Como cada unidade e cada observação serão registradas e contextualizadas? | Construir um esquema de dados rastreável |
            | Categorias históricas e analíticas | Quem classificou, em que contexto e segundo qual regra? | Evitar naturalizar ou apagar classificações |
            | Comparação de representações | O que muda quando o mesmo material é modelado de outra maneira? | Tornar visíveis perdas e consequências das escolhas |
            | Validade da representação | A representação é adequada, consistente, abrangente e rastreável? | Examinar se os dados podem sustentar a interpretação |
            | Mapa de operacionalização | Como documentar toda a cadeia e suas limitações? | Produzir o resultado parcial do notebook |

            ![Ciclo de oito etapas: conceito e dimensão, indicador, unidade de análise, registro, categorias, comparação, validade e mapa de operacionalização, com retorno ao início.](imagens/02_ciclo_operacionalizacao.svg)

            *A seta de retorno mostra que o mapa não é uma sequência irreversível:
            perdas ou incompatibilidades exigem revisar decisões anteriores.*

            As etapas formam um ciclo, não uma sequência irreversível. Ao descobrir
            uma perda ou incompatibilidade, retorne às decisões anteriores e revise-as.

            **Nota de fundamentação:** este percurso de oito etapas é uma **síntese
            didática elaborada para a unidade**, e não uma taxonomia reproduzida de
            uma única obra. Ele articula a discussão de conceituação e
            operacionalização de Babbie (2021), a relação entre conceitos,
            indicadores e validade de Adcock e Collier (2001), a explicitação de
            unidades e procedimentos de codificação de Krippendorff (2019) e os
            debates das Humanidades Digitais sobre representação, classificação,
            contexto e poder. As referências específicas aparecem junto a cada
            etapa e ao final do notebook.

            ## Retomada

            1. Qual foi a pergunta delimitada no Notebook 01?
            2. Que palavra ou expressão dessa pergunta ainda precisa ser definida?

            ## 1. Conceito e dimensão

            Conceitos como modernização, identidade, prestígio, violência ou
            participação política não aparecem prontos em uma planilha. Para analisá-los,
            começamos distinguindo:

            - **conceito teórico:** ideia que orienta a investigação;
            - **dimensão:** aspecto particular do conceito que será examinado.

            Um conceito pode possuir várias dimensões. “Centralidade”, por exemplo,
            pode envolver presença, extensão, posição em uma rede ou destaque na
            organização de um documento. Escolher uma dimensão delimita o aspecto que
            a pesquisa observará, mas ainda não define como ele será reconhecido nas
            fontes.

            A próxima etapa constrói essa ponte por meio de um indicador. A distinção
            entre conceito, dimensões e modos de operacionalização acompanha a
            discussão metodológica de Babbie (2021, cap. 5); o encadeamento particular
            usado aqui foi adaptado às necessidades de uma pesquisa em Humanidades
            Digitais.
            """
        ),
        texto(
            """
            ### Possibilidades de dimensão para o conceito do exemplo

            Para estudar a **centralidade do tema educação**, o pesquisador pode
            delimitar diferentes aspectos do conceito. A tabela funciona como um
            repertório para orientar a escolha, não como uma lista que precise ser
            aplicada integralmente.

            | Dimensão possível | Pergunta que orienta a observação | Exemplo de indicador |
            |---|---|---|
            | Presença | O tema aparece no documento? | presença ou ausência do tema |
            | Extensão | Quanto espaço do documento é dedicado ao tema? | proporção de palavras ou parágrafos pertinentes |
            | Frequência | Quantas vezes o tema é mencionado? | número de ocorrências segundo uma regra explícita |
            | Posição | Em que parte do documento o tema aparece? | título, abertura, corpo ou conclusão |
            | Destaque editorial | Que visibilidade formal o tema recebe? | manchete, primeira página, seção ou tamanho do texto |
            | Recorrência temporal | Com que regularidade o tema aparece na coleção? | número ou proporção de edições com o tema por período |
            | Intensidade | Com que ênfase o tema é tratado? | escala definida por critérios linguísticos ou discursivos |
            | Enquadramento | De que maneira o tema é apresentado? | direito, progresso, disciplina, custo ou outra categoria justificada |
            | Valência | Que avaliação é associada ao tema? | favorável, contrária, ambivalente ou não classificável |
            | Associação | Com quais temas ele aparece? | coocorrência com trabalho, cidadania ou progresso |
            | Diversidade de atores | Quantos grupos participam da discussão? | número e tipos de atores mencionados ou citados |
            | Protagonismo | Quem recebe voz ou capacidade de agir? | fala direta, autoria ou posição do ator na narrativa |

            ![O conceito centralidade do tema educação se ramifica em presença, extensão, posição, enquadramento e protagonismo, cada qual associado a um indicador possível.](imagens/02_conceito_dimensoes.svg)

            *O diagrama apresenta apenas cinco exemplos para tornar visível a
            ramificação. A tabela mantém o repertório mais amplo de dimensões.*

            As dimensões não são universais nem intercambiáveis. “Extensão”, por
            exemplo, mede o espaço ocupado pela discussão, mas não demonstra por si
            só sua importância histórica. O estudante deve escolher a dimensão que
            melhor corresponda à pergunta. A última coluna apenas antecipa exemplos
            de **indicadores**, que serão definidos formalmente na seção seguinte.
            """
        ),
        texto(
            """
            ## 2. Indicador

            Um **indicador** é um traço observável escolhido como evidência de uma
            dimensão do conceito. Ele pode ser uma presença, contagem, proporção,
            relação, posição, característica textual ou classificação produzida por
            uma regra explícita.

            O indicador aponta para o conceito, mas não é idêntico a ele. Contar
            palavras relacionadas à educação, por exemplo, pode indicar extensão da
            discussão, mas não mede automaticamente importância histórica. Escolher um
            indicador exige justificar por que ele é pertinente, indicar suas perdas e
            reconhecer interpretações que ele não sustenta.

            **Operacionalizar** começa por construir e justificar a relação entre
            conceito, dimensão e indicador. Nas etapas seguintes, será necessário
            definir sobre que unidade o indicador será observado e como será registrado.
            Babbie (2021, cap. 5) oferece a base para essa passagem metodológica, e
            Adcock e Collier (2001) mostram por que a relação entre conceitos e
            indicadores precisa ser avaliada quanto à validade. A crítica de Drucker
            (2011) acrescenta que a representação não apenas descreve o objeto: ela
            produz uma forma particular de torná-lo observável.
            """
        ),
        texto(
            """
            ### Exemplo — do conceito e da dimensão ao indicador

            | Conceito | Dimensão | Indicador | Limitação inicial |
            |---|---|---|---|
            | Centralidade do tema educação | Presença no documento | Tema dominante atribuído | Um único tema apaga ambiguidades |
            | Centralidade do tema educação | Extensão da discussão | Palavras no trecho pertinente | Extensão não equivale a importância |

            Este primeiro passo ainda não define unidade, variável, valores, fonte ou
            regra. Ele serve apenas para comparar duas pontes possíveis entre conceito
            e observação. O mapa completo será construído ao final do notebook. A
            tabela não precisa ser criada em Python, pois ainda não contém observações
            a serem processadas.
            """
        ),
        texto(
            """
            ## 3. Unidade de análise

            A unidade de análise é a entidade sobre a qual fazemos afirmações: pessoa,
            documento, parágrafo, evento, instituição, município, imagem ou relação.

            Ela não deve ser confundida com:

            - **fonte:** material do qual extraímos informação;
            - **unidade de observação:** onde uma medida é efetivamente registrada;
            - **nível de agregação:** escala em que resumimos resultados.

            Um jornal pode ser a fonte, cada artigo a unidade de análise e cada parágrafo
            a unidade de observação. Trocar de unidade altera o significado das medidas.
            Krippendorff (2019, cap. 5) mostra que a definição das unidades e das
            funções que elas exercem é uma decisão metodológica indispensável na
            análise de conteúdo; os termos acima foram organizados aqui para tornar
            explícita a cadeia de inferência deste curso.
            """
        ),
        texto(
            """
            ### Exemplo de estrutura tabular

            | `id` | `ano` | `genero` | `tema` |
            |---|---:|---|---|
            | D001 | 1890 | editorial | progresso |
            | D002 | 1891 | carta | trabalho |
            | D003 | 1892 | notícia | educação |

            **Neste modelo**, cada linha representa um documento e, portanto, há três
            unidades de análise registradas. Isso não decorre naturalmente do formato
            de tabela: é uma decisão de modelagem. Se cada linha representasse um
            parágrafo, uma pessoa citada ou uma ocorrência temática, contar linhas não
            equivaleria a contar documentos.

            Antes de continuar, pergunte: o que cada linha representa, sobre qual
            entidade a pesquisa fará afirmações e qual identificador permite distinguir
            uma unidade da outra?
            """
        ),
        texto(
            """
            ## 4. Variáveis, valores, documentos e metadados

            Em uma tabela, linhas frequentemente representam unidades e colunas
            representam variáveis. Uma **variável** é um campo que registra uma
            característica da unidade; uma **categoria ou valor** é uma forma que esse
            campo pode assumir. Por exemplo, `genero` é a variável e `editorial` é uma
            de suas categorias; `ano` é a variável e `1890` é um valor observado.

            Um **identificador** distingue cada unidade, mas não descreve uma
            característica substantiva. O campo `id`, por exemplo, permite relacionar
            tabelas e reencontrar o documento sem ser uma categoria analítica.

            Um **documento** é um objeto de pesquisa, não apenas uma sequência de
            caracteres. Seu suporte, autoria, circulação, gênero e proveniência
            participam da interpretação.

            **Metadados** são dados que descrevem, identificam, contextualizam ou
            administram outros dados e documentos. Eles podem ser parte da própria
            análise — por exemplo, data, autoria, local e gênero documental.

            Krippendorff (2019, caps. 7–8) fundamenta a necessidade de explicitar
            regras de registro, codificação e variáveis. Para a distinção entre dados
            e metadados e para as funções descritiva, administrativa, estrutural e de
            preservação dos metadados, consulte Riley (2017). A tabela é apenas uma
            forma possível de implementar essas decisões.
            """
        ),
        texto(
            """
            ### Exemplos de campos, valores e papéis

            | Campo ou variável | Papel | Categoria ou valor de exemplo |
            |---|---|---|
            | `id` | Identificador | D001 |
            | `ano` | Variável temporal | 1890 |
            | `genero` | Variável documental categórica | editorial |
            | `tema` | Variável analítica categórica | progresso |
            | `texto` | Conteúdo documental | trecho integral |
            | `arquivo_origem` | Metadado de proveniência | caixa_03.pdf |

            A tabela documenta o esquema. O código passa a ser relevante quando há
            registros concretos a inspecionar, transformar ou comparar.
            """
        ),
        texto(
            """
            ## 5. Categorias históricas e analíticas

            Categorizar significa produzir equivalências e diferenças. Antes de usar
            uma categoria, pergunte:

            1. ela vem da fonte, de uma instituição ou do pesquisador?
            2. as definições são explícitas?
            3. casos ambíguos podem ser registrados?
            4. as categorias mudaram historicamente?
            5. quem ou o que se torna invisível?

            ### O que são categorias históricas?

            **Categorias históricas** são termos e sistemas de classificação cujo
            significado e uso pertencem a um contexto específico. Elas podem ter sido
            empregadas pelos próprios atores, atribuídas por instituições — como
            Estado, Igreja, polícia, imprensa ou arquivo — ou produzidas posteriormente
            por pesquisadores. Não são apenas categorias “antigas”: são classificações
            situadas no tempo, ligadas a práticas, disputas e relações de poder.

            É útil distinguir três níveis:

            | Nível | Quem classifica? | Exemplo | Questão crítica |
            |---|---|---|---|
            | Categoria presente na fonte | pessoa que fala ou escreve | alguém se identifica como “operário” | o termo expressa autodefinição, estratégia ou convenção do gênero documental? |
            | Categoria institucional | agente ou instituição que produz o registro | condição registrada como “livre”, “liberto” ou “escravizado” | quais regras jurídicas e administrativas produziram a classificação? |
            | Categoria analítica | pesquisador ou equipe do projeto | agrupar ocupações em setores econômicos | que diferenças históricas o agrupamento preserva ou apaga? |

            Uma mesma palavra pode mudar de sentido entre períodos e lugares. Termos
            diferentes também não devem ser tratados automaticamente como sinônimos.
            Designações de cor, condição jurídica, ocupação, gênero, origem ou
            pertencimento social podem ter sido impostas, negociadas, omitidas ou
            registradas de maneira inconsistente. Algumas expressam hierarquias e
            violências do contexto que as produziu.

            Em uma base de dados, portanto, não convém substituir silenciosamente o
            termo da fonte por uma categoria atual. Uma modelagem rastreável pode
            manter campos separados:

            | Campo | O que registra |
            |---|---|
            | `termo_na_fonte` | transcrição da classificação encontrada no documento |
            | `categoria_analitica` | agrupamento criado para responder à pergunta atual |
            | `agente_classificador` | quem atribuiu a classificação, quando isso for identificável |
            | `regra_de_correspondencia` | justificativa para relacionar o termo histórico à categoria analítica |
            | `incerteza` | dúvida, ambiguidade, conflito ou ausência de informação |

            Preservar o termo original não significa aceitá-lo como descrição neutra;
            normalizá-lo não significa que as diferenças desapareceram. O pesquisador
            deve justificar quando mantém, agrupa, separa ou recusa uma categoria e
            avaliar se a reprodução de termos ofensivos é necessária para a análise.
            Bowker e Star (1999) mostram que classificações e infraestruturas possuem
            consequências e não devem ser tratadas como recipientes neutros. Rodrigues
            (2020) examina concretamente os problemas éticos e metodológicos de
            transpor categorias de registros históricos da escravidão para uma base de
            dados. Rawson e Muñoz (2019) alertam para as perdas produzidas pela
            “limpeza” de dados, enquanto D'Ignazio e Klein (2020) mostram que decidir
            o que e como contar envolve poder, trabalho e experiências que podem
            desaparecer das estruturas formais.
            """
        ),
        texto(
            """
            ## 6. Comparação de representações

            ### Experimento — uma decisão de representação altera a contagem

            Os mesmos três documentos serão representados de duas maneiras: com um
            único tema dominante e com todos os temas atribuídos. Antes de executar,
            preveja quais temas desaparecerão ou terão sua frequência alterada.

            No segundo modelo, `explode()` cria temporariamente uma linha para cada
            combinação documento–tema. Isso permite contar os temas sem descartar as
            coexistências registradas em um mesmo documento.
            """
        ),
        codigo(
            """
            import pandas as pd

            documentos_temas = pd.DataFrame({
                "id": ["D001", "D002", "D003"],
                "tema_dominante": ["educação", "trabalho", "educação"],
                "temas_atribuidos": [
                    ["educação", "progresso"],
                    ["trabalho"],
                    ["educação", "trabalho"],
                ],
            })

            contagem_dominante = documentos_temas["tema_dominante"].value_counts()
            contagem_multipla = (
                documentos_temas.explode("temas_atribuidos")["temas_atribuidos"]
                .value_counts()
            )

            comparacao = pd.concat(
                [contagem_dominante, contagem_multipla],
                axis=1,
                keys=["tema dominante", "múltiplos temas"],
            ).fillna(0).astype(int)
            comparacao.index.name = "tema"
            comparacao
            """
        ),
        texto(
            """
            Compare as duas colunas:

            1. Por que “progresso” não aparece na contagem de temas dominantes?
            2. Por que “trabalho” passa de uma para duas ocorrências?
            3. Em qual modelo a soma das frequências pode superar o número de
               documentos e por quê?
            4. Qual representação seria mais adequada à sua pergunta de pesquisa?

            A primeira representação facilita uma contagem, mas força exclusividade. A
            segunda preserva coexistências, porém demanda regras explícitas para
            comparar documentos. Nenhuma estrutura é naturalmente correta: a escolha
            depende da pergunta, da teoria, das fontes e da qualidade da anotação.

            ![Comparação dos mesmos três documentos: o modelo dominante produz três atribuições, enquanto o modelo de múltiplos temas produz cinco relações documento-tema.](imagens/02_representacoes_temas.svg)

            *No primeiro modelo, a unidade contada coincide com o documento. No
            segundo, a contagem recai sobre relações documento–tema; por isso a soma
            pode superar o número de documentos.*

            Comparar as duas estruturas torna observável, em escala didática, o
            argumento de Drucker (2011) e Rawson e Muñoz (2019): organizar ou
            transformar dados também produz um modelo interpretativo.
            """
        ),
        texto(
            """
            ## 7. Validade da representação

            A lista abaixo é um **roteiro didático de verificação**, não uma taxonomia
            retirada integralmente de uma única referência. Ela articula a validade da
            mensuração discutida por Adcock e Collier (2001), a confiabilidade e a
            validade na análise de conteúdo examinadas por Krippendorff (2019) e as
            exigências de contexto e documentação destacadas pelas Humanidades
            Digitais. Uma operacionalização será examinada em quatro dimensões:

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
            ## 8. Mapa de operacionalização

            **Atividade:** produção individual seguida de comparação em dupla.

            **Tempo sugerido:** 25 minutos individuais e 10 minutos em dupla.
            **Produto:** duas operacionalizações alternativas e um parágrafo
            comparativo na célula seguinte.

            1. preencha individualmente as duas linhas;
            2. troque o mapa com um colega;
            3. o colega identifica uma perda ou ambiguidade em cada alternativa;
            4. revise o parágrafo comparativo após a conversa.

            Escolha um conceito central de sua pergunta. Proponha ao menos duas
            operacionalizações. Compare o que cada uma permite observar e o que perde.
            """
        ),
        texto(
            """
            ### Exemplo preenchido — duas alternativas para o mesmo conceito

            | Conceito | Dimensão | Indicador | Unidade de análise | Variável | Categorias ou valores | Fonte | Regra | Limitação |
            |---|---|---|---|---|---|---|---|---|
            | Centralidade do tema educação | Presença temática | Tema dominante atribuído | Documento | `tema_dominante` | educação, trabalho, progresso | Texto integral | Após a leitura, atribuir uma categoria principal segundo um guia de codificação | Força exclusividade e perde temas secundários |
            | Centralidade do tema educação | Extensão da discussão | Proporção de palavras em trechos anotados como educação | Documento | `proporcao_educacao` | número entre 0 e 1 | Texto integral e anotação dos trechos | Dividir o número de palavras dos trechos pertinentes pelo total de palavras do documento | Extensão não equivale a importância histórica ou discursiva |

            **Como ler o exemplo:** as duas linhas partem do mesmo conceito, mas
            escolhem dimensões e indicadores diferentes. A primeira alternativa é
            mais simples, porém apaga a coexistência de temas. A segunda registra a
            extensão da discussão, mas depende de uma regra adicional para decidir
            quais trechos tratam de educação. Nenhuma alternativa é automaticamente
            superior: a escolha precisa ser justificada pela pergunta de pesquisa.

            Use o exemplo como modelo de encadeamento entre as colunas, não como um
            conjunto de categorias que deva ser copiado para qualquer pesquisa.
            """
        ),
        texto(
            """
            ### Meu mapa de operacionalização

            Preencha a tabela diretamente nesta célula:

            | Conceito | Dimensão | Indicador | Unidade de análise | Variável | Categorias ou valores | Fonte | Regra | Limitação |
            |---|---|---|---|---|---|---|---|---|
            | Escreva | Escreva | Escreva | Escreva | Escreva | Escreva | Escreva | Escreva | Escreva |
            | Mesmo conceito | Alternativa | Indicador alternativo | Escreva | Escreva | Escreva | Escreva | Escreva | Escreva |

            Compare as duas linhas em um pequeno parágrafo:

            Escreva aqui.
            """
        ),
        texto(
            """
            ## Referências e leituras

            ### De onde vêm os elementos do percurso?

            | Etapa da unidade | Base bibliográfica | Como a referência é usada aqui |
            |---|---|---|
            | 1. Conceito e dimensão | Babbie (2021, cap. 5) | Apoia a conceituação e a explicitação de dimensões antes da mensuração |
            | 2. Indicador | Babbie (2021, cap. 5); Adcock e Collier (2001) | Sustenta a passagem do conceito a observações e a avaliação de sua validade |
            | 3. Unidade de análise | Krippendorff (2019, cap. 5) | Fundamenta a necessidade de explicitar as unidades usadas na análise |
            | 4. Variáveis, valores, documentos e metadados | Krippendorff (2019, caps. 7–8); Riley (2017) | Apoia regras de registro, variáveis e funções dos metadados |
            | 5. Categorias históricas e analíticas | Bowker e Star (1999); Rodrigues (2020) | Permite examinar classificações como construções situadas e suas consequências |
            | 6. Comparação de representações | Drucker (2011); Rawson e Muñoz (2019) | Sustenta a comparação crítica entre modelos e transformações dos dados |
            | 7. Validade da representação | Adcock e Collier (2001); Krippendorff (2019) | Apoia o exame de validade, confiabilidade e adequação das inferências |
            | 8. Mapa de operacionalização | Síntese didática desta unidade | Reúne os elementos anteriores em um instrumento de planejamento e documentação |

            A tabela indica **afinidades e usos**, não equivalência terminológica
            perfeita: os autores não empregam necessariamente os mesmos termos nem
            apresentam juntos este percurso de oito etapas.

            - ADCOCK, Robert; COLLIER, David (2001). “Measurement Validity: A
              Shared Standard for Qualitative and Quantitative Research”.
            - BABBIE, Earl R. (2021). *The Practice of Social Research*, cap. 5.
            - BOWKER, Geoffrey C.; STAR, Susan Leigh (1999). *Sorting Things Out:
              Classification and Its Consequences*.
            - D'IGNAZIO, Catherine; KLEIN, Lauren F. (2020). *Data Feminism*.
            - DRUCKER, Johanna (2011). “Humanities Approaches to Graphical Display”.
            - KRIPPENDORFF, Klaus (2019). *Content Analysis: An Introduction to
              Its Methodology*, caps. 5, 7–8.
            - RAWSON, Katie; MUÑOZ, Trevor (2019). “Against Cleaning”.
            - RILEY, Jenn (2017). *Understanding Metadata: What Is Metadata, and
              What Is It For? A Primer*.
            - RODRIGUES, Aldair (2020). “Humanidades digitais e diáspora africana”.

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

            ![Três painéis diferenciam população como universo, amostra como subconjunto selecionado e corpus como conjunto de materiais delimitado para análise.](imagens/03_populacao_amostra_corpus.svg)

            *Um corpus pode coincidir parcialmente com uma população ou ser formado
            por seleção, preservação e acesso, mas não deve ser chamado
            automaticamente de amostra representativa.*

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

            | Arquivo do exemplo | Classificação neste notebook | Por quê? |
            |---|---|---|
            | CSV (`documentos_exemplo.csv`) | Estruturado | Os registros seguem o mesmo esquema de linhas e colunas, com um campo definido para cada característica. |
            | JSON (`metadados_exemplo.json`) | Semiestruturado | As informações possuem chaves e organização explícita, mas podem formar listas e objetos hierárquicos, sem depender de uma tabela regular. |
            | TXT (`texto_exemplo.txt`) | Não estruturado | O conteúdo chega como texto contínuo, sem campos computacionais previamente marcados para tema, local ou gênero. |

            A classificação descreve **como a informação está organizada neste
            exemplo**, e não uma propriedade absoluta da extensão do arquivo. Um JSON
            submetido a um esquema rígido, por exemplo, pode ser tratado como dado
            estruturado. O código seguinte permite observar essas diferenças na
            prática.
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

            ### Materialidade documental — um periódico real

            Observe a primeira página abaixo antes de reduzi-la a campos. Título, data,
            preço, público presumido, organização da página, textos e ilustrações são
            dimensões diferentes do objeto. Uma tabela pode registrar algumas delas,
            mas não substitui o documento.

            ![Primeira página de A Estação, de 15 de julho de 1890, com título, data, preços de assinatura, colunas de texto e ilustrações de moda.](imagens/03_periodico_1890.jpg)

            *A Estação: Jornal Illustrado para a Familia*, n. 13, 15 jul. 1890.
            Acervo da Fundação Biblioteca Nacional — Brasil, via Wikimedia Commons,
            domínio público. Esta página **não integra a coleção fictícia** dos
            exercícios; é apresentada apenas para discutir documento, materialidade e
            metadados. Créditos completos em `imagens/README.md`.
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

            ### Objetivo da seção

            Esta seção distingue o que está registrado nos dados, o que o computador
            calcula e o que o pesquisador pode interpretar. Esses níveis se relacionam,
            mas não são equivalentes:

            | Nível | Neste exemplo | Questão de controle |
            |---|---|---|
            | Dados registrados | valores `Capital` e `Interior` na coluna `local` | o que significa `local` e quem atribuiu essa categoria? |
            | Operação computacional | contar quantas vezes cada valor aparece | qual regra o código aplica? |
            | Resultado computacional | seis registros em cada categoria | o resultado está tecnicamente correto para esta tabela? |
            | Evidência para a pesquisa | resultado mobilizado para responder a uma pergunta delimitada | que afirmação o corpus e a operação conseguem sustentar? |
            | Interpretação humanística | explicação situada do significado e dos limites do resultado | que contexto, fontes e bibliografia são necessários? |

            Um resultado não se transforma automaticamente em evidência para qualquer
            afirmação. Ele pode funcionar como evidência quando a pergunta, a origem
            dos dados, as categorias, a operação e o alcance da conclusão estão
            explicitados.

            ### A cadeia de produção da evidência

            | Etapa | Aplicação ao exemplo didático | Pergunta crítica |
            |---|---|---|
            | Fonte | documentos representados pela coleção fictícia | quem produziu os documentos e em que contexto? |
            | Seleção | doze registros incluídos na coleção | por que estes registros foram incluídos e outros não? |
            | Digitalização | conversão ou transcrição para formato computacional, simplificada no exemplo sintético | o que foi perdido, corrigido ou normalizado? |
            | Descrição | campos como `id`, `ano`, `local` e `tema` | quem definiu e preencheu os campos? |
            | Transformação | organização dos registros em CSV e carregamento no pandas | valores foram agrupados ou alterados? |
            | Operação | aplicação de `value_counts()` à coluna `local` | o que exatamente está sendo contado? |
            | Resultado | seis registros como `Capital` e seis como `Interior` | há ausências, grafias divergentes ou casos ambíguos? |
            | Interpretação | formulação de uma afirmação sobre a coleção | a conclusão permanece dentro do alcance do corpus? |

            ![Cadeia em oito etapas: fonte, seleção, digitalização, descrição, transformação, operação, resultado e interpretação, com retorno para revisão.](imagens/03_cadeia_evidencia.svg)

            *A operação ocupa apenas uma etapa. O valor do resultado como evidência
            depende das decisões anteriores e do limite dado à interpretação.*

            Cada etapa condiciona as seguintes. Uma contagem pode estar correta em
            relação à tabela e ainda ser inadequada para uma afirmação histórica ampla.

            ### Experimento — contar registros por categoria local

            No código seguinte, `documentos["local"]` seleciona apenas a coluna
            `local`. O método `value_counts()` agrupa valores iguais e conta quantas
            linhas pertencem a cada categoria. Como cada linha representa um documento,
            o resultado contará documentos **dentro desta coleção**.

            Antes de executar, observe a tabela importada e formule uma previsão. O
            código conhece os rótulos registrados, mas não conhece o significado
            histórico de `Capital` e `Interior`, nem avalia como o corpus foi formado.
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
            ### Como ler a saída

            | Categoria registrada | Número de registros |
            |---|---:|
            | Capital | 6 |
            | Interior | 6 |

            A soma é doze, correspondente ao número de documentos da coleção. O
            resultado descreve a distribuição do campo `local`; ele não explica por
            que a distribuição é igual nem demonstra que a coleção representa uma
            população histórica.

            | Afirmação | Avaliação | Justificativa |
            |---|---|---|
            | “Na coleção didática, seis registros estão classificados como Capital e seis como Interior.” | Sustentada | reproduz a operação e limita o sujeito da frase ao conjunto analisado |
            | “A coleção está numericamente equilibrada entre as duas categorias locais.” | Sustentada, com escopo explícito | descreve a distribuição sem generalizar para além da coleção |
            | “A produção jornalística da Capital e do Interior era igual.” | Não sustentada | exigiria conhecer a população, a preservação e o procedimento de seleção |
            | “O local explica as diferenças entre os documentos.” | Não sustentada | uma contagem descritiva não testa explicação nem causalidade |

            A leitura também depende de pressupostos que precisam ser verificados:

            - cada linha representa efetivamente um documento;
            - `local` possui uma definição documentada e foi aplicado de modo
              consistente;
            - valores ausentes, ambíguos ou grafados de outra forma foram identificados;
            - os critérios de seleção são compatíveis com a pergunta.

            Se um desses pressupostos falhar, o Python ainda poderá produzir `6` e `6`,
            mas o valor do resultado como evidência será reduzido. Uma interpretação
            responsável explicita o sujeito da frase — “na coleção analisada”, e não
            “na sociedade” — e retorna aos documentos quando encontra um padrão.

            Por isso o desenho da pesquisa é iterativo:

            **pergunta → amostragem → leitura → modelagem → resultado → releitura
            → reformulação**

            Neste exemplo, o equilíbrio numérico pode levar à releitura dos documentos,
            à verificação da definição de `local` e ao cruzamento com `genero`, `tema`
            ou `ano`. D'Ignazio e Klein (2020) ajudam a compreender por que números
            dependem de contexto, teoria, trabalho de produção dos dados e relações de
            poder: a operação calcula; o pesquisador constrói e limita a interpretação.
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

            **Modalidade:** produção individual seguida de revisão em dupla.
            **Tempo sugerido:** 30 minutos individuais e 15 minutos em dupla.
            **Produto:** ficha preenchida e uma revisão motivada pelo comentário do
            colega.

            Primeiro, responda aos sete itens com base em seu projeto. Depois, troque a
            ficha com um colega. A revisão deve localizar um critério impreciso, uma
            ausência pouco discutida e uma conclusão que talvez exceda o corpus.

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
            - RODRIGUES, Aldair (2020). “Humanidades digitais e diáspora africana:
              questões éticas e metodológicas na elaboração de uma base de dados
              sobre a população escravizada de Mariana (século XVIII)”.

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

            **Modalidade:** elaboração individual, seguida da revisão em pares ao
            final. **Tempo sugerido:** 60 minutos para a primeira versão e 30 minutos
            para a revisão recíproca. **Produto:** proposta inicial completa, parecer
            recebido e mudanças justificadas.

            Não há código neste notebook: formular, justificar e interpretar são
            atividades de escrita. Os experimentos computacionais dos notebooks
            anteriores devem informar suas decisões, não substituir sua argumentação.

            Recupere os três produtos parciais. Em cada seção, registre o que foi
            mantido, o que mudou e por quê. Revisar uma decisão diante de nova evidência
            é parte do trabalho acadêmico.

            ![Pergunta reformulada, mapa de operacionalização e ficha do corpus convergem para uma proposta inicial, que passa por revisão entre pares e retorna como proposta revisada.](imagens/04_construcao_projeto.svg)

            *A oficina não começa do zero: ela integra os produtos anteriores, testa a
            coerência entre eles e registra mudanças motivadas pela revisão.*
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

            **Finalidade predominante e justificativa:**
            Escreva aqui.

            **Estrutura analítica inicial, etapas secundárias e justificativa:**
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
            variável, categorias ou valores possíveis, fonte da observação, regra e
            limitação. Inclua ao menos duas alternativas para o conceito central.
            """
        ),
        texto(
            """
            ### Meu mapa de operacionalização

            | Conceito | Dimensão | Indicador | Variável | Categorias ou valores | Fonte | Regra | Limitação |
            |---|---|---|---|---|---|---|---|
            | Conceito central | Escreva | Escreva | Escreva | Escreva | Escreva | Escreva | Escreva |
            | Mesmo conceito | Alternativa | Indicador alternativo | Escreva | Escreva | Escreva | Escreva | Escreva |

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
            | Escreva | documento, metadado, identificador ou variável | Escreva | Escreva | Escreva |

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
            ## Atividade — revisão entre pares

            **Modalidade:** duplas, com dois turnos. **Tempo sugerido:** 15 minutos por
            proposta. **Produto:** parecer breve recebido e registro das mudanças
            realizadas.

            No primeiro turno, o autor apresenta a proposta por até 3 minutos; o
            revisor lê a síntese, responde às cinco perguntas e oferece um comentário
            prioritário. Depois, invertam os papéis. Não reescreva a proposta do
            colega: indique o ponto que precisa de decisão ou justificativa.

            Peça a uma colega ou a um colega que responda:

            1. consigo identificar exatamente o que será observado?
            2. os dados propostos podem responder à pergunta?
            3. conceito e indicador estão diferenciados?
            4. o alcance da conclusão está claro?
            5. qual escolha precisa de maior justificativa?

            Revise a formulação após receber o comentário. A pergunta resultante encerra
            a Unidade 1 e orientará a construção da base na Unidade 2.

            ### Parecer recebido

            Escreva aqui.

            ### Mudanças realizadas e justificativa

            Escreva aqui.
            """
        ),
    ]


def criar_readme() -> None:
    links = tabela_links_colab(
        UNIDADE.name,
        (
            ("Guia da unidade", "00_guia_da_unidade.ipynb"),
            ("Perguntas e problemas", "01_perguntas_e_problemas_computacionais.ipynb"),
            ("Representação e operacionalização", "02_representacao_e_operacionalizacao.ipynb"),
            ("Dados, corpus e evidências", "03_dados_corpus_e_evidencias.ipynb"),
            ("Oficina do projeto", "04_oficina_projeto_de_pesquisa.ipynb"),
        ),
    )
    conteudo = f"""\
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

## Abrir os notebooks no Google Colab

{links}

O link carrega o notebook diretamente do GitHub. No Notebook 03, execute a
célula **Preparação do ambiente** antes das demais: ela clona o repositório no
ambiente temporário e posiciona a execução na pasta desta unidade. Os demais
notebooks não dependem de arquivos locais para executar seu código.

## Dependências

- Python 3
- pandas
- JupyterLab, Jupyter Notebook ou VS Code com extensão Jupyter

Os exemplos não dependem de acesso à internet. Os dados da pasta `dados` são
fictícios e foram criados exclusivamente para fins didáticos; não devem ser
utilizados para produzir afirmações históricas.

A pasta `imagens` reúne diagramas autorais, a ilustração conceitual de abertura
e uma fonte histórica em domínio público. O arquivo `imagens/README.md` registra
proveniência, licença, alterações e textos alternativos. As imagens são locais e
continuam disponíveis em uso offline e no Colab.

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

A pasta `professor` contém o roteiro cronológico para condução dos encontros.
O arquivo `cronograma_aula_01_4h.md` organiza a primeira aula de quatro horas,
incluindo intervalo, atividades essenciais e ajustes conforme o ritmo da turma.

A pasta separa organizacionalmente o material, mas não restringe o acesso de
quem possui o repositório.

## Revisão antes da oferta

A pasta `notes/revisores` define uma banca de revisão com seis especialidades:
nível acadêmico, didática, alinhamento, Humanidades Digitais, referências e
qualidade técnica/acessibilidade. Ela também contém matriz de avaliação e modelo
de parecer.

Os pareceres executados ficam em `notes/revisores/pareceres`. Após alterações
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
    salvar_notebook(
        "03_dados_corpus_e_evidencias.ipynb",
        corpus(),
        requer_repositorio=True,
    )
    salvar_notebook("04_oficina_projeto_de_pesquisa.ipynb", oficina())
    print(f"Notebooks, dados e README reconstruídos em: {UNIDADE}")


if __name__ == "__main__":
    main()
