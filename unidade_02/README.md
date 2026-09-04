# Unidade 2 — Construção e documentação da base

Material teórico-prático da segunda unidade de **Computação Aplicada a
Problemas em Humanidades Digitais**.

## Ordem de estudo

1. `00_guia_da_unidade.ipynb`
2. `01_fontes_populacao_e_selecao.ipynb`
3. `02_cobertura_vieses_e_silencios.ipynb`
4. `03_metadados_identificadores_e_proveniencia.ipynb`
5. `04_oficina_protocolo_da_base.ipynb`
6. `exercicios_unidade_02.html`
7. `referencias.md`

## Abrir os notebooks no Google Colab

| Material | Arquivo | Google Colab |
|---|---|---|
| Guia da unidade | [`00_guia_da_unidade.ipynb`](00_guia_da_unidade.ipynb) | [Abrir no Colab](https://colab.research.google.com/github/lalvim/disciplina_computacao_aplicada_humanidades_digitais/blob/main/unidade_02/00_guia_da_unidade.ipynb) |
| Fontes, população e seleção | [`01_fontes_populacao_e_selecao.ipynb`](01_fontes_populacao_e_selecao.ipynb) | [Abrir no Colab](https://colab.research.google.com/github/lalvim/disciplina_computacao_aplicada_humanidades_digitais/blob/main/unidade_02/01_fontes_populacao_e_selecao.ipynb) |
| Cobertura, vieses e silêncios | [`02_cobertura_vieses_e_silencios.ipynb`](02_cobertura_vieses_e_silencios.ipynb) | [Abrir no Colab](https://colab.research.google.com/github/lalvim/disciplina_computacao_aplicada_humanidades_digitais/blob/main/unidade_02/02_cobertura_vieses_e_silencios.ipynb) |
| Metadados, identificadores e proveniência | [`03_metadados_identificadores_e_proveniencia.ipynb`](03_metadados_identificadores_e_proveniencia.ipynb) | [Abrir no Colab](https://colab.research.google.com/github/lalvim/disciplina_computacao_aplicada_humanidades_digitais/blob/main/unidade_02/03_metadados_identificadores_e_proveniencia.ipynb) |
| Oficina do protocolo | [`04_oficina_protocolo_da_base.ipynb`](04_oficina_protocolo_da_base.ipynb) | [Abrir no Colab](https://colab.research.google.com/github/lalvim/disciplina_computacao_aplicada_humanidades_digitais/blob/main/unidade_02/04_oficina_protocolo_da_base.ipynb) |

O link carrega o notebook diretamente do GitHub. Nos Notebooks 00 a 03,
execute primeiro a célula **Preparação do ambiente**; ela clona o
repositório no ambiente temporário e posiciona a execução nesta unidade. O
Notebook 04 é discursivo e não precisa de clonagem.

## Dependências e dados

Requer Python 3 e pandas. Os exemplos funcionam offline. Todos os registros
em `dados/` são fictícios e contêm lacunas deliberadas; não sustentam
afirmações sobre instituições ou processos históricos reais.

A pasta `imagens/` reúne uma abertura conceitual e sete diagramas acessíveis.
Os arquivos são locais, funcionam offline e têm finalidade, proveniência e
textos alternativos documentados em `imagens/README.md`.

## Carga sugerida

Duas semanas, oito horas no total, incluindo preparação e revisão. A oficina
produz o protocolo da base do projeto iniciado na Unidade 1.

O arquivo `exercicios_unidade_02.html` contém 18 questões com correção e
funciona offline. Há uma versão textual equivalente.

## Material do docente e revisão

`gabaritos/` reúne respostas-modelo e rubricas. `revisores/` define seis
perspectivas de avaliação e contém os pareceres executados. Os modelos das
atividades abertas orientam a correção, mas não constituem respostas únicas.

## Limite de escopo

A unidade diagnostica problemas de formato, valores e duplicatas, mas não
ensina sua correção. Limpeza, padronização e integração pertencem à Unidade 3.

## Execução

A partir da raiz:

```bash
jupyter lab unidade_02
```

Execute as células na ordem. Respostas e justificativas pertencem às células
Markdown; Python é usado apenas para experimentos e auditorias.
