"""Constrói a Unidade 13 — validade, robustez e vieses."""
from __future__ import annotations
import csv,json,random
from pathlib import Path
from textwrap import dedent
from apoio_colab import adicionar_link_na_abertura,preparacao_colab,tabela_links_colab
R=Path(__file__).resolve().parents[1];U=R/"unidade_13";D=U/"dados"
def md(s):return {"cell_type":"markdown","metadata":{},"source":dedent(s).strip().splitlines(keepends=True)}
def code(s):return {"cell_type":"code","execution_count":None,"metadata":{},"outputs":[],"source":dedent(s).strip().splitlines(keepends=True)}
def salvar(n,cs,d=True):
 o=[adicionar_link_na_abertura(cs[0],U.name,n)];o+=([code(preparacao_colab(U.name))] if d else []);o+=cs[1:]
 (U/n).write_text(json.dumps({"cells":o,"metadata":{"kernelspec":{"display_name":"Python 3","language":"python","name":"python3"},"language_info":{"name":"Python","version":"3"}},"nbformat":4,"nbformat_minor":5},ensure_ascii=False,indent=1)+"\n",encoding="utf-8")
def dados():
 D.mkdir(parents=True,exist_ok=True);rng=random.Random(20261026);linhas=[]
 for i in range(240):
  periodo="antigo" if i<120 else "recente";origem="Capital" if i%3 else "Interior";y=1 if i%2==0 else 0
  p=.80 if periodo=="recente" else .68
  if origem=="Interior":p-=.12
  prev=y if rng.random()<p else 1-y
  linhas.append([f"C{i+1:03d}",periodo,origem,y,prev,"claro" if i%7 else "ambíguo",round(.52+rng.random()*.46,3)])
 with (D/"predicoes_auditoria.csv").open("w",encoding="utf-8",newline="") as f:w=csv.writer(f);w.writerow(["id_caso","periodo","origem","classe_ouro","classe_prevista","tipo_caso","confianca"]);w.writerows(linhas)
 sens=[("especificação principal","TF-IDF 1–2 gramas",42,.742),("sem bigramas","TF-IDF unigramas",42,.721),("outra semente","TF-IDF 1–2 gramas",17,.713),("sem casos ambíguos","TF-IDF 1–2 gramas",42,.781),("teste temporal","treino antigo; teste recente",42,.648)]
 with (D/"analises_sensibilidade.csv").open("w",encoding="utf-8",newline="") as f:w=csv.writer(f);w.writerow(["analise","representacao","semente","f1"]);w.writerows(sens)
 casos=[("C001","trecho ambíguo com termo fora de contexto","falso positivo","operacionalização lexical"),("C008","grafia histórica não reconhecida","falso negativo","mudança linguística"),("C121","novo vocabulário institucional","falso negativo","mudança temporal"),("C180","metadado de origem incorreto","falso positivo","qualidade da base")]
 with (D/"casos_qualitativos.csv").open("w",encoding="utf-8",newline="") as f:w=csv.writer(f);w.writerow(["id_caso","descricao","erro","hipotese"]);w.writerows(casos)
 (D/"proveniencia.json").write_text(json.dumps({"natureza":"dados inteiramente fictícios","finalidade":"auditoria de validade, incerteza, robustez e viés","desenho":"desempenho menor no período antigo e no Interior foi inserido deliberadamente","limite":"não descreve grupos ou sistemas reais"},ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
def svg(n,t,es,r):
 w=190;gap=(920-len(es)*w)/max(1,len(es)-1);a=[]
 for i,e in enumerate(es):
  x=40+i*(w+gap);a.append(f'<rect x="{x:.0f}" y="82" width="{w}" height="112" rx="14" fill="#f4f0e6" stroke="#294c60" stroke-width="2"/><text x="{x+w/2:.0f}" y="140" text-anchor="middle" font-size="17">{e}</text>')
  if i<len(es)-1:a.append(f'<path d="M{x+w+5:.0f} 140 H{x+w+gap-8:.0f}" stroke="#a44a3f" stroke-width="3" marker-end="url(#a)"/>')
 (U/"imagens"/n).write_text(f'<svg xmlns="http://www.w3.org/2000/svg" width="1000" height="280" role="img" aria-labelledby="title desc"><title id="title">{t}</title><desc id="desc">{r}</desc><defs><marker id="a" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L0,6 L9,3 z" fill="#a44a3f"/></marker></defs><rect width="100%" height="100%" fill="#fffdf8"/><text x="500" y="40" text-anchor="middle" font-size="25" font-weight="bold">{t}</text>{"".join(a)}<text x="500" y="245" text-anchor="middle" font-size="16">{r}</text></svg>',encoding="utf-8")
def guia():return [md('''# Unidade 13 — Guia de estudo
## Como saber se os resultados são válidos?

Validade não é selo único. Perguntamos se a operacionalização representa o conceito,
se a análise sustenta a inferência, se ela se transporta para outros contextos e se as
evidências resistem a escolhas razoáveis.

![Pergunta, medida, análise, contexto e conclusão formam uma cadeia.](imagens/00_cadeia_validade.svg)'''),md('''## Vocabulário e percurso

- **validade de construto:** ligação entre conceito e medida;
- **validade interna:** alternativas à inferência dentro do estudo;
- **validade externa:** alcance para populações, tempos e contextos;
- **robustez:** estabilidade diante de escolhas defensáveis;
- **incerteza:** conjunto de valores/decisões ainda compatíveis com a evidência.

| Notebook | Foco | Produto |
|---|---|---|
| 00 | mapa de validade | cadeia de alegações |
| 01 | construto, interna e externa | auditoria por inferência |
| 02 | métricas, baseline e casos | avaliação mista |
| 03 | robustez e incerteza | análise de sensibilidade |
| 04 | amostra, corpus, algoritmo e contexto | auditoria de vieses |
| 05 | síntese | seção de ameaças à validade |'''),code('''import json,pandas as pd
p=pd.read_csv("dados/predicoes_auditoria.csv");s=pd.read_csv("dados/analises_sensibilidade.csv")
print(json.loads(open("dados/proveniencia.json",encoding="utf-8").read())["natureza"])
display(p.head(3));display(s)'''),md('''### U13-A01 — Discussão — localizar a ameaça

**Dinâmica (15 minutos):** para “o classificador mostra que o discurso cresceu”,
localize ameaças de construto, interna e externa e proponha evidência para cada uma.
**Resposta:** escreva aqui.

## Passagem

O diagnóstico começa na cadeia entre conceito, dados, método e afirmação — antes de
calcular outra métrica.''')]
def validades():return [md('''# Validade de construto, interna e externa

Uma medida pode ser reproduzível e ainda representar mal o conceito. Uma associação
pode ser correta na base e ainda admitir seleção, confundimento ou mudança documental.
Uma conclusão pode valer no corpus e falhar em outro período.

![Três perguntas de validade cercam a mesma conclusão.](imagens/01_tipos_validade.svg)'''),md('''## Matriz de auditoria preenchível

| Alegação | Construto | Interna | Externa | Evidência necessária |
|---|---|---|---|---|
| “Tema aumentou” | palavra mede tema? | cobertura mudou? | vale fora do acervo? | concordâncias, metadados e outro corpus |
| “Grupo difere” | categoria é coerente? | composição explica? | outros grupos/períodos? | casos, controles e replicação |

### U13-A02 — Atividade — cadeia de uma alegação

Escolha uma conclusão do projeto e preencha conceito, indicador, transformação,
resultado, inferência e três ameaças. **Dinâmica (30 minutos):** individual e revisão
em dupla; o colega tenta quebrar um elo. **Resposta:** escreva aqui.

## Passagem

O mapa indica o que avaliar. Agora combinaremos métricas com leitura manual, pois cada
uma enxerga erros diferentes.''')]
def avaliacao():return [md('''# Avaliação quantitativa e qualitativa

Uma linha de base dá escala ao desempenho. Métricas agregam; casos explicam mecanismos
de erro. A amostra manual deve incluir acertos, erros, confiança alta/baixa e grupos.

![Métrica, baseline, amostra e interpretação se complementam.](imagens/02_avaliacao_mista.svg)'''),code('''import pandas as pd
from sklearn.metrics import accuracy_score,precision_score,recall_score,f1_score,confusion_matrix
d=pd.read_csv("dados/predicoes_auditoria.csv");base=[d.classe_ouro.mode()[0]]*len(d)
def medir(y,p):return {"acurácia":accuracy_score(y,p),"precisão":precision_score(y,p,zero_division=0),"revocação":recall_score(y,p,zero_division=0),"F1":f1_score(y,p,zero_division=0)}
resultado=pd.DataFrame([{"método":"maioria",**medir(d.classe_ouro,base)},{"método":"modelo",**medir(d.classe_ouro,d.classe_prevista)}]).set_index("método")
display(resultado.round(3));display(pd.DataFrame(confusion_matrix(d.classe_ouro,d.classe_prevista),index=["ouro 0","ouro 1"],columns=["prev 0","prev 1"]))'''),code('''casos=pd.read_csv("dados/casos_qualitativos.csv");amostra=d[(d.classe_ouro!=d.classe_prevista)|d.id_caso.isin(casos.id_caso)].merge(casos,on="id_caso",how="left")
display(amostra.head(12))'''),md('''### U13-A03 — Atividade — amostra que desafia a média

Compare modelo e baseline; monte amostra estratificada de 12 casos; agrupe erros por
hipótese e diga qual correção mudaria o estudo. **Dinâmica (30 minutos):** trio com
analista, leitor e crítico. **Resposta:** escreva aqui.

## Passagem

Mesmo avaliação bem desenhada depende de sementes, representação e inclusão de casos.
Sensibilidade torna essa dependência visível.''')]
def robustez():return [md('''# Robustez, incerteza e resultados inconclusivos

Análise de sensibilidade varia decisões plausíveis uma por vez ou em combinações
justificadas. Robustez não significa resultado idêntico: pergunta se a conclusão muda
em direção, magnitude ou decisão.

![Especificações alternativas produzem uma faixa de resultados.](imagens/03_robustez.svg)'''),code('''import numpy as np,pandas as pd,matplotlib.pyplot as plt
s=pd.read_csv("dados/analises_sensibilidade.csv")
display(s.sort_values("f1"));s.plot.barh(x="analise",y="f1",legend=False,xlim=(0,1));plt.xlabel("F1");plt.title("Sensibilidade das especificações — dados fictícios");plt.tight_layout();plt.show()
d=pd.read_csv("dados/predicoes_auditoria.csv");rng=np.random.default_rng(42);boots=[]
for _ in range(1000):
 a=d.sample(len(d),replace=True,random_state=int(rng.integers(1_000_000)));boots.append((a.classe_ouro==a.classe_prevista).mean())
intervalo_bootstrap=np.quantile(boots,[.025,.975]);print("IC bootstrap descritivo da acurácia:",intervalo_bootstrap.round(3))'''),md('''O intervalo resume reamostragem dos casos observados; não corrige viés de seleção. O
teste temporal baixo questiona generalização. Resultado negativo ou inconclusivo deve
ser relatado quando a direção muda, a faixa é ampla ou o desenho não discrimina hipóteses.

### U13-A04 — Atividade — o que permanece?

Ordene especificações, defina previamente um limiar decisório, interprete o intervalo
e escreva conclusão robusta e conclusão que seria forte demais. **Dinâmica (30
minutos):** duplas com posições favorável e cética. **Resposta:** escreva aqui.

## Passagem

Sensibilidade global ainda pode ocultar quem foi mal representado. A seguir separamos
amostra, corpus, algoritmo e mudança de contexto.''')]
def vieses():return [md('''# Viés de amostra, corpus, algoritmo e contexto

Viés é desvio sistemático ligado a como casos entram, são representados e recebem
decisões. Diferença de desempenho é sinal para investigação, não diagnóstico automático
de causa nem medida completa de justiça.

![Seleção, representação, algoritmo e uso formam uma cadeia de vieses.](imagens/04_vieses.svg)'''),code('''import pandas as pd
from sklearn.metrics import accuracy_score,precision_score,recall_score,f1_score
d=pd.read_csv("dados/predicoes_auditoria.csv")
def medir(g):return pd.Series({"n":len(g),"acurácia":accuracy_score(g.classe_ouro,g.classe_prevista),"F1":f1_score(g.classe_ouro,g.classe_prevista)})
por_periodo=d.groupby("periodo").apply(medir,include_groups=False);por_origem=d.groupby("origem").apply(medir,include_groups=False)
display(por_periodo.round(3));display(por_origem.round(3))'''),md('''## Mudança entre períodos e contextos

Queda no período antigo pode refletir grafia, OCR, gêneros ou anotação. Queda no
Interior pode refletir menor cobertura ou diferença substantiva. Audite composição,
qualidade e erros antes de atribuir o problema ao grupo.

### U13-A05 — Atividade — diferença, mecanismo e mitigação

Escolha uma lacuna, quantifique-a, leia casos e proponha três mecanismos rivais. Para
cada mecanismo, defina teste e mitigação. **Dinâmica (35 minutos):** grupos de três
devem preservar ao menos duas explicações. **Resposta:** escreva aqui.

## Passagem

A oficina reunirá todas as ameaças numa seção priorizada, sem transformar a lista de
limitações em ritual genérico.''')]
def oficina():return [md('''# Oficina — validade, limitações e ameaças

**Produto:** seção no mesmo relatório-notebook. Ela deve alterar o alcance das
conclusões e propor verificações; não é uma lista genérica no final.

![Alegação, ameaça, evidência, impacto e ação estruturam a entrega.](imagens/05_entrega.svg)'''),md('''## Roteiro de 75 minutos

| Tempo | Ação | Evidência |
|---:|---|---|
| 0–12 | selecionar três alegações | mapa |
| 12–27 | auditar construto/interna/externa | matriz |
| 27–42 | comparar baseline, métricas e casos | avaliação mista |
| 42–55 | testar duas especificações | sensibilidade |
| 55–65 | examinar período/grupo | auditoria de viés |
| 65–75 | priorizar e reescrever conclusões | seção final |

### U13-A06 — Oficina — incremento cumulativo

Para cada ameaça, registre evidência, probabilidade, impacto, ação e efeito na
conclusão. **Resposta:** no mesmo relatório-notebook.

### U13-A07 — Revisão por pares — testar a conclusão

O colega escolhe a alegação mais forte e procura elo frágil, especificação alternativa
e grupo/contexto omitido. Registra ponto claro, dúvida e mudança. **Dinâmica:** 20 min.

## Fechamento

Validade é propriedade do argumento apoiado por evidências. A Unidade 14 organizará
essa cadeia numa versão reprodutível, compartilhável e comunicável.''')]
def extras():
 nbs=(("Guia","00_guia_da_unidade.ipynb"),("Tipos de validade","01_validade_de_construto_interna_e_externa.ipynb"),("Avaliação mista","02_avaliacao_quantitativa_e_qualitativa.ipynb"),("Robustez","03_robustez_incerteza_e_sensibilidade.ipynb"),("Vieses","04_vieses_e_mudanca_de_contexto.ipynb"),("Oficina","05_oficina_validade_e_limitacoes.ipynb"))
 (U/"README.md").write_text(f"# Unidade 13 — Validade, robustez e vieses\n\n{tabela_links_colab('unidade_13',nbs)}\n\nExecute a preparação nos notebooks 00 e 02–04. O Notebook 01 e a oficina são discursivos. A entrega atualiza o mesmo relatório.\n",encoding="utf-8")
 (U/"referencias.md").write_text("""# Referências da Unidade 13

- SHADISH, William R.; COOK, Thomas D.; CAMPBELL, Donald T. *Experimental and Quasi-Experimental Designs for Generalized Causal Inference*. 2002.
- MESSICK, Samuel. Validity of psychological assessment. *American Psychologist*, 1995.
- SALGANIK, Matthew J. *Bit by Bit*. Princeton University Press, 2018.
- GRIMMER, Justin; STEWART, Brandon M. Text as Data. *Political Analysis*, 2013.
- SURESH, Harini; GUTTAG, John. A Framework for Understanding Sources of Harm throughout the Machine Learning Life Cycle. EAAMO, 2021.
- SIMMONS, Joseph P.; NELSON, Leif D.; SIMONSOHN, Uri. False-positive psychology. *Psychological Science*, 2011.
""",encoding="utf-8")
 qs=["validade é selo único","construto liga conceito e medida","validade interna examina alternativas","externa trata alcance","métrica alta garante construto","baseline dá escala","casos explicam mecanismos","amostra manual deve incluir erros","robustez exige resultado idêntico","sensibilidade varia escolhas plausíveis","bootstrap corrige seleção","inconclusivo deve ser relatado","diferença por grupo prova causa","n deve acompanhar métricas","mudança temporal afeta generalização","viés pode entrar na seleção","algoritmo é única fonte de viés","limite deve alterar conclusão","resultado negativo é falha","ameaça deve ter ação"]
 linhas=["# U13-A08 — Exercícios de múltipla escolha",""]
 for i,q in enumerate(qs,1):linhas += [f"## Questão {i}",q.capitalize()+"?  ","A) Sempre.  B) Não necessariamente; depende da alegação e evidência.  C) Apenas com IA.  D) Apenas sem amostra.",""]
 (U/"exercicios_unidade_13_texto.md").write_text("\n".join(linhas),encoding="utf-8")
 p=U/"gabaritos";p.mkdir(parents=True,exist_ok=True);ids=[("U13-A01","00_guia"),("U13-A02","01_validade"),("U13-A03","02_avaliacao"),("U13-A04","03_robustez"),("U13-A05","04_vieses"),("U13-A06","05_oficina"),("U13-A07","05_oficina"),("U13-A08","exercicios")]
 (p/"README.md").write_text("# Gabaritos da Unidade 13\n\n"+"\n".join(f"- {i}: `gabarito_{a}.md`" for i,a in ids)+"\n",encoding="utf-8")
 tx={"00_guia":"‘Discurso’ pode não ser capturado por palavra; cobertura pode mudar; o corpus pode não representar outros jornais. Testes: concordâncias, metadados e replicação.","01_validade":"Alegação: tema aumentou. Indicador: proporção classificada. Ameaças: deriva do conceito, mudança de OCR e alcance restrito. Cada ameaça recebe evidência e revisão da frase.","02_avaliacao":"Compare baseline e modelo, mas leia falsos positivos/negativos por período, origem, ambiguidade e confiança. A correção deve responder a mecanismo, não só elevar média.","03_robustez":"O teste temporal é a maior queda e limita generalização. Bootstrap quantifica variação amostral observada, não seleção. Conclusão forte demais ignora a faixa das especificações.","04_vieses":"A lacuna por origem pode vir de cobertura, linguagem ou anotação. Teste composição e erros; mitigação pode exigir novas fontes, rótulos e avaliação, não apenas ajuste do algoritmo.","05_oficina":"Exemplo: três alegações, matriz de validade, baseline, 20 erros lidos, análise temporal e duas especificações. A conclusão é reduzida ao corpus e duas verificações futuras são priorizadas.","exercicios":"Exemplo da questão 11: bootstrap reamostra os casos presentes; se o corpus excluiu um grupo, nenhuma reamostragem o recupera."}
 for a,t in tx.items():
  ais=[i for i,b in ids if b==a];(p/f"gabarito_{a}.md").write_text(f"# Gabarito — {a}\n\n**Atividades associadas:**\n"+"\n".join(f"- {i}" for i in ais)+f"\n\n## Exemplo de resolução\n\n{t}\n",encoding="utf-8")
 rv=U/"revisores";rv.mkdir(parents=True,exist_ok=True);(rv/"README.md").write_text("# Revisores da Unidade 13\n\nExecute seis pareceres.\n",encoding="utf-8")
 for i,t in enumerate(["nível acadêmico","didática","alinhamento","humanidades digitais","referências","técnica e acessibilidade"],1):(rv/f"{i:02d}_{t.replace(' ','_')}.md").write_text(f"# Revisor — {t}\n\nAvalie validade, robustez, vieses, casos e correções verificáveis.\n",encoding="utf-8")
 (rv/"matriz_de_avaliacao.md").write_text("# Matriz\n\nAvalie alegações, ameaças, evidências, impacto e ação.\n",encoding="utf-8");(rv/"modelo_de_parecer.md").write_text("# Parecer\n\n## Evidências\n\n## Correções\n",encoding="utf-8")
def main():
 for p in [U,D,U/"imagens"]:p.mkdir(parents=True,exist_ok=True)
 dados();imgs=[("00_cadeia_validade.svg","Validade da cadeia",["Conceito","Dados","Método","Alegação"],"Cada elo pode limitar a conclusão."),("01_tipos_validade.svg","Três perguntas",["Construto","Interna","Externa","Evidência"],"Validade depende da inferência."),("02_avaliacao_mista.svg","Métricas e casos",["Baseline","Métricas","Erros","Mecanismos"],"Agregados e leitura se complementam."),("03_robustez.svg","Resultados em faixa",["Escolhas","Especificações","Incerteza","Decisão"],"Robustez não é identidade."),("04_vieses.svg","Cadeia de vieses",["Seleção","Representação","Algoritmo","Uso"],"Dano pode entrar em várias etapas."),("05_entrega.svg","Ameaça acionável",["Alegação","Ameaça","Impacto","Ação"],"Limites reescrevem conclusões.")]
 for x in imgs:svg(*x)
 salvar("00_guia_da_unidade.ipynb",guia());salvar("01_validade_de_construto_interna_e_externa.ipynb",validades(),False);salvar("02_avaliacao_quantitativa_e_qualitativa.ipynb",avaliacao());salvar("03_robustez_incerteza_e_sensibilidade.ipynb",robustez());salvar("04_vieses_e_mudanca_de_contexto.ipynb",vieses());salvar("05_oficina_validade_e_limitacoes.ipynb",oficina(),False);extras();(U/"imagens"/"README.md").write_text("# Ilustrações\n\nSVGs autorais e acessíveis.\n",encoding="utf-8");(R/"notes"/"plano_unidade_13.md").write_text("# Plano — Unidade 13\n\nAuditar validade de construto, interna e externa; combinar baseline, métricas e casos; testar robustez, incerteza, generalização e vieses; incorporar ameaças e ações ao relatório.\n",encoding="utf-8")
if __name__=="__main__":main()
