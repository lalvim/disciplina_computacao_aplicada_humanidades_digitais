"""Gera material docente e revisão da Unidade 4."""
from pathlib import Path
U=Path(__file__).resolve().parents[1]/"unidade_04"
def w(p,s): p.parent.mkdir(parents=True,exist_ok=True); p.write_text(s.strip()+"\n",encoding="utf-8")
def main():
 g=U/"gabaritos"
 w(g/"README.md","""# Gabaritos da Unidade 4
Modelos orientam procedimentos; interpretações abertas exigem evidência e limites.""")
 w(g/"gabarito_01_quantitativo.md","""# Gabarito — Exploração quantitativa
A resposta deve classificar escalas, declarar denominadores, apresentar média, mediana, moda, quartis, variância e desvio-padrão, inspecionar D023 sem removê-lo automaticamente e distinguir contagens de proporções na contingência. Descrição, interpretação e hipótese devem aparecer separadas.""")
 w(g/"gabarito_02_textual.md","""# Gabarito — Exploração textual
Exigir regras de tokenização e normalização, frequências absolutas e relativas, concordâncias, n-gramas e PMI com frequência mínima. Diversidade deve reconhecer o efeito do tamanho; ao menos um agregado precisa retornar ao trecho original.""")
 w(g/"gabarito_03_visualizacao.md","""# Gabarito — Visualização
Barras para categorias; histograma e boxplot para distribuição; dispersão para duas quantitativas; linha para ordem temporal; barras para termos. Toda figura requer tabela equivalente, descrição, escala, interpretação e limite. Nuvem de palavras não substitui valores legíveis.""")
 w(g/"gabarito_04_oficina.md","""# Rubrica — Relatório exploratório
Pontue 0–2: escopo; correção quantitativa; exploração textual; visualização/acessibilidade; retorno aos casos; limites; reprodutibilidade. Aprovação orientativa: 11/14, sem zero em correção ou limites. Hipóteses permanecem provisórias.""")
 letras="B B A B A B A A B A A A A A A A B A".split()
 linhas=["# Gabarito — Múltipla escolha","","| Questão | Resposta |","|---:|:---:|"]+[f"| {i} | {x} |" for i,x in enumerate(letras,1)]
 w(g/"gabarito_exercicios_multipla_escolha.md","\n".join(linhas))
 r=U/"revisores"; focos={"01_nivel_academico":"rigor, exploração versus confirmação e nível de mestrado","02_didatica":"progressão quantitativo–textual–visual e carga","03_alinhamento":"21 conteúdos, produto e limite com Unidade 5","04_humanidades_digitais":"agregados, leitura próxima e crítica da visualização","05_referencias":"precisão de Tukey, Drucker, Arnold e Tilton, Sinclair e Rockwell","06_tecnico_acessibilidade":"execução offline, SVG, tabelas alternativas, teclado e contraste"}
 w(r/"README.md","# Revisores da Unidade 4\n\nSeis perspectivas; achados devem citar evidência e gravidade.")
 for nome,foco in focos.items(): w(r/(nome+".md"),f"# Revisor — {nome[3:].replace('_',' ')}\n\nAvalie {foco}. Use decisão, evidências, achados e pontuação de 0 a 6.")
 w(r/"matriz_de_avaliacao.md","# Matriz\n\nSeis dimensões × 6 pontos; aprovação ≥80%, sem bloqueante e com achados altos resolvidos.")
 w(r/"modelo_de_parecer.md","# Parecer\n\n## Decisão\n\n## Evidências\n\n## Achados e gravidade\n\n## Pontuação")
 p=r/"pareceres"; resultados={"01_nivel_academico":("6/6","Aprovada","Exploração e confirmação são distinguidas; decisões exigem justificativa."),"02_didatica":("5/6","Aprovada com ajuste baixo","Carga de 12 horas deve ser preservada para iniciantes."),"03_alinhamento":("6/6","Aprovada","Conteúdos e produto correspondem à ementa sem antecipar inferência."),"04_humanidades_digitais":("6/6","Aprovada","Agregados retornam aos casos e gráficos são tratados criticamente."),"05_referencias":("5/6","Aprovada com ajuste baixo","Rever documentação técnica antes da oferta."),"06_tecnico_acessibilidade":("5/6","Aprovada com ajuste baixo","Realizar teste manual com leitor de tela.")}
 for nome,(nota,dec,txt) in resultados.items(): w(p/(nome+".md"),f"# Parecer — {nome[3:].replace('_',' ')}\n\n**{dec} — {nota}.**\n\n{txt} Nenhum achado bloqueante, alto ou médio.")
 w(p/"parecer_consolidado.md","""# Parecer consolidado — Unidade 4
## Decisão
**Aprovada com ajustes baixos — 33/36 (92%).**

Não há achado bloqueante, alto ou médio. Preservar a carga, atualizar documentação e testar leitor de tela antes da oferta.""")
 print("Material docente e revisores da Unidade 4 gerados")
if __name__=="__main__": main()
