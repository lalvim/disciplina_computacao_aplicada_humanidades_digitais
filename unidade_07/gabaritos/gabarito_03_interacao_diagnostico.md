# Gabarito — interação e diagnóstico

**Atividade associada:** U07-A04 — Atividade — interação e diagnóstico

## Exemplo de resolução

No modelo, a inclinação de urbanização é $\beta_1+\beta_3E_c$. Portanto, as curvas de
8, 10 e 12 anos podem ter inclinações diferentes. Comparei previsões ao longo da
faixa observada em vez de interpretar apenas o sinal de $\beta_3$.

A tabela de resíduos leva a M150, com resíduo próximo de 4,043. Conferi a linha no CSV
e li `proveniencia.json`, que declara alteração deliberada. Mantive o modelo completo
como principal ($R^2=0{,}314$; RMSE $=0{,}639$) e apresentei a versão sem M150 como
sensibilidade ($R^2=0{,}372$; RMSE $=0{,}547$). O coeficiente de interação passa de
aproximadamente 0,003 para 0,004.

**Resposta-modelo:** “A heterogeneidade sugerida pelo modelo deve ser lida como
associação contextual. O resultado é parcialmente sensível ao caso didático M150;
ambas as especificações são apresentadas, e nenhuma identifica efeito causal.”
