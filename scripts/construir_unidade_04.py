"""Constrói a Unidade 4."""
import csv,json
from pathlib import Path
from textwrap import dedent
R=Path(__file__).resolve().parents[1]; U=R/"unidade_04"; D=U/"dados"
def m(s): return {"cell_type":"markdown","metadata":{},"source":dedent(s).strip().splitlines(keepends=True)}
def c(s): return {"cell_type":"code","execution_count":None,"metadata":{},"outputs":[],"source":dedent(s).strip().splitlines(keepends=True)}
def nb(n,cells):
 d={"cells":cells,"metadata":{"kernelspec":{"display_name":"Python 3","language":"python","name":"python3"},"language_info":{"name":"python","version":"3"}},"nbformat":4,"nbformat_minor":5}
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
def quant(): return [m('''# Exploração quantitativa
## Tipos de variáveis
Nominais distinguem; ordinais ordenam; quantitativas discretas contam; contínuas medem. Datas e identificadores têm papéis próprios. `dtype` não determina a escala conceitual.'''),c('''import pandas as pd,numpy as np
dados=pd.read_csv("dados/documentos.csv")
pd.DataFrame([["genero","nominal"],["ano","temporal"],["palavras","quantitativa discreta"],["id_documento","identificador"]],columns=["variavel","escala"])'''),m('''## Frequências e proporções
Declare o denominador: documentos não medem automaticamente intensidade ou importância.'''),c('''pd.concat([dados.tema.value_counts().rename("frequencia"),dados.tema.value_counts(normalize=True).rename("proporcao")],axis=1)'''),m('''## Centro, quartis e dispersão
Média é sensível a extremos; mediana é posição; moda é frequência. Variância e desvio-padrão descrevem dispersão em torno da média.'''),c('''x=dados.palavras
pd.Series({"media":x.mean(),"mediana":x.median(),"moda":x.mode().iloc[0],"q1":x.quantile(.25),"q3":x.quantile(.75),"variancia":x.var(),"desvio_padrao":x.std()})'''),m('''## Distribuição e valores extremos
A regra 1,5×IQR sinaliza inspeção, nunca exclusão automática.'''),c('''q1,q3=x.quantile([.25,.75]); iqr=q3-q1; limite=q3+1.5*iqr
dados[x>limite][["id_documento","palavras","genero","tema"]]'''),m('''## Tabela de contingência
Contagens e proporções por linha respondem perguntas diferentes. Padrão não é teste ou explicação.'''),c('''pd.crosstab(dados.genero,dados.tema),pd.crosstab(dados.genero,dados.tema,normalize="index").round(2)'''),m('''## Atividade
Classifique variáveis, escolha medidas e denominadores, inspecione extremo e contingência. Separe descrição, interpretação e hipótese. Escreva aqui.''')]
def texto(): return [m('''# Exploração textual
## Tokenização e normalização
Tokenizar segmenta por regra. Minúsculas, pontuação e stopwords podem apagar distinções; preserve o texto e documente decisões.'''),c('''import re,math,pandas as pd
from collections import Counter
dados=pd.read_csv("dados/documentos.csv")
def tok(s): return re.findall(r"[a-záàâãéêíóôõúç]+",s.lower())
dados["tokens"]=dados.texto.map(tok); todos=[t for d in dados.tokens for t in d]; dados[["id_documento","tokens"]].head(2)'''),m('''## Frequências absoluta e relativa
A relativa usa o total de tokens. Stopwords são escolha analítica.'''),c('''freq=Counter(todos); total=len(todos); stop={"a","o","e","de","do","da","como","em","nas","um","uma","também"}
pd.DataFrame([(p,n,n/total) for p,n in freq.most_common() if p not in stop][:12],columns=["palavra","frequencia","relativa"])'''),m('''## Concordâncias
Janelas recuperam contexto perdido pelo agregado.'''),c('''def concord(ts,a,j=4): return [" ".join(ts[max(0,i-j):i+j+1]) for i,t in enumerate(ts) if t==a]
concord(todos,"trabalho")[:8]'''),m('''## N-gramas e colocações
N-gramas preservam adjacência. PMI favorece raros; use frequência mínima e concordâncias.'''),c('''bi=Counter(zip(todos,todos[1:])); N=sum(bi.values()); linhas=[]
for (a,b),n in bi.items():
 if n>=3: linhas.append((a+" "+b,n,math.log2(n*N/(freq[a]*freq[b]))))
pd.DataFrame(sorted(linhas,key=lambda z:z[2],reverse=True),columns=["bigrama","freq","pmi"]).head(10)'''),m('''## Vocabulário e diversidade lexical
Types são formas, tokens ocorrências. TTR cai com tamanho; compare amostras padronizadas.'''),c('''def div(ts,n=25): a=ts[:n]; return len(set(a))/len(a) if a else 0
pd.DataFrame({"id":dados.id_documento,"tokens":dados.tokens.map(len),"types":dados.tokens.map(lambda z:len(set(z))),"ttr":dados.tokens.map(lambda z:len(set(z))/len(z)),"ttr_25":dados.tokens.map(div)}).head()'''),m('''## Atividade
Documente regras, frequências, concordâncias, n-gramas, colocação e diversidade. Retorne a trechos. Escreva aqui.''')]
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
 return SVG(f'<svg xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{titulo}" width="650" height="350">{b}</svg>')'''),m('''## Barras — categorias'''),c('''f=dados.tema.value_counts(); display(barras(f.index,f.values,"Documentos por tema")); f'''),m('''## Histograma e boxplot — distribuições
Bins alteram histogramas; boxplots resumem quartis. A tabela abaixo oferece faixas e resumo equivalentes.'''),c('''faixas=[0,400,600,800,1000,2200]; h=dados.groupby(pd.cut(dados.palavras,faixas),observed=False).size(); display(barras(h.index.astype(str),h.values,"Histograma da extensão")); q=dados.palavras.quantile([0,.25,.5,.75,1]); sc=lambda x:60+520*(x-q.iloc[0])/(q.iloc[-1]-q.iloc[0]); svg=f'<svg xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Boxplot da extensão: mínimo {q.iloc[0]}, Q1 {q.iloc[1]}, mediana {q.iloc[2]}, Q3 {q.iloc[3]}, máximo {q.iloc[4]}" width="650" height="180"><line x1="{sc(q.iloc[0])}" y1="90" x2="{sc(q.iloc[4])}" y2="90" stroke="black"/><rect x="{sc(q.iloc[1])}" y="55" width="{sc(q.iloc[3])-sc(q.iloc[1])}" height="70" fill="#b9d4dc" stroke="black"/><line x1="{sc(q.iloc[2])}" y1="55" x2="{sc(q.iloc[2])}" y2="125" stroke="#9a4f37"/></svg>'; display(SVG(svg)); h,dados.palavras.describe()'''),m('''## Dispersão — relação entre quantitativas
Padrão visual não implica causalidade.'''),c('''display(pontos(dados.paginas.tolist(),dados.palavras.tolist(),"Páginas e palavras")); dados[["paginas","palavras"]].head()'''),m('''## Série temporal
Agregação anual também reflete composição do corpus.'''),c('''a=dados.groupby("ano").palavras.mean(); display(pontos(a.index.tolist(),a.values.tolist(),"Média por ano",linha=True)); a'''),m('''## Frequências textuais
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
def main():
 U.mkdir(exist_ok=True); dados(); nb("00_guia_da_unidade.ipynb",guia()); nb("01_exploracao_quantitativa.ipynb",quant()); nb("02_exploracao_textual.ipynb",texto()); nb("03_visualizacao_exploratoria.ipynb",visual()); nb("04_oficina_relatorio_exploratorio.ipynb",oficina()); (U/"README.md").write_text("# Unidade 4 — Exploração\n\nExecute notebooks 00–04. Requer pandas, NumPy e Jupyter. Dados são fictícios. Produto: relatório exploratório; inferência fica para a Unidade 5.\n",encoding="utf-8"); print("Unidade 4 construída")
if __name__=="__main__": main()
