# Diretrizes de formatação e escrita do material didático

## 1. Finalidade

Estas diretrizes orientam a produção dos notebooks da disciplina **Computação
Aplicada a Problemas em Humanidades Digitais**. Seu objetivo é manter uma
distinção clara entre:

- exposição conceitual;
- argumentação e interpretação;
- atividades de escrita;
- demonstrações e experimentos computacionais.

O princípio geral é:

> **Markdown para pensar, argumentar e interpretar; Python para experimentar,
> transformar e observar.**

O fato de o material estar em um Jupyter Notebook não significa que toda
atividade precise ser transformada em código.

## 2. Quando usar células Markdown

Usar Markdown para conteúdos cujo resultado principal seja compreensão,
formulação ou argumentação:

- explicações conceituais;
- contextualização histórica, social, linguística ou cultural;
- definição de termos;
- apresentação de problemas de pesquisa;
- exemplos discursivos;
- instruções de atividades;
- perguntas de reflexão;
- formulação de hipóteses;
- justificativas metodológicas;
- interpretação de resultados;
- descrição de limitações, vieses e questões éticas;
- sínteses e conclusões;
- respostas escritas pelo estudante;
- planejamento do projeto de pesquisa;
- revisão entre pares.

### Modelo para resposta discursiva

```markdown
## Minha pergunta de pesquisa

Escreva aqui.

## Justificativa

Escreva aqui.

## Limitações iniciais

Escreva aqui.
```

Não usar dicionários, listas, `Series` ou `DataFrame` apenas para armazenar
respostas discursivas.

## 3. Quando usar Python

Usar Python quando a execução de uma operação ajudar o estudante a observar,
testar ou comparar algo que não seria igualmente claro apenas com texto.

Situações adequadas:

- carregar dados;
- inspecionar registros;
- selecionar unidades segundo critérios;
- filtrar e ordenar dados;
- transformar valores ou formatos;
- contar ocorrências;
- calcular medidas;
- comparar grupos, períodos, documentos ou diferentes recortes;
- testar operacionalizações alternativas;
- produzir tabelas derivadas dos dados;
- visualizar distribuições e relações;
- processar textos;
- simular consequências de decisões metodológicas;
- avaliar erros, incerteza ou desempenho;
- produzir resultados reprodutíveis.

Toda célula de código deve responder a uma pergunta explícita ou demonstrar uma
operação relevante para os objetivos da unidade.

### Sequência recomendada

1. apresentar a pergunta em Markdown;
2. explicar o que será observado;
3. executar uma operação curta em Python;
4. mostrar o resultado;
5. solicitar sua interpretação em Markdown;
6. discutir o que o resultado não permite concluir.

### Exemplo

```markdown
## O recorte altera a composição do corpus?

Vamos comparar a coleção completa com um corpus limitado a determinado período.
```

```python
corpus_periodo = documentos[documentos["ano"].between(1890, 1895)]

documentos["tema"].value_counts(), corpus_periodo["tema"].value_counts()
```

```markdown
### Interpretação

Que diferenças aparecem? Elas resultam do fenômeno estudado ou dos critérios de
seleção? Escreva aqui.
```

## 4. Quando usar tabelas

### Tabela Markdown

Usar uma tabela Markdown quando seu objetivo for:

- apresentar definições;
- comparar conceitos;
- documentar critérios;
- oferecer um roteiro preenchível;
- organizar uma rubrica;
- descrever um esquema ainda não implementado;
- registrar uma decisão metodológica.

### `DataFrame`

Usar um `DataFrame` quando as linhas representarem observações ou quando a
tabela for efetivamente manipulada por código:

- filtrar registros;
- agrupar categorias;
- calcular valores;
- combinar bases;
- localizar ausências;
- comparar subconjuntos;
- ordenar resultados;
- preparar visualizações.

Não criar um `DataFrame` apenas para exibir uma tabela fixa que poderia ser
escrita diretamente em Markdown.

## 5. Atividades do estudante

Cada atividade deve indicar claramente sua natureza.

### Atividade de escrita

Usar quando o estudante precisar formular, explicar, interpretar ou justificar.
A resposta deve ser registrada em uma célula Markdown.

### Experimento guiado

Oferecer código executável, acompanhado de parâmetros simples que possam ser
alterados. Explicar o que deve ser comparado antes e depois da alteração.

### Exercício de programação

Usar somente quando escrever ou completar código for um objetivo de
aprendizagem da unidade. Informar:

- o problema;
- os dados de entrada;
- o resultado esperado;
- quais elementos o estudante deve implementar;
- critérios de verificação.

Não transformar uma atividade conceitual em exercício de sintaxe.

### Atividade integrada

Combinar uma operação computacional e uma resposta interpretativa:

1. estudante executa ou altera o código;
2. observa a saída;
3. registra em Markdown o que mudou;
4. discute o alcance e os limites do resultado.

## 6. Organização de cada notebook

Sempre que pertinente, seguir esta progressão:

1. título e problema orientador;
2. objetivos de aprendizagem;
3. situação ou exemplo das Humanidades;
4. explicação conceitual;
5. pergunta que motiva o experimento;
6. experimento em Python;
7. interpretação do resultado;
8. atividade guiada;
9. atividade autônoma;
10. reflexão crítica;
11. síntese;
12. produto parcial da unidade.

Nem todo tópico exige código. Células computacionais devem aparecer apenas nos
pontos em que acrescentem valor demonstrativo ou analítico.

## 7. Formatação das células Markdown

- usar um único título de nível 1 (`#`) por notebook;
- usar nível 2 (`##`) para seções principais;
- usar nível 3 (`###`) para exemplos, atividades e subseções;
- preferir parágrafos curtos;
- usar listas quando houver uma enumeração real;
- usar tabelas somente para comparações ou campos recorrentes;
- definir termos técnicos antes de utilizá-los;
- identificar claramente exemplos fictícios;
- destacar avisos importantes sem excesso de negrito;
- evitar blocos muito longos de texto sem subtítulos;
- escrever perguntas de atividade de forma direta;
- usar `Escreva aqui.` para marcar espaços de resposta.

## 8. Formatação e qualidade do código

- manter células curtas e com uma finalidade principal;
- usar nomes de variáveis descritivos, preferencialmente em português;
- comentar decisões, não cada linha óbvia;
- evitar abstrações prematuras;
- introduzir bibliotecas somente quando forem necessárias;
- evitar código que dependa de internet durante a aula;
- evitar efeitos ocultos entre células distantes;
- carregar os dados explicitamente no início do experimento;
- garantir que as células executem na ordem;
- evitar saídas excessivamente longas;
- não ocultar avisos ou erros relevantes;
- não usar código apenas para imprimir textos que pertencem ao Markdown;
- não usar Python como formulário de respostas discursivas.

Quando uma função for apresentada, ela deve ajudar a compreender uma operação
reutilizável, e não apenas encapsular campos ou perguntas.

## 9. Dados e exemplos

- usar dados reais quando houver fonte, licença e contexto adequados;
- identificar a proveniência e as transformações realizadas;
- quando os dados forem fictícios, declará-lo no notebook e nos próprios
  metadados;
- não produzir afirmações históricas ou sociais reais a partir de dados
  didáticos fictícios;
- manter conjuntos iniciais pequenos e transparentes;
- aumentar a complexidade somente quando isso for objetivo da unidade;
- representar ausências, ambiguidades e limitações sempre que possível.

## 10. Resultados e interpretação

Uma saída computacional deve ser acompanhada de orientação interpretativa.
Sempre que pertinente, responder:

1. o que foi calculado ou transformado?
2. sobre quais dados?
3. qual decisão metodológica condicionou o resultado?
4. o que o resultado permite afirmar?
5. o que ele não permite afirmar?
6. que casos precisam ser examinados qualitativamente?

Evitar apresentar uma tabela, medida ou gráfico como conclusão autossuficiente.

## 11. Acessibilidade e progressão

- não pressupor experiência anterior com Python quando ela ainda não tiver sido
  ensinada;
- explicar a sintaxe nova antes de exigir que o estudante a produza;
- manter exemplos executáveis antes de propor modificações;
- separar dificuldade conceitual de dificuldade de programação;
- não avaliar domínio de sintaxe em uma atividade cujo objetivo seja
  interpretação;
- oferecer instruções suficientes para que o estudante recupere o fluxo após um
  erro;
- preferir uma operação simples e interpretável a uma solução sofisticada e
  opaca.

## 12. Validação antes da publicação

Antes de considerar um notebook pronto:

- executar todas as células desde um kernel reiniciado;
- confirmar que os arquivos são encontrados por caminhos relativos;
- verificar que nenhuma resposta discursiva está implementada como formulário
  Python;
- confirmar que todo código tem finalidade experimental ou analítica;
- revisar a correspondência entre objetivo, atividade e produto;
- conferir se resultados possuem interpretação e limites;
- verificar a identificação de dados fictícios;
- revisar ortografia, títulos e hierarquia das seções;
- confirmar que o notebook pode ser utilizado sem acesso à internet, salvo
  quando isso for objetivo explícito;
- remover saídas desnecessárias e informações específicas do ambiente local.

## 13. Regra de decisão rápida

Antes de criar uma célula de código, perguntar:

> O estudante precisa executar uma operação para observar ou testar alguma
> consequência?

- Se **sim**, usar Python e solicitar a interpretação do resultado.
- Se **não**, usar Markdown.

