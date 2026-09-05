# Plano de execução — Unidade 4

**Situação:** executado em 31 de julho de 2026. A primeira rodada dos seis
revisores aprovou a unidade com ajustes baixos de manutenção.

## 1. Escopo

**Unidade:** Como conhecer uma base antes de aplicar modelos?

**Problema orientador:** Como obter uma visão inicial dos padrões, diferenças,
erros e limitações presentes nos dados?

**Carga sugerida:** 12 horas em três encontros. A unidade articula estatística
descritiva, exploração textual e visualização.

**Produto:** Relatório exploratório contendo tabelas, visualizações, leituras de
casos e hipóteses iniciais explicitamente apresentadas como provisórias.

## 2. Objetivos

O estudante deverá ser capaz de:

1. classificar variáveis conforme seu papel e escala;
2. calcular e interpretar frequências, proporções e medidas de centro;
3. usar quartis, variância e desvio-padrão para descrever dispersão;
4. examinar distribuições e valores extremos sem removê-los automaticamente;
5. construir e interpretar tabelas de contingência;
6. tokenizar e normalizar textos com regras documentadas;
7. calcular frequências absolutas e relativas;
8. recuperar concordâncias para retornar do agregado ao contexto;
9. produzir e avaliar n-gramas e colocações;
10. descrever vocabulário e diversidade lexical reconhecendo efeito do tamanho;
11. escolher entre barras, histograma, boxplot, dispersão e série temporal;
12. produzir visualizações textuais acessíveis e substantivamente justificadas;
13. formular hipóteses exploratórias sem confundi-las com testes ou conclusões.

## 3. Notebooks

1. `00_guia_da_unidade.ipynb` — percurso, diagnóstico e princípios;
2. `01_exploracao_quantitativa.ipynb` — variáveis, medidas, distribuições,
   extremos e contingência;
3. `02_exploracao_textual.ipynb` — tokens, frequências, concordâncias, n-gramas,
   colocações e diversidade;
4. `03_visualizacao_exploratoria.ipynb` — seis famílias de gráficos, escolha,
   acessibilidade e crítica;
5. `04_oficina_relatorio_exploratorio.ipynb` — roteiro integrado do produto.

## 4. Estratégia

Python será usado para calcular, reorganizar e visualizar; Markdown será usado
para previsões, interpretação, hipóteses e limites. Cada agregado deverá apontar
de volta para registros ou trechos que permitam leitura próxima.

Os gráficos serão SVG acessível produzido offline por um pequeno módulo didático
incluído na unidade. O objetivo é estudar a gramática das escolhas visuais sem
introduzir uma dependência não disponível no ambiente. O README indicará como
substituí-lo por bibliotecas de visualização em projetos futuros.

O conjunto visual implementado compreende uma ilustração conceitual de abertura,
oito diagramas SVG autorais e sete gráficos calculados com Python. Os diagramas
tratam do percurso exploratório, das camadas da escrita, dos tipos de variáveis,
da tokenização, da PMI, da escolha de gráficos, do retorno aos casos e da cadeia
argumentativa. Os gráficos apresentam distribuição anotada, TTR bruta e
padronizada, barras categóricas, histograma e boxplot, dispersão, série temporal
e frequências textuais.

Todos os recursos ficam em `unidade_04/imagens/`, com inventário, proveniência e
textos alternativos. O módulo `unidade_04/graficos.py` produz SVGs acessíveis com
eixos, escalas e descrições sem introduzir nova dependência gráfica.

As medidas quantitativas e textuais serão apresentadas em três camadas: definição
em linguagem corrente, fórmula em LaTeX e operação correspondente em Python. A
notação será usada apenas quando explicitar numerador, denominador, unidade ou
convenção de cálculo. Frequências, média, mediana, variância, IQR, contingência,
PMI, TTR, intervalos do histograma e médias anuais terão fórmulas; classificação
de variáveis, concordâncias e escolhas gráficas permanecerão prioritariamente
discursivas.

## 5. Limites

- sem intervalos de confiança ou testes de hipótese, reservados à Unidade 5;
- sem TF-IDF, similaridades ou matrizes documento-termo, também da Unidade 5;
- sem inferência causal;
- sem remoção automática de extremos;
- sem nuvem de palavras como substituta de frequências legíveis;
- sem comparar diversidade lexical bruta entre textos de tamanhos muito distintos.

## 6. Execução e aceitação

1. criar dados quantitativos e textuais fictícios ligados por identificador;
2. produzir notebooks e módulo SVG;
3. incluir exercícios, gabaritos e referências;
4. executar seis revisores;
5. validar os 21 conteúdos da ementa, notebooks, gráficos e exercícios textuais;
6. corrigir achados altos ou bloqueantes;
7. marcar o plano como executado.

A unidade estará pronta quando todo código executar offline, as visualizações
tiverem título/descrição e dados tabulares equivalentes, e o relatório distinguir
claramente descrição, interpretação e hipótese.
