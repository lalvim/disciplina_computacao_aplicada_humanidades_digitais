"""Constrói a Unidade 9 — agrupamentos e temas sem categorias prévias."""

from __future__ import annotations

import csv
import json
import random
from pathlib import Path
from textwrap import dedent

from apoio_colab import adicionar_link_na_abertura, preparacao_colab, tabela_links_colab

RAIZ = Path(__file__).resolve().parents[1]
UNIDADE = RAIZ / "unidade_09"
DADOS = UNIDADE / "dados"


def md(texto: str) -> dict:
    return {"cell_type": "markdown", "metadata": {}, "source": dedent(texto).strip().splitlines(keepends=True)}


def code(texto: str) -> dict:
    return {"cell_type": "code", "execution_count": None, "metadata": {}, "outputs": [], "source": dedent(texto).strip().splitlines(keepends=True)}


def salvar(nome: str, celulas: list[dict], dados: bool = True, scipy: bool = False) -> None:
    publicadas = [adicionar_link_na_abertura(celulas[0], UNIDADE.name, nome)]
    if dados:
        pacotes = [("sklearn", "scikit-learn>=1.5,<2")]
        if scipy: pacotes.append(("scipy", "scipy>=1.11,<2"))
        publicadas.append(code(preparacao_colab(UNIDADE.name, tuple(pacotes))))
    publicadas.extend(celulas[1:])
    doc = {"cells": publicadas, "metadata": {"kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"}, "language_info": {"name": "python", "version": "3"}}, "nbformat": 4, "nbformat_minor": 5}
    (UNIDADE/nome).write_text(json.dumps(doc, ensure_ascii=False, indent=1)+"\n", encoding="utf-8")


def criar_dados() -> None:
    DADOS.mkdir(parents=True, exist_ok=True); rng = random.Random(20261024)
    perfis = [(4200, 18, 9000, 380000), (14500, 55, 28000, 1250000), (7800, 95, 17000, 820000)]
    linhas = []
    for i in range(120):
        base = perfis[i % 3]
        regiao = ["Norte", "Nordeste", "Centro-Oeste", "Sudeste", "Sul"][i % 5]
        valores = [max(1, rng.gauss(base[0], base[0]*.18)), max(1, rng.gauss(base[1], base[1]*.18)), max(50, rng.gauss(base[2], base[2]*.18)), max(10000, rng.gauss(base[3], base[3]*.20))]
        linhas.append([f"I{i+1:03d}", f"Instituição Fictícia {i+1:03d}", regiao, *[round(v, 1) for v in valores]])
    with (DADOS/"instituicoes_culturais.csv").open("w", encoding="utf-8", newline="") as f:
        w=csv.writer(f); w.writerow(["id_instituicao","instituicao","regiao","itens_acervo","eventos_ano","publico_ano","orcamento_anual"]); w.writerows(linhas)

    vocab = {
        "saude": ["hospital vacina higiene epidemia cuidado", "médico posto prevenção doença atendimento", "salubridade remédio enfermaria campanha sanitária"],
        "educacao": ["escola professor aula aluno ensino", "biblioteca leitura curso matrícula educação", "colégio livro infância aprendizagem formação"],
        "cultura": ["teatro música exposição artista concerto", "museu patrimônio pintura festival cultura", "poesia espetáculo associação literária palco"],
    }
    docs=[]; temas=list(vocab)
    for i in range(180):
        ano=1890+i%30; periodo="1890–1899" if ano<1900 else ("1900–1909" if ano<1910 else "1910–1919")
        tema=temas[(i + (1 if ano>=1910 else 0))%3]
        palavra_nucleo={"saude":"saúde sanitária cuidado", "educacao":"educação escolar ensino", "cultura":"cultura artística patrimônio"}[tema]
        texto=palavra_nucleo + " " + rng.choice(vocab[tema])
        if i%7==0:
            outro=temas[(temas.index(tema)+1)%3]; texto += " " + " ".join(rng.choice(vocab[outro]).split()[:2])
        docs.append([f"T{i+1:03d}", ano, periodo, texto+f" registro {i+1}"])
    with (DADOS/"documentos_temas.csv").open("w", encoding="utf-8", newline="") as f:
        w=csv.writer(f); w.writerow(["id_documento","ano","periodo","texto"]); w.writerows(docs)
    dicio=[["id_instituicao","nominal","identificador fictício"],["itens_acervo","razão","itens catalogados simulados"],["eventos_ano","razão","eventos anuais simulados"],["publico_ano","razão","público anual simulado"],["orcamento_anual","razão","orçamento simulado"],["texto","texto","excerto sintético multitemático"]]
    with (DADOS/"dicionario_dados.csv").open("w", encoding="utf-8", newline="") as f:
        w=csv.writer(f); w.writerow(["variavel","tipo","descricao"]); w.writerows(dicio)
    prov={"natureza":"dados inteiramente fictícios","semente":20261024,"finalidade":"agrupamento numérico, textual e modelagem de tópicos","estrutura_didatica":"três perfis e três vocabulários latentes foram inseridos, com ruído e documentos mistos","limite":"clusters e tópicos não representam instituições, documentos ou grupos sociais reais"}
    (DADOS/"proveniencia.json").write_text(json.dumps(prov,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")


def svg(nome: str, titulo: str, desc: str, etapas: list[str], rodape: str) -> None:
    n=len(etapas); w=190 if n>=4 else 245; gap=(1000-80-n*w)/max(1,n-1); itens=[]
    for i,e in enumerate(etapas):
        x=40+i*(w+gap); partes=e.split("|"); itens.append(f'<rect x="{x:.0f}" y="82" width="{w}" height="118" rx="14" fill="#f4f0e6" stroke="#294c60" stroke-width="2"/>')
        for j,p in enumerate(partes): itens.append(f'<text x="{x+w/2:.0f}" y="{130+j*24}" text-anchor="middle" font-size="17" fill="#172b35">{p}</text>')
        if i<n-1: itens.append(f'<path d="M{x+w+6:.0f} 141 H{x+w+gap-8:.0f}" stroke="#a44a3f" stroke-width="3" marker-end="url(#a)"/>')
    texto=f'''<svg xmlns="http://www.w3.org/2000/svg" width="1000" height="285" viewBox="0 0 1000 285" role="img" aria-labelledby="title desc"><title id="title">{titulo}</title><desc id="desc">{desc}</desc><defs><marker id="a" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L0,6 L9,3 z" fill="#a44a3f"/></marker></defs><rect width="100%" height="100%" fill="#fffdf8"/><text x="500" y="40" text-anchor="middle" font-size="25" font-weight="bold" fill="#172b35">{titulo}</text>{''.join(itens)}<text x="500" y="250" text-anchor="middle" font-size="16" fill="#46565e">{rodape}</text></svg>'''
    (UNIDADE/"imagens"/nome).write_text(texto,encoding="utf-8")


def guia() -> list[dict]:
    return [md('''
    # Unidade 9 — Guia de estudo
    ## Como descobrir grupos e temas sem categorias prévias?

    Aprendizado não supervisionado encontra regularidades segundo uma representação,
    uma distância e um algoritmo escolhidos. Ele não revela automaticamente grupos
    sociais reais nem conceitos teóricos. A descoberta é uma hipótese organizada para
    voltar aos casos.

    ![O percurso passa por representação, distância, agrupamento e interpretação.](imagens/00_percurso_descoberta.svg)
    '''), md('''
    ## Percurso

    | Notebook | Pergunta | Produto |
    |---|---|---|
    | 00 | O que significa descobrir? | contrato interpretativo |
    | 01 | Como escala e distância mudam grupos? | K-means comparado |
    | 02 | Os grupos são estáveis e caracterizáveis? | hierarquia e sensibilidade |
    | 03 | Documentos se aproximam por quais palavras? | agrupamento TF-IDF |
    | 04 | Que misturas de temas aparecem? | LDA e evolução temporal |
    | 05 | Algum percurso serve ao projeto? | incremento ou não adoção |
    '''), code('''
    import json, pandas as pd
    instituicoes=pd.read_csv("dados/instituicoes_culturais.csv")
    documentos=pd.read_csv("dados/documentos_temas.csv")
    proveniencia=json.loads(open("dados/proveniencia.json",encoding="utf-8").read())
    print(proveniencia["natureza"]); print(len(instituicoes),"instituições e",len(documentos),"documentos")
    instituicoes.head(3)
    '''), md('''
    ### U09-A01 — Discussão em duplas — padrão, grupo ou hipótese?

    **Dinâmica (15 minutos):** compare “o algoritmo formou três clusters” com “existem
    três tipos naturais de instituição”. Liste as decisões intermediárias e reescreva a
    segunda frase como hipótese exploratória verificável nos casos e nas fontes.

    **Resposta:** escreva aqui.

    ## Passagem

    A primeira decisão escondida costuma ser a escala: orçamento pode dominar eventos
    apenas por usar números maiores. Começaremos tornando essa consequência visível.
    ''')]


def kmeans() -> list[dict]:
    return [md('''
    # Padronização, distância e K-means

    Distância traduz “semelhança” em regra geométrica. Na distância euclidiana,
    diferenças grandes pesam quadraticamente. Padronizar coloca cada variável em média
    zero e desvio-padrão um; isso não a torna neutra, apenas muda a pergunta.

    ![A mesma nuvem produz vizinhanças diferentes antes e depois da padronização.](imagens/01_escala_distancia.svg)
    '''), code('''
    import pandas as pd, matplotlib.pyplot as plt
    from sklearn.preprocessing import StandardScaler
    from sklearn.cluster import KMeans
    from sklearn.metrics import silhouette_score
    dados=pd.read_csv("dados/instituicoes_culturais.csv")
    variaveis=["itens_acervo","eventos_ano","publico_ano","orcamento_anual"]
    X=dados[variaveis]
    Xz=StandardScaler().fit_transform(X)
    sem_escala=KMeans(n_clusters=3,random_state=42,n_init=20).fit_predict(X)
    com_escala=KMeans(n_clusters=3,random_state=42,n_init=20).fit_predict(Xz)
    comparacao=pd.crosstab(sem_escala,com_escala,rownames=["sem padronizar"],colnames=["padronizado"])
    display(comparacao)
    '''), md('''
    ## 2. Escolher $k$ sem procurar um número mágico

    K-means minimiza distâncias quadráticas aos centroides e pressupõe grupos
    aproximadamente compactos. Inércia sempre cai quando $k$ cresce. Silhueta compara
    coesão e separação entre -1 e 1, mas não decide relevância humanística.
    '''), code('''
    avaliacoes=[]
    for k in range(2,7):
        rotulos=KMeans(n_clusters=k,random_state=42,n_init=20).fit_predict(Xz)
        avaliacoes.append({"k":k,"inercia":KMeans(n_clusters=k,random_state=42,n_init=20).fit(Xz).inertia_,"silhueta":silhouette_score(Xz,rotulos)})
    tabela_k=pd.DataFrame(avaliacoes)
    display(tabela_k.round(3))
    fig,ax=plt.subplots(1,2,figsize=(10,4)); ax[0].plot(tabela_k.k,tabela_k.inercia,marker="o"); ax[0].set(title="Inércia",xlabel="k"); ax[1].plot(tabela_k.k,tabela_k.silhueta,marker="o"); ax[1].set(title="Silhueta",xlabel="k",ylim=(-1,1)); plt.tight_layout(); plt.show()
    modelo_k=KMeans(n_clusters=3,random_state=42,n_init=20)
    dados["cluster_kmeans"]=modelo_k.fit_predict(Xz)
    '''), md('''
    ### U09-A02 — Atividade integrada — escala e número de grupos

    Compare rótulos com e sem padronização, examine $k=2$ a $6$ e escolha duas soluções
    plausíveis. Para cada uma, diga o que a métrica favorece e que questão substantiva
    ainda falta responder. **Dinâmica (30 minutos):** individual na execução e dupla na
    decisão; não escolha apenas o maior valor.

    **Resposta:** escreva aqui.

    ## Passagem

    Uma partição não basta. Precisamos caracterizar seus casos, compará-la a outro
    algoritmo e verificar se pequenas mudanças alteram a conclusão.
    ''')]


def hierarquia() -> list[dict]:
    return [md('''
    # Agrupamento hierárquico, caracterização e estabilidade

    O agrupamento hierárquico aglomerativo começa com casos separados e os reúne. O
    dendrograma mostra uma sequência de fusões, não uma taxonomia pronta. Cortá-lo em
    três grupos é uma decisão analítica.

    ![Casos se fundem sucessivamente e um corte define a partição.](imagens/02_hierarquia.svg)
    '''), code('''
    import numpy as np, pandas as pd, matplotlib.pyplot as plt
    from sklearn.preprocessing import StandardScaler
    from sklearn.cluster import KMeans, AgglomerativeClustering
    from sklearn.metrics import adjusted_rand_score
    from scipy.cluster.hierarchy import linkage, dendrogram
    dados=pd.read_csv("dados/instituicoes_culturais.csv")
    variaveis=["itens_acervo","eventos_ano","publico_ano","orcamento_anual"]
    Xz=StandardScaler().fit_transform(dados[variaveis])
    dados["cluster_hierarquico"]=AgglomerativeClustering(n_clusters=3,linkage="ward").fit_predict(Xz)
    Z=linkage(Xz,method="ward")
    plt.figure(figsize=(11,4)); dendrogram(Z,no_labels=True,color_threshold=None); plt.title("Dendrograma de Ward — dados fictícios"); plt.xlabel("Casos"); plt.ylabel("Distância de fusão"); plt.tight_layout(); plt.show()
    '''), md('''
    ## 2. Caracterizar sem batizar cedo demais

    Médias descrevem perfis, mas nomes como “modernas” ou “precárias” acrescentariam
    julgamento não contido nos dados. Comece por rótulos neutros e examine casos
    próximos e distantes do centro antes de propor uma interpretação contextual.
    '''), code('''
    perfil=dados.groupby("cluster_hierarquico")[variaveis].agg(["mean","median","count"])
    display(perfil.round(1))
    display(pd.crosstab(dados["cluster_hierarquico"],dados["regiao"],normalize="index").round(2))
    '''), md('''
    ## 3. Estabilidade: a solução resiste a perturbações?

    Repetimos K-means em subamostras de 80% e comparamos os rótulos dos casos comuns
    pelo índice de Rand ajustado (ARI), que é invariável à troca dos números dos
    clusters. A simulação não substitui validação externa, mas revela fragilidade.
    '''), code('''
    referencia=KMeans(n_clusters=3,random_state=42,n_init=20).fit_predict(Xz)
    estabilidade=[]
    rng=np.random.default_rng(42)
    for repeticao in range(20):
        idx=np.sort(rng.choice(len(Xz),size=int(.8*len(Xz)),replace=False))
        parcial=KMeans(n_clusters=3,random_state=repeticao,n_init=20).fit_predict(Xz[idx])
        estabilidade.append(adjusted_rand_score(referencia[idx],parcial))
    tabela_estabilidade=pd.Series(estabilidade,name="ARI").describe()
    display(tabela_estabilidade.round(3))
    '''), md('''
    ### U09-A03 — Atividade — perfil, casos e estabilidade

    Descreva os três grupos sem adjetivos valorativos; escolha dois casos de cada grupo
    para inspeção; compare hierarquia e K-means; interprete mínimo, mediana e máximo do
    ARI. **Dinâmica (35 minutos):** trios, com papéis de cálculo, leitura de casos e
    crítica dos nomes. Proponham nomes somente ao final e marquem-nos como hipóteses.

    **Resposta:** escreva aqui.

    ## Passagem

    Variáveis numéricas tinham dimensões previamente definidas. Em textos, a própria
    representação lexical decide quais semelhanças podem aparecer.
    ''')]


def textos() -> list[dict]:
    return [md('''
    # Agrupamento de documentos

    Representaremos excertos com TF-IDF e distância cosseno implícita na normalização.
    K-means ainda agrupa vetores; interpretar exige examinar termos característicos e
    documentos, não apenas projetar pontos coloridos.

    ![Textos tornam-se vetores, recebem grupos e retornam à leitura.](imagens/03_textos_clusters.svg)
    '''), code('''
    import numpy as np, pandas as pd
    from sklearn.feature_extraction.text import TfidfVectorizer
    from sklearn.cluster import KMeans
    from sklearn.metrics import silhouette_score
    documentos=pd.read_csv("dados/documentos_temas.csv")
    vetorizador=TfidfVectorizer(min_df=2,ngram_range=(1,2),stop_words=None)
    Xtexto=vetorizador.fit_transform(documentos["texto"])
    modelo_texto=KMeans(n_clusters=3,random_state=42,n_init=20)
    documentos["cluster_texto"]=modelo_texto.fit_predict(Xtexto)
    silhueta_texto=silhouette_score(Xtexto,documentos["cluster_texto"],metric="cosine")
    print(f"Silhueta cosseno: {silhueta_texto:.3f}")
    '''), md('''
    ## 2. Termos e documentos representativos

    Os termos mais próximos do centro ajudam a descrever o padrão lexical. O documento
    mais próximo do centro é um exemplar matemático, não necessariamente o mais
    importante historicamente. Documentos distantes podem ser mistos ou revelar falha
    da representação.
    '''), code('''
    termos=vetorizador.get_feature_names_out(); centros=modelo_texto.cluster_centers_
    termos_cluster=[]
    for c in range(3):
        top=centros[c].argsort()[-8:][::-1]
        termos_cluster.append({"cluster":c,"termos":"; ".join(termos[top])})
    display(pd.DataFrame(termos_cluster))

    distancias=modelo_texto.transform(Xtexto)
    documentos["distancia_ao_centro"]=distancias[np.arange(len(documentos)),documentos["cluster_texto"]]
    amostra_casos=pd.concat([g.nsmallest(2,"distancia_ao_centro") for _,g in documentos.groupby("cluster_texto")])
    display(amostra_casos[["id_documento","periodo","cluster_texto","distancia_ao_centro","texto"]])
    '''), md('''
    ### U09-A04 — Atividade — do vetor ao documento

    Para cada cluster, proponha um nome descritivo apoiado em termos e dois documentos.
    Depois leia dois documentos mais distantes do próprio centro e registre se são
    híbridos, ruidosos ou mal representados. Compare a distribuição por período sem
    concluir automaticamente que o tema “cresceu”.

    **Dinâmica (30 minutos):** duplas; uma nomeia pelos termos, outra tenta refutar o
    nome pelos casos. A versão final deve registrar evidência favorável e exceção.

    **Resposta:** escreva aqui.

    ## Passagem

    Clusters atribuem um grupo predominante. A modelagem de tópicos permite que cada
    documento seja uma mistura, mas os componentes continuam sendo padrões estatísticos.
    ''')]


def topicos() -> list[dict]:
    return [md('''
    # Modelagem de tópicos com LDA

    No LDA, cada documento é uma **mistura de tópicos**, e tópicos são distribuições de palavras.
    “Tópico” é um componente probabilístico, não sinônimo automático de tema teórico.
    O número de tópicos e o pré-processamento condicionam o resultado.

    ![Documentos misturam tópicos, e tópicos distribuem probabilidades sobre palavras.](imagens/04_lda.svg)
    '''), code('''
    import numpy as np, pandas as pd, matplotlib.pyplot as plt
    from sklearn.feature_extraction.text import CountVectorizer
    from sklearn.decomposition import LatentDirichletAllocation
    documentos=pd.read_csv("dados/documentos_temas.csv")
    contagem=CountVectorizer(min_df=2)
    Xcontagem=contagem.fit_transform(documentos["texto"])
    lda=LatentDirichletAllocation(
        n_components=3, random_state=42, learning_method="batch", max_iter=80,
        doc_topic_prior=.1, topic_word_prior=.1
    )
    mistura=lda.fit_transform(Xcontagem)
    termos=contagem.get_feature_names_out()
    descricoes=[]
    for t,pesos in enumerate(lda.components_):
        top=pesos.argsort()[-10:][::-1]
        descricoes.append({"topico":t,"palavras":"; ".join(termos[top])})
    tabela_topicos=pd.DataFrame(descricoes)
    display(tabela_topicos)
    '''), md('''
    ## 2. Misturas e nomeação

    Nomear requer ler documentos com alta proporção e documentos mistos. Um rótulo
    curto é interpretação provisória; mantenha também as palavras e exemplos que o
    sustentam para que outra pessoa possa discordar.
    '''), code('''
    for t in range(3): documentos[f"topico_{t}"]=mistura[:,t]
    documentos["topico_predominante"]=mistura.argmax(axis=1)
    casos=[]
    for t in range(3):
        amostra=documentos.nlargest(3,f"topico_{t}")[["id_documento","texto",f"topico_{t}"]].copy()
        amostra=amostra.rename(columns={f"topico_{t}":"proporcao_topico"})
        amostra["topico"]=t
        casos.append(amostra)
    casos_topicos=pd.concat(casos,ignore_index=True)
    display(casos_topicos[["topico","proporcao_topico","id_documento","texto"]])
    '''), md('''
    ## 3. Evolução temporal sem confundir composição e mudança histórica

    Agregamos proporções médias por período. Uma curva pode mudar porque o corpus mudou,
    porque palavras mudaram de sentido ou porque a simulação alterou a composição. O
    gráfico gera perguntas para inspeção documental; não explica sozinho o processo.
    '''), code('''
    colunas_topicos=[f"topico_{t}" for t in range(3)]
    evolucao=documentos.groupby("periodo")[colunas_topicos].mean()
    display(evolucao.round(3))
    evolucao.plot(marker="o",ylim=(0,1),title="Proporção média dos tópicos — dados fictícios")
    plt.ylabel("Proporção média"); plt.xlabel("Período"); plt.tight_layout(); plt.show()
    '''), md('''
    ### U09-A05 — Atividade — tópicos como hipóteses

    Nomeie cada tópico usando palavras e três documentos; identifique ao menos um caso
    misto; escolha uma mudança temporal e formule duas explicações alternativas, uma
    substantiva e outra ligada ao corpus. **Dinâmica (35 minutos):** grupos de três
    defendem nomes diferentes e preservam a divergência no registro.

    **Resposta:** escreva aqui.

    ## Passagem

    A oficina exige escolher entre perfis numéricos, clusters textuais, tópicos ou não
    adoção. Mais métodos não significam automaticamente mais evidência.
    ''')]


def oficina() -> list[dict]:
    return [md('''
    # Oficina — perfis, agrupamentos ou temas

    **Produto:** uma seção no mesmo relatório-notebook cumulativo. Escolha apenas um
    percurso coerente — perfis numéricos, agrupamento textual ou tópicos — ou justifique
    a não adoção. Não entregue um arquivo separado.

    ![Representação e sensibilidade sustentam uma interpretação que retorna aos casos.](imagens/05_cadeia_entrega.svg)
    '''), md('''
    ## Roteiro de 75 minutos

    | Tempo | Ação | Evidência |
    |---:|---|---|
    | 0–12 | justificar pergunta exploratória | pergunta e unidade |
    | 12–25 | definir representação e distância | quadro de decisões |
    | 25–42 | comparar duas especificações | tabela/gráfico |
    | 42–55 | caracterizar e testar estabilidade | perfis e sensibilidade |
    | 55–66 | voltar a casos típicos e exceções | amostra comentada |
    | 66–75 | limitar e integrar a conclusão | parágrafo no projeto |

    ### U09-A06 — Oficina — incremento do relatório-notebook

    **Dinâmica:** trabalhe no próprio projeto. A pessoa docente verifica representação
    aos 25 minutos e casos aos 55. Inclua pergunta, unidades, escolhas, duas
    especificações, estabilidade, nomes provisórios, casos e limites.

    **Resposta:** inclua no mesmo relatório-notebook.

    ### U09-A07 — Revisão por pares — desfazer a reificação

    **Dinâmica (20 minutos):** o colega sublinha frases que tratam cluster/tópico como
    entidade natural, tenta reconstruir os nomes pelos casos e propõe uma especificação
    alternativa. Registra um ponto claro, uma dúvida e uma mudança prioritária.

    **Resposta:** anexe parecer e decisão do autor.

    ## Critérios e fechamento

    Avalie coerência da representação, comparação de soluções, estabilidade, retorno
    aos casos, prudência na nomeação e integração humanística. A Unidade 10 passará da
    descoberta de padrões à extração explícita de entidades, relações e eventos.
    ''')]


QUESTOES = [
    ("Aprendizado não supervisionado", ["usa sempre rótulos prévios","busca padrões sem alvo anotado","prova grupos reais","dispensa decisões"],"B","busca padrões sem alvo anotado"),
    ("Padronizar variáveis", ["elimina viés","torna categorias causais","coloca escalas em base comparável","remove extremos"],"C","coloca escalas em base comparável"),
    ("A distância euclidiana", ["formaliza uma noção de proximidade","é neutra","serve só a textos","define causalidade"],"A","formaliza proximidade escolhida"),
    ("K-means procura", ["tópicos probabilísticos","rótulos humanos","árvores causais","minimizar distâncias aos centroides"],"D","minimiza distâncias aos centroides"),
    ("A inércia ao aumentar k", ["sempre aumenta","tende a diminuir","fica igual","mede validade externa"],"B","tende a diminuir"),
    ("Silhueta alta sugere", ["coesão e separação geométrica","grupo social real","causalidade","nome correto"],"A","resume coesão e separação"),
    ("Um dendrograma mostra", ["probabilidades","erros de anotação","sequência de fusões","classes verdadeiras"],"C","mostra fusões hierárquicas"),
    ("Cortar o dendrograma", ["é decisão analítica","é automático","remove casos","prova taxonomia"],"A","define uma partição escolhida"),
    ("Caracterizar cluster exige", ["apenas cor","somente tamanho","nome imediato","perfis e casos"],"D","combina perfis e casos"),
    ("ARI compara", ["médias","partições sem depender dos números dos rótulos","tópicos e palavras","causalidade"],"B","compara partições"),
    ("Estabilidade alta", ["prova realidade social","dispensa fontes","não garante validade substantiva","define nome"],"C","não garante validade substantiva"),
    ("TF-IDF enfatiza", ["termos frequentes no documento e raros na coleção","datas apenas","rótulos","coordenadas"],"A","pondera frequência e raridade"),
    ("Centroide textual é", ["documento histórico","conceito teórico","verdade de campo","resumo vetorial"],"D","é resumo vetorial"),
    ("Documento típico matemático", ["é sempre importante","é próximo do centro","é causal","não precisa leitura"],"B","é próximo do centro"),
    ("No LDA, documento é", ["uma única classe","um erro","mistura de tópicos","um centroide"],"C","é mistura de tópicos"),
    ("No LDA, tópico é", ["distribuição sobre palavras","conceito provado","grupo social","período"],"A","é distribuição sobre palavras"),
    ("Nomear tópico", ["encerra análise","é interpretação provisória","é automático","dispensa exemplos"],"B","é interpretação provisória"),
    ("Mudança de tópico no tempo", ["prova processo histórico","é sempre ruído","elimina viés","pode refletir composição do corpus"],"D","pode refletir o corpus"),
    ("Comparar especificações ajuda a", ["escolher maior gráfico","provar categorias","avaliar sensibilidade","remover exceções"],"C","avalia sensibilidade"),
    ("Sem pertinência ao projeto", ["forçar três clusters","justificar não adoção","inventar texto","ocultar decisão"],"B","justifica não adoção"),
]


def materiais() -> None:
    nbs=(("Guia","00_guia_da_unidade.ipynb"),("K-means","01_padronizacao_distancia_e_kmeans.ipynb"),("Hierarquia e estabilidade","02_hierarquia_caracterizacao_e_estabilidade.ipynb"),("Agrupamento textual","03_agrupamento_de_documentos.ipynb"),("LDA e evolução","04_modelagem_de_topicos_e_tempo.ipynb"),("Oficina","05_oficina_agrupamentos_e_temas.ipynb"))
    (UNIDADE/"README.md").write_text(f'''# Unidade 9 — Agrupamentos e temas

Execute os notebooks 00 a 05. A unidade explora padrões sem categorias prévias, sem
confundir resultados algorítmicos com grupos naturais.

## Abrir no Google Colab

{tabela_links_colab("unidade_09",nbs)}

Execute **Preparação do ambiente** nos Notebooks 00 a 04. A oficina atualiza o mesmo
relatório-notebook cumulativo. Os dados são inteiramente fictícios.

## Materiais

Dados e proveniência em `dados/`; exercícios em `exercicios_unidade_09_texto.md`;
resoluções em `gabaritos/`; bibliografia em `referencias.md`; diagramas acessíveis em
`imagens/`; instrumentos editoriais em `revisores/`.
''',encoding="utf-8")
    (UNIDADE/"referencias.md").write_text('''# Referências da Unidade 9

- HASTIE, Trevor; TIBSHIRANI, Robert; FRIEDMAN, Jerome. *The Elements of Statistical Learning*. 2. ed. Springer, 2009. Capítulos de aprendizado não supervisionado.
- KAUFMAN, Leonard; ROUSSEEUW, Peter J. *Finding Groups in Data*. Wiley, 1990. Distâncias, caracterização e avaliação crítica de agrupamentos.
- ROUSSEEUW, Peter J. Silhouettes: a graphical aid to interpretation and validation of cluster analysis. *Journal of Computational and Applied Mathematics*, 1987.
- BISHOP, Christopher M. *Pattern Recognition and Machine Learning*. Springer, 2006. Modelos de mistura e aprendizado não supervisionado.
- BLEI, David M.; NG, Andrew Y.; JORDAN, Michael I. Latent Dirichlet Allocation. *Journal of Machine Learning Research*, v. 3, 2003.
- GRIMMER, Justin; STEWART, Brandon M. Text as data. *Political Analysis*, v. 21, n. 3, 2013. Interpretação e validação de métodos textuais.
- BAUMER, Eric P. S. et al. Comparing grounded theory and topic modeling. In: *ICML Workshop on Human Interpretability in Machine Learning*, 2017.

Documentação técnica: guias oficiais do scikit-learn para clustering, K-means,
silhueta, TF-IDF e LDA. Os exemplos locais são sintéticos.
''',encoding="utf-8")
    linhas=["# U09-A08 — Exercícios de múltipla escolha",""]
    for i,(q,ops,_,_) in enumerate(QUESTOES,1): linhas += [f"## Questão {i}",q+":  ","  ".join(f"{l}) {o}." for l,o in zip("ABCD",ops)),""]
    (UNIDADE/"exercicios_unidade_09_texto.md").write_text("\n".join(linhas),encoding="utf-8")


def gabaritos() -> None:
    p=UNIDADE/"gabaritos"; p.mkdir(parents=True,exist_ok=True)
    (p/"README.md").write_text('''# Gabaritos da Unidade 9

| Atividade | Notebook e título | Arquivo |
|---|---|---|
| U09-A01 | 00 — padrão, grupo ou hipótese? | `gabarito_00_guia.md` |
| U09-A02 | 01 — escala e número de grupos | `gabarito_01_kmeans.md` |
| U09-A03 | 02 — perfil, casos e estabilidade | `gabarito_02_hierarquia.md` |
| U09-A04 | 03 — do vetor ao documento | `gabarito_03_textos.md` |
| U09-A05 | 04 — tópicos como hipóteses | `gabarito_04_topicos.md` |
| U09-A06 | 05 — oficina | `gabarito_05_oficina.md` |
| U09-A07 | 05 — revisão por pares | `gabarito_05_oficina.md` |
| U09-A08 | exercícios | `gabarito_exercicios_multipla_escolha.md` |
''',encoding="utf-8")
    textos={
    "gabarito_00_guia.md":'''# Gabarito — contrato interpretativo

**Atividade associada:** U09-A01 — Discussão em duplas — padrão, grupo ou hipótese?

Três clusters resultam de variáveis, escalas, distância, algoritmo, $k$ e semente. A
frase defensável é: “Com quatro indicadores padronizados e K-means com $k=3$, emergem
três perfis geométricos; investigaremos se suas diferenças correspondem a histórias
institucionais observáveis”. A leitura exige documentos e comparação de especificações.
''',
    "gabarito_01_kmeans.md":'''# Gabarito — K-means

**Atividade associada:** U09-A02 — Atividade integrada — escala e número de grupos

A tabela cruzada mostra se orçamento dominou a solução sem escala. Após padronizar,
$k=3$ tende a ter boa silhueta porque a base foi construída com três perfis; isso é
conhecido apenas pela proveniência didática. Comparo também $k=2$: pode resumir escala
institucional, enquanto $k=3$ separa instituições com muitos eventos. Escolho $k=3$
como hipótese de leitura, não como descoberta de três tipos reais.
''',
    "gabarito_02_hierarquia.md":'''# Gabarito — hierarquia e estabilidade

**Atividade associada:** U09-A03 — Atividade — perfil, casos e estabilidade

Descrevo “grupo com maior acervo e público”, “grupo com mais eventos” e “grupo de
menores valores médios”, sem usar “avançado” ou “precário”. Leio duas instituições de
cada grupo e comparo a composição regional. ARI próximo de 1 nas subamostras indica
consistência geométrica nesta simulação, mas não valida os nomes nem generaliza para
instituições reais. Diferenças entre Ward e K-means são mantidas como evidência.
''',
    "gabarito_03_textos.md":'''# Gabarito — documentos

**Atividade associada:** U09-A04 — Atividade — do vetor ao documento

Os termos sugerem provisoriamente saúde, educação e cultura. Para cada rótulo, cito
dois excertos próximos do centro. Documentos distantes combinam palavras de dois
vocabulários e impedem tratar fronteiras como puras. Uma mudança da proporção por
período pode refletir a composição artificial da coleção; seria necessário comparar
volumes, cobertura e sentidos dos termos antes de narrar mudança histórica.
''',
    "gabarito_04_topicos.md":'''# Gabarito — tópicos

**Atividade associada:** U09-A05 — Atividade — tópicos como hipóteses

Nomeio os componentes por palavras e três documentos de alta proporção, preservando a
tabela original. Um excerto com “teatro beneficente” pode misturar cultura e saúde.
Para uma curva crescente, hipótese substantiva: institucionalização do assunto;
alternativa documental: aumento de fontes daquele gênero ou vocabulário. O gráfico
orienta inspeção, não decide entre explicações.
''',
    "gabarito_05_oficina.md":'''# Gabarito — oficina

**Atividades associadas:**

- U09-A06 — Oficina — incremento do relatório-notebook
- U09-A07 — Revisão por pares — desfazer a reificação

## Exemplo de entrega

Pergunta: que perfis de circulação aparecem nas revistas? Padronizo tiragem, páginas e
periodicidade; comparo K-means $k=2/3$, Ward e subamostras; descrevo centroides e leio
casos centrais e exceções. Conclusão: “perfis computacionais nesta base”, não “tipos de
revista”. O parecer pediu remover “revistas modernas”; substituí pelo perfil observado
e registrei a mudança.
'''}
    for nome,texto in textos.items(): (p/nome).write_text(texto,encoding="utf-8")
    linhas=["# Gabarito — múltipla escolha","","**Atividade associada:** U09-A08 — Exercícios de múltipla escolha","","| Questão | Resposta | Justificativa |","|---:|:---:|---|"]
    for i,(_,_,letra,just) in enumerate(QUESTOES,1): linhas.append(f"| {i} | {letra} | {just}. |")
    linhas += ["","**Exemplo de raciocínio (Questão 18):** se a proporção média de um tópico cresce, primeiro verifico número e gêneros dos documentos por período. Sem cobertura comparável, a curva pode descrever o corpus, não o mundo histórico."]
    (p/"gabarito_exercicios_multipla_escolha.md").write_text("\n".join(linhas)+"\n",encoding="utf-8")


def revisores() -> None:
    p=UNIDADE/"revisores"; p.mkdir(parents=True,exist_ok=True)
    (p/"README.md").write_text("# Revisores da Unidade 9\n\nExecute seis pareceres e consolide correções antes da publicação.\n",encoding="utf-8")
    itens=[("01_nivel_academico.md","Nível acadêmico","distância, algoritmos, estabilidade e não reificação"),("02_didatica.md","Didática","transições, explicação do código e carga cognitiva"),("03_alinhamento.md","Alinhamento","ementa, passagem da classificação e produto cumulativo"),("04_humanidades_digitais.md","Humanidades digitais","retorno aos casos, historicidade e crítica das categorias"),("05_referencias.md","Referências","fontes acadêmicas e documentação técnica primária"),("06_tecnico_acessibilidade.md","Técnica e acessibilidade","execução, sementes, gráficos, LaTeX e SVGs")]
    for arq,tit,foco in itens: (p/arq).write_text(f"# Revisor — {tit}\n\nAvalie {foco}. Registre local, evidência, gravidade e correção verificável; conclua com aprovado, aprovado com ajustes ou requer revisão.\n",encoding="utf-8")
    (p/"matriz_de_avaliacao.md").write_text("# Matriz de avaliação\n\n| Critério | Insuficiente | Adequado | Excelente |\n|---|---|---|---|\n| Representação | implícita | documentada | alternativas comparadas |\n| Estabilidade | ausente | medida | muda a interpretação |\n| Casos | só centroides | exemplos lidos | exceções refutam nomes |\n| Linguagem | reifica | limita | preserva hipóteses rivais |\n",encoding="utf-8")
    (p/"modelo_de_parecer.md").write_text("# Parecer da Unidade 9\n\n**Revisor:**  \n**Data:**  \n**Decisão:**  \n\n## Evidências\n\n## Correções\n\n## Verificação\n",encoding="utf-8")


def main() -> None:
    for p in [UNIDADE,DADOS,UNIDADE/"imagens"]: p.mkdir(parents=True,exist_ok=True)
    criar_dados()
    imagens=[
    ("00_percurso_descoberta.svg","Descoberta como hipótese","Representação, distância, algoritmo e interpretação.",["Representação","Distância","Algoritmo","Casos"],"Mudar uma decisão pode mudar o padrão encontrado."),
    ("01_escala_distancia.svg","Escala redefine vizinhanças","Comparação antes e depois da padronização.",["Valores|originais","Padronização","Distâncias","Clusters"],"Proximidade é uma regra construída."),
    ("02_hierarquia.svg","Fusões e cortes","Agrupamento hierárquico como sequência de fusões.",["Casos","Fusões","Dendrograma","Corte"],"O corte escolhido não é uma taxonomia natural."),
    ("03_textos_clusters.svg","Do texto ao caso","Texto, TF-IDF, cluster e releitura.",["Textos","TF-IDF","Clusters","Releitura"],"Termos descrevem; documentos contestam."),
    ("04_lda.svg","Documentos como misturas","Relação entre palavras, tópicos e documentos.",["Palavras","Tópicos","Misturas","Tempo"],"Um tópico estatístico não equivale a um conceito teórico."),
    ("05_cadeia_entrega.svg","Uma descoberta auditável","Decisões, sensibilidade, casos e limites.",["Pergunta","Soluções","Estabilidade","Limites"],"O projeto incorpora hipótese, não essência."),]
    for item in imagens: svg(*item)
    salvar("00_guia_da_unidade.ipynb",guia()); salvar("01_padronizacao_distancia_e_kmeans.ipynb",kmeans()); salvar("02_hierarquia_caracterizacao_e_estabilidade.ipynb",hierarquia(),scipy=True); salvar("03_agrupamento_de_documentos.ipynb",textos()); salvar("04_modelagem_de_topicos_e_tempo.ipynb",topicos()); salvar("05_oficina_agrupamentos_e_temas.ipynb",oficina(),dados=False)
    materiais(); gabaritos(); revisores()
    (UNIDADE/"imagens"/"README.md").write_text("# Ilustrações da Unidade 9\n\nSVGs autorais, locais e acessíveis.\n",encoding="utf-8")
    (RAIZ/"notes"/"plano_unidade_09.md").write_text("# Plano de execução — Unidade 9\n\nConstruir progressivamente padronização e distâncias, K-means, hierarquia, caracterização, estabilidade, agrupamento textual e LDA; retornar aos casos; incorporar um percurso pertinente ou não adoção ao mesmo relatório-notebook; validar execução, atividades, referências e acessibilidade.\n",encoding="utf-8")


if __name__=="__main__": main()
