# Gabarito orientativo — Junções e integração

A junção municipal é `many_to_one`: vários documentos podem referenciar um
município, enquanto cada código ocorre uma vez na referência. O número de linhas
deve permanecer oito e não deve haver código sem correspondência no exemplo.

A saída recomendada mantém três tabelas:

- documentos processáveis, uma linha por registro;
- documento–tema, uma linha por relação;
- indicadores longos, uma linha por documento, tema e período.

Uma resposta adequada explicita cardinalidade, verifica contagens antes/depois,
preserva não correspondências e mantém chaves entre textos, metadados e fontes.
