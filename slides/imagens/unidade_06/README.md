# Imagens calculadas dos slides da Unidade 6

Os três arquivos SVG deste diretório são gerados por
[`scripts/construir_graficos_slides_unidade_06.py`](../../../scripts/construir_graficos_slides_unidade_06.py)
a partir das bases inteiramente fictícias de `unidade_06/dados/`.

- `01_proporcao_tema_periodo.svg`: proporções por período e denominadores;
- `02_dispersao_estratificada.svg`: extensão, referências e estratificação local;
- `03_rede_coocorrencia.svg`: projeção do grafo de entidades com pesos;

Para reproduzir, execute na raiz do repositório:

```bash
python3 scripts/construir_graficos_slides_unidade_06.py
```

As posições do grafo são fixadas apenas para produzir um desenho estável. Elas
não representam espaço geográfico nem distância histórica.
