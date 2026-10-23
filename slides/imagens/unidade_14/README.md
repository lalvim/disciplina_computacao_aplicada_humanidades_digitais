# Imagens calculadas dos slides da Unidade 14

Os cinco SVGs desta pasta são gerados por
[`scripts/construir_graficos_slides_unidade_14.py`](../../../scripts/construir_graficos_slides_unidade_14.py)
a partir dos dados fictícios em `unidade_14/dados/`.

As figuras apresentam:

- manifesto de artefatos e níveis de acesso;
- verificações de execução e hash do arquivo de resultados;
- estimativas acompanhadas por intervalos;
- comparação entre escala completa e eixo truncado;
- risco didático de combinações raras após remoção de nomes.

Para reproduzir:

```bash
python3 scripts/construir_graficos_slides_unidade_14.py
```

Os registros e resultados são inteiramente fictícios. A figura de combinações
raras ensina um risco; não constitui avaliação de anonimização de dados reais.
