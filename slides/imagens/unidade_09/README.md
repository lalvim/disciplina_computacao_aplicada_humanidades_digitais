# Imagens calculadas dos slides da Unidade 9

Os SVGs são gerados por
[`scripts/construir_graficos_slides_unidade_09.py`](../../../scripts/construir_graficos_slides_unidade_09.py)
com as mesmas dependências e parâmetros dos notebooks.

- `01_efeito_padronizacao.svg`: mudanças de grupo após padronizar;
- `02_inercia_silhueta.svg`: diagnósticos para diferentes valores de `k`;
- `03_perfis_grupos.svg`: médias padronizadas dos três perfis;
- `04_estabilidade.svg`: ARI em vinte subamostras;
- `05_clusters_textuais.svg`: termos característicos e tamanhos dos grupos;
- `06_evolucao_topicos.svg`: mistura média de tópicos por período.

Para reproduzir em ambiente com as dependências da Unidade 9:

```bash
python3 scripts/construir_graficos_slides_unidade_09.py
```

Os dados e resultados são inteiramente fictícios.
