# Plano de execução — Unidade 1

Este plano segue as
[diretrizes de formatação e escrita do material](diretrizes_formatacao_material.md).

## 1. Escopo

**Unidade:** Como transformar uma questão das Humanidades em um problema computacional?

**Problema orientador:** Como representar computacionalmente um fenômeno histórico, social, linguístico ou cultural sem reduzir indevidamente sua complexidade?

**Carga horária sugerida:** 8 horas, distribuídas em duas semanas.

**Produto da unidade:** Formulação inicial da pergunta de pesquisa do projeto da disciplina.

## 2. Objetivos de aprendizagem

Ao concluir a unidade, o estudante deverá ser capaz de:

1. reconhecer possibilidades e limites da pesquisa orientada por dados em Humanidades Digitais;
2. diferenciar perguntas descritivas, comparativas, associativas, explicativas e preditivas;
3. transformar uma questão humanística ampla em uma pergunta observável e computacionalmente tratável;
4. distinguir conceito teórico, indicador, variável e categoria;
5. definir unidade de análise, população, amostra e corpus;
6. reconhecer dados estruturados, semiestruturados e não estruturados;
7. relacionar documentos e metadados;
8. interpretar resultados computacionais como evidências parciais e contextualizadas;
9. explicitar perdas, vieses e limites decorrentes da quantificação e da automação.

## 3. Organização dos materiais

```text
unidade_01/
├── 00_guia_da_unidade.ipynb
├── 01_perguntas_e_problemas_computacionais.ipynb
├── 02_representacao_e_operacionalizacao.ipynb
├── 03_dados_corpus_e_evidencias.ipynb
├── 04_oficina_projeto_de_pesquisa.ipynb
├── README.md
└── dados/
    ├── documentos_exemplo.csv
    ├── metadados_exemplo.json
    └── texto_exemplo.txt
```

## 4. Conteúdo dos notebooks

### Notebook 00 — Guia da unidade

- problema orientador e objetivos;
- percurso de aprendizagem;
- apresentação do estudo de caso;
- instruções para executar os notebooks;
- diagnóstico inicial;
- apresentação do produto final e dos critérios de avaliação.

### Notebook 01 — Perguntas e problemas computacionais

- Humanidades Digitais e pesquisa orientada por dados;
- perguntas descritivas, comparativas, associativas, explicativas e preditivas;
- diferença entre pergunta humanística, pergunta de pesquisa e tarefa computacional;
- organização de exemplos em uma pequena base;
- filtragem e contagem de tipos de pergunta com Python;
- reformulação progressiva de uma questão ampla.

**Produto parcial:** três versões progressivamente mais tratáveis de uma pergunta.

### Notebook 02 — Representação e operacionalização

- conceitos teóricos e operacionalização;
- unidade de análise;
- variáveis, categorias, documentos e metadados;
- relação entre conceito, indicador e representação;
- criação e inspeção de uma pequena tabela;
- comparação de operacionalizações alternativas;
- discussão das perdas introduzidas por cada escolha.

**Produto parcial:** mapa de operacionalização da pesquisa.

### Notebook 03 — Dados, corpus e evidências

- população, amostra e corpus;
- critérios de inclusão e exclusão;
- dados estruturados, semiestruturados e não estruturados;
- leitura de CSV, JSON e TXT;
- relação entre documentos e metadados;
- delimitação de corpora com critérios explícitos;
- demonstração de como escolhas diferentes alteram os resultados;
- evidência computacional e interpretação humanística;
- limites da quantificação e da automação.

**Produto parcial:** ficha de delimitação do corpus e avaliação de suas limitações.

### Notebook 04 — Oficina do projeto de pesquisa

- roteiro integralmente preenchível em células Markdown;
- definição do fenômeno e do contexto;
- formulação e revisão da pergunta;
- identificação do tipo de pergunta;
- definição da unidade de análise;
- delimitação da população, amostra ou corpus;
- operacionalização de conceitos;
- especificação de documentos, variáveis e metadados;
- indicação de possíveis fontes;
- descrição das evidências esperadas;
- registro de vieses, limites e questões éticas;
- autoavaliação por meio de uma rubrica.

**Produto final:** formulação inicial documentada da pergunta do projeto da disciplina.

## 5. Estratégia didática

Os notebooks seguirão uma estrutura recorrente:

1. situação-problema;
2. explicação conceitual;
3. exemplo em Humanidades;
4. experimento em Python, quando houver dados a manipular ou comparar;
5. interpretação da saída;
6. atividade guiada;
7. atividade autônoma;
8. reflexão crítica;
9. síntese e produto parcial.

Será adotado o princípio **Markdown para pensar, argumentar e interpretar;
Python para experimentar, transformar e observar**. Respostas discursivas,
justificativas e a proposta de pesquisa serão escritas em células Markdown. O
código será introdutório, comentado e executável célula por célula, aparecendo
somente quando uma operação sobre dados tornar uma decisão ou consequência
observável. A programação não será usada como formulário e os resultados
computacionais não serão tratados como interpretações autossuficientes.

## 6. Cronograma sugerido

### Semana 1 — 4 horas

1. apresentação, diagnóstico e Notebook 00 — 40 minutos;
2. Notebook 01 — 1 hora e 30 minutos;
3. Notebook 02 — 1 hora e 30 minutos;
4. síntese e registro dos produtos parciais — 20 minutos.

### Semana 2 — 4 horas

1. retomada — 20 minutos;
2. Notebook 03 — 1 hora e 40 minutos;
3. Notebook 04 — 1 hora e 30 minutos;
4. discussão entre pares e revisão — 30 minutos.

## 7. Dependências técnicas

- Python 3;
- JupyterLab, Jupyter Notebook ou VS Code com suporte a notebooks;
- `pandas`.

Visualização, processamento de linguagem, estatística e aprendizado de máquina
serão introduzidos nas unidades posteriores, quando essas ferramentas forem
necessárias para responder às perguntas propostas.

## 8. Etapas de execução

1. registrar este plano;
2. criar a estrutura de diretórios da unidade;
3. produzir dados didáticos pequenos, transparentes e contextualizados;
4. redigir os conteúdos conceituais em células Markdown;
5. implementar em Python somente os experimentos com dados;
6. incluir exercícios guiados e autônomos, usando Markdown para respostas
   discursivas;
7. criar a oficina preenchível do projeto;
8. preparar instruções de uso;
9. executar todos os notebooks em sequência;
10. revisar cobertura da ementa, clareza, acessibilidade e carga de trabalho.

## 9. Critérios de conclusão

A unidade será considerada pronta quando:

- os nove tópicos previstos na ementa estiverem contemplados;
- cada conceito central possuir exemplo situado nas Humanidades;
- os elementos representáveis tiverem demonstração em Python;
- todos os notebooks executarem sem erros e em ordem;
- os exercícios forem compatíveis com estudantes sem pré-requisitos;
- houver distinção clara entre resultado computacional e interpretação;
- o estudante concluir a unidade com pergunta delimitada, unidade de análise e proposta inicial de dados;
- os limites, vieses e implicações éticas forem explicitamente discutidos.
