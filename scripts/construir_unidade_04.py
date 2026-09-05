"""Constrói a Unidade 4."""
import csv,json
from pathlib import Path
from textwrap import dedent
from apoio_colab import adicionar_link_na_abertura, preparacao_colab, tabela_links_colab
R=Path(__file__).resolve().parents[1]; U=R/"unidade_04"; D=U/"dados"
def m(s):
 texto = dedent(s).strip()
 # $ e $$ têm renderização mais consistente no Jupyter, GitHub e Colab.
 linhas = ["$$" if linha in {r"\[", r"\]"} else linha for linha in texto.splitlines()]
 texto = "\n".join(linhas).replace(r"\(", "$").replace(r"\)", "$")
 return {"cell_type":"markdown","metadata":{},"source":texto.splitlines(keepends=True)}
def c(s): return {"cell_type":"code","execution_count":None,"metadata":{},"outputs":[],"source":dedent(s).strip().splitlines(keepends=True)}
def nb(n,cells,requer_repositorio=False):
 publicadas=[adicionar_link_na_abertura(cells[0],U.name,n)]
 if requer_repositorio: publicadas.append(c(preparacao_colab(U.name)))
 publicadas.extend(cells[1:])
 d={"cells":publicadas,"metadata":{"kernelspec":{"display_name":"Python 3","language":"python","name":"python3"},"language_info":{"name":"python","version":"3"}},"nbformat":4,"nbformat_minor":5}
 (U/n).write_text(json.dumps(d,ensure_ascii=False,indent=1)+"\n",encoding="utf-8")
def dados():
 D.mkdir(parents=True,exist_ok=True); ts=["educação","trabalho","progresso","saúde"]; gs=["editorial","notícia","carta"]
 frases={"educação":"A escola noturna amplia a instrução pública e o ensino social.","trabalho":"O trabalho nas oficinas reúne jornada salário e associação.","progresso":"A estrada e a máquina anunciam progresso e também conflito.","saúde":"A cidade debate higiene água saúde e cuidado coletivo."}
 rows=[]
 for i in range(24):
  t=ts[i%4]; texto=(frases[t]+" "+frases[ts[(i+1)%4]])*(1+i%3); p=2100 if i==22 else 320+(47*i)%760
  rows.append([f"D{i+1:03d}",1890+i%12,gs[i%3],["Capital","Interior"][(i//3)%2],t,p,(3*i)%11,1+i%6,texto])
 with (D/"documentos.csv").open("w",encoding="utf-8",newline="") as f:
  w=csv.writer(f); w.writerow(["id_documento","ano","genero","local","tema","palavras","pessoas","paginas","texto"]); w.writerows(rows)
 (D/"proveniencia.json").write_text(json.dumps({"natureza":"inteiramente fictícios","nota":"D023 é extremo deliberado"},ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
def guia(): return [m('''# Unidade 4 — Guia
## Como conhecer uma base antes de aplicar modelos?

![Registros abstratos conduzem a padrões quantitativos e textuais; linhas de proveniência retornam a documentos examinados por uma lupa e se abrem em interpretações alternativas.](imagens/00_abertura_conceitual.png)

Exploração descreve, diagnostica e formula perguntas; não confirma hipóteses retrospectivas. Arnold e Tilton (2019) relacionam estatística exploratória, visualização e computação às Humanidades Digitais. Drucker (2011) lembra que gráficos incorporam escolhas.'''),m('''## Percurso

![Cinco etapas ligam base documentada, descrição, visualização, leitura próxima e formulação de hipóteses; uma seta retorna às decisões anteriores.](imagens/00_percurso_exploracao.svg)

01 exploração quantitativa; 02 textual; 03 visual; 04 relatório. Os 24 registros são fictícios e D023 é extremo deliberado.'''),c('''import json,pandas as pd
dados=pd.read_csv("dados/documentos.csv"); prov=json.loads(open("dados/proveniencia.json",encoding="utf-8").read()); print(dados.shape,prov["natureza"]); dados.head()'''),m('''## Regra de escrita

![A escrita passa por procedimento, descrição, interpretação, limite e próximo passo.](imagens/00_camadas_escrita.svg)

Separe descrição do cálculo, interpretação situada e hipótese provisória. Testes, confiança e comparação inferencial ficam para a Unidade 5.
### Diagnóstico
Que padrão espera e que saída revelaria erro? Escreva aqui.'''),m('''## Produto
Relatório com tabelas, quatro famílias de gráficos, perfil textual, concordâncias, casos extremos, hipóteses e limites.''')]
def quant():
 return [
  m('''# Exploração quantitativa
## Tipos de variáveis

![Escalas nominal, ordinal, quantitativa e temporal são relacionadas a operações e gráficos; identificadores aparecem separados das medidas.](imagens/01_tipos_variaveis.svg)

Nominais distinguem; ordinais ordenam; quantitativas discretas contam; contínuas medem. Datas e identificadores têm papéis próprios. `dtype` não determina a escala conceitual.'''),
  c('''import pandas as pd
import numpy as np
import sys
from pathlib import Path
from IPython.display import display
sys.path.insert(0, str(Path.cwd())) if str(Path.cwd()) not in sys.path else None
from graficos import distribuicao_anotada

dados = pd.read_csv("dados/documentos.csv")
pd.DataFrame(
    [["genero", "nominal"], ["ano", "temporal"],
     ["palavras", "quantitativa discreta"], ["id_documento", "identificador"]],
    columns=["variavel", "escala"],
)'''),
  m(r'''## Frequências e proporções

Se $x_i$ é a categoria do documento $i$, a frequência absoluta da categoria
$k$ e sua proporção são:

\[
f_k = \sum_{i=1}^{n}\mathbf{1}(x_i=k),
\qquad
p_k = \frac{f_k}{n}.
\]

| Símbolo | Significado | Operação em Python |
|---|---|---|
| $n$ | total de documentos incluídos | `len(dados)` |
| $f_k$ | documentos cuja categoria é $k$ | `value_counts()` |
| $p_k$ | parcela do total na categoria $k$ | `value_counts(normalize=True)` |

A função indicadora \(\mathbf{1}(x_i=k)\) vale 1 quando o documento pertence à
categoria e 0 caso contrário. Declare sempre $n$: documentos não medem
automaticamente intensidade, importância histórica ou quantidade de menções.'''),
  c('''frequencias_tema = dados["tema"].value_counts().rename("frequencia")
proporcoes_tema = dados["tema"].value_counts(normalize=True).rename("proporcao")
pd.concat([frequencias_tema, proporcoes_tema], axis=1)'''),
  m(r'''## Centro, quartis e dispersão

Para uma variável quantitativa com valores $x_1,\ldots,x_n$, a média é:

\[
\bar{x}=\frac{1}{n}\sum_{i=1}^{n}x_i.
\]

Depois de ordenar os valores, $x_{(1)}\leq\cdots\leq x_{(n)}$, a mediana é:

\[
\widetilde{x}=
\begin{cases}
x_{((n+1)/2)}, & n \text{ ímpar},\\[4pt]
\dfrac{x_{(n/2)}+x_{(n/2+1)}}{2}, & n \text{ par}.
\end{cases}
\]

O pandas calcula por padrão a variância amostral e o desvio-padrão amostral:

\[
s^2=\frac{1}{n-1}\sum_{i=1}^{n}(x_i-\bar{x})^2,
\qquad
s=\sqrt{s^2}.
\]

A média usa todos os valores e é sensível a extremos; a mediana depende da
posição ordenada; a moda é o valor de maior frequência. O denominador $n-1$
corresponde a `var(ddof=1)` e `std(ddof=1)`. Se o objetivo fosse descrever uma
população integral com denominador $n$, seria necessário declarar `ddof=0`.'''),
  c('''x = dados["palavras"]
resumo = pd.Series({
    "n": x.count(),
    "media": x.mean(),
    "mediana": x.median(),
    "moda": x.mode().iloc[0],
    "q1": x.quantile(0.25, interpolation="linear"),
    "q3": x.quantile(0.75, interpolation="linear"),
    "variancia_amostral": x.var(ddof=1),
    "desvio_padrao_amostral": x.std(ddof=1),
})

display(distribuicao_anotada(
    x.tolist(), dados["id_documento"].tolist(), x.mean(), x.median()
))
resumo'''),
  m(r'''## Distribuição e valores extremos

O intervalo interquartil cobre a metade central dos valores ordenados:

\[
IQR=Q_3-Q_1.
\]

A regra usada pelo boxplot define dois limites:

\[
L_{\mathrm{inferior}}=Q_1-1{,}5\,IQR,
\qquad
L_{\mathrm{superior}}=Q_3+1{,}5\,IQR.
\]

Um caso fora desses limites é um candidato à inspeção, nunca uma exclusão
automática ou prova de erro. Quartis possuem convenções de cálculo diferentes;
neste notebook registramos explicitamente a interpolação linear usada pelo pandas.'''),
  c('''q1 = x.quantile(0.25, interpolation="linear")
q3 = x.quantile(0.75, interpolation="linear")
iqr = q3 - q1
limite_inferior = q1 - 1.5 * iqr
limite_superior = q3 + 1.5 * iqr

extremos = dados[
    (dados["palavras"] < limite_inferior)
    | (dados["palavras"] > limite_superior)
]
print("Limites:", limite_inferior, "a", limite_superior)
extremos[["id_documento", "palavras", "genero", "tema"]]'''),
  m(r'''## Tabela de contingência

Se $A$ representa o gênero e $B$ o tema, a célula $n_{ij}$ conta os
documentos que pertencem simultaneamente à linha $i$ e à coluna $j$:

\[
n_{ij}=\sum_{r=1}^{n}\mathbf{1}(A_r=i \land B_r=j).
\]

A proporção por linha usa como denominador o total daquela linha:

\[
p_{j\mid i}=\frac{n_{ij}}{\sum_j n_{ij}}.
\]

Assim, contagens e proporções por linha respondem perguntas diferentes.
`normalize="index"` implementa $p_{j\mid i}$. Um padrão descritivo não é teste,
explicação causal ou evidência automática de associação histórica.'''),
  c('''contagens = pd.crosstab(dados["genero"], dados["tema"])
proporcoes_por_genero = pd.crosstab(
    dados["genero"], dados["tema"], normalize="index"
).round(3)
contagens, proporcoes_por_genero'''),
  m('''## Atividade
Classifique variáveis, escolha medidas e denominadores, inspecione extremo e contingência. Separe descrição, interpretação e hipótese. Escreva aqui.'''),
 ]
def texto():
 return [
  m('''# Exploração textual
## Tokenização e normalização

![O texto preservado passa por normalização, tokenização, filtro e contagem; o diagrama indica possíveis perdas em cada transformação.](imagens/02_fluxo_tokenizacao.svg)

Tokenizar segmenta por regra. Minúsculas, pontuação e stopwords podem apagar distinções; preserve o texto e documente decisões. Neste exemplo, os tokens são calculados separadamente por documento para não criar contextos ou n-gramas entre o fim de um texto e o início do seguinte.'''),
  c('''import math
import re
from collections import Counter

import pandas as pd
import sys
from pathlib import Path
from IPython.display import display
sys.path.insert(0, str(Path.cwd())) if str(Path.cwd()) not in sys.path else None
from graficos import ttr_duplo

dados = pd.read_csv("dados/documentos.csv")

def tokenizar(texto):
    return re.findall(r"[a-záàâãéêíóôõúç]+", texto.lower())

dados["tokens"] = dados["texto"].map(tokenizar)
todos_tokens = [token for documento in dados["tokens"] for token in documento]
dados[["id_documento", "tokens"]].head(2)'''),
  m(r'''## Frequências absoluta e relativa

Se $t_i$ é o token na posição $i$, a frequência de uma palavra $w$ é:

\[
f(w)=\sum_{i=1}^{N}\mathbf{1}(t_i=w),
\qquad
p(w)=\frac{f(w)}{N}.
\]

O valor de $p(w)$ só é interpretável quando $N$ está declarado. Neste
experimento mostraremos dois denominadores:

| Medida | Denominador |
|---|---|
| frequência relativa entre todos os tokens | $N$, antes de retirar stopwords |
| frequência relativa entre tokens de conteúdo | $N_c$, depois de retirar stopwords |

Remover stopwords apenas da tabela, mas manter $N$ como denominador, responde a
uma pergunta diferente de recalcular a proporção dentro do vocabulário filtrado.'''),
  c('''stopwords = {"a", "o", "e", "de", "do", "da", "como", "em", "nas", "um", "uma", "também"}
frequencias = Counter(todos_tokens)
tokens_conteudo = [token for token in todos_tokens if token not in stopwords]
frequencias_conteudo = Counter(tokens_conteudo)
total_tokens = len(todos_tokens)
total_tokens_conteudo = len(tokens_conteudo)

tabela_frequencias = pd.DataFrame([
    {
        "palavra": palavra,
        "frequencia": frequencia,
        "relativa_todos_tokens": frequencia / total_tokens,
        "relativa_tokens_conteudo": frequencia / total_tokens_conteudo,
    }
    for palavra, frequencia in frequencias_conteudo.most_common(12)
])
tabela_frequencias'''),
  m(r'''## Concordâncias

Uma concordância recupera uma janela de $j$ tokens à esquerda e à direita de
cada ocorrência. Não é necessário transformar essa operação em uma medida única:
seu papel é devolver contexto ao agregado. As janelas devem respeitar as fronteiras
dos documentos e conservar o identificador da fonte.'''),
  c('''def concordancias(tabela, alvo, janela=4):
    resultados = []
    for _, documento in tabela.iterrows():
        tokens = documento["tokens"]
        for posicao, token in enumerate(tokens):
            if token == alvo:
                inicio = max(0, posicao - janela)
                fim = min(len(tokens), posicao + janela + 1)
                resultados.append({
                    "id_documento": documento["id_documento"],
                    "contexto": " ".join(tokens[inicio:fim]),
                })
    return pd.DataFrame(resultados)

concordancias(dados, "trabalho", janela=4).head(8)'''),
  m(r'''## N-gramas e colocações

![A frequência do bigrama é comparada às frequências marginais; o resultado deve ser examinado com frequência mínima e concordâncias.](imagens/02_anatomia_pmi.svg)

Um bigrama é o par adjacente $(t_i,t_{i+1})$ dentro de um mesmo documento.
Para comparar a frequência conjunta com as frequências marginais das posições
esquerda e direita, usaremos informação mútua pontual:

\[
PMI(a,b)=\log_2\left(\frac{P(a,b)}{P_L(a)P_R(b)}\right)
=\log_2\left(\frac{c(a,b)\,N_b}{c_L(a)c_R(b)}\right).
\]

| Símbolo | Significado |
|---|---|
| $c(a,b)$ | frequência do bigrama $(a,b)$ |
| $N_b$ | total de bigramas dentro dos documentos |
| $c_L(a)$ | ocorrências de $a$ na posição esquerda dos bigramas |
| $c_R(b)$ | ocorrências de $b$ na posição direita dos bigramas |

PMI alto indica associação acima do esperado pelas marginais; não indica
causalidade, importância histórica ou estabilidade. Como a medida favorece eventos
raros, exigiremos frequência mínima e retornaremos às concordâncias.'''),
  c('''bigramas = Counter()
marginal_esquerda = Counter()
marginal_direita = Counter()

for tokens_documento in dados["tokens"]:
    pares_documento = list(zip(tokens_documento, tokens_documento[1:]))
    bigramas.update(pares_documento)
    marginal_esquerda.update(a for a, _ in pares_documento)
    marginal_direita.update(b for _, b in pares_documento)

total_bigramas = sum(bigramas.values())
frequencia_minima = 3
linhas_pmi = []
for (a, b), frequencia in bigramas.items():
    if frequencia >= frequencia_minima:
        pmi = math.log2(
            frequencia * total_bigramas
            / (marginal_esquerda[a] * marginal_direita[b])
        )
        linhas_pmi.append((f"{a} {b}", frequencia, pmi))

tabela_colocacoes = pd.DataFrame(
    sorted(linhas_pmi, key=lambda linha: linha[2], reverse=True),
    columns=["bigrama", "frequencia", "pmi"],
)
tabela_colocacoes.head(10)'''),
  m(r'''## Vocabulário e diversidade lexical

Se $V_d$ é o número de formas distintas e $N_d$ o número de tokens do
documento $d$, a razão forma–token é:

\[
TTR(d)=\frac{V_d}{N_d}.
\]

Como a TTR tende a cair quando o texto cresce, podemos comparar segmentos de
tamanho fixo $m$:

\[
TTR_m(d)=\frac{\left|\{t_1,\ldots,t_m\}\right|}{m},
\qquad N_d\geq m.
\]

Para que todos os 24 documentos participem, adotaremos como $m$ o tamanho do
menor texto da base. Usar os primeiros $m$ tokens controla o tamanho, mas ainda é
sensível à posição do trecho; projetos reais devem comparar segmentos ou amostras
com um protocolo explícito.'''),
  c('''tamanho_padrao = int(dados["tokens"].map(len).min())

def ttr_padronizada(tokens, tamanho):
    if len(tokens) < tamanho:
        return pd.NA
    segmento = tokens[:tamanho]
    return len(set(segmento)) / tamanho

diversidade = pd.DataFrame({
    "id_documento": dados["id_documento"],
    "tokens": dados["tokens"].map(len),
    "formas": dados["tokens"].map(lambda tokens: len(set(tokens))),
    "ttr": dados["tokens"].map(lambda tokens: len(set(tokens)) / len(tokens)),
    f"ttr_{tamanho_padrao}": dados["tokens"].map(
        lambda tokens: ttr_padronizada(tokens, tamanho_padrao)
    ),
})
print("Tamanho comum adotado:", tamanho_padrao, "tokens")

display(ttr_duplo(
    diversidade["tokens"].tolist(),
    diversidade["ttr"].tolist(),
    diversidade[f"ttr_{tamanho_padrao}"].tolist(),
    tamanho_padrao,
))
diversidade.head()'''),
  m('''## Atividade
Documente regras, frequências, concordâncias, n-gramas, colocação e diversidade. Retorne a trechos. Escreva aqui.'''),
 ]
def visual():
 return [
  m('''# Visualização exploratória

![Cinco tipos de pergunta são ligados a barras, histograma e boxplot, dispersão, pontos e linha, ou barras de termos.](imagens/03_escolha_grafico.svg)

Gráficos são argumentos. Comece pela pergunta e pela escala conceitual da
variável. Toda figura terá título, eixos, unidades, descrição e tabela
equivalente. Os gráficos abaixo são calculados com Python a partir da base
fictícia; não constituem evidência histórica.'''),
  c('''import re
from collections import Counter

import pandas as pd
import sys
from pathlib import Path
from IPython.display import display
sys.path.insert(0, str(Path.cwd())) if str(Path.cwd()) not in sys.path else None
from graficos import barras_categorias, barras_horizontais, dispersao, histograma_boxplot, serie_temporal

dados = pd.read_csv("dados/documentos.csv")
'''),
  m('''## Barras — categorias

As barras respondem a uma comparação entre categorias. Neste conjunto didático,
cada tema possui seis documentos: a igualdade foi construída deliberadamente e
não representa equilíbrio histórico. A tabela devolvida pelo código torna os
valores e o denominador auditáveis.'''),
  c('''tabela_temas = dados["tema"].value_counts().sort_index().rename("documentos").to_frame()
display(barras_categorias(
    tabela_temas.index.tolist(), tabela_temas["documentos"].tolist(),
    "Documentos por tema (n = 24)", "Tema atribuído", "Número de documentos",
    "Quatro barras de mesma altura mostram seis documentos em cada tema.",
))
tabela_temas'''),
  m(r'''## Histograma e boxplot — distribuições

Se os limites dos intervalos são $b_0,b_1,\ldots,b_J$, a altura da barra $j$
é a quantidade de valores dentro daquele intervalo:

\[
h_j=\sum_{i=1}^{n}\mathbf{1}(b_{j-1}<x_i\leq b_j).
\]

Alterar os limites $b_j$ pode mudar a forma visível da distribuição, mesmo sem
alterar os documentos. O boxplot aplica a regra de 1,5 IQR: os whiskers terminam
nos valores não extremos e D023 aparece como ponto separado. A tabela informa os
intervalos e o resumo numérico equivalentes.'''),
  c('''faixas = [0, 400, 600, 800, 1000, 2200]
tabela_intervalos = dados.groupby(pd.cut(dados["palavras"], faixas), observed=False).size().rename("documentos")
display(histograma_boxplot(
    dados["palavras"].tolist(), faixas, dados["id_documento"].tolist()
))
tabela_intervalos, dados["palavras"].describe()'''),
  m('''## Dispersão — relação entre quantitativas

Cada ponto representa um documento. Forma e cor distinguem os gêneros, enquanto
a tabela mantém os pares e IDs disponíveis. D023 deve ser inspecionado; o padrão
visual entre páginas e palavras não demonstra causalidade.'''),
  c('''display(dispersao(
    dados["paginas"].tolist(), dados["palavras"].tolist(),
    dados["genero"].tolist(), dados["id_documento"].tolist(),
    "Páginas e extensão dos documentos", "Páginas", "Palavras",
))
dados[["id_documento", "genero", "paginas", "palavras"]]'''),
  m(r'''## Série temporal

Se $n_t$ documentos pertencem ao ano $t$, a média anual representada pela
linha é:

\[
\bar{x}_t=\frac{1}{n_t}\sum_{i:\,\mathrm{ano}_i=t}x_i.
\]

A fórmula torna visível o denominador anual. Mostraremos os documentos individuais
junto da média, pois cada ano contém apenas dois casos. D023 eleva a média de 1900;
a linha reflete a composição do corpus e não demonstra mudança histórica contínua.'''),
  c('''resumo_anual = dados.groupby("ano")["palavras"].agg(n="size", media="mean")
display(serie_temporal(
    dados["ano"].tolist(), dados["palavras"].tolist(), dados["id_documento"].tolist(),
    resumo_anual["media"].to_dict(), resumo_anual["n"].to_dict(),
))
resumo_anual'''),
  m('''## Frequências textuais

Barras preservam valores melhor que nuvem de palavras. A tabela informa as
frequências e o denominador deve ser lido junto das regras de tokenização e da
lista de stopwords.'''),
  c('''tokens = re.findall(r"[a-záàâãéêíóôõúç]+", " ".join(dados["texto"]).lower())
stopwords = {"a", "o", "e", "de", "do", "da", "como", "em", "nas", "um", "uma", "também"}
tokens_conteudo = [token for token in tokens if token not in stopwords]
top = Counter(tokens_conteudo).most_common(10)
tabela_termos = pd.DataFrame(top, columns=["termo", "frequencia"])
ordenada = tabela_termos.sort_values("frequencia")
display(barras_horizontais(
    ordenada["termo"].tolist(), ordenada["frequencia"].tolist(),
    f"Termos frequentes após stopwords (Nc = {len(tokens_conteudo)})",
    "Dez barras horizontais ordenadas mostram frequências absolutas dos tokens de conteúdo.",
))
tabela_termos'''),
  m('''## Atividade

Produza barras, histograma/boxplot, dispersão ou tempo e frequência textual. Para
cada figura, entregue tabela, descrição alternativa, escala, padrão, caso, limite
e hipótese. Explique também por que o gráfico escolhido responde à pergunta.

**Minha análise:** Escreva aqui.'''),
 ]
def oficina():
 return [
  m('''# Oficina — Relatório exploratório

## O que será produzido

Nesta atividade integrada, você reunirá os resultados dos Notebooks 01, 02 e 03
em um **relatório exploratório curto e auditável**. O relatório deve apresentar o
que existe na base, destacar padrões e casos que merecem leitura próxima e formular
hipóteses provisórias. Ele não deve apresentar testes estatísticos nem tratar padrões
descritivos como conclusões históricas.

Este notebook é deliberadamente discursivo: execute ou adapte os cálculos em seu
notebook técnico e registre aqui as escolhas, resultados e interpretações em células
Markdown. Você pode trabalhar com os 24 registros fictícios da unidade ou com uma
base própria já preparada segundo as Unidades 2 e 3.

**Entrega esperada:** um relatório com escopo, perfil quantitativo, perfil textual,
quatro visualizações acompanhadas de tabelas, retorno a três casos, até três
hipóteses, limitações e instruções de reprodução.'''),
  m('''## Como realizar a oficina

![Pergunta, tabela, figura, leitura e limite formam uma cadeia; divergências exigem revisão.](imagens/04_cadeia_argumento.svg)

Siga esta ordem:

1. declare a pergunta, o corpus e a unidade de análise;
2. selecione somente medidas pertinentes às variáveis e à pergunta;
3. produza tabelas antes de interpretar gráficos;
4. descreva o padrão observado sem explicar sua causa;
5. retorne a documentos ou trechos que possam qualificar o agregado;
6. formule hipóteses alternativas e indique dados necessários para avaliá-las;
7. registre limites e verifique se outra pessoa consegue reproduzir os resultados.

Para cada resultado, use a sequência abaixo:

- **Procedimento:** o que foi calculado, sobre quais registros e com qual regra?
- **Descrição:** que valores ou padrões aparecem?
- **Interpretação:** que leitura situada pode ser considerada?
- **Limite:** o que esse resultado não permite afirmar?
- **Próximo passo:** que caso, dado ou método deveria ser examinado?

Evite frases como “o gráfico prova”. Prefira “nesta base”, “o padrão observado” e
“uma hipótese a investigar”.'''),
  m('''## 1. Escopo e qualidade da base

### O que fazer

- formule uma pergunta exploratória compatível com os dados disponíveis;
- identifique corpus, período, unidade de análise e quantidade de registros;
- classifique as variáveis que serão utilizadas;
- informe ausências, erros conhecidos, cobertura e casos extremos;
- explique por que a base é adequada — ou apenas parcialmente adequada — à pergunta.

### O que entregar

| Elemento | Resposta |
|---|---|
| Pergunta exploratória | Escreva aqui. |
| Corpus e período | Escreva aqui. |
| Unidade de análise | Escreva aqui. |
| Variáveis e escalas | Escreva aqui. |
| Cobertura e ausências | Escreva aqui. |
| Erros conhecidos e casos extremos | Escreva aqui. |
| Adequação e principal limite | Escreva aqui. |

Não descreva apenas o arquivo. Explique a relação entre a pergunta e aquilo que cada
linha efetivamente representa.'''),
  m('''## 2. Perfil quantitativo

### O que fazer

1. apresente ao menos uma frequência absoluta e a proporção correspondente;
2. escolha uma variável quantitativa e calcule medidas de centro e dispersão;
3. examine sua distribuição e os limites de 1,5 IQR;
4. inspecione os registros sinalizados, sem removê-los automaticamente;
5. construa uma tabela de contingência com contagens e proporções por linha;
6. separe descrição, interpretação e hipótese.

### Evidências mínimas

| Resultado | Denominador ou convenção | Valor observado | Leitura e limite |
|---|---|---|---|
| frequência/proporção | Escreva aqui. | Escreva aqui. | Escreva aqui. |
| centro e dispersão | `ddof`, quartis e variável | Escreva aqui. | Escreva aqui. |
| caso extremo | limites inferior e superior | Escreva aqui. | Escreva aqui. |
| contingência | total de cada linha | Escreva aqui. | Escreva aqui. |

### Exemplo do nível de escrita esperado

> **Descrição:** D023 possui 2.100 palavras e é o único registro acima do limite
> superior de 1,5 IQR. **Interpretação:** ele pode representar um documento
> efetivamente mais extenso ou uma diferença de registro. **Limite:** a regra não
> demonstra erro e não justifica exclusão. **Próximo passo:** conferir a fonte e o
> procedimento de contagem de D023.

**Minha análise quantitativa:** Escreva aqui.'''),
  m('''## 3. Perfil textual

### O que fazer

- documente tokenização, conversão para minúsculas, pontuação e stopwords;
- apresente frequências absolutas e relativas com denominador explícito;
- escolha um termo relevante e examine concordâncias com identificador documental;
- apresente bigramas e PMI com frequência mínima declarada;
- compare TTR bruta e TTR em segmentos de tamanho comum;
- retorne ao texto sempre que uma contagem ou colocação parecer substantivamente
  importante.

### Evidências mínimas

| Etapa | Regra ou parâmetro | Resultado selecionado | Interpretação e limite |
|---|---|---|---|
| tokenização/normalização | Escreva aqui. | Escreva aqui. | Escreva aqui. |
| frequências | denominador: Escreva aqui. | Escreva aqui. | Escreva aqui. |
| concordância | termo e janela: Escreva aqui. | Escreva aqui. | Escreva aqui. |
| colocação | frequência mínima: Escreva aqui. | Escreva aqui. | Escreva aqui. |
| diversidade | tamanho comum: Escreva aqui. | Escreva aqui. | Escreva aqui. |

Uma lista de palavras não constitui interpretação. Explique como as regras de
processamento condicionam o que aparece no resultado.

**Meu perfil textual:** Escreva aqui.'''),
  m('''## 4. Visualizações

### O que fazer

Produza **quatro visualizações**, escolhendo famílias adequadas às perguntas e
variáveis. Uma combinação possível é: barras categóricas, histograma ou boxplot,
dispersão ou série temporal e barras de frequências textuais.

| Pergunta | Visual recomendado | O que deve acompanhar |
|---|---|---|
| como categorias se distribuem? | barras | contagens/proporções e denominador |
| como uma quantitativa se distribui? | histograma e/ou boxplot | intervalos, quartis e casos sinalizados |
| como duas quantitativas variam juntas? | dispersão | tabela dos pares e aviso de não causalidade |
| como um agregado muda por ano? | linha | tamanho e composição de cada grupo anual |
| quais termos são frequentes? | barras | tabela ordenada e regra de tokenização |

Para **cada figura**, entregue:

1. pergunta respondida e justificativa do tipo de gráfico;
2. título informativo, escalas e unidades;
3. tabela equivalente aos valores representados;
4. descrição alternativa acessível;
5. descrição do padrão e identificação de pelo menos um caso;
6. interpretação situada e limite.

**Figura 1 e análise:** Escreva aqui.

**Figura 2 e análise:** Escreva aqui.

**Figura 3 e análise:** Escreva aqui.

**Figura 4 e análise:** Escreva aqui.'''),
  m('''## 5. Retorno aos casos

![Agregados orientam a seleção de casos; a leitura próxima retorna para revisar categorias, contagens, hipóteses e limites.](imagens/04_ciclo_agregados_casos.svg)

### O que fazer

Escolha três casos que ajudem a compreender, contradizer ou qualificar os agregados.
Inclua obrigatoriamente um caso extremo ou inesperado e pelo menos um trecho textual.
Não selecione apenas exemplos que confirmem sua primeira interpretação.

| Caso/ID | Por que foi escolhido? | Evidência documental ou trecho | O que muda na leitura do agregado? |
|---|---|---|---|
| Caso 1 | Escreva aqui. | Escreva aqui. | Escreva aqui. |
| Caso 2 | Escreva aqui. | Escreva aqui. | Escreva aqui. |
| Caso 3 | Escreva aqui. | Escreva aqui. | Escreva aqui. |

O objetivo é praticar o movimento entre leitura distante e leitura próxima, não
usar três exemplos isolados como prova do comportamento de todo o corpus.'''),
  m('''## 6. Hipóteses provisórias

Formule no máximo três hipóteses. Cada uma deve permanecer compatível com o caráter
exploratório desta unidade.

| Hipótese provisória | Evidência exploratória | Explicação alternativa | Dados adicionais necessários | Método futuro |
|---|---|---|---|---|
| H1 | Escreva aqui. | Escreva aqui. | Escreva aqui. | Escreva aqui. |
| H2, se necessária | Escreva aqui. | Escreva aqui. | Escreva aqui. | Escreva aqui. |
| H3, se necessária | Escreva aqui. | Escreva aqui. | Escreva aqui. | Escreva aqui. |

Uma hipótese adequada poderia começar com “A diferença observada pode estar
associada a...”. Não use “comprovamos”, “é significativo” ou linguagem causal sem
desenho e evidência apropriados.'''),
  m('''## 7. Limitações e reprodutibilidade

### Limitações

Responda explicitamente:

- que grupos, períodos ou tipos de documento podem estar sub-representados?
- que escolhas de limpeza, tokenização ou agregação afetam os resultados?
- que padrões podem resultar da construção fictícia ou institucional da base?
- quais conclusões não devem ser formuladas?

**Limitações do relatório:** Escreva aqui.

### Reprodutibilidade

Outra pessoa deve conseguir identificar:

- arquivo e versão da entrada;
- ambiente e dependências;
- ordem dos notebooks ou células;
- parâmetros alterados, como stopwords, janela, frequência mínima e bins;
- tabelas que sustentam cada gráfico;
- caminho entre agregado, ID e documento.

**Instruções para reproduzir:** Escreva aqui.'''),
  m('''## 8. Estrutura do relatório final

Organize a entrega nesta ordem:

1. pergunta, corpus, unidade e qualidade da base;
2. perfil quantitativo;
3. perfil textual;
4. quatro visualizações com tabelas equivalentes;
5. retorno aos três casos;
6. hipóteses provisórias e alternativas;
7. limitações;
8. instruções de reprodução;
9. referências utilizadas.

O relatório pode ser entregue neste notebook preenchido ou em documento equivalente,
desde que preserve essas evidências e a ligação com o notebook técnico.'''),
  m('''## 9. Dinâmica sugerida e revisão por pares

Para uma aula de quatro horas, a meta é produzir uma primeira versão completa do
relatório. Os cálculos básicos já devem ter sido executados nos Notebooks 01 a 03.

| Tempo | Trabalho |
|---:|---|
| 20 min | definir pergunta, unidade e diagnóstico da base |
| 40 min | selecionar resultados quantitativos e conferir denominadores |
| 15 min | pausa |
| 40 min | selecionar resultados textuais e retornar a concordâncias |
| 40 min | escolher quatro visualizações e suas tabelas equivalentes |
| 15 min | pausa |
| 30 min | selecionar três casos e formular hipóteses alternativas |
| 20 min | revisão por um colega |
| 20 min | incorporar correções, limites e instruções de reprodução |

O colega revisor deve conseguir responder: “Qual é a unidade?”, “Qual é o
denominador?”, “Que caso sustenta ou contradiz a leitura?”, “O gráfico possui tabela e
descrição?” e “A hipótese está apresentada como provisória?”.

**Parecer recebido:** Escreva aqui.

**Mudanças realizadas após a revisão:** Escreva aqui.'''),
  m('''## 10. Rubrica e checklist de entrega

Avalie cada critério de 0 a 2. Use 0 para ausente ou inadequado, 1 para parcial e 2
para completo e justificável.

| Critério | 0 | 1 | 2 | Minha nota e evidência |
|---|---|---|---|---|
| escopo e qualidade | não definidos | parciais | pergunta, unidade, cobertura e limites coerentes | Escreva aqui. |
| correção quantitativa | cálculos inadequados | resultados sem convenções | medidas, denominadores e extremos verificados | Escreva aqui. |
| exploração textual | regras ausentes | resultados sem contexto | regras, métricas e concordâncias documentadas | Escreva aqui. |
| visualização e acessibilidade | gráficos inadequados | documentação parcial | quatro figuras com tabela e descrição | Escreva aqui. |
| retorno aos casos | ausente | casos apenas confirmatórios | três casos que qualificam agregados | Escreva aqui. |
| hipóteses e limites | conclusão indevida | limites genéricos | hipóteses alternativas e limites específicos | Escreva aqui. |
| reprodutibilidade | percurso desconhecido | instruções incompletas | entradas, parâmetros e ordem reconstruíveis | Escreva aqui. |

**Total:** Escreva aqui, de 14 pontos. A referência de aprovação é 11/14, sem zero
em correção quantitativa ou hipóteses e limites.

Antes de entregar, confirme: quatro visualizações, quatro tabelas equivalentes, três
casos, no máximo três hipóteses, limitações específicas, instruções de reprodução e
referências. A Unidade 5 tratará inferência; não acrescente significância estatística
sem que o método tenha sido estudado.'''),
 ]
def readme():
 links=tabela_links_colab(U.name,(
  ("Guia da unidade","00_guia_da_unidade.ipynb"),
  ("Exploração quantitativa","01_exploracao_quantitativa.ipynb"),
  ("Exploração textual","02_exploracao_textual.ipynb"),
  ("Visualização exploratória","03_visualizacao_exploratoria.ipynb"),
  ("Oficina do relatório","04_oficina_relatorio_exploratorio.ipynb"),
 ))
 conteudo=f'''# Unidade 4 — Exploração

## Ordem de estudo

Execute os notebooks 00 a 04. O produto da unidade é um relatório
exploratório; a inferência fica para a Unidade 5.

## Abrir os notebooks no Google Colab

{links}

O link carrega o notebook diretamente do GitHub. Nos Notebooks 00 a 03,
execute primeiro a célula **Preparação do ambiente**; ela clona o repositório
no ambiente temporário e posiciona a execução nesta unidade. O Notebook 04 é
discursivo e não precisa de clonagem.

## Dependências e dados

Requer pandas, NumPy, IPython e Jupyter. Os dados são fictícios.

As fórmulas são escritas em LaTeX nas células Markdown e renderizadas pelo
Jupyter/Colab, sem pacote adicional. Cada fórmula é acompanhada de definição em
linguagem corrente e da operação correspondente em Python.

O arquivo `exercicios_unidade_04_texto.md` reúne 18 questões de múltipla
escolha; as respostas comentadas ficam em `gabaritos/`.

A pasta `imagens/` reúne uma ilustração conceitual e oito diagramas SVG
acessíveis. Finalidade, proveniência e textos alternativos estão documentados em
`imagens/README.md`. Os gráficos calculados permanecem nos notebooks e são
acompanhados de tabelas equivalentes. O módulo local `graficos.py` produz esses
gráficos em SVG sem acrescentar uma biblioteca gráfica ao ambiente didático;
projetos futuros podem substituir essa camada por Matplotlib, Altair ou outra
biblioteca adequada às suas necessidades.
'''
 (U/"README.md").write_text(conteudo,encoding="utf-8")
def main():
 U.mkdir(exist_ok=True); dados(); nb("00_guia_da_unidade.ipynb",guia(),True); nb("01_exploracao_quantitativa.ipynb",quant(),True); nb("02_exploracao_textual.ipynb",texto(),True); nb("03_visualizacao_exploratoria.ipynb",visual(),True); nb("04_oficina_relatorio_exploratorio.ipynb",oficina()); readme(); print("Unidade 4 construída")
if __name__=="__main__": main()
