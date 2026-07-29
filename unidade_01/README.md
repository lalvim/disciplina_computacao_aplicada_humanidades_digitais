# Unidade 1 — Questões das Humanidades e problemas computacionais

Esta pasta contém o material teórico-prático da primeira unidade da disciplina
**Computação Aplicada a Problemas em Humanidades Digitais**.

## Ordem de estudo

1. `00_guia_da_unidade.ipynb`
2. `01_perguntas_e_problemas_computacionais.ipynb`
3. `02_representacao_e_operacionalizacao.ipynb`
4. `03_dados_corpus_e_evidencias.ipynb`
5. `04_oficina_projeto_de_pesquisa.ipynb`
6. `exercicios_unidade_01.html`

## Dependências

- Python 3
- pandas
- JupyterLab, Jupyter Notebook ou VS Code com extensão Jupyter

Os exemplos não dependem de acesso à internet. Os dados da pasta `dados` são
fictícios e foram criados exclusivamente para fins didáticos; não devem ser
utilizados para produzir afirmações históricas.

O arquivo `exercicios_unidade_01.html` contém 18 questões de múltipla escolha
com correção, explicações e revisão por tópico. Ele pode ser aberto diretamente
em um navegador e funciona sem servidor ou acesso à internet.

## Material do docente

A pasta `gabaritos` contém respostas objetivas, respostas-modelo e rubricas.
Como grande parte da unidade envolve formulação e interpretação, os modelos das
atividades abertas são referências de coerência, não respostas únicas.

A pasta separa organizacionalmente o material, mas não restringe o acesso de
quem possui o repositório.

## Revisão antes da oferta

A pasta `revisores` define uma banca de revisão com seis especialidades:
nível acadêmico, didática, alinhamento, Humanidades Digitais, referências e
qualidade técnica/acessibilidade. Ela também contém matriz de avaliação e modelo
de parecer.

Uma unidade sem referências acadêmicas verificáveis deve ser classificada como
necessitando revisão obrigatória antes da oferta em nível de mestrado.

## Execução

A partir da raiz do repositório:

```bash
python3 -m pip install -r requirements.txt
jupyter lab unidade_01
```

Também é possível abrir os arquivos individualmente no VS Code. Execute as
células na ordem. Nas atividades de escrita, entre no modo de edição das células
Markdown e substitua `Escreva aqui` por suas respostas. As células Python são
experimentos: execute-as, altere os parâmetros quando solicitado e interprete
os resultados no texto.

## Produto da unidade

O último notebook conduz à formulação inicial da pergunta de pesquisa, incluindo
unidade de análise, corpus, operacionalização, evidências esperadas e limites.
