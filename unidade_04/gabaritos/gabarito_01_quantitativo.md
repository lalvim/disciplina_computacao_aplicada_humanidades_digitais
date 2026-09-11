# Gabarito — Exploração quantitativa

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
- excluir D023 somente por ultrapassar a cerca de Tukey.
