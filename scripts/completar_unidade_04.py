"""Gera material docente e revisão da Unidade 4."""
from pathlib import Path
U=Path(__file__).resolve().parents[1]/"unidade_04"
def w(p,s): p.parent.mkdir(parents=True,exist_ok=True); p.write_text(s.strip()+"\n",encoding="utf-8")
def main():
 g=U/"gabaritos"
 w(g/"README.md","""# Gabaritos da Unidade 4
Modelos orientam procedimentos; interpretações abertas exigem evidência e limites.

## Índice das atividades e gabaritos

| ID | Atividade | Gabarito |
|---|---|---|
| U04-A01 | Diagnóstico inicial | `gabarito_00_guia.md` |
| U04-A02 | Exploração quantitativa | `gabarito_01_quantitativo.md` |
| U04-A03 | Exploração textual | `gabarito_02_textual.md` |
| U04-A04 | Visualização exploratória | `gabarito_03_visualizacao.md` |
| U04-A05 | Oficina do relatório exploratório | `gabarito_04_oficina.md` |
| U04-A06 | Revisão por pares da oficina | `gabarito_04_oficina.md` |
| U04-A07 | Exercícios de múltipla escolha | `gabarito_exercicios_multipla_escolha.md` |""")
 w(g/"gabarito_00_guia.md","""# Gabarito orientativo — Diagnóstico inicial

**Atividade associada:** `U04-A01`.

## Exemplo de resposta

Espero encontrar diferenças de extensão entre temas. Uma saída que revelaria problema seria uma contagem maior que 24 documentos ou proporções incompatíveis com o denominador declarado. A expectativa é hipótese de trabalho, não conclusão.""")
 w(g/"gabarito_01_quantitativo.md","""# Gabarito — Exploração quantitativa

**Atividade associada:** `U04-A02`.

## Exemplo de resolução

Na variável `palavras`, a soma dos 24 valores é 16.838; portanto, a média é 16.838 ÷ 24 ≈ 701,58 palavras. Depois da ordenação, a mediana é 621,5 palavras. Como todos os valores aparecem uma única vez, não há uma moda informativa. Nesse caso, `Series.mode()` devolve todos os valores: selecionar apenas o primeiro produziria, incorretamente, uma falsa moda única.

As medidas de tendência central respondem onde os valores se concentram. As medidas de dispersão respondem quanto eles se espalham. Neste exemplo, mínimo e máximo são 320 e 2.100, de modo que a amplitude é 1.780 palavras. Com $Q_1=459$ e $Q_3=848,75$, o intervalo interquartil é 389,75 palavras. A variância amostral é aproximadamente 138.786,95 palavras ao quadrado, enquanto o desvio-padrão amostral é 372,54 palavras e retorna à unidade original.

O documento D023 deve ser inspecionado porque ultrapassa o limite superior do critério `Q3 + 1,5 × IQR`. Isso não autoriza sua remoção automática. Uma resposta defensável compara média e mediana, descreve como D023 afeta média, amplitude, variância e desvio-padrão e verifica a proveniência do registro antes de decidir como tratá-lo.

Na tabela de contingência, a resposta deve informar se apresenta contagens ou proporções e declarar o denominador das proporções. Descrição, interpretação e hipótese precisam aparecer separadas.

## Critérios de qualidade

- classificar corretamente as escalas das variáveis;
- distinguir medidas de tendência central de medidas de dispersão;
- reconhecer quando a moda não é informativa;
- declarar denominadores e diferenciar contagens de proporções;
- inspecionar valores extremos sem removê-los automaticamente;
- separar descrição, interpretação e hipótese.

## Erros frequentes

- afirmar que `320` é a moda apenas porque é o primeiro resultado de `Series.mode()`;
- interpretar variância e desvio-padrão como se tivessem a mesma unidade;
- tratar média e mediana como equivalentes diante de valores extremos;
- excluir D023 somente por ultrapassar a cerca de Tukey.""")
 w(g/"gabarito_02_textual.md","""# Gabarito — Exploração textual
**Atividade associada:** `U04-A03`.

Exigir regras de tokenização e normalização, frequências absolutas e relativas, concordâncias, n-gramas e PMI com frequência mínima. Diversidade deve reconhecer o efeito do tamanho; ao menos um agregado precisa retornar ao trecho original.""")
 w(g/"gabarito_03_visualizacao.md","""# Gabarito — Visualização
**Atividade associada:** `U04-A04`.

Barras para categorias; histograma e boxplot para distribuição; dispersão para duas quantitativas; linha para ordem temporal; barras para termos. Toda figura requer tabela equivalente, descrição, escala, interpretação e limite. Nuvem de palavras não substitui valores legíveis.""")
 w(g/"gabarito_04_oficina.md","""# Rubrica — Relatório exploratório
**Atividades associadas:** `U04-A05` e `U04-A06`.

Pontue 0–2: escopo; correção quantitativa; exploração textual; visualização/acessibilidade; retorno aos casos; limites; reprodutibilidade. Aprovação orientativa: 11/14, sem zero em correção ou limites. Hipóteses permanecem provisórias.""")
 letras="B B A B A B A A B A A A A A A A B A".split()
 linhas=["# Gabarito — Múltipla escolha","","**Atividade associada:** `U04-A07`.","","| Questão | Resposta |","|---:|:---:|"]+[f"| {i} | {x} |" for i,x in enumerate(letras,1)]
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
