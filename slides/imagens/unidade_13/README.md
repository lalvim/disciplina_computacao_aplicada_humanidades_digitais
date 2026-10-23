# Imagens calculadas dos slides da Unidade 13

Os cinco SVGs desta pasta são gerados por
[`scripts/construir_graficos_slides_unidade_13.py`](../../../scripts/construir_graficos_slides_unidade_13.py)
a partir dos dados fictícios de auditoria em `unidade_13/dados/`.

As figuras apresentam:

- comparação entre baseline de maioria e modelo;
- matriz de confusão dos 240 casos;
- sensibilidade a cinco especificações;
- distribuição bootstrap descritiva da acurácia;
- desempenho separado por período e origem.

Para reproduzir em ambiente com as dependências da unidade:

```bash
python3 scripts/construir_graficos_slides_unidade_13.py
```

Os dados foram construídos para produzir diferenças didáticas. Não descrevem
grupos, contextos ou sistemas reais.
