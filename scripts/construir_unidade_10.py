"""Constrói a Unidade 10 — extração estruturada de textos."""
from __future__ import annotations
import csv,json,re
from pathlib import Path
from textwrap import dedent
from apoio_colab import adicionar_link_na_abertura,preparacao_colab,tabela_links_colab
RAIZ=Path(__file__).resolve().parents[1]; U=RAIZ/"unidade_10"; D=U/"dados"
def md(s): return {"cell_type":"markdown","metadata":{},"source":dedent(s).strip().splitlines(keepends=True)}
def code(s): return {"cell_type":"code","execution_count":None,"metadata":{},"outputs":[],"source":dedent(s).strip().splitlines(keepends=True)}
def salvar(nome,cs,dados=True):
    out=[adicionar_link_na_abertura(cs[0],U.name,nome)]; out+=([code(preparacao_colab(U.name))] if dados else []); out+=cs[1:]
    (U/nome).write_text(json.dumps({"cells":out,"metadata":{"kernelspec":{"display_name":"Python 3","language":"python","name":"python3"},"language_info":{"name":"python","version":"3"}},"nbformat":4,"nbformat_minor":5},ensure_ascii=False,indent=1)+"\n",encoding="utf-8")
def dados():
    D.mkdir(parents=True,exist_ok=True)
    textos=[
    ("D001",1901,"Gazeta Aurora","Em 12 de março de 1901, Ana Ferreira fundou a Liga Aurora em Porto Claro."),
    ("D002",1902,"Gazeta Aurora","A Liga Aurora inaugurou a Escola Livre em Porto Claro, dirigida por Bento Reis."),
    ("D003",1903,"Correio do Norte","Bento Reis escreveu a Ana Ferreira sobre a Escola Livre em 4 de maio de 1903."),
    ("D004",1904,"Jornal Horizonte","A médica Ana Ferreira visitou o Hospital Central de Santa Rita."),
    ("D005",1905,"Jornal Horizonte","A Associação Aurora promoveu conferência no Teatro União em Santa Rita."),
    ("D006",1906,"Correio do Norte","O professor Caio Martins assumiu a Escola Livre de Porto Claro."),
    ("D007",1907,"Gazeta Aurora","Ana F. participou da reunião da Liga Aurora no Teatro União."),
    ("D008",1908,"Jornal Horizonte","O vapor Santa Rita chegou a Porto Claro; não se trata da cidade homônima."),
    ("D009",1909,"Correio do Norte","Dora Silva deixou a Biblioteca Popular e ingressou na Liga Aurora."),
    ("D010",1910,"Gazeta Aurora","A Liga Aurora realizou campanha com o Hospital Central em Porto Claro."),
    ("D011",1911,"Jornal Horizonte","Caio Martins falou com Dora Silva na Biblioteca Popular."),
    ("D012",1912,"Correio do Norte","Em 7 de julho de 1912, a Escola Livre contratou Eva Lima."),]
    with (D/"documentos.csv").open("w",encoding="utf-8",newline="") as f: w=csv.writer(f);w.writerow(["id_documento","ano","fonte","texto"]);w.writerows(textos)
    autoridade=[("P001","Ana Ferreira","PESSOA","Ana F.;Dra. Ana Ferreira"),("P002","Bento Reis","PESSOA","Bento R."),("P003","Caio Martins","PESSOA","Caio M."),("P004","Dora Silva","PESSOA","Dora S."),("P005","Eva Lima","PESSOA","Eva L."),("O001","Liga Aurora","ORGANIZACAO","Associação Aurora"),("O002","Escola Livre","ORGANIZACAO",""),("O003","Hospital Central","ORGANIZACAO",""),("O004","Teatro União","ORGANIZACAO",""),("O005","Biblioteca Popular","ORGANIZACAO",""),("L001","Porto Claro","LUGAR",""),("L002","Santa Rita","LUGAR","cidade de Santa Rita")]
    with (D/"autoridades.csv").open("w",encoding="utf-8",newline="") as f: w=csv.writer(f);w.writerow(["id_entidade","nome_canonico","tipo","variantes"]);w.writerows(autoridade)
    ouro=[("D001","Ana Ferreira","P001","PESSOA"),("D001","Liga Aurora","O001","ORGANIZACAO"),("D001","Porto Claro","L001","LUGAR"),("D002","Liga Aurora","O001","ORGANIZACAO"),("D002","Escola Livre","O002","ORGANIZACAO"),("D002","Porto Claro","L001","LUGAR"),("D002","Bento Reis","P002","PESSOA"),("D007","Ana F.","P001","PESSOA"),("D007","Liga Aurora","O001","ORGANIZACAO"),("D007","Teatro União","O004","ORGANIZACAO"),("D008","Santa Rita","","OUTRO"),("D008","Porto Claro","L001","LUGAR")]
    with (D/"anotacao_ouro.csv").open("w",encoding="utf-8",newline="") as f: w=csv.writer(f);w.writerow(["id_documento","mencao","id_entidade","tipo"]);w.writerows(ouro)
    (D/"proveniencia.json").write_text(json.dumps({"natureza":"dados inteiramente fictícios","finalidade":"NER, vinculação, relações e eventos","ambiguidade":"Santa Rita é cidade em D004/D005 e nome de embarcação em D008","limite":"não sustenta afirmações históricas reais"},ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
def svg(nome,titulo,etapas,rodape):
    n=len(etapas);w=190;gap=(920-n*w)/max(1,n-1);a=[]
    for i,e in enumerate(etapas):
        x=40+i*(w+gap);a.append(f'<rect x="{x:.0f}" y="82" width="{w}" height="112" rx="14" fill="#f4f0e6" stroke="#294c60" stroke-width="2"/><text x="{x+w/2:.0f}" y="140" text-anchor="middle" font-size="17">{e}</text>')
        if i<n-1:a.append(f'<path d="M{x+w+5:.0f} 140 H{x+w+gap-8:.0f}" stroke="#a44a3f" stroke-width="3" marker-end="url(#a)"/>')
    (U/"imagens"/nome).write_text(f'<svg xmlns="http://www.w3.org/2000/svg" width="1000" height="280" role="img" aria-labelledby="title desc"><title id="title">{titulo}</title><desc id="desc">{rodape}</desc><defs><marker id="a" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L0,6 L9,3 z" fill="#a44a3f"/></marker></defs><rect width="100%" height="100%" fill="#fffdf8"/><text x="500" y="40" text-anchor="middle" font-size="25" font-weight="bold">{titulo}</text>{"".join(a)}<text x="500" y="245" text-anchor="middle" font-size="16">{rodape}</text></svg>',encoding="utf-8")
def guia():return [md('''# Unidade 10 — Guia de estudo
## Como transformar textos em informações estruturadas?

Extração identifica menções e propõe registros; não converte linguagem em fatos sem
mediação. Distinguiremos **menção** (forma no texto), **entidade** (referente
hipotético) e **registro** (representação criada pela pesquisa).

![Percurso do texto à validação.](imagens/00_percurso_extracao.svg)'''),md('''## Percurso

| Notebook | Problema | Produto |
|---|---|---|
| 00 | O que está sendo extraído? | contrato de representação |
| 01 | Como localizar pessoas, organizações, lugares e datas? | menções por regras/dicionário |
| 02 | Duas formas referem-se à mesma entidade? | vinculação auditável |
| 03 | Como representar ações e vínculos? | tabelas de relações e eventos |
| 04 | Como medir e corrigir erros? | avaliação e rede derivada |
| 05 | O método serve ao projeto? | incremento ou não adoção |'''),code('''import json,pandas as pd
documentos=pd.read_csv("dados/documentos.csv"); autoridades=pd.read_csv("dados/autoridades.csv")
print(json.loads(open("dados/proveniencia.json",encoding="utf-8").read())["natureza"])
display(documentos.head(3));display(autoridades.head(3))'''),md('''### U10-A01 — Discussão — menção, entidade ou fato?

**Dinâmica (15 minutos):** classifique “Ana F.”, P001 e “Ana fundou a Liga” como
menção, entidade ou afirmação extraída. Diga que evidência e incerteza cada registro
deve preservar. **Resposta:** escreva aqui.

## Passagem

Com as camadas separadas, começaremos pela tarefa mais local: localizar sequências que
podem ser nomes ou datas, preservando documento e forma original.''')]
def ner():return [md('''# Reconhecimento de entidades nomeadas

NER localiza e tipifica menções. Regras são transparentes e frágeis; dicionários têm
alta precisão no domínio conhecido e baixa cobertura de novidades; modelos aprendem
padrões, mas exigem dados e avaliação. Aqui combinaremos regex e autoridade local.

![Regras, dicionários e modelos oferecem coberturas distintas.](imagens/01_metodos_ner.svg)'''),code('''import re,pandas as pd
docs=pd.read_csv("dados/documentos.csv"); aut=pd.read_csv("dados/autoridades.csv").fillna("")
mapa={}
for _,r in aut.iterrows():
    for forma in [r.nome_canonico,*[x for x in r.variantes.split(";") if x]]: mapa[forma]=(r.id_entidade,r.tipo,r.nome_canonico)
padrao=re.compile("|".join(sorted(map(re.escape,mapa),key=len,reverse=True)))
extracoes=[]
for _,d in docs.iterrows():
    for m in padrao.finditer(d.texto):
        ident,tipo,canon=mapa[m.group()];extracoes.append([d.id_documento,m.group(),m.start(),m.end(),ident,tipo,canon,"dicionário"])
    for m in re.finditer(r"\\b\\d{1,2} de [a-zç]+ de \\d{4}\\b",d.texto.lower()): extracoes.append([d.id_documento,d.texto[m.start():m.end()],m.start(),m.end(),"","DATA","","regex"])
entidades=pd.DataFrame(extracoes,columns=["id_documento","mencao","inicio","fim","id_entidade","tipo","nome_canonico","metodo"])
display(entidades.head(12));display(entidades.tipo.value_counts())'''),md('''A posição inicial/final torna a extração rastreável. O dicionário não encontra nomes
novos; a regex de data não compreende calendários, apenas padrões. Um modelo treinado
poderia ampliar cobertura, mas seus erros continuariam exigindo amostra anotada.

### U10-A02 — Atividade integrada — cobertura e falsos positivos

Leia todos os documentos, marque uma menção perdida e um possível falso positivo,
proponha regra ou entrada de dicionário e explique o novo erro que ela pode criar.
**Dinâmica (25 minutos):** duplas, uma amplia cobertura e outra tenta quebrar a regra.
**Resposta:** escreva aqui.

## Passagem

Localizar “Ana F.” ainda não informa se é Ana Ferreira. O notebook seguinte separa
normalização gráfica de vinculação a um referente.''')]
def vinculo():return [md('''# Desambiguação e vinculação de entidades

Normalizar reduz variação de escrita; vincular atribui um identificador; desambiguar
decide entre referentes possíveis. Um catálogo de autoridade deve preservar variantes,
fonte da decisão e opção **não resolvido**.

![Menções variantes convergem para um identificador, enquanto homônimos exigem contexto.](imagens/02_vinculacao.svg)'''),code('''import pandas as pd,re,unicodedata
docs=pd.read_csv("dados/documentos.csv");aut=pd.read_csv("dados/autoridades.csv").fillna("")
def normalizar(s):
    s=unicodedata.normalize("NFKD",s);return re.sub(r"[^a-z0-9 ]","",s.encode("ascii","ignore").decode().lower()).strip()
indice={}
for _,r in aut.iterrows():
    for f in [r.nome_canonico,*[x for x in r.variantes.split(";") if x]]: indice[normalizar(f)]=r.id_entidade
teste=pd.DataFrame({"mencao":["Ana F.","Dra. Ana Ferreira","Associação Aurora","Santa Rita" ]})
teste["forma_normalizada"]=teste.mencao.map(normalizar);teste["id_proposto"]=teste.forma_normalizada.map(indice)
display(teste)'''),md('''“Santa Rita” demonstra por que igualdade textual não basta: em D008 é embarcação; em
outros documentos, lugar. O contexto e o tipo esperado devem poder bloquear a ligação.

### U10-A03 — Atividade — ficha de vinculação

Para quatro menções, registre forma, candidato, contexto, evidência, decisão e grau de
confiança. Inclua D008 como `não vincular a L002`. **Dinâmica (25 minutos):** decisão
individual e adjudicação em trio. **Resposta:** escreva aqui.

## Passagem

Entidades vinculadas permitem representar ações, mas proximidade na frase não prova
relação. A próxima etapa explicita sujeito, predicado, objeto, tempo e evidência.''')]
def relacoes():return [md('''# Relações, eventos e tabelas derivadas

Uma relação é um vínculo relativamente estável; um evento é uma ocorrência situada.
Representaremos ambos como alegações rastreáveis, não fatos descontextualizados.

![Uma frase origina participantes, ação, tempo e evidência.](imagens/03_evento.svg)'''),code('''import pandas as pd,re
docs=pd.read_csv("dados/documentos.csv")
regras=[("fundou",r"(?P<sujeito>Ana Ferreira) fundou a (?P<objeto>Liga Aurora)","fundacao"),("inaugurou",r"(?P<sujeito>Liga Aurora) inaugurou a (?P<objeto>Escola Livre)","inauguracao"),("ingressou",r"(?P<sujeito>Dora Silva).* ingressou na (?P<objeto>Liga Aurora)","ingresso"),("contratou",r"(?P<sujeito>Escola Livre) contratou (?P<objeto>Eva Lima)","contratacao")]
linhas=[]
for _,d in docs.iterrows():
    for nome,padrao,tipo in regras:
        m=re.search(padrao,d.texto)
        if m: linhas.append([d.id_documento,tipo,m["sujeito"],m["objeto"],d.ano,m.group(),"regra"])
eventos=pd.DataFrame(linhas,columns=["id_documento","tipo_evento","participante_1","participante_2","ano","evidencia_textual","metodo"])
display(eventos)'''),md('''## Esquema mínimo

Cada linha preserva documento, tipo, participantes, tempo, trecho e método. Relações
negadas, hipotéticas ou citadas exigiriam atributos próprios; não devem entrar como
afirmações positivas.

### U10-A04 — Atividade — do trecho ao registro

Modele D003, D009 e D010. Para cada um, escolha relação/evento, papéis, tempo,
evidência e incerteza. Compare sua tabela à regra automática e explique uma perda.
**Dinâmica (30 minutos):** grupos de três; modelador, crítico e documentador.
**Resposta:** escreva aqui.

## Passagem

Uma tabela legível pode ainda estar errada. Avaliaremos menções contra uma pequena
anotação de referência e mostraremos como extrações validadas podem formar uma rede.''')]
def avaliacao():return [md('''# Avaliação, validação humana e rede derivada

Precisão mede a parcela das extrações corretas; revocação, a parcela das menções de
referência encontradas; F1 combina ambas. A correspondência deve usar documento,
limites, tipo e, quando pertinente, identidade.

![Predições são comparadas ao ouro e os erros retornam ao texto.](imagens/04_avaliacao.svg)'''),code('''import pandas as pd,re
docs=pd.read_csv("dados/documentos.csv");aut=pd.read_csv("dados/autoridades.csv").fillna("");ouro=pd.read_csv("dados/anotacao_ouro.csv").fillna("")
formas=[]
for _,r in aut.iterrows():
    for f in [r.nome_canonico,*[x for x in r.variantes.split(";") if x]]: formas.append((f,r.id_entidade,r.tipo))
pred=[]
for _,d in docs[docs.id_documento.isin(ouro.id_documento.unique())].iterrows():
    for f,i,t in formas:
        if f in d.texto: pred.append((d.id_documento,f,i,t))
P=set(pred);G=set(map(tuple,ouro[["id_documento","mencao","id_entidade","tipo"]].to_records(index=False)))
vp=len(P&G);precisao=vp/len(P);revocacao=vp/len(G);f1=2*precisao*revocacao/(precisao+revocacao)
print(f"Precisão={precisao:.3f} | Revocação={revocacao:.3f} | F1={f1:.3f}")
print("Falsos positivos:",P-G);print("Falsos negativos:",G-P)'''),code('''# Rede somente com relações já validadas no exemplo
eventos=pd.DataFrame([["Ana Ferreira","Liga Aurora","fundacao"],["Liga Aurora","Escola Livre","inauguracao"],["Dora Silva","Liga Aurora","ingresso"],["Escola Livre","Eva Lima","contratacao"]],columns=["origem","destino","relacao"])
arestas=eventos.groupby(["origem","destino"]).size().reset_index(name="peso")
display(arestas)'''),md('''Uma rede herda todos os erros de reconhecimento, vinculação e relação. Centralidade não
corrige extrações ruins; por isso, mantenha ligação aos documentos e uma amostra humana.

### U10-A05 — Atividade — erro em cascata

Explique um falso positivo, um falso negativo e como cada um alteraria a rede. Proponha
uma correção e reavalie a mesma amostra. **Dinâmica (30 minutos):** duplas produzem uma
linha de auditoria por erro. **Resposta:** escreva aqui.

## Passagem

A oficina reúne esquema, extração, avaliação e retorno às fontes no projeto cumulativo.''')]
def oficina():return [md('''# Oficina — base estruturada derivada de textos

**Produto:** seção no mesmo relatório-notebook, não arquivo separado. Inclua esquema,
extração, validação e exemplos ligados às fontes, ou justifique a não adoção.

![A entrega liga texto, tabela, avaliação e interpretação.](imagens/05_entrega.svg)'''),md('''## Roteiro de 75 minutos

| Tempo | Ação | Evidência |
|---:|---|---|
| 0–15 | definir entidade/relação/evento | esquema |
| 15–30 | criar amostra anotada | ouro local |
| 30–48 | extrair e vincular | tabela rastreável |
| 48–60 | calcular e ler erros | métricas e casos |
| 60–68 | revisar regras | comparação antes/depois |
| 68–75 | integrar limites | conclusão |

### U10-A06 — Oficina — incremento do relatório-notebook

Trabalhe no próprio corpus; preserve texto original, identificadores, método e incerteza.
**Resposta:** inclua no mesmo relatório-notebook.

### U10-A07 — Revisão por pares — rastrear até a fonte

O colega escolhe três linhas e tenta chegar ao trecho original, questiona uma ligação e
um evento e propõe correção. Anexe parecer e decisão. **Dinâmica:** 20 minutos.

## Fechamento

Extração responsável produz alegações verificáveis. A Unidade 11 usará registros
temporais e espaciais sem esquecer como foram construídos.''')]
def materiais():
    nbs=(("Guia","00_guia_da_unidade.ipynb"),("NER","01_reconhecimento_de_entidades.ipynb"),("Vinculação","02_desambiguacao_e_vinculacao.ipynb"),("Relações e eventos","03_relacoes_eventos_e_tabelas.ipynb"),("Avaliação","04_avaliacao_validacao_e_rede.ipynb"),("Oficina","05_oficina_base_derivada_de_textos.ipynb"))
    (U/"README.md").write_text(f"# Unidade 10 — Extração estruturada de textos\n\n{tabela_links_colab('unidade_10',nbs)}\n\nExecute a preparação nos notebooks 00–04. A oficina atualiza o mesmo relatório-notebook. Dados inteiramente fictícios.\n",encoding="utf-8")
    (U/"referencias.md").write_text("""# Referências da Unidade 10

- JURAFSKY, Daniel; MARTIN, James H. *Speech and Language Processing*. 3. ed., rascunho. Capítulos de NER e extração de relações.
- EHRMANN, Maud et al. Named Entity Recognition and Classification in Historical Documents: A Survey. *ACM Computing Surveys*, 2023.
- VAN HOOLAND, Seth; VERBORGH, Ruben. *Linked Data for Libraries, Archives and Museums*. Facet, 2014.
- BRUNNER, Annelen; ENGEL, Juliane. Linking historical entities: entity linking in cultural heritage. Referência para desambiguação e autoridade.
- HOGAN, Aidan et al. Knowledge Graphs. *ACM Computing Surveys*, 2021. DOI: 10.1145/3447772.

As referências sustentam conceitos; os exemplos são sintéticos e baseados em regras transparentes.
""",encoding="utf-8")
    qs=["menção e entidade são iguais","dicionário reconhece novidades automaticamente","regex compreende significado","posição no texto favorece rastreabilidade","normalização prova identidade","identificador canônico reúne variantes","homônimo exige contexto","não resolvido é decisão válida","relação é sempre coocorrência","evento deve preservar tempo","negação exige tratamento","tabela deve guardar evidência","precisão usa extrações previstas","revocação usa menções de referência","F1 combina precisão e revocação","ouro é infalível","erro de NER pode afetar rede","centralidade corrige extração","validação humana permanece necessária","não adoção pode ser correta"]
    linhas=["# U10-A08 — Exercícios de múltipla escolha",""]
    for i,q in enumerate(qs,1): linhas += [f"## Questão {i}",q.capitalize()+"?  ","A) Sim, sempre.  B) Não necessariamente; depende da definição e do contexto.  C) Apenas com gráfico.  D) Apenas sem fontes.",""]
    (U/"exercicios_unidade_10_texto.md").write_text("\n".join(linhas),encoding="utf-8")
def gabs():
    p=U/"gabaritos";p.mkdir(parents=True,exist_ok=True)
    ids=[("U10-A01","00_guia"),("U10-A02","01_ner"),("U10-A03","02_vinculacao"),("U10-A04","03_relacoes"),("U10-A05","04_avaliacao"),("U10-A06","05_oficina"),("U10-A07","05_oficina"),("U10-A08","exercicios_multipla_escolha")]
    (p/"README.md").write_text("# Gabaritos da Unidade 10\n\n"+"\n".join(f"- {i}: `gabarito_{a}.md`" for i,a in ids)+"\n",encoding="utf-8")
    textos={"00_guia":"Menção é a cadeia ‘Ana F.’; P001 é a entidade proposta; ‘fundou’ é uma alegação que exige trecho e documento. Não se deve colapsar as três camadas.","01_ner":"A regra perde ‘médica Ana’ se a autoridade não contiver variante; ampliar para qualquer maiúscula gera falsos positivos. Registre posição, tipo, método e caso adversarial.","02_vinculacao":"Ana F. liga a P001 pela autoridade e contexto. Santa Rita em D008 não liga a L002 porque ‘vapor’ indica embarcação. A decisão correta pode ser não resolvido.","03_relacoes":"D003 é comunicação entre Bento e Ana; D009 contém saída e ingresso; D010 contém cooperação. Cada linha guarda papéis, ano, evidência e incerteza.","04_avaliacao":"D008 produz o erro instrutivo: igualdade de nome confundiria embarcação e lugar. O erro criaria nó ou aresta espúria; corrige-se com contexto e reavaliação da mesma amostra.","05_oficina":"Exemplo: extrair pessoas e instituições de cartas, anotar 30 trechos, comparar regra ao ouro, ler falsos negativos e publicar tabela com documento, trecho, método e confiança. O par revisa três linhas até a fonte.","exercicios_multipla_escolha":"Nas questões, desconfie de ‘sempre’, de automatismos e da ideia de ouro infalível. Resposta-modelo para a 17: sim, uma entidade perdida remove suas relações e altera medidas da rede; por isso o erro deve ser propagado e documentado."}
    for arq,txt in textos.items():
        associados=[i for i,a in ids if a==arq]; cab="\n".join(f"- {i}" for i in associados)
        (p/f"gabarito_{arq}.md").write_text(f"# Gabarito — {arq}\n\n**Atividades associadas:**\n{cab}\n\n## Exemplo de resolução\n\n{txt}\n",encoding="utf-8")
def revisores():
    p=U/"revisores";p.mkdir(parents=True,exist_ok=True);(p/"README.md").write_text("# Revisores da Unidade 10\n\nExecute seis pareceres.\n",encoding="utf-8")
    for i,t in enumerate(["nível acadêmico","didática","alinhamento","humanidades digitais","referências","técnica e acessibilidade"],1):(p/f"{i:02d}_{t.replace(' ','_')}.md").write_text(f"# Revisor — {t}\n\nAvalie evidências, rastreabilidade, erros e correções verificáveis.\n",encoding="utf-8")
    (p/"matriz_de_avaliacao.md").write_text("# Matriz\n\nAvalie conceito, execução, casos, ética e integração.\n",encoding="utf-8");(p/"modelo_de_parecer.md").write_text("# Parecer\n\n## Evidências\n\n## Correções\n",encoding="utf-8")
def main():
    for p in [U,D,U/"imagens"]:p.mkdir(parents=True,exist_ok=True)
    dados(); imgs=[("00_percurso_extracao.svg","Do texto à alegação",["Texto","Menção","Entidade","Validação"],"Toda linha retorna à fonte."),("01_metodos_ner.svg","Três caminhos",["Regras","Dicionários","Modelos","Erros"],"Cobertura e transparência variam."),("02_vinculacao.svg","Vincular com contexto",["Variantes","Candidatos","Contexto","ID"],"Não resolvido é válido."),("03_evento.svg","Representar uma ação",["Sujeito","Ação","Objeto","Evidência"],"Uma frase não é fato automático."),("04_avaliacao.svg","Avaliar e reler",["Predição","Ouro","Erros","Revisão"],"Métricas levam aos casos."),("05_entrega.svg","Extração auditável",["Esquema","Tabela","Avaliação","Limites"],"O projeto preserva rastreabilidade.")]
    for x in imgs:svg(*x)
    salvar("00_guia_da_unidade.ipynb",guia());salvar("01_reconhecimento_de_entidades.ipynb",ner());salvar("02_desambiguacao_e_vinculacao.ipynb",vinculo());salvar("03_relacoes_eventos_e_tabelas.ipynb",relacoes());salvar("04_avaliacao_validacao_e_rede.ipynb",avaliacao());salvar("05_oficina_base_derivada_de_textos.ipynb",oficina(),False)
    materiais();gabs();revisores();(U/"imagens"/"README.md").write_text("# Ilustrações\n\nSVGs autorais e acessíveis.\n",encoding="utf-8");(RAIZ/"notes"/"plano_unidade_10.md").write_text("# Plano — Unidade 10\n\nPercorrer menções, vinculação, relações, eventos, avaliação, rede e incremento cumulativo com rastreabilidade.\n",encoding="utf-8")
if __name__=="__main__":main()
