# Plano de execução — Unidade 5

**Situação:** executada em 6 de setembro de 2026. Os seis revisores aprovaram a
unidade, com dois ajustes baixos de manutenção e nenhum achado alto ou
bloqueante. A execução integral confirmou 20/20 conteúdos, 38 células Markdown,
23 células de código, 20 exercícios e 12 recursos visuais.

Este plano segue as
[diretrizes de formatação e escrita do material](diretrizes_formatacao_material.md)
e usa como ponto de partida o relatório exploratório produzido na Unidade 4.

## 1. Escopo

**Unidade:** Como comparar grupos, períodos e documentos?

**Problema orientador:** Como verificar se grupos sociais, instituições,
períodos ou documentos apresentam diferenças relevantes?

**Carga horária sugerida:** 12 horas, distribuídas em três encontros de quatro
horas. A carga se justifica pela presença de dois eixos metodológicos —
comparação quantitativa e comparação textual — e por uma oficina que os integra
sem confundir suas unidades, pressupostos e medidas.

**Produto final:** análise comparativa entre ao menos dois grupos, períodos ou
subconjuntos documentais, contendo pergunta, estimativa da diferença, incerteza
quando pertinente, tamanho de efeito ou medida de similaridade, inspeção dos
casos e interpretação substantiva dos limites.

## 2. Decisões conceituais centrais

A unidade não será organizada como um catálogo de testes e métricas. Toda
comparação deverá explicitar:

1. quais unidades e subconjuntos estão sendo comparados;
2. qual quantidade ou representação responde à pergunta;
3. qual medida define diferença ou semelhança;
4. que pressupostos permitem calcular e interpretar a medida;
5. quanto o resultado muda diante de variabilidade ou de outra escolha métrica;
6. quais registros ou trechos precisam ser relidos;
7. qual afirmação substantiva é sustentada e qual excede os dados.

No eixo quantitativo, a ênfase principal será **estimar e interpretar diferenças**.
Testes de hipótese serão introduzidos como uma forma limitada de avaliar a
compatibilidade dos dados com um modelo nulo, e não como mecanismo automático de
descoberta. Intervalos, valores de *p* e tamanhos de efeito não corrigem amostras
de conveniência, vieses de seleção ou categorias inadequadas.

No eixo textual, “semelhança” será tratada como resultado de uma cadeia de
decisões: unidade textual, tokenização, normalização, representação, ponderação e
métrica. Documentos semelhantes por vocabulário podem divergir em sentido,
posição ou contexto histórico.

## 3. Objetivos de aprendizagem

Ao concluir a unidade, o estudante deverá ser capaz de:

1. formular uma comparação coerente com a pergunta e a unidade de análise;
2. comparar médias, medianas e proporções sem tratar essas medidas como
   intercambiáveis;
3. calcular e interpretar diferenças absolutas e relativas;
4. explicar variabilidade amostral e distingui-la de erro de medição, cobertura
   e variação histórica;
5. construir e interpretar intervalos de confiança introdutórios;
6. explicar hipótese nula, estatística de teste, distribuição de referência e
   valor de *p*;
7. interpretar tamanho de efeito junto à escala original e ao contexto;
8. distinguir significância estatística de relevância substantiva;
9. representar textos por *Bag of Words* e matriz documento-termo;
10. calcular e interpretar pesos TF-IDF;
11. comparar conjuntos de termos por similaridade de Jaccard;
12. comparar vetores documentais por similaridade de cosseno;
13. comparar sequências e versões por distância de edição;
14. selecionar uma medida de similaridade conforme a pergunta;
15. comparar autores, períodos ou coleções sem essencializar grupos;
16. recuperar e inspecionar documentos semelhantes e pares divergentes;
17. realizar leitura próxima dos casos que sustentam ou desafiam o agregado;
18. produzir uma análise comparativa reproduzível e criticamente delimitada.

## 4. Organização dos materiais

```text
unidade_05/
├── 00_guia_da_unidade.ipynb
├── 01_estimativas_e_tamanhos_de_efeito.ipynb
├── 02_incerteza_e_testes_de_hipotese.ipynb
├── 03_representacao_vetorial_de_textos.ipynb
├── 04_similaridade_documentos_e_versoes.ipynb
├── 05_oficina_analise_comparativa.ipynb
├── dados/
│   ├── documentos.csv
│   ├── documentos_comparacao.csv
│   ├── versoes_textuais.csv
│   └── proveniencia.json
├── imagens/
│   └── README.md
├── gabaritos/
│   ├── README.md
│   ├── gabarito_01_estimativas.md
│   ├── gabarito_02_inferencia.md
│   ├── gabarito_03_representacao_textual.md
│   ├── gabarito_04_similaridade.md
│   └── gabarito_05_oficina.md
├── revisores/
├── exercicios_unidade_05_texto.md
├── referencias.md
└── README.md
```

Não serão produzidos exercício em HTML nem script associado, seguindo a decisão
adotada nas unidades anteriores. Os exercícios objetivos permanecerão em
Markdown e os gabaritos conterão explicação e exemplo completo de resolução.

## 5. Conteúdo dos notebooks

### Notebook 00 — Guia da unidade

- retomada do relatório exploratório da Unidade 4;
- distinção entre descrição, comparação, associação e explicação;
- apresentação dos dois eixos da unidade;
- diagnóstico sobre diferença, incerteza e similaridade;
- mapa cumulativo dos produtos;
- explicação do produto final e dos critérios de avaliação;
- alerta inicial sobre população, corpus e possibilidade de generalização.

**Produto:** escolha preliminar de uma comparação quantitativa ou textual e
registro dos pressupostos que ainda precisam ser verificados.

### Notebook 01 — Estimativas e tamanhos de efeito

- pergunta comparativa, unidade, grupos e quantidade de interesse;
- comparação de médias, medianas e proporções;
- diferença absoluta e interpretação na escala original;
- diferença relativa, definição do grupo de referência e problema do
  denominador próximo de zero;
- tamanho de efeito bruto e padronizado;
- distribuição interna dos grupos e sobreposição entre casos;
- contraste entre diferença numérica e relevância humanística;
- experimento em que o mesmo resultado é narrado por medidas diferentes;
- retorno aos documentos extremos e aos casos próximos da fronteira.

**Produto parcial:** quadro de estimativas com medida escolhida, justificativa,
diferença, escala, casos inspecionados e limite interpretativo.

### Notebook 02 — Variabilidade, intervalos e testes de hipótese

- população, amostra, corpus completo e coleção de conveniência;
- o que é variabilidade amostral e o que ela não representa;
- distribuição amostral por simulação transparente;
- erro-padrão como variabilidade de uma estimativa sob um procedimento;
- intervalo de confiança introdutório, com interpretação frequencista cuidadosa;
- *bootstrap* como ferramenta didática e seus pressupostos;
- hipótese nula, estatística de teste e distribuição de referência;
- teste de permutação para diferença entre dois grupos;
- interpretação do valor de *p* sem probabilidade posterior da hipótese;
- tamanho de efeito, intervalo e valor de *p* apresentados em conjunto;
- multiplicidade, decisões analíticas e transparência como alerta introdutório;
- situações em que a inferência amostral não é justificável.

O teste de permutação será preferido como primeira demonstração porque permite
visualizar a lógica da comparação sob a hipótese nula. Testes paramétricos podem
aparecer como extensão comentada, não como lista de receitas.

**Produto parcial:** ficha de comparação inferencial com estimativa, intervalo,
teste introdutório, pressupostos, população-alvo e interpretação substantiva.

### Notebook 03 — *Bag of Words*, matriz documento-termo e TF-IDF

- retomada das regras de tokenização e normalização da Unidade 4;
- documento como unidade e vocabulário como conjunto de atributos;
- *Bag of Words* e a perda deliberada de ordem e contexto;
- construção transparente de uma matriz documento-termo;
- frequência de termo, frequência de documento e frequência inversa;
- TF-IDF e suas convenções possíveis;
- comparação entre contagem bruta e ponderação TF-IDF;
- termos que distinguem documentos, períodos ou subconjuntos;
- efeito de palavras raras, tamanho documental e escolhas de normalização;
- inspeção por concordâncias dos termos que receberam maior peso.

**Produto parcial:** matriz documentada, vocabulário, regra de ponderação e
interpretação de termos distintivos com retorno aos trechos.

### Notebook 04 — Similaridade entre documentos e versões

- semelhança como relação produzida por uma medida;
- Jaccard para conjuntos de termos;
- cosseno para vetores de contagem e TF-IDF;
- distância de edição para sequências e comparação de versões;
- diferença entre similaridade e distância;
- exemplos em que Jaccard e cosseno ordenam documentos de maneira diferente;
- efeito da normalização e da ponderação sobre os vizinhos encontrados;
- comparação entre autores, períodos e coleções;
- identificação dos documentos mais semelhantes;
- comparação de versões, transcrições ou resultados de OCR;
- inspeção qualitativa de falsos semelhantes e falsos diferentes;
- limites de usar proximidade lexical como proximidade histórica ou semântica.

**Produto parcial:** relatório de pares comparados com métrica justificada,
resultado, trechos inspecionados, convergências entre medidas e divergências.

### Notebook 05 — Oficina da análise comparativa

- retomada da pergunta e do relatório exploratório;
- definição dos grupos, períodos ou subconjuntos documentais;
- auditoria da comparabilidade das unidades e da cobertura;
- escolha entre percurso quantitativo, textual ou combinado;
- execução e documentação da medida principal;
- análise de sensibilidade com uma medida ou representação alternativa;
- inspeção de casos e leitura próxima;
- separação entre resultado, interpretação e hipótese explicativa;
- relevância substantiva, incerteza e limites;
- rubrica de autoavaliação;
- revisão por pares com roteiro explícito;
- revisão final e indicação do produto que poderá alimentar a Unidade 6.

**Produto final:** análise comparativa curta, reproduzível e argumentada, com
tabelas ou visualizações acessíveis, código executável e interpretação em
Markdown.

## 6. Fórmulas e notação

As fórmulas serão introduzidas somente quando explicitarem a quantidade
calculada, a convenção adotada ou um pressuposto. Cada fórmula terá definição em
linguagem corrente, exemplo numérico e operação correspondente em Python.

Serão consideradas:

- diferença absoluta, $\Delta = \hat{\theta}_A-\hat{\theta}_B$;
- diferença relativa, com grupo de referência explicitado;
- diferença padronizada entre médias, apresentada junto à diferença bruta;
- intervalo como estimativa acompanhada de limites inferior e superior;
- proporção de permutações tão ou mais extremas que o resultado observado;
- matriz documento-termo, $X_{d,t}$;
- frequência de documento, $df(t)$;
- uma convenção suavizada e explicitamente documentada de IDF;
- peso $tfidf(t,d)=tf(t,d)\times idf(t)$;
- Jaccard, $J(A,B)=|A\cap B|/|A\cup B|$;
- cosseno, $\cos(\mathbf{x},\mathbf{y})=(\mathbf{x}\cdot\mathbf{y})/(\|\mathbf{x}\|\|\mathbf{y}\|)$;
- recorrência da distância de Levenshtein, acompanhada por uma pequena matriz de
  programação dinâmica.

Notação não será usada para ornamentação. A interpretação do intervalo e do
valor de *p* será escrita por extenso e avaliada também em exemplos incorretos.

## 7. Estratégia didática

Será mantido o princípio **Markdown para pensar, argumentar e interpretar;
Python para experimentar, transformar e observar**.

Python será usado para:

- calcular medidas sobre registros reais ou fictícios;
- reamostrar e permutar dados com semente fixa;
- construir matrizes derivadas de documentos;
- calcular pesos, distâncias e similaridades;
- ordenar e recuperar pares de documentos;
- comparar resultados sob escolhas alternativas;
- produzir tabelas e gráficos reproduzíveis.

Markdown será usado para:

- formular a pergunta e justificar os grupos;
- declarar pressupostos e população-alvo;
- prever resultados;
- interpretar estimativas, intervalos, testes e similaridades;
- realizar leitura próxima;
- discutir relevância, limites, categorias e ética;
- registrar revisão por pares.

Cada experimento seguirá a sequência: pergunta → previsão → operação → saída →
interpretação → limite → retorno aos casos. Cada mudança de seção terá uma ponte
que explique o resultado anterior, sua insuficiência e a razão da próxima etapa.
Cada notebook encerrará indicando o produto parcial levado ao seguinte.

## 8. Dados didáticos

O núcleo quantitativo reutilizará, por cópia documentada, os 24 registros
fictícios da Unidade 4. A continuidade permite comparar hipóteses exploratórias
já formuladas sem apresentar um novo domínio a cada unidade. Campos adicionais
só serão criados quando necessários e terão proveniência explícita.

Será acrescentado um conjunto pequeno de versões textuais fictícias, ligado aos
documentos por identificador, para demonstrar distância de edição, alterações de
transcrição e comparação de versões. Os textos não representarão pessoas,
instituições ou acontecimentos reais.

Para evitar rankings triviais produzidos pelas frases repetidas da Unidade 4,
um corpus textual derivado reunirá doze identificadores e acrescentará frases
fictícias controladas por gênero e local, além de uma marca didática por
documento. Texto original e texto derivado permanecerão em colunas separadas, e
a transformação será registrada na proveniência.

Os dados deverão conter:

- ao menos dois períodos e dois subconjuntos comparáveis;
- variáveis numéricas e binárias adequadas a médias, medianas e proporções;
- distribuições com sobreposição e pelo menos um caso influente;
- textos curtos com vocabulário compartilhado e termos distintivos;
- pares lexicalmente próximos com sentidos ou contextos diferentes;
- versões com inserções, exclusões e substituições identificáveis;
- arquivo de proveniência que documente origem, versão e transformações.

Resultados inferenciais sobre esses dados serão apresentados apenas como
experimentos metodológicos. Eles não fundamentarão afirmações históricas reais.

## 9. Recursos visuais previstos

O conjunto visual deverá cumprir função explicativa e permanecer acessível:

1. ilustração conceitual de abertura: duas coleções comparadas por diferentes
   lentes, identificada como gerada e não documental;
2. fluxo da unidade: estimar → quantificar incerteza → representar textos →
   medir similaridade → inspecionar casos → interpretar;
3. diagrama que separa diferença observada, variabilidade e relevância;
4. animação não será necessária; uma sequência estática mostrará reamostragens;
5. distribuição de referência com resultado observado e caudas marcadas;
6. mapa conceitual da interpretação correta de intervalo e valor de *p*;
7. diagrama documento → tokens → vocabulário → matriz documento-termo;
8. mapa de calor acessível da matriz, acompanhado por tabela equivalente;
9. comparação geométrica entre Jaccard e cosseno;
10. matriz de programação dinâmica para distância de edição;
11. diagrama de vizinhos textuais com os pares também listados em tabela;
12. cadeia argumentativa da oficina, com retorno aos documentos.

Fluxos, matrizes conceituais e diagramas serão SVGs autorais. Gráficos resultarão
dos dados e serão gerados por código. Nenhuma captura rasterizada substituirá
tabela ou saída reproduzível. Todos os recursos terão texto alternativo, título,
descrição, explicação no entorno e registro em `imagens/README.md`.

## 10. Cronograma sugerido

### Encontro 1 — 4 horas

1. guia, retomada e diagnóstico — 30 minutos;
2. comparação de médias, medianas e proporções — 55 minutos;
3. diferenças absolutas, relativas e escala — 45 minutos;
4. intervalo da aula — 10 minutos;
5. tamanhos de efeito e inspeção de casos — 55 minutos;
6. atividade integrada e discussão — 45 minutos.

### Encontro 2 — 4 horas

1. variabilidade amostral e possibilidade de inferência — 45 minutos;
2. simulação e *bootstrap* — 55 minutos;
3. intervalo da aula — 10 minutos;
4. intervalo de confiança — 40 minutos;
5. teste de permutação e valor de *p* — 55 minutos;
6. significância, relevância e atividade — 35 minutos.

### Encontro 3 — 4 horas

1. *Bag of Words*, matriz documento-termo e TF-IDF — 55 minutos;
2. Jaccard, cosseno e comparação das escolhas — 50 minutos;
3. intervalo da aula — 10 minutos;
4. distância de edição e comparação de versões — 30 minutos;
5. oficina da análise comparativa — 60 minutos;
6. revisão por pares e fechamento — 35 minutos.

Leituras preparatórias e exercícios complementares não integrarão as doze horas
presenciais. Se a turma precisar de mais apoio em inferência, TF-IDF deverá ser
mantido no núcleo e distância de edição poderá ser transferida para atividade
orientada, sem retirar sua explicação e seu exemplo executável do notebook.

## 11. Referências de partida

### Essenciais

- WASSERSTEIN, Ronald L.; LAZAR, Nicole A. (2016). “The ASA Statement on
  p-Values: Context, Process, and Purpose”. Base para interpretação de valores de
  *p*, transparência e distinção entre significância e importância.
- WASSERSTEIN, Ronald L.; SCHIRM, Allen L.; LAZAR, Nicole A. (2019). “Moving to a
  World Beyond ‘p < 0.05’”. Base para evitar decisões binárias por limiar.
- EFRON, Bradley; TIBSHIRANI, Robert J. (1993). *An Introduction to the
  Bootstrap*. Referência para reamostragem e intervalos.
- MANNING, Christopher D.; RAGHAVAN, Prabhakar; SCHÜTZE, Hinrich (2008).
  *Introduction to Information Retrieval*. Base para matriz documento-termo,
  TF-IDF, modelo vetorial e cosseno.

### Humanidades Digitais e leitura crítica

- DRUCKER, Johanna (2011). “Humanities Approaches to Graphical Display”.
- D'IGNAZIO, Catherine; KLEIN, Lauren F. (2020). *Data Feminism*.
- JOCKERS, Matthew L. (2013). *Macroanalysis: Digital Methods and Literary
  History*.
- UNDERWOOD, Ted (2019). *Distant Horizons: Digital Evidence and Literary
  Change*.

Na execução, dados bibliográficos, DOI, páginas e links foram verificados antes
de entrar em `referencias.md`. As leituras essenciais foram associadas às
seções em que fundamentam uma decisão, não apenas listadas ao final.

## 12. Dependências técnicas

- Python 3;
- `pandas`;
- `numpy`;
- biblioteca padrão: `collections`, `itertools`, `math`, `random` e `re`.

O núcleo não dependerá de `scikit-learn`. Matriz documento-termo, TF-IDF,
Jaccard, cosseno e distância de edição serão implementados de forma pequena e
transparente para tornar as convenções visíveis. Uma extensão poderá mostrar a
equivalência com bibliotecas consolidadas, sem ser necessária para executar o
material offline ou no Colab.

## 13. Limites de escopo

- sem inferência causal;
- sem correlação ou associação entre variáveis, reservadas à Unidade 6;
- sem regressão, reservada à Unidade 7;
- sem classificação supervisionada, reservada à Unidade 8;
- sem agrupamento ou modelagem temática, reservados à Unidade 9;
- sem apresentar valor de *p* como probabilidade de a hipótese nula ser verdadeira;
- sem tratar intervalo de confiança como intervalo que contém um parâmetro com
  determinada probabilidade após o cálculo;
- sem aplicar inferência amostral a um corpus de conveniência sem discutir a
  população e o mecanismo de seleção;
- sem escolher automaticamente média, mediana, proporção ou métrica textual;
- sem interpretar semelhança lexical como equivalência semântica ou histórica;
- sem ocultar pré-processamento, ponderação ou casos divergentes.

## 14. Exercícios, gabaritos e revisão

Os exercícios textuais deverão cobrir os vinte conteúdos da ementa e combinar:

- interpretação de saídas e fórmulas;
- identificação de conclusões indevidas;
- escolha justificada de medida;
- comparação de resultados sob duas especificações;
- leitura de pequenos pares documentais;
- análise crítica de significância e similaridade.

Cada atividade dos notebooks terá gabarito detalhado com pelo menos um exemplo
completo de resolução. Respostas abertas incluirão critérios de qualidade,
alternativas defensáveis e erros frequentes, sem sugerir que existe uma única
interpretação substantiva correta.

Serão criados e executados os seis revisores já adotados no projeto:

1. nível acadêmico de mestrado;
2. didática e carga;
3. alinhamento à ementa, produto e unidades vizinhas;
4. Humanidades Digitais e retorno às fontes;
5. referências e precisão conceitual;
6. execução técnica, acessibilidade e Colab.

O parecer consolidado deverá distinguir correções obrigatórias de expansões
opcionais. Achados altos ou bloqueantes serão corrigidos e submetidos a nova
rodada antes de a unidade ser considerada pronta.

## 15. Etapas de execução

1. aprovar e registrar este plano;
2. verificar referências metodológicas e bibliográficas;
3. copiar e documentar os dados da Unidade 4;
4. criar o conjunto de versões textuais e a proveniência;
5. construir os seis notebooks com encadeamento explícito;
6. produzir fórmulas, tabelas, gráficos e diagramas acessíveis;
7. criar exercícios textuais e gabaritos com exemplos;
8. criar README e links de abertura no Colab;
9. criar e executar os seis revisores;
10. implementar achados altos ou bloqueantes;
11. executar todos os notebooks em ordem e com estado limpo;
12. validar cobertura, referências, dados, fórmulas, imagens e acessibilidade;
13. atualizar o README principal com a Unidade 5;
14. marcar o plano como executado somente após a validação final.

## 16. Critérios de conclusão

A unidade estará pronta quando:

- os vinte conteúdos previstos estiverem ensinados e aplicados;
- estimativa, incerteza, teste e relevância forem conceitualmente diferenciados;
- a possibilidade de generalização estiver ligada ao desenho dos dados;
- cada medida quantitativa e textual tiver pergunta, fórmula, código e limite;
- os resultados retornarem a registros ou trechos para inspeção;
- ao menos um experimento mostrar que outra medida altera a conclusão;
- todo código executar offline, com sementes reprodutíveis quando houver acaso;
- notebooks, exercícios e gabaritos forem consistentes;
- imagens e gráficos tiverem alternativa textual e proveniência;
- a oficina produzir uma análise comparativa completa;
- os revisores não registrarem achados altos ou bloqueantes;
- o produto preparar a passagem da comparação para relações na Unidade 6.
