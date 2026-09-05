"""Gera notebooks, dados didáticos e README da Unidade 2."""

from __future__ import annotations

import csv
import json
from pathlib import Path
from textwrap import dedent

from apoio_colab import adicionar_link_na_abertura, preparacao_colab, tabela_links_colab
from construir_imagens_unidade_02 import main as criar_imagens


RAIZ = Path(__file__).resolve().parents[1]
UNIDADE = RAIZ / "unidade_02"
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


def salvar_notebook(
    nome: str,
    celulas: list[dict],
    requer_repositorio: bool = False,
) -> None:
    publicadas = [adicionar_link_na_abertura(celulas[0], UNIDADE.name, nome)]
    if requer_repositorio:
        publicadas.append(codigo(preparacao_colab(UNIDADE.name)))
    publicadas.extend(celulas[1:])
    documento = {
        "cells": publicadas,
        "metadata": {
            "kernelspec": {
                "display_name": "Python 3",
                "language": "python",
                "name": "python3",
            },
            "language_info": {"name": "python", "version": "3"},
        },
        "nbformat": 4,
        "nbformat_minor": 5,
    }
    (UNIDADE / nome).write_text(
        json.dumps(documento, ensure_ascii=False, indent=1) + "\n",
        encoding="utf-8",
    )


def criar_dados() -> None:
    DADOS.mkdir(parents=True, exist_ok=True)
    registros = [
        ["A001", "Arquivo Municipal", "ata", 1890, "Capital", "elite administrativa", "sim", "sim", "público", "completo"],
        ["A002", "Arquivo Municipal", "ata", 1891, "Capital", "elite administrativa", "sim", "sim", "público", "completo"],
        ["A003", "Arquivo Municipal", "requerimento", 1892, "Capital", "trabalhadores", "sim", "não", "restrito", "parcial"],
        ["A004", "Arquivo Municipal", "requerimento", 1894, "Interior", "trabalhadores", "sim", "sim", "público", "completo"],
        ["A005", "Arquivo Municipal", "ata", 1901, "Capital", "elite administrativa", "sim", "sim", "público", "completo"],
        ["B001", "Museu Comunitário", "carta", 1890, "Interior", "associação comunitária", "sim", "sim", "mediante autorização", "parcial"],
        ["B002", "Museu Comunitário", "carta", 1893, "Interior", "mulheres associadas", "sim", "sim", "mediante autorização", "completo"],
        ["B003", "Museu Comunitário", "fotografia", 1895, "Interior", "associação comunitária", "sim", "não", "mediante autorização", "mínimo"],
        ["B004", "Museu Comunitário", "carta", 1902, "Interior", "mulheres associadas", "sim", "sim", "mediante autorização", "parcial"],
        ["C001", "Biblioteca Regional", "jornal", 1890, "Capital", "público leitor", "sim", "sim", "público", "completo"],
        ["C002", "Biblioteca Regional", "jornal", 1892, "Capital", "público leitor", "sim", "sim", "público", "completo"],
        ["C003", "Biblioteca Regional", "jornal", 1895, "Interior", "público leitor", "sim", "sim", "público", "parcial"],
        ["C004", "Biblioteca Regional", "jornal", 1900, "Capital", "público leitor", "sim", "sim", "público", "completo"],
        ["C005", "Biblioteca Regional", "jornal", 1904, "Interior", "público leitor", "sim", "não", "público", "mínimo"],
        ["D001", "Coleção Particular", "diário", 1891, "Capital", "família proprietária", "não", "não", "sem autorização", "mínimo"],
        ["D002", "Coleção Particular", "diário", 1903, "Interior", "família proprietária", "sim", "não", "restrito", "parcial"],
    ]
    with (DADOS / "catalogo_fontes.csv").open("w", encoding="utf-8", newline="") as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerow(
            [
                "id_fonte", "instituicao", "tipo_documental", "ano", "local",
                "grupo_representado", "localizado", "digitalizado",
                "condicao_acesso", "qualidade_metadados",
            ]
        )
        escritor.writerows(registros)

    proveniencia = {
        "titulo": "Catálogo didático de fontes",
        "natureza": "dados inteiramente fictícios",
        "criado_em": "2026-07-30",
        "responsavel": "equipe docente",
        "finalidade": "demonstrar seleção, cobertura, metadados e proveniência",
        "origem": "registros simulados, sem correspondência com acervos reais",
        "transformacoes": [
            "atribuição manual de identificadores",
            "normalização didática de nomes de instituições",
            "criação deliberada de lacunas de digitalização e metadados",
        ],
        "restricoes": [
            "não usar para afirmações históricas",
            "condições de acesso são exemplos pedagógicos",
        ],
    }
    (DADOS / "proveniencia_catalogo.json").write_text(
        json.dumps(proveniencia, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )

    dicionario = [
        ["id_fonte", "Identificador estável no catálogo didático", "texto", "único e não vazio", "equipe docente"],
        ["instituicao", "Custodiante fictício da fonte", "categoria", "quatro valores previstos", "catálogo simulado"],
        ["tipo_documental", "Gênero atribuído ao item", "categoria", "vocabulário controlado", "catálogo simulado"],
        ["ano", "Ano atribuído ao item", "inteiro", "1890 a 1904", "catálogo simulado"],
        ["local", "Recorte espacial amplo", "categoria", "Capital ou Interior", "catálogo simulado"],
        ["grupo_representado", "Grupo mais diretamente registrado", "categoria", "interpretação didática", "equipe docente"],
        ["localizado", "Item localizado no levantamento", "categoria", "sim ou não", "levantamento simulado"],
        ["digitalizado", "Representação digital disponível", "categoria", "sim ou não", "levantamento simulado"],
        ["condicao_acesso", "Condição informada pelo custodiante", "categoria", "não equivale a licença de uso", "catálogo simulado"],
        ["qualidade_metadados", "Completude descritiva aproximada", "ordinal", "mínimo, parcial ou completo", "equipe docente"],
    ]
    with (DADOS / "dicionario_dados.csv").open("w", encoding="utf-8", newline="") as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerow(["campo", "descricao", "tipo", "regra", "origem"])
        escritor.writerows(dicionario)


def guia() -> list[dict]:
    return [
        texto(
            """
            # Unidade 2 — Guia de estudo

            ## Como construir uma base adequada à pergunta?

            Observe na ilustração que as fontes atravessam diferentes decisões, mas
            os registros excluídos não desaparecem: eles permanecem documentados para
            auditoria e possível revisão.

            ![Conjunto heterogêneo de fontes atravessa filtros de seleção até formar uma base organizada; registros não selecionados permanecem documentados e ligados à cadeia de proveniência.](imagens/00_abertura_conceitual.png)

            *Ilustração conceitual gerada para a abertura da unidade; não representa
            documentos ou acervos históricos reais.*

            **Problema orientador:** quais dados são necessários e como saber se eles
            representam adequadamente o fenômeno investigado?

            Uma base não é adequada apenas porque contém muitos registros. Sua
            adequação depende da pergunta, das unidades observadas, da cadeia de
            produção das fontes, da cobertura, das exclusões e das condições de uso.
            Esta unidade transforma a pergunta da Unidade 1 em um protocolo auditável
            de construção da base.
            """
        ),
        texto(
            """
            ## Objetivos

            Ao final, você deverá ser capaz de:

            1. delimitar população, população acessível e corpus;
            2. justificar fontes e critérios de seleção;
            3. avaliar cobertura, vieses, ausências e silêncios;
            4. documentar metadados, identificadores e proveniência;
            5. relacionar os princípios FAIR e CARE à documentação do ciclo de
               vida de uma base;
            6. reconhecer responsabilidades éticas e questões legais;
            7. produzir o protocolo da base do seu projeto.
            """
        ),
        texto(
            """
            ## Percurso

            | Notebook | Questão central | Produto |
            |---|---|---|
            | 00 | O que torna uma base adequada? | Diagnóstico |
            | 01 | De onde vêm e como selecionar os registros? | Protocolo de seleção |
            | 02 | Quem e o que a base cobre ou silencia? | Matriz de cobertura |
            | 03 | Como tornar a base auditável? | Dicionário e proveniência |
            | 04 | Reutilizável para quem e sob qual autoridade? | Ficha de governança e documentação |
            | 05 | O desenho da base é defensável? | Protocolo completo |

            Os dados são **inteiramente fictícios**. As lacunas foram criadas para
            permitir experimentos sem fazer afirmações sobre acervos reais.

            O diagrama abaixo mostra que cada notebook produz uma parte do protocolo e
            que os resultados podem exigir o retorno às decisões anteriores.

            ![Percurso dos Notebooks 00 a 05: diagnóstico, seleção, cobertura, documentação, governança e oficina conduzem a um protocolo defensável, com uma seta de retorno para revisão.](imagens/00_percurso_unidade.svg)

            O percurso é cumulativo, mas não estritamente linear: uma lacuna percebida
            na cobertura pode levar à revisão das fontes ou dos critérios de seleção.
            """
        ),
        codigo(
            """
            from pathlib import Path
            import pandas as pd

            pasta_dados = Path("dados")
            catalogo = pd.read_csv(pasta_dados / "catalogo_fontes.csv")
            print(f"Registros didáticos disponíveis: {len(catalogo)}")
            catalogo.head(3)
            """
        ),
        texto(
            """
            ## Diagnóstico inicial

            Responda em Markdown:

            1. Uma coleção digitalizada é necessariamente representativa? Por quê?
            2. Que diferença existe entre não localizar uma fonte e encontrar um campo
               vazio em uma planilha?
            3. Que informação você precisaria para reutilizar uma base criada por outra
               pessoa?
            4. Dados publicamente acessíveis podem ser coletados e republicados sem
               qualquer avaliação ética ou legal?

            ### Minha resposta

            Escreva aqui.
            """
        ),
        texto(
            """
            ## Critérios do produto

            O protocolo final será avaliado por: alinhamento à pergunta; seleção
            reproduzível; análise de cobertura; documentação; proveniência; ética e
            legalidade; reconhecimento explícito dos limites.

            **Leituras de orientação:** Gebru et al. (2021) sobre documentação de
            bases; Rodrigues (2020) sobre decisões éticas e metodológicas em uma base
            histórica; ANPD (2023/2025) para tratamento de dados pessoais em pesquisa.
            Dados completos: `referencias.md`.
            """
        ),
    ]


def fontes_selecao() -> list[dict]:
    return [
        texto(
            """
            # Fontes, população e seleção

            ## 1. A base começa antes da planilha

            Retome sua pergunta da Unidade 1. A **população de interesse** reúne os
            casos sobre os quais se deseja argumentar; a **população acessível** reúne
            os casos que podem ser localizados e consultados nas condições do projeto;
            o **corpus** é o conjunto efetivamente delimitado por critérios explícitos.

            Essas extensões não são automaticamente iguais. Um acervo digital costuma
            refletir preservação, catalogação, digitalização, acesso e decisões
            institucionais anteriores à pesquisa.

            Observe como o diagrama situa o corpus dentro da população acessível e
            explicita as mediações que limitam a passagem entre os conjuntos.

            ![População de interesse contém a população acessível, que contém o corpus; ao lado, produção, preservação, catalogação, localização, digitalização, acesso e seleção aparecem como mediações.](imagens/01_populacao_acessivel_corpus.svg)

            A figura é um modelo conceitual, não uma prova de representatividade. Um
            corpus pode ser grande e ainda assim resultar de acesso muito desigual.
            """
        ),
        texto(
            """
            ## 2. Fonte primária, secundária e dado derivado

            Na prática historiográfica, a distinção pode ser formulada assim:

            | Relação com a pesquisa | Definição operacional |
            |---|---|
            | **Fonte primária** | Documento, objeto, imagem, registro estatístico, testemunho ou outro vestígio produzido no período estudado ou por atores diretamente relacionados a ele, mobilizado como evidência sobre esse contexto. |
            | **Fonte secundária** | Interpretação posterior que analisa o passado com base em fontes primárias e em diálogo com outras interpretações. Livros e artigos historiográficos são exemplos recorrentes. |

            A American Historical Association (AHA, 2023) emprega uma noção ampla
            de documento primário — que inclui textos, artefatos, imagens, vídeos,
            estatísticas, relatos orais e ambientes construídos — e define a
            literatura secundária como interpretações posteriores fundamentadas
            nesses documentos. A própria associação adverte, contudo, que a fronteira
            entre as duas categorias depende em grande medida da pergunta de pesquisa.

            O mesmo catálogo ocupa posições diferentes no diagrama conforme o que se
            pretende investigar.

            ![O mesmo catálogo institucional funciona como instrumento ou dado derivado para uma pergunta sobre cartas e como fonte primária para uma pergunta sobre práticas de catalogação.](imagens/01_papel_das_fontes.svg)

            Portanto, “primária” e “secundária” descrevem uma **relação entre o
            material, o problema e o uso analítico**, não uma qualidade fixa do
            arquivo. Um catálogo institucional pode ser fonte secundária para estudar
            as cartas que descreve, mas fonte primária para investigar práticas de
            catalogação. Do mesmo modo, um artigo historiográfico é secundário para
            estudar o período que interpreta, mas pode ser primário em uma pesquisa
            sobre a historiografia daquele tema.

            A classificação também não estabelece uma hierarquia automática de
            verdade: fontes primárias e secundárias exigem crítica de autoria,
            finalidade, contexto, mediação, ausências e limites. Uma tabela criada por
            transcrição ou OCR é um **dado derivado**. Ela não substitui o documento e
            deve permanecer ligada à fonte e às decisões que a produziram.

            Fontes governamentais, institucionais e documentais exigem perguntas
            distintas: quem produziu o registro, com qual finalidade, sob quais
            categorias e com que condições de acesso?

            **Referência:** American Historical Association (2023), seção “Shared
            Values of Historians”. Dados completos em `referencias.md`.
            """
        ),
        texto(
            """
            ## 3. Critérios antes da filtragem

            Um critério deve informar campo, regra, justificativa e tratamento dos
            casos limítrofes. Para o experimento, adotaremos:

            - período de 1890 a 1900;
            - item localizado;
            - representação digital disponível;
            - acesso público ou mediante autorização.

            Preveja quais grupos e instituições poderão perder presença.
            """
        ),
        codigo(
            """
            import pandas as pd

            catalogo = pd.read_csv("dados/catalogo_fontes.csv")
            criterio_periodo = catalogo["ano"].between(1890, 1900)
            criterio_localizado = catalogo["localizado"].eq("sim")
            criterio_digital = catalogo["digitalizado"].eq("sim")
            criterio_acesso = catalogo["condicao_acesso"].isin(
                ["público", "mediante autorização"]
            )

            corpus = catalogo[
                criterio_periodo
                & criterio_localizado
                & criterio_digital
                & criterio_acesso
            ].copy()
            corpus[["id_fonte", "instituicao", "ano", "grupo_representado"]]
            """
        ),
        texto(
            """
            ## 4. Registrar exclusões

            Reprodutibilidade não exige apenas uma lista final. Exige saber por que um
            registro ficou de fora. O código abaixo produz um diagnóstico; a
            justificativa substantiva continua sendo responsabilidade da pesquisa.
            """
        ),
        codigo(
            """
            motivos = pd.DataFrame(
                {
                    "id_fonte": catalogo["id_fonte"],
                    "fora_periodo": ~criterio_periodo,
                    "nao_localizado": ~criterio_localizado,
                    "sem_digitalizacao": ~criterio_digital,
                    "acesso_incompativel": ~criterio_acesso,
                }
            )
            motivos["incluido"] = ~motivos.iloc[:, 1:].any(axis=1)
            motivos
            """
        ),
        texto(
            """
            ### Interpretação

            1. Quantos registros foram excluídos por cada regra?
            2. Um registro pode ter mais de um motivo?
            3. “Não digitalizado” é uma propriedade do fenômeno ou da infraestrutura?
            4. Seria possível consultar presencialmente parte do material excluído?

            Escreva aqui.
            """
        ),
        texto(
            """
            ## Atividade — protocolo de seleção

            Para seu projeto, registre:

            **População de interesse:** Escreva aqui.

            **População acessível e condições de acesso:** Escreva aqui.

            **Unidade de análise:** Escreva aqui.

            **Fontes e relação com a pergunta:** Escreva aqui.

            **Critérios de inclusão, justificativas e evidências:** Escreva aqui.

            **Critérios de exclusão e casos limítrofes:** Escreva aqui.

            **Como as exclusões serão registradas:** Escreva aqui.
            """
        ),
        texto(
            """
            ## Síntese e leituras

            Selecionar é construir o alcance da análise. Uma regra tecnicamente clara
            pode continuar substantivamente inadequada. Rodrigues (2020) mostra como
            a elaboração de uma base histórica envolve escolhas metodológicas e
            éticas; Gebru et al. (2021) recomendam documentar motivação, composição,
            coleta e usos. Dados completos: `referencias.md`.
            """
        ),
    ]


def cobertura() -> list[dict]:
    return [
        texto(
            """
            # Cobertura, vieses e silêncios

            ## 1. Cobertura não é sinônimo de representatividade

            **Cobertura** descreve quais períodos, lugares, instituições, tipos
            documentais ou grupos aparecem na base. **Representatividade** é uma
            afirmação mais forte: depende da população, do mecanismo de seleção e do
            tipo de inferência pretendida. Um corpus pode ter boa cobertura temporal e
            ainda excluir sistematicamente determinadas experiências.
            """
        ),
        texto(
            """
            ## 2. Três ausências diferentes

            | Situação | Exemplo | Consequência |
            |---|---|---|
            | ausência no registro histórico | uma experiência não foi documentada | não pode ser corrigida preenchendo uma célula |
            | ausência na base | fonte existente não foi localizada ou selecionada | requer busca, novo acesso ou revisão do recorte |
            | valor ausente | campo não preenchido em registro incluído | requer diagnóstico e regra de tratamento |

            A cadeia abaixo localiza as ausências no processo que vai da experiência
            vivida ao campo preenchido na base.

            ![Cadeia da experiência ao registro, à preservação, à base e ao campo preenchido; entre as etapas aparecem ausência no registro histórico, perda de preservação, ausência na base e valor ausente.](imagens/02_cadeia_ausencias.svg)

            Silêncios documentais também são efeitos de poder: quem podia registrar,
            preservar, classificar e autorizar acesso? Trouillot (1995) situa silêncios
            em diferentes momentos da produção histórica; Schwartz e Cook (2002)
            discutem arquivos, memória e poder.
            """
        ),
        texto(
            """
            ## 3. Comparar universo acessível e corpus

            Vamos reutilizar os critérios do notebook anterior e comparar distribuições.
            Contagens pequenas não medem importância social; tornam perdas de cobertura
            visíveis para revisão.
            """
        ),
        codigo(
            """
            import pandas as pd

            catalogo = pd.read_csv("dados/catalogo_fontes.csv")
            corpus = catalogo[
                catalogo["ano"].between(1890, 1900)
                & catalogo["localizado"].eq("sim")
                & catalogo["digitalizado"].eq("sim")
                & catalogo["condicao_acesso"].isin(
                    ["público", "mediante autorização"]
                )
            ].copy()

            cobertura = pd.concat(
                [
                    catalogo["grupo_representado"].value_counts().rename("catálogo"),
                    corpus["grupo_representado"].value_counts().rename("corpus"),
                ],
                axis=1,
            ).fillna(0).astype(int)
            cobertura
            """
        ),
        texto(
            """
            ### Leitura da saída

            A visualização retoma os valores calculados e permite perceber rapidamente
            quais grupos diminuem ou desaparecem após a aplicação dos critérios.

            ![Barras comparam grupos no catálogo e no corpus: família proprietária cai de dois para zero, trabalhadores de dois para um e público leitor de cinco para quatro.](imagens/02_cobertura_catalogo_corpus.svg)

            A tabela não revela diretamente a composição da população histórica. Ela
            revela como decisões de localização, digitalização, acesso e período
            alteram este catálogo fictício. Identifique grupos que desaparecem,
            diminuem ou permanecem e associe cada mudança a uma etapa da seleção.

            Escreva aqui.
            """
        ),
        codigo(
            """
            por_instituicao = pd.crosstab(
                catalogo["instituicao"],
                catalogo["digitalizado"],
                margins=True,
            )
            por_instituicao
            """
        ),
        texto(
            """
            ## 4. Viés de seleção

            Viés de seleção ocorre quando a inclusão se relaciona de modo sistemático
            a características relevantes para a pergunta. “Usar apenas o que está
            digitalizado” pode favorecer instituições com mais recursos, gêneros mais
            fáceis de digitalizar ou materiais com acesso menos restrito.

            Associação entre instituição e digitalização, neste exemplo, é um sinal
            para investigar o processo de seleção; não é explicação histórica.
            """
        ),
        texto(
            """
            ## Atividade — matriz de cobertura

            | Dimensão | Cobertura desejada | Cobertura acessível | Lacuna | Consequência | Mitigação |
            |---|---|---|---|---|---|
            | temporal | Escreva aqui | Escreva aqui | Escreva aqui | Escreva aqui | Escreva aqui |
            | geográfica | Escreva aqui | Escreva aqui | Escreva aqui | Escreva aqui | Escreva aqui |
            | institucional | Escreva aqui | Escreva aqui | Escreva aqui | Escreva aqui | Escreva aqui |
            | social | Escreva aqui | Escreva aqui | Escreva aqui | Escreva aqui | Escreva aqui |
            | documental | Escreva aqui | Escreva aqui | Escreva aqui | Escreva aqui | Escreva aqui |

            **Silêncios que a ampliação da coleta talvez não resolva:** Escreva aqui.

            **Como os limites restringem minhas afirmações:** Escreva aqui.
            """
        ),
        texto(
            """
            ## Da cobertura à governança

            Mais dados não são sempre a resposta. Ampliar um corpus pode reduzir
            certas lacunas, mas também pode contrariar direitos, protocolos de acesso
            ou interesses das pessoas e comunidades relacionadas aos dados. O
            Notebook 04 aprofundará essa passagem da disponibilidade técnica para a
            governança, distinguindo os princípios FAIR e CARE.

            ## Síntese

            Uma análise responsável documenta não só o que existe na tabela, mas os
            processos que produziram presenças, ausências e possibilidades de acesso.
            """
        ),
    ]


def metadados() -> list[dict]:
    return [
        texto(
            """
            # Metadados, identificadores e proveniência

            ## 1. Documentação como parte da base

            Metadados permitem compreender, localizar, relacionar, administrar e
            reutilizar registros. Para esta unidade, distinguiremos:

            - **descritivos:** título, autoria, data, assunto;
            - **administrativos:** direitos, acesso, formato, responsável;
            - **estruturais:** relações entre partes, páginas ou versões;
            - **proveniência:** origem, agentes, datas e transformações.

            As categorias se sobrepõem em padrões reais; servem aqui como guia de
            inspeção.
            """
        ),
        texto(
            """
            ## 2. Dicionário de dados

            Um dicionário deve registrar ao menos nome, definição, tipo, valores ou
            regras, origem e limitações. Ele documenta o significado esperado; não
            garante que os registros estejam corretos.
            """
        ),
        codigo(
            """
            import json
            import pandas as pd

            catalogo = pd.read_csv("dados/catalogo_fontes.csv")
            dicionario = pd.read_csv("dados/dicionario_dados.csv")
            dicionario
            """
        ),
        texto(
            """
            ## 3. Identificadores

            Um identificador deve ser único no escopo definido, persistente o bastante
            para manter relações e independente de atributos que podem mudar. Título
            ou número da linha são candidatos frágeis. O teste abaixo verifica
            unicidade e ausência, mas não prova persistência institucional.
            """
        ),
        codigo(
            """
            auditoria_id = {
                "registros": len(catalogo),
                "ids_ausentes": int(catalogo["id_fonte"].isna().sum()),
                "ids_duplicados": int(catalogo["id_fonte"].duplicated().sum()),
                "ids_unicos": int(catalogo["id_fonte"].nunique()),
            }
            auditoria_id
            """
        ),
        texto(
            """
            ## 4. Campos e domínios esperados

            Esta auditoria compara o esquema observado com o documentado e verifica
            domínios simples. Diagnosticar não é limpar: decisões de padronização serão
            trabalhadas na Unidade 3.
            """
        ),
        codigo(
            """
            campos_documentados = set(dicionario["campo"])
            campos_observados = set(catalogo.columns)
            print("Sem documentação:", sorted(campos_observados - campos_documentados))
            print("Documentados e ausentes:", sorted(campos_documentados - campos_observados))

            dominios_esperados = {
                "localizado": {"sim", "não"},
                "digitalizado": {"sim", "não"},
                "qualidade_metadados": {"mínimo", "parcial", "completo"},
            }
            for campo, dominio in dominios_esperados.items():
                inesperados = set(catalogo[campo].dropna()) - dominio
                print(campo, "valores inesperados:", inesperados)
            """
        ),
        texto(
            """
            ## 5. Proveniência

            No diagrama, o dicionário explica o significado dos campos, enquanto a
            proveniência registra a trajetória entre fonte, atividade, agente e dado
            derivado.

            ![Cadeia conecta fonte, registro e identificador, transformação e dado derivado; o dicionário de dados define os campos e a proveniência registra entidades, atividades, agentes, versões e datas.](imagens/03_documentacao_proveniencia.svg)

            Proveniência responde: quem criou ou custodiou o registro, de onde ele
            veio, quando foi obtido, sob quais condições e que transformações sofreu?
            Ela forma uma cadeia entre fonte, representação e resultado. Um endereço
            eletrônico sozinho não documenta data de acesso, versão, autoria nem
            transformação.
            """
        ),
        codigo(
            """
            with open("dados/proveniencia_catalogo.json", encoding="utf-8") as arquivo:
                proveniencia = json.load(arquivo)

            for chave in ["titulo", "natureza", "criado_em", "responsavel", "origem"]:
                print(f"{chave}: {proveniencia[chave]}")
            print("Transformações registradas:", len(proveniencia["transformacoes"]))
            """
        ),
        texto(
            """
            ## Atividade — documentação do projeto

            **Estratégia de identificadores e escopo de unicidade:** Escreva aqui.

            **Metadados mínimos e justificativa:** Escreva aqui.

            **Campos do dicionário, definições e domínios:** Escreva aqui.

            **Origem, custodiante, versão e data de acesso:** Escreva aqui.

            **Transformações previstas e responsável por registrá-las:** Escreva aqui.

            **Relação entre registro derivado e fonte:** Escreva aqui.
            """
        ),
        texto(
            """
            ## Leituras e síntese

            O modelo PROV-O do W3C oferece conceitos para representar entidades,
            atividades e agentes. Ele não substitui a descrição arquivística ou os
            padrões específicos do campo; oferece uma linguagem para tornar relações
            e decisões rastreáveis. No Notebook 04, a documentação será ampliada para
            motivação, composição, usos, distribuição e manutenção da base a partir
            da proposta de *Datasheets for Datasets*.

            Uma base auditável combina documentação legível por pessoas com
            verificações computacionais simples. Dados completos: `referencias.md`.
            """
        ),
    ]


def governanca_documentacao() -> list[dict]:
    return [
        texto(
            """
            # Governança, reuso e documentação de bases

            ## Uma base bem documentada é automaticamente justa e reutilizável?

            Uma base pode ter identificadores persistentes, metadados completos e
            formato aberto e, ainda assim, ter sido disponibilizada sem participação
            das comunidades relacionadas aos dados. Também pode ter acesso restrito
            por razões justificáveis e continuar bem documentada e reutilizável sob
            condições explícitas.

            Este notebook aproxima três lentes complementares: os princípios FAIR,
            os princípios CARE e a proposta de *Datasheets for Datasets*.

            ![Três lentes complementares examinam uma base: FAIR focaliza encontrabilidade e reuso técnico, CARE focaliza pessoas, autoridade e responsabilidade, e datasheets documentam o ciclo de vida.](imagens/04_fair_care_datasheets.svg)

            **Problema orientador:** reutilizável para quem, com qual finalidade, sob
            qual autoridade e com que documentação?

            Ao final, você deverá ser capaz de:

            1. explicar o que FAIR procura tornar possível;
            2. situar CARE na governança de dados indígenas;
            3. distinguir abertura, acessibilidade e autoridade;
            4. adaptar perguntas de *datasheets* a uma base de Humanidades Digitais;
            5. produzir uma ficha de governança e documentação para seu projeto.
            """
        ),
        texto(
            """
            ## 1. Três lentes, três perguntas

            | Lente | Pergunta central | Unidade de atenção | O que não garante sozinha |
            |---|---|---|---|
            | FAIR | Os objetos digitais podem ser encontrados, acessados, combinados e reutilizados? | dados, metadados, identificadores, protocolos e vocabulários | justiça, autorização comunitária ou ausência de dano |
            | CARE | Para quem os dados geram benefício, quem exerce autoridade e quais responsabilidades existem? | povos indígenas, relações, direitos, interesses e finalidades | implementação técnica ou documentação completa |
            | *Datasheets* | Como e por que a base foi criada, processada, distribuída e mantida? | ciclo de vida, produtores, consumidores e pessoas afetadas | aprovação ética, qualidade absoluta ou uso futuro sem risco |

            As três lentes não formam uma escala e não produzem automaticamente um
            selo de qualidade. Elas tornam perguntas diferentes visíveis. Uma decisão
            defensável precisa registrar tanto as evidências quanto aquilo que ainda
            depende de consulta, negociação ou avaliação institucional.
            """
        ),
        texto(
            """
            ## 2. Princípios FAIR

            Wilkinson et al. (2016) formularam princípios para ampliar a reutilização
            de objetos digitais por pessoas e máquinas. FAIR é um acrônimo:

            | Princípio | Sentido | Evidências possíveis em uma base histórica |
            |---|---|---|
            | **F — Findable / Encontrável** | dados e metadados possuem identificadores e podem ser localizados | identificador persistente, descrição rica e mecanismo de busca |
            | **A — Accessible / Acessível** | existe um protocolo explícito para recuperar dados ou metadados | endereço documentado, protocolo padronizado e condições de acesso |
            | **I — Interoperable / Interoperável** | dados e metadados podem relacionar-se a outros sistemas | formatos documentados, vocabulários e relações qualificadas |
            | **R — Reusable / Reutilizável** | contexto, proveniência e condições permitem avaliar novos usos | licença ou termos, proveniência, padrões do campo e limitações |

            ### Acessível não significa necessariamente aberto

            FAIR não exige que todo arquivo seja oferecido irrestritamente. Dados
            sensíveis ou protegidos podem exigir autenticação e autorização. Nesse
            caso, os metadados e o procedimento de solicitação devem permanecer tão
            claros quanto possível. A pergunta não é somente “consigo baixar?”, mas
            “as condições de acesso estão descritas e podem ser aplicadas?”.

            FAIR também não é um padrão técnico único nem uma propriedade binária. Os
            princípios orientam decisões; sua aplicação depende do domínio, da
            infraestrutura e do objeto digital considerado.
            """
        ),
        texto(
            """
            ## 3. Experimento guiado — quais evidências podem ser auditadas?

            O código abaixo não decide se a base “é FAIR”. Ele verifica apenas sinais
            observáveis no pacote didático: identificadores, documentação dos campos,
            condições de acesso, formato, proveniência e licença. Antes de executar,
            preveja quais verificações falharão.
            """
        ),
        codigo(
            """
            from pathlib import Path
            import json
            import pandas as pd

            pasta_dados = Path("dados")
            catalogo = pd.read_csv(pasta_dados / "catalogo_fontes.csv")
            dicionario = pd.read_csv(pasta_dados / "dicionario_dados.csv")
            with (pasta_dados / "proveniencia_catalogo.json").open(encoding="utf-8") as arquivo:
                proveniencia = json.load(arquivo)

            ids_validos = catalogo["id_fonte"].notna().all() and catalogo["id_fonte"].is_unique
            campos_documentados = set(catalogo.columns) <= set(dicionario["campo"])
            acesso_descrito = catalogo["condicao_acesso"].notna().all()

            auditoria = pd.DataFrame([
                {"princípio": "F", "evidência examinada": "identificadores únicos e não vazios", "presente": ids_validos},
                {"princípio": "F", "evidência examinada": "campos do catálogo documentados", "presente": campos_documentados},
                {"princípio": "A", "evidência examinada": "condição de acesso por registro", "presente": acesso_descrito},
                {"princípio": "A", "evidência examinada": "protocolo de solicitação ou recuperação", "presente": "protocolo_acesso" in proveniencia},
                {"princípio": "I", "evidência examinada": "formato estruturado e dicionário de dados", "presente": dicionario.shape[0] > 0},
                {"princípio": "R", "evidência examinada": "origem e transformações registradas", "presente": bool(proveniencia.get("origem")) and bool(proveniencia.get("transformacoes"))},
                {"princípio": "R", "evidência examinada": "licença ou termos de reutilização", "presente": "licenca" in proveniencia},
            ])
            auditoria
            """
        ),
        texto(
            """
            ### Interpretação da auditoria

            1. Qual ausência impede compreender como solicitar acesso?
            2. Por que `condicao_acesso` não equivale a uma licença de reutilização?
            3. Que aspectos de interoperabilidade não foram examinados pelo código?
            4. Por que não devemos somar a coluna `presente` para produzir uma “nota
               FAIR” definitiva?

            **Minha interpretação:** Escreva aqui.

            O resultado é uma lista de evidências e lacunas. Ele não avalia a
            qualidade semântica dos metadados, a estabilidade futura dos
            identificadores, a adequação dos vocabulários nem a legitimidade das
            condições de acesso.
            """
        ),
        texto(
            """
            ## 4. Princípios CARE e soberania de dados indígenas

            Os princípios CARE foram desenvolvidos em consulta com povos indígenas e
            redes de soberania de dados indígenas. Carroll et al. (2020) os apresentam
            como orientação centrada em pessoas e propósitos, complementar à ênfase
            de FAIR nos dados e na infraestrutura.

            | Princípio | Questões para análise situada |
            |---|---|
            | **C — Collective Benefit / Benefício coletivo** | A iniciativa responde a prioridades definidas pelos povos envolvidos? Que benefícios retornam às comunidades? |
            | **A — Authority to Control / Autoridade para controlar** | Quem tem direito e poder efetivo para decidir coleta, acesso, uso e reutilização? |
            | **R — Responsibility / Responsabilidade** | Que relações, capacidades e deveres de cuidado devem ser mantidos ao longo do projeto? |
            | **E — Ethics / Ética** | Como minimizar danos, promover justiça e permitir que os próprios povos avaliem riscos e usos futuros? |

            CARE não deve ser separado de sua origem e convertido em uma lista ética
            genérica. Quando o projeto envolver dados, conhecimentos, territórios ou
            patrimônio de povos indígenas, a aplicação exige participação e
            autoridade reais; responder individualmente a um formulário não demonstra
            conformidade. Em outros contextos, CARE pode provocar perguntas úteis
            sobre poder e benefício, mas o projeto não deve alegar adesão aos
            princípios sem justificar seu âmbito e sua governança.
            """
        ),
        texto(
            """
            ## 5. FAIR e CARE podem produzir tensões produtivas

            Compare os casos fictícios:

            | Caso | Leitura por FAIR | Leitura por CARE |
            |---|---|---|
            | Um repositório publica imagens, metadados e API aberta de uma coleção indígena sem participação do povo relacionado | os objetos podem ser encontráveis, acessíveis e interoperáveis | abertura técnica não responde quem autorizou, quem se beneficia nem quais usos causam dano |
            | Uma comunidade mantém certos registros restritos, mas publica metadados e um procedimento de acesso sob sua autoridade | a restrição não impede necessariamente FAIR, se o protocolo estiver documentado | o controle de acesso pode expressar autoridade, responsabilidade e ética |

            ### Discussão em duplas — abrir, restringir ou negociar?

            **Dinâmica:** em 5 minutos, cada estudante escolhe um caso e formula uma
            decisão. Em 10 minutos, a dupla compara as decisões usando ao menos uma
            evidência FAIR e duas questões CARE. Em 10 minutos, as duplas apresentam
            uma condição que faria sua decisão mudar.

            Não procure uma regra universal. Identifique quem pode decidir, quais
            informações faltam e quais danos ou benefícios cada forma de acesso pode
            produzir.
            """
        ),
        texto(
            """
            ## 6. *Datasheets for Datasets*

            Gebru et al. (2021) propõem que uma base seja acompanhada por um documento
            estruturado que ajude produtores e usuários a refletir sobre sua criação e
            seus usos. As perguntas acompanham aproximadamente o ciclo de vida:

            | Parte | O que documentar em uma adaptação para Humanidades Digitais |
            |---|---|
            | motivação | pergunta, finalidade, equipe, instituições e financiamento |
            | composição | unidade, população, corpus, campos, lacunas e pessoas ou grupos representados |
            | coleta | fontes, custodiantes, período, seleção, consentimento ou autorizações aplicáveis |
            | processamento | transcrição, OCR, classificação, exclusões, normalização e versões preservadas |
            | usos | análises previstas, usos inadequados, riscos e limites das inferências |
            | distribuição | forma de acesso, licença, termos, restrições e documentação fornecida |
            | manutenção | responsável, contato, correções, novas versões, retenção e descontinuação |

            A proposta nasceu no contexto de aprendizado de máquina. Aqui ela será
            adaptada criticamente para catálogos, corpus e coleções digitais. Ela não
            substitui descrição arquivística, plano de gestão, avaliação ética,
            parecer jurídico ou consulta às comunidades relacionadas aos dados.

            Os autores também alertam que a criação da ficha não deve ser totalmente
            automatizada: seu valor está na reflexão sobre escolhas, riscos e
            responsabilidades, não apenas na extração de propriedades técnicas.
            """
        ),
        texto(
            """
            ## 7. Atividade integrada — ficha de governança e documentação

            **Produto:** uma ficha de uma a duas páginas que será incorporada ao
            protocolo da oficina.

            **Dinâmica:** trabalhe individualmente por 20 minutos; troque a ficha com
            uma dupla por 15 minutos; revise-a por 10 minutos a partir do parecer.

            ### Parte A — evidências FAIR

            Use a auditoria como ponto de partida. Para cada princípio, registre uma
            evidência existente, uma lacuna e uma ação possível. Não atribua nota
            numérica.

            | Princípio | Evidência | Lacuna | Ação ou decisão |
            |---|---|---|---|
            | F | Escreva aqui | Escreva aqui | Escreva aqui |
            | A | Escreva aqui | Escreva aqui | Escreva aqui |
            | I | Escreva aqui | Escreva aqui | Escreva aqui |
            | R | Escreva aqui | Escreva aqui | Escreva aqui |

            ### Parte B — governança e CARE

            **Os dados envolvem povos indígenas ou conhecimentos, territórios e
            patrimônio a eles relacionados? Que consulta fundamenta a resposta?**
            Escreva aqui.

            **Quem se beneficia e quem pode autorizar ou recusar usos?** Escreva aqui.

            **Que responsabilidades continuarão após a coleta ou publicação?**
            Escreva aqui.

            **Que riscos e usos futuros precisam ser avaliados pelas pessoas ou
            comunidades afetadas?** Escreva aqui.

            ### Parte C — minidatasheet

            **Motivação e responsáveis:** Escreva aqui.

            **Composição, cobertura e lacunas:** Escreva aqui.

            **Coleta e processamento previstos:** Escreva aqui.

            **Usos recomendados e usos inadequados:** Escreva aqui.

            **Distribuição, acesso e licença:** Escreva aqui.

            **Manutenção, contato e versionamento:** Escreva aqui.

            ### Parte D — parecer da dupla e revisão

            O colega deve localizar: uma afirmação sem evidência; uma condição de
            acesso confundida com licença; uma pessoa ou coletividade afetada ainda
            ausente; e um uso futuro que precisa ser limitado.

            **Parecer recebido:** Escreva aqui.

            **Mudança realizada e justificativa:** Escreva aqui.
            """
        ),
        texto(
            """
            ## 8. Síntese e leituras

            - FAIR orienta a encontrabilidade, o acesso, a interoperabilidade e o
              reuso de objetos digitais, inclusive por máquinas.
            - CARE recoloca povos indígenas, autoridade, relações, benefício e ética
              no centro da governança de dados.
            - *Datasheets* organizam a documentação reflexiva do ciclo de vida.
            - documentação não transforma uma decisão injusta em decisão justa;
              restrição justificada não torna automaticamente uma base mal gerida.

            **Leituras essenciais:** Wilkinson et al. (2016), Carroll et al. (2020) e
            Gebru et al. (2021). Dados bibliográficos e links: `referencias.md`.

            Leve a ficha revisada para o Notebook 05. Ela sustentará as decisões sobre
            documentação, acesso, governança, ética e usos do protocolo final.
            """
        ),
    ]


def oficina() -> list[dict]:
    return [
        texto(
            """
            # Oficina — Protocolo da base

            Este notebook é integralmente discursivo. Use Markdown para justificar o
            desenho da base do projeto iniciado na Unidade 1. Não invente uma fonte
            apenas para preencher o roteiro: registre incerteza e um plano de
            verificação.

            O mapa abaixo funciona como orientação de preenchimento. Ele mostra que as
            seções não são formulários independentes: precisam sustentar umas às
            outras e retornar à revisão por pares.

            ![Pergunta, fontes, seleção, cobertura, documentação, responsabilidade e viabilidade convergem para um protocolo defensável, com retorno da revisão por pares.](imagens/05_protocolo_integrado.svg)

            Use as conexões para conferir coerência. Se a pergunta mudar, revise a
            unidade de análise, as fontes, os critérios, a cobertura e os riscos.
            """
        ),
        texto(
            """
            ## 1. Alinhamento

            **Pergunta delimitada:** Escreva aqui.

            **Finalidade e estrutura analítica:** Escreva aqui.

            **Unidade de análise:** Escreva aqui.

            **Que observações seriam necessárias para responder:** Escreva aqui.
            """
        ),
        texto(
            """
            ## 2. Fontes e cadeia de produção

            **Fontes primárias em relação à pergunta:** Escreva aqui.

            **Fontes secundárias e dados derivados:** Escreva aqui.

            **Instituições, produtores e custodiantes:** Escreva aqui.

            **Finalidade original dos registros e categorias herdadas:** Escreva aqui.

            **Condições materiais e técnicas de acesso:** Escreva aqui.
            """
        ),
        texto(
            """
            ## 3. População, corpus e seleção

            **População de interesse:** Escreva aqui.

            **População acessível:** Escreva aqui.

            **Corpus previsto:** Escreva aqui.

            | Critério | Campo/evidência | Regra | Justificativa | Caso limítrofe |
            |---|---|---|---|---|
            | inclusão | Escreva aqui | Escreva aqui | Escreva aqui | Escreva aqui |
            | exclusão | Escreva aqui | Escreva aqui | Escreva aqui | Escreva aqui |

            **Registro das exclusões:** Escreva aqui.
            """
        ),
        texto(
            """
            ## 4. Cobertura, vieses e silêncios

            | Dimensão | Cobertura | Lacuna | Efeito sobre a análise | Mitigação |
            |---|---|---|---|---|
            | temporal | Escreva aqui | Escreva aqui | Escreva aqui | Escreva aqui |
            | espacial | Escreva aqui | Escreva aqui | Escreva aqui | Escreva aqui |
            | social | Escreva aqui | Escreva aqui | Escreva aqui | Escreva aqui |
            | institucional | Escreva aqui | Escreva aqui | Escreva aqui | Escreva aqui |
            | documental | Escreva aqui | Escreva aqui | Escreva aqui | Escreva aqui |

            **Possíveis mecanismos de viés de seleção:** Escreva aqui.

            **Silêncios não redutíveis a valores ausentes:** Escreva aqui.

            **Limites das afirmações:** Escreva aqui.
            """
        ),
        texto(
            """
            ## 5. Metadados, identificadores e proveniência

            **Identificador, escopo e persistência:** Escreva aqui.

            | Campo | Definição | Tipo/domínio | Origem | Regra | Limitação |
            |---|---|---|---|---|---|
            | Escreva aqui | Escreva aqui | Escreva aqui | Escreva aqui | Escreva aqui | Escreva aqui |

            **Metadados administrativos e de direitos:** Escreva aqui.

            **Como a fonte será ligada ao registro derivado:** Escreva aqui.

            **Versão, data de acesso, agente e transformações:** Escreva aqui.
            """
        ),
        texto(
            """
            ## 6. Governança, reuso, ética e questões legais

            Acesso público não significa ausência de responsabilidade. Identifique,
            sem emitir parecer jurídico:

            **Evidências e lacunas FAIR prioritárias:** Escreva aqui.

            **Forma de acesso, licença ou termos de reutilização:** Escreva aqui.

            **Usos recomendados e usos que devem ser evitados:** Escreva aqui.

            **Responsável pelo datasheet, manutenção e novas versões:** Escreva aqui.

            **Dados pessoais ou pessoais sensíveis possíveis:** Escreva aqui.

            **Pessoas ou comunidades potencialmente afetadas:** Escreva aqui.

            **CARE é pertinente ao caso? Se houver dados indígenas, como benefício,
            autoridade, responsabilidade e ética serão definidos com os povos
            envolvidos?** Escreva aqui.

            **Necessidade de avaliação pelo sistema de ética da instituição:** Escreva aqui.

            **Finalidade, minimização, segurança e controle de acesso:** Escreva aqui.

            **Direitos autorais, licença, termos de uso e autorização:** Escreva aqui.

            **Forma de publicação e risco de reidentificação:** Escreva aqui.

            Para situações concretas, consulte a instituição, o comitê de ética, a
            ANPD e assessoria jurídica quando aplicável. O guia da ANPD não possui
            caráter normativo e não substitui a legislação.
            """
        ),
        texto(
            """
            ## 7. Viabilidade e contingência

            **Estimativa de volume e trabalho de coleta:** Escreva aqui.

            **Amostra piloto:** Escreva aqui.

            **Dependências de autorização ou infraestrutura:** Escreva aqui.

            **Plano B se a principal fonte não puder ser usada:** Escreva aqui.

            **O que será deliberadamente deixado de fora:** Escreva aqui.
            """
        ),
        texto(
            """
            ## 8. Rubrica de autoavaliação

            Atribua 0 (ausente), 1 (parcial) ou 2 (defensável) e justifique.

            | Critério | Nota | Evidência ou revisão necessária |
            |---|---:|---|
            | alinhamento entre pergunta e dados |  | Escreva aqui |
            | seleção reproduzível |  | Escreva aqui |
            | cobertura e vieses |  | Escreva aqui |
            | metadados e identificadores |  | Escreva aqui |
            | proveniência |  | Escreva aqui |
            | governança, reuso, ética e questões legais |  | Escreva aqui |
            | viabilidade |  | Escreva aqui |

            **Decisão:** manter, reformular ou abandonar esta proposta de base?
            Justifique. Escreva aqui.
            """
        ),
        texto(
            """
            ## 9. Revisão por pares

            O colega deve localizar no protocolo:

            1. uma escolha bem fundamentada;
            2. uma exclusão que possa alterar as conclusões;
            3. um campo ou metadado ainda ambíguo;
            4. um risco ético ou legal que precise de verificação;
            5. uma afirmação que exceda a cobertura.

            **Parecer recebido:** Escreva aqui.

            **Mudanças realizadas e justificativa:** Escreva aqui.
            """
        ),
        texto(
            """
            ## Entrega

            O protocolo é um documento vivo. Na Unidade 3, ele orientará a importação,
            estruturação, limpeza e integração das fontes. Guarde distinções entre:
            limite documental, decisão de seleção e problema técnico — cada um exige
            resposta diferente.

            **Referências efetivamente utilizadas no protocolo:** Escreva aqui.
            """
        ),
    ]


def criar_readme() -> None:
    links = tabela_links_colab(
        UNIDADE.name,
        (
            ("Guia da unidade", "00_guia_da_unidade.ipynb"),
            ("Fontes, população e seleção", "01_fontes_populacao_e_selecao.ipynb"),
            ("Cobertura, vieses e silêncios", "02_cobertura_vieses_e_silencios.ipynb"),
            ("Metadados, identificadores e proveniência", "03_metadados_identificadores_e_proveniencia.ipynb"),
            ("Governança, reuso e documentação", "04_governanca_reuso_e_documentacao_de_bases.ipynb"),
            ("Oficina do protocolo", "05_oficina_protocolo_da_base.ipynb"),
        ),
    )
    conteudo = """
    # Unidade 2 — Construção e documentação da base

    Material teórico-prático da segunda unidade de **Computação Aplicada a
    Problemas em Humanidades Digitais**.

    ## Ordem de estudo

    1. `00_guia_da_unidade.ipynb`
    2. `01_fontes_populacao_e_selecao.ipynb`
    3. `02_cobertura_vieses_e_silencios.ipynb`
    4. `03_metadados_identificadores_e_proveniencia.ipynb`
    5. `04_governanca_reuso_e_documentacao_de_bases.ipynb`
    6. `05_oficina_protocolo_da_base.ipynb`
    7. `exercicios_unidade_02_texto.md`
    8. `referencias.md`

    ## Abrir os notebooks no Google Colab

    __LINKS_COLAB__

    O link carrega o notebook diretamente do GitHub. Nos Notebooks 00 a 04,
    execute primeiro a célula **Preparação do ambiente**; ela clona o
    repositório no ambiente temporário e posiciona a execução nesta unidade. O
    Notebook 05 é discursivo e não precisa de clonagem.

    ## Dependências e dados

    Requer Python 3 e pandas. Os exemplos funcionam offline. Todos os registros
    em `dados/` são fictícios e contêm lacunas deliberadas; não sustentam
    afirmações sobre instituições ou processos históricos reais.

    A pasta `imagens/` reúne uma abertura conceitual e oito diagramas acessíveis.
    Os arquivos são locais, funcionam offline e têm finalidade, proveniência e
    textos alternativos documentados em `imagens/README.md`.

    ## Carga sugerida

    Duas semanas, oito horas no total, incluindo preparação e revisão. A oficina
    produz o protocolo da base do projeto iniciado na Unidade 1.

    O arquivo `exercicios_unidade_02_texto.md` contém 21 questões de múltipla
    escolha. As respostas e justificativas ficam no gabarito correspondente.

    ## Material do docente e revisão

    `gabaritos/` reúne respostas-modelo e rubricas. `revisores/` define seis
    perspectivas de avaliação e contém os pareceres executados. Os modelos das
    atividades abertas orientam a correção, mas não constituem respostas únicas.

    ## Limite de escopo

    A unidade diagnostica problemas de formato, valores e duplicatas, mas não
    ensina sua correção. Limpeza, padronização e integração pertencem à Unidade 3.

    ## Execução

    A partir da raiz:

    ```bash
    jupyter lab unidade_02
    ```

    Execute as células na ordem. Respostas e justificativas pertencem às células
    Markdown; Python é usado apenas para experimentos e auditorias.
    """
    conteudo = dedent(conteudo).replace("__LINKS_COLAB__", links)
    (UNIDADE / "README.md").write_text(conteudo.strip() + "\n", encoding="utf-8")


def main() -> None:
    UNIDADE.mkdir(exist_ok=True)
    criar_dados()
    criar_imagens()
    salvar_notebook("00_guia_da_unidade.ipynb", guia(), requer_repositorio=True)
    salvar_notebook(
        "01_fontes_populacao_e_selecao.ipynb",
        fontes_selecao(),
        requer_repositorio=True,
    )
    salvar_notebook(
        "02_cobertura_vieses_e_silencios.ipynb",
        cobertura(),
        requer_repositorio=True,
    )
    salvar_notebook(
        "03_metadados_identificadores_e_proveniencia.ipynb",
        metadados(),
        requer_repositorio=True,
    )
    salvar_notebook(
        "04_governanca_reuso_e_documentacao_de_bases.ipynb",
        governanca_documentacao(),
        requer_repositorio=True,
    )
    salvar_notebook("05_oficina_protocolo_da_base.ipynb", oficina())
    criar_readme()
    print(f"Unidade 2 construída em: {UNIDADE}")


if __name__ == "__main__":
    main()
