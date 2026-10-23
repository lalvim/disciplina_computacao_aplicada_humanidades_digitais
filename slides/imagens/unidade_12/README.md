# Imagens calculadas dos slides da Unidade 12

Os cinco SVGs desta pasta são produzidos por
[`scripts/construir_graficos_slides_unidade_12.py`](../../../scripts/construir_graficos_slides_unidade_12.py)
a partir do corpus e das saídas hipotéticas em `unidade_12/dados/`.

As figuras apresentam:

- rankings gerados por TF-IDF e por uma projeção SVD local;
- uma analogia didática de atenção como combinação ponderada;
- recuperação para pergunta respondível e pergunta ausente;
- auditoria das seis saídas simuladas;
- fluxo de decisão sobre privacidade, minimização e envio.

Para reproduzir em ambiente com as dependências da unidade:

```bash
python3 scripts/construir_graficos_slides_unidade_12.py
```

Nenhuma figura representa ou avalia um serviço real. Corpus, respostas, pessoas
e instituições são inteiramente fictícios.
