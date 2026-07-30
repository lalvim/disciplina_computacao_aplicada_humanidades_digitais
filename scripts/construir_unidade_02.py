"""Gera notebooks, dados didáticos e README da Unidade 2."""

from __future__ import annotations

import csv
import json
from pathlib import Path
from textwrap import dedent


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


def salvar_notebook(nome: str, celulas: list[dict]) -> None:
    documento = {
        "cells": celulas,
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
            5. reconhecer responsabilidades éticas e questões legais;
            6. produzir o protocolo da base do seu projeto.
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
            | 04 | O desenho da base é defensável? | Protocolo completo |

            Os dados são **inteiramente fictícios**. As lacunas foram criadas para
            permitir experimentos sem fazer afirmações sobre acervos reais.
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
            """
        ),
        texto(
            """
            ## 2. Fonte primária, secundária e dado derivado

            “Primária” e “secundária” descrevem a relação entre material e pergunta,
            não uma qualidade fixa do arquivo. Um catálogo institucional pode ser
            fonte secundária para estudar cartas, mas fonte primária para investigar
            práticas de catalogação. Uma tabela criada por transcrição é dado derivado
            e deve permanecer ligada ao documento e às decisões que a produziram.

            Fontes governamentais, institucionais e documentais exigem perguntas
            distintas: quem produziu o registro, com qual finalidade, sob quais
            categorias e com que condições de acesso?
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
            ## Perspectiva ética

            Mais dados não são sempre a resposta. Os princípios CARE (Carroll et al.,
            2020) lembram que dados relativos a povos indígenas envolvem benefício
            coletivo, autoridade para controlar, responsabilidade e ética. Acesso
            técnico não elimina direitos, interesses comunitários ou contextos de
            governança.

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

            Gebru et al. (2021) propõem *datasheets* que documentam motivação,
            composição, coleta, usos e manutenção. O modelo PROV-O do W3C oferece
            conceitos para representar entidades, atividades e agentes. Eles não
            substituem a descrição arquivística ou os padrões específicos do campo;
            oferecem perguntas para tornar decisões rastreáveis.

            Uma base auditável combina documentação legível por pessoas com
            verificações computacionais simples. Dados completos: `referencias.md`.
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
            ## 6. Ética e questões legais

            Acesso público não significa ausência de responsabilidade. Identifique,
            sem emitir parecer jurídico:

            **Dados pessoais ou pessoais sensíveis possíveis:** Escreva aqui.

            **Pessoas ou comunidades potencialmente afetadas:** Escreva aqui.

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
            | ética e questões legais |  | Escreva aqui |
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
    conteudo = """
    # Unidade 2 — Construção e documentação da base

    Material teórico-prático da segunda unidade de **Computação Aplicada a
    Problemas em Humanidades Digitais**.

    ## Ordem de estudo

    1. `00_guia_da_unidade.ipynb`
    2. `01_fontes_populacao_e_selecao.ipynb`
    3. `02_cobertura_vieses_e_silencios.ipynb`
    4. `03_metadados_identificadores_e_proveniencia.ipynb`
    5. `04_oficina_protocolo_da_base.ipynb`
    6. `exercicios_unidade_02.html`
    7. `referencias.md`

    ## Dependências e dados

    Requer Python 3 e pandas. Os exemplos funcionam offline. Todos os registros
    em `dados/` são fictícios e contêm lacunas deliberadas; não sustentam
    afirmações sobre instituições ou processos históricos reais.

    ## Carga sugerida

    Duas semanas, oito horas no total, incluindo preparação e revisão. A oficina
    produz o protocolo da base do projeto iniciado na Unidade 1.

    O arquivo `exercicios_unidade_02.html` contém 18 questões com correção e
    funciona offline. Há uma versão textual equivalente.

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
    (UNIDADE / "README.md").write_text(dedent(conteudo).strip() + "\n", encoding="utf-8")


def main() -> None:
    UNIDADE.mkdir(exist_ok=True)
    criar_dados()
    salvar_notebook("00_guia_da_unidade.ipynb", guia())
    salvar_notebook("01_fontes_populacao_e_selecao.ipynb", fontes_selecao())
    salvar_notebook("02_cobertura_vieses_e_silencios.ipynb", cobertura())
    salvar_notebook(
        "03_metadados_identificadores_e_proveniencia.ipynb", metadados()
    )
    salvar_notebook("04_oficina_protocolo_da_base.ipynb", oficina())
    criar_readme()
    print(f"Unidade 2 construída em: {UNIDADE}")


if __name__ == "__main__":
    main()
