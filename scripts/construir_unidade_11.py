"""Constrói a Unidade 11 — análise temporal e espacial."""
from __future__ import annotations
import csv,json,math,random
from pathlib import Path
from textwrap import dedent
from apoio_colab import adicionar_link_na_abertura,preparacao_colab,tabela_links_colab
R=Path(__file__).resolve().parents[1];U=R/"unidade_11";D=U/"dados"
def md(s):return {"cell_type":"markdown","metadata":{},"source":dedent(s).strip().splitlines(keepends=True)}
def code(s):return {"cell_type":"code","execution_count":None,"metadata":{},"outputs":[],"source":dedent(s).strip().splitlines(keepends=True)}
def salvar(n,cs,d=True):
 o=[adicionar_link_na_abertura(cs[0],U.name,n)];o+=([code(preparacao_colab(U.name))] if d else []);o+=cs[1:]
 (U/n).write_text(json.dumps({"cells":o,"metadata":{"kernelspec":{"display_name":"Python 3","language":"python","name":"python3"},"language_info":{"name":"python","version":"3"}},"nbformat":4,"nbformat_minor":5},ensure_ascii=False,indent=1)+"\n",encoding="utf-8")
def criar_dados():
 D.mkdir(parents=True,exist_ok=True);rng=random.Random(20261025);serie=[]
 for ano in range(1960,2021):
  pop=42000*(1.018**(ano-1960)); base=18+0.55*(ano-1960)+4*math.sin((ano-1960)/5); eventos=max(1,round(base+rng.gauss(0,3)))
  definicao="registro administrativo A" if ano<1990 else "registro ampliado B"
  if ano>=1990:eventos+=12
  serie.append([ano,round(pop),eventos,round(eventos/pop*100000,2),definicao])
 with (D/"serie_cultural.csv").open("w",encoding="utf-8",newline="") as f:w=csv.writer(f);w.writerow(["ano","populacao","eventos","taxa_100mil","definicao"]);w.writerows(serie)
 termos=[]
 for ano in range(1960,2021):
  total=80+(ano-1960)%12; patrimonio=max(1,round(12+.35*(ano-1960)+rng.gauss(0,2)));digital=max(0,round(-4+.32*(ano-1990)+rng.gauss(0,1.5))) if ano>=1990 else 0
  termos.append([ano,total,patrimonio,digital])
 with (D/"termos_por_ano.csv").open("w",encoding="utf-8",newline="") as f:w=csv.writer(f);w.writerow(["ano","documentos","mencoes_patrimonio","mencoes_digital"]);w.writerows(termos)
 esp=[]
 for i in range(16):
  x=i%4;y=i//4;pop=9000+3500*x+2200*y+rng.randint(-1000,1000);idosos=.08+.035*y; jovens=.22-.02*y
  casos=round(pop*(.0018+.008*idosos)+rng.gauss(0,2));equip=max(1,round(pop/8000+1.2*x+rng.gauss(0,1)))
  esp.append([f"T{i+1:02d}",f"Território Fictício {i+1:02d}",x,y,pop,round(jovens,3),round(idosos,3),casos,equip])
 with (D/"territorios.csv").open("w",encoding="utf-8",newline="") as f:w=csv.writer(f);w.writerow(["codigo","territorio","x","y","populacao","prop_jovens","prop_idosos","ocorrencias","equipamentos"]);w.writerows(esp)
 prov={"natureza":"dados inteiramente fictícios","semente":20261025,"ruptura":"em 1990 a definição de evento foi ampliada deliberadamente","geografia":"grade abstrata 4 x 4, sem correspondência territorial real","limite":"não sustenta afirmações históricas, demográficas ou espaciais reais"}
 (D/"proveniencia.json").write_text(json.dumps(prov,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
def svg(n,t,es,r):
 w=190;gap=(920-len(es)*w)/max(1,len(es)-1);a=[]
 for i,e in enumerate(es):
  x=40+i*(w+gap);a.append(f'<rect x="{x:.0f}" y="82" width="{w}" height="112" rx="14" fill="#f4f0e6" stroke="#294c60" stroke-width="2"/><text x="{x+w/2:.0f}" y="140" text-anchor="middle" font-size="17">{e}</text>')
  if i<len(es)-1:a.append(f'<path d="M{x+w+5:.0f} 140 H{x+w+gap-8:.0f}" stroke="#a44a3f" stroke-width="3" marker-end="url(#a)"/>')
 (U/"imagens"/n).write_text(f'<svg xmlns="http://www.w3.org/2000/svg" width="1000" height="280" role="img" aria-labelledby="title desc"><title id="title">{t}</title><desc id="desc">{r}</desc><defs><marker id="a" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L0,6 L9,3 z" fill="#a44a3f"/></marker></defs><rect width="100%" height="100%" fill="#fffdf8"/><text x="500" y="40" text-anchor="middle" font-size="25" font-weight="bold">{t}</text>{"".join(a)}<text x="500" y="245" text-anchor="middle" font-size="16">{r}</text></svg>',encoding="utf-8")
def guia():return [md('''# Unidade 11 — Guia de estudo
## Como analisar mudanças no tempo e no espaço?

Tempo e espaço não são colunas neutras: dependem de calendários, períodos, cobertura,
fronteiras e escalas. Uma linha ou mapa descreve unidades construídas e precisa manter
visíveis mudanças de definição e denominadores.

![Percurso da unidade.](imagens/00_percurso_tempo_espaco.svg)'''),md('''## Percurso

| Notebook | Pergunta | Produto |
|---|---|---|
| 00 | Que tempo e território foram construídos? | contrato analítico |
| 01 | Como medir mudança? | taxas e crescimento |
| 02 | Tendência resiste a recortes e definições? | sensibilidade temporal |
| 03 | Palavras/temas mudam ou muda o corpus? | série textual normalizada |
| 04 | Como mapear sem naturalizar áreas? | taxas e mapa crítico |
| 05 | Qual percurso serve ao projeto? | incremento cumulativo |'''),code('''import json,pandas as pd
serie=pd.read_csv("dados/serie_cultural.csv");territorios=pd.read_csv("dados/territorios.csv")
print(json.loads(open("dados/proveniencia.json",encoding="utf-8").read())["natureza"])
display(serie.head(3));display(territorios.head(3))'''),md('''### U11-A01 — Discussão — coluna ou construção?

**Dinâmica (15 minutos):** para “eventos aumentaram após 1990”, identifique unidade,
denominador, cobertura, ruptura de definição e duas periodizações possíveis. Reescreva
a afirmação de modo testável. **Resposta:** escreva aqui.

## Passagem

Começaremos por distinguir contagem, taxa e crescimento, três respostas diferentes.''')]
def series():return [md('''# Datas, taxas de crescimento e séries

Contagens respondem “quantos”; taxas ajustam por população exposta; crescimento
compara valores no tempo. Nenhuma medida corrige automaticamente mudança documental.

![Contagem, denominador e taxa.](imagens/01_taxas.svg)'''),code('''import pandas as pd,matplotlib.pyplot as plt
d=pd.read_csv("dados/serie_cultural.csv");d["crescimento_pct"]=d.eventos.pct_change()*100
display(d.loc[d.ano.isin([1960,1989,1990,2020])])
fig,ax=plt.subplots(2,1,figsize=(10,6),sharex=True);ax[0].plot(d.ano,d.eventos);ax[0].set_ylabel("Eventos");ax[1].plot(d.ano,d.taxa_100mil);ax[1].set_ylabel("Taxa por 100 mil");ax[1].set_xlabel("Ano");plt.tight_layout();plt.show()'''),md('''A taxa é $r_t=(y_t/N_t)\\times100000$. O crescimento anual é
$g_t=((y_t-y_{t-1})/y_{t-1})\\times100$. Crescimento instável pode resultar de base
pequena; compare também níveis absolutos.

### U11-A02 — Atividade — três leituras da mudança

Escolha dois anos e interprete contagem, taxa e crescimento. Depois investigue 1990 na
proveniência. **Dinâmica (25 minutos):** individual no cálculo, dupla na crítica da
ruptura. **Resposta:** escreva aqui.

## Passagem

Oscilações anuais dificultam enxergar padrões; médias móveis ajudam, mas deslocam e
suavizam eventos. O próximo notebook compara decisões de janela e período.''')]
def tendencia():return [md('''# Tendência, médias móveis e rupturas

Média móvel é resumo local: janela curta preserva ruído; longa suaviza mudanças. Ela
não explica causas. Uma mudança de definição deve aparecer no gráfico e na conclusão.

![Janelas diferentes produzem curvas diferentes.](imagens/02_janelas.svg)'''),code('''import pandas as pd,matplotlib.pyplot as plt
d=pd.read_csv("dados/serie_cultural.csv")
for j in [3,5,9]:d[f"media_{j}"]=d.taxa_100mil.rolling(j,center=True).mean()
ax=d.plot(x="ano",y=["taxa_100mil","media_3","media_9"],figsize=(10,4));ax.axvline(1990,color="black",linestyle="--",label="mudança de definição");ax.set_ylabel("Taxa por 100 mil");plt.tight_layout();plt.show()
periodos=pd.cut(d.ano,[1959,1979,1989,2004,2020],labels=["1960–1979","1980–1989","1990–2004","2005–2020"])
resumo=d.groupby(periodos,observed=True).taxa_100mil.agg(["count","mean","median"]);display(resumo.round(2))'''),md('''## Comparabilidade

Comparar antes/depois de 1990 mistura mudança substantiva e ampliação do registro.
Soluções: restringir à definição comum, modelar ruptura, apresentar séries separadas ou
declarar incomparabilidade. Escolher depende dos metadados, não só do gráfico.

### U11-A03 — Atividade — janela e definição

Compare janelas 3 e 9; descreva o que cada uma apaga. Proponha duas formas de tratar
1990 e diga qual adotaria. **Dinâmica (30 minutos):** trios defendem decisões distintas
e registram a divergência. **Resposta:** escreva aqui.

## Passagem

Em textos, o denominador também muda: contagens de palavras crescem quando há mais
documentos. Normalizaremos antes de interpretar temas ao longo do tempo.''')]
def textual():return [md('''# Temas e palavras ao longo do tempo

Contagem lexical depende do volume do corpus. Usaremos menções por 100 documentos e
uma média móvel, preservando a diferença entre palavra, tema e conceito.

![Corpus, contagem, normalização e releitura.](imagens/03_tempo_textual.svg)'''),code('''import pandas as pd,matplotlib.pyplot as plt
d=pd.read_csv("dados/termos_por_ano.csv")
for termo in ["patrimonio","digital"]:
 d[f"taxa_{termo}"]=100*d[f"mencoes_{termo}"]/d.documentos
 d[f"media_{termo}"]=d[f"taxa_{termo}"].rolling(5,center=True).mean()
display(d.loc[d.ano.isin([1960,1990,2000,2020])].round(2))
d.plot(x="ano",y=["media_patrimonio","media_digital"],figsize=(10,4));plt.ylabel("Menções por 100 documentos — média móvel de 5 anos");plt.tight_layout();plt.show()'''),md('''A emergência de “digital” pode refletir novo vocabulário, OCR, composição do corpus
ou fenômeno histórico. Inspecione concordâncias e gêneros antes de nomear um tema.

### U11-A04 — Atividade — curva e corpus

Escolha uma curva, identifique denominador e bordas sem média, leia anos extremos e
formule duas explicações rivais. **Dinâmica (25 minutos):** dupla alterna gráfico e
metadados. **Resposta:** escreva aqui.

## Passagem

Do tempo passamos ao espaço. A mesma regra permanece: taxas dependem de denominadores,
e padrões dependem das fronteiras escolhidas.''')]
def espacial():return [md('''# Distribuição espacial, taxas e unidades geográficas

Um mapa coroplético colore áreas por valores comparáveis. Contagens brutas confundem
tamanho populacional; taxas instáveis em populações pequenas exigem cautela. A grade é
abstrata e não representa lugar real.

![Do código territorial ao mapa e à crítica das unidades.](imagens/04_mapa_critico.svg)'''),code('''import pandas as pd,numpy as np,matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
d=pd.read_csv("dados/territorios.csv");d["taxa_bruta"]=100000*d.ocorrencias/d.populacao
# Padronização direta didática com duas faixas e população-padrão 70%/30%.
d["taxa_jovens_est"]=120+40*d.x;d["taxa_idosos_est"]=650+55*d.y
d["taxa_padronizada"]=.7*d.taxa_jovens_est+.3*d.taxa_idosos_est
fig,eixos=plt.subplots(1,2,figsize=(10,4))
for ax,col,titulo in zip(eixos,["ocorrencias","taxa_bruta"],["Contagem","Taxa por 100 mil"]):
 norm=plt.Normalize(d[col].min(),d[col].max())
 for _,r in d.iterrows():ax.add_patch(Rectangle((r.x,r.y),1,1,facecolor=plt.cm.viridis(norm(r[col])),edgecolor="white"));ax.text(r.x+.5,r.y+.5,r.codigo,ha="center",va="center",fontsize=8)
 ax.set(xlim=(0,4),ylim=(0,4),aspect="equal",title=titulo);ax.axis("off")
plt.tight_layout();plt.show();display(d[["codigo","populacao","ocorrencias","taxa_bruta","taxa_padronizada"]].round(1))'''),md('''## Falácia ecológica e problema das unidades geográficas

Associação entre territórios não implica associação entre indivíduos: essa passagem é
a **falácia ecológica**. Agregar as 16 células em linhas ou quadrantes pode mudar o
padrão — problema das unidades espaciais modificáveis (MAUP). Fronteiras são escolhas
administrativas e analíticas.

### U11-A05 — Atividade — dois mapas, duas histórias

Compare contagem e taxa, escolha dois territórios cuja posição muda e explique por
quê. Reagrupe mentalmente por linhas/quadrantes e escreva uma conclusão que não cometa
falácia ecológica. **Dinâmica (35 minutos):** trios com papéis de cartógrafo, demógrafo
e crítico territorial. **Resposta:** escreva aqui.

## Passagem

A oficina pede um percurso temporal ou espacial pertinente, não ambos por obrigação.''')]
def oficina():return [md('''# Oficina — transformação temporal ou distribuição espacial

**Produto:** seção no mesmo relatório-notebook. Escolha tempo, espaço ou não adoção
fundamentada. Não entregue outro arquivo.

![Decisões, gráfico, casos e limites formam a entrega.](imagens/05_entrega.svg)'''),md('''## Roteiro de 75 minutos

| Tempo | Ação | Evidência |
|---:|---|---|
| 0–15 | definir unidade, tempo/espaço e pergunta | contrato |
| 15–30 | auditar cobertura, códigos e definições | diagnóstico |
| 30–48 | calcular denominador e visualização | código e figura |
| 48–60 | comparar recorte/janela/agregação | sensibilidade |
| 60–68 | inspecionar casos/fontes | notas qualitativas |
| 68–75 | redigir limites | conclusão |

### U11-A06 — Oficina — incremento cumulativo

Inclua no próprio projeto decisões, visualização autônoma, sensibilidade, casos e
limites. **Resposta:** no mesmo relatório-notebook.

### U11-A07 — Revisão por pares — reconstruir tempo e espaço

O colega identifica denominador, cobertura, ruptura/fronteira, caso e limite. Registra
um ponto claro, uma dúvida e uma mudança. **Dinâmica:** 20 minutos.

## Fechamento

Visualizar transformação exige declarar o que permaneceu comparável. A Unidade 12
testará modelos de linguagem sob o mesmo princípio de comparação controlada.''')]
def extras():
 nbs=(("Guia","00_guia_da_unidade.ipynb"),("Séries e taxas","01_datas_taxas_e_series.ipynb"),("Tendência e rupturas","02_tendencias_medias_moveis_e_rupturas.ipynb"),("Tempo textual","03_temas_e_palavras_no_tempo.ipynb"),("Espaço","04_distribuicao_espacial_e_taxas.ipynb"),("Oficina","05_oficina_tempo_ou_espaco.ipynb"))
 (U/"README.md").write_text(f"# Unidade 11 — Tempo e espaço\n\n{tabela_links_colab('unidade_11',nbs)}\n\nExecute a preparação nos notebooks 00–04. A oficina atualiza o mesmo relatório-notebook. Dados fictícios.\n",encoding="utf-8")
 (U/"referencias.md").write_text("""# Referências da Unidade 11

- HYNDMAN, Rob J.; ATHANASOPOULOS, George. *Forecasting: Principles and Practice*. 3. ed., 2021. Séries, tendências e médias móveis.
- CLIFF, Andrew D.; ORD, J. Keith. *Spatial Processes*. Pion, 1981. Dependência e análise espacial.
- OPENSHAW, Stan. The Modifiable Areal Unit Problem. Geo Books, 1984.
- ROBINSON, W. S. Ecological correlations and the behavior of individuals. *American Sociological Review*, 1950.
- MONMONIER, Mark. *How to Lie with Maps*. 3. ed. University of Chicago Press, 2018.
- GREGORY, Ian; GEDDES, Alistair. *Toward Spatial Humanities*. Indiana University Press, 2014.
""",encoding="utf-8")
 qs=["contagem e taxa respondem à mesma pergunta","taxa exige denominador","crescimento pode oscilar com base pequena","média móvel explica causa","janela altera suavização","ruptura de definição deve ser marcada","períodos são neutros","contagem lexical depende do corpus","normalização resolve mudança semântica","bordas da média móvel têm ausências","mapa coroplético deve mapear taxas comparáveis","contagem espacial reflete população","taxa pequena pode ser instável","padronização usa população de referência","falácia ecológica infere indivíduos de áreas","MAUP trata efeito das fronteiras","código territorial ajuda integração","mapa substitui casos","sensibilidade compara escolhas","não adoção é permitida"]
 linhas=["# U11-A08 — Exercícios de múltipla escolha",""]
 for i,q in enumerate(qs,1):linhas += [f"## Questão {i}",q.capitalize()+"?  ","A) Sempre.  B) Nunca.  C) Depende da medida, cobertura e unidade.  D) Apenas em mapas.",""]
 (U/"exercicios_unidade_11_texto.md").write_text("\n".join(linhas),encoding="utf-8")
 p=U/"gabaritos";p.mkdir(parents=True,exist_ok=True);ids=[("U11-A01","00_guia"),("U11-A02","01_series"),("U11-A03","02_tendencia"),("U11-A04","03_textos"),("U11-A05","04_espaco"),("U11-A06","05_oficina"),("U11-A07","05_oficina"),("U11-A08","exercicios")]
 (p/"README.md").write_text("# Gabaritos da Unidade 11\n\n"+"\n".join(f"- {i}: `gabarito_{a}.md`" for i,a in ids)+"\n",encoding="utf-8")
 tx={"00_guia":"A frase após 1990 mistura tendência, população e registro ampliado. Uma formulação defensável limita-se à série, explicita taxa e compara definições.","01_series":"Contagem cresce com população; taxa compara exposição; crescimento usa o ano anterior. O salto de 1990 não pode ser lido sem a mudança administrativa.","02_tendencia":"Janela 3 preserva oscilações; 9 suaviza e perde eventos locais. Apresente séries separadas por definição ou restrinja a um critério comum.","03_textos":"Menções por 100 documentos controlam volume, não gênero, OCR ou mudança semântica. Leia anos extremos e preserve explicações rivais.","04_espaco":"Um território pode liderar em contagem e cair em taxa por ter população maior. Não conclua sobre indivíduos e compare agregações alternativas.","05_oficina":"Exemplo: série de jornais por década, taxa por edições disponíveis, janela 5, ruptura de catalogação, inspeção de anos extremos e conclusão limitada ao acervo.","exercicios":"Exemplo da questão 15: uma correlação entre renda média territorial e equipamento não permite afirmar que indivíduos de maior renda frequentam mais; essa inferência é ecológica."}
 for a,t in tx.items():
  ais=[i for i,b in ids if b==a];(p/f"gabarito_{a}.md").write_text(f"# Gabarito — {a}\n\n**Atividades associadas:**\n"+"\n".join(f"- {i}" for i in ais)+f"\n\n## Exemplo de resolução\n\n{t}\n",encoding="utf-8")
 rv=U/"revisores";rv.mkdir(parents=True,exist_ok=True);(rv/"README.md").write_text("# Revisores da Unidade 11\n\nExecute seis pareceres.\n",encoding="utf-8")
 for i,t in enumerate(["nível acadêmico","didática","alinhamento","humanidades digitais","referências","técnica e acessibilidade"],1):(rv/f"{i:02d}_{t.replace(' ','_')}.md").write_text(f"# Revisor — {t}\n\nAvalie denominadores, comparabilidade, casos, mapas e correções verificáveis.\n",encoding="utf-8")
 (rv/"matriz_de_avaliacao.md").write_text("# Matriz\n\nAvalie tempo, espaço, sensibilidade, interpretação e integração.\n",encoding="utf-8");(rv/"modelo_de_parecer.md").write_text("# Parecer\n\n## Evidências\n\n## Correções\n",encoding="utf-8")
def main():
 for p in [U,D,U/"imagens"]:p.mkdir(parents=True,exist_ok=True)
 criar_dados();imgs=[("00_percurso_tempo_espaco.svg","Tempo e espaço construídos",["Unidades","Denominadores","Visualização","Limites"],"Comparabilidade antecede interpretação."),("01_taxas.svg","Contagem não é taxa",["Eventos","População","Taxa","Leitura"],"O denominador muda a pergunta."),("02_janelas.svg","Suavizar é escolher",["Série","Janela","Tendência","Ruptura"],"A curva não explica causas."),("03_tempo_textual.svg","Palavras no tempo",["Corpus","Contagem","Normalização","Casos"],"Vocabulário não equivale a conceito."),("04_mapa_critico.svg","Mapa e unidade",["Código","Taxa","Área","Crítica"],"Fronteiras condicionam padrões."),("05_entrega.svg","Evidência situada",["Pergunta","Figura","Sensibilidade","Limite"],"Um percurso pertinente basta.")]
 for x in imgs:svg(*x)
 salvar("00_guia_da_unidade.ipynb",guia());salvar("01_datas_taxas_e_series.ipynb",series());salvar("02_tendencias_medias_moveis_e_rupturas.ipynb",tendencia());salvar("03_temas_e_palavras_no_tempo.ipynb",textual());salvar("04_distribuicao_espacial_e_taxas.ipynb",espacial());salvar("05_oficina_tempo_ou_espaco.ipynb",oficina(),False);extras();(U/"imagens"/"README.md").write_text("# Ilustrações\n\nSVGs autorais e acessíveis.\n",encoding="utf-8");(R/"notes"/"plano_unidade_11.md").write_text("# Plano — Unidade 11\n\nPercorrer taxas, crescimento, tendência, rupturas, tempo textual, mapas, padronização, falácia ecológica e MAUP; incorporar um percurso ao projeto e validar.\n",encoding="utf-8")
if __name__=="__main__":main()
