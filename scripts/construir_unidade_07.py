"""Constrói a Unidade 7 — modelos de associação condicionada."""

from __future__ import annotations

import csv
import json
import math
import random
from pathlib import Path
from textwrap import dedent

from apoio_colab import adicionar_link_na_abertura, preparacao_colab, tabela_links_colab


RAIZ = Path(__file__).resolve().parents[1]
UNIDADE = RAIZ / "unidade_07"
DADOS = UNIDADE / "dados"


def md(valor: str) -> dict:
    return {
        "cell_type": "markdown",
        "metadata": {},
        "source": dedent(valor).strip().splitlines(keepends=True),
    }


def code(valor: str) -> dict:
    return {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": dedent(valor).strip().splitlines(keepends=True),
    }


def salvar_notebook(nome: str, celulas: list[dict], requer_dados: bool = True) -> None:
    publicadas = [adicionar_link_na_abertura(celulas[0], UNIDADE.name, nome)]
    if requer_dados:
        publicadas.append(code(preparacao_colab(UNIDADE.name)))
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
    (UNIDADE / nome).write_text(
        json.dumps(documento, ensure_ascii=False, indent=1) + "\n", encoding="utf-8"
    )


def criar_dados() -> None:
    """Gera municípios fictícios com associações conhecidas, sem valor empírico."""
    DADOS.mkdir(parents=True, exist_ok=True)
    rng = random.Random(20261022)
    regioes = ["Centro-Oeste", "Nordeste", "Norte", "Sudeste", "Sul"]
    efeitos = {"Centro-Oeste": 0.0, "Nordeste": -0.18, "Norte": -0.28, "Sudeste": 0.32, "Sul": 0.22}
    linhas = []
    for i in range(150):
        regiao = regioes[i % len(regioes)]
        urbanizacao = min(98, max(35, rng.gauss(72 + efeitos[regiao] * 12, 12)))
        renda = max(650, rng.gauss(1550 + efeitos[regiao] * 500 + 7 * urbanizacao, 280))
        escolaridade = min(13, max(5, rng.gauss(7.4 + 0.035 * urbanizacao + efeitos[regiao], 0.75)))
        distancia = max(8, rng.gauss(310 - 1.7 * urbanizacao, 105))
        populacao = int(max(8000, math.exp(rng.gauss(11.0 + urbanizacao / 180, 0.65))))
        equipamento = (
            0.35 + 0.00075 * renda + 0.16 * escolaridade + 0.012 * urbanizacao
            - 0.0015 * distancia + efeitos[regiao]
            + 0.0018 * (urbanizacao - 70) * (escolaridade - 10)
            + rng.gauss(0, 0.38)
        )
        equipamento = max(0.25, equipamento)
        logito = -5.0 + 0.00115 * renda + 0.20 * escolaridade + 0.020 * urbanizacao - 0.0022 * distancia
        probabilidade = 1 / (1 + math.exp(-logito))
        biblioteca = "sim" if rng.random() < probabilidade else "não"
        linhas.append([
            f"M{i+1:03d}", f"Município Fictício {i+1:03d}", regiao,
            round(urbanizacao, 1), round(renda, 2), round(escolaridade, 1),
            round(distancia, 1), populacao, round(equipamento, 2), biblioteca,
        ])

    # Caso deliberadamente atípico para tornar o diagnóstico visível.
    linhas[-1][8] = round(float(linhas[-1][8]) + 3.8, 2)
    campos = [
        "id_municipio", "municipio", "regiao", "urbanizacao_pct", "renda_pc",
        "escolaridade_media_anos", "distancia_capital_km", "populacao",
        "equipamentos_culturais_100mil", "biblioteca_publica",
    ]
    with (DADOS / "municipios_culturais.csv").open("w", encoding="utf-8", newline="") as f:
        escritor = csv.writer(f)
        escritor.writerow(campos)
        escritor.writerows(linhas)

    dicionario = [
        ("id_municipio", "identificador", "nominal", "código fictício"),
        ("municipio", "nome", "nominal", "nome fictício"),
        ("regiao", "categoria", "nominal", "macrorregião apenas para exercício"),
        ("urbanizacao_pct", "%", "razão", "parcela da população em área urbana"),
        ("renda_pc", "unidade monetária", "razão", "renda mensal per capita simulada"),
        ("escolaridade_media_anos", "anos", "razão", "média simulada"),
        ("distancia_capital_km", "km", "razão", "distância simulada"),
        ("populacao", "pessoas", "razão", "população simulada"),
        ("equipamentos_culturais_100mil", "equipamentos/100 mil", "razão", "resposta contínua"),
        ("biblioteca_publica", "sim/não", "binária", "resposta binária"),
    ]
    with (DADOS / "dicionario_dados.csv").open("w", encoding="utf-8", newline="") as f:
        escritor = csv.writer(f)
        escritor.writerow(["variavel", "unidade", "tipo", "descricao"])
        escritor.writerows(dicionario)

    proveniencia = {
        "natureza": "dados inteiramente fictícios",
        "finalidade": "ensino de regressão linear, interação, diagnóstico e regressão logística",
        "geracao": "simulação determinística com semente 20261022",
        "caso_atipico": "M150 recebeu acréscimo deliberado na resposta contínua para o diagnóstico",
        "limite": "não representa municípios nem sustenta afirmações sobre políticas culturais reais",
    }
    (DADOS / "proveniencia.json").write_text(
        json.dumps(proveniencia, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )


def criar_svg(nome: str, titulo: str, descricao: str, etapas: list[str], rodape: str) -> None:
    largura = 1000
    n = len(etapas)
    w = 200 if n >= 4 else 250
    gap = (largura - 80 - n * w) / max(1, n - 1)
    itens = []
    for i, etapa in enumerate(etapas):
        x = 40 + i * (w + gap)
        linhas = etapa.split("|")
        itens.append(f'<rect x="{x:.0f}" y="84" width="{w}" height="116" rx="15" fill="#f4f0e6" stroke="#294c60" stroke-width="2"/>')
        for j, linha in enumerate(linhas):
            itens.append(f'<text x="{x+w/2:.0f}" y="{130+j*25}" text-anchor="middle" font-size="17" fill="#172b35">{linha}</text>')
        if i < n - 1:
            itens.append(f'<path d="M{x+w+7:.0f} 142 H{x+w+gap-9:.0f}" stroke="#a44a3f" stroke-width="3" marker-end="url(#a)"/>')
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{largura}" height="285" viewBox="0 0 {largura} 285" role="img" aria-labelledby="title desc"><title id="title">{titulo}</title><desc id="desc">{descricao}</desc><defs><marker id="a" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L0,6 L9,3 z" fill="#a44a3f"/></marker></defs><rect width="100%" height="100%" fill="#fffdf8"/><text x="500" y="40" text-anchor="middle" font-size="25" font-weight="bold" fill="#172b35">{titulo}</text>{''.join(itens)}<text x="500" y="250" text-anchor="middle" font-size="16" fill="#46565e">{rodape}</text></svg>'''
    (UNIDADE / "imagens" / nome).write_text(svg, encoding="utf-8")


def funcoes_modelagem() -> str:
    return '''
    def ajustar_ols(X, y, nomes):
        X_com_intercepto = np.column_stack([np.ones(len(X)), np.asarray(X, dtype=float)])
        coeficientes = np.linalg.lstsq(X_com_intercepto, np.asarray(y, dtype=float), rcond=None)[0]
        previstos = X_com_intercepto @ coeficientes
        residuos = np.asarray(y, dtype=float) - previstos
        r2 = 1 - np.sum(residuos ** 2) / np.sum((y - np.mean(y)) ** 2)
        return {
            "X": X_com_intercepto, "coeficientes": coeficientes,
            "previstos": previstos, "residuos": residuos,
            "r2": r2, "rmse": np.sqrt(np.mean(residuos ** 2)),
            "mae": np.mean(np.abs(residuos)), "nomes": ["intercepto", *nomes],
        }

    def tabela_coeficientes(modelo):
        return pd.DataFrame({"termo": modelo["nomes"], "coeficiente": modelo["coeficientes"]})
    '''


def guia() -> list[dict]:
    return [md('''
    # Unidade 7 — Guia de estudo
    ## Como explicar um resultado?

    **Problema orientador:** quais fatores estão associados a um resultado quando
    outras características observadas são consideradas?

    Na Unidade 6 examinamos relações duas a duas e redes. Agora construiremos modelos
    que reúnem variáveis numa mesma expressão. Em dados observacionais, “explicar”
    significará principalmente **descrever associações condicionadas**. Um coeficiente
    não transforma associação em causa.

    ![O percurso vai da pergunta ao modelo, passa pelo diagnóstico e termina numa interpretação limitada.](imagens/00_percurso_modelo.svg)
    '''), md('''
    ## Objetivos e percurso

    | Notebook | Etapa | Pergunta | Produto de aprendizagem |
    |---|---|---|---|
    | 00 | enquadrar | O que o modelo pode afirmar? | contrato interpretativo |
    | 01 | estimar | Como uma resposta numérica varia com um fator? | regressão linear simples |
    | 02 | condicionar | O que muda ao incluir fatores e categorias? | modelo múltiplo |
    | 03 | tensionar | A associação muda por contexto e o ajuste é adequado? | interação e diagnóstico |
    | 04 | modelar ocorrência | Como tratar uma resposta sim/não? | regressão logística |
    | 05 | comunicar | Que modelo serve ao projeto? | incremento do relatório-notebook |

    A sequência não é uma escada para “provar” hipóteses. Cada etapa amplia a pergunta
    e também cria novas exigências de documentação.
    '''), code('''
    import json
    import pandas as pd

    dados = pd.read_csv("dados/municipios_culturais.csv")
    dicionario = pd.read_csv("dados/dicionario_dados.csv")
    proveniencia = json.loads(open("dados/proveniencia.json", encoding="utf-8").read())
    print("Natureza:", proveniencia["natureza"])
    print("Unidades de análise:", len(dados))
    display(dicionario)
    dados.head(3)
    '''), md('''
    ## Vocabulário mínimo

    - **variável de resposta:** resultado que o modelo procura descrever;
    - **variável explicativa:** característica usada para modelar diferenças na resposta;
    - **coeficiente:** mudança estimada na resposta associada a uma mudança na explicativa;
    - **controle estatístico:** comparação matemática entre unidades semelhantes nas variáveis incluídas;
    - **resíduo:** diferença entre valor observado e valor previsto.

    “Explicativa” nomeia seu papel na equação, não garante explicação causal.

    ### U07-A01 — Discussão em duplas — graduar a afirmação

    **Dinâmica (15 minutos):** para “municípios com maior renda possuem mais
    equipamentos culturais”, identifique resposta, explicativa, duas alternativas e
    reescreva a frase em três níveis: descrição, associação condicionada e hipótese
    causal. Marque qual nível os dados observacionais permitem sustentar.

    **Resposta:** escreva aqui.

    ## Passagem

    Com o contrato interpretativo estabelecido, começaremos pelo modelo mais simples.
    Isso permite ver cada peça antes de acrescentar controles e categorias.
    ''')]


def linear_simples() -> list[dict]:
    return [md('''
    # Regressão linear simples

    A regressão linear simples resume como uma resposta numérica varia, em média,
    com uma variável explicativa. O diagrama recorda que a reta não elimina a distância
    entre cada caso e a previsão.

    ![Pontos observados, reta estimada e distâncias verticais chamadas resíduos.](imagens/01_reta_residuos.svg)
    '''), md('''
    ## 1. Da pergunta às variáveis

    Pergunta: **como a quantidade de equipamentos culturais por 100 mil habitantes
    varia com a renda per capita no conjunto fictício?**

    Definimos $Y$ como `equipamentos_culturais_100mil` e $X$ como `renda_pc`.
    A unidade de análise é o município fictício. Primeiro inspecionamos forma, escala e
    casos; só então resumimos a relação por uma reta.
    '''), code('''
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt

    dados = pd.read_csv("dados/municipios_culturais.csv")
    plt.scatter(dados["renda_pc"], dados["equipamentos_culturais_100mil"], alpha=.65, color="#426b78")
    plt.xlabel("Renda per capita simulada")
    plt.ylabel("Equipamentos por 100 mil")
    plt.title("Renda e equipamentos — dados inteiramente fictícios")
    plt.tight_layout(); plt.show()
    '''), md('''
    ## 2. A equação como argumento resumido

    $$Y_i = \\beta_0 + \\beta_1 X_i + \\varepsilon_i$$

    O intercepto $\\beta_0$ é o valor previsto quando $X=0$; pode não ter sentido
    substantivo se zero estiver fora dos dados. A inclinação $\\beta_1$ é a mudança média
    prevista em $Y$ para uma unidade adicional de $X$. O resíduo $\\varepsilon_i$ reúne a
    parcela que esta reta não descreve.

    A célula seguinte reúne os cálculos matriciais numa função reutilizável. Você não
    precisa memorizar `lstsq`: acompanhe suas entradas (`X`, `y` e nomes) e as saídas
    interpretáveis (coeficientes, previsões, resíduos, $R^2$, RMSE e MAE).
    '''), code(funcoes_modelagem()), code('''
    simples = ajustar_ols(
        dados[["renda_pc"]], dados["equipamentos_culturais_100mil"], ["renda_pc"]
    )
    display(tabela_coeficientes(simples).round(4))
    print(f"R²: {simples['r2']:.3f} | RMSE: {simples['rmse']:.3f}")

    ordem = np.argsort(dados["renda_pc"].to_numpy())
    plt.scatter(dados["renda_pc"], dados["equipamentos_culturais_100mil"], alpha=.55)
    plt.plot(dados["renda_pc"].to_numpy()[ordem], simples["previstos"][ordem], color="#a44a3f", linewidth=2)
    plt.xlabel("Renda per capita simulada"); plt.ylabel("Equipamentos por 100 mil")
    plt.title("Reta estimada sobre os casos observados")
    plt.tight_layout(); plt.show()
    '''), md('''
    ## 3. Interpretar em escala compreensível

    Como uma unidade monetária é pequena, multiplicamos a inclinação por 500. Essa
    reexpressão muda a leitura, não o modelo. $R^2$ indica a proporção da variação de
    $Y$ resumida pela reta neste conjunto; RMSE expressa o erro típico na unidade de $Y$.
    Nenhuma medida demonstra causalidade ou qualidade da fonte.
    '''), code('''
    inclinacao_500 = simples["coeficientes"][1] * 500
    print(f"Associação estimada para +500 unidades de renda: {inclinacao_500:.2f} equipamento(s) por 100 mil.")
    '''), md('''
    ### U07-A02 — Atividade — ler uma regressão simples

    1. Declare unidade, resposta e explicativa.
    2. Interprete a inclinação para 500 unidades de renda e o $R^2$.
    3. Inspecione dois casos distantes da reta.
    4. Escreva uma conclusão de até 90 palavras, incluindo um limite causal.

    **Dinâmica (25 minutos):** trabalho individual por 15 minutos; depois, troque a
    conclusão com uma colega e circule palavras fortes demais, como “causa” ou “prova”.

    **Resposta:** escreva aqui.

    ## Passagem

    A reta simples mistura renda com outras diferenças entre municípios. O próximo
    notebook inclui essas características e ensina a interpretar a comparação
    condicionada que daí resulta.
    ''')]


def multipla_categorias() -> list[dict]:
    return [md('''
    # Regressão múltipla, categorias e controle estatístico

    Um modelo múltiplo estima uma associação enquanto mantém matematicamente fixas as
    demais variáveis incluídas. Isso responde a uma pergunta mais específica que a
    regressão simples, mas não corrige automaticamente seleção, mensuração ruim ou
    variáveis omitidas.

    ![Uma resposta recebe setas de fatores observados; uma categoria de referência ancora as comparações regionais.](imagens/02_controle_referencia.svg)
    '''), md('''
    ## 1. De uma associação bruta a associações condicionadas

    Incluiremos urbanização, escolaridade e distância. Para cada coeficiente, a leitura
    será: diferença média prevista na resposta associada a uma unidade da variável,
    **entre casos iguais nos outros termos do modelo**. Essa igualdade é matemática;
    sua plausibilidade depende de haver casos comparáveis no corpus.

    $$Y_i = \\beta_0 + \\beta_1 renda_i + \\beta_2 urbanizacao_i
    + \\beta_3 escolaridade_i + \\beta_4 distancia_i + \\varepsilon_i$$

    Reutilizaremos a mesma função do notebook anterior. Ela executa a álgebra para que
    a atenção permaneça na especificação e na interpretação; não é um exercício de
    programação matricial.
    '''), code('''
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt

    dados = pd.read_csv("dados/municipios_culturais.csv")
    '''), code(funcoes_modelagem()), code('''
    numericas = ["renda_pc", "urbanizacao_pct", "escolaridade_media_anos", "distancia_capital_km"]
    multiplo = ajustar_ols(dados[numericas], dados["equipamentos_culturais_100mil"], numericas)
    comparacao = pd.DataFrame({
        "modelo": ["simples", "múltiplo"],
        "R²": [ajustar_ols(dados[["renda_pc"]], dados["equipamentos_culturais_100mil"], ["renda_pc"])["r2"], multiplo["r2"]],
        "RMSE": [ajustar_ols(dados[["renda_pc"]], dados["equipamentos_culturais_100mil"], ["renda_pc"])["rmse"], multiplo["rmse"]],
    })
    display(tabela_coeficientes(multiplo).round(4))
    display(comparacao.round(3))
    '''), md('''
    ## 2. Variáveis categóricas e categoria de referência

    Uma variável com cinco regiões não entra como os números 1 a 5: isso inventaria
    uma ordem. Criamos indicadores 0/1. Uma região fica de fora como **referência**;
    seus casos não somem, apenas formam o ponto de comparação. Aqui, por ordem
    alfabética, `Centro-Oeste` será a referência.

    O coeficiente de `regiao_Sudeste`, por exemplo, é a diferença prevista entre
    Sudeste e Centro-Oeste para os mesmos valores das variáveis numéricas incluídas.
    Trocar a referência muda os contrastes exibidos, mas não as previsões do modelo.
    '''), code('''
    indicadores_regiao = pd.get_dummies(dados["regiao"], prefix="regiao", drop_first=True, dtype=float)
    referencia = sorted(dados["regiao"].unique())[0]
    X_categorico = pd.concat([dados[numericas], indicadores_regiao], axis=1)
    com_regiao = ajustar_ols(X_categorico, dados["equipamentos_culturais_100mil"], list(X_categorico.columns))
    print("Categoria de referência:", referencia)
    display(tabela_coeficientes(com_regiao).round(4))
    '''), md('''
    ## 3. Previsões substantivas, não só coeficientes

    Coeficientes em escalas diferentes são difíceis de comparar. Por isso, calculamos
    previsões para dois perfis transparentes. Elas são cenários do modelo, não destinos
    inevitáveis de municípios reais.
    '''), code('''
    perfil_base = {coluna: 0.0 for coluna in X_categorico.columns}
    perfil_base.update({"renda_pc": 1500, "urbanizacao_pct": 60, "escolaridade_media_anos": 9, "distancia_capital_km": 250})
    perfil_alto = perfil_base.copy()
    perfil_alto.update({"renda_pc": 2200, "urbanizacao_pct": 85, "escolaridade_media_anos": 11})
    cenarios = pd.DataFrame([perfil_base, perfil_alto], index=["perfil A", "perfil B"])
    cenarios["previsao"] = np.column_stack([np.ones(2), cenarios[X_categorico.columns]]) @ com_regiao["coeficientes"]
    display(cenarios[["renda_pc", "urbanizacao_pct", "escolaridade_media_anos", "distancia_capital_km", "previsao"]].round(2))
    '''), md('''
    ### U07-A03 — Atividade — controle e referência

    1. Compare o coeficiente de renda nos modelos simples e múltiplo.
    2. Interprete um coeficiente numérico e um regional sem dizer “efeito causal”.
    3. Explique a um leitor por que Centro-Oeste não desapareceu.
    4. Crie dois perfis plausíveis e compare previsões, registrando cada valor escolhido.

    **Dinâmica (30 minutos):** grupos de três; uma pessoa executa, outra confere as
    escalas e a terceira atua como revisora da linguagem. Troquem papéis na metade.

    **Resposta:** escreva aqui.

    ## Passagem

    Até aqui, supusemos uma mesma inclinação e um ajuste aceitável para todos os casos.
    O próximo notebook testa essas duas simplificações com interação e resíduos.
    ''')]


def interacoes_diagnostico() -> list[dict]:
    return [md('''
    # Interações, resíduos e qualidade do ajuste

    Uma interação representa uma associação que varia conforme outra característica.
    O diagnóstico, por sua vez, pergunta onde o modelo falha. Ambos impedem que uma
    única média seja tomada como retrato uniforme do corpus.

    ![Duas retas com inclinações distintas representam uma interação.](imagens/03_interacao.svg)
    '''), md('''
    ## 1. Interação: quando a inclinação depende do contexto

    Investigaremos se a associação entre urbanização e equipamentos varia com a
    escolaridade. Centralizar as duas variáveis faz o intercepto e os termos principais
    se referirem a valores médios observados.

    $$Y_i = \\beta_0 + \\beta_1 U_{ci} + \\beta_2 E_{ci}
    + \\beta_3(U_{ci}E_{ci}) + \\varepsilon_i$$

    Com interação, $\\beta_1$ não é uma inclinação universal: a inclinação de
    urbanização é $\\beta_1 + \\beta_3 E_c$.

    O código primeiro cria versões centralizadas e seu produto; depois usa a função de
    ajuste já conhecida. Observe essa sequência conceitual, não a sintaxe algébrica.
    '''), code('''
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt

    dados = pd.read_csv("dados/municipios_culturais.csv")
    dados["urbanizacao_c"] = dados["urbanizacao_pct"] - dados["urbanizacao_pct"].mean()
    dados["escolaridade_c"] = dados["escolaridade_media_anos"] - dados["escolaridade_media_anos"].mean()
    dados["interacao"] = dados["urbanizacao_c"] * dados["escolaridade_c"]
    '''), code(funcoes_modelagem()), code('''
    nomes_interacao = ["urbanizacao_c", "escolaridade_c", "interacao"]
    modelo_interacao = ajustar_ols(dados[nomes_interacao], dados["equipamentos_culturais_100mil"], nomes_interacao)
    display(tabela_coeficientes(modelo_interacao).round(4))

    grades = np.linspace(dados["urbanizacao_pct"].min(), dados["urbanizacao_pct"].max(), 80)
    for escolaridade in [8, 10, 12]:
        uc = grades - dados["urbanizacao_pct"].mean()
        ec = escolaridade - dados["escolaridade_media_anos"].mean()
        matriz = np.column_stack([np.ones(len(grades)), uc, np.repeat(ec, len(grades)), uc * ec])
        plt.plot(grades, matriz @ modelo_interacao["coeficientes"], label=f"{escolaridade} anos")
    plt.xlabel("Urbanização (%)"); plt.ylabel("Equipamentos previstos por 100 mil")
    plt.title("Previsões condicionais do modelo de interação")
    plt.legend(title="Escolaridade"); plt.tight_layout(); plt.show()
    '''), md('''
    ## 2. Diagnóstico: voltar dos resumos aos casos

    Resíduos grandes identificam casos mal descritos; alavancagem alta identifica
    combinações incomuns de explicativas. Nenhuma é defeito automático. São convites
    para conferir fonte, codificação, contexto e dependência do resultado.

    ![O diagnóstico confronta previstos, resíduos, casos influentes e decisão analítica.](imagens/03_diagnostico.svg)
    '''), code('''
    X = modelo_interacao["X"]
    alavancagem = np.diag(X @ np.linalg.pinv(X.T @ X) @ X.T)
    diagnostico = dados[["id_municipio", "municipio", "equipamentos_culturais_100mil"]].copy()
    diagnostico["previsto"] = modelo_interacao["previstos"]
    diagnostico["residuo"] = modelo_interacao["residuos"]
    diagnostico["alavancagem"] = alavancagem
    display(diagnostico.reindex(diagnostico["residuo"].abs().sort_values(ascending=False).index).head(6).round(3))

    fig, eixos = plt.subplots(1, 2, figsize=(11, 4))
    eixos[0].scatter(modelo_interacao["previstos"], modelo_interacao["residuos"], alpha=.6)
    eixos[0].axhline(0, color="#a44a3f"); eixos[0].set(xlabel="Previstos", ylabel="Resíduos", title="Resíduos × previstos")
    eixos[1].scatter(dados["equipamentos_culturais_100mil"], modelo_interacao["previstos"], alpha=.6)
    limites = [dados["equipamentos_culturais_100mil"].min(), dados["equipamentos_culturais_100mil"].max()]
    eixos[1].plot(limites, limites, color="#a44a3f"); eixos[1].set(xlabel="Observados", ylabel="Previstos", title="Observados × previstos")
    plt.tight_layout(); plt.show()
    print(f"R²={modelo_interacao['r2']:.3f} | RMSE={modelo_interacao['rmse']:.3f} | MAE={modelo_interacao['mae']:.3f}")
    '''), md('''
    ## 3. Sensibilidade a um caso atípico

    Remover um caso só para melhorar o resultado seria inadequado. Como o arquivo de
    proveniência declara uma observação didaticamente alterada, fazemos uma análise de
    sensibilidade: comparamos resultados com e sem ela e mantemos as duas versões.
    '''), code('''
    sem_m150 = dados[dados["id_municipio"] != "M150"]
    modelo_sem_m150 = ajustar_ols(sem_m150[nomes_interacao], sem_m150["equipamentos_culturais_100mil"], nomes_interacao)
    sensibilidade = pd.DataFrame({
        "modelo": ["todos os casos", "sem M150"],
        "R²": [modelo_interacao["r2"], modelo_sem_m150["r2"]],
        "RMSE": [modelo_interacao["rmse"], modelo_sem_m150["rmse"]],
        "coef_interacao": [modelo_interacao["coeficientes"][3], modelo_sem_m150["coeficientes"][3]],
    })
    display(sensibilidade.round(3))
    '''), md('''
    ### U07-A04 — Atividade — interação e diagnóstico

    1. Explique por que o coeficiente de urbanização depende da escolaridade.
    2. Leia as três linhas previstas sem comparar apenas o coeficiente de interação.
    3. Inspecione o maior resíduo na base e na proveniência.
    4. Compare o modelo completo e a sensibilidade; justifique qual relatar.

    **Dinâmica (35 minutos):** duplas produzem uma figura comentada e um parágrafo de
    cautela. Na plenária, outra dupla deve conseguir reconstruir a decisão tomada.

    **Resposta:** escreva aqui.

    ## Passagem

    A resposta foi contínua até agora. Para presença ou ausência, a reta pode prever
    valores abaixo de zero ou acima de um. A regressão logística modela a ocorrência
    respeitando o intervalo da probabilidade.
    ''')]


def logistica() -> list[dict]:
    return [md('''
    # Introdução à regressão logística

    Quando a resposta registra ocorrência — sim/não, presente/ausente — modelamos a
    probabilidade do evento. O exemplo pergunta: **quais características estão
    associadas à presença de biblioteca pública no conjunto fictício?**

    ![Probabilidade transforma-se em chance e logaritmo da chance antes da combinação linear.](imagens/04_probabilidade_chance.svg)
    '''), md('''
    ## 1. Probabilidade, chance e logito

    A probabilidade $p$ varia de 0 a 1. A chance compara ocorrência e não ocorrência:

    $$chance = \\frac{p}{1-p}$$

    Se $p=0{,}75$, a chance é 3:1. O logito transforma a chance numa escala sem limites:

    $$\\log\\left(\\frac{p_i}{1-p_i}\\right)=\\beta_0+\\beta_1X_{1i}+\\cdots+\\beta_kX_{ki}$$

    Um coeficiente exponenciado, $e^{\\beta}$, é uma razão de chances. Razão de chances
    não é a mesma coisa que diferença de probabilidades.

    A próxima célula mostra didaticamente a transformação dos dados e a otimização. Não
    se espera que você reprograme o algoritmo; concentre-se em como a resposta é
    codificada, como as escalas são padronizadas e como a saída será traduzida.
    '''), code('''
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt

    dados = pd.read_csv("dados/municipios_culturais.csv")
    y_logistico = (dados["biblioteca_publica"] == "sim").astype(float).to_numpy()
    variaveis_logisticas = ["renda_pc", "urbanizacao_pct", "escolaridade_media_anos", "distancia_capital_km"]
    medias = dados[variaveis_logisticas].mean()
    desvios = dados[variaveis_logisticas].std(ddof=0)
    X_padronizado = ((dados[variaveis_logisticas] - medias) / desvios).to_numpy()
    X_logistico = np.column_stack([np.ones(len(dados)), X_padronizado])

    def sigmoide(z):
        z = np.clip(z, -30, 30)
        return 1 / (1 + np.exp(-z))

    def ajustar_logistico(X, y, taxa=.08, iteracoes=8000):
        beta = np.zeros(X.shape[1])
        for _ in range(iteracoes):
            probabilidades = sigmoide(X @ beta)
            beta -= taxa * (X.T @ (probabilidades - y)) / len(y)
        return beta, sigmoide(X @ beta)

    beta_logistico, probabilidades = ajustar_logistico(X_logistico, y_logistico)
    coeficientes_logisticos = pd.DataFrame({
        "termo": ["intercepto", *[f"{v} (+1 desvio-padrão)" for v in variaveis_logisticas]],
        "coeficiente_logito": beta_logistico,
        "razao_de_chances": np.exp(beta_logistico),
    })
    display(coeficientes_logisticos.round(3))
    '''), md('''
    ## 2. Por que padronizar neste exemplo?

    Renda, quilômetros e anos têm escalas diferentes. A padronização faz cada
    coeficiente representar aumento de um desvio-padrão e estabiliza a otimização
    numérica didática. O sinal mostra a direção da associação condicionada; a razão de
    chances mostra a multiplicação estimada das chances, mantidos os demais termos.

    A implementação acima explicita o algoritmo para aprendizagem. Em pesquisa,
    bibliotecas estatísticas devem fornecer erros-padrão, intervalos e testes; eles não
    são substituídos por esta demonstração.
    '''), md('''
    ## 3. Traduzir o modelo de volta para probabilidades

    Razões de chances são pouco intuitivas. Vamos variar a urbanização, manter as
    outras variáveis em suas médias e observar probabilidades previstas. Isso torna
    claro que uma mesma razão de chances não implica a mesma variação percentual em
    todos os pontos da curva.
    '''), code('''
    grade_urbana = np.linspace(dados["urbanizacao_pct"].min(), dados["urbanizacao_pct"].max(), 100)
    cenarios_originais = pd.DataFrame({v: np.repeat(medias[v], len(grade_urbana)) for v in variaveis_logisticas})
    cenarios_originais["urbanizacao_pct"] = grade_urbana
    cenarios_z = ((cenarios_originais[variaveis_logisticas] - medias) / desvios).to_numpy()
    prob_grade = sigmoide(np.column_stack([np.ones(len(grade_urbana)), cenarios_z]) @ beta_logistico)
    plt.plot(grade_urbana, prob_grade, color="#a44a3f", linewidth=2)
    plt.xlabel("Urbanização (%)"); plt.ylabel("Probabilidade prevista de biblioteca")
    plt.ylim(0, 1); plt.title("Cenários do modelo — demais variáveis nas médias")
    plt.tight_layout(); plt.show()

    faixas = pd.qcut(probabilidades, 5, duplicates="drop")
    calibracao_descritiva = pd.DataFrame({"faixa": faixas, "observado": y_logistico, "previsto": probabilidades}).groupby("faixa", observed=True).agg(n=("observado", "size"), proporcao_observada=("observado", "mean"), probabilidade_media=("previsto", "mean"))
    display(calibracao_descritiva.round(3))
    '''), md('''
    A tabela confronta probabilidades médias com proporções observadas por faixa. É um
    diagnóstico descritivo interno, não prova de desempenho fora da amostra. Avaliação
    preditiva com separação treino/teste pertence à Unidade 8.

    ### U07-A05 — Atividade — interpretar ocorrência

    1. Converta as probabilidades 0,20 e 0,75 em chances.
    2. Interprete uma razão de chances do modelo, mencionando a padronização.
    3. Compare as probabilidades previstas em 50% e 90% de urbanização.
    4. Escreva por que o resultado não demonstra que urbanização cria bibliotecas.

    **Dinâmica (30 minutos):** individual até o item 2; os itens 3 e 4 são revisados em
    duplas. Cada dupla substitui uma frase causal por uma formulação associativa.

    **Resposta:** escreva aqui.

    ## Passagem

    Já sabemos estimar, diagnosticar e traduzir dois tipos de modelo. A oficina não
    pede um relatório novo: ela orienta a incorporação de uma análise pertinente ao
    mesmo projeto cumulativo da disciplina.
    ''')]


def oficina() -> list[dict]:
    return [md('''
    # Oficina — modelo associativo e interpretação substantiva

    **Produto:** uma nova seção no mesmo relatório-notebook cumulativo. Não entregue
    um arquivo separado. Use seu problema, corpus e decisões das unidades anteriores.

    ![A pergunta leva à especificação, diagnóstico, casos e afirmação limitada.](imagens/05_cadeia_argumento.svg)
    '''), md('''
    ## 1. Antes de modelar: decisão de pertinência

    A regressão só é adequada quando há uma resposta definida, variação suficiente,
    unidades comparáveis e número razoável de casos. Se seu corpus não atende a essas
    condições, a entrega correta é uma **não adoção fundamentada**, acompanhada por
    uma análise descritiva coerente. Não fabrique observações nem troque o problema
    apenas para usar a técnica.

    ## 2. O que acrescentar ao relatório-notebook

    Inclua uma seção `Unidade 7 — Modelo de associação condicionada` com:

    1. pergunta e justificativa do modelo ou da não adoção;
    2. unidade de análise, resposta, explicativas, escalas e ausências;
    3. fórmula conceitual antes do código;
    4. tabela ou gráfico de resultados com legenda autônoma;
    5. ao menos um diagnóstico e inspeção de casos;
    6. interpretação substantiva em escala compreensível;
    7. limites, alternativas e linguagem causal compatível com o desenho.

    O código deve aparecer junto da transformação ou análise que realiza. Não use um
    `DataFrame` para substituir argumentos que devem ser escritos em prosa.
    '''), md('''
    ## 3. Roteiro de trabalho em 70 minutos

    | Tempo | Ação | Evidência no notebook |
    |---:|---|---|
    | 0–10 | recuperar pergunta e corpus | parágrafo de pertinência |
    | 10–20 | definir resposta e explicativas | quadro de especificação |
    | 20–40 | estimar ou justificar não adoção | código reproduzível ou diagnóstico |
    | 40–52 | produzir figura/tabela e voltar aos casos | saída comentada |
    | 52–62 | redigir interpretação e limites | parágrafo substantivo |
    | 62–70 | revisão por pares | registro de uma mudança |

    ### U07-A06 — Oficina — incremento do relatório-notebook

    **Dinâmica:** trabalhe em seu próprio projeto seguindo o roteiro. A pessoa docente
    faz duas paradas coletivas: aos 20 minutos para conferir especificações e aos 52
    para conferir diagnósticos. Entregue o mesmo notebook já usado nas outras unidades.

    **Resposta:** inclua no seu relatório-notebook.

    ### U07-A07 — Revisão por pares — afirmação, evidência e limite

    **Dinâmica (20 minutos):** o colega localiza, sem explicação oral, (a) a pergunta,
    (b) a unidade de análise, (c) a interpretação de um resultado, (d) um caso
    inspecionado e (e) o limite causal. Registra um ponto claro, uma dúvida e uma
    mudança prioritária. O autor implementa ou justifica por que não implementou.

    **Resposta:** anexe ao final da seção o parecer recebido e sua decisão.

    ## 4. Critérios de avaliação

    - coerência entre pergunta, resposta, explicativas e modelo;
    - execução reproduzível e dados documentados;
    - interpretação de escala, referência e condicionamento;
    - diagnóstico ligado a casos, não apenas a métricas;
    - distinção explícita entre associação e causalidade;
    - integração com o argumento cumulativo do projeto.

    ## Fechamento

    O modelo é uma compressão argumentativa: torna comparações explícitas, mas não
    substitui crítica das fontes, contexto e desenho de pesquisa. Mesmo com bom ajuste,
    o modelo não demonstra causalidade. A Unidade 8 retomará
    essa base ao separar explicação e previsão e avaliar desempenho fora da amostra.
    ''')]


def criar_materiais_textuais() -> None:
    notebooks = (
        ("Guia", "00_guia_da_unidade.ipynb"),
        ("Regressão linear simples", "01_regressao_linear_simples.ipynb"),
        ("Modelo múltiplo e categorias", "02_regressao_multipla_e_categorias.ipynb"),
        ("Interações e diagnóstico", "03_interacoes_residuos_e_qualidade.ipynb"),
        ("Regressão logística", "04_regressao_logistica.ipynb"),
        ("Oficina", "05_oficina_modelo_associativo.ipynb"),
    )
    readme = f'''# Unidade 7 — Modelos de associação condicionada

## Ordem de estudo

Execute os notebooks 00 a 05. A unidade parte das associações da Unidade 6 e mostra
como modelar uma resposta considerando simultaneamente características observadas.

## Abrir no Google Colab

{tabela_links_colab("unidade_07", notebooks)}

Nos Notebooks 00 a 04, execute primeiro **Preparação do ambiente**. A oficina é
discursiva e orienta a atualização do projeto.

## Entrega incremental

A Unidade 7 não exige outro relatório. O estudante atualiza o mesmo notebook do
projeto com um modelo pertinente ou uma não adoção fundamentada.

## Materiais

- `dados/`: base fictícia, dicionário e proveniência;
- `exercicios_unidade_07_texto.md`: vinte questões;
- `gabaritos/`: exemplos completos de resolução;
- `referencias.md`: bibliografia por tema;
- `imagens/`: diagramas SVG acessíveis;
- `revisores/`: instrumentos para avaliação acadêmica e didática.

Os dados são inteiramente fictícios e não sustentam afirmações sobre municípios ou
políticas culturais reais.
'''
    (UNIDADE / "README.md").write_text(readme, encoding="utf-8")

    referencias = '''# Referências da Unidade 7

## Regressão como prática de modelagem

- GELMAN, Andrew; HILL, Jennifer; VEHTARI, Aki. *Regression and Other Stories*.
  Cambridge: Cambridge University Press, 2020. DOI: 10.1017/9781139161879.
  Sustenta a ênfase em construção, visualização, verificação e interpretação de modelos.
- FOX, John. *Applied Regression Analysis and Generalized Linear Models*. 3. ed.
  Thousand Oaks: Sage, 2016. Apoia regressão múltipla, categorias, interação e diagnóstico.

## Regressão logística

- HOSMER, David W.; LEMESHOW, Stanley; STURDIVANT, Rodney X. *Applied Logistic
  Regression*. 3. ed. Hoboken: Wiley, 2013. DOI: 10.1002/9781118548387.
  Fundamenta probabilidade, chance, logito e interpretação de razões de chances.

## Causalidade e dados observacionais

- HERNÁN, Miguel A.; ROBINS, James M. *Causal Inference: What If*. Boca Raton:
  Chapman & Hall/CRC, 2020. Apoia a separação entre ajuste associativo e identificação causal.
- PEARL, Judea. *Causality: Models, Reasoning, and Inference*. 2. ed. Cambridge:
  Cambridge University Press, 2009. Fundamenta a necessidade de hipóteses causais externas à regressão.

## Humanidades digitais

- UNDERWOOD, Ted. *Distant Horizons: Digital Evidence and Literary Change*.
  Chicago: University of Chicago Press, 2019. Exemplo de modelagem estatística ligada
  a questões interpretativas nas humanidades.
- DRUCKER, Johanna. Humanities approaches to graphical display. *Digital
  Humanities Quarterly*, v. 5, n. 1, 2011. Apoia a comunicação da incerteza e o
  tratamento crítico das visualizações.

As referências fundamentam os conceitos; os dados e resultados desta unidade são
didáticos e inteiramente fictícios.
'''
    (UNIDADE / "referencias.md").write_text(referencias, encoding="utf-8")

    exercicios = '''# U07-A08 — Exercícios de múltipla escolha

## Questão 1
Em regressão, “variável explicativa” significa:  
A) causa comprovada. B) variável usada para modelar a resposta. C) variável sem erro. D) resposta binária.

## Questão 2
O resíduo de um caso é:  
A) observado menos previsto. B) média menos mediana. C) coeficiente dividido pelo erro. D) chance menos probabilidade.

## Questão 3
Na regressão simples, a inclinação representa:  
A) causalidade. B) mudança média prevista em Y por unidade de X. C) valor máximo de Y. D) tamanho da amostra.

## Questão 4
Um intercepto pode ter pouca interpretação substantiva quando:  
A) X=0 está fora do domínio observado. B) R² é positivo. C) há categorias. D) Y é numérico.

## Questão 5
R² resume:  
A) proporção da variação de Y descrita pelo modelo na amostra. B) causalidade. C) viés da fonte. D) validade externa.

## Questão 6
RMSE é expresso:  
A) na unidade da resposta. B) sempre em porcentagem. C) sem unidade. D) na unidade da explicativa.

## Questão 7
Em um modelo múltiplo, um coeficiente é lido:  
A) ignorando outros termos. B) condicionado aos demais termos incluídos. C) como experimento. D) como frequência.

## Questão 8
Controle estatístico:  
A) elimina todo confundimento. B) compara matematicamente casos nos termos incluídos. C) corrige fontes. D) cria aleatorização.

## Questão 9
Uma variável nominal com cinco categorias costuma entrar como:  
A) cinco números ordenados. B) indicadores com uma referência. C) um resíduo. D) uma probabilidade.

## Questão 10
A categoria de referência:  
A) é excluída dos dados. B) ancora contrastes. C) deve ser a maior. D) causa as demais.

## Questão 11
Ao trocar a referência categórica:  
A) mudam os contrastes, não as previsões. B) somem casos. C) prova-se causalidade. D) muda Y.

## Questão 12
Uma interação indica que:  
A) uma associação varia com outra variável. B) não há resíduos. C) X é causa. D) a amostra é aleatória.

## Questão 13
Com interação entre X e Z, o coeficiente isolado de X:  
A) vale para qualquer Z. B) depende do ponto de referência de Z. C) é R². D) é uma chance.

## Questão 14
Resíduo grande deve levar primeiro a:  
A) apagamento automático. B) inspeção do caso e da fonte. C) conclusão causal. D) troca da resposta.

## Questão 15
Alavancagem alta indica:  
A) combinação incomum de explicativas. B) erro ortográfico. C) maior causalidade. D) resposta binária.

## Questão 16
Se p=0,75, a chance de ocorrência é:  
A) 0,25. B) 0,75. C) 3 para 1. D) 75 para 1.

## Questão 17
Na regressão logística, exp(beta) representa:  
A) diferença de médias. B) razão de chances. C) R². D) resíduo.

## Questão 18
Razão de chances igual a 2 significa necessariamente +100 pontos percentuais?  
A) sim. B) não, a mudança de probabilidade depende do ponto inicial. C) só com R². D) só em categorias.

## Questão 19
Um bom ajuste observacional demonstra causalidade?  
A) sempre. B) nunca precisa de hipótese. C) não; identificação causal exige desenho e pressupostos. D) se houver gráfico.

## Questão 20
Se regressão não é pertinente ao projeto, a entrega adequada é:  
A) fabricar dados. B) não adoção fundamentada e análise coerente. C) omitir a unidade. D) copiar o exemplo.
'''
    (UNIDADE / "exercicios_unidade_07_texto.md").write_text(exercicios, encoding="utf-8")


def criar_gabaritos() -> None:
    pasta = UNIDADE / "gabaritos"
    pasta.mkdir(parents=True, exist_ok=True)
    indice = '''# Gabaritos da Unidade 7

| Atividade | Gabarito |
|---|---|
| U07-A01 | `gabarito_00_guia.md` |
| U07-A02 | `gabarito_01_linear.md` |
| U07-A03 | `gabarito_02_multipla.md` |
| U07-A04 | `gabarito_03_interacao_diagnostico.md` |
| U07-A05 | `gabarito_04_logistica.md` |
| U07-A06 | `gabarito_05_oficina.md` |
| U07-A07 | `gabarito_05_oficina.md` |
| U07-A08 | `gabarito_exercicios_multipla_escolha.md` |

Os valores numéricos podem variar se o estudante mudar a especificação. Avalie a
coerência entre pergunta, código, resultados, casos e limites, não a reprodução cega.
'''
    (pasta / "README.md").write_text(indice, encoding="utf-8")
    textos = {
        "gabarito_00_guia.md": '''# Gabarito — graduar a afirmação

**Atividade associada:** U07-A01 — Discussão em duplas — graduar a afirmação

## Exemplo de resolução

- Resposta: equipamentos culturais por 100 mil habitantes.
- Explicativa: renda per capita.
- Alternativas: urbanização pode estar ligada a ambas; políticas estaduais podem
  distribuir equipamentos e também afetar oportunidades econômicas.
- Descrição: “Nos dados fictícios, municípios de maior renda tendem a registrar mais equipamentos.”
- Associação condicionada: “A renda permanece positivamente associada ao número
  previsto de equipamentos após considerar urbanização, escolaridade e distância.”
- Hipótese causal: “Aumentar renda produziria equipamentos.” Esta última não é
  identificada pelo desenho observacional.

**Resposta-modelo:** o segundo nível é o mais forte que o exercício permite, desde
que sejam citadas as variáveis condicionantes e as limitações da simulação.
''',
        "gabarito_01_linear.md": '''# Gabarito — regressão linear simples

**Atividade associada:** U07-A02 — Atividade — ler uma regressão simples

## Exemplo de resolução

A unidade é o município fictício; a resposta é equipamentos por 100 mil e a
explicativa é renda per capita. O intercepto é 1,238 e a inclinação é 0,0014 por
unidade monetária: para 500 unidades, o aumento previsto é cerca de 0,70 equipamento
por 100 mil. O $R^2$ é 0,412 e o RMSE, 0,591 equipamento por 100 mil.

Ordenei os resíduos absolutos e inspecionei as linhas correspondentes. M150 está muito
acima da reta; a proveniência esclarece que foi alterado para fins didáticos. Não o
removi silenciosamente.

**Resposta-modelo:** “No conjunto fictício, 500 unidades adicionais de renda estão
associadas a um aumento médio previsto de equipamentos. A dispersão em torno da reta
e M150 mostram que renda sozinha não descreve todos os casos. O ajuste não demonstra
que elevar renda causaria expansão cultural.”
''',
        "gabarito_02_multipla.md": '''# Gabarito — regressão múltipla e categorias

**Atividade associada:** U07-A03 — Atividade — controle e referência

## Exemplo de resolução

Comparei a inclinação de renda: aproximadamente 0,0014 no modelo simples e 0,0011 no
múltiplo. O $R^2$ passou de 0,412 para 0,551 e o RMSE de 0,591 para 0,517. A mudança
revela que a associação simples agregava diferenças correlatas;
não autoriza escolher o resultado “mais bonito”. O coeficiente de escolaridade é a
mudança prevista para um ano adicional entre casos iguais nos demais termos.

Centro-Oeste é a referência alfabética. Seus casos continuam no ajuste e formam o
ponto zero dos contrastes regionais. O coeficiente de `regiao_Sudeste` é cerca de
0,346: compara Sudeste a Centro-Oeste condicionando às variáveis numéricas. Os perfis
A e B têm previsões de 3,23 e 4,45; a diferença modelada é 1,22 equipamento por 100
mil, sem que o contraste seja chamado de intervenção.

**Resposta-modelo:** “O modelo descreve diferenças condicionadas entre perfis
observados. A interpretação depende de haver sobreposição entre esses perfis e não
elimina variáveis omitidas ou problemas de mensuração.”
''',
        "gabarito_03_interacao_diagnostico.md": '''# Gabarito — interação e diagnóstico

**Atividade associada:** U07-A04 — Atividade — interação e diagnóstico

## Exemplo de resolução

No modelo, a inclinação de urbanização é $\\beta_1+\\beta_3E_c$. Portanto, as curvas de
8, 10 e 12 anos podem ter inclinações diferentes. Comparei previsões ao longo da
faixa observada em vez de interpretar apenas o sinal de $\\beta_3$.

A tabela de resíduos leva a M150, com resíduo próximo de 4,043. Conferi a linha no CSV
e li `proveniencia.json`, que declara alteração deliberada. Mantive o modelo completo
como principal ($R^2=0{,}314$; RMSE $=0{,}639$) e apresentei a versão sem M150 como
sensibilidade ($R^2=0{,}372$; RMSE $=0{,}547$). O coeficiente de interação passa de
aproximadamente 0,003 para 0,004.

**Resposta-modelo:** “A heterogeneidade sugerida pelo modelo deve ser lida como
associação contextual. O resultado é parcialmente sensível ao caso didático M150;
ambas as especificações são apresentadas, e nenhuma identifica efeito causal.”
''',
        "gabarito_04_logistica.md": '''# Gabarito — regressão logística

**Atividade associada:** U07-A05 — Atividade — interpretar ocorrência

## Exemplo de resolução

- $p=0{,}20$: chance $=0{,}20/0{,}80=0{,}25$, ou 1:4.
- $p=0{,}75$: chance $=0{,}75/0{,}25=3$, ou 3:1.

Escolhi `urbanizacao_pct`. Como as explicativas foram padronizadas, sua razão de
chances, cerca de 1,616, compara um acréscimo de um desvio-padrão, mantendo as demais
constantes. Com renda, escolaridade e distância em suas médias, as probabilidades
previstas são aproximadamente 0,443 em 50% e 0,820 em 90% de urbanização: diferença
de 0,377, ou 37,7 pontos percentuais, apenas nos cenários do modelo.

**Resposta-modelo:** “Maior urbanização está associada à probabilidade prevista de
biblioteca neste conjunto. A curva traduz a associação para probabilidades, mas não
demonstra que urbanizar produz bibliotecas: políticas, história institucional e
seleção municipal não foram identificadas causalmente.”
''',
        "gabarito_05_oficina.md": '''# Gabarito da oficina

**Atividades associadas:**

- U07-A06 — Oficina — incremento do relatório-notebook
- U07-A07 — Revisão por pares — afirmação, evidência e limite

## Exemplo de incremento do relatório-notebook

**Pergunta:** a extensão de um documento está associada ao número de instituições
mencionadas quando gênero e período são considerados?  
**Unidade:** documento. **Resposta:** contagem de instituições. **Explicativas:**
extensão, gênero e período.  
**Decisão:** como a resposta é contagem pequena, uma regressão linear seria apenas
aproximação exploratória; registro esse limite e comparo previstos com resíduos.

O notebook mostra código de preparação, fórmula conceitual, tabela de coeficientes,
gráfico observado-previsto e três documentos com maiores resíduos. A conclusão diz
“associação condicionada”, explica a escala de 100 palavras e propõe um modelo de
contagem como desenvolvimento futuro.

**Exemplo de não adoção:** com apenas nove cartas comparáveis, não ajustei modelo
múltiplo. Mantive uma tabela de casos e expliquei que poucos graus de liberdade e
ausência de sobreposição tornariam os coeficientes instáveis.

## Exemplo de revisão por pares

- Ponto claro: unidade e resposta aparecem antes do código.
- Dúvida: o gráfico não informa se o período foi mantido constante.
- Prioridade: acrescentar legenda com variáveis condicionantes e inspecionar D017.
- Decisão do autor: aceitei; refiz a legenda e acrescentei uma nota sobre D017.
''',
        "gabarito_exercicios_multipla_escolha.md": '''# Gabarito — múltipla escolha

**Atividade associada:** U07-A08 — Exercícios de múltipla escolha

| Questão | Resposta | Justificativa breve |
|---:|:---:|---|
| 1 | B | “Explicativa” é função no modelo, não estatuto causal. |
| 2 | A | Resíduo é observado menos previsto. |
| 3 | B | A inclinação resume mudança média prevista. |
| 4 | A | Extrapolar o intercepto pode ser substantivamente vazio. |
| 5 | A | R² é resumo de variação descrita na amostra. |
| 6 | A | RMSE retorna à escala da resposta. |
| 7 | B | A leitura é condicionada aos demais termos. |
| 8 | B | Controle só abrange variáveis incluídas e pressupostos. |
| 9 | B | Indicadores evitam impor ordem nominal. |
| 10 | B | A referência ancora os contrastes. |
| 11 | A | A parametrização muda; os valores previstos não. |
| 12 | A | Interação expressa associação heterogênea. |
| 13 | B | O termo principal depende do ponto de referência. |
| 14 | B | O caso precisa ser compreendido, não apagado. |
| 15 | A | Alavancagem aponta posição incomum em X. |
| 16 | C | $0{,}75/(1-0{,}75)=3$. |
| 17 | B | Exponenciar beta produz razão de chances. |
| 18 | B | Probabilidades dependem do nível inicial. |
| 19 | C | Ajuste e identificação causal são problemas distintos. |
| 20 | B | A não adoção argumentada preserva coerência do projeto. |

**Exemplo de raciocínio (Questão 18):** partindo de chance 1:4 ($p=0{,}20$), dobrá-la
gera 1:2 ($p\\approx0{,}33$), aumento de 13 pontos. Partindo de chance 3:1
($p=0{,}75$), dobrá-la gera 6:1 ($p\\approx0{,}86$), aumento de 11 pontos. A mesma
razão de chances não é uma diferença fixa de probabilidade.
''',
    }
    for nome, conteudo in textos.items():
        (pasta / nome).write_text(conteudo, encoding="utf-8")


def criar_revisores() -> None:
    pasta = UNIDADE / "revisores"
    pasta.mkdir(parents=True, exist_ok=True)
    (pasta / "README.md").write_text(
        "# Revisores da Unidade 7\n\nExecute os seis pareceres após a construção. "
        "Use a matriz e consolide correções antes da publicação.\n", encoding="utf-8"
    )
    criterios = {
        "01_nivel_academico.md": ("Nível acadêmico", "complexidade de mestrado; precisão conceitual; diferença entre associação condicionada, previsão e causalidade; profundidade das interpretações"),
        "02_didatica.md": ("Didática", "encadeamento entre seções; explicação antes do código; carga cognitiva; clareza das dinâmicas; acessibilidade para estudantes de Humanidades"),
        "03_alinhamento.md": ("Alinhamento", "cobertura da ementa; problema orientador; continuidade com a Unidade 6 e preparação da Unidade 8; produto cumulativo"),
        "04_humanidades_digitais.md": ("Humanidades digitais", "crítica de fontes e categorias; retorno aos casos; interpretação substantiva; pertinência dos exemplos culturais"),
        "05_referencias.md": ("Referências", "bibliografia acadêmica; correspondência entre afirmações e fontes; equilíbrio entre estatística, causalidade e Humanidades Digitais"),
        "06_tecnico_acessibilidade.md": ("Técnica e acessibilidade", "execução integral; escalas e rótulos; fórmulas renderizáveis; texto alternativo; proveniência e reprodutibilidade"),
    }
    for nome, (titulo, itens) in criterios.items():
        (pasta / nome).write_text(f'''# Revisor — {titulo}

Avalie: {itens}.

Para cada achado, registre **local**, **evidência**, **gravidade** (bloqueador,
importante ou sugestão) e **correção verificável**. Não aprove por impressão geral.
Conclua com `aprovado`, `aprovado com ajustes` ou `requer revisão`.
''', encoding="utf-8")
    (pasta / "matriz_de_avaliacao.md").write_text('''# Matriz de avaliação

| Critério | Insuficiente | Adequado | Excelente |
|---|---|---|---|
| Rigor | confunde associação e causa | limita afirmações | explicita pressupostos e alternativas |
| Didática | código sem preparação | percurso compreensível | transições antecipam a função de cada etapa |
| HD | técnica descontextualizada | retorna ao problema | casos e categorias reorientam a análise |
| Evidência | resultado sem diagnóstico | inclui diagnóstico | sensibilidade altera ou sustenta a conclusão |
| Entrega | produto isolado | integra o relatório | justifica adoção ou não adoção |
''', encoding="utf-8")
    (pasta / "modelo_de_parecer.md").write_text('''# Parecer da Unidade 7

**Revisor:**  
**Data:**  
**Decisão:**  

## Pontos fortes

## Achados e evidências

## Correções prioritárias

## Verificação após ajustes
''', encoding="utf-8")


def main() -> None:
    for pasta in [UNIDADE, DADOS, UNIDADE / "imagens"]:
        pasta.mkdir(parents=True, exist_ok=True)
    criar_dados()
    ilustracoes = [
        ("00_percurso_modelo.svg", "Do problema à afirmação", "Sequência de pergunta, especificação, diagnóstico e interpretação.", ["Pergunta", "Especificação", "Diagnóstico", "Interpretação"], "Um modelo organiza comparações; o desenho limita a afirmação."),
        ("01_reta_residuos.svg", "A reta não contém todos os casos", "A regressão resume tendência e preserva resíduos.", ["Casos|observados", "Reta|estimada", "Resíduos|inspecionados"], "A distância até a reta também é evidência."),
        ("02_controle_referencia.svg", "Condicionar e comparar", "Explicativas numéricas e indicadores alimentam uma resposta.", ["Variáveis|numéricas", "Categoria|de referência", "Resposta|prevista"], "Controle estatístico não equivale a controle experimental."),
        ("03_interacao.svg", "Associação que varia", "Duas condições produzem inclinações distintas.", ["Contexto A|inclinação 1", "Interação", "Contexto B|inclinação 2"], "Interprete previsões condicionais, não um coeficiente isolado."),
        ("03_diagnostico.svg", "Diagnosticar é voltar aos casos", "Percurso dos previstos aos resíduos e casos.", ["Previstos", "Resíduos", "Casos", "Decisão"], "Não remova observações apenas para melhorar métricas."),
        ("04_probabilidade_chance.svg", "Da probabilidade ao logito", "Transformações da regressão logística.", ["Probabilidade|0 a 1", "Chance|p/(1-p)", "Logito", "Predição"], "Razão de chances não é diferença de probabilidades."),
        ("05_cadeia_argumento.svg", "Cadeia de evidências", "A entrega conecta modelo, diagnóstico e limite.", ["Pergunta", "Modelo", "Casos", "Limite"], "O mesmo relatório-notebook acumula as decisões do projeto."),
    ]
    for args in ilustracoes:
        criar_svg(*args)
    salvar_notebook("00_guia_da_unidade.ipynb", guia())
    salvar_notebook("01_regressao_linear_simples.ipynb", linear_simples())
    salvar_notebook("02_regressao_multipla_e_categorias.ipynb", multipla_categorias())
    salvar_notebook("03_interacoes_residuos_e_qualidade.ipynb", interacoes_diagnostico())
    salvar_notebook("04_regressao_logistica.ipynb", logistica())
    salvar_notebook("05_oficina_modelo_associativo.ipynb", oficina(), requer_dados=False)
    criar_materiais_textuais()
    criar_gabaritos()
    criar_revisores()
    (UNIDADE / "imagens" / "README.md").write_text(
        "# Ilustrações da Unidade 7\n\nSVGs autorais, locais, com `title`, `desc` e texto alternativo nos notebooks.\n",
        encoding="utf-8",
    )
    plano = '''# Plano de execução — Unidade 7

## Escopo

Construir uma unidade de nível de mestrado sobre regressão linear e logística como
modelos de associação condicionada, com interpretação substantiva e limites causais.

## Sequência

1. distinguir resposta, explicativas e níveis de afirmação;
2. estimar e interpretar regressão linear simples;
3. incluir controles, categorias e referências;
4. explorar interação, resíduos, alavancagem e sensibilidade;
5. introduzir probabilidade, chance, logito e regressão logística;
6. incorporar análise pertinente ou não adoção ao relatório-notebook cumulativo;
7. revisar atividades, gabaritos, referências, acessibilidade e execução.

## Critérios de conclusão

Notebooks executáveis e encadeados; dados fictícios identificados; atividades
U07-A01–A08 ligadas a exemplos de resolução; figuras acessíveis; links Colab;
referências acadêmicas; validação automatizada.
'''
    (RAIZ / "notes" / "plano_unidade_07.md").write_text(plano, encoding="utf-8")


if __name__ == "__main__":
    main()
