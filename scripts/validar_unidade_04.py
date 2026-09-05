"""Valida a Unidade 4."""
import json
import math
import os
import re
import struct
import xml.etree.ElementTree as ET
from pathlib import Path
R=Path(__file__).resolve().parents[1]; U=R/"unidade_04"
def src(c): return "".join(c["source"]) if isinstance(c["source"],list) else c["source"]
def run(p):
 d=json.loads(p.read_text(encoding="utf-8")); env={"__name__":"__main__"}; a=b=0; old=Path.cwd()
 try:
  os.chdir(U)
  for i,x in enumerate(d["cells"],1):
   s=src(x); assert s.strip()
   if x["cell_type"]=="markdown": a+=1
   else: b+=1; assert "Escreva aqui" not in s; exec(compile(s,f"{p.name}:{i}","exec"),env)
 finally: os.chdir(old)
 return a,b,env

def validar_latex(notebooks):
 texto = "\n".join(
  src(c)
  for p in notebooks
  for c in json.loads(p.read_text(encoding="utf-8"))["cells"]
  if c["cell_type"] == "markdown"
 )
 for controle in ["\x08", "\x0c", "\x0b"]:
  assert controle not in texto, "caractere de controle introduzido por LaTeX"
 for p in notebooks:
  for celula in json.loads(p.read_text(encoding="utf-8"))["cells"]:
   if celula["cell_type"] == "markdown":
    conteudo = src(celula)
    assert conteudo.replace("$$", "").count("$") % 2 == 0, (
     f"delimitador LaTeX inline sem par em {p.name}"
    )
 formulas = [
  r"f_k = \sum", r"\bar{x}=\frac", r"\widetilde{x}",
  r"s^2=\frac", r"IQR=Q_3-Q_1", r"L_{\mathrm{inferior}}",
  r"n_{ij}=\sum", r"p_{j\mid i}", r"f(w)=\sum",
  r"PMI(a,b)=", r"TTR(d)=", r"TTR_m(d)=", r"h_j=\sum",
  r"\bar{x}_t=\frac",
 ]
 ausentes = [formula for formula in formulas if formula not in texto]
 assert not ausentes, f"fórmulas LaTeX ausentes: {ausentes}"
 delimitadores = re.findall(r"^\$\$$", texto, re.MULTILINE)
 assert len(delimitadores) == 28
 assert not re.search(r"^\\[\[\]]$", texto, re.MULTILINE)
 assert r"\(" not in texto and r"\)" not in texto

def validar_resultados(ambientes):
 quantitativo = ambientes["01_exploracao_quantitativa.ipynb"]
 resumo = quantitativo["resumo"]
 assert resumo["variancia_amostral"] == quantitativo["x"].var(ddof=1)
 assert quantitativo["limite_inferior"] < quantitativo["limite_superior"]
 assert quantitativo["extremos"]["id_documento"].tolist() == ["D023"]
 somas_linha = quantitativo["proporcoes_por_genero"].sum(axis=1)
 assert all(abs(valor - 1) <= 0.002 for valor in somas_linha)

 textual = ambientes["02_exploracao_textual.ipynb"]
 esperado_bigramas = sum(max(len(tokens) - 1, 0) for tokens in textual["dados"]["tokens"])
 assert textual["total_bigramas"] == esperado_bigramas
 assert sum(textual["marginal_esquerda"].values()) == esperado_bigramas
 assert sum(textual["marginal_direita"].values()) == esperado_bigramas
 assert textual["tamanho_padrao"] == 19
 assert textual["diversidade"]["ttr_19"].notna().all()
 for _, linha in textual["tabela_frequencias"].iterrows():
  assert math.isclose(
   linha["relativa_todos_tokens"], linha["frequencia"] / textual["total_tokens"]
  )
  assert math.isclose(
   linha["relativa_tokens_conteudo"],
   linha["frequencia"] / textual["total_tokens_conteudo"],
  )
 assert {"id_documento", "contexto"}.issubset(
  textual["concordancias"](textual["dados"], "trabalho").columns
 )
 primeira = textual["tabela_colocacoes"].iloc[0]
 a, b = primeira["bigrama"].split()
 esperado_pmi = math.log2(
  primeira["frequencia"] * textual["total_bigramas"]
  / (textual["marginal_esquerda"][a] * textual["marginal_direita"][b])
 )
 assert math.isclose(primeira["pmi"], esperado_pmi)

def validar_oficina():
 caminho = U / "04_oficina_relatorio_exploratorio.ipynb"
 documento = json.loads(caminho.read_text(encoding="utf-8"))
 markdown = "\n".join(
  src(celula) for celula in documento["cells"] if celula["cell_type"] == "markdown"
 )
 secoes = [
  "## O que será produzido",
  "## Como realizar a oficina",
  "## 1. Escopo e qualidade da base",
  "## 2. Perfil quantitativo",
  "## 3. Perfil textual",
  "## 4. Visualizações",
  "## 5. Retorno aos casos",
  "## 6. Hipóteses provisórias",
  "## 7. Limitações e reprodutibilidade",
  "## 8. Estrutura do relatório final",
  "## 9. Dinâmica sugerida e revisão por pares",
  "## 10. Rubrica e checklist de entrega",
 ]
 assert all(secao in markdown for secao in secoes)
 assert markdown.count("Escreva aqui") >= 30
 for termo in [
  "Procedimento:", "Descrição:", "Interpretação:", "Limite:", "Próximo passo:",
  "quatro visualizações", "três casos", "tabela equivalente", "revisão por pares",
 ]:
  assert termo in markdown, f"instrução ausente na oficina: {termo}"

 gabarito = (U / "gabaritos" / "gabarito_04_oficina.md").read_text(encoding="utf-8")
 for termo in [
  "## Exemplo de resolução completa", "701,58", "138.786,95", "1.433,375", "936 tokens",
  "TTR-19", "D023", "D001", "D003", "14/14",
 ]:
  assert termo in gabarito, f"gabarito da oficina incompleto: {termo}"

def validar_imagens():
 pasta=U/"imagens"
 esperados={
  "README.md", "00_abertura_conceitual.png", "00_percurso_exploracao.svg",
  "00_camadas_escrita.svg", "01_tipos_variaveis.svg", "02_fluxo_tokenizacao.svg",
  "02_anatomia_pmi.svg", "03_escolha_grafico.svg", "04_ciclo_agregados_casos.svg",
  "04_cadeia_argumento.svg",
 }
 encontrados={p.name for p in pasta.iterdir() if p.is_file()}
 assert encontrados==esperados, f"inventário visual divergente: {encontrados ^ esperados}"
 ns={"svg":"http://www.w3.org/2000/svg"}
 for caminho in pasta.glob("*.svg"):
  raiz=ET.parse(caminho).getroot()
  titulo=raiz.find("svg:title",ns); descricao=raiz.find("svg:desc",ns)
  assert titulo is not None and (titulo.text or "").strip()
  assert descricao is not None and len((descricao.text or "").split())>=8
  assert raiz.attrib.get("role")=="img" and "aria-labelledby" in raiz.attrib
 png=(pasta/"00_abertura_conceitual.png").read_bytes()
 assert png[:8]==b"\x89PNG\r\n\x1a\n"
 largura,altura=struct.unpack(">II",png[16:24])
 assert largura>=1200 and altura>=500
 ficha=(pasta/"README.md").read_text(encoding="utf-8")
 for nome in esperados-{"README.md"}: assert nome in ficha
 notebooks="\n".join(p.read_text(encoding="utf-8") for p in U.glob("*.ipynb"))
 for nome in esperados-{"README.md"}: assert nome in notebooks

def validar_encadeamento():
 esperados={
  "00_guia_da_unidade.ipynb":[
   "Se explorar significa construir", "A inspeção inicial mostra",
   "A regra de escrita acompanhará",
  ],
  "01_exploracao_quantitativa.ipynb":[
   "O guia definiu que explorar", "A classificação anterior determina",
   "Frequências e proporções resumem", "As medidas anteriores condensam",
   "Até aqui descrevemos uma variável", "A tabela de contingência encerra",
  ],
  "02_exploracao_textual.ipynb":[
   "O Notebook 01 descreveu", "A tokenização transforma",
   "As frequências mostram", "As concordâncias permitem",
   "N-gramas e PMI observam", "A diversidade lexical completa",
  ],
  "03_visualizacao_exploratoria.ipynb":[
   "O mapa anterior relaciona", "As barras anteriores representam",
   "Histograma e boxplot descrevem", "O gráfico de dispersão não exige",
   "Até aqui visualizamos", "As cinco famílias mostraram",
  ],
  "04_oficina_relatorio_exploratorio.ipynb":[
   "A entrega esperada enumera", "A sequência anterior funciona",
   "Com corpus, unidade e qualidade", "O perfil quantitativo descreve",
   "Os perfis quantitativo e textual", "As visualizações tornam",
   "Depois do retorno aos casos", "Uma hipótese exploratória só",
   "Agora já existem resultados", "A estrutura define",
   "O parecer do colega fornece",
  ],
 }
 for nome,marcadores in esperados.items():
  conteudo=(U/nome).read_text(encoding="utf-8")
  ausentes=[marcador for marcador in marcadores if marcador not in conteudo]
  assert not ausentes, f"encadeamentos ausentes em {nome}: {ausentes}"

def main():
 ns=sorted(U.glob("*.ipynb")); assert len(ns)==5; texto=""; tm=tc=0; ambientes={}
 for p in ns:
  a,b,env=run(p); ambientes[p.name]=env; tm+=a;tc+=b; print("OK",p.name,a,b); d=json.loads(p.read_text(encoding="utf-8")); texto+=" ".join(src(x) for x in d["cells"]).lower()
  if p.name=="04_oficina_relatorio_exploratorio.ipynb": assert b==0
 termos=["tipos de variáveis","frequências","mediana","quartis","variância","distribuição","valores extremos","contingência","tokenização","normalização","frequências absoluta e relativa","concordâncias","n-gramas","colocações","vocabulário","diversidade lexical","barras","histograma","boxplot","dispersão","série temporal"]
 assert all(t in texto for t in termos)
 t=(U/"exercicios_unidade_04_texto.md").read_text(encoding="utf-8"); numeros=[int(n) for n in re.findall(r"^## Questão (\d+)",t,re.M)]; assert numeros==list(range(1,19)); assert len(re.findall(r"^- \[ \] \*\*[A-D]\.\*\*",t,re.M))==72
 chave=(U/"gabaritos/gabarito_exercicios_multipla_escolha.md").read_text(encoding="utf-8"); resp=re.findall(r"^\|\s*\d+\s*\|\s*([A-D])",chave,re.M); assert len(resp)==18
 assert len(list((U/"revisores").glob("*.md")))==9 and len(list((U/"revisores/pareceres").glob("*.md")))==7
 validar_latex(ns); validar_resultados(ambientes); validar_oficina(); validar_imagens(); validar_encadeamento()
 print("OK 14 fórmulas LaTeX e resultados quantitativos/textuais")
 print("OK oficina: instruções, dinâmica, rubrica e exemplo resolvido")
 print("OK imagens: 1 abertura e 8 diagramas acessíveis, locais e documentados")
 print("OK encadeamento: transições internas e passagens entre notebooks")
 print("OK 21/21 conteúdos; exercícios textuais, gabaritos e revisão; total",tm,tc)
if __name__=="__main__": main()
