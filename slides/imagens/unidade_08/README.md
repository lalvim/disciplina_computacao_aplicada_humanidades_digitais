# Imagens calculadas dos slides da Unidade 8

Os SVGs deste diretório são gerados por
[`scripts/construir_graficos_slides_unidade_08.py`](../../../scripts/construir_graficos_slides_unidade_08.py)
a partir das bases inteiramente fictícias da unidade. O script requer as mesmas
dependências instaladas pelos notebooks no Colab, incluindo `scikit-learn`.

- `01_concordancia.svg`: acordos, desacordos e kappa;
- `02_divisao_treino_teste.svg`: divisão estratificada e classes;
- `03_comparacao_modelos.svg`: quatro métricas por método;
- `04_matrizes_confusao.svg`: árvore por metadados e modelo textual;
- `05_metricas_periodo.svg`: auditoria descritiva por período;
- `06_termos_modelo.svg`: coeficientes textuais extremos.

Para reproduzir na raiz do repositório, em ambiente com as dependências da unidade:

```bash
python3 scripts/construir_graficos_slides_unidade_08.py
```

Os resultados não descrevem documentos históricos reais.
