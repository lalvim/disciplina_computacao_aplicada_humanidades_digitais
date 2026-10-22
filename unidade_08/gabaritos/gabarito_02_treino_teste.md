# Gabarito — treino e teste

**Atividade associada:** U08-A03 — Atividade — proteger o teste

A divisão estratificada com semente 42 produz 120 casos de treino e 40 de teste, com
20 casos por classe no teste. O baseline escolhe “não relevante” no empate: tem
acurácia 0,50, mas precisão, revocação e F1 iguais a zero para “relevante”. Isso mostra
por que acurácia isolada pode ocultar a falha completa na classe de interesse.
Escolher outra semente por melhorar o resultado vazaria informação da
avaliação para a decisão; preservo a divisão pré-registrada.
