"""Constrói a Unidade 4."""
import csv,json
from pathlib import Path
from textwrap import dedent
from apoio_colab import adicionar_link_na_abertura, preparacao_colab, tabela_links_colab
R=Path(__file__).resolve().parents[1]; U=R/"unidade_04"; D=U/"dados"
def m(s): return {"cell_type":"markdown","metadata":{},"source":dedent(s).strip().splitlines(keepends=True)}
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
Exploração descreve, diagnostica e formula perguntas; não confirma hipóteses retrospectivas. Arnold e Tilton (2019) relacionam estatística exploratória, visualização e computação às Humanidades Digitais. Drucker (2011) lembra que gráficos incorporam escolhas.'''),m('''## Percurso
01 exploração quantitativa; 02 textual; 03 visual; 04 relatório. Os 24 registros são fictícios e D023 é extremo deliberado.'''),c('''import json,pandas as pd
dados=pd.read_csv("dados/documentos.csv"); prov=json.loads(open("dados/proveniencia.json",encoding="utf-8").read()); print(dados.shape,prov["natureza"]); dados.head()'''),m('''## Regra de escrita
Separe descrição do cálculo, interpretação situada e hipótese provisória. Testes, confiança e comparação inferencial ficam para a Unidade 5.
### Diagnóstico
Que padrão espera e que saída revelaria erro? Escreva aqui.'''),m('''## Produto
Relatório com tabelas, quatro famílias de gráficos, perfil textual, concordâncias, casos extremos, hipóteses e limites.''')]
def quant():
 return [
  m('''# Exploração quantitativa
## Tipos de variáveis
Nominais distinguem; ordinais ordenam; quantitativas discretas contam; contínuas medem. Datas e identificadores têm papéis próprios. `dtype` não determina a escala conceitual.'''),
  c('''import pandas as pd
import numpy as np

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
Tokenizar segmenta por regra. Minúsculas, pontuação e stopwords podem apagar distinções; preserve o texto e documente decisões. Neste exemplo, os tokens são calculados separadamente por documento para não criar contextos ou n-gramas entre o fim de um texto e o início do seguinte.'''),
  c('''import math
import re
from collections import Counter

import pandas as pd

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
diversidade.head()'''),
  m('''## Atividade
Documente regras, frequências, concordâncias, n-gramas, colocação e diversidade. Retorne a trechos. Escreva aqui.'''),
 ]
def visual(): return [m('''# Visualização exploratória
Gráficos são argumentos. Toda figura terá título, descrição e tabela equivalente. Usaremos SVG acessível e offline.'''),c('''import pandas as pd,re
from collections import Counter
from IPython.display import SVG,display
dados=pd.read_csv("dados/documentos.csv")
def barras(rotulos,valores,titulo):
 m=max(valores) or 1; corpo=f'<text x="10" y="22">{titulo}</text>'
 for i,(r,v) in enumerate(zip(rotulos,valores)):
  y=40+i*32; z=400*v/m; corpo+=f'<text x="10" y="{y+16}">{r}</text><rect x="120" y="{y}" width="{z}" height="20" fill="#356a7a"/><text x="{130+z}" y="{y+16}">{v:.1f}</text>'
 return SVG(f'<svg xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{titulo}" width="650" height="{70+32*len(valores)}">{corpo}</svg>')
def pontos(xs,ys,titulo,linha=False):
 xmin,xmax=min(xs),max(xs); ymin,ymax=min(ys),max(ys); ps=[(50+550*(x-xmin)/(xmax-xmin or 1),320-260*(y-ymin)/(ymax-ymin or 1)) for x,y in zip(xs,ys)]; b=f'<text x="10" y="20">{titulo}</text>'
 if linha: b+=f'<polyline points="{" ".join(f"{x},{y}" for x,y in ps)}" fill="none" stroke="#356a7a"/>'
 else:
  for x,y in ps: b+=f'<circle cx="{x}" cy="{y}" r="5" fill="#9a4f37"/>'
 return SVG(f'<svg xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{titulo}" width="650" height="350">{b}</svg>')'''),m('''## Barras — categorias'''),c('''f=dados.tema.value_counts(); display(barras(f.index,f.values,"Documentos por tema")); f'''),m(r'''## Histograma e boxplot — distribuições

Se os limites dos intervalos são $b_0,b_1,\ldots,b_J$, a altura da barra $j$
é a quantidade de valores dentro daquele intervalo:

\[
h_j=\sum_{i=1}^{n}\mathbf{1}(b_{j-1}<x_i\leq b_j).
\]

Alterar os limites $b_j$ pode mudar a forma visível da distribuição, mesmo sem
alterar os documentos. O boxplot retoma $Q_1$, mediana, $Q_3$ e os limites de
1,5 IQR apresentados no Notebook 01. A tabela abaixo oferece os intervalos e o
resumo numérico equivalentes.'''),c('''faixas=[0,400,600,800,1000,2200]; h=dados.groupby(pd.cut(dados.palavras,faixas),observed=False).size(); display(barras(h.index.astype(str),h.values,"Histograma da extensão")); q=dados.palavras.quantile([0,.25,.5,.75,1]); sc=lambda x:60+520*(x-q.iloc[0])/(q.iloc[-1]-q.iloc[0]); svg=f'<svg xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Boxplot da extensão: mínimo {q.iloc[0]}, Q1 {q.iloc[1]}, mediana {q.iloc[2]}, Q3 {q.iloc[3]}, máximo {q.iloc[4]}" width="650" height="180"><line x1="{sc(q.iloc[0])}" y1="90" x2="{sc(q.iloc[4])}" y2="90" stroke="black"/><rect x="{sc(q.iloc[1])}" y="55" width="{sc(q.iloc[3])-sc(q.iloc[1])}" height="70" fill="#b9d4dc" stroke="black"/><line x1="{sc(q.iloc[2])}" y1="55" x2="{sc(q.iloc[2])}" y2="125" stroke="#9a4f37"/></svg>'; display(SVG(svg)); h,dados.palavras.describe()'''),m('''## Dispersão — relação entre quantitativas
Padrão visual não implica causalidade.'''),c('''display(pontos(dados.paginas.tolist(),dados.palavras.tolist(),"Páginas e palavras")); dados[["paginas","palavras"]].head()'''),m(r'''## Série temporal

Se $n_t$ documentos pertencem ao ano $t$, a média anual representada pela
linha é:

\[
\bar{x}_t=\frac{1}{n_t}\sum_{i:\,\mathrm{ano}_i=t}x_i.
\]

A fórmula torna visível o denominador anual. A linha conecta agregados dos
documentos disponíveis; ela também reflete a composição do corpus e não demonstra,
por si só, uma mudança histórica contínua.'''),c('''media_por_ano = dados.groupby("ano")["palavras"].mean()
display(pontos(media_por_ano.index.tolist(),media_por_ano.values.tolist(),"Média por ano",linha=True))
media_por_ano'''),m('''## Frequências textuais
Barras preservam valores melhor que nuvem de palavras.'''),c('''co=Counter(re.findall(r"[a-záàâãéêíóôõúç]+"," ".join(dados.texto).lower())); stop={"a","o","e","de","do","da","como","em","nas","um","uma","também"}; top=[z for z in co.most_common() if z[0] not in stop][:10]; display(barras([p for p,n in top],[n for p,n in top],"Termos frequentes")); pd.DataFrame(top,columns=["termo","frequencia"])'''),m('''## Atividade
Produza barras, histograma/boxplot, dispersão ou tempo e frequência textual. Para cada: tabela, descrição, escala, padrão, caso, limite e hipótese. Escreva aqui.''')]
def oficina(): return [m('''# Oficina — Relatório exploratório
Roteiro discursivo; execute análises em notebook próprio.'''),m('''## Escopo e qualidade
Pergunta, corpus, unidade, cobertura, variáveis, ausências, extremos e erros: Escreva aqui.'''),m('''## Perfil quantitativo
Frequências/proporções; centro/dispersão; distribuição; extremos; contingência; descrição e interpretação: Escreva aqui.'''),m('''## Perfil textual
Regras; frequências; concordâncias; n-gramas; colocações; diversidade e tamanho: Escreva aqui.'''),m('''## Visualizações
Inclua quatro famílias com tabela, descrição alternativa, interpretação e limite. Escreva aqui.'''),m('''## Retorno aos casos
Escolha três documentos ou trechos que qualifiquem agregados. Escreva aqui.'''),m('''## Hipóteses provisórias
Até três hipóteses com evidência, alternativas, dados adicionais e método futuro. Escreva aqui.'''),m('''## Rubrica e entrega
Avalie de 0 a 2: escopo, estatística, texto, visualização/acessibilidade, casos, limites e reprodutibilidade. A Unidade 5 tratará inferência. Escreva aqui.''')]
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

Requer pandas, NumPy e Jupyter. Os dados são fictícios.

As fórmulas são escritas em LaTeX nas células Markdown e renderizadas pelo
Jupyter/Colab, sem pacote adicional. Cada fórmula é acompanhada de definição em
linguagem corrente e da operação correspondente em Python.
'''
 (U/"README.md").write_text(conteudo,encoding="utf-8")
def main():
 U.mkdir(exist_ok=True); dados(); nb("00_guia_da_unidade.ipynb",guia(),True); nb("01_exploracao_quantitativa.ipynb",quant(),True); nb("02_exploracao_textual.ipynb",texto(),True); nb("03_visualizacao_exploratoria.ipynb",visual(),True); nb("04_oficina_relatorio_exploratorio.ipynb",oficina()); readme(); print("Unidade 4 construída")
if __name__=="__main__": main()
