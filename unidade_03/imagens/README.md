# Imagens da Unidade 3

As imagens foram selecionadas por função didática. Os diagramas explicam relações
que seriam mais difíceis de acompanhar apenas em prosa; tabelas e resultados de
código permanecem nos notebooks, onde podem ser examinados e reproduzidos.

## Inventário e função

| Arquivo | Notebook | Função didática | Produção |
|---|---|---|---|
| `00_abertura_conceitual.png` | 00 | apresentar transformação, preservação e proveniência como um mesmo fluxo | imagem gerada |
| `00_percurso_unidade.svg` | 00 | antecipar as quatro etapas e o retorno provocado pela auditoria | SVG autoral |
| `01_pdf_texto_imagem_ocr.svg` | 01 | distinguir extração de camada textual e OCR | SVG autoral |
| `02_largo_longo.svg` | 02 | tornar visível a mudança da unidade da linha | SVG autoral |
| `02_transformacao_rastreavel.svg` | 02 | relacionar original, regra, derivado, precisão, log e teste | SVG autoral |
| `03_cardinalidades.svg` | 03 | comparar relações 1:1, 1:N e N:N | SVG autoral |
| `03_modelo_relacional_base.svg` | 03 | mostrar a organização da base em tabelas ligadas por chaves | SVG autoral |
| `04_pacote_processavel.svg` | 04 | sintetizar os componentes da entrega final | SVG autoral |

Os SVGs são reconstruídos por `scripts/construir_imagens_unidade_03.py`. Todos
incluem `title`, `desc`, `role="img"` e `aria-labelledby`; os notebooks também
fornecem texto alternativo e interpretação no entorno da figura.

As imagens `pagina_digitalizada.png` e `pagina_digitalizada_degradada.png` não
aparecem neste diretório: são entradas sintéticas do experimento de OCR e ficam em
`dados/brutos`. Elas são produzidas de modo reprodutível por
`scripts/construir_unidade_03.py` e não representam documentos históricos reais.

## Ilustração de abertura

A abertura foi gerada com o recurso de geração de imagens do Codex e depois
inspecionada. Prompt usado:

> Create a wide 3:1 editorial illustration for a graduate-level Digital Humanities
> teaching unit about transforming sources into analyzable data. Show an abstract,
> elegant workflow from left to right: varied source forms such as paper sheets, a
> bound volume, a photographic page, a spreadsheet grid and a small structured
> record enter a layered transparent workbench; the untouched originals remain
> visibly preserved in a side archive; carefully transformed tables, linked records
> and text segments emerge on the right. Thin provenance threads connect every
> derivative back to its source, with subtle checkpoints suggesting validation and
> human judgment. No people. No readable text, letters, numbers, logos, fake
> historical documents, computer code, dashboards, binary rain, or decorative
> clutter. Scholarly editorial illustration, tactile paper and ink textures combined
> with restrained geometric forms, warm cream background, deep navy, muted teal,
> terracotta, plum and sand accents, high visual clarity, generous negative space,
> refined museum-catalog aesthetic, cohesive with accessible academic diagrams.
> Landscape, 1800x600 composition.

O arquivo final tem 2172 × 724 pixels. Ele é conceitual: não deve ser citado como
fonte, evidência histórica ou representação literal de um acervo.
