# Gabarito — regressão múltipla e categorias

**Atividade associada:** U07-A03 — Atividade — controle e referência

## Exemplo de resolução

Comparei a inclinação de renda: aproximadamente 0,0014 no modelo simples e 0,0011 no
múltiplo. O $R^2$ passou de 0,412 para 0,551 e o RMSE de 0,591 para 0,517. A mudança
revela que a associação simples agregava diferenças correlatas;
não autoriza escolher o resultado “mais bonito”. O coeficiente de escolaridade é a
mudança prevista para um ano adicional entre casos iguais nos demais termos.

Centro-Oeste é a referência alfabética. Seus casos continuam no ajuste e formam o
ponto zero dos contrastes regionais. O coeficiente de `regiao_Sudeste` é cerca de
0,346: compara Sudeste a Centro-Oeste condicionando às variáveis numéricas. Os perfis
A e B têm previsões de 3,23 e 4,45; a diferença modelada é 1,22 equipamento por 100
mil, sem que o contraste seja chamado de intervenção.

**Resposta-modelo:** “O modelo descreve diferenças condicionadas entre perfis
observados. A interpretação depende de haver sobreposição entre esses perfis e não
elimina variáveis omitidas ou problemas de mensuração.”
