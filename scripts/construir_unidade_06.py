"""Constrói a Unidade 6 — associações, coocorrências e redes."""

from __future__ import annotations

import csv
import json
import random
from itertools import combinations
from pathlib import Path
from textwrap import dedent

from apoio_colab import adicionar_link_na_abertura, preparacao_colab, tabela_links_colab


RAIZ = Path(__file__).resolve().parents[1]
UNIDADE = RAIZ / "unidade_06"
DADOS = UNIDADE / "dados"


def md(valor: str) -> dict:
    texto = dedent(valor).strip()
    texto = "\n".join("$$" if linha in {r"\[", r"\]"} else linha for linha in texto.splitlines())
    texto = texto.replace(r"\(", "$ ").replace(r"\)", " $")
    return {"cell_type": "markdown", "metadata": {}, "source": texto.splitlines(keepends=True)}


def code(valor: str) -> dict:
    return {"cell_type": "code", "execution_count": None, "metadata": {}, "outputs": [], "source": dedent(valor).strip().splitlines(keepends=True)}


def salvar_notebook(nome: str, celulas: list[dict], requer_dados: bool = True, networkx: bool = False) -> None:
    publicadas = [adicionar_link_na_abertura(celulas[0], UNIDADE.name, nome)]
    if requer_dados:
        pacotes = (("networkx", "networkx>=3,<4"),) if networkx else ()
        publicadas.append(code(preparacao_colab(UNIDADE.name, pacotes)))
    publicadas.extend(celulas[1:])
    documento = {
        "cells": publicadas,
        "metadata": {
            "kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"},
            "language_info": {"name": "python", "version": "3"},
        },
        "nbformat": 4,
        "nbformat_minor": 5,
    }
    (UNIDADE / nome).write_text(json.dumps(documento, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")


def criar_dados() -> None:
    DADOS.mkdir(parents=True, exist_ok=True)
    rng = random.Random(20261022)
    linhas = []
    for i in range(80):
        ano = 1890 + i % 20
        periodo = "1890–1899" if ano < 1900 else "1900–1909"
        local = "Capital" if i % 4 in (0, 1) else "Interior"
        genero = ("editorial", "notícia", "carta")[i % 3]
        prob_educacao = 0.18 + (0.42 if ano >= 1900 else 0) + (0.10 if genero == "editorial" else 0)
        tema_educacao = "sim" if rng.random() < prob_educacao else "não"
        prob_ilustracao = 0.18 + (0.23 if ano >= 1900 else 0) + (0.12 if local == "Capital" else 0)
        tem_ilustracao = "sim" if rng.random() < prob_ilustracao else "não"
        extensao = int(340 + (90 if genero == "editorial" else 0) + (60 if local == "Capital" else 0) + rng.gauss(0, 85))
        referencias = max(0, round(0.0045 * extensao + (1 if tema_educacao == "sim" else 0) + rng.gauss(0, 0.9)))
        circulacao = int(450 + 1.55 * extensao + (420 if local == "Capital" else 0) + (180 if ano >= 1900 else 0) + rng.gauss(0, 150))
        qualidade = max(45, min(99, round(73 + (8 if ano >= 1900 else 0) + rng.gauss(0, 7), 1)))
        linhas.append([f"R{i+1:03d}", ano, periodo, local, genero, tema_educacao, tem_ilustracao, extensao, referencias, circulacao, qualidade])
    campos = ["id_registro", "ano", "periodo", "local", "genero", "tema_educacao", "tem_ilustracao", "extensao_palavras", "referencias_instituicoes", "circulacao_estimada", "qualidade_ocr_pct"]
    with (DADOS / "registros_associacao.csv").open("w", encoding="utf-8", newline="") as f:
        w = csv.writer(f); w.writerow(campos); w.writerows(linhas)

    conjuntos = [
        ["Ana F.", "Liga Aurora", "Escola Livre"], ["Bento R.", "Liga Aurora", "Sindicato Norte"],
        ["Ana F.", "Jornal Horizonte", "Escola Livre"], ["Caio M.", "Sindicato Norte", "Jornal Horizonte"],
        ["Bento R.", "Biblioteca Popular", "Escola Livre"], ["Dora S.", "Biblioteca Popular", "Círculo Sul"],
        ["Eva L.", "Círculo Sul", "Teatro União"], ["Dora S.", "Jornal Horizonte", "Teatro União"],
        ["Fábio C.", "Cooperativa Leste", "Teatro União"], ["Eva L.", "Cooperativa Leste", "Círculo Sul"],
        ["Ana F.", "Liga Aurora", "Biblioteca Popular"], ["Caio M.", "Sindicato Norte", "Escola Livre"],
        ["Bento R.", "Jornal Horizonte", "Liga Aurora"], ["Dora S.", "Círculo Sul", "Biblioteca Popular"],
        ["Eva L.", "Teatro União", "Jornal Horizonte"], ["Fábio C.", "Cooperativa Leste", "Círculo Sul"],
        ["Ana F.", "Escola Livre", "Sindicato Norte"], ["Caio M.", "Jornal Horizonte", "Liga Aurora"],
        ["Dora S.", "Biblioteca Popular", "Jornal Horizonte"], ["Fábio C.", "Teatro União", "Cooperativa Leste"],
        ["Bento R.", "Liga Aurora", "Escola Livre"], ["Eva L.", "Círculo Sul", "Jornal Horizonte"],
        ["Caio M.", "Sindicato Norte", "Liga Aurora"], ["Fábio C.", "Cooperativa Leste", "Biblioteca Popular"],
    ]
    rel = []
    for i, entidades in enumerate(conjuntos, 1):
        rel.append([f"D{i:03d}", 1894 + i % 12, "Capital" if i % 2 else "Interior", ";".join(entidades), "documento fictício para demonstração de coocorrência"])
    with (DADOS / "documentos_entidades.csv").open("w", encoding="utf-8", newline="") as f:
        w = csv.writer(f); w.writerow(["id_documento", "ano", "local", "entidades", "nota"]); w.writerows(rel)

    arestas = []
    pessoas = ["Ana F.", "Bento R.", "Caio M.", "Dora S.", "Eva L.", "Fábio C."]
    for i in range(12):
        arestas.append([pessoas[i % 6], pessoas[(i * 2 + 1) % 6], 1895 + i, 1 + i % 3])
    with (DADOS / "correspondencia_direta.csv").open("w", encoding="utf-8", newline="") as f:
        w = csv.writer(f); w.writerow(["remetente", "destinatario", "ano", "cartas"]); w.writerows(arestas)

    proveniencia = {
        "natureza": "dados inteiramente fictícios",
        "registros_associacao.csv": "80 registros simulados para associação categórica e numérica",
        "documentos_entidades.csv": "24 documentos inventados com entidades separadas por ponto e vírgula",
        "correspondencia_direta.csv": "12 relações dirigidas inventadas para distinguir vínculo observado de coocorrência",
        "limite": "não sustenta afirmações históricas, sociais ou institucionais reais",
    }
    (DADOS / "proveniencia.json").write_text(json.dumps(proveniencia, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def criar_svg(nome: str, titulo: str, descricao: str, etapas: list[str]) -> None:
    largura = 980
    n = len(etapas)
    w = 250 if n <= 3 else 190
    gap = (largura - 80 - n * w) / max(1, n - 1)
    caixas = []
    for i, etapa in enumerate(etapas):
        x = 40 + i * (w + gap)
        caixas.append(f'<rect x="{x:.0f}" y="90" width="{w}" height="105" rx="14" fill="#f4f0e6" stroke="#294c60" stroke-width="2"/><text x="{x+w/2:.0f}" y="135" text-anchor="middle" font-size="18" fill="#172b35">{etapa}</text>')
        if i < n - 1:
            x2 = x + w
            caixas.append(f'<path d="M{x2+8:.0f} 142 H{x2+gap-10:.0f}" stroke="#a44a3f" stroke-width="3" marker-end="url(#a)"/>')
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{largura}" height="280" viewBox="0 0 {largura} 280" role="img" aria-labelledby="title desc"><title id="title">{titulo}</title><desc id="desc">{descricao}</desc><defs><marker id="a" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L0,6 L9,3 z" fill="#a44a3f"/></marker></defs><rect width="100%" height="100%" fill="#fffdf8"/><text x="490" y="42" text-anchor="middle" font-size="25" font-weight="bold" fill="#172b35">{titulo}</text>{''.join(caixas)}<text x="490" y="242" text-anchor="middle" font-size="16" fill="#46565e">Toda relação depende da regra que produziu os dados.</text></svg>'''
    (UNIDADE / "imagens" / nome).write_text(svg, encoding="utf-8")


def guia() -> list[dict]:
    return [md('''
    # Unidade 6 — Guia de estudo
    ## Como investigar relações entre características?

    **Problema orientador:** como verificar se variáveis, palavras, pessoas,
    instituições ou conceitos estão relacionados?

    A Unidade 5 comparou grupos e documentos. Agora mudamos a pergunta: em vez de
    perguntar apenas “A difere de B?”, examinaremos se duas características variam
    juntas ou se entidades estão conectadas segundo uma regra documentada. Relação
    observada não é sinônimo de explicação, influência ou causalidade.

    ![O percurso parte da pergunta, explicita a regra da relação, calcula uma medida e retorna aos casos.](imagens/00_percurso_associacao.svg)
    ''') , md('''
    ## Objetivos e percurso

    | Notebook | Pergunta | Produto de aprendizagem |
    |---|---|---|
    | 00 | Que tipo de relação está sendo afirmada? | diagnóstico inicial |
    | 01 | Duas categorias aparecem associadas? | tabela condicionada e medida |
    | 02 | Duas quantidades variam juntas? | correlação com sensibilidade |
    | 03 | Como documentos produzem relações? | matriz e lista de arestas |
    | 04 | O que a posição em um grafo permite interpretar? | leitura estrutural |
    | 05 | Qual percurso serve ao projeto? | incremento no relatório-notebook |

    Os dois percursos convergem numa regra: defina unidades, direção, peso e universo
    antes de calcular; depois inspecione casos e limite a afirmação.
    ''') , code('''
    import json
    import pandas as pd

    proveniencia = json.loads(open("dados/proveniencia.json", encoding="utf-8").read())
    associacao = pd.read_csv("dados/registros_associacao.csv")
    relacional = pd.read_csv("dados/documentos_entidades.csv")
    print("Natureza:", proveniencia["natureza"])
    print("Registros associativos:", len(associacao))
    print("Documentos relacionais:", len(relacional))
    associacao.head(3)
    ''') , md('''
    ## U06-A01 — Discussão em duplas — que relação está sendo afirmada?

    **Dinâmica (15 minutos):** cada dupla escolhe uma frase e identifica unidades,
    variáveis ou entidades, regra da relação, alternativa plausível e limite causal.

    1. “Textos mais longos citam mais instituições.”
    2. “Educação tornou-se mais central porque a circulação cresceu.”
    3. “Duas instituições são próximas porque aparecem no mesmo documento.”

    Registre uma reformulação descritiva defensável e compartilhe com outra dupla.

    **Resposta:** Escreva aqui.

    ## Passagem

    O diagnóstico separou associação estatística, coocorrência documental e nexo
    causal. O Notebook 01 começa pelo caso categórico, no qual os denominadores são
    tão importantes quanto as contagens.
    ''')]


def categoricas() -> list[dict]:
    return [md('''
    # Associação entre variáveis categóricas

    Uma tabela cruzada conta combinações de categorias. Para interpretar associação,
    precisamos comparar proporções condicionais e explicitar qual variável define o
    denominador. Contagens maiores podem resultar apenas de grupos maiores.

    ![Contagens observadas passam a proporções condicionais, valores esperados e uma medida de associação.](imagens/01_tabela_condicional.svg)
    '''), code('''
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt

    dados = pd.read_csv("dados/registros_associacao.csv")
    tabela = pd.crosstab(dados["periodo"], dados["tema_educacao"])
    proporcoes_linha = pd.crosstab(
        dados["periodo"], dados["tema_educacao"], normalize="index"
    )
    display(tabela)
    display((100 * proporcoes_linha).round(1))
    '''), md('''
    ## 2. Da independência esperada à discrepância observada

    Sob independência, a frequência esperada de uma célula é o produto dos totais de
    sua linha e coluna dividido pelo total geral:

    $$E_{ij}=\\frac{n_{i\\cdot}n_{\\cdot j}}{n}$$

    A estatística qui-quadrado resume discrepâncias; o $V$ de Cramér a normaliza entre
    0 e 1. Nenhuma delas informa direção causal ou importância histórica.
    '''), code('''
    observada = tabela.to_numpy(dtype=float)
    esperada = np.outer(observada.sum(axis=1), observada.sum(axis=0)) / observada.sum()
    qui_quadrado = ((observada - esperada) ** 2 / esperada).sum()
    n = observada.sum()
    k = min(observada.shape)
    v_cramer = np.sqrt(qui_quadrado / (n * (k - 1)))
    display(pd.DataFrame(esperada, index=tabela.index, columns=tabela.columns).round(2))
    print(f"Qui-quadrado descritivo: {qui_quadrado:.3f}")
    print(f"V de Cramér: {v_cramer:.3f}")

    (100 * proporcoes_linha["sim"]).plot.bar(color="#5a7d8c")
    plt.ylabel("Documentos com tema educação (%)")
    plt.xlabel("Período")
    plt.title("Proporção condicionada pelo período — dados fictícios")
    plt.xticks(rotation=0); plt.ylim(0, 100); plt.tight_layout(); plt.show()
    '''), md('''
    A tabela e o gráfico descrevem este conjunto fictício. Antes de atribuir a
    diferença ao tempo, seria necessário examinar gênero, local, seleção do corpus e
    mudança na classificação. O $V$ resume intensidade no arranjo observado, não uma
    escala universal de relevância.

    ## U06-A02 — Atividade integrada — tabela associativa documentada

    1. Escolha outro par categórico (`local`, `genero` ou `tem_ilustracao`).
    2. Produza contagens e proporções com denominador explícito.
    3. Calcule frequências esperadas e $V$ de Cramér.
    4. Inspecione ao menos quatro registros e escreva uma conclusão limitada.

    **Resposta e interpretação:** Escreva aqui.

    ## Passagem

    Categorias exigem tabelas condicionadas. Para quantidades, o próximo notebook
    examina forma, ordem, extremos e estratificação antes de resumir a associação.
    ''')]


def correlacao() -> list[dict]:
    return [md('''
    # Correlação, forma e causalidade

    Correlação de Pearson resume associação **linear**; Spearman calcula Pearson
    sobre postos e resume associação **monotônica**. Ambas variam de -1 a 1, mas um
    coeficiente isolado pode ocultar curvas, grupos, extremos e variáveis de confusão.

    $$r=\\frac{\\sum_i(x_i-\\bar{x})(y_i-\\bar{y})}{\\sqrt{\\sum_i(x_i-\\bar{x})^2\\sum_i(y_i-\\bar{y})^2}}$$
    ''') , code('''
    import pandas as pd
    import matplotlib.pyplot as plt

    dados = pd.read_csv("dados/registros_associacao.csv")
    x = dados["extensao_palavras"]
    y = dados["referencias_instituicoes"]
    pearson = x.corr(y)
    spearman = x.rank(method="average").corr(y.rank(method="average"))
    print(f"Pearson: {pearson:.3f}")
    print(f"Spearman: {spearman:.3f}")

    cores = dados["local"].map({"Capital": "#a44a3f", "Interior": "#4c768b"})
    plt.figure(figsize=(7, 4.5))
    plt.scatter(x, y, c=cores, alpha=.75)
    plt.xlabel("Extensão do documento (palavras)")
    plt.ylabel("Referências a instituições")
    plt.title("Forma e grupos antes do coeficiente — dados fictícios")
    plt.tight_layout(); plt.show()
    ''') , md('''
    ## 2. Sensibilidade, estratificação e confundimento

    Um coeficiente agregado combina relações internas e diferenças entre grupos.
    Recalcularemos por local e sem o registro de maior circulação. A finalidade não é
    escolher o número preferido, mas entender de que decisões ele depende.
    ''') , code('''
    por_local = dados.groupby("local").apply(
        lambda g: pd.Series({
            "n": len(g),
            "Pearson": g["extensao_palavras"].corr(g["referencias_instituicoes"]),
            "Spearman": g["extensao_palavras"].rank().corr(g["referencias_instituicoes"].rank()),
        }), include_groups=False
    )
    sem_extremo = dados.drop(dados["circulacao_estimada"].idxmax())
    sensibilidade = pd.Series({
        "Pearson completo": pearson,
        "Pearson sem maior circulação": sem_extremo["extensao_palavras"].corr(sem_extremo["referencias_instituicoes"]),
    })
    display(por_local.round(3)); display(sensibilidade.round(3).to_frame("coeficiente"))
    ''') , md('''
    ![Associação observada pode refletir direção causal, causa reversa, fator comum, seleção ou coincidência.](imagens/02_correlacao_causalidade.svg)

    Correlação não estabelece temporalidade, mecanismo, ausência de confundimento ou
    efeito de intervenção. A expressão “X causa Y” exige desenho e evidências além do
    coeficiente. Correlações espúrias também podem surgir de tendências temporais,
    testes múltiplos ou seleção posterior das variáveis.

    ## U06-A03 — Atividade integrada — correlação com auditoria

    Analise `qualidade_ocr_pct` e `ano`, ou `circulacao_estimada` e
    `extensao_palavras`. Apresente gráfico, Pearson, Spearman, estratificação por um
    grupo, sensibilidade a um extremo e três explicações rivais.

    **Resposta:** Escreva aqui.

    ## Passagem

    Até aqui a relação existia entre colunas. O Notebook 03 mostra como documentos
    podem ser transformados em relações entre entidades — uma mudança de ontologia,
    não apenas de formato.
    ''')]


def coocorrencia() -> list[dict]:
    return [md('''
    # Coocorrência e matrizes relacionais

    Coocorrência significa que duas entidades satisfazem uma regra de contexto — por
    exemplo, aparecem no mesmo documento. Isso não prova contato, colaboração ou
    afinidade. A janela e a unidade documental definem a relação.

    ## 1. Palavras: a janela define o contexto

    Em textos, duas palavras podem coocorrer na mesma frase, parágrafo, documento ou
    dentro de uma janela de $k$ posições. Janelas menores aproximam contexto local;
    documentos inteiros misturam passagens distintas. Remoção de palavras frequentes,
    lematização e repetição dentro da janela também alteram as arestas.

    | Relação | Nós | Regra de aresta | Direção possível |
    |---|---|---|---|
    | palavras | termos | mesma janela/frase/documento | normalmente não dirigida |
    | entidades | pessoas/instituições | mesma unidade documental | normalmente não dirigida |
    | correspondência | pessoas/instituições | remessa registrada | remetente → destinatário |
    | citação | obras/autores | referência registrada | citante → citado |
    | personagens | personagens | fala, interação ou mesma cena | depende da regra |

    ![Uma matriz documento-entidade é projetada em uma matriz entidade-entidade, com perda de contexto.](imagens/03_projecao_bipartida.svg)
    '''), code('''
    from collections import Counter
    from itertools import combinations
    import numpy as np
    import pandas as pd

    tokens = "educação trabalho associação biblioteca educação curso".split()
    janela = 2
    pares_palavras = Counter()
    for i, palavra in enumerate(tokens):
        for vizinha in tokens[i + 1:i + 1 + janela]:
            pares_palavras[tuple(sorted((palavra, vizinha)))] += 1
    display(pd.DataFrame(
        [(a, b, peso) for (a, b), peso in pares_palavras.items()],
        columns=["palavra_a", "palavra_b", "peso"],
    ).sort_values("peso", ascending=False))

    # Agora mudamos de palavras para entidades por documento.
    documentos = pd.read_csv("dados/documentos_entidades.csv")
    mencoes = documentos.assign(entidade=documentos["entidades"].str.split(";")).explode("entidade")
    incidencia = pd.crosstab(mencoes["id_documento"], mencoes["entidade"]).astype(int)
    display(mencoes.head(8))
    display(incidencia.iloc[:6, :7])
    ''') , md('''
    ## 2. Projetar documentos em pares de entidades

    Se $B$ é a matriz documento-entidade, $B^TB$ conta quantos documentos cada par
    compartilha. A diagonal conta documentos por entidade e deve ser separada quando
    o objetivo são arestas entre entidades.

    $$W=B^TB$$
    ''') , code('''
    matriz_coocorrencia = incidencia.T @ incidencia
    np.fill_diagonal(matriz_coocorrencia.values, 0)
    entidades = matriz_coocorrencia.index.tolist()
    arestas = pd.DataFrame(
        [
            (entidades[i], entidades[j], int(matriz_coocorrencia.iat[i, j]))
            for i in range(len(entidades))
            for j in range(i + 1, len(entidades))
            if matriz_coocorrencia.iat[i, j] > 0
        ],
        columns=["origem", "destino", "peso"],
    ).sort_values(["peso", "origem"], ascending=[False, True]).reset_index(drop=True)
    display(arestas.head(12))
    ''') , md('''
    A projeção simplifica uma **rede bipartida**: depois dela, nem sempre sabemos
    quais documentos produziram cada peso. Preserve a tabela de menções e retorne aos
    registros. Documentos com muitas entidades também geram muitos pares e podem
    dominar a rede.

    ## 3. Coocorrência não é correspondência

    `correspondencia_direta.csv` contém remetente e destinatário: é uma relação
    dirigida observada no modelo dos dados. A coocorrência é simétrica e construída
    pelo analista. As duas redes não são intercambiáveis.

    ## U06-A04 — Atividade integrada — matriz relacional auditável

    Altere o recorte por período ou local, reconstrua incidência, matriz e arestas,
    compare os cinco pares mais fortes e recupere os documentos que sustentam um par.
    Explique o que “peso” significa e o que não significa.

    **Resposta:** Escreva aqui.

    ## Passagem

    Temos agora uma lista de nós e arestas com proveniência. O Notebook 04 usa o
    grafo como modelo analítico, sem transformar posição estrutural em importância
    histórica automática.
    ''')]


def grafos() -> list[dict]:
    return [md('''
    # Grafos, centralidades e comunidades

    Um grafo reúne nós e arestas; ambos podem ter atributos, direção e peso. Grau
    conta vizinhos, força soma pesos e intermediação resume participação em caminhos
    mínimos. Cada medida responde a uma pergunta estrutural distinta.

    ![Grau, força e intermediação destacam propriedades diferentes do mesmo grafo.](imagens/04_centralidades.svg)
    ''') , code('''
    import networkx as nx
    import pandas as pd
    import matplotlib.pyplot as plt

    arestas = pd.read_csv("dados/arestas_coocorrencia.csv")
    grafo = nx.from_pandas_edgelist(
        arestas, source="origem", target="destino", edge_attr="peso"
    )
    print("Nós:", grafo.number_of_nodes(), "Arestas:", grafo.number_of_edges())
    ''') , md('''
    ## 2. Medidas como perguntas

    - **grau:** com quantos nós diferentes esta entidade coocorre?
    - **força:** quantas coocorrências ponderadas incidem sobre ela?
    - **intermediação:** em quantos caminhos mínimos ela ocupa posição intermediária?

    Para um grafo não dirigido com $n$ nós, o grau normalizado é
    $C_D(v)=deg(v)/(n-1)$; a força é $s(v)=\\sum_u w_{vu}$. As fórmulas deixam claro
    que vizinhos diferentes e repetição de vínculos não são a mesma propriedade.

    Peso de coocorrência representa repetição documental, não confiança, influência
    ou intensidade social.
    ''') , code('''
    grau = nx.degree_centrality(grafo)
    forca = dict(grafo.degree(weight="peso"))
    intermediacao = nx.betweenness_centrality(grafo, weight=None)
    metricas = pd.DataFrame({
        "grau_normalizado": pd.Series(grau),
        "forca": pd.Series(forca),
        "intermediacao": pd.Series(intermediacao),
    }).sort_values("forca", ascending=False)
    display(metricas.round(3))

    comunidades = list(nx.community.greedy_modularity_communities(grafo, weight="peso"))
    comunidade_de = {no: i + 1 for i, grupo in enumerate(comunidades) for no in grupo}
    metricas["comunidade_algoritmica"] = pd.Series(comunidade_de)
    display(metricas.sort_values(["comunidade_algoritmica", "forca"]))
    ''') , md('''
    Comunidades maximizam uma função estrutural sob escolhas algorítmicas; não são
    automaticamente grupos sociais reconhecidos. Estabilidade a recortes e retorno
    aos documentos são necessários antes de nomeá-las.
    ''') , code('''
    posicao = nx.spring_layout(grafo, seed=2026, weight="peso")
    tamanhos = [250 + 55 * forca[no] for no in grafo.nodes]
    cores = [comunidade_de[no] for no in grafo.nodes]
    larguras = [0.5 + grafo[u][v]["peso"] * 0.6 for u, v in grafo.edges]
    plt.figure(figsize=(10, 7))
    nx.draw_networkx(
        grafo, posicao, node_size=tamanhos, node_color=cores, cmap="Set2",
        width=larguras, edge_color="#999999", font_size=8
    )
    plt.title("Rede de coocorrência — dados inteiramente fictícios")
    plt.axis("off"); plt.tight_layout(); plt.show()
    ''') , md('''
    ## 3. Direção e atributos: correspondência não é coocorrência

    Uma carta registra remetente e destinatário. Esse modelo requer um `DiGraph`:
    grau de entrada e de saída respondem perguntas diferentes. Ano e quantidade de
    cartas são atributos das arestas; tipo de entidade pode ser atributo do nó.
    ''') , code('''
    correspondencia = pd.read_csv("dados/correspondencia_direta.csv")
    grafo_dirigido = nx.from_pandas_edgelist(
        correspondencia,
        source="remetente", target="destinatario",
        edge_attr=["ano", "cartas"], create_using=nx.DiGraph,
    )
    graus_dirigidos = pd.DataFrame({
        "saída": dict(grafo_dirigido.out_degree()),
        "entrada": dict(grafo_dirigido.in_degree()),
        "cartas_enviadas": dict(grafo_dirigido.out_degree(weight="cartas")),
        "cartas_recebidas": dict(grafo_dirigido.in_degree(weight="cartas")),
    }).fillna(0).astype(int)
    display(graus_dirigidos.sort_values("cartas_recebidas", ascending=False))
    ''') , md('''
    O desenho de força é uma disposição, não um mapa geográfico nem uma medida. A
    proximidade visual depende do algoritmo e da semente; leia métricas e documentos,
    não apenas a aparência.

    ## U06-A05 — Atividade integrada — leitura estrutural e retorno aos casos

    Escolha duas entidades com posições contrastantes. Compare grau, força e
    intermediação; identifique suas arestas principais; recupere três documentos que
    sustentam a interpretação; teste um limiar de peso e registre o que mudou.

    **Resposta:** Escreva aqui.

    ## Passagem

    As medidas ampliaram a descrição, mas não substituíram a crítica da relação. A
    oficina exige escolher apenas o percurso pertinente ao projeto e incorporá-lo ao
    mesmo relatório-notebook iniciado nas unidades anteriores.
    ''')]


def oficina() -> list[dict]:
    return [md('''
    # U06-A06 — Oficina — associação ou rede no relatório incremental

    Esta oficina **não cria uma entrega separada**. Abra o mesmo relatório-notebook
    do projeto, salve uma nova versão e acrescente uma seção da Unidade 6. Escolha
    somente um percurso principal:

    - **A — associação entre variáveis:** categórica ou numérica;
    - **B — rede:** relação direta ou coocorrência com regra documentada;
    - **C — não adoção fundamentada:** quando a base não contém relações defensáveis.

    ![Dados documentados passam por um modelo relacional, produzem um resultado e terminam em uma interpretação limitada.](imagens/05_cadeia_argumento.svg)
    '''), md('''
    ## 1. Pergunta e pertinência

    Escreva a pergunta relacional, a conexão com o argumento anterior e por que o
    percurso escolhido é adequado. **Resposta:** Escreva aqui.
    '''), md('''
    ## 2. Unidades e regra de construção

    Declare unidade, variáveis ou nós, arestas, direção, peso, recorte, ausências e
    versões da base. **Resposta:** Escreva aqui.
    '''), md('''
    ## 3. Código e resultado selecionado

    Inclua no relatório apenas o código necessário para reconstruir uma tabela e um
    gráfico ou rede. Antes da célula, formule a pergunta; depois, interprete a saída.
    **Plano:** Escreva aqui.
    '''), md('''
    ## 4. Sensibilidade e retorno aos casos

    Altere uma decisão relevante — estrato, extremo, janela, limiar ou peso — e
    recupere ao menos três casos/fontes. **Resultado:** Escreva aqui.
    '''), md('''
    ## 5. Afirmação e limites

    Escreva uma conclusão descritiva ou associativa. Separe claramente o que foi
    observado, o que foi inferido e o que não pode ser afirmado. **Resposta:** Escreva aqui.
    '''), md('''
    ## 6. Registro incremental

    Registre versão, seção acrescentada, arquivos modificados, decisões revistas e
    questão que seguirá para a Unidade 7. **Resposta:** Escreva aqui.
    '''), md('''
    ## U06-A07 — Revisão por pares — a relação resiste à auditoria?

    **Dinâmica (25 minutos):** troque o notebook com outra pessoa. O revisor deve
    localizar a regra da relação, tentar reconstruir um resultado, verificar a
    interpretação do gráfico, apontar uma alternativa e sugerir uma revisão. O autor
    registra o parecer e a mudança incorporada.

    **Parecer recebido e resposta:** Escreva aqui.
    '''), md('''
    ## Checklist da etapa

    - [ ] o mesmo relatório-notebook foi atualizado;
    - [ ] a relação e os denominadores estão definidos;
    - [ ] código, tabela/gráfico e análise formam uma sequência;
    - [ ] há sensibilidade e retorno aos casos;
    - [ ] causalidade não foi inferida indevidamente;
    - [ ] a próxima pergunta do projeto foi registrada.
    ''')]


def criar_arestas_derivadas() -> None:
    contagem: dict[tuple[str, str], int] = {}
    with (DADOS / "documentos_entidades.csv").open(encoding="utf-8") as f:
        for linha in csv.DictReader(f):
            entidades = sorted(set(linha["entidades"].split(";")))
            for a, b in combinations(entidades, 2):
                contagem[(a, b)] = contagem.get((a, b), 0) + 1
    with (DADOS / "arestas_coocorrencia.csv").open("w", encoding="utf-8", newline="") as f:
        w = csv.writer(f); w.writerow(["origem", "destino", "peso"])
        for (a, b), peso in sorted(contagem.items(), key=lambda x: (-x[1], x[0])):
            w.writerow([a, b, peso])


def criar_exercicios() -> None:
    questoes = [
        ("Em uma tabela cruzada, qual porcentagem responde melhor a 'entre os documentos de cada período, quantos tratam de educação'?", ["Percentual do total geral", "Percentual por linha, se período está nas linhas", "Percentual por coluna em qualquer arranjo", "Somente contagens"], "B"),
        ("O que indica V de Cramér próximo de zero?", ["Ausência de causalidade", "Associação categórica fraca no arranjo observado", "Igualdade das médias", "Erro de codificação"], "B"),
        ("Pearson é especialmente sensível a quê?", ["Ordem alfabética", "Relação linear e valores extremos", "Número de categorias nominais", "Direção das arestas"], "B"),
        ("Spearman é calculado principalmente a partir de quê?", ["Postos", "Frequências esperadas", "Caminhos mínimos", "TF-IDF"], "A"),
        ("Correlação positiva permite concluir que X causa Y?", ["Sempre", "Somente se r > 0,8", "Não, sem desenho e evidências causais", "Sim, se o gráfico for linear"], "C"),
        ("Qual procedimento ajuda a detectar confundimento?", ["Ocultar grupos", "Estratificar por uma terceira variável justificada", "Arredondar coeficientes", "Remover todos os extremos"], "B"),
        ("Em uma rede de coocorrência documental, uma aresta significa quê?", ["Contato comprovado", "Compartilhamento da unidade definida", "Causalidade", "Amizade"], "B"),
        ("O peso de uma aresta de coocorrência deste material representa quê?", ["Número de documentos compartilhados", "Importância histórica", "Distância geográfica", "Confiança"], "A"),
        ("Qual estrutura preserva documentos e entidades como tipos distintos de nó?", ["Rede bipartida", "Histograma", "Tabela de médias", "Árvore causal"], "A"),
        ("O que se perde ao projetar uma matriz documento-entidade?", ["Todos os nomes", "Parte do contexto documental que gerou cada par", "Todos os pesos", "A possibilidade de contar"], "B"),
        ("Grau de um nó responde a qual pergunta?", ["Quantos vizinhos diferentes possui", "Quantas palavras há no corpus", "Qual é sua causa", "Qual é sua localização"], "A"),
        ("Força de um nó ponderado é normalmente quê?", ["Soma dos pesos incidentes", "Número de comunidades", "Média dos anos", "Valor de p"], "A"),
        ("Intermediação elevada garante influência histórica?", ["Sim", "Não; indica posição em caminhos sob o modelo", "Só em redes pequenas", "Só com pesos"], "B"),
        ("Uma comunidade algorítmica deve ser nomeada como grupo social quando?", ["Automaticamente", "Após estabilidade e evidência contextual", "Quando tem cor distinta", "Quando possui três nós"], "B"),
        ("Por que fixar a semente do layout?", ["Provar causalidade", "Tornar a disposição reproduzível", "Aumentar o grau", "Remover arestas"], "B"),
        ("Uma rede de correspondência difere da coocorrência porque pode registrar quê?", ["Relação dirigida entre remetente e destinatário", "Somente palavras", "Apenas médias", "Nenhum atributo"], "A"),
        ("Qual é uma análise de sensibilidade válida para rede?", ["Mudar o limiar de peso e comparar", "Escolher a figura mais bonita", "Apagar casos discordantes", "Renomear comunidades"], "A"),
        ("O que deve vir depois de um gráfico no relatório-notebook?", ["Outro código sem texto", "Interpretação e limites", "Somente legenda", "Uma conclusão causal"], "B"),
        ("Se o projeto não possui relações defensáveis, o estudante deve quê?", ["Inventar arestas", "Justificar a não adoção e demonstrar aprendizagem", "Trocar o corpus sem registro", "Aplicar correlação a códigos nominais"], "B"),
        ("Qual frase é metodologicamente mais prudente?", ["A instituição central controlava a rede", "No modelo de coocorrência, o nó tem maior força", "A correlação prova o mecanismo", "A comunidade é uma facção real"], "B"),
    ]
    linhas = ["# U06-A08 — Exercícios de múltipla escolha", "", "Assinale uma alternativa por questão.", ""]
    letras = "ABCD"
    for i, (pergunta, alternativas, _) in enumerate(questoes, 1):
        linhas += [f"## Questão {i}", "", pergunta, ""] + [f"{letras[j]}. {a}" for j, a in enumerate(alternativas)] + [""]
    (UNIDADE / "exercicios_unidade_06_texto.md").write_text("\n".join(linhas), encoding="utf-8")
    gab = ["# U06-A08 — Gabarito — exercícios de múltipla escolha", "", "## Respostas comentadas", ""]
    for i, (pergunta, _, resposta) in enumerate(questoes, 1):
        gab += [f"### {i}. {resposta}", f"A alternativa {resposta} corresponde à definição ou cautela trabalhada na unidade; as demais confundem descrição estrutural, associação e causalidade.", ""]
    (UNIDADE / "gabaritos" / "gabarito_exercicios_multipla_escolha.md").write_text("\n".join(gab), encoding="utf-8")


def criar_gabaritos() -> None:
    pasta = UNIDADE / "gabaritos"; pasta.mkdir(parents=True, exist_ok=True)
    indice = '''# Gabaritos da Unidade 6

| ID | Material | Atividade | Gabarito |
|---|---|---|---|
| U06-A01 | Notebook 00 | Diagnóstico de relações | `gabarito_00_guia.md` |
| U06-A02 | Notebook 01 | Tabela associativa | `gabarito_01_categoricas.md` |
| U06-A03 | Notebook 02 | Correlação com auditoria | `gabarito_02_correlacao.md` |
| U06-A04 | Notebook 03 | Matriz relacional | `gabarito_03_coocorrencia.md` |
| U06-A05 | Notebook 04 | Leitura estrutural | `gabarito_04_grafos.md` |
| U06-A06 | Notebook 05 | Oficina incremental | `gabarito_05_oficina.md` |
| U06-A07 | Notebook 05 | Revisão por pares | `gabarito_05_oficina.md` |
| U06-A08 | Exercícios | Múltipla escolha | `gabarito_exercicios_multipla_escolha.md` |

Os exemplos mostram uma resolução defensável, não uma resposta única. Use-os depois de realizar a atividade.'''
    (pasta / "README.md").write_text(indice, encoding="utf-8")
    textos = {
        "gabarito_00_guia.md": '''# U06-A01 — Gabarito — diagnóstico

## Exemplo de resolução

Na frase “textos mais longos citam mais instituições”, a unidade é o documento; as variáveis são extensão e número de referências. “Citam mais” descreve associação, não efeito da extensão. Gênero, período e critérios de anotação são alternativas. Uma formulação prudente é: “neste corpus, examinaremos se extensão e referências variam juntas e se a associação permanece por gênero”.

## Critérios

Identificar unidades, regra, alternativa e limite causal.''',
        "gabarito_01_categoricas.md": '''# U06-A02 — Gabarito — associação categórica

## Exemplo de resolução

Cruza-se `local` com `tem_ilustracao`. O denominador é o total de documentos de cada local, porque a pergunta compara a proporção ilustrada dentro de Capital e Interior. Exibem-se contagens, porcentagens por linha, esperados e V de Cramér. Quatro registros — dois por combinação contrastante — são inspecionados.

### Procedimento

1. confirme que cada linha representa um documento;
2. use `pd.crosstab` para as frequências observadas;
3. repita com `normalize="index"` e multiplique por 100;
4. calcule esperados a partir dos totais marginais;
5. calcule V e verifique células pequenas;
6. abra os quatro documentos e confira a codificação.

**Resposta-modelo:** “A proporção difere no corpus fictício, mas V resume apenas associação. Período e gênero podem compor a diferença; não concluímos que o local cause ilustração.”

## Erros frequentes

Misturar denominadores; interpretar V como causalidade; omitir células raras.''',
        "gabarito_02_correlacao.md": '''# U06-A03 — Gabarito — correlação

## Exemplo de resolução

Para `circulacao_estimada` e `extensao_palavras`, apresenta-se dispersão, Pearson e Spearman. Recalcula-se por local e sem o maior valor. Diferença entre coeficientes sugere sensibilidade à ordem, forma ou extremos.

### Procedimento

1. inspecione unidade e escalas;
2. faça o gráfico antes do coeficiente;
3. calcule Pearson e Spearman sem arredondamento prematuro;
4. estratifique por `local`;
5. retire apenas para sensibilidade o caso de maior circulação e documente-o;
6. formule alternativas: período, gênero, seleção e regra de simulação.

**Resposta-modelo:** “Há associação positiva nos dados simulados, mas parte pode refletir local, período e a própria regra de geração. Os coeficientes não demonstram que textos longos produzam circulação.”

## Critérios

Gráfico antes do resumo; comparação de medidas; estratificação; explicações rivais.''',
        "gabarito_03_coocorrencia.md": '''# U06-A04 — Gabarito — coocorrência

## Exemplo de resolução

Filtram-se documentos da Capital, explode-se `entidades`, constrói-se incidência e calcula-se $B^TB$. O peso é o número de documentos do recorte em que o par aparece. Para o par mais forte, listam-se IDs e notas dos documentos.

### Produto esperado

- matriz com documentos nas linhas e entidades nas colunas;
- diagonal zerada na projeção;
- lista sem pares duplicados;
- peso definido em linguagem corrente;
- tabela com os documentos que sustentam um par;
- comparação com o recorte completo.

**Resposta-modelo:** “O par é recorrente sob a regra de mesmo documento; isso não comprova contato. A projeção depende do recorte e documentos com três entidades geram três pares.”''',
        "gabarito_04_grafos.md": '''# U06-A05 — Gabarito — grafos

## Exemplo de resolução

Comparam-se o nó de maior força e um nó periférico. Grau responde à diversidade de vizinhos; força, à soma de pesos; intermediação, aos caminhos. Recria-se o grafo com `peso >= 2` e registram-se nós ou pontes perdidos.

No exemplo executado, `Jornal Horizonte` possui a maior força e a maior intermediação. Isso orienta a inspeção de seus documentos, mas não autoriza chamá-lo de instituição dominante. O limiar `peso >= 2` remove vínculos únicos; a comparação deve registrar quais entidades ficam isoladas ou mudam de comunidade.

**Resposta-modelo:** “A posição é central no modelo documental, não prova liderança. Três documentos sustentam as arestas principais e mostram contextos distintos que o grafo agrega.”''',
        "gabarito_05_oficina.md": '''# Gabarito — oficina e revisão

## U06-A06 — Exemplo de resolução

**Percurso:** associação numérica. **Pergunta:** extensão e referências institucionais variam juntas? **Evidência:** dispersão, Pearson/Spearman, estratificação por local e inspeção de três documentos. **Conclusão:** associação descritiva no corpus, sensível à composição e sem interpretação causal. A seção é acrescentada à versão anterior do mesmo relatório-notebook.

### Estrutura da seção acrescentada

1. pergunta herdada e motivo da análise;
2. definição das duas variáveis e do corpus;
3. código curto e executável;
4. gráfico com eixos e unidades;
5. coeficientes e análise de sensibilidade;
6. leitura de três registros;
7. conclusão limitada e questão para a Unidade 7.

## U06-A07 — Exemplo de parecer

“A regra está clara e o resultado é reproduzível, mas o gráfico usa cor sem explicar os grupos. Sugiro legenda, tabela equivalente e análise por período.” O autor registra se incorporou a mudança e por quê.

## Critérios

Continuidade, código executável, análise após saída, sensibilidade, casos e limites.''',
    }
    for nome, conteudo in textos.items():
        (pasta / nome).write_text(dedent(conteudo).strip() + "\n", encoding="utf-8")


def criar_referencias() -> None:
    conteudo = '''# Referências — Unidade 6

## Associação e causalidade

- AGRESTI, Alan. *An Introduction to Categorical Data Analysis*. 3. ed. Wiley, 2018.
- CRAMÉR, Harald. *Mathematical Methods of Statistics*. Princeton University Press, 1946.
- PEARSON, Karl. Mathematical Contributions to the Theory of Evolution. III. Regression, Heredity, and Panmixia. *Philosophical Transactions of the Royal Society A*, v. 187, p. 253–318, 1896.
- SPEARMAN, Charles. The Proof and Measurement of Association between Two Things. *The American Journal of Psychology*, v. 15, n. 1, p. 72–101, 1904. DOI: https://doi.org/10.2307/1412159.
- PEARL, Judea. *Causality*. 2. ed. Cambridge University Press, 2009.

## Redes e Humanidades Digitais

- WASSERMAN, Stanley; FAUST, Katherine. *Social Network Analysis: Methods and Applications*. Cambridge University Press, 1994.
- FREEMAN, Linton C. Centrality in Social Networks: Conceptual Clarification. *Social Networks*, v. 1, n. 3, p. 215–239, 1978/1979. DOI: https://doi.org/10.1016/0378-8733(78)90021-7.
- NEWMAN, Mark. *Networks: An Introduction*. Oxford University Press, 2010.
- MORETTI, Franco. *Network Theory, Plot Analysis*. Stanford Literary Lab Pamphlet 2, 2011. https://litlab.stanford.edu/projects/network-theory-plot-analysis/.
- GRANDJEAN, Martin. A Social Network Analysis of Twitter: Mapping the Digital Humanities Community. *Cogent Arts & Humanities*, v. 3, 2016. DOI: https://doi.org/10.1080/23311983.2016.1171458.
- NETWORKX DEVELOPERS. *NetworkX documentation: centrality and community algorithms*. https://networkx.org/documentation/stable/.

## Uso no material

Agresti e Cramér fundamentam associação categórica; Pearson e Spearman, correlações; Pearl, a distinção entre associação e causalidade. Wasserman e Faust, Freeman e Newman fundamentam grafos e centralidades. Moretti e Grandjean situam redes em problemas das Humanidades, inclusive seus limites interpretativos. A documentação do NetworkX sustenta as implementações, não substitui as referências conceituais.'''
    (UNIDADE / "referencias.md").write_text(conteudo, encoding="utf-8")


def criar_readme() -> None:
    notebooks = (
        ("Guia", "00_guia_da_unidade.ipynb"), ("Associação categórica", "01_associacao_variaveis_categoricas.ipynb"),
        ("Correlação", "02_correlacao_variaveis_numericas.ipynb"), ("Coocorrência", "03_coocorrencia_e_matrizes_relacionais.ipynb"),
        ("Grafos", "04_grafos_centralidade_e_comunidades.ipynb"), ("Oficina", "05_oficina_associacao_ou_rede.ipynb"),
    )
    conteudo = f'''# Unidade 6 — Associações e redes

## Ordem de estudo

Execute os notebooks 00 a 05. A unidade parte das comparações da Unidade 5 e passa a investigar relações entre variáveis e entre entidades.

## Abrir no Google Colab

{tabela_links_colab(UNIDADE.name, notebooks)}

Nos Notebooks 00 a 04, execute primeiro **Preparação do ambiente**. A oficina é discursiva. O Notebook 04 instala NetworkX no Colab somente se necessário.

## Entrega incremental

A Unidade 6 não exige outro relatório. O estudante atualiza o mesmo notebook do projeto e incorpora uma associação, uma rede ou uma não adoção fundamentada.

## Materiais

- `dados/`: bases fictícias e proveniência;
- `exercicios_unidade_06_texto.md`: vinte questões;
- `gabaritos/`: exemplos completos de resolução;
- `referencias.md`: bibliografia por tema;
- `imagens/`: diagramas SVG acessíveis;
- `revisores/`: instrumentos para avaliação acadêmica e didática.

Os dados são inteiramente fictícios e não sustentam afirmações reais.'''
    (UNIDADE / "README.md").write_text(conteudo, encoding="utf-8")


def criar_imagens() -> None:
    pasta = UNIDADE / "imagens"; pasta.mkdir(parents=True, exist_ok=True)
    specs = [
        ("00_percurso_associacao.svg", "Percurso da relação", "Pergunta, regra, medida e retorno aos casos.", ["pergunta", "regra", "medida", "casos"]),
        ("01_tabela_condicional.svg", "Associação categórica", "Contagens passam a proporções e medida.", ["contagens", "proporções", "associação"]),
        ("02_correlacao_causalidade.svg", "Da correlação à cautela", "Correlação exige forma, grupos e alternativas causais.", ["gráfico", "coeficientes", "alternativas"]),
        ("03_projecao_bipartida.svg", "Projeção relacional", "Documentos e entidades produzem pares ponderados.", ["incidência", "projeção", "arestas"]),
        ("04_centralidades.svg", "Medidas de posição", "Grau, força e intermediação respondem perguntas diferentes.", ["grau", "força", "intermediação"]),
        ("05_cadeia_argumento.svg", "Cadeia do argumento", "Dados, modelo, resultado e interpretação limitada.", ["dados", "modelo", "resultado", "limite"]),
    ]
    for args in specs: criar_svg(*args)
    linhas = ["# Inventário visual — Unidade 6", "", "Todos os diagramas são SVGs autorais, locais e acessíveis.", ""]
    for nome, titulo, desc, _ in specs:
        linhas += [f"## `{nome}`", "", f"- **Finalidade:** {titulo}. {desc}", "- **Proveniência:** produzido por `scripts/construir_unidade_06.py`.", "- **Licença:** material didático do repositório.", "- **Acessibilidade:** contém `title`, `desc`, `role` e `aria-labelledby`.", ""]
    (pasta / "README.md").write_text("\n".join(linhas), encoding="utf-8")


def criar_revisores() -> None:
    pasta = UNIDADE / "revisores"; pasta.mkdir(parents=True, exist_ok=True)
    dimensoes = {
        "01_nivel_academico.md": "Avalie rigor conceitual, distinção entre associação e causalidade, nível de mestrado e qualidade das interpretações.",
        "02_didatica.md": "Avalie progressão, transições, carga cognitiva, exemplos, atividades e apoio a estudantes de Humanidades.",
        "03_alinhamento.md": "Compare problema, conteúdos, atividades, produto incremental e ementa da Unidade 6.",
        "04_humanidades_digitais.md": "Avalie retorno às fontes, crítica das categorias, construção das relações e contribuição às Humanidades Digitais.",
        "05_referencias.md": "Confira se conceitos e fórmulas possuem referências pertinentes e se cada obra é efetivamente mobilizada.",
        "06_tecnico_acessibilidade.md": "Execute notebooks e examine caminhos, Colab, gráficos, tabelas equivalentes, SVGs, texto alternativo e reprodutibilidade.",
    }
    for nome, instrucao in dimensoes.items():
        (pasta / nome).write_text(f"# Revisor — {nome[3:-3].replace('_', ' ')}\n\n{instrucao}\n\nRegistre evidências por arquivo e classifique cada achado como bloqueador, importante ou desejável.\n", encoding="utf-8")
    (pasta / "README.md").write_text("# Revisores da Unidade 6\n\nExecute os seis pareceres após a construção. Use a matriz e consolide correções antes da publicação.\n", encoding="utf-8")
    (pasta / "matriz_de_avaliacao.md").write_text("# Matriz de avaliação\n\n| Dimensão | Atende | Parcial | Não atende | Evidência | Ação |\n|---|---|---|---|---|---|\n| Nível acadêmico |  |  |  |  |  |\n| Didática |  |  |  |  |  |\n| Alinhamento |  |  |  |  |  |\n| Humanidades Digitais |  |  |  |  |  |\n| Referências |  |  |  |  |  |\n| Técnico e acessibilidade |  |  |  |  |  |\n", encoding="utf-8")
    (pasta / "modelo_de_parecer.md").write_text("# Parecer\n\n## Síntese\n\n## Evidências\n\n## Bloqueadores\n\n## Melhorias importantes\n\n## Recomendação final\n", encoding="utf-8")


def criar_plano() -> None:
    conteudo = '''# Plano de execução — Unidade 6

## Escopo

Construir uma unidade de nível de mestrado que conecte associação categórica e numérica a coocorrência e grafos, sempre distinguindo descrição, construção relacional e causalidade.

## Sequência

1. diagnosticar o significado de “relação”;
2. trabalhar tabelas cruzadas, proporções, esperados e V de Cramér;
3. trabalhar Pearson, Spearman, forma, extremos e confundimento;
4. construir incidência e projeção de coocorrência;
5. interpretar grau, força, intermediação e comunidades;
6. incorporar somente um percurso pertinente ao relatório-notebook incremental;
7. revisar atividades, gabaritos, referências, acessibilidade e execução.

## Critérios de conclusão

Notebooks executáveis e conectados; dados fictícios identificados; atividades U06-A01–A08 associadas a exemplos de resolução; imagens acessíveis; links Colab; referências acadêmicas; validação automatizada.'''
    (RAIZ / "notes" / "plano_unidade_06.md").write_text(conteudo, encoding="utf-8")


def main() -> None:
    UNIDADE.mkdir(exist_ok=True)
    criar_dados(); criar_arestas_derivadas(); criar_imagens(); criar_gabaritos(); criar_exercicios(); criar_referencias(); criar_readme(); criar_revisores(); criar_plano()
    salvar_notebook("00_guia_da_unidade.ipynb", guia())
    salvar_notebook("01_associacao_variaveis_categoricas.ipynb", categoricas())
    salvar_notebook("02_correlacao_variaveis_numericas.ipynb", correlacao())
    salvar_notebook("03_coocorrencia_e_matrizes_relacionais.ipynb", coocorrencia())
    salvar_notebook("04_grafos_centralidade_e_comunidades.ipynb", grafos(), networkx=True)
    salvar_notebook("05_oficina_associacao_ou_rede.ipynb", oficina(), requer_dados=False)
    print("Unidade 6 construída em", UNIDADE)


if __name__ == "__main__":
    main()
