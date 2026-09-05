# Unidade 3 — Transformação de fontes em dados analisáveis

## Ordem

1. `00_guia_da_unidade.ipynb`
2. `01_formatos_importacao_e_extracao.ipynb`
3. `02_estrutura_limpeza_e_qualidade.ipynb`
4. `03_juncoes_integracao_e_reprodutibilidade.ipynb`
5. `04_oficina_base_processavel.ipynb`
6. `exercicios_unidade_03_texto.md`

## Abrir os notebooks no Google Colab

| Material | Arquivo | Google Colab |
|---|---|---|
| Guia da unidade | [`00_guia_da_unidade.ipynb`](00_guia_da_unidade.ipynb) | [Abrir no Colab](https://colab.research.google.com/github/lalvim/disciplina_computacao_aplicada_humanidades_digitais/blob/main/unidade_03/00_guia_da_unidade.ipynb) |
| Formatos, importação e extração | [`01_formatos_importacao_e_extracao.ipynb`](01_formatos_importacao_e_extracao.ipynb) | [Abrir no Colab](https://colab.research.google.com/github/lalvim/disciplina_computacao_aplicada_humanidades_digitais/blob/main/unidade_03/01_formatos_importacao_e_extracao.ipynb) |
| Estrutura, limpeza e qualidade | [`02_estrutura_limpeza_e_qualidade.ipynb`](02_estrutura_limpeza_e_qualidade.ipynb) | [Abrir no Colab](https://colab.research.google.com/github/lalvim/disciplina_computacao_aplicada_humanidades_digitais/blob/main/unidade_03/02_estrutura_limpeza_e_qualidade.ipynb) |
| Junções, integração e reprodutibilidade | [`03_juncoes_integracao_e_reprodutibilidade.ipynb`](03_juncoes_integracao_e_reprodutibilidade.ipynb) | [Abrir no Colab](https://colab.research.google.com/github/lalvim/disciplina_computacao_aplicada_humanidades_digitais/blob/main/unidade_03/03_juncoes_integracao_e_reprodutibilidade.ipynb) |
| Oficina da base processável | [`04_oficina_base_processavel.ipynb`](04_oficina_base_processavel.ipynb) | [Abrir no Colab](https://colab.research.google.com/github/lalvim/disciplina_computacao_aplicada_humanidades_digitais/blob/main/unidade_03/04_oficina_base_processavel.ipynb) |

O link carrega o notebook diretamente do GitHub. Nos Notebooks 00 a 03,
execute primeiro a célula **Preparação do ambiente**. Ela clona o
repositório, posiciona a execução nesta unidade e instala apenas alguma
dependência ausente. O Notebook 04 é discursivo e não precisa de clonagem.

## Dados e dependências

Dados fictícios e um extrato didático documentado do IBGE ficam separados em
`brutos`, `intermediarios` e `derivados`. Requer Python 3, pandas, openpyxl,
pypdf e Pillow. Tesseract é opcional; há saída pré-computada para execução
offline sem o programa. `imagens/` reúne a ilustração de abertura e sete
diagramas SVG acessíveis; as duas imagens sintéticas de OCR ficam em `dados/brutos`
porque são entradas do experimento, não apenas elementos decorativos.

Nunca edite os dados brutos. Reconstrua intermediários e derivados executando os
notebooks em ordem. As análises substantivas começam na Unidade 4.

`exercicios_unidade_03_texto.md` contém 18 questões de múltipla escolha.
`gabaritos/` reúne respostas-modelo e rubrica; `revisores/` contém
seis roteiros e seus pareceres executados.
