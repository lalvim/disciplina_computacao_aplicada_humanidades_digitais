# Imagens calculadas dos slides da Unidade 7

Os SVGs deste diretório são gerados por
[`scripts/construir_graficos_slides_unidade_07.py`](../../../scripts/construir_graficos_slides_unidade_07.py)
a partir da base inteiramente fictícia `unidade_07/dados/municipios_culturais.csv`.

- `01_regressao_simples.svg`: observações, reta estimada e caso M150;
- `02_interacao.svg`: previsões por urbanização em três níveis de escolaridade;
- `03_diagnostico_residuos.svg`: resíduos e destaque do caso M150;
- `04_curva_logistica.svg`: probabilidades previstas por urbanização.
- `05_padronizacao.svg`: transformação da renda para unidades de desvio-padrão.

Para reproduzir, execute na raiz do repositório:

```bash
python3 scripts/construir_graficos_slides_unidade_07.py
```

As figuras são recursos didáticos, não evidência sobre municípios ou políticas
culturais reais.
