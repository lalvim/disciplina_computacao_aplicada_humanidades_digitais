# Gabarito — oficina comparativa

## U05-A06 — Exemplo de análise completa da oficina

**Pergunta:** na coleção fictícia, documentos de Capital e Interior diferem em extensão
simulada, e essa leitura resiste ao caso D023?

**Unidade e cobertura:** documento; 24 registros; coleção de conveniência, sem
generalização populacional.

**Especificação:** diferença de médias, acompanhada por mediana, distribuição, `d`,
intervalo bootstrap didático e teste de permutação. A ordem é Capital menos Interior.

**Sensibilidade:** recalcular sem D023. Se magnitude ou direção mudar, declarar que a
leitura depende do caso influente, sem apagá-lo da base.

**Casos:** D023 como influente, um documento próximo da mediana de cada grupo e seus
textos/metadados.

**Conclusão-modelo:** “A diferença calculada descreve a extensão simulada nesta coleção.
A sensibilidade a D023 e a origem não probabilística impedem transformar intervalo e
valor de p em evidência sobre toda a imprensa. Os casos mostram que `palavras` não mede
intensidade temática.”

## Autoavaliação — exemplo

21/21 quando todos os sete critérios recebem 3, desde que a justificativa acompanhe a
pontuação. Uma nota alta não substitui correção conceitual.

## U05-A07 — Revisão por pares — exemplo

**Parecer:** “Explique por que média é principal e acrescente a mediana; limite a
conclusão à coleção.” **Mudança:** incluir mediana, análise sem D023 e reformular o
sujeito da conclusão.

## Alternativa textual defensável

Comparar dois períodos com cosseno TF-IDF, usar Jaccard como sensibilidade e reler um
par estável e um divergente. A conclusão deve tratar proximidade lexical, não igualdade
histórica ou semântica.
