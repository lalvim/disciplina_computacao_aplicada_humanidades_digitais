"""Constrói a Unidade 14 — documentação e comunicação reprodutível."""
from __future__ import annotations
import csv,hashlib,json
from pathlib import Path
from textwrap import dedent
from apoio_colab import adicionar_link_na_abertura,preparacao_colab,tabela_links_colab
R=Path(__file__).resolve().parents[1];U=R/"unidade_14";D=U/"dados"
def md(s):return {"cell_type":"markdown","metadata":{},"source":dedent(s).strip().splitlines(keepends=True)}
def code(s):return {"cell_type":"code","execution_count":None,"metadata":{},"outputs":[],"source":dedent(s).strip().splitlines(keepends=True)}
def salvar(n,cs,d=True):
 o=[adicionar_link_na_abertura(cs[0],U.name,n)];o+=([code(preparacao_colab(U.name))] if d else []);o+=cs[1:]
 (U/n).write_text(json.dumps({"cells":o,"metadata":{"kernelspec":{"display_name":"Python 3","language":"python","name":"python3"},"language_info":{"name":"Python","version":"3"}},"nbformat":4,"nbformat_minor":5},ensure_ascii=False,indent=1)+"\n",encoding="utf-8")
def dados():
 D.mkdir(parents=True,exist_ok=True)
 manifesto=[("README.md","documentação","aberto","descreve pergunta, execução e limites"),("relatorio.ipynb","análise","aberto","narrativa, código e resultados"),("dados/processados.csv","dados derivados","restrito","contém quase-identificadores"),("dados/dicionario.csv","documentação","aberto","define campos e ausências"),("dados/proveniencia.json","documentação","aberto","origem e transformações"),("requirements.txt","ambiente","aberto","dependências versionadas"),("LICENSE","licença","aberto","condições do código")]
 with (D/"manifesto_projeto.csv").open("w",encoding="utf-8",newline="") as f:w=csv.writer(f);w.writerow(["caminho","papel","acesso","justificativa"]);w.writerows(manifesto)
 pessoas=[("R001","40–49","Capital","tema A",3),("R002","30–39","Interior","tema B",1),("R003","40–49","Capital","tema A",2),("R004","60–69","Interior","tema raro",1),("R005","30–39","Capital","tema B",4),("R006","50–59","Interior","tema A",2),("R007","60–69","Capital","tema C",1),("R008","40–49","Interior","tema B",3)]
 with (D/"registros_compartilhamento.csv").open("w",encoding="utf-8",newline="") as f:w=csv.writer(f);w.writerow(["id_pesquisa","faixa_etaria","local","tema","documentos"]);w.writerows(pessoas)
 resultados=[("modelo principal",.71,.64,.77,"associação condicionada"),("sensibilidade",.68,.59,.75,"resultado parcialmente sensível"),("baseline",.50,.42,.58,"referência simples")]
 with (D/"resultados_comunicacao.csv").open("w",encoding="utf-8",newline="") as f:w=csv.writer(f);w.writerow(["analise","estimativa","limite_inferior","limite_superior","alcance"]);w.writerows(resultados)
 (D/"proveniencia.json").write_text(json.dumps({"natureza":"dados inteiramente fictícios","finalidade":"auditoria de documentação, compartilhamento e comunicação","risco_didatico":"tema raro e combinação de atributos simulam risco de reidentificação","limite":"não contém pessoas ou projetos reais"},ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
def svg(n,t,es,r):
 w=190;gap=(920-len(es)*w)/max(1,len(es)-1);a=[]
 for i,e in enumerate(es):
  x=40+i*(w+gap);a.append(f'<rect x="{x:.0f}" y="82" width="{w}" height="112" rx="14" fill="#f4f0e6" stroke="#294c60" stroke-width="2"/><text x="{x+w/2:.0f}" y="140" text-anchor="middle" font-size="17">{e}</text>')
  if i<len(es)-1:a.append(f'<path d="M{x+w+5:.0f} 140 H{x+w+gap-8:.0f}" stroke="#a44a3f" stroke-width="3" marker-end="url(#a)"/>')
 (U/"imagens"/n).write_text(f'<svg xmlns="http://www.w3.org/2000/svg" width="1000" height="280" role="img" aria-labelledby="title desc"><title id="title">{t}</title><desc id="desc">{r}</desc><defs><marker id="a" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L0,6 L9,3 z" fill="#a44a3f"/></marker></defs><rect width="100%" height="100%" fill="#fffdf8"/><text x="500" y="40" text-anchor="middle" font-size="25" font-weight="bold">{t}</text>{"".join(a)}<text x="500" y="245" text-anchor="middle" font-size="16">{r}</text></svg>',encoding="utf-8")
def guia():return [md('''# Unidade 14 — Guia de estudo
## Como documentar e comunicar uma pesquisa computacional?

Um projeto reprodutível permite compreender o que foi feito, verificar resultados e
reexecutar o que pode ser compartilhado. Reprodutibilidade não exige abrir materiais
sensíveis: exige explicar acesso, restrições e procedimentos.

![Pergunta, dados, código, ambiente, resultados e limites formam o projeto.](imagens/00_projeto_reprodutivel.svg)'''),md('''## Percurso e fechamento comum

| Notebook | Pergunta | Produto |
|---|---|---|
| 00 | O que outra pessoa precisa entender? | mapa do projeto |
| 01 | Como documentar arquivos e decisões? | manifesto e histórico |
| 02 | O que significa reproduzir? | protocolo e verificações |
| 03 | Como comunicar resultado e incerteza? | figura e alegação calibrada |
| 04 | O que pode ser compartilhado? | plano de acesso e relatório |
| 05 | O projeto está pronto? | versão final e apresentação |

As entregas anteriores convergem no mesmo relatório-notebook: pergunta, corpus,
preparação, exploração, método, avaliação, limites e conclusão.'''),code('''import json,pandas as pd
m=pd.read_csv("dados/manifesto_projeto.csv");p=json.loads(open("dados/proveniencia.json",encoding="utf-8").read())
print(p["natureza"]);display(m)'''),md('''### U14-A01 — Discussão — reproduzir, replicar ou reutilizar?

**Dinâmica (15 minutos):** diferencie reexecutar os mesmos dados/código, testar em
novos dados e reutilizar componentes. Para cada objetivo, liste o que deve estar
documentado e o que pode permanecer restrito. **Resposta:** escreva aqui.

## Passagem

Começaremos pelo inventário do projeto: arquivos, papéis, acesso, versões e decisões.''')]
def documentacao():return [md('''# Notebooks, documentação e versionamento

Um notebook deve explicar antes de executar, interpretar depois e registrar limites.
README orienta entrada; dicionário define campos; proveniência registra origem e
transformações; histórico de versões explica mudanças, não apenas armazena arquivos.

![Documentação distribui funções entre README, notebook, dados e ambiente.](imagens/01_documentacao.svg)'''),code('''import pandas as pd
m=pd.read_csv("dados/manifesto_projeto.csv")
checks=pd.DataFrame({"verificacao":["README presente","dicionário presente","proveniência presente","ambiente presente","acesso justificado"],"resultado":[m.caminho.eq("README.md").any(),m.caminho.str.contains("dicionario").any(),m.caminho.str.contains("proveniencia").any(),m.caminho.eq("requirements.txt").any(),m.justificativa.notna().all()]})
display(checks);display(pd.crosstab(m.papel,m.acesso))'''),md('''## Registro mínimo de decisão

| Campo | Exemplo |
|---|---|
| decisão | excluir duplicatas exatas |
| motivo | mesma fonte e identificador |
| alternativa | manter e ponderar |
| impacto | 12 registros removidos |
| versão/data | v0.4, 2026-10-22 |

Commits pequenos e mensagens substantivas ajudam a reconstruir mudanças. Versionar não
autoriza publicar dados restritos nem credenciais.

### U14-A02 — Atividade — manifesto e registro de decisão

Crie o manifesto real do projeto e documente três decisões que alteraram resultados.
**Dinâmica (30 minutos):** dupla tenta localizar cada arquivo e reconstruir uma decisão
sem explicação oral. **Resposta:** escreva aqui.

## Passagem

Arquivos presentes ainda podem falhar ao reexecutar. O próximo notebook transforma
reprodutibilidade em verificações observáveis.''')]
def reproducao():return [md('''# Ambiente, execução e verificações reprodutíveis

Registre versões, ordem, sementes, caminhos relativos e entradas. Uma execução limpa
deve produzir saídas esperadas; checks detectam mudanças silenciosas em esquema,
quantidade, ausências e arquivos.

![Entradas e ambiente passam por código até resultados verificáveis.](imagens/02_reproducao.svg)'''),code('''import hashlib,json,platform,pandas as pd,numpy as np
from pathlib import Path
arquivo=Path("dados/resultados_comunicacao.csv");d=pd.read_csv(arquivo)
hash_sha256=hashlib.sha256(arquivo.read_bytes()).hexdigest()
ambiente={"python":platform.python_version(),"pandas":pd.__version__,"numpy":np.__version__}
checks={"linhas":len(d)==3,"colunas":list(d.columns)==["analise","estimativa","limite_inferior","limite_superior","alcance"],"intervalos_validos":((d.limite_inferior<=d.estimativa)&(d.estimativa<=d.limite_superior)).all()}
print("SHA-256:",hash_sha256);print("Ambiente:",ambiente);print("Checks:",checks);assert all(checks.values())'''),md('''Hash detecta mudança de bytes, não garante qualidade ou autenticidade. Versões exatas
favorecem repetição; faixas controladas favorecem manutenção. Registre sistema e data,
mas não publique caminhos pessoais, tokens ou segredos.

### U14-A03 — Atividade — teste de execução limpa

Reinicie e execute tudo; registre tempo, versões, primeiro erro e correção; crie três
checks substantivos. **Dinâmica (30 minutos):** troca de notebooks entre duplas sem
instruções orais. **Resposta:** escreva aqui.

## Passagem

Reproduzir números não garante comunicação correta. A seguir alinharemos figura,
incerteza, escala e força da afirmação.''')]
def comunicacao():return [md('''# Visualização responsável, incerteza e linguagem

Uma figura deve declarar dados, unidade, denominador, escala e incerteza. Eixos
truncados e cores inacessíveis podem produzir ênfase indevida. Título não deve
antecipar causalidade que o desenho não sustenta.

![Resultado, incerteza, casos e linguagem calibrada.](imagens/03_comunicacao.svg)'''),code('''import pandas as pd,matplotlib.pyplot as plt
d=pd.read_csv("dados/resultados_comunicacao.csv")
erro=[d.estimativa-d.limite_inferior,d.limite_superior-d.estimativa]
fig,ax=plt.subplots(figsize=(8,4));ax.errorbar(d.estimativa,d.analise,xerr=erro,fmt="o",capsize=5,color="#294c60");ax.axvline(.5,color="#777",linestyle="--",label="baseline");ax.set(xlim=(0,1),xlabel="Estimativa e intervalo",title="Resultados e incerteza — dados fictícios");ax.legend();plt.tight_layout();plt.show()
display(d)'''),md('''## Escada da afirmação

| Nível | Formulação |
|---|---|
| descrição | “na coleção, a proporção foi...” |
| associação | “X esteve associado a Y...” |
| previsão | “no teste reservado, o modelo previu...” |
| causalidade | “intervir em X alteraria Y...” — exige desenho causal |

### U14-A04 — Atividade — figura, legenda e alegação

Reescreva título, legenda e conclusão de uma figura. Inclua unidade, denominador,
incerteza, caso e limite. **Dinâmica (30 minutos):** uma pessoa vê apenas a figura; se
não reconstruir a leitura, o autor revisa. **Resposta:** escreva aqui.

## Passagem

Clareza não autoriza abertura irrestrita. A próxima etapa decide o que compartilhar,
restringir, anonimizar ou apenas documentar.''')]
def compartilhamento():return [md('''# Proteção de dados, direitos e compartilhamento responsável

Remover nomes não garante anonimização: combinações raras podem reidentificar. Avalie
necessidade, base ética/jurídica, consentimento, licença, direitos autorais, risco de
ligação, acesso e retenção.

![Classificar risco antecede transformar e definir acesso.](imagens/04_compartilhamento.svg)'''),code('''import pandas as pd
d=pd.read_csv("dados/registros_compartilhamento.csv")
combinacoes=d.groupby(["faixa_etaria","local","tema"]).size().rename("k").reset_index()
avaliacao=d.merge(combinacoes,on=["faixa_etaria","local","tema"])
avaliacao["risco_didatico"]=avaliacao.k.map(lambda k:"alto: combinação única" if k==1 else "menor: combinação repetida")
display(avaliacao);combinacoes_unicas=(avaliacao.k==1).sum();print("Combinações únicas:",combinacoes_unicas)'''),md('''## Estratégias e limites

- minimizar campos e precisão;
- agregar ou generalizar categorias;
- separar chaves e dados analíticos;
- controlar acesso em vez de publicar;
- compartilhar código, dicionário e dados sintéticos quando o original for restrito;
- registrar licença e titularidade de cada fonte.

$k$-anonimato descritivo mostra combinações raras, mas não resolve atributos sensíveis,
ataques auxiliares ou finalidade indevida.

### U14-A05 — Atividade — plano de compartilhamento

Classifique cada artefato como aberto, restrito ou não compartilhável; indique direito,
risco, transformação, acesso e substituto reproduzível. **Dinâmica (35 minutos):** trio
com pesquisador, participante e curador. **Resposta:** escreva aqui.

## Passagem

O fechamento reúne narrativa acadêmica, pacote verificável e apresentação oral.''')]
def oficina():return [md('''# Oficina final — projeto reprodutível e apresentação

**Produto:** versão final do mesmo relatório-notebook, acompanhada pelos artefatos que
podem ser compartilhados e por uma apresentação. Não recomponha o projeto em um novo
notebook sem histórico.

![Pergunta, evidência, método, avaliação e contribuição fecham o projeto.](imagens/05_fechamento.svg)'''),md('''## Estrutura do relatório-notebook

1. pergunta, contribuição e contexto humanístico;
2. fontes, corpus, critérios, ética e proveniência;
3. preparação e decisões reproduzíveis;
4. exploração e método escolhido;
5. resultados com figuras/tabelas e casos;
6. avaliação, sensibilidade, vieses e limites;
7. conclusão calibrada e próximos passos;
8. referências, ambiente e instruções de execução.

## Roteiro de oficina — 90 minutos

| Tempo | Ação | Evidência |
|---:|---|---|
| 0–15 | executar do início | log e checks |
| 15–30 | conferir manifesto e acesso | pacote |
| 30–48 | revisar cadeia argumentativa | mapa |
| 48–63 | revisar figuras e casos | comunicação |
| 63–75 | ensaiar apresentação de 7 min | roteiro |
| 75–90 | receber e implementar parecer | registro |

### U14-A06 — Oficina — versão final cumulativa

Entregue o mesmo notebook evoluído, dados compartilháveis ou substitutos, dicionário,
proveniência, requisitos e README. **Resposta:** links e versão no repositório.

### U14-A07 — Banca simulada — contribuição e limite

Apresente em 7 minutos: problema, dados, método, resultado, caso, validade, limite e
contribuição. Pares fazem duas perguntas; o autor registra resposta e ajuste final.

## Critérios finais

Coerência pergunta–dados–método; contribuição às Humanidades; reprodutibilidade;
avaliação mista; ética e direitos; comunicação da incerteza; honestidade sobre limites.''')]
def extras():
 nbs=(("Guia","00_guia_da_unidade.ipynb"),("Documentação","01_documentacao_e_versionamento.ipynb"),("Reprodução","02_execucao_e_verificacoes.ipynb"),("Comunicação","03_visualizacao_incerteza_e_linguagem.ipynb"),("Compartilhamento","04_protecao_direitos_e_compartilhamento.ipynb"),("Oficina final","05_oficina_projeto_final.ipynb"))
 (U/"README.md").write_text(f"# Unidade 14 — Documentar e comunicar\n\n{tabela_links_colab('unidade_14',nbs)}\n\nExecute a preparação nos notebooks 00–04. A oficina fecha o mesmo relatório-notebook cumulativo. Dados fictícios.\n",encoding="utf-8")
 (U/"referencias.md").write_text("""# Referências da Unidade 14

- WILSON, Greg et al. Good Enough Practices in Scientific Computing. *PLOS Computational Biology*, 2017.
- RULE, Adam et al. Ten Simple Rules for Writing and Sharing Computational Analyses in Jupyter Notebooks. *PLOS Computational Biology*, 2019.
- PENG, Roger D. Reproducible Research in Computational Science. *Science*, 2011.
- WILKINSON, Mark D. et al. The FAIR Guiding Principles. *Scientific Data*, 2016.
- CARROLL, Stephanie Russo et al. The CARE Principles for Indigenous Data Governance. *Data Science Journal*, 2020.
- CLEVELAND, William S.; MCGILL, Robert. Graphical Perception. *JASA*, 1984.
- BRUNTON, Finn; NISSENBAUM, Helen. *Obfuscation*. MIT Press, 2015.
""",encoding="utf-8")
 qs=["notebook substitui README","dicionário define campos","proveniência registra origem","versionamento autoriza publicar dados","semente ajuda reprodução","hash garante qualidade","check detecta mudança","caminho relativo favorece portabilidade","figura deve declarar unidade","eixo truncado pode induzir ênfase","intervalo deve ser comunicado","associação equivale a causalidade","remover nome anonimiza sempre","combinação rara eleva risco","k-anonimato resolve todo risco","licença deve ser verificada","dados restritos impedem qualquer reprodução","substituto sintético pode ajudar","apresentação deve incluir limite","entrega final é novo projeto"]
 linhas=["# U14-A08 — Exercícios de múltipla escolha",""]
 for i,q in enumerate(qs,1):linhas += [f"## Questão {i}",q.capitalize()+"?  ","A) Sempre.  B) Não necessariamente; requer documentação e contexto.  C) Apenas no Colab.  D) Apenas com dados abertos.",""]
 (U/"exercicios_unidade_14_texto.md").write_text("\n".join(linhas),encoding="utf-8")
 p=U/"gabaritos";p.mkdir(parents=True,exist_ok=True);ids=[("U14-A01","00_guia"),("U14-A02","01_documentacao"),("U14-A03","02_reproducao"),("U14-A04","03_comunicacao"),("U14-A05","04_compartilhamento"),("U14-A06","05_oficina"),("U14-A07","05_oficina"),("U14-A08","exercicios")]
 (p/"README.md").write_text("# Gabaritos da Unidade 14\n\n"+"\n".join(f"- {i}: `gabarito_{a}.md`" for i,a in ids)+"\n",encoding="utf-8")
 tx={"00_guia":"Reprodução reexecuta; replicação testa novos dados; reutilização adapta componentes. Dados podem ser restritos se código, esquema, acesso e substitutos forem documentados.","01_documentacao":"Manifesto lista papel, acesso e justificativa. Decisões registram motivo, alternativa, impacto e versão; commits não contêm dados ou segredos.","02_reproducao":"Execução limpa registra versões, hash e checks de esquema, linhas e intervalos. Hash detecta bytes diferentes, não valida conteúdo.","03_comunicacao":"Título descritivo, eixo 0–1, intervalo e baseline. A legenda informa dados fictícios e a conclusão usa associação ou previsão, não causalidade.","04_compartilhamento":"Tema raro combinado a idade/local cria unicidade. Generalize, restrinja acesso ou forneça sintético; registre direitos e perda analítica.","05_oficina":"Exemplo final: notebook executável, README, dados permitidos/sintéticos, dicionário, proveniência, requisitos, licença, seção de validade e apresentação com caso e limite.","exercicios":"Exemplo da questão 17: dados restritos podem ter protocolo de acesso, código, metadados, esquema e dados sintéticos; reprodução é graduada, não tudo ou nada."}
 for a,t in tx.items():
  ais=[i for i,b in ids if b==a];(p/f"gabarito_{a}.md").write_text(f"# Gabarito — {a}\n\n**Atividades associadas:**\n"+"\n".join(f"- {i}" for i in ais)+f"\n\n## Exemplo de resolução\n\n{t}\n",encoding="utf-8")
 rv=U/"revisores";rv.mkdir(parents=True,exist_ok=True);(rv/"README.md").write_text("# Revisores da Unidade 14\n\nExecute seis pareceres e uma auditoria final.\n",encoding="utf-8")
 for i,t in enumerate(["nível acadêmico","didática","alinhamento","humanidades digitais","referências","técnica e acessibilidade"],1):(rv/f"{i:02d}_{t.replace(' ','_')}.md").write_text(f"# Revisor — {t}\n\nAvalie reprodutibilidade, direitos, comunicação, integração e correções verificáveis.\n",encoding="utf-8")
 (rv/"matriz_de_avaliacao.md").write_text("# Matriz\n\nAvalie argumento, pacote, execução, ética, comunicação e contribuição.\n",encoding="utf-8");(rv/"modelo_de_parecer.md").write_text("# Parecer final\n\n## Evidências\n\n## Correções\n\n## Decisão\n",encoding="utf-8")
def main():
 for p in [U,D,U/"imagens"]:p.mkdir(parents=True,exist_ok=True)
 dados();imgs=[("00_projeto_reprodutivel.svg","Projeto verificável",["Pergunta","Dados","Código","Limites"],"Reprodução e proteção podem coexistir."),("01_documentacao.svg","Papéis documentais",["README","Notebook","Dados","Ambiente"],"Cada artefato responde a uma pergunta."),("02_reproducao.svg","Execução verificável",["Entradas","Ambiente","Código","Checks"],"Reexecutar inclui conferir."),("03_comunicacao.svg","Alegação calibrada",["Resultado","Incerteza","Casos","Linguagem"],"O desenho limita o verbo."),("04_compartilhamento.svg","Acesso responsável",["Risco","Direitos","Transformação","Acesso"],"Aberto quando possível; protegido quando necessário."),("05_fechamento.svg","Fechamento comum",["Problema","Evidência","Validade","Contribuição"],"O mesmo projeto chega à versão final.")]
 for x in imgs:svg(*x)
 salvar("00_guia_da_unidade.ipynb",guia());salvar("01_documentacao_e_versionamento.ipynb",documentacao());salvar("02_execucao_e_verificacoes.ipynb",reproducao());salvar("03_visualizacao_incerteza_e_linguagem.ipynb",comunicacao());salvar("04_protecao_direitos_e_compartilhamento.ipynb",compartilhamento());salvar("05_oficina_projeto_final.ipynb",oficina(),False);extras();(U/"imagens"/"README.md").write_text("# Ilustrações\n\nSVGs autorais e acessíveis.\n",encoding="utf-8");(R/"notes"/"plano_unidade_14.md").write_text("# Plano — Unidade 14\n\nConsolidar documentação, versionamento, execução, checks, comunicação, proteção, direitos, compartilhamento, relatório e apresentação no mesmo projeto cumulativo.\n",encoding="utf-8")
if __name__=="__main__":main()
