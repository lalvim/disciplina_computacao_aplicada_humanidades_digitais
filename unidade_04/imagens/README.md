# Recursos visuais da Unidade 4

Os recursos visuais desta pasta foram escolhidos por função didática. Diagramas
explicam relações conceituais; gráficos calculados nos notebooks representam os
dados fictícios e permanecem acompanhados de tabelas equivalentes.

## Inventário

| Arquivo | Notebook | Função didática | Produção |
|---|---|---|---|
| `00_abertura_conceitual.png` | 00 | apresentar exploração como movimento entre agregados, documentos e hipóteses | imagem gerada |
| `00_percurso_exploracao.svg` | 00 | antecipar o percurso completo da unidade e seus retornos | SVG autoral |
| `00_camadas_escrita.svg` | 00 | distinguir procedimento, descrição, interpretação, limite e próximo passo | SVG autoral |
| `01_tipos_variaveis.svg` | 01 | relacionar escalas conceituais, operações e gráficos | SVG autoral |
| `02_fluxo_tokenizacao.svg` | 02 | mostrar transformações textuais e possíveis perdas | SVG autoral |
| `02_anatomia_pmi.svg` | 02 | relacionar bigrama, marginais, PMI e cautelas | SVG autoral |
| `03_escolha_grafico.svg` | 03 | orientar a escolha do gráfico pela pergunta e pelas variáveis | SVG autoral |
| `04_ciclo_agregados_casos.svg` | 04 | representar o retorno entre leitura distante e próxima | SVG autoral |
| `04_cadeia_argumento.svg` | 04 | ligar pergunta, tabela, figura, leitura e limite | SVG autoral |

Os SVGs são reconstruídos por `scripts/construir_imagens_unidade_04.py`. Todos
contêm `title`, `desc`, `role="img"` e `aria-labelledby`. Os textos ao redor das
figuras nos notebooks também explicam sua finalidade e seu conteúdo.

## Ilustração conceitual gerada

### `00_abertura_conceitual.png`

- **Finalidade:** abertura visual da Unidade 4.
- **Origem:** gerada em 5 de setembro de 2026 com a ferramenta integrada de
  geração de imagens da OpenAI.
- **Natureza:** ilustração conceitual; não representa documentos, acervos ou
  resultados históricos reais.
- **Alterações posteriores:** nenhuma.
- **Texto alternativo:** registros abstratos conduzem a padrões quantitativos e
  textuais; linhas de proveniência retornam a documentos examinados por uma lupa
  e se abrem em interpretações alternativas.

### Prompt final

```text
Use case: scientific-educational
Asset type: wide conceptual opening illustration for Unit 4 of a master's-level
Jupyter course in Digital Humanities
Primary request: represent exploratory analysis as a careful movement between a
small documented dataset, quantitative and textual patterns, visualizations, and
close reading of individual documents, ending in provisional questions rather
than conclusions
Scene/backdrop: warm cream background with a restrained scholarly workbench;
abstract records and text fragments on the left, text-free visual forms in the
center, and selected source fragments with branching interpretive paths on the
right; fine provenance threads connect all stages
Style/medium: polished editorial illustration with subtle paper and ink texture
plus crisp geometric forms
Color palette: deep navy, muted teal, terracotta, plum and sand on warm cream
Text: no text, letters, numbers, formulas, code, labels, logos or watermark
Constraints: conceptual illustration only; patterns reconnect to source
fragments; no people, fake manuscripts or historical claim
```

## Princípios de uso

- A ilustração de abertura não constitui evidência histórica.
- Diagramas não substituem as explicações textuais.
- Gráficos são reconstruídos a partir de `dados/documentos.csv`.
- Toda figura calculada deve ter título, eixos, unidades, descrição e tabela
  equivalente.
- Cor nunca deve ser o único meio de distinguir grupos ou casos.
- O conjunto fictício foi construído para ensinar procedimentos; suas
  regularidades não sustentam interpretações históricas.
