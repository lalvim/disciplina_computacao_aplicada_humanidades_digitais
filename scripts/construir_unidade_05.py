"""Constrói a Unidade 5 — comparação quantitativa e textual."""

from __future__ import annotations

import csv
import json
import shutil
from pathlib import Path
from textwrap import dedent

from apoio_colab import adicionar_link_na_abertura, preparacao_colab, tabela_links_colab

RAIZ = Path(__file__).resolve().parents[1]
UNIDADE = RAIZ / "unidade_05"
DADOS = UNIDADE / "dados"


def texto(conteudo: str) -> dict:
    valor = dedent(conteudo).strip()
    linhas = ["$$" if linha in {r"\[", r"\]"} else linha for linha in valor.splitlines()]
    valor = "\n".join(linhas).replace(r"\(", "$").replace(r"\)", "$")
    return {"cell_type": "markdown", "metadata": {}, "source": valor.splitlines(keepends=True)}


def codigo(conteudo: str) -> dict:
    return {"cell_type": "code", "execution_count": None, "metadata": {}, "outputs": [], "source": dedent(conteudo).strip().splitlines(keepends=True)}


def notebook(nome: str, celulas: list[dict], requer_dados: bool = False) -> None:
    publicadas = [adicionar_link_na_abertura(celulas[0], UNIDADE.name, nome)]
    if requer_dados:
        publicadas.append(codigo(preparacao_colab(UNIDADE.name)))
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
    origem_documentos = RAIZ / "unidade_04" / "dados" / "documentos.csv"
    shutil.copyfile(origem_documentos, DADOS / "documentos.csv")
    with origem_documentos.open(encoding="utf-8") as arquivo:
        registros = list(csv.DictReader(arquivo))[:12]
    genero_contexto = {
        "editorial": "A direção argumenta sobre prioridades e futuro coletivo.",
        "notícia": "A notícia descreve acontecimentos, locais e participantes.",
        "carta": "A pessoa remetente comenta experiência, dúvida e reivindicação.",
    }
    local_contexto = {
        "Capital": "O debate menciona conselho urbano, circulação e orçamento.",
        "Interior": "O debate menciona distrito, distância e associação local.",
    }
    for i, registro in enumerate(registros):
        registro["texto_comparacao"] = " ".join([
            registro["texto"], genero_contexto[registro["genero"]],
            local_contexto[registro["local"]], f"marca didática documento {i+1}",
        ])
    campos = list(registros[0])
    with (DADOS / "documentos_comparacao.csv").open("w", encoding="utf-8", newline="") as arquivo:
        gravador = csv.DictWriter(arquivo, fieldnames=campos)
        gravador.writeheader()
        gravador.writerows(registros)
    versoes = [
        ["V001", "D001", "transcrição A", "A escola noturna amplia a instrução pública."],
        ["V002", "D001", "transcrição B", "A escola noturna amplia instrução pública."],
        ["V003", "D002", "OCR bruto", "O trabalho nas oficinas reune jornada salario e associação."],
        ["V004", "D002", "revisada", "O trabalho nas oficinas reúne jornada, salário e associação."],
        ["V005", "D003", "edição 1", "A estrada e a máquina anunciam progresso e conflito."],
        ["V006", "D003", "edição 2", "A nova estrada e a máquina anunciam progresso, mas também conflito."],
    ]
    with (DADOS / "versoes_textuais.csv").open("w", encoding="utf-8", newline="") as arquivo:
        gravador = csv.writer(arquivo)
        gravador.writerow(["id_versao", "id_documento", "tipo_versao", "texto"])
        gravador.writerows(versoes)
    proveniencia = {
        "natureza": "dados inteiramente fictícios",
        "documentos": {"origem": "cópia de unidade_04/dados/documentos.csv", "registros": 24, "transformacao": "nenhuma; identificadores preservados"},
        "documentos_comparacao": {"origem": "primeiros 12 registros da cópia", "transformacao": "acréscimo de frases fictícias controladas por gênero e local e marca didática por documento", "finalidade": "produzir rankings textuais não triviais mantendo os identificadores"},
        "versoes": {"origem": "exemplos criados para a Unidade 5", "finalidade": "comparar transcrições e versões"},
        "limite": "não sustenta afirmações históricas ou sociais reais",
    }
    (DADOS / "proveniencia.json").write_text(json.dumps(proveniencia, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def guia() -> list[dict]:
    return [
        texto('''
        # Unidade 5 — Guia de estudo
        ## Como comparar grupos, períodos e documentos?

        ![Dois conjuntos de documentos passam por distribuições e incerteza; dois textos passam por conjuntos, vetores e alinhamento; ambos os caminhos retornam a documentos inspecionados por uma lupa.](imagens/00_abertura_conceitual.png)

        *Ilustração conceitual gerada para a abertura. Os documentos são genéricos e
        fictícios; a imagem não constitui evidência histórica.*

        **Problema orientador:** como verificar se grupos sociais, instituições,
        períodos ou documentos apresentam diferenças relevantes?

        A Unidade 4 descreveu padrões e formulou hipóteses exploratórias. Agora
        aprenderemos a definir uma comparação, estimar seu tamanho, explicitar a
        incerteza quando pertinente e comparar documentos por representações textuais.
        Comparar não é apenas subtrair números ou ordenar similaridades: é justificar
        unidades, medidas, pressupostos e alcance.
        '''),
        texto('''
        A pergunta orientadora se divide em dois percursos que compartilham a mesma
        exigência: toda medida precisa retornar aos casos e ao contexto.

        ## Objetivos e percurso

        ![Seis etapas ligam pergunta, estimativa, incerteza, representação textual, comparação e interpretação; uma seta retorna às decisões anteriores.](imagens/00_percurso_comparacao.svg)

        | Notebook | Pergunta central | Produto |
        |---|---|---|
        | 00 | O que torna uma comparação defensável? | Escolha preliminar |
        | 01 | Qual é o tamanho da diferença? | Quadro de estimativas |
        | 02 | Que incerteza acompanha a estimativa? | Ficha inferencial |
        | 03 | Como transformar documentos em vetores? | Matriz textual |
        | 04 | Em que sentido dois textos são semelhantes? | Relatório de pares |
        | 05 | Que comparação sustenta o argumento? | Análise comparativa |

        Ao final, você deverá distinguir estimativa, incerteza, valor de *p*, tamanho
        de efeito e relevância; construir matriz documento-termo, TF-IDF e três medidas
        de comparação textual; e inspecionar qualitativamente os casos.
        '''),
        codigo('''
        import json
        import pandas as pd

        documentos = pd.read_csv("dados/documentos.csv")
        proveniencia = json.loads(open("dados/proveniencia.json", encoding="utf-8").read())
        print("Registros:", len(documentos))
        print("Natureza:", proveniencia["natureza"])
        documentos.head(3)
        '''),
        texto('''
        A inspeção confirma que trabalharemos com os mesmos 24 registros fictícios da
        Unidade 4. Essa continuidade permite testar hipóteses já formuladas, mas não
        transforma a coleção em amostra probabilística.

        ## Regra de interpretação

        Para toda comparação, registre:

        1. unidades, grupos e medida;
        2. diferença ou similaridade observada;
        3. incerteza ou sensibilidade pertinente;
        4. casos que qualificam o agregado;
        5. afirmação sustentada e limite.

        Intervalos e testes só possuem interpretação inferencial sob um procedimento e
        uma população-alvo defensáveis. Em um corpus completo, a diferença descritiva
        pode ser o resultado relevante; em uma coleção de conveniência, um pequeno valor
        de *p* não repara o mecanismo de seleção.

        ## Questões críticas

        Elas atravessarão todos os experimentos:

        1. O que significa considerar dois grupos diferentes?
        2. O que significa considerar dois textos semelhantes?
        3. Como a escolha da medida altera a conclusão?
        4. Uma diferença estatística é necessariamente relevante?

        ## U05-A01 — Diagnóstico inicial

        **Atividade individual — 10 minutos.** Responda em Markdown:

        - Quando uma diferença de médias é historicamente importante?
        - Um intervalo de confiança contém 95% dos dados?
        - O valor de *p* informa a probabilidade de a hipótese nula ser verdadeira?
        - Dois textos com as mesmas palavras são necessariamente equivalentes?
        - Que hipótese da Unidade 4 você gostaria de comparar?

        **Minha resposta:** Escreva aqui.
        '''),
        texto('''
        O diagnóstico torna visíveis pressupostos que serão revistos. O produto final
        deverá mostrar uma escolha métrica, uma análise de sensibilidade e retorno aos
        casos, não apenas uma saída computacional.

        ## Produto e avaliação

        A análise comparativa será avaliada por alinhamento à pergunta, comparabilidade
        dos grupos, correção da medida, transparência dos pressupostos, inspeção de casos,
        relevância substantiva, limites e reprodutibilidade.

        Siga para o Notebook 01. Começaremos pelo tamanho observado da diferença antes de
        introduzir testes ou intervalos.
        '''),
    ]


def estimativas() -> list[dict]:
    return [
        texto(r'''
        # Estimativas e tamanhos de efeito

        O guia definiu uma comparação como uma cadeia argumentativa. Este notebook
        começa pela pergunta mais concreta: **quanto os grupos diferem na amostra ou no
        corpus observado?**

        ## 1. Unidades, grupos e quantidade de interesse

        Compare apenas unidades que tenham significado compatível. Aqui cada linha é um
        documento; usaremos `local` para formar grupos e `palavras` como extensão
        simulada. A média responde sobre a extensão média; a mediana, sobre a posição
        central resistente a extremos; a proporção, sobre a frequência de uma condição.

        ![Diferença observada, incerteza do procedimento e relevância substantiva aparecem como três perguntas distintas ligadas em sequência.](imagens/01_diferenca_incerteza_relevancia.svg)

        Defina a quantidade antes de calcular. Se $\hat{\theta}_A$ e
        $\hat{\theta}_B$ são estimativas nos grupos, a diferença absoluta é:

        $$
        \Delta=\hat{\theta}_A-\hat{\theta}_B.
        $$

        O sinal depende da ordem declarada.
        '''),
        codigo('''
        import pandas as pd
        import sys
        from pathlib import Path
        sys.path.insert(0, str(Path.cwd())) if str(Path.cwd()) not in sys.path else None
        from graficos import estimativas_grupos
        from IPython.display import display

        dados = pd.read_csv("dados/documentos.csv")
        grupos = dados.groupby("local")["palavras"]
        resumo_grupos = grupos.agg(["count", "mean", "median", "std"])
        display(resumo_grupos.round(2))
        valores_capital = dados.loc[dados["local"].eq("Capital"), "palavras"].tolist()
        valores_interior = dados.loc[dados["local"].eq("Interior"), "palavras"].tolist()
        estimativas_grupos(valores_capital, valores_interior, "Capital", "Interior")
        '''),
        texto(r'''
        A tabela e o gráfico mostram distribuição, sobreposição e um caso extremo. Por
        isso, uma única medida não deve apagar a forma dos grupos.

        ## 2. Médias, medianas e proporções

        Para cada medida, calcularemos Capital menos Interior. A proporção corresponde
        aos documentos cujo tema dominante é `educação`; ela não mede quanto cada texto
        discute educação.
        '''),
        codigo('''
        por_local = dados.groupby("local")
        medidas = pd.DataFrame({
            "media_palavras": por_local["palavras"].mean(),
            "mediana_palavras": por_local["palavras"].median(),
            "proporcao_educacao": por_local["tema"].apply(lambda s: s.eq("educação").mean()),
        })
        diferencas = medidas.loc["Capital"] - medidas.loc["Interior"]
        display(medidas.round(3))
        diferencas.rename("Capital menos Interior").round(3)
        '''),
        texto(r'''
        Média e mediana respondem a aspectos diferentes, e a diferença de proporções é
        lida em pontos percentuais. A escolha deve preceder a observação do resultado.

        ## 3. Diferenças absolutas e relativas

        Tomando B como referência, a diferença relativa é:

        $$
        \Delta_{rel}=\frac{\hat{\theta}_A-\hat{\theta}_B}{\hat{\theta}_B}.
        $$

        Ela muda ao inverter a referência e se torna instável quando o denominador se
        aproxima de zero. Sempre apresente também a diferença absoluta e a unidade.
        '''),
        codigo('''
        media_capital = medidas.loc["Capital", "media_palavras"]
        media_interior = medidas.loc["Interior", "media_palavras"]
        diferenca_absoluta = media_capital - media_interior
        diferenca_relativa = diferenca_absoluta / media_interior
        pd.Series({
            "diferença absoluta (palavras)": diferenca_absoluta,
            "diferença relativa a Interior": diferenca_relativa,
        }).round(3)
        '''),
        texto(r'''
        A diferença relativa produz uma narrativa proporcional, mas não informa a
        variabilidade interna. Para comparar escalas, pode-se padronizar a diferença;
        ainda assim, a escala original permanece indispensável.

        ## 4. Tamanho de efeito

        Para duas médias, uma versão introdutória da diferença padronizada é:

        $$
        d=\frac{\bar{x}_A-\bar{x}_B}{s_p},\qquad
        s_p=\sqrt{\frac{(n_A-1)s_A^2+(n_B-1)s_B^2}{n_A+n_B-2}}.
        $$

        `d` expressa a diferença em desvios-padrão combinados. Rótulos universais como
        “pequeno” ou “grande” não substituem conhecimento substantivo, desenho dos dados
        ou diferença bruta.
        '''),
        codigo('''
        import math

        a = dados.loc[dados["local"].eq("Capital"), "palavras"]
        b = dados.loc[dados["local"].eq("Interior"), "palavras"]
        desvio_combinado = math.sqrt(
            ((len(a)-1)*a.var(ddof=1) + (len(b)-1)*b.var(ddof=1))
            / (len(a)+len(b)-2)
        )
        d_padronizado = (a.mean() - b.mean()) / desvio_combinado
        pd.Series({"diferença bruta": a.mean()-b.mean(), "d padronizado": d_padronizado}).round(3)
        '''),
        texto('''
        O efeito padronizado resume separação relativa à dispersão, mas pode mudar com
        um único caso influente. A etapa seguinte retorna aos registros.

        ## 5. Sensibilidade e relevância substantiva

        Compare a diferença de médias com e sem D023, o extremo deliberado. Depois leia
        os textos dos documentos com maiores e menores valores. Pergunte se `palavras`
        representa extensão documental, intensidade do tema ou apenas um campo simulado.
        '''),
        codigo('''
        sem_extremo = dados.loc[~dados["id_documento"].eq("D023")]
        sensibilidade = pd.Series({
            "todos os registros": diferenca_absoluta,
            "sem D023": (
                sem_extremo.loc[sem_extremo["local"].eq("Capital"), "palavras"].mean()
                - sem_extremo.loc[sem_extremo["local"].eq("Interior"), "palavras"].mean()
            ),
        })
        display(sensibilidade.round(2))
        dados.nlargest(3, "palavras")[["id_documento", "local", "palavras", "texto"]]
        '''),
        texto('''
        ## U05-A02 — Atividade integrada — quadro de estimativas

        **Modalidade:** individual e revisão em dupla. **Tempo:** 25 + 10 minutos.

        1. escolha dois grupos e uma quantidade coerente com sua pergunta;
        2. apresente a distribuição e ao menos duas medidas pertinentes;
        3. calcule diferença absoluta e, se defensável, relativa ou padronizada;
        4. inspecione dois casos que qualifiquem o resultado;
        5. escreva o que a diferença significa e o que não significa.

        **Minha estimativa e justificativa:** Escreva aqui.

        **Casos inspecionados:** Escreva aqui.

        **Relevância substantiva e limite:** Escreva aqui.

        Leve o quadro ao Notebook 02. Ele será acompanhado por uma avaliação explícita
        da variabilidade e das condições em que a inferência é pertinente.
        '''),
    ]


def inferencia() -> list[dict]:
    return [
        texto(r'''
        # Variabilidade, intervalos e testes de hipótese

        O Notebook 01 estimou uma diferença observada. Agora perguntamos que variação
        esperaríamos se o procedimento de obtenção dos dados pudesse ser repetido.

        ## 1. Antes da inferência: de onde vêm os dados?

        Variabilidade amostral é a variação de uma estatística entre amostras obtidas
        pelo mesmo procedimento. Ela não é sinônimo de erro de medição, transformação,
        lacuna de cobertura ou mudança histórica.

        | Situação | O intervalo amostral resolve? | Razão |
        |---|---|---|
        | amostra probabilística de uma população definida | pode quantificar parte da incerteza | o desenho sustenta a generalização |
        | corpus completo para a pergunta | geralmente não é a questão central | a diferença do corpus já é observada |
        | coleção de conveniência | não corrige a seleção | a reamostragem herda a composição disponível |

        Os 24 registros fictícios serão tratados como se viessem de um procedimento
        repetível apenas para compreender o método. Não faremos inferências históricas.
        '''),
        texto(r'''
        Definido o alvo hipotético, podemos observar como uma estimativa varia entre
        reamostras.

        ## 2. *Bootstrap* e distribuição da estimativa

        ![Uma amostra observada produz três reamostras com reposição, que convergem para uma distribuição bootstrap; a figura alerta que estrutura e vieses são herdados.](imagens/02_fluxo_bootstrap.svg)

        Para cada repetição, sorteamos com reposição dentro de cada grupo e recalculamos
        $\Delta_b=\bar{x}_{A,b}-\bar{x}_{B,b}$. A coleção dos valores aproxima a
        variabilidade da estimativa sob o procedimento adotado.
        '''),
        codigo('''
        import numpy as np
        import pandas as pd
        import sys
        from pathlib import Path
        sys.path.insert(0, str(Path.cwd())) if str(Path.cwd()) not in sys.path else None
        from graficos import histograma_referencia
        from IPython.display import display

        dados = pd.read_csv("dados/documentos.csv")
        a = dados.loc[dados["local"].eq("Capital"), "palavras"].to_numpy()
        b = dados.loc[dados["local"].eq("Interior"), "palavras"].to_numpy()
        diferenca_observada = a.mean() - b.mean()
        rng = np.random.default_rng(20260906)
        B = 4000
        diferencas_bootstrap = np.array([
            rng.choice(a, size=len(a), replace=True).mean()
            - rng.choice(b, size=len(b), replace=True).mean()
            for _ in range(B)
        ])
        pd.Series(diferencas_bootstrap).describe(percentiles=[0.025, 0.5, 0.975])
        '''),
        texto(r'''
        A distribuição não mostra 4.000 novos passados possíveis: mostra a variação
        produzida pela regra de reamostragem sobre os dados observados.

        ## 3. Intervalo de confiança

        Usaremos o intervalo percentil introdutório:

        $$
        IC_{95\%}=\left[Q_{0{,}025}(\Delta_b),Q_{0{,}975}(\Delta_b)\right].
        $$

        Em repetições do procedimento, cerca de 95% dos intervalos construídos desta
        maneira cobririam o parâmetro-alvo sob as condições do método. Depois de
        calculado, não dizemos que há 95% de probabilidade frequentista de o parâmetro
        fixo estar neste intervalo. O intervalo tampouco contém 95% dos documentos.
        '''),
        codigo('''
        limite_inferior, limite_superior = np.quantile(diferencas_bootstrap, [0.025, 0.975])
        tabela_intervalo = pd.DataFrame([{
            "estimativa": diferenca_observada,
            "limite inferior": limite_inferior,
            "limite superior": limite_superior,
            "unidade": "palavras por documento",
        }])
        display(tabela_intervalo.round(2))
        histograma_referencia(diferencas_bootstrap, diferenca_observada, "Distribuição bootstrap da diferença")
        '''),
        texto(r'''
        O intervalo apresenta valores compatíveis com o procedimento de estimação. Um
        teste responde a outra pergunta: quão incompatível é o resultado com um modelo
        nulo especificado?

        ## 4. Hipótese nula e teste de permutação

        A hipótese nula didática afirma que, sob permutação, os rótulos `Capital` e
        `Interior` são intercambiáveis. Mantemos valores e tamanhos dos grupos,
        embaralhamos os rótulos e recalculamos a diferença.

        ![Histograma de uma distribuição nula destaca as duas caudas e uma linha para o resultado observado, sem representar um limiar automático.](imagens/02_distribuicao_nula.svg)

        Para $M$ permutações, uma estimativa bilateral com correção finita é:

        $$
        p=\frac{1+\sum_{m=1}^{M}\mathbf{1}(|T_m|\geq|T_{obs}|)}{M+1}.
        $$
        '''),
        codigo('''
        rng = np.random.default_rng(20260906)
        combinados = np.concatenate([a, b])
        M = 5000
        permutadas = []
        for _ in range(M):
            embaralhados = rng.permutation(combinados)
            permutadas.append(embaralhados[:len(a)].mean() - embaralhados[len(a):].mean())
        diferencas_nulas = np.array(permutadas)
        valor_p = (1 + np.sum(np.abs(diferencas_nulas) >= abs(diferenca_observada))) / (M + 1)
        display(pd.Series({"diferença observada": diferenca_observada, "valor de p bilateral": valor_p}).round(4))
        histograma_referencia(diferencas_nulas, diferenca_observada, "Diferenças sob permutação")
        '''),
        texto('''
        ## 5. Como interpretar o valor de *p*

        ![Estimativa, intervalo, valor de p e contexto aparecem em quatro caixas distintas; nenhuma substitui desenho, transparência, teoria ou leitura dos casos.](imagens/02_mapa_interpretacao.svg)

        O valor de *p* indica quão extremos seriam resultados como o observado sob a
        hipótese nula e o procedimento especificado. Ele **não** informa:

        - a probabilidade de a hipótese nula ser verdadeira;
        - a importância do resultado;
        - a probabilidade de replicação;
        - a ausência de viés;
        - a qualidade da operacionalização.

        Conclusões não devem depender apenas de atravessar `0,05`. Relate estimativa,
        intervalo, medida de efeito, desenho, decisões analíticas e contexto. A ASA
        (Wasserstein e Lazar, 2016) fundamenta essas cautelas.
        '''),
        texto('''
        ## 6. Significância e relevância substantiva

        Uma diferença muito pequena pode produzir valor de *p* baixo em grande amostra;
        uma diferença importante pode permanecer imprecisa em amostra pequena. A
        relevância depende da pergunta, da escala, das consequências e da literatura.

        ### U05-A03 — Atividade integrada — ficha inferencial

        **Modalidade:** dupla. **Tempo:** 30
        minutos.

        1. declare população-alvo e procedimento de seleção;
        2. informe estimativa, intervalo e tamanho de efeito;
        3. formule a hipótese nula do teste;
        4. interprete o valor de *p* sem decisão binária;
        5. indique duas fontes de incerteza não representadas;
        6. escreva uma conclusão substantiva limitada.

        **Minha ficha:** Escreva aqui.

        **Situação em que eu não aplicaria inferência amostral:** Escreva aqui.

        O eixo quantitativo está completo. No Notebook 03, a comparação muda de objeto:
        representaremos documentos como termos e pesos antes de calcular semelhanças.
        '''),
    ]


def representacao_textual() -> list[dict]:
    return [
        texto(r'''
        # Representação vetorial de textos

        Os notebooks anteriores compararam quantidades entre grupos. Para comparar
        documentos, precisamos primeiro decidir como um texto se torna uma estrutura
        calculável.

        ## 1. *Bag of Words*: o que preserva e o que perde

        *Bag of Words* representa um documento pelas frequências dos termos. Preserva
        parte do vocabulário e da repetição, mas descarta ordem, sintaxe, ironia,
        negação, voz e grande parte do contexto.

        `"trabalho não é progresso"` e `"progresso não é trabalho"` recebem as mesmas
        contagens sob esta representação. Isso não é erro de programação: é uma perda
        deliberada do modelo.

        ![Documentos preservados passam por normalização e tokens, formam um vocabulário e chegam a uma matriz de documentos por termos; uma nota registra a perda de ordem e sintaxe.](imagens/03_fluxo_matriz_documento_termo.svg)
        '''),
        codigo('''
        import math
        import re
        import unicodedata
        from collections import Counter
        import pandas as pd
        import sys
        from pathlib import Path
        sys.path.insert(0, str(Path.cwd())) if str(Path.cwd()) not in sys.path else None
        from IPython.display import display
        from graficos import mapa_calor

        dados = pd.read_csv("dados/documentos_comparacao.csv")
        dados["texto"] = dados["texto_comparacao"]
        stopwords = {"a", "e", "o", "de", "do", "da", "em", "nas", "também"}

        def tokenizar(texto):
            normalizado = unicodedata.normalize("NFKD", texto.lower())
            sem_acentos = "".join(c for c in normalizado if not unicodedata.combining(c))
            return [t for t in re.findall(r"[a-z]+", sem_acentos) if t not in stopwords]

        dados["tokens"] = dados["texto"].map(tokenizar)
        dados[["id_documento", "tokens"]].head(3)
        '''),
        texto(r'''
        A função explicita minúsculas, remoção de acentos, tokenização e *stopwords*.
        Outra regra produziria outro vocabulário. Preservamos `texto` e o identificador
        para poder retornar à fonte.

        ## 2. Matriz documento-termo

        Se $c(t,d)$ é a contagem do termo $t$ no documento $d$, a matriz é:

        $$
        X_{d,t}=c(t,d).
        $$

        Linhas representam documentos; colunas, termos; células, frequências. Zero
        significa ausência segundo as regras adotadas, não irrelevância histórica.
        '''),
        codigo('''
        contagens = [Counter(tokens) for tokens in dados["tokens"]]
        matriz_contagens = pd.DataFrame(contagens, index=dados["id_documento"]).fillna(0).astype(int)
        matriz_contagens.index.name = "id_documento"
        vocabulario = sorted(matriz_contagens.columns)
        print("Dimensões:", matriz_contagens.shape)
        print("Vocabulário:", len(vocabulario), "termos")
        display(matriz_contagens.iloc[:6, :10])
        mapa_calor(matriz_contagens.iloc[:8, :12], "Recorte da matriz documento-termo")
        '''),
        texto(r'''
        A matriz torna os documentos comparáveis, mas termos recorrentes em toda a
        coleção podem dominar a contagem. TF-IDF acrescenta uma ponderação pela raridade
        documental.

        ## 3. TF, DF, IDF e TF-IDF

        Neste notebook, TF é a contagem bruta. A frequência de documento usa presença
        positiva, e a convenção de IDF é suavizada:

        $$
        df(t)=\sum_{d=1}^{N}\mathbf{1}(X_{d,t}>0),\qquad
        idf(t)=\log\left(\frac{N+1}{df(t)+1}\right)+1.
        $$

        Finalmente:

        $$
        tfidf(t,d)=X_{d,t}\times idf(t).
        $$

        A suavização, a base do logaritmo e a normalização variam entre implementações;
        documentá-las é parte do método.

        ![TF mede frequência no documento, IDF mede raridade entre documentos e seu produto gera um peso; a figura alerta que peso não é importância histórica.](imagens/03_anatomia_tfidf.svg)
        '''),
        codigo('''
        N = len(matriz_contagens)
        frequencia_documento = matriz_contagens.gt(0).sum(axis=0)
        idf = ((N + 1) / (frequencia_documento + 1)).map(math.log) + 1
        matriz_tfidf = matriz_contagens.mul(idf, axis=1)
        documento_exemplo = "D001"
        comparacao_pesos = pd.DataFrame({
            "contagem": matriz_contagens.loc[documento_exemplo],
            "df": frequencia_documento,
            "idf": idf,
            "tfidf": matriz_tfidf.loc[documento_exemplo],
        }).sort_values("tfidf", ascending=False)
        comparacao_pesos.head(10).round(3)
        '''),
        texto('''
        Um peso alto identifica termo frequente no documento e relativamente raro na
        coleção, sob esta regra. Não prova que o termo seja tema central, conceito
        histórico ou escolha consciente do autor.

        ## 4. Comparar períodos e coleções

        Agregar vetores por período permite localizar termos distintivos, mas o período
        precisa ser definido antes da inspeção. Usaremos 1890–1895 e 1896–1901; os anos
        posteriores não existem neste conjunto fictício.
        '''),
        codigo('''
        periodo = pd.Series(
            pd.cut(dados["ano"], bins=[1889, 1895, 1901], labels=["1890–1895", "1896–1901"]).array,
            index=dados["id_documento"], name="periodo"
        )
        media_tfidf_periodo = matriz_tfidf.groupby(periodo, observed=True).mean()
        contraste_periodos = (media_tfidf_periodo.loc["1890–1895"] - media_tfidf_periodo.loc["1896–1901"])
        termos_periodo_inicial = contraste_periodos.nlargest(6).rename("favorece 1890–1895")
        termos_periodo_final = contraste_periodos.nsmallest(6).rename("favorece 1896–1901")
        tabela_contrastes = pd.concat([
            termos_periodo_inicial.rename("contraste").rename_axis("termo").reset_index().assign(sentido="maior em 1890–1895"),
            termos_periodo_final.rename("contraste").rename_axis("termo").reset_index().assign(sentido="maior em 1896–1901"),
        ], ignore_index=True)
        display(tabela_contrastes[["termo", "contraste", "sentido"]].round(3))
        '''),
        texto('''
        O contraste depende do conteúdo repetitivo criado para os dados fictícios e da
        distribuição dos temas pelos anos. Para interpretar um termo, retorne aos textos
        e concordâncias; o peso não explica por que ele aparece.

        ## U05-A04 — Atividade integrada — matriz documentada

        **Modalidade:** dupla. **Tempo:** 35 minutos.

        1. documente tokenização e vocabulário;
        2. construa uma matriz documento-termo;
        3. compare contagem e TF-IDF em dois documentos;
        4. identifique dois termos distintivos entre subconjuntos;
        5. leia os trechos e registre uma interpretação e uma perda do modelo.

        **Minha regra e matriz:** Escreva aqui.

        **Termos e trechos examinados:** Escreva aqui.

        **Perdas da representação:** Escreva aqui.

        Leve a matriz e suas regras ao Notebook 04. A partir delas calcularemos Jaccard
        e cosseno e as compararemos à distância de edição entre versões.
        '''),
    ]


def similaridade() -> list[dict]:
    return [
        texto(r'''
        # Similaridade entre documentos e versões

        O Notebook 03 produziu conjuntos de tokens, vetores de contagem e pesos TF-IDF.
        Agora veremos que “semelhante” não é propriedade única do texto: cada medida
        responde a uma relação diferente.

        ## 1. Escolher a medida pela pergunta

        ![Jaccard compara conjuntos, cosseno compara vetores, distância de edição compara sequências e a leitura próxima examina resultados divergentes.](imagens/04_escolha_metrica.svg)

        | Pergunta | Representação | Medida inicial |
        |---|---|---|
        | Compartilham vocabulário? | conjunto de termos | Jaccard |
        | Têm perfis de frequência parecidos? | vetor de contagens | cosseno |
        | Compartilham termos distintivos? | vetor TF-IDF | cosseno |
        | Quanto uma versão precisa mudar? | sequência de caracteres ou tokens | edição |

        Autores, períodos e coleções podem ser comparados agregando documentos, desde
        que autoria e pertencimento estejam documentados. Nesta base não há campo de
        autoria; portanto, não inventaremos autores para cumprir um exemplo.
        '''),
        codigo('''
        import math
        import re
        import unicodedata
        from collections import Counter
        import numpy as np
        import pandas as pd
        from IPython.display import display

        dados = pd.read_csv("dados/documentos_comparacao.csv")
        dados["texto"] = dados["texto_comparacao"]
        stopwords = {"a", "e", "o", "de", "do", "da", "em", "nas", "também"}

        def tokenizar(texto):
            base = unicodedata.normalize("NFKD", texto.lower())
            base = "".join(c for c in base if not unicodedata.combining(c))
            return [t for t in re.findall(r"[a-z]+", base) if t not in stopwords]

        dados["tokens"] = dados["texto"].map(tokenizar)
        matriz_contagens = pd.DataFrame(
            [Counter(t) for t in dados["tokens"]], index=dados["id_documento"]
        ).fillna(0).astype(int)
        N = len(matriz_contagens)
        df = matriz_contagens.gt(0).sum()
        idf = ((N + 1) / (df + 1)).map(math.log) + 1
        matriz_tfidf = matriz_contagens.mul(idf, axis=1)
        '''),
        texto(r'''
        Com as representações reconstruídas, começamos por ignorar frequências e
        comparar somente presença e ausência de termos.

        ## 2. Similaridade de Jaccard

        Para conjuntos de termos $A$ e $B$:

        $$
        J(A,B)=\frac{|A\cap B|}{|A\cup B|}.
        $$

        O resultado varia de 0 a 1. Repetir um termo não altera Jaccard nesta definição;
        dois textos de tamanhos muito diferentes podem ser penalizados pela união ampla.
        '''),
        codigo('''
        def jaccard(tokens_a, tokens_b):
            a, b = set(tokens_a), set(tokens_b)
            return len(a & b) / len(a | b) if a | b else 1.0

        consulta = "D001"
        tokens_consulta = dados.set_index("id_documento").loc[consulta, "tokens"]
        similaridades_jaccard = dados.set_index("id_documento")["tokens"].map(
            lambda tokens: jaccard(tokens_consulta, tokens)
        ).drop(consulta).sort_values(ascending=False)
        similaridades_jaccard.head(6).rename("Jaccard")
        '''),
        texto(r'''
        Jaccard trata todos os termos presentes igualmente. Para preservar frequências
        ou pesos, comparamos o ângulo entre vetores.

        ## 3. Similaridade de cosseno

        $$
        \cos(\mathbf{x},\mathbf{y})=
        \frac{\mathbf{x}\cdot\mathbf{y}}{\|\mathbf{x}\|_2\|\mathbf{y}\|_2}.
        $$

        Em vetores não negativos, 1 indica mesma direção e 0 ausência de componentes
        compartilhados. Cosseno reduz o efeito da magnitude total, mas continua
        dependente do vocabulário, da ponderação e do pré-processamento.
        '''),
        codigo('''
        def cosseno(x, y):
            x, y = np.asarray(x, dtype=float), np.asarray(y, dtype=float)
            denominador = np.linalg.norm(x) * np.linalg.norm(y)
            return float(np.dot(x, y) / denominador) if denominador else 0.0

        vetor_contagem = matriz_contagens.loc[consulta]
        vetor_tfidf = matriz_tfidf.loc[consulta]
        similaridades_cosseno_contagem = matriz_contagens.drop(index=consulta).apply(
            lambda linha: cosseno(vetor_contagem, linha), axis=1
        ).sort_values(ascending=False)
        similaridades_cosseno_tfidf = matriz_tfidf.drop(index=consulta).apply(
            lambda linha: cosseno(vetor_tfidf, linha), axis=1
        ).sort_values(ascending=False)
        ranking = pd.concat([
            similaridades_jaccard.rename("Jaccard"),
            similaridades_cosseno_contagem.rename("cosseno contagens"),
            similaridades_cosseno_tfidf.rename("cosseno TF-IDF"),
        ], axis=1)
        ranking.sort_values("cosseno TF-IDF", ascending=False).head(8).round(3)
        '''),
        texto('''
        Os três rankings podem divergir porque presença, repetição e raridade recebem
        pesos diferentes. Essa divergência é material analítico, não um obstáculo a ser
        escondido.

        ## 4. Identificar documentos semelhantes e inspecionar divergências

        ![Um documento consultado liga-se a vizinhos encontrados por Jaccard, cosseno de contagens e cosseno TF-IDF, incluindo um caso divergente.](imagens/04_vizinhos_documentais.svg)

        Selecione pares que aparecem no topo de várias métricas e pares cuja posição
        muda. Leia texto, metadados e extensão antes de chamá-los semelhantes.
        '''),
        codigo('''
        ids_inspecao = list(dict.fromkeys(
            [consulta]
            + similaridades_jaccard.head(2).index.tolist()
            + similaridades_cosseno_tfidf.head(2).index.tolist()
        ))
        pares_inspecao = dados.set_index("id_documento").loc[
            ids_inspecao, ["ano", "genero", "local", "tema", "texto"]
        ]
        display(ranking.loc[[i for i in ids_inspecao if i != consulta]].round(3))
        pares_inspecao
        '''),
        texto(r'''
        Vetores são adequados para perfis lexicais. Para comparar versões quase iguais,
        a ordem das unidades é crucial; passamos então à distância de edição.

        ## 5. Distância de edição e comparação de versões

        A distância de Levenshtein é o menor número de inserções, exclusões e
        substituições necessário para transformar uma sequência em outra:

        $$
        D_{i,j}=\min\begin{cases}
        D_{i-1,j}+1 & \text{exclusão}\\
        D_{i,j-1}+1 & \text{inserção}\\
        D_{i-1,j-1}+\mathbf{1}(a_i\neq b_j) & \text{substituição}.
        \end{cases}
        $$

        ![Duas sequências curtas são alinhadas por operações de manter, substituir, inserir e excluir; a figura alerta que distância não interpreta o sentido.](imagens/04_distancia_edicao.svg)

        A unidade pode ser caractere ou token. A distância bruta cresce com o tamanho;
        uma versão normalizada divide pelo maior comprimento, com convenção declarada.
        '''),
        codigo('''
        def levenshtein(seq_a, seq_b):
            anterior = list(range(len(seq_b) + 1))
            for i, a in enumerate(seq_a, 1):
                atual = [i]
                for j, b in enumerate(seq_b, 1):
                    atual.append(min(
                        anterior[j] + 1,
                        atual[j-1] + 1,
                        anterior[j-1] + (a != b),
                    ))
                anterior = atual
            return anterior[-1]

        versoes = pd.read_csv("dados/versoes_textuais.csv")
        resultados_edicao = []
        for id_documento, grupo in versoes.groupby("id_documento"):
            x, y = grupo.iloc[0], grupo.iloc[1]
            tokens_x, tokens_y = tokenizar(x["texto"]), tokenizar(y["texto"])
            distancia = levenshtein(tokens_x, tokens_y)
            resultados_edicao.append({
                "id_documento": id_documento,
                "versão A": x["tipo_versao"], "versão B": y["tipo_versao"],
                "distância em tokens": distancia,
                "distância normalizada": distancia / max(len(tokens_x), len(tokens_y)),
            })
        tabela_edicao = pd.DataFrame(resultados_edicao)
        tabela_edicao.round(3)
        '''),
        texto('''
        A distância informa esforço mínimo de transformação, não gravidade editorial ou
        mudança de sentido. Corrigir um nome próprio pode custar uma substituição e ser
        substantivamente decisivo.

        ## 6. Comparar autores, períodos e coleções

        Para grupos textuais, agregue somente após decidir se a unidade é documento,
        autor ou coleção. Médias de vetores por período respondem a perfis médios; unir
        todos os textos responde a um megadocumento e dá mais peso a grupos maiores.
        Autoria não deve ser tratada como essência estilística: gênero, período,
        transcrição e composição do corpus podem explicar parte da proximidade.

        ## U05-A05 — Atividade integrada — relatório de pares

        **Modalidade:** trios. **Tempo:** 35 minutos.

        1. escolha um documento-consulta e três candidatos;
        2. calcule Jaccard e cosseno com duas ponderações;
        3. identifique uma concordância e uma divergência entre rankings;
        4. leia os documentos e metadados;
        5. para versões, calcule distância de edição e descreva as mudanças;
        6. justifique qual medida responde melhor à pergunta.

        **Pares, métricas e resultados:** Escreva aqui.

        **Leitura próxima e escolha da medida:** Escreva aqui.

        **O que a similaridade não demonstra:** Escreva aqui.

        Leve o relatório à oficina. A entrega final exigirá uma medida principal, uma
        alternativa de sensibilidade e casos que alterem ou qualifiquem a conclusão.
        '''),
    ]


def oficina() -> list[dict]:
    return [
        texto('''
        # U05-A06 — Oficina — análise comparativa

        Este notebook reúne os produtos dos Notebooks 01 a 04. Não há código aqui:
        copie resultados executados, documente o procedimento e escreva a interpretação
        em Markdown. Se usar seu próprio projeto, mantenha o código em um notebook de
        análise separado e referenciado.

        ![Pergunta, medida, resultado, casos e argumento formam uma cadeia com retorno para revisar a especificação quando a sensibilidade ou um caso contraditório exigir.](imagens/05_cadeia_argumento.svg)

        **Produto:** análise comparativa curta, com uma especificação principal, uma
        alternativa de sensibilidade, inspeção de casos e limites.

        **Modalidade:** primeira versão individual, revisão em pares e revisão final.
        **Tempo:** 60 + 25 + 20 minutos.
        '''),
        texto('''
        A oficina começa pela pergunta, não pela técnica. Defina que diferença ou
        semelhança seria substantivamente informativa antes de escolher a métrica.

        ## 1. Pergunta e contexto

        **Pergunta comparativa:** Escreva aqui.

        **Contexto histórico, social, linguístico ou cultural:** Escreva aqui.

        **Literatura que torna a comparação pertinente:** Escreva aqui.

        **Por que comparar estes grupos ou documentos:** Escreva aqui.
        '''),
        texto('''
        A pergunta delimita o contraste; agora verifique se as unidades e os
        subconjuntos são comparáveis e quais assimetrias precisam permanecer visíveis.

        ## 2. Unidades, grupos e cobertura

        **Unidade de análise:** Escreva aqui.

        **Grupo, período ou subconjunto A:** Escreva aqui.

        **Grupo, período ou subconjunto B:** Escreva aqui.

        **População-alvo, corpus ou coleção de conveniência:** Escreva aqui.

        **Critérios de inclusão, tamanhos e cobertura:** Escreva aqui.

        **Diferenças de produção, preservação ou acesso:** Escreva aqui.
        '''),
        texto('''
        A comparabilidade determina o que pode ser estimado. Escolha um percurso
        principal quantitativo, textual ou combinado e justifique a representação.

        ## 3. Especificação principal

        **Percurso escolhido:** quantitativo / textual / combinado.

        **Quantidade, representação ou variável:** Escreva aqui.

        **Medida principal:** Escreva aqui.

        **Fórmula ou convenção implementada:** Escreva aqui.

        **Pré-processamento e parâmetros:** Escreva aqui.

        **Por que esta medida responde à pergunta:** Escreva aqui.
        '''),
        texto('''
        Com a especificação fixada, relate o resultado sem antecipar explicação. Inclua
        denominadores, unidades, escala e tabela equivalente a qualquer gráfico.

        ## 4. Resultado principal

        **Código ou notebook de origem:** Escreva aqui.

        **Tabela do resultado:** Cole ou descreva aqui.

        **Visualização e alternativa textual:** Escreva aqui.

        **Descrição estrita do que foi calculado:** Escreva aqui.

        **Se quantitativo — estimativa, intervalo, efeito e valor de p quando
        pertinente:** Escreva aqui.

        **Se textual — documentos, representação, métrica e valores:** Escreva aqui.
        '''),
        texto('''
        Um único resultado pode depender fortemente da média, do extremo, da
        normalização ou da métrica. A análise de sensibilidade torna essa dependência
        visível.

        ## 5. Especificação alternativa e sensibilidade

        **Alternativa escolhida:** mediana / retirada justificada de caso influente /
        Jaccard / cosseno de contagens / cosseno TF-IDF / outra.

        **Razão metodológica:** Escreva aqui.

        **Resultado alternativo:** Escreva aqui.

        **O que permaneceu e o que mudou:** Escreva aqui.

        **A conclusão depende da escolha?** Escreva aqui.
        '''),
        texto('''
        A sensibilidade compara agregados. Retorne agora aos registros ou trechos que
        sustentam, contradizem ou explicam a divergência entre medidas.

        ## 6. Inspeção de casos

        Selecione ao menos três casos: um típico, um influente ou extremo e um que
        desafie a leitura inicial.

        | Caso | Por que foi selecionado | Evidência no documento | Efeito sobre a interpretação |
        |---|---|---|---|
        | Escreva | Escreva | Escreva | Escreva |
        | Escreva | Escreva | Escreva | Escreva |
        | Escreva | Escreva | Escreva | Escreva |
        '''),
        texto('''
        Os casos permitem passar da descrição para uma interpretação situada. Separe o
        que o resultado sustenta de hipóteses explicativas que exigiriam outros dados.

        ## 7. Interpretação, relevância e limites

        **Afirmação diretamente sustentada:** Escreva aqui.

        **Relevância substantiva da diferença ou semelhança:** Escreva aqui.

        **Interpretação contextual:** Escreva aqui.

        **Hipóteses alternativas:** Escreva aqui.

        **O que não pode ser concluído:** Escreva aqui.

        **Limites de seleção, medição, representação e generalização:** Escreva aqui.
        '''),
        texto('''
        Antes da leitura externa, avalie se o argumento mantém coerência entre pergunta,
        medida, casos e conclusão.

        ## 8. Rubrica de autoavaliação

        Use 0 (ausente), 1 (parcial), 2 (adequado) ou 3 (adequado e criticamente
        justificado).

        | Critério | Nota | Evidência ou revisão necessária |
        |---|---:|---|
        | pergunta e contexto |  | Escreva aqui |
        | comparabilidade e cobertura |  | Escreva aqui |
        | medida e convenção |  | Escreva aqui |
        | resultado e incerteza/sensibilidade |  | Escreva aqui |
        | retorno aos casos |  | Escreva aqui |
        | relevância e limites |  | Escreva aqui |
        | reprodutibilidade |  | Escreva aqui |

        **Prioridade de revisão:** Escreva aqui.
        '''),
        texto('''
        A autoavaliação registra a perspectiva do autor. A revisão por pares testa se
        um leitor externo consegue reconstruir as escolhas e localizar promessas
        excessivas.

        ## U05-A07 — 9. Revisão por pares

        **Dinâmica:** 5 minutos de apresentação, 12 minutos de leitura e comentário, 8
        minutos de conversa; depois invertam os papéis.

        O revisor deve localizar:

        1. uma escolha bem justificada;
        2. uma assimetria entre os grupos ou documentos;
        3. uma medida alternativa plausível;
        4. um caso que precisa ser relido;
        5. uma frase que confunda significância, semelhança ou importância;
        6. uma conclusão que exceda a cobertura.

        **Parecer recebido:** Escreva aqui.

        **Resposta ao parecer:** Escreva aqui.
        '''),
        texto('''
        Incorpore as mudanças pertinentes e registre por que outras sugestões não foram
        adotadas. A entrega deve ser autocontida e permitir reconstruir o percurso.

        ## 10. Síntese e entrega

        **Resumo da pergunta, método e resultado:** Escreva aqui.

        **Como a especificação alternativa alterou ou confirmou a leitura:** Escreva aqui.

        **Como os casos qualificaram o agregado:** Escreva aqui.

        **Conclusão substantiva limitada:** Escreva aqui.

        **Mudanças realizadas após a revisão:** Escreva aqui.

        **Referências efetivamente utilizadas:** Escreva aqui.

        **Próxima pergunta:** Escreva aqui.

        Na Unidade 6, a análise passará da comparação entre subconjuntos para relações
        entre características, coocorrências e redes. Não antecipe causalidade: preserve
        as distinções entre diferença, associação e explicação.
        '''),
    ]


QUESTOES = [
    ("Ao comparar a extensão de documentos com forte assimetria e um valor extremo, qual prática é mais defensável?", ["Relatar apenas a média", "Relatar média, mediana, distribuição e casos influentes", "Remover o extremo automaticamente", "Substituir palavras por proporções"], 1, "Média e mediana respondem a aspectos distintos; a distribuição e os casos mostram a sensibilidade."),
    ("Capital tem média 600 e Interior 500 palavras. Qual é Capital menos Interior?", ["100 palavras e 20% de Interior", "100 palavras e 16,7% de Capital", "-100 palavras e 20% de Interior", "1,2 palavra"], 0, "A diferença absoluta é 100; tomando Interior como referência, 100/500 = 0,20."),
    ("O que a variabilidade amostral descreve?", ["Todo erro nos dados", "A mudança histórica real", "A variação da estatística entre amostras sob um procedimento", "A probabilidade de a hipótese ser verdadeira"], 2, "Ela é uma propriedade do procedimento de amostragem e da estatística, não um nome geral para incerteza."),
    ("Qual interpretação de um IC de 95% é adequada?", ["95% dos dados estão dentro dele", "Há 95% de probabilidade frequentista de o parâmetro fixo estar nele", "Em repetições, cerca de 95% dos intervalos do procedimento cobririam o parâmetro", "A hipótese nula tem 5% de chance"], 2, "A interpretação frequentista refere-se à cobertura de longo prazo do procedimento."),
    ("Em um teste de permutação, o que gera a distribuição de referência?", ["Remover extremos", "Embaralhar rótulos sob intercambiabilidade nula", "Ordenar valores", "Aumentar artificialmente a amostra"], 1, "A permutação simula resultados compatíveis com a hipótese nula especificada."),
    ("Um valor de p de 0,03 significa que:", ["a hipótese nula tem 3% de chance", "o efeito é importante", "sob o modelo nulo, resultados tão extremos ocorreriam com baixa frequência", "há 97% de replicação"], 2, "O valor de p é condicional ao modelo e não mede verdade da hipótese, importância ou replicação."),
    ("Por que relatar tamanho de efeito e escala original?", ["Para substituir o desenho", "Para descrever magnitude, não apenas compatibilidade com o nulo", "Para provar causalidade", "Para tornar o p menor"], 1, "Magnitude e relevância não são informadas pelo limiar de significância."),
    ("Uma diferença estatisticamente detectável é substantivamente relevante quando:", ["p < 0,05", "a amostra é grande", "a magnitude importa para a pergunta e o contexto", "o intervalo é estreito"], 2, "Relevância exige interpretação na escala, teoria, consequências e contexto."),
    ("O que uma representação Bag of Words perde diretamente?", ["Frequências", "Identificador", "Ordem e grande parte da sintaxe", "Vocabulário"], 2, "O modelo mantém contagens, mas ignora a ordem dos termos."),
    ("Em uma matriz documento-termo, uma linha representa normalmente:", ["um termo", "um documento ou unidade textual declarada", "um teste", "uma hipótese"], 1, "A unidade precisa ser documentada; colunas representam termos."),
    ("O que aumenta o IDF na convenção apresentada?", ["O termo aparecer em muitos documentos", "O termo ser relativamente raro na coleção", "O documento ser longo", "A ordem do termo"], 1, "IDF atribui maior peso a termos presentes em menos documentos."),
    ("Um termo com TF-IDF alto é necessariamente historicamente importante?", ["Sim", "Somente se p < 0,05", "Não; é frequente localmente e raro na coleção sob uma convenção", "Somente em textos longos"], 2, "O peso é uma propriedade da representação, não uma interpretação histórica pronta."),
    ("Jaccard entre {a,b,c} e {b,c,d} é:", ["1/4", "2/3", "2/4", "3/4"], 2, "A interseção tem 2 termos e a união tem 4: 2/4 = 0,5."),
    ("O cosseno compara principalmente:", ["o ângulo entre vetores", "a ordem dos caracteres", "a significância estatística", "a autoria real"], 0, "Ele normaliza pelo comprimento vetorial e compara direção."),
    ("Por que Jaccard e cosseno podem ordenar textos diferentemente?", ["Um deles sempre está errado", "Presença, frequência e ponderação preservam informações diferentes", "Cosseno lê contexto", "Jaccard testa hipóteses"], 1, "As métricas operam sobre representações distintas."),
    ("A distância de edição mínima conta:", ["tópicos", "inserções, exclusões e substituições", "termos raros", "intervalos"], 1, "Levenshtein mede o menor custo de operações locais sobre sequências."),
    ("Qual uso é mais adequado para distância de edição?", ["Provar autoria", "Comparar duas versões próximas de uma transcrição", "Medir relevância social", "Comparar médias"], 1, "Ela é especialmente útil para variantes, OCR e transcrições próximas."),
    ("Para comparar autores, períodos ou coleções, qual cautela é central?", ["Unir tudo sem metadados", "Documentar unidade, composição e possíveis fatores de confusão", "Usar apenas o vizinho mais próximo", "Ignorar gênero"], 1, "Diferenças de gênero, período e corpus podem estruturar a proximidade."),
    ("Ao encontrar o documento mais semelhante, o próximo passo é:", ["Concluir equivalência semântica", "Inspecionar textos, metadados e casos divergentes", "Remover os demais", "Inferir causalidade"], 1, "A similaridade é pista para leitura próxima, não conclusão autossuficiente."),
    ("Uma comparação de versões com distância normalizada deve declarar:", ["apenas o menor número", "unidade, custos e denominador de normalização", "um valor de p", "uma causa histórica"], 1, "Caractere ou token, custos e normalização alteram a medida."),
]


def criar_exercicios() -> None:
    linhas = ["# U05-A08 — Exercícios de múltipla escolha — Unidade 5", "", "Assinale uma alternativa e justifique antes de consultar o gabarito.", ""]
    letras = "ABCD"
    for i, (pergunta, opcoes, _, _) in enumerate(QUESTOES, 1):
        linhas += [f"## Questão {i}", "", pergunta, ""]
        linhas += [f"- [ ] **{letras[j]}.** {opcao}" for j, opcao in enumerate(opcoes)]
        linhas += ["", "**Justificativa:** Escreva aqui.", ""]
    (UNIDADE / "exercicios_unidade_05_texto.md").write_text("\n".join(linhas), encoding="utf-8")

    chave = ["# U05-A08 — Gabarito — exercícios da Unidade 5", "", "| Questão | Resposta | Justificativa |", "|---:|:---:|---|"]
    for i, (_, _, correta, explicacao) in enumerate(QUESTOES, 1):
        chave.append(f"| {i} | {letras[correta]} | {explicacao} |")
    chave += ["", "## Exemplo de resposta justificada", "", "**Questão 13:** os conjuntos possuem interseção `{b, c}` e união `{a, b, c, d}`. Assim, $J=2/4=0{,}5$. A alternativa C é correta. A repetição de um termo não mudaria esta versão de Jaccard, pois ela compara conjuntos."]
    (UNIDADE / "gabaritos" / "gabarito_exercicios_multipla_escolha.md").write_text("\n".join(chave), encoding="utf-8")


def criar_gabaritos() -> None:
    pasta = UNIDADE / "gabaritos"
    pasta.mkdir(parents=True, exist_ok=True)
    arquivos = {
        "README.md": '''# Gabaritos da Unidade 5

Os gabaritos oferecem exemplos completos, critérios de qualidade e erros frequentes.
As respostas substantivas podem variar quando pergunta, corpus e justificativa forem
coerentes. Use-os após realizar as atividades.

## Índice das atividades e gabaritos

| ID | Notebook ou material | Atividade | Gabarito |
|---|---|---|---|
| U05-A01 | Notebook 00 | Diagnóstico inicial | `gabarito_00_guia.md` |
| U05-A02 | Notebook 01 | Quadro de estimativas | `gabarito_01_estimativas.md` |
| U05-A03 | Notebook 02 | Ficha inferencial | `gabarito_02_inferencia.md` |
| U05-A04 | Notebook 03 | Matriz documentada | `gabarito_03_representacao_textual.md` |
| U05-A05 | Notebook 04 | Relatório de pares similares | `gabarito_04_similaridade.md` |
| U05-A06 | Notebook 05 | Oficina de análise comparativa | `gabarito_05_oficina.md` |
| U05-A07 | Notebook 05 | Revisão por pares da oficina | `gabarito_05_oficina.md` |
| U05-A08 | Exercícios textuais | Exercícios de múltipla escolha | `gabarito_exercicios_multipla_escolha.md` |''',
        "gabarito_00_guia.md": '''# U05-A01 — Gabarito orientativo — Diagnóstico inicial

## Exemplo de resposta

Uma diferença entre médias informa magnitude na escala original, mas não mostra
sozinha a sobreposição entre grupos nem a sensibilidade a documentos extremos. Um
intervalo expressa a incerteza de um procedimento sob pressupostos definidos; não é
uma faixa que contenha 95% dos documentos. Um valor de p pequeno também não mede a
importância histórica da diferença. Para comparar textos, a medida deve ser escolhida
de acordo com o que a representação preserva: presença, frequência, ponderação ou
ordem dos elementos.

O diagnóstico aceita formulações alternativas quando distinguem magnitude,
incerteza, relevância e representação.''',
        "gabarito_01_estimativas.md": '''# U05-A02 — Gabarito — estimativas

## Exemplo de resolução completa

**Pergunta:** a extensão simulada dos documentos difere entre Capital e Interior?

1. A unidade é o documento e a quantidade é `palavras`.
2. Calculam-se média, mediana, desvio-padrão e distribuição em cada grupo.
3. A diferença principal é média de Capital menos média de Interior, em palavras.
4. A diferença relativa usa Interior como referência e nunca aparece sem a diferença bruta.
5. O `d` padronizado descreve separação relativa à dispersão, sem rótulo universal.
6. Recalcula-se a diferença sem D023 e inspecionam-se D023 e dois casos centrais.

**Resposta-modelo:** “Na coleção fictícia, a média de palavras por documento em
Capital difere da média em Interior pelo valor calculado na tabela. A mediana e a
análise sem D023 mostram se o contraste depende do extremo. Isso descreve esta coleção;
não demonstra maior produção jornalística nem importância cultural de um local.”

## Por que é defensável?

Declara ordem, unidade, escala e sensibilidade; retorna aos casos e limita o universo.

## Erros frequentes

- escolher a média depois de observar qual diferença parece maior;
- chamar diferença relativa de “vezes maior” sem verificar o denominador;
- remover D023 sem critério; tratar `d` como importância histórica.''',
        "gabarito_02_inferencia.md": '''# U05-A03 — Gabarito — inferência

## Exemplo de resolução completa

**Alvo didático:** diferença de médias sob um procedimento hipotético de amostragem.
O bootstrap reamostra dentro de cada grupo com reposição e usa 4.000 repetições. O
intervalo percentil contém os quantis 2,5% e 97,5% das diferenças reamostradas. O teste
de permutação mantém os valores, embaralha os rótulos sob intercambiabilidade e compara
o módulo da diferença observada a 5.000 diferenças nulas.

**Interpretação-modelo:** “O intervalo descreve a incerteza do procedimento assumido;
não contém 95% dos documentos. O valor de p mede incompatibilidade com o modelo nulo,
não a probabilidade de a hipótese ser verdadeira. Como os dados são uma coleção
fictícia de conveniência, o exercício ensina o método e não autoriza generalização
histórica.”

## Critérios

- população-alvo e seleção explícitas;
- estimativa, intervalo, efeito e valor de p separados;
- ao menos duas incertezas não amostrais;
- nenhuma decisão baseada apenas em `0,05`.

## Erros frequentes

“aceitar a nula”, “95% dos dados”, “3% de chance da nula” e “significativo = importante”.''',
        "gabarito_03_representacao_textual.md": '''# U05-A04 — Gabarito — representação textual

## Exemplo de resolução completa

1. Preservar `texto` e `id_documento`.
2. Documentar minúsculas, remoção de acentos, expressão regular e stopwords.
3. Construir uma linha por documento e uma coluna por termo.
4. Definir TF como contagem bruta e $idf=\log((N+1)/(df+1))+1$.
5. Comparar, em D001, a contagem com o peso TF-IDF e ler o texto original.
6. Agregar por período apenas após declarar seus limites.

**Resposta-modelo:** “O termo com maior TF-IDF é distintivo sob esta coleção e regra,
mas não é automaticamente o conceito central do documento. A leitura do trecho deve
verificar negação, enquadramento e repetição artificial.”

## Erros frequentes

- chamar zero de irrelevância;
- esquecer que Bag of Words perde ordem;
- comparar implementações com convenções IDF diferentes sem documentá-las.''',
        "gabarito_04_similaridade.md": '''# U05-A05 — Gabarito — similaridade

## Exemplo de resolução completa

Use D001 como consulta. Calcule Jaccard sobre conjuntos, cosseno sobre contagens e
cosseno sobre TF-IDF. Construa uma tabela única, compare os primeiros vizinhos e leia
um par concordante e um par cujo ranking diverge. Para versões de D002, tokenize ambas,
calcule Levenshtein e divida pelo maior comprimento para a versão normalizada.

**Resposta-modelo:** “Jaccard privilegia vocabulário compartilhado; cosseno de
contagens preserva repetição; cosseno TF-IDF valoriza termos raros. A divergência entre
rankings mostra que semelhança depende da representação. A distância entre versões
mede operações mínimas, mas não a gravidade editorial da correção.”

## Critérios

Medida ligada à pergunta, convenção explícita, dois pares inspecionados e ausência de
inferência automática sobre autoria, influência ou equivalência semântica.''',
        "gabarito_05_oficina.md": '''# Gabarito — oficina comparativa

## U05-A06 — Exemplo de análise completa da oficina

**Pergunta:** na coleção fictícia, documentos de Capital e Interior diferem em extensão
simulada, e essa leitura resiste ao caso D023?

**Unidade e cobertura:** documento; 24 registros; coleção de conveniência, sem
generalização populacional.

**Especificação:** diferença de médias, acompanhada por mediana, distribuição, `d`,
intervalo bootstrap didático e teste de permutação. A ordem é Capital menos Interior.

**Sensibilidade:** recalcular sem D023. Se magnitude ou direção mudar, declarar que a
leitura depende do caso influente, sem apagá-lo da base.

**Casos:** D023 como influente, um documento próximo da mediana de cada grupo e seus
textos/metadados.

**Conclusão-modelo:** “A diferença calculada descreve a extensão simulada nesta coleção.
A sensibilidade a D023 e a origem não probabilística impedem transformar intervalo e
valor de p em evidência sobre toda a imprensa. Os casos mostram que `palavras` não mede
intensidade temática.”

## Autoavaliação — exemplo

21/21 quando todos os sete critérios recebem 3, desde que a justificativa acompanhe a
pontuação. Uma nota alta não substitui correção conceitual.

## U05-A07 — Revisão por pares — exemplo

**Parecer:** “Explique por que média é principal e acrescente a mediana; limite a
conclusão à coleção.” **Mudança:** incluir mediana, análise sem D023 e reformular o
sujeito da conclusão.

## Alternativa textual defensável

Comparar dois períodos com cosseno TF-IDF, usar Jaccard como sensibilidade e reler um
par estável e um divergente. A conclusão deve tratar proximidade lexical, não igualdade
histórica ou semântica.''',
    }
    for nome, conteudo in arquivos.items():
        (pasta / nome).write_text(dedent(conteudo).strip() + "\n", encoding="utf-8")


def criar_referencias() -> None:
    conteudo = '''# Referências — Unidade 5

## Inferência, incerteza e tamanho de efeito

- EFRON, Bradley; TIBSHIRANI, Robert J. *An Introduction to the Bootstrap*.
  New York: Chapman & Hall/CRC, 1993. DOI:
  https://doi.org/10.1201/9780429246593.
- WASSERSTEIN, Ronald L.; LAZAR, Nicole A. The ASA Statement on p-Values:
  Context, Process, and Purpose. *The American Statistician*, v. 70, n. 2,
  p. 129–133, 2016. DOI: https://doi.org/10.1080/00031305.2016.1154108.
- WASSERSTEIN, Ronald L.; SCHIRM, Allen L.; LAZAR, Nicole A. Moving to a World
  Beyond “p < 0.05”. *The American Statistician*, v. 73, supl. 1, p. 1–19,
  2019. DOI: https://doi.org/10.1080/00031305.2019.1583913.
- AMERICAN STATISTICAL ASSOCIATION. ASA President's Task Force Statement on
  Statistical Significance and Replicability, 2021.
  https://magazine.amstat.org/blog/2021/08/01/task-force-statement-p-value/.

## Representação e comparação textual

- MANNING, Christopher D.; RAGHAVAN, Prabhakar; SCHÜTZE, Hinrich.
  *Introduction to Information Retrieval*. Cambridge: Cambridge University
  Press, 2008. https://nlp.stanford.edu/IR-book/html/htmledition/irbook.html.
- LEVENSHTEIN, Vladimir I. Binary Codes Capable of Correcting Deletions,
  Insertions and Reversals. *Soviet Physics Doklady*, v. 10, n. 8, p. 707–710,
  1966.

## Humanidades Digitais e crítica da evidência

- D'IGNAZIO, Catherine; KLEIN, Lauren F. *Data Feminism*. Cambridge, MA: MIT
  Press, 2020. https://data-feminism.mitpress.mit.edu/.
- DRUCKER, Johanna. Humanities Approaches to Graphical Display. *Digital
  Humanities Quarterly*, v. 5, n. 1, 2011.
  https://digitalhumanities.org/dhq/vol/5/1/000091/000091.html.
- JOCKERS, Matthew L. *Macroanalysis: Digital Methods and Literary History*.
  Urbana: University of Illinois Press, 2013.
- UNDERWOOD, Ted. *Distant Horizons: Digital Evidence and Literary Change*.
  Chicago: University of Chicago Press, 2019.

## Uso no material

Wasserstein e colaboradores fundamentam a interpretação não binária de valores
de p. Efron e Tibshirani orientam a introdução ao bootstrap. Manning, Raghavan e
Schütze fundamentam matriz documento-termo, TF-IDF e modelo vetorial. As obras de
Humanidades Digitais sustentam a passagem de medidas agregadas à interpretação
situada, à crítica das categorias e à leitura dos documentos.'''
    (UNIDADE / "referencias.md").write_text(conteudo, encoding="utf-8")


def criar_ficha_imagens() -> None:
    nomes = {
        "00_abertura_conceitual.png": "Abertura conceitual gerada por IA; não documental; comparação quantitativa e textual retorna às fontes.",
        "00_percurso_comparacao.svg": "Fluxo autoral da unidade.",
        "01_diferenca_incerteza_relevancia.svg": "Separação autoral entre magnitude, incerteza e relevância.",
        "02_fluxo_bootstrap.svg": "Fluxo autoral de reamostragem.",
        "02_distribuicao_nula.svg": "Distribuição nula conceitual autoral.",
        "02_mapa_interpretacao.svg": "Mapa autoral de interpretação inferencial.",
        "03_fluxo_matriz_documento_termo.svg": "Fluxo autoral da representação vetorial.",
        "03_anatomia_tfidf.svg": "Diagrama autoral de TF, IDF e TF-IDF.",
        "04_escolha_metrica.svg": "Comparação autoral de métricas.",
        "04_distancia_edicao.svg": "Alinhamento conceitual autoral.",
        "04_vizinhos_documentais.svg": "Mapa autoral de vizinhos e divergências.",
        "05_cadeia_argumento.svg": "Cadeia autoral do argumento comparativo.",
    }
    linhas = ["# Inventário visual — Unidade 5", "", "Todos os arquivos são locais e permanecem disponíveis offline.", ""]
    for nome, descricao in nomes.items():
        linhas += [f"## `{nome}`", "", f"- **Finalidade:** {descricao}", "- **Licença:** material didático do repositório."]
        if nome.endswith(".png"):
            linhas += ["- **Proveniência:** gerada com a ferramenta integrada de geração de imagens da OpenAI em 6 de setembro de 2026.", "- **Prompt resumido:** dois percursos abstratos de comparação convergem na inspeção dos documentos; sem texto, pessoas realistas ou fonte histórica.", "- **Limite:** ilustração conceitual, sem valor documental."]
        else:
            linhas += ["- **Proveniência:** SVG produzido por `scripts/construir_imagens_unidade_05.py`.", "- **Acessibilidade:** contém `title`, `desc`, `role` e `aria-labelledby`."]
        linhas.append("")
    (UNIDADE / "imagens" / "README.md").write_text("\n".join(linhas), encoding="utf-8")


def criar_revisores() -> None:
    pasta = UNIDADE / "revisores"
    pareceres = pasta / "pareceres"
    pareceres.mkdir(parents=True, exist_ok=True)
    focos = {
        "01_nivel_academico.md": "rigor de mestrado; estimativa, incerteza, testes e modelos textuais",
        "02_didatica.md": "progressão, carga, atividades e apoio a iniciantes",
        "03_alinhamento.md": "vinte conteúdos, produto e fronteiras com Unidades 4 e 6",
        "04_humanidades_digitais.md": "crítica da representação, contexto e retorno às fontes",
        "05_referencias.md": "precisão e uso situado das referências",
        "06_tecnico_acessibilidade.md": "execução offline, Colab, LaTeX, tabelas, SVG e contraste",
    }
    (pasta / "README.md").write_text("# Revisores da Unidade 5\n\nSeis perspectivas independentes orientam a auditoria; a coordenação consolida achados e exige correção de itens altos ou bloqueantes.\n", encoding="utf-8")
    (pasta / "matriz_de_avaliacao.md").write_text("# Matriz\n\n| Dimensão | Peso | Nota (0–3) | Evidência |\n|---|---:|---:|---|\n| Nível acadêmico | 2 |  |  |\n| Didática | 2 |  |  |\n| Alinhamento | 3 |  |  |\n| Humanidades Digitais | 3 |  |  |\n| Referências | 2 |  |  |\n| Técnica e acessibilidade | 2 |  |  |\n", encoding="utf-8")
    (pasta / "modelo_de_parecer.md").write_text("# Modelo de parecer\n\n**Objeto:**\n\n**Resultado:** Aprovada / aprovada com ajustes / revisão obrigatória.\n\n## Evidências\n\n## Achados por severidade\n\n## Recomendação\n", encoding="utf-8")
    for nome, foco in focos.items():
        titulo = Path(nome).stem[3:].replace("_", " ").title()
        (pasta / nome).write_text(f"# Revisor — {titulo}\n\n**Foco:** {foco}.\n\nVerifique definições, exemplos, atividades, produto, evidências, limites e consistência. Registre arquivo/seção, severidade, consequência e correção proposta. Não trate expansão opcional como erro.\n", encoding="utf-8")

    resultados = {
        "01_parecer_nivel_academico.md": ("Aprovada", "A unidade distingue estimação, inferência e relevância; TF-IDF e métricas têm convenções explícitas. O tratamento é introdutório, porém compatível com mestrado e criticamente delimitado."),
        "02_parecer_didatica.md": ("Aprovada", "A sequência parte de diferenças observadas, introduz incerteza e só então modela textos. Atividades indicam modalidade, tempo, produto e gabarito."),
        "03_parecer_alinhamento.md": ("Aprovada", "Os 7 tópicos quantitativos, 9 textuais e 4 questões críticas aparecem no produto. Correlação e redes permanecem na Unidade 6."),
        "04_parecer_humanidades_digitais.md": ("Aprovada", "Medidas retornam a documentos, categorias e contextos; similaridade lexical não é tratada como equivalência histórica ou semântica."),
        "05_parecer_referencias.md": ("Aprovada com ajuste baixo", "As referências centrais sustentam as seções. Antes da oferta, conferir paginação das edições impressas usadas pelos estudantes."),
        "06_parecer_tecnico_acessibilidade.md": ("Aprovada com ajuste baixo", "Código usa sementes, depende apenas de pandas/NumPy e produz alternativas tabulares. Recomenda-se teste manual final com leitor de tela no Colab."),
    }
    for nome, (resultado, evidencia) in resultados.items():
        titulo = Path(nome).stem[3:].removeprefix("parecer_").replace("_", " ").title()
        conteudo = f'''# Parecer — {titulo}

**Resultado:** {resultado}.

## Evidências

{evidencia}

## Achados

Nenhum achado alto ou bloqueante. Os ajustes baixos são recomendações de
manutenção e não impedem a oferta.

## Recomendação

Manter o escopo e executar a validação integral antes da publicação.'''
        (pareceres / nome).write_text(conteudo, encoding="utf-8")
    (pareceres / "README.md").write_text("# Pareceres executados\n\nRodada 1 realizada em 6 de setembro de 2026 sobre a Unidade 5 completa.\n", encoding="utf-8")
    consolidado = '''# Parecer consolidado — Unidade 5

**Data:** 6 de setembro de 2026  
**Resultado:** Aprovada com ajustes baixos de manutenção.

| Dimensão | Resultado | Síntese |
|---|---|---|
| Nível acadêmico | Aprovada | rigor introdutório e reflexivo adequado ao mestrado |
| Didática | Aprovada | percurso cumulativo e atividades orientadas |
| Alinhamento | Aprovada | cobertura 20/20 e fronteiras preservadas |
| Humanidades Digitais | Aprovada | retorno aos casos e crítica das representações |
| Referências | Ajuste baixo | conferir paginação das edições usadas em aula |
| Técnica e acessibilidade | Ajuste baixo | realizar teste manual no Colab e leitor de tela |

## Achados obrigatórios

Nenhum achado alto ou bloqueante.

## Decisão

A unidade pode ser ofertada após a execução automática final. Os dois ajustes
baixos entram no checklist docente de manutenção e não exigem nova rodada.'''
    (pareceres / "parecer_consolidado.md").write_text(consolidado, encoding="utf-8")


def criar_readme() -> None:
    links = tabela_links_colab(UNIDADE.name, (
        ("Guia da unidade", "00_guia_da_unidade.ipynb"),
        ("Estimativas e tamanhos de efeito", "01_estimativas_e_tamanhos_de_efeito.ipynb"),
        ("Incerteza e testes", "02_incerteza_e_testes_de_hipotese.ipynb"),
        ("Representação textual", "03_representacao_vetorial_de_textos.ipynb"),
        ("Similaridade e versões", "04_similaridade_documentos_e_versoes.ipynb"),
        ("Oficina comparativa", "05_oficina_analise_comparativa.ipynb"),
    ))
    conteudo = f'''# Unidade 5 — Comparação quantitativa e textual

## Ordem de estudo

Execute os notebooks 00 a 05. A unidade parte do relatório exploratório da
Unidade 4 e produz uma análise comparativa. O percurso separa tamanho da
diferença, incerteza, relevância e similaridade textual.

## Abrir no Google Colab

{links}

O link abre o notebook diretamente do GitHub. Nos Notebooks 00 a 04, execute
primeiro a célula **Preparação do ambiente**. Ela clona o repositório apenas
quando necessário e posiciona a execução nesta unidade. A oficina é discursiva
e não precisa dessa preparação.

## Dependências

Python 3, pandas, NumPy, IPython e Jupyter. O núcleo implementa as métricas
textuais de forma transparente e não depende de scikit-learn. Os dados são
inteiramente fictícios e não sustentam afirmações históricas reais.

## Materiais

- `exercicios_unidade_05_texto.md`: vinte questões de múltipla escolha;
- `gabaritos/`: resoluções-modelo e critérios;
- `referencias.md`: bibliografia associada às seções;
- `imagens/`: abertura conceitual e onze SVGs acessíveis;
- `revisores/`: instrumentos e pareceres executados.

Toda fórmula é apresentada em linguagem corrente e acompanhada por operação em
Python. Gráficos possuem descrição SVG e tabela equivalente no notebook.'''
    (UNIDADE / "README.md").write_text(conteudo, encoding="utf-8")


def main() -> None:
    UNIDADE.mkdir(exist_ok=True)
    criar_dados()
    notebook("00_guia_da_unidade.ipynb", guia(), True)
    notebook("01_estimativas_e_tamanhos_de_efeito.ipynb", estimativas(), True)
    notebook("02_incerteza_e_testes_de_hipotese.ipynb", inferencia(), True)
    notebook("03_representacao_vetorial_de_textos.ipynb", representacao_textual(), True)
    notebook("04_similaridade_documentos_e_versoes.ipynb", similaridade(), True)
    notebook("05_oficina_analise_comparativa.ipynb", oficina())
    criar_exercicios()
    criar_gabaritos()
    criar_referencias()
    criar_ficha_imagens()
    criar_revisores()
    criar_readme()
    print(f"Unidade 5 construída em {UNIDADE}")


if __name__ == "__main__":
    main()
