# Gabarito — inferência

## Exemplo de resolução completa

**Alvo didático:** diferença de médias sob um procedimento hipotético de amostragem.
O bootstrap reamostra dentro de cada grupo com reposição e usa 4.000 repetições. O
intervalo percentil contém os quantis 2,5% e 97,5% das diferenças reamostradas. O teste
de permutação mantém os valores, embaralha os rótulos sob intercambiabilidade e compara
o módulo da diferença observada a 5.000 diferenças nulas.

**Interpretação-modelo:** “O intervalo descreve a incerteza do procedimento assumido;
não contém 95% dos documentos. O valor de p mede incompatibilidade com o modelo nulo,
não a probabilidade de a hipótese ser verdadeira. Como os dados são uma coleção
fictícia de conveniência, o exercício ensina o método e não autoriza generalização
histórica.”

## Critérios

- população-alvo e seleção explícitas;
- estimativa, intervalo, efeito e valor de p separados;
- ao menos duas incertezas não amostrais;
- nenhuma decisão baseada apenas em `0,05`.

## Erros frequentes

“aceitar a nula”, “95% dos dados”, “3% de chance da nula” e “significativo = importante”.
