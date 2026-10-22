# Gabarito da oficina

**Atividades associadas:**

- U07-A06 — Oficina — incremento do relatório-notebook
- U07-A07 — Revisão por pares — afirmação, evidência e limite

## Exemplo de incremento do relatório-notebook

**Pergunta:** a extensão de um documento está associada ao número de instituições
mencionadas quando gênero e período são considerados?  
**Unidade:** documento. **Resposta:** contagem de instituições. **Explicativas:**
extensão, gênero e período.  
**Decisão:** como a resposta é contagem pequena, uma regressão linear seria apenas
aproximação exploratória; registro esse limite e comparo previstos com resíduos.

O notebook mostra código de preparação, fórmula conceitual, tabela de coeficientes,
gráfico observado-previsto e três documentos com maiores resíduos. A conclusão diz
“associação condicionada”, explica a escala de 100 palavras e propõe um modelo de
contagem como desenvolvimento futuro.

**Exemplo de não adoção:** com apenas nove cartas comparáveis, não ajustei modelo
múltiplo. Mantive uma tabela de casos e expliquei que poucos graus de liberdade e
ausência de sobreposição tornariam os coeficientes instáveis.

## Exemplo de revisão por pares

- Ponto claro: unidade e resposta aparecem antes do código.
- Dúvida: o gráfico não informa se o período foi mantido constante.
- Prioridade: acrescentar legenda com variáveis condicionantes e inspecionar D017.
- Decisão do autor: aceitei; refiz a legenda e acrescentei uma nota sobre D017.
