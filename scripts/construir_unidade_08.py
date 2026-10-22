"""Constrói a Unidade 8 — classificação supervisionada e análise de erros."""

from __future__ import annotations

import csv
import json
import random
from pathlib import Path
from textwrap import dedent

from apoio_colab import adicionar_link_na_abertura, preparacao_colab, tabela_links_colab


RAIZ = Path(__file__).resolve().parents[1]
UNIDADE = RAIZ / "unidade_08"
DADOS = UNIDADE / "dados"


def md(texto: str) -> dict:
    return {"cell_type": "markdown", "metadata": {}, "source": dedent(texto).strip().splitlines(keepends=True)}


def code(texto: str) -> dict:
    return {"cell_type": "code", "execution_count": None, "metadata": {}, "outputs": [], "source": dedent(texto).strip().splitlines(keepends=True)}


def salvar(nome: str, celulas: list[dict], dados: bool = True) -> None:
    publicadas = [adicionar_link_na_abertura(celulas[0], UNIDADE.name, nome)]
    if dados:
        publicadas.append(code(preparacao_colab(UNIDADE.name, (("sklearn", "scikit-learn>=1.5,<2"),))))
    publicadas.extend(celulas[1:])
    doc = {"cells": publicadas, "metadata": {"kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"}, "language_info": {"name": "python", "version": "3"}}, "nbformat": 4, "nbformat_minor": 5}
    (UNIDADE / nome).write_text(json.dumps(doc, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")


def criar_dados() -> None:
    DADOS.mkdir(parents=True, exist_ok=True)
    rng = random.Random(20261023)
    positivos = [
        "campanha de vacinação amplia atendimento nos bairros",
        "hospital debate prevenção e cuidado coletivo",
        "boletim registra casos de febre e medidas sanitárias",
        "conselho discute acesso à saúde e novos postos",
        "médicos orientam famílias sobre higiene e prevenção",
    ]
    negativos = [
        "companhia anuncia espetáculo de teatro no centro",
        "biblioteca recebe coleção de romances e periódicos",
        "associação promove concerto e exposição de pintura",
        "jornal comenta eleição e reunião do conselho municipal",
        "escola organiza festa literária e concurso de poesia",
    ]
    ambiguos = [
        "teatro beneficente arrecada recursos para o hospital",
        "conselho debate orçamento da biblioteca e do posto de saúde",
        "jornal publica anúncio de remédio ao lado da programação cultural",
        "escola recebe palestra sobre higiene durante festa comunitária",
    ]
    linhas = []
    for i in range(160):
        periodo = "1890–1899" if i < 80 else "1900–1909"
        origem = "Capital" if i % 3 else "Interior"
        alvo = "relevante" if i % 2 == 0 else "não relevante"
        texto = rng.choice(positivos if alvo == "relevante" else negativos)
        if i % 11 == 0:
            texto = rng.choice(ambiguos)
        # Vocabulário de época correlacionado ao alvo cria oportunidade para auditar grupos.
        if periodo == "1890–1899" and alvo == "relevante":
            texto += " salubridade pública"
        if periodo == "1900–1909" and alvo == "relevante":
            texto += " serviço sanitário"
        texto += f" registro {i+1}"
        linhas.append([f"D{i+1:03d}", periodo, origem, texto, alvo])
    with (DADOS / "documentos_classificacao.csv").open("w", encoding="utf-8", newline="") as f:
        w = csv.writer(f); w.writerow(["id_documento", "periodo", "origem", "texto", "classe_alvo"]); w.writerows(linhas)

    anotacoes = []
    for i, linha in enumerate(linhas[:32]):
        ouro = linha[-1]
        a = ouro if i not in {5, 18, 27} else ("não relevante" if ouro == "relevante" else "relevante")
        b = ouro if i not in {3, 18, 22, 30} else ("não relevante" if ouro == "relevante" else "relevante")
        anotacoes.append([linha[0], linha[3], a, b, ouro])
    with (DADOS / "amostra_anotacao.csv").open("w", encoding="utf-8", newline="") as f:
        w = csv.writer(f); w.writerow(["id_documento", "texto", "anotador_a", "anotador_b", "decisao_adjudicada"]); w.writerows(anotacoes)

    dicionario = [
        ["id_documento", "nominal", "identificador fictício"], ["periodo", "ordinal", "grupo temporal"],
        ["origem", "nominal", "grupo de origem"], ["texto", "texto", "excerto sintético"],
        ["classe_alvo", "binária", "relevância temática adjudicada"],
    ]
    with (DADOS / "dicionario_dados.csv").open("w", encoding="utf-8", newline="") as f:
        w = csv.writer(f); w.writerow(["variavel", "tipo", "descricao"]); w.writerows(dicionario)
    prov = {"natureza": "dados inteiramente fictícios", "semente": 20261023, "finalidade": "classificação textual supervisionada", "limite": "os textos não são fontes históricas e as métricas não descrevem sistemas reais", "alerta": "padrões de vocabulário por período foram inseridos deliberadamente para auditoria"}
    (DADOS / "proveniencia.json").write_text(json.dumps(prov, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def svg(nome: str, titulo: str, desc: str, etapas: list[str], rodape: str) -> None:
    n = len(etapas); largura = 1000; w = 190 if n >= 4 else 245; gap = (largura - 80 - n*w) / max(1, n-1); itens = []
    for i, etapa in enumerate(etapas):
        x = 40 + i*(w+gap); linhas = etapa.split("|")
        itens.append(f'<rect x="{x:.0f}" y="82" width="{w}" height="118" rx="14" fill="#f4f0e6" stroke="#294c60" stroke-width="2"/>')
        for j, linha in enumerate(linhas): itens.append(f'<text x="{x+w/2:.0f}" y="{130+j*24}" text-anchor="middle" font-size="17" fill="#172b35">{linha}</text>')
        if i<n-1: itens.append(f'<path d="M{x+w+6:.0f} 141 H{x+w+gap-8:.0f}" stroke="#a44a3f" stroke-width="3" marker-end="url(#a)"/>')
    conteudo = f'''<svg xmlns="http://www.w3.org/2000/svg" width="1000" height="285" viewBox="0 0 1000 285" role="img" aria-labelledby="title desc"><title id="title">{titulo}</title><desc id="desc">{desc}</desc><defs><marker id="a" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L0,6 L9,3 z" fill="#a44a3f"/></marker></defs><rect width="100%" height="100%" fill="#fffdf8"/><text x="500" y="40" text-anchor="middle" font-size="25" font-weight="bold" fill="#172b35">{titulo}</text>{''.join(itens)}<text x="500" y="250" text-anchor="middle" font-size="16" fill="#46565e">{rodape}</text></svg>'''
    (UNIDADE / "imagens" / nome).write_text(conteudo, encoding="utf-8")


def guia() -> list[dict]:
    return [md('''
    # Unidade 8 — Guia de estudo
    ## Como atribuir categorias a documentos ou registros?

    Classificar é aplicar uma regra a novos casos com base em exemplos anotados. A
    tarefa exige categorias defensáveis, separação entre aprendizagem e avaliação e
    análise qualitativa dos erros. Uma boa métrica não torna a categoria natural.

    ![O percurso liga categoria, anotação, separação dos dados, modelo e auditoria.](imagens/00_percurso_classificacao.svg)
    '''), md('''
    ## Percurso e produtos

    | Notebook | Decisão central | Produto de aprendizagem |
    |---|---|---|
    | 00 | O que significa a categoria? | contrato classificatório |
    | 01 | Humanos aplicam a regra do mesmo modo? | guia e concordância |
    | 02 | Como avaliar sem reutilizar o gabarito? | treino, teste e linha de base |
    | 03 | Que modelo erra, onde e para quem? | métricas, matriz e auditoria |
    | 04 | Como representar textos? | TF-IDF e comparação conceitual com embeddings |
    | 05 | A classificação serve ao projeto? | incremento ou não adoção fundamentada |
    '''), code('''
    import json
    import pandas as pd
    dados = pd.read_csv("dados/documentos_classificacao.csv")
    dicionario = pd.read_csv("dados/dicionario_dados.csv")
    proveniencia = json.loads(open("dados/proveniencia.json", encoding="utf-8").read())
    print(proveniencia["natureza"], "—", len(dados), "documentos")
    display(dicionario)
    dados.head(3)
    '''), md('''
    ### U08-A01 — Discussão em duplas — categoria ou descoberta?

    **Dinâmica (15 minutos):** compare “documento relevante para saúde pública” e
    “documento que contém a palavra hospital”. Para cada formulação, indique unidade,
    regra, caso limítrofe, custo de falso positivo e custo de falso negativo. Escolha
    qual requer anotação interpretativa e justifique.

    **Resposta:** escreva aqui.

    ## Passagem

    Antes de treinar um modelo, precisamos saber se a própria regra pode ser aplicada
    de modo consistente. O próximo notebook transforma uma definição em guia testável.
    ''')]


def anotacao() -> list[dict]:
    return [md('''
    # Categorias, anotação e concordância

    Um guia de anotação converte o conceito em decisões observáveis. Deve incluir
    definição, inclusões, exclusões, casos limítrofes, unidade de contexto e processo de
    adjudicação. Concordância mede consistência; não prova validade do construto.

    ![Do conceito ao guia, a duas anotações independentes e à adjudicação.](imagens/01_anotacao.svg)
    '''), md('''
    ## 1. Guia mínimo do exemplo

    **Relevante:** o excerto trata saúde, doença, prevenção, cuidado ou instituição
    sanitária como assunto, não como menção lateral. **Não relevante:** saúde aparece
    apenas em anúncio ou contexto secundário. Leia o excerto inteiro. Discordâncias são
    justificadas e adjudicadas sem apagar os rótulos originais.
    '''), code('''
    import pandas as pd
    from sklearn.metrics import cohen_kappa_score, confusion_matrix
    anotacoes = pd.read_csv("dados/amostra_anotacao.csv")
    acordo = (anotacoes["anotador_a"] == anotacoes["anotador_b"]).mean()
    kappa = cohen_kappa_score(anotacoes["anotador_a"], anotacoes["anotador_b"])
    print(f"Acordo bruto: {acordo:.1%} | Kappa de Cohen: {kappa:.3f}")
    discordancias = anotacoes[anotacoes["anotador_a"] != anotacoes["anotador_b"]]
    display(discordancias)
    '''), md('''
    O acordo bruto conta coincidências; kappa desconta a concordância esperada pelas
    distribuições marginais. Um valor não resolve discordâncias: releia os casos e
    revise o guia. O exemplo usa duas pessoas e categorias nominais; outros desenhos
    exigem outras medidas.

    ### U08-A02 — Atividade integrada — revisar o guia pelos desacordos

    **Dinâmica (30 minutos):** grupos de três leem as discordâncias. Duas pessoas
    aplicam o guia independentemente; a terceira registra justificativas e conduz a
    adjudicação. Proponham uma alteração precisa no guia e digam qual novo caso a testa.

    **Resposta:** registre regra anterior, caso, decisão e regra revisada.

    ## Passagem

    Com rótulos documentados, ainda não podemos avaliar o modelo nos mesmos exemplos
    usados para ajustá-lo. A próxima etapa separa aprendizagem e teste.
    ''')]


def treino_teste() -> list[dict]:
    return [md('''
    # Treinamento, teste e linha de base

    O conjunto de treinamento ensina parâmetros; o teste estima desempenho em casos
    não usados no ajuste. A divisão deve ocorrer antes de decisões guiadas pelo
    resultado. Estratificar preserva aproximadamente a proporção da classe-alvo.

    ![Os dados anotados se dividem em treino e teste, e o teste permanece reservado.](imagens/02_treino_teste.svg)
    '''), code('''
    import pandas as pd
    from sklearn.model_selection import train_test_split
    from sklearn.dummy import DummyClassifier
    from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

    dados = pd.read_csv("dados/documentos_classificacao.csv")
    treino, teste = train_test_split(dados, test_size=.25, random_state=42, stratify=dados["classe_alvo"])
    print("Treino:", len(treino), "| Teste reservado:", len(teste))
    display(pd.crosstab(index=["treino"], columns=treino["classe_alvo"], normalize="index").round(3))
    display(pd.crosstab(index=["teste"], columns=teste["classe_alvo"], normalize="index").round(3))
    '''), md('''
    ## 2. Linha de base antes do modelo

    Uma linha de base responde: o método supera uma regra trivial? Usaremos a classe
    mais frequente. Como as classes são quase equilibradas, a acurácia da maioria deve
    ficar perto de 50%. Com **desbalanceamento**, ela pode parecer alta e ainda ignorar
    inteiramente a classe de interesse.
    '''), code('''
    linha_base = DummyClassifier(strategy="most_frequent")
    linha_base.fit([[0]] * len(treino), treino["classe_alvo"])
    previsto_base = linha_base.predict([[0]] * len(teste))

    def metricas(y, previsto):
        return pd.Series({
            "acurácia": accuracy_score(y, previsto),
            "precisão": precision_score(y, previsto, pos_label="relevante", zero_division=0),
            "revocação": recall_score(y, previsto, pos_label="relevante", zero_division=0),
            "F1": f1_score(y, previsto, pos_label="relevante", zero_division=0),
        })

    metricas_base = metricas(teste["classe_alvo"], previsto_base)
    display(metricas_base.to_frame("linha de base").T.round(3))
    '''), md('''
    ### U08-A03 — Atividade — proteger o teste

    Explique por que não devemos escolher palavras, parâmetros ou regras após olhar os
    erros do teste repetidamente. Compare uma divisão estratificada e outra sem
    estratificação; registre proporções, semente e qual versão será preservada.

    **Dinâmica (25 minutos):** individual na execução; dupla na justificativa. Não
    escolha a divisão que produz a maior métrica.

    **Resposta:** escreva aqui.

    ## Passagem

    Fixados teste e linha de base, podemos comparar modelos. A avaliação seguinte não
    se limita a um número: separa tipos de erro e grupos afetados.
    ''')]


def modelos_erros() -> list[dict]:
    return [md('''
    # Modelos, métricas e análise de erros

    Regressão logística e árvore podem classificar, mas aprendem regras distintas. A
    primeira combina evidências numa fronteira linear; a segunda cria decisões
    sucessivas. Aqui usamos apenas metadados para tornar essas escolhas visíveis.

    ![A matriz separa verdadeiros e falsos positivos e negativos.](imagens/03_matriz_confusao.svg)
    '''), code('''
    import pandas as pd
    import matplotlib.pyplot as plt
    from sklearn.compose import ColumnTransformer
    from sklearn.preprocessing import OneHotEncoder
    from sklearn.pipeline import Pipeline
    from sklearn.model_selection import train_test_split
    from sklearn.linear_model import LogisticRegression
    from sklearn.tree import DecisionTreeClassifier, plot_tree
    from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix, ConfusionMatrixDisplay

    dados = pd.read_csv("dados/documentos_classificacao.csv")
    treino, teste = train_test_split(dados, test_size=.25, random_state=42, stratify=dados["classe_alvo"])
    colunas = ["periodo", "origem"]
    preparo = ColumnTransformer([("categorias", OneHotEncoder(handle_unknown="ignore"), colunas)])
    modelos = {
        "logística": Pipeline([("preparo", preparo), ("modelo", LogisticRegression(max_iter=1000, random_state=42))]),
        "árvore": Pipeline([("preparo", preparo), ("modelo", DecisionTreeClassifier(max_depth=3, min_samples_leaf=8, random_state=42))]),
    }

    def medir(y, previsto):
        return {"acurácia": accuracy_score(y, previsto), "precisão": precision_score(y, previsto, pos_label="relevante", zero_division=0), "revocação": recall_score(y, previsto, pos_label="relevante", zero_division=0), "F1": f1_score(y, previsto, pos_label="relevante", zero_division=0)}

    previsoes = {}; resultados = []
    for nome, modelo in modelos.items():
        modelo.fit(treino[colunas], treino["classe_alvo"])
        previsoes[nome] = modelo.predict(teste[colunas])
        resultados.append({"modelo": nome, **medir(teste["classe_alvo"], previsoes[nome])})
    tabela_metricas = pd.DataFrame(resultados).set_index("modelo")
    display(tabela_metricas.round(3))
    '''), md('''
    ## 2. Métricas respondem a perguntas diferentes

    - **Acurácia:** parcela total correta.
    - **Precisão:** entre os previstos como relevantes, quantos eram relevantes?
    - **Revocação:** entre os relevantes, quantos foram encontrados?
    - **F1:** média harmônica de precisão e revocação.

    Escolher uma métrica é decidir qual erro importa. Em triagem documental, falso
    negativo pode ocultar uma fonte; em publicação automática, falso positivo pode ser
    mais danoso. A matriz de confusão conserva os quatro tipos de resultado.
    '''), code('''
    melhor_nome = tabela_metricas["F1"].idxmax()
    melhor_previsto = previsoes[melhor_nome]
    ConfusionMatrixDisplay.from_predictions(teste["classe_alvo"], melhor_previsto, labels=["não relevante", "relevante"], cmap="Blues")
    plt.title(f"Matriz de confusão — {melhor_nome} — teste reservado")
    plt.tight_layout(); plt.show()
    erros = teste.assign(previsto=melhor_previsto)
    erros = erros[erros["classe_alvo"] != erros["previsto"]]
    display(erros[["id_documento", "periodo", "origem", "texto", "classe_alvo", "previsto"]].head(10))
    '''), md('''
    ## 3. Desempenho entre grupos

    Uma média pode ocultar dano concentrado. Calculamos métricas por período no mesmo
    teste. Grupos pequenos produzem estimativas instáveis; o resultado é uma auditoria
    descritiva, não certificado de equidade.
    '''), code('''
    auditoria = []
    avaliacao = teste.assign(previsto=melhor_previsto)
    for periodo, grupo in avaliacao.groupby("periodo"):
        auditoria.append({"periodo": periodo, "n": len(grupo), **medir(grupo["classe_alvo"], grupo["previsto"])})
    metricas_grupo = pd.DataFrame(auditoria).set_index("periodo")
    display(metricas_grupo.round(3))
    '''), md('''
    ### U08-A04 — Atividade integrada — escolher pelo custo do erro

    Escolha logística ou árvore após comparar linha de base, quatro métricas, matriz,
    cinco erros e grupos. Declare qual erro é mais custoso para uma pergunta de
    Humanidades e se a diferença entre grupos muda sua decisão.

    **Dinâmica (35 minutos):** grupos de três assumem papéis de pesquisador, responsável
    pelo acervo e pessoa afetada pela decisão. Produzam uma escolha e uma objeção.

    **Resposta:** escreva aqui.

    ## Passagem

    Metadados sozinhos não leem o documento. O próximo notebook representa palavras
    por TF-IDF, compara com a linha de base e preserva o retorno aos textos errados.
    ''')]


def textos() -> list[dict]:
    return [md('''
    # Classificação de textos: TF-IDF e embeddings

    TF-IDF representa documentos por palavras ou sequências curtas, ponderadas pela
    frequência no documento e raridade na coleção. Embeddings representam proximidades
    aprendidas em espaços densos. Ambos são representações parciais, não o texto em si.

    ![TF-IDF privilegia termos discriminativos; embeddings aproximam usos semanticamente semelhantes.](imagens/04_representacoes.svg)
    '''), md('''
    ## 1. Um modelo textual reproduzível e offline

    Ajustamos o vocabulário somente no treino por meio de um `Pipeline`; assim o teste
    não informa quais termos devem existir. Usamos regressão logística por oferecer
    coeficientes inspecionáveis. O objetivo não é decorar parâmetros, mas acompanhar a
    cadeia texto → vetor → modelo → erro.
    '''), code('''
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
    from sklearn.model_selection import train_test_split
    from sklearn.pipeline import Pipeline
    from sklearn.feature_extraction.text import TfidfVectorizer
    from sklearn.linear_model import LogisticRegression
    from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, ConfusionMatrixDisplay

    dados = pd.read_csv("dados/documentos_classificacao.csv")
    treino, teste = train_test_split(dados, test_size=.25, random_state=42, stratify=dados["classe_alvo"])
    classificador_textual = Pipeline([
        ("tfidf", TfidfVectorizer(lowercase=True, ngram_range=(1, 2), min_df=2)),
        ("modelo", LogisticRegression(max_iter=1000, random_state=42)),
    ])
    classificador_textual.fit(treino["texto"], treino["classe_alvo"])
    previsto_texto = classificador_textual.predict(teste["texto"])
    metricas_texto = pd.Series({
        "acurácia": accuracy_score(teste["classe_alvo"], previsto_texto),
        "precisão": precision_score(teste["classe_alvo"], previsto_texto, pos_label="relevante"),
        "revocação": recall_score(teste["classe_alvo"], previsto_texto, pos_label="relevante"),
        "F1": f1_score(teste["classe_alvo"], previsto_texto, pos_label="relevante"),
    })
    display(metricas_texto.to_frame("TF-IDF + logística").T.round(3))
    '''), md('''
    ## 2. O que o modelo textual utilizou?

    Coeficientes positivos aproximam termos associados a “relevante” no treino;
    negativos, a “não relevante”. Eles não medem importância histórica nem significado
    intrínseco. Termos de período podem denunciar atalho: desempenho alto apoiado em
    marcas contextuais que talvez mudem fora desta coleção.
    '''), code('''
    termos = classificador_textual.named_steps["tfidf"].get_feature_names_out()
    coef = classificador_textual.named_steps["modelo"].coef_[0]
    extremos = pd.DataFrame({"termo": termos, "coeficiente": coef})
    display(pd.concat([extremos.nsmallest(8, "coeficiente"), extremos.nlargest(8, "coeficiente")]).sort_values("coeficiente"))

    avaliacao_texto = teste.assign(previsto=previsto_texto)
    erros_texto = avaliacao_texto[avaliacao_texto["classe_alvo"] != avaliacao_texto["previsto"]]
    display(erros_texto[["id_documento", "texto", "classe_alvo", "previsto"]].head(10))
    '''), md('''
    ## 3. Onde entram embeddings?

    Um embedding troca milhares de contagens esparsas por vetores densos aprendidos em
    grandes coleções. Pode aproximar paráfrases sem palavras idênticas, mas carrega
    vieses, domínio, versão e custo do modelo de origem. Nesta unidade ele é introduzido
    conceitualmente; executar um modelo remoto tornaria a aula dependente de rede e
    enviaria textos a terceiros. Uma comparação controlada pertence à Unidade 12.

    ### U08-A05 — Atividade — termos, atalhos e erros

    Inspecione os termos extremos e todos os erros textuais. Identifique um termo
    substantivo, um possível atalho e um caso ambíguo. Proponha uma nova rodada de
    anotação ou teste temporal capaz de desafiar o resultado.

    **Dinâmica (30 minutos):** duplas; uma pessoa lê a tabela e outra retorna ao texto.
    Troquem papéis antes de formular a proposta.

    **Resposta:** escreva aqui.

    ## Passagem

    A oficina reúne definição, avaliação e leitura dos erros. Classificar só entra no
    projeto quando a categoria e o custo de seus erros forem defensáveis.
    ''')]


def oficina() -> list[dict]:
    return [md('''
    # Oficina — protótipo de classificação e análise de erros

    **Produto:** uma nova seção no mesmo relatório-notebook cumulativo. Não entregue
    outro arquivo. Se classificação não responde à pergunta, produza uma não adoção
    fundamentada em vez de inventar uma categoria.

    ![A entrega conecta regra, teste, comparação, erros e decisão.](imagens/05_cadeia_entrega.svg)
    '''), md('''
    ## Roteiro de 75 minutos

    | Tempo | Ação | Evidência no notebook |
    |---:|---|---|
    | 0–12 | definir uso e custo dos erros | pergunta decisória |
    | 12–25 | escrever/testar guia | exemplos e caso limítrofe |
    | 25–38 | reservar teste e criar base | divisão documentada |
    | 38–55 | comparar ao menos um método à base | métricas e matriz |
    | 55–65 | ler erros e grupos | tabela comentada |
    | 65–75 | revisar decisão | limite e próximo teste |

    ### U08-A06 — Oficina — incremento do relatório-notebook

    **Dinâmica:** trabalhe no próprio projeto. A pessoa docente verifica o guia aos 25
    minutos e a separação do teste aos 38. Inclua categoria-alvo, guia, divisão,
    baseline, modelo, métricas escolhidas, matriz, casos errados, grupos e limites.

    **Resposta:** inclua no mesmo relatório-notebook.

    ### U08-A07 — Revisão por pares — reconstruir a decisão

    **Dinâmica (20 minutos):** sem explicação oral, o colega tenta localizar finalidade,
    regra, teste reservado, base, custo do erro, três casos e limite de generalização.
    Registra um ponto claro, uma dúvida e uma mudança prioritária. O autor implementa a
    mudança ou justifica a não implementação.

    **Resposta:** anexe parecer e decisão ao final da seção.

    ## Critérios de avaliação

    Coerência da categoria; ausência de vazamento; comparação à linha de base; escolha
    justificada de métricas; inspeção qualitativa; auditoria entre grupos; integração ao
    problema humanístico; reprodutibilidade e prudência na generalização.

    ## Fechamento

    Classificação não descobre automaticamente essências: operacionaliza uma decisão.
    A Unidade 9 inverterá o ponto de partida e perguntará o que ocorre quando não há
    categorias prévias — sem transformar agrupamentos em grupos naturais.
    ''')]


def materiais() -> None:
    notebooks = (("Guia", "00_guia_da_unidade.ipynb"), ("Anotação", "01_categorias_anotacao_e_concordancia.ipynb"), ("Treino, teste e baseline", "02_treinamento_teste_e_linha_de_base.ipynb"), ("Modelos e erros", "03_modelos_metricas_e_erros.ipynb"), ("Classificação textual", "04_classificacao_textual_tfidf_e_embeddings.ipynb"), ("Oficina", "05_oficina_classificacao.ipynb"))
    (UNIDADE / "README.md").write_text(f'''# Unidade 8 — Classificação supervisionada

## Ordem de estudo

Execute os notebooks 00 a 05. A unidade transforma categorias documentadas em um
protótipo avaliado fora do treino e retorna dos resumos aos documentos.

## Abrir no Google Colab

{tabela_links_colab("unidade_08", notebooks)}

Nos Notebooks 00 a 04, execute primeiro **Preparação do ambiente**. A oficina é
discursiva e atualiza o mesmo projeto cumulativo.

## Materiais

- `dados/`: documentos sintéticos, amostra anotada, dicionário e proveniência;
- `exercicios_unidade_08_texto.md`: vinte questões;
- `gabaritos/`: exemplos completos de resolução;
- `referencias.md`, `imagens/` e `revisores/`: sustentação acadêmica e editorial.

Os dados são inteiramente fictícios e não sustentam afirmações históricas reais.
''', encoding="utf-8")
    (UNIDADE / "referencias.md").write_text('''# Referências da Unidade 8

- ARTSTEIN, Ron; POESIO, Massimo. Inter-coder agreement for computational linguistics.
  *Computational Linguistics*, v. 34, n. 4, 2008. DOI: 10.1162/coli.07-034-R2.
- JURAFSKY, Daniel; MARTIN, James H. *Speech and Language Processing*. 3. ed., rascunho.
  Capítulos sobre classificação textual, regressão logística e avaliação.
- PEDREGOSA, Fabian et al. Scikit-learn: Machine Learning in Python. *JMLR*, v. 12,
  2011. Biblioteca usada nos experimentos reproduzíveis.
- SALTON, Gerard; BUCKLEY, Christopher. Term-weighting approaches in automatic text
  retrieval. *Information Processing & Management*, v. 24, n. 5, 1988.
- BENDER, Emily M. et al. On the dangers of stochastic parrots. In: *FAccT*, 2021.
  DOI: 10.1145/3442188.3445922. Apoia a crítica de escala, documentação e vieses.
- SCULLEY, D. et al. Hidden technical debt in machine learning systems. In: *NeurIPS*,
  2015. Apoia a atenção a vazamento, dependências e mudança de distribuição.

Documentação técnica consultada: guias oficiais do scikit-learn sobre divisão de
dados, métricas, `DummyClassifier`, TF-IDF, regressão logística e árvores.
''', encoding="utf-8")
    questoes = [
        ("Uma categoria-alvo deve ser:", ["tratada como natural", "operacionalizada por regra e exemplos", "definida pelo algoritmo", "mantida sem casos limítrofes"]),
        ("Concordância alta entre anotadores:", ["prova causalidade", "elimina adjudicação", "não prova validade do construto", "dispensa o guia"]),
        ("Adjudicação serve para:", ["resolver e documentar desacordos", "apagar rótulos originais", "treinar no teste", "maximizar acurácia"]),
        ("O conjunto de teste deve ser usado para:", ["criar o vocabulário", "escolher a categoria", "corrigir cada regra", "avaliar casos não usados no ajuste"]),
        ("A estratificação procura:", ["ordenar documentos", "preservar aproximadamente as proporções das classes", "aumentar a amostra", "remover casos ambíguos"]),
        ("Uma linha de base permite:", ["comparar o modelo a uma regra trivial", "provar validade", "substituir o teste", "eliminar desbalanceamento"]),
        ("Há vazamento quando:", ["o treino tem rótulos", "há erros", "informação do teste orienta o treinamento", "o modelo usa palavras"]),
        ("Acurácia é:", ["a proporção de positivos", "a parcela total de previsões corretas", "a média dos coeficientes", "a concordância entre anotadores"]),
        ("Precisão da classe positiva pergunta:", ["quantos casos existem", "quantos negativos foram encontrados", "quantos erros há no treino", "quantos positivos previstos eram positivos"]),
        ("Revocação da classe positiva pergunta:", ["quantos positivos existentes foram encontrados", "quantas previsões totais estavam corretas", "quantos termos existem", "qual é a classe majoritária"]),
        ("F1 combina:", ["acurácia e tamanho", "treino e teste", "precisão e revocação", "kappa e baseline"]),
        ("A matriz de confusão mostra:", ["somente acertos", "combinações entre observado e previsto", "coeficientes TF-IDF", "apenas falsos negativos"]),
        ("O desbalanceamento pode:", ["garantir F1 alto", "eliminar falsos positivos", "tornar o teste desnecessário", "tornar a acurácia isolada enganosa"]),
        ("Uma árvore excessivamente profunda tende a:", ["capturar regras específicas do treino", "ser sempre causal", "dispensar categorias", "impedir qualquer erro"]),
        ("TF-IDF representa documentos por:", ["coordenadas geográficas", "classes adjudicadas", "termos ponderados por frequência e raridade", "relações causais"]),
        ("O vocabulário TF-IDF deve ser ajustado:", ["no conjunto completo", "somente no treino", "somente nos erros", "depois de ler o teste"]),
        ("Um coeficiente de termo mede:", ["importância histórica intrínseca", "causalidade lexical", "qualidade da fonte", "associação daquele termo no modelo"]),
        ("Embeddings são:", ["representações densas aprendidas", "rótulos humanos", "matrizes de confusão", "guias de anotação"]),
        ("Métricas por grupo ajudam a:", ["provar equidade", "substituir leitura", "detectar desempenho desigual", "aumentar automaticamente a amostra"]),
        ("Sem categoria defensável, a entrega deve:", ["fabricar rótulos", "justificar a não adoção", "usar o teste como treino", "omitir a decisão"]),
    ]
    linhas = ["# U08-A08 — Exercícios de múltipla escolha", ""]
    for i, (enunciado, opcoes) in enumerate(questoes, 1):
        linhas += [f"## Questão {i}", enunciado + "  ", "  ".join(f"{letra}) {opcao}." for letra, opcao in zip("ABCD", opcoes)), ""]
    (UNIDADE / "exercicios_unidade_08_texto.md").write_text("\n".join(linhas), encoding="utf-8")


def gabaritos() -> None:
    p = UNIDADE / "gabaritos"; p.mkdir(parents=True, exist_ok=True)
    (p / "README.md").write_text('''# Gabaritos da Unidade 8

| Atividade | Notebook e título | Arquivo |
|---|---|---|
| U08-A01 | 00 — categoria ou descoberta? | `gabarito_00_guia.md` |
| U08-A02 | 01 — revisar o guia | `gabarito_01_anotacao.md` |
| U08-A03 | 02 — proteger o teste | `gabarito_02_treino_teste.md` |
| U08-A04 | 03 — custo do erro | `gabarito_03_modelos_erros.md` |
| U08-A05 | 04 — termos, atalhos e erros | `gabarito_04_textos.md` |
| U08-A06 | 05 — oficina | `gabarito_05_oficina.md` |
| U08-A07 | 05 — revisão por pares | `gabarito_05_oficina.md` |
| U08-A08 | exercícios | `gabarito_exercicios_multipla_escolha.md` |
''', encoding="utf-8")
    respostas = {
        "gabarito_00_guia.md": '''# Gabarito — contrato classificatório

**Atividade associada:** U08-A01 — Discussão em duplas — categoria ou descoberta?

“Contém hospital” é regra lexical verificável, mas inclui anúncio lateral. “Relevante
para saúde pública” exige interpretar assunto e contexto. Unidade: excerto. Um teatro
beneficente para hospital é limítrofe. Falso negativo oculta fonte potencial; falso
positivo aumenta leitura manual. **Resposta-modelo:** usar relevância quando a pesquisa
requer pertinência temática, com guia, dupla anotação e busca lexical como baseline.
''',
        "gabarito_01_anotacao.md": '''# Gabarito — anotação

**Atividade associada:** U08-A02 — Atividade integrada — revisar o guia pelos desacordos

O resultado executado é acordo bruto de 84,4% e kappa próximo de 0,690. D004 menciona
programação e saúde; as justificativas divergem sobre centralidade. Regra revisada:
“classifique como relevante somente se saúde motivar a ação principal; benefício
financeiro sem discussão sanitária não basta”. Novo teste: notícia de concerto cuja
renda compra medicamentos. A adjudicação é registrada, sem apagar A e B.
''',
        "gabarito_02_treino_teste.md": '''# Gabarito — treino e teste

**Atividade associada:** U08-A03 — Atividade — proteger o teste

A divisão estratificada com semente 42 produz 120 casos de treino e 40 de teste, com
20 casos por classe no teste. O baseline escolhe “não relevante” no empate: tem
acurácia 0,50, mas precisão, revocação e F1 iguais a zero para “relevante”. Isso mostra
por que acurácia isolada pode ocultar a falha completa na classe de interesse.
Escolher outra semente por melhorar o resultado vazaria informação da
avaliação para a decisão; preservo a divisão pré-registrada.
''',
        "gabarito_03_modelos_erros.md": '''# Gabarito — modelos e erros

**Atividade associada:** U08-A04 — Atividade integrada — escolher pelo custo do erro

Com apenas período e origem, os modelos não leem conteúdo e tendem a ficar próximos da
linha de base. Para triagem inclusiva, priorizo revocação, mas rejeito um modelo que
marca tudo como relevante: a precisão e a carga de leitura importam. A matriz e os
excertos mostram que o erro não é mero número. Relato métricas por período com `n` e
não afirmo equidade, pois há só 20 casos de teste por classe e dados sintéticos.
''',
        "gabarito_04_textos.md": '''# Gabarito — classificação textual

**Atividade associada:** U08-A05 — Atividade — termos, atalhos e erros

“vacinação” é termo substantivamente coerente; “salubridade pública” e “serviço
sanitário” podem funcionar como atalhos temporais. Um anúncio de remédio junto da
programação é ambíguo: palavra temática não garante centralidade. Proponho reservar o
período 1900–1909 inteiro como teste temporal e anotar novamente todos os textos
mistos, ocultando o rótulo anterior. Queda de desempenho indicaria dependência do
vocabulário do período, não simples falha técnica.
''',
        "gabarito_05_oficina.md": '''# Gabarito — oficina

**Atividades associadas:**

- U08-A06 — Oficina — incremento do relatório-notebook
- U08-A07 — Revisão por pares — reconstruir a decisão

## Exemplo de entrega

Pergunta: quais cartas devem ser priorizadas para leitura sobre migração? Categoria:
relevante quando deslocamento territorial é assunto, não simples topônimo. O notebook
preserva 25% para teste, compara maioria e TF-IDF, justifica revocação, apresenta matriz
e lê cinco falsos negativos. A métrica por década mostra onde falta anotação.

## Exemplo de parecer

Ponto claro: teste reservado antes do vocabulário. Dúvida: “mudança” aparece como
atalho? Prioridade: testar outra década. Decisão: aceita; acrescentado teste temporal e
conclusão limitada à coleção.
''',
    }
    for nome, texto in respostas.items(): (p / nome).write_text(texto, encoding="utf-8")
    justificativas = ["regra operacional", "consistência não é validade", "documenta resolução", "casos não usados", "preserva proporções", "comparação trivial", "teste influencia treino", "proporção correta", "positivos previstos", "positivos encontrados", "média harmônica", "tipos de resultado", "acurácia pode enganar", "sobreajuste", "frequência e raridade", "evita vazamento", "associação no modelo", "vetores densos", "desigualdade entre grupos", "não adoção coerente"]
    letras = list("BCADBACBDACBDACBDACB")
    tabela = ["# Gabarito — múltipla escolha", "", "**Atividade associada:** U08-A08 — Exercícios de múltipla escolha", "", "| Questão | Resposta | Justificativa |", "|---:|:---:|---|"]
    for i, (letra, just) in enumerate(zip(letras, justificativas), 1): tabela.append(f"| {i} | {letra} | {just}. |")
    tabela += ["", "**Exemplo de raciocínio (Questão 10):** se existem 20 relevantes e o modelo encontra 12, a revocação é 12/20 = 0,60. Os falsos positivos não entram nesse denominador; eles afetam a precisão."]
    (p / "gabarito_exercicios_multipla_escolha.md").write_text("\n".join(tabela) + "\n", encoding="utf-8")


def revisores() -> None:
    p = UNIDADE / "revisores"; p.mkdir(parents=True, exist_ok=True)
    (p / "README.md").write_text("# Revisores da Unidade 8\n\nExecute os seis pareceres e consolide correções antes da publicação.\n", encoding="utf-8")
    itens = [("01_nivel_academico.md", "Nível acadêmico", "validade das categorias, avaliação fora da amostra e precisão conceitual"), ("02_didatica.md", "Didática", "encadeamento, explicação antes do código e carga para estudantes de Humanidades"), ("03_alinhamento.md", "Alinhamento", "ementa, transição da Unidade 7 e preparação da Unidade 9"), ("04_humanidades_digitais.md", "Humanidades digitais", "interpretação, retorno aos documentos e não reificação das classes"), ("05_referencias.md", "Referências", "bibliografia acadêmica e documentação técnica primária"), ("06_tecnico_acessibilidade.md", "Técnica e acessibilidade", "execução, vazamento, sementes, rótulos e SVGs acessíveis")]
    for arq, tit, foco in itens: (p/arq).write_text(f"# Revisor — {tit}\n\nAvalie {foco}. Para cada achado, indique local, evidência, gravidade e correção verificável. Conclua com aprovado, aprovado com ajustes ou requer revisão.\n", encoding="utf-8")
    (p/"matriz_de_avaliacao.md").write_text("# Matriz de avaliação\n\n| Critério | Insuficiente | Adequado | Excelente |\n|---|---|---|---|\n| Categoria | implícita | guia básico | casos limítrofes revisam o guia |\n| Avaliação | treino = teste | teste reservado | baseline, erros e grupos |\n| Interpretação | só métrica | lê casos | erros reorientam o argumento |\n| Entrega | arquivo isolado | integra projeto | adoção ou recusa justificada |\n", encoding="utf-8")
    (p/"modelo_de_parecer.md").write_text("# Parecer da Unidade 8\n\n**Revisor:**  \n**Data:**  \n**Decisão:**  \n\n## Evidências\n\n## Correções prioritárias\n\n## Verificação\n", encoding="utf-8")


def main() -> None:
    for pasta in [UNIDADE, DADOS, UNIDADE / "imagens"]: pasta.mkdir(parents=True, exist_ok=True)
    criar_dados()
    imagens = [
        ("00_percurso_classificacao.svg", "Classificar é uma cadeia de decisões", "Categoria, anotação, separação, modelo e auditoria.", ["Categoria", "Anotação", "Treino|e teste", "Auditoria"], "A qualidade começa antes do algoritmo e termina nos casos."),
        ("01_anotacao.svg", "Da definição à adjudicação", "Fluxo de anotação independente e revisão do guia.", ["Conceito|e guia", "Anotação|independente", "Desacordos", "Adjudicação"], "Discordâncias são evidência para revisar a regra."),
        ("02_treino_teste.svg", "O teste permanece reservado", "Dados anotados dividem-se entre treino e teste.", ["Dados|anotados", "Treino|ajusta", "Teste|avalia"], "Consultar repetidamente o teste contamina a avaliação."),
        ("03_matriz_confusao.svg", "Quatro resultados, custos diferentes", "Verdadeiros e falsos positivos e negativos.", ["Observado", "Previsto", "Matriz|de confusão", "Custo|do erro"], "Uma métrica única não preserva todos os tipos de erro."),
        ("04_representacoes.svg", "Representar não é reproduzir", "Comparação conceitual entre TF-IDF e embeddings.", ["Texto", "TF-IDF|termos", "Embeddings|vetores", "Modelo"], "Toda representação seleciona sinais e perde contexto."),
        ("05_cadeia_entrega.svg", "Da regra à decisão responsável", "Entrega liga guia, avaliação, casos e limites.", ["Guia", "Baseline", "Erros", "Decisão"], "O mesmo relatório registra adoção ou não adoção."),
    ]
    for item in imagens: svg(*item)
    salvar("00_guia_da_unidade.ipynb", guia())
    salvar("01_categorias_anotacao_e_concordancia.ipynb", anotacao())
    salvar("02_treinamento_teste_e_linha_de_base.ipynb", treino_teste())
    salvar("03_modelos_metricas_e_erros.ipynb", modelos_erros())
    salvar("04_classificacao_textual_tfidf_e_embeddings.ipynb", textos())
    salvar("05_oficina_classificacao.ipynb", oficina(), dados=False)
    materiais(); gabaritos(); revisores()
    (UNIDADE/"imagens"/"README.md").write_text("# Ilustrações da Unidade 8\n\nSVGs autorais, locais, acessíveis e licenciados com o restante do repositório.\n", encoding="utf-8")
    (RAIZ/"notes"/"plano_unidade_08.md").write_text('''# Plano de execução — Unidade 8

## Escopo

Construir classificação supervisionada como decisão documentada: categoria, anotação,
teste reservado, baseline, modelo, métricas, erros, grupos e limites.

## Sequência

1. definir categoria e custo dos erros;
2. testar guia e concordância;
3. separar treino/teste e estabelecer baseline;
4. comparar logística e árvore com metadados;
5. classificar textos com TF-IDF e situar embeddings;
6. incorporar protótipo ou não adoção ao projeto cumulativo;
7. validar execução, atividades, gabaritos, referências e acessibilidade.

## Conclusão esperada

Seis notebooks executáveis; oito atividades; exemplos de resolução; dados fictícios
documentados; figuras acessíveis; links Colab e validador automatizado.
''', encoding="utf-8")


if __name__ == "__main__": main()
