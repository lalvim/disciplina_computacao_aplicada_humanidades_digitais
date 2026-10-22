"""Constrói a Unidade 12 — uso responsável de modelos de linguagem."""
from __future__ import annotations
import csv,json
from pathlib import Path
from textwrap import dedent
from apoio_colab import adicionar_link_na_abertura,preparacao_colab,tabela_links_colab
R=Path(__file__).resolve().parents[1];U=R/"unidade_12";D=U/"dados"
def md(s):return {"cell_type":"markdown","metadata":{},"source":dedent(s).strip().splitlines(keepends=True)}
def code(s):return {"cell_type":"code","execution_count":None,"metadata":{},"outputs":[],"source":dedent(s).strip().splitlines(keepends=True)}
def salvar(n,cs,d=True):
 o=[adicionar_link_na_abertura(cs[0],U.name,n)];o+=([code(preparacao_colab(U.name,(("sklearn","scikit-learn>=1.5,<2"),)))] if d else []);o+=cs[1:]
 (U/n).write_text(json.dumps({"cells":o,"metadata":{"kernelspec":{"display_name":"Python 3","language":"python","name":"python3"},"language_info":{"name":"Python","version":"3"}},"nbformat":4,"nbformat_minor":5},ensure_ascii=False,indent=1)+"\n",encoding="utf-8")
def dados():
 D.mkdir(parents=True,exist_ok=True)
 docs=[("F001",1901,"Ata da Liga Aurora","A Liga Aurora aprovou a abertura de uma escola noturna em 12 de março de 1901.","documento fictício"),("F002",1902,"Relatório da Escola Livre","A Escola Livre registrou 84 matrículas, das quais 31 eram de trabalhadoras.","documento fictício"),("F003",1903,"Carta de Ana Ferreira","Ana solicitou livros de leitura e afirmou que as aulas ocorreriam às terças-feiras.","documento fictício"),("F004",1904,"Jornal Horizonte","O jornal anunciou conferência sobre higiene no Teatro União, sem informar público presente.","documento fictício"),("F005",1905,"Relatório municipal","O orçamento destinou 2.400 unidades à biblioteca e 1.800 à escola noturna.","documento fictício"),("F006",1906,"Carta de Bento Reis","Bento criticou a falta de iluminação, mas não pediu o fechamento da escola.","documento fictício"),("F007",1907,"Ata da Biblioteca Popular","A biblioteca recebeu 126 volumes e decidiu abrir também aos domingos.","documento fictício"),("F008",1908,"Jornal Horizonte","Uma nota mencionou a Liga Aurora e a Biblioteca Popular em campanha de arrecadação.","documento fictício"),("F009",1909,"Relatório da Escola Livre","O documento informou 97 matrículas e 68 presenças regulares.","documento fictício"),("F010",1910,"Ata da Liga Aurora","A diretoria adiou a mudança de sede; nenhuma nova data foi registrada.","documento fictício")]
 with (D/"corpus_local.csv").open("w",encoding="utf-8",newline="") as f:w=csv.writer(f);w.writerow(["id_documento","ano","titulo","texto","natureza"]);w.writerows(docs)
 saidas=[("P01","Resuma F002 em uma frase.","O relatório registra 84 matrículas, incluindo 31 trabalhadoras.","adequada","F002","fiel e apoiada"),("P02","Quantos estudantes concluíram o curso em F002?","Sessenta estudantes concluíram o curso.","alucinacao","","número não aparece"),("P03","A escola fechou por falta de luz?","Sim, a escola foi fechada.","contradicao","F006","o texto nega fechamento"),("P04","Liste valores do orçamento e cite a fonte.","Biblioteca: 2.400; escola noturna: 1.800 (F005).","adequada","F005","valores rastreáveis"),("P05","Quem participou da conferência?","O documento não informa participantes ou público.","abstencao_adequada","F004","reconhece ausência"),("P06","Escreva uma narrativa dramática sobre Ana.","Ana enfrentou perseguição política e fundou três escolas.","extrapolacao","","afirmações inventadas")]
 with (D/"saidas_modelo_hipotetico.csv").open("w",encoding="utf-8",newline="") as f:w=csv.writer(f);w.writerow(["id_teste","prompt","resposta","rotulo_ouro","fontes_declaradas","justificativa"]);w.writerows(saidas)
 (D/"proveniencia.json").write_text(json.dumps({"natureza":"corpus e saídas inteiramente fictícios","modelo":"hipotético; nenhuma saída foi produzida por serviço real","finalidade":"avaliação controlada, prompting, recuperação e rastreabilidade","privacidade":"nenhum dado pessoal real","limite":"não permite comparar fornecedores ou modelos reais"},ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
def svg(n,t,es,r):
 w=190;gap=(920-len(es)*w)/max(1,len(es)-1);a=[]
 for i,e in enumerate(es):
  x=40+i*(w+gap);a.append(f'<rect x="{x:.0f}" y="82" width="{w}" height="112" rx="14" fill="#f4f0e6" stroke="#294c60" stroke-width="2"/><text x="{x+w/2:.0f}" y="140" text-anchor="middle" font-size="17">{e}</text>')
  if i<len(es)-1:a.append(f'<path d="M{x+w+5:.0f} 140 H{x+w+gap-8:.0f}" stroke="#a44a3f" stroke-width="3" marker-end="url(#a)"/>')
 (U/"imagens"/n).write_text(f'<svg xmlns="http://www.w3.org/2000/svg" width="1000" height="280" role="img" aria-labelledby="title desc"><title id="title">{t}</title><desc id="desc">{r}</desc><defs><marker id="a" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L0,6 L9,3 z" fill="#a44a3f"/></marker></defs><rect width="100%" height="100%" fill="#fffdf8"/><text x="500" y="40" text-anchor="middle" font-size="25" font-weight="bold">{t}</text>{"".join(a)}<text x="500" y="245" text-anchor="middle" font-size="16">{r}</text></svg>',encoding="utf-8")
def guia():return [md('''# Unidade 12 — Guia de estudo
## Como utilizar modelos de linguagem de maneira responsável?

Modelos de linguagem podem apoiar busca, classificação, extração, resumo e redação,
mas produzem texto plausível sem garantir verdade ou fonte. Nesta unidade, cada tarefa
terá referência, comparação simples, amostra de avaliação e condição de recusa.

![O percurso liga tarefa, referência, modelo, avaliação e decisão.](imagens/00_percurso_responsavel.svg)'''),md('''## Ambiente controlado

Nenhum notebook chama API ou envia documentos. As saídas são explicitamente simuladas
e pertencem a um modelo hipotético. Isso permite estudar erros, não avaliar um produto.

| Notebook | Problema | Produto |
|---|---|---|
| 00 | Quando usar? | contrato de uso |
| 01 | Como textos viram vetores? | similaridade comparada |
| 02 | Como instruções alteram respostas? | protocolo de prompts |
| 03 | Recuperação melhora rastreabilidade? | RAG local simplificado |
| 04 | Como avaliar e proteger dados? | ficha de auditoria |
| 05 | O ganho justifica o risco? | experimento cumulativo |'''),code('''import json,pandas as pd
corpus=pd.read_csv("dados/corpus_local.csv");saidas=pd.read_csv("dados/saidas_modelo_hipotetico.csv")
print(json.loads(open("dados/proveniencia.json",encoding="utf-8").read())["modelo"])
display(corpus.head(3));display(saidas.head(3))'''),md('''### U12-A01 — Discussão — assistência ou delegação?

**Dinâmica (15 minutos):** classifique resumo, busca, interpretação e decisão ética
como assistência possível, tarefa condicionada ou delegação inadequada. Para cada uma,
defina evidência e revisão humana. **Resposta:** escreva aqui.

## Passagem

Começaremos pelas representações que sustentam similaridade, sem tratar proximidade
vetorial como equivalência semântica perfeita.''')]
def representacoes():return [md('''# Representações vetoriais e transformers

TF-IDF representa ocorrências lexicais; embeddings densos aproximam usos aprendidos.
Transformers contextualizam tokens por atenção, mas contexto computacional não é
compreensão histórica garantida. Representação, corpus de treino e versão importam.

![TF-IDF e embeddings preservam sinais diferentes.](imagens/01_representacoes.svg)'''),code('''import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.decomposition import TruncatedSVD
d=pd.read_csv("dados/corpus_local.csv");v=TfidfVectorizer();X=v.fit_transform(d.texto)
consulta="matrículas na escola noturna";q=v.transform([consulta]);d["similaridade_tfidf"]=cosine_similarity(q,X)[0]
# Projeção densa local é apenas analogia didática, não embedding de transformer.
svd=TruncatedSVD(n_components=4,random_state=42);Xd=svd.fit_transform(X);qd=svd.transform(q);d["similaridade_densa_local"]=cosine_similarity(qd,Xd)[0]
display(d.nlargest(5,"similaridade_tfidf")[["id_documento","titulo","similaridade_tfidf","similaridade_densa_local"]])'''),md('''A projeção SVD demonstra densidade, mas não deve ser chamada de embedding contextual.
Um modelo pré-treinado exigiria documentação de versão, domínio, licença e dados enviados.

### U12-A02 — Atividade — proximidade não é resposta

Altere a consulta, compare os dois rankings e leia os documentos. Registre um acerto e
um vizinho enganoso. **Dinâmica (25 minutos):** dupla alterna ranking e leitura.
**Resposta:** escreva aqui.

## Passagem

Representação seleciona contexto; o prompt seleciona tarefa, formato e critérios. A
seguir isolaremos variações de instrução sem atribuir diferenças a um serviço real.''')]
def prompts():return [md('''# Tarefas, prompting e sensibilidade

Um protocolo de prompt declara tarefa, corpus permitido, formato, evidência, tratamento
da ausência e critérios. Pequenas mudanças podem alterar a resposta; registre prompt,
configuração, versão, data e saída, sem escolher apenas a melhor tentativa.

![Componentes de um prompt auditável.](imagens/02_prompt.svg)'''),code('''import pandas as pd
s=pd.read_csv("dados/saidas_modelo_hipotetico.csv").fillna("")
display(pd.crosstab(s.rotulo_ouro,s.fontes_declaradas.ne(""),rownames=["tipo de saída"],colnames=["declara fonte"]))
display(s[["id_teste","prompt","resposta","rotulo_ouro","justificativa"]])'''),md('''## Comparação justa

Pré-defina variantes, aplique-as ao mesmo conjunto e conte recusas adequadas.
Classificação, extração e resumo exigem critérios distintos; fluência não é fidelidade.

### U12-A03 — Atividade — protocolo de prompt

Reescreva P02 incluindo corpus permitido, citação e “se ausente, diga não consta”. Crie
rubrica de fidelidade, cobertura, citação e abstinência. **Dinâmica (30 minutos):**
trios; autor, adversário e avaliador cego. **Resposta:** escreva aqui.

## Passagem

Fornecer trechos pode limitar a resposta, mas recuperação também erra. Separaremos
recuperar de gerar.''')]
def rag():return [md('''# Recuperação aumentada por documentos

RAG combina recuperação e geração. Aqui implementamos recuperação local e resposta
extrativa como referência verificável. Um gerador deveria limitar-se aos trechos e
citar identificadores.

![Consulta, trechos, resposta e verificação.](imagens/03_rag.svg)'''),code('''import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
d=pd.read_csv("dados/corpus_local.csv");v=TfidfVectorizer();X=v.fit_transform(d.texto)
def recuperar(pergunta,k=3):
 s=cosine_similarity(v.transform([pergunta]),X)[0];idx=s.argsort()[::-1][:k]
 return d.iloc[idx].assign(pontuacao=s[idx])[["id_documento","titulo","texto","pontuacao"]]
pergunta="Quantas matrículas foram registradas e quantas presenças eram regulares?"
contexto=recuperar(pergunta,3);display(contexto)
resposta_referencia="F002 registra 84 matrículas; F009 registra 97 matrículas e 68 presenças regulares."
print(resposta_referencia)'''),md('''Recuperação não garante resposta, e uma citação pode não sustentar a frase. Avalie
separadamente cobertura da recuperação, fidelidade e correção da citação.

### U12-A04 — Atividade — falhas do RAG

Teste pergunta respondível, ambígua e ausente. Avalie trechos, escreva resposta
extrativa ou abstinência e confira cada afirmação. **Dinâmica (30 minutos):** dupla,
recuperador e verificador. **Resposta:** escreva aqui.

## Passagem

Rastreabilidade reduz um risco, não todos. Avaliaremos erros, privacidade e baseline.''')]
def avaliacao():return [md('''# Avaliação, alucinação, privacidade e comparação

Alucinação é conteúdo sem sustentação; contradição conflita com a fonte; extrapolação
vai além dela; abstinência adequada reconhece ausência. Avalie tarefas reais e casos.

![Afirmação, fonte, rótulo, risco e decisão.](imagens/04_auditoria.svg)'''),code('''import pandas as pd
s=pd.read_csv("dados/saidas_modelo_hipotetico.csv").fillna("")
s["apoiada"]=s.rotulo_ouro.isin(["adequada","abstencao_adequada"])
resumo=s.groupby("rotulo_ouro").agg(n=("id_teste","size"),proporcao_com_fonte=("fontes_declaradas",lambda x:(x!="").mean()))
display(resumo);taxa_apoiada=s.apoiada.mean();print("Taxa apoiada:",round(taxa_apoiada,3))'''),md('''## Matriz de risco antes do envio

| Pergunta | Decisão |
|---|---|
| Há dados pessoais, sigilosos ou restritos? | não enviar sem base e proteção |
| O serviço retém ou usa dados? | verificar termos e configuração |
| A tarefa pode ser local? | preferir minimização |
| Há revisão e contestação? | implementar antes do uso |

Compare com busca lexical, regra, TF-IDF ou trabalho humano amostrado. Fluência não
compensa automaticamente custo, risco ou erro.

### U12-A05 — Atividade — auditoria de seis saídas

Confira cada rótulo no corpus; calcule taxa apoiada; identifique o erro de maior dano e
preencha a matriz de risco. **Dinâmica (35 minutos):** avaliação independente e
adjudicação em trio. **Resposta:** escreva aqui.

## Passagem

A oficina transforma as verificações num experimento pré-definido e comparável.''')]
def oficina():return [md('''# Oficina — experimento controlado com modelo de linguagem

**Produto:** seção no mesmo relatório-notebook. Compare uma abordagem de linguagem a
uma referência simples, ou justifique não enviar/usar o corpus. Serviço externo não é
obrigatório.

![Tarefa, referência, protocolo, avaliação e decisão.](imagens/05_entrega.svg)'''),md('''## Roteiro de 75 minutos

| Tempo | Ação | Evidência |
|---:|---|---|
| 0–12 | definir tarefa e risco | contrato |
| 12–25 | criar referência simples | baseline |
| 25–38 | congelar prompts e amostra | protocolo |
| 38–55 | produzir/importar saídas autorizadas | registro |
| 55–67 | avaliar afirmações e casos | rubrica |
| 67–75 | decidir adoção, revisão ou recusa | conclusão |

### U12-A06 — Oficina — incremento cumulativo

Registre modelo/versão quando houver, prompts, dados enviados, baseline, amostra, erros,
custos e decisão. **Resposta:** no mesmo relatório-notebook.

### U12-A07 — Revisão por pares — reproduzir e contestar

O colega reconstrói tarefa, dados, prompt, fonte e julgamento de três respostas.
Registra ponto claro, dúvida e mudança. **Dinâmica:** 20 minutos.

## Fechamento

Uso responsável é decisão comparativa e revogável. A Unidade 13 reunirá validade,
robustez, generalização, incerteza e vieses.''')]
def extras():
 nbs=(("Guia","00_guia_da_unidade.ipynb"),("Representações","01_representacoes_e_transformers.ipynb"),("Prompting","02_tarefas_prompting_e_sensibilidade.ipynb"),("RAG local","03_recuperacao_aumentada_por_documentos.ipynb"),("Avaliação e privacidade","04_avaliacao_alucinacao_e_privacidade.ipynb"),("Oficina","05_oficina_experimento_controlado.ipynb"))
 (U/"README.md").write_text(f"# Unidade 12 — Modelos de linguagem responsáveis\n\n{tabela_links_colab('unidade_12',nbs)}\n\nOs notebooks 00–04 usam apenas arquivos locais; execute a preparação. A oficina atualiza o relatório cumulativo. Nenhum exemplo avalia produto real.\n",encoding="utf-8")
 (U/"referencias.md").write_text("""# Referências da Unidade 12

- VASWANI, Ashish et al. Attention Is All You Need. *NeurIPS*, 2017.
- DEVLIN, Jacob et al. BERT: Pre-training of Deep Bidirectional Transformers. *NAACL*, 2019.
- LEWIS, Patrick et al. Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks. *NeurIPS*, 2020.
- BENDER, Emily M. et al. On the Dangers of Stochastic Parrots. *FAccT*, 2021.
- LIANG, Percy et al. Holistic Evaluation of Language Models. *TMLR*, 2023.
- MITCHELL, Margaret et al. Model Cards for Model Reporting. *FAT*, 2019.
- NIST. *Artificial Intelligence Risk Management Framework: Generative AI Profile*. NIST AI 600-1, 2024.
""",encoding="utf-8")
 qs=["embedding é o texto completo","transformer usa atenção","similaridade prova sentido","prompt deve ser registrado","escolher só melhor tentativa é válido","fluência garante fidelidade","RAG separa recuperação e geração","citação sempre sustenta frase","pergunta ausente pede abstinência","alucinação é conteúdo sem apoio","contradição conflita com fonte","extrapolação vai além da fonte","média substitui casos","baseline simples é útil","versão do modelo importa","dados sigilosos podem ser enviados livremente","minimização reduz exposição","revisão humana pode ser necessária","resultado simulado avalia fornecedor real","não adoção pode ser responsável"]
 linhas=["# U12-A08 — Exercícios de múltipla escolha",""]
 for i,q in enumerate(qs,1):linhas += [f"## Questão {i}",q.capitalize()+"?  ","A) Sim, sempre.  B) Não necessariamente; deve ser testado e documentado.  C) Apenas com API.  D) Apenas sem fontes.",""]
 (U/"exercicios_unidade_12_texto.md").write_text("\n".join(linhas),encoding="utf-8")
 p=U/"gabaritos";p.mkdir(parents=True,exist_ok=True);ids=[("U12-A01","00_guia"),("U12-A02","01_representacoes"),("U12-A03","02_prompt"),("U12-A04","03_rag"),("U12-A05","04_avaliacao"),("U12-A06","05_oficina"),("U12-A07","05_oficina"),("U12-A08","exercicios")]
 (p/"README.md").write_text("# Gabaritos da Unidade 12\n\n"+"\n".join(f"- {i}: `gabarito_{a}.md`" for i,a in ids)+"\n",encoding="utf-8")
 tx={"00_guia":"Busca e resumo podem assistir; interpretação exige fontes e revisão; decisão ética não deve ser delegada. Cada tarefa recebe evidência e condição de recusa.","01_representacoes":"Os rankings mudam porque TF-IDF e projeção densa preservam sinais distintos. Leia o vizinho e não chame proximidade de equivalência semântica.","02_prompt":"Prompt revisado limita ao corpus, exige ID e manda dizer ‘não consta’. A rubrica separa fidelidade, cobertura, citação e abstinência.","03_rag":"Pergunta respondível recupera F002/F009; pergunta ausente deve gerar abstinência. Citação é conferida afirmação por afirmação.","04_avaliacao":"P02 inventa número; P03 contradiz F006; P06 extrapola. O dano maior depende do uso. Não envie corpus sensível sem base, termos e minimização.","05_oficina":"Exemplo: comparar busca TF-IDF e respostas registradas em 20 perguntas, avaliar fontes e recusas, calcular custo e decidir uso apenas como triagem revisada.","exercicios":"Exemplo da questão 8: uma resposta pode citar F005 e ainda atribuir a ele frase ausente. Verifique entailment entre afirmação e trecho, não só presença do ID."}
 for a,t in tx.items():
  ais=[i for i,b in ids if b==a];(p/f"gabarito_{a}.md").write_text(f"# Gabarito — {a}\n\n**Atividades associadas:**\n"+"\n".join(f"- {i}" for i in ais)+f"\n\n## Exemplo de resolução\n\n{t}\n",encoding="utf-8")
 rv=U/"revisores";rv.mkdir(parents=True,exist_ok=True);(rv/"README.md").write_text("# Revisores da Unidade 12\n\nExecute seis pareceres.\n",encoding="utf-8")
 for i,t in enumerate(["nível acadêmico","didática","alinhamento","humanidades digitais","referências","técnica e acessibilidade"],1):(rv/f"{i:02d}_{t.replace(' ','_')}.md").write_text(f"# Revisor — {t}\n\nAvalie comparação, rastreabilidade, privacidade, casos e correções verificáveis.\n",encoding="utf-8")
 (rv/"matriz_de_avaliacao.md").write_text("# Matriz\n\nAvalie tarefa, baseline, protocolo, evidência, risco e decisão.\n",encoding="utf-8");(rv/"modelo_de_parecer.md").write_text("# Parecer\n\n## Evidências\n\n## Correções\n",encoding="utf-8")
def main():
 for p in [U,D,U/"imagens"]:p.mkdir(parents=True,exist_ok=True)
 dados();imgs=[("00_percurso_responsavel.svg","Uso responsável",["Tarefa","Referência","Avaliação","Decisão"],"Fluência não substitui evidência."),("01_representacoes.svg","Representações parciais",["Texto","TF-IDF","Vetores","Leitura"],"Proximidade depende da representação."),("02_prompt.svg","Prompt auditável",["Tarefa","Contexto","Formato","Recusa"],"Registre todas as variantes."),("03_rag.svg","Recuperar e verificar",["Consulta","Trechos","Resposta","Fontes"],"Citação também precisa ser conferida."),("04_auditoria.svg","Auditar afirmações",["Saída","Fonte","Erro","Risco"],"Médias não substituem casos."),("05_entrega.svg","Experimento controlado",["Baseline","Protocolo","Casos","Decisão"],"Não adoção é resultado válido.")]
 for x in imgs:svg(*x)
 salvar("00_guia_da_unidade.ipynb",guia());salvar("01_representacoes_e_transformers.ipynb",representacoes());salvar("02_tarefas_prompting_e_sensibilidade.ipynb",prompts());salvar("03_recuperacao_aumentada_por_documentos.ipynb",rag());salvar("04_avaliacao_alucinacao_e_privacidade.ipynb",avaliacao());salvar("05_oficina_experimento_controlado.ipynb",oficina(),False);extras();(U/"imagens"/"README.md").write_text("# Ilustrações\n\nSVGs autorais e acessíveis.\n",encoding="utf-8");(R/"notes"/"plano_unidade_12.md").write_text("# Plano — Unidade 12\n\nPercorrer representações, transformers, tarefas, prompting, RAG, erros, avaliação, baseline e privacidade; incorporar experimento ou não adoção ao projeto.\n",encoding="utf-8")
if __name__=="__main__":main()
