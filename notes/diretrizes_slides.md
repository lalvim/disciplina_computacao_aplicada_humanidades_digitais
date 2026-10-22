# Diretrizes para os slides da disciplina

## 1. Finalidade

Estas diretrizes orientam a criação das apresentações da disciplina **Computação
Aplicada a Problemas em Humanidades Digitais**. Os slides não devem resumir os
notebooks linha por linha. Sua função é:

- criar uma entrada concreta para o problema;
- tornar relações, processos e decisões visíveis;
- apoiar a explicação oral da pessoa docente;
- preparar o estudante para atividades e experimentos nos notebooks;
- conservar rigor acadêmico sem sobrecarregar a tela.

O princípio central é:

> **Primeiro um caso que produza uma pergunta; depois os conceitos necessários para
> investigá-la; por fim, aplicação, crítica e retorno ao caso.**

## 2. Formato técnico

Os slides serão escritos em Markdown compatível com **Marp**, usando:

- front matter YAML no início do arquivo;
- `---` como separador entre slides;
- um título principal por slide;
- caminhos relativos para imagens locais;
- fórmulas em LaTeX delimitadas por `$...$` ou `$$...$$`;
- comentários HTML para notas da pessoa docente, quando necessários.

Modelo de abertura:

```markdown
---
marp: true
theme: default
paginate: true
math: katex
---

# Unidade 4

## Como conhecer uma base antes de aplicar modelos?
```

Os arquivos serão armazenados em `slides/`, com os nomes:

```text
slides/
├── README.md
├── unidade_01.md
├── unidade_02.md
├── ...
└── unidade_14.md
```

As apresentações devem reutilizar prioritariamente as ilustrações presentes em
`unidade_XX/imagens/`. Novos recursos visuais específicos para apresentação serão
armazenados em `slides/imagens/unidade_XX/`.

## 3. Sequência narrativa obrigatória

Cada apresentação seguirá esta macroestrutura.

### 3.1 Abertura

1. título da unidade e problema orientador;
2. exemplo concreto, situação-problema ou documento;
3. pergunta provocada pelo exemplo;
4. agenda da apresentação;
5. objetivos de aprendizagem em linguagem observável.

O exemplo deve aparecer **antes da exposição teórica**. A agenda pode vir depois do
exemplo, pois assim seus tópicos respondem a uma dúvida já criada.

### 3.2 Desenvolvimento de cada conceito

Cada bloco conceitual seguirá, sempre que pertinente, o ciclo:

1. exemplo ou contraste;
2. pergunta de observação;
3. conceito e definição;
4. representação visual ou fórmula;
5. aplicação a um segundo caso;
6. erro frequente ou limite;
7. pergunta breve para a turma.

Evitar sequências longas de slides apenas conceituais. Depois de dois ou três slides
de explicação, inserir um exemplo, comparação, interpretação de saída ou decisão.

### 3.3 Fechamento

Cada unidade terminará com:

1. síntese do percurso;
2. retorno ao exemplo inicial;
3. implicação para o projeto cumulativo;
4. pergunta ou atividade de saída;
5. um ou mais slides de referências.

O último slide da unidade será sempre **Referências**. Quando a bibliografia não
couber com legibilidade, usar `Referências — 1/2` e `Referências — 2/2`.

## 4. Agenda obrigatória

Toda apresentação terá um slide intitulado `Agenda`. A agenda deverá:

- conter de quatro a sete tópicos;
- refletir a ordem real da apresentação;
- usar verbos ou perguntas, e não apenas nomes isolados;
- indicar atividades ou demonstrações importantes;
- reaparecer de forma reduzida nas transições entre grandes blocos, quando útil.

Exemplo:

```markdown
# Agenda

1. Observar um problema de comparação
2. Distinguir contagem, proporção e taxa
3. Interpretar tendência e incerteza
4. Testar uma decisão com Python
5. Retornar aos casos e discutir limites
```

## 5. Exemplos antes da teoria

O primeiro exemplo deve ser compreensível sem vocabulário técnico e conter uma tensão
real: duas interpretações possíveis, um resultado enganoso, uma categoria ambígua ou
uma decisão com consequências.

Tipos de abertura recomendados:

- dois documentos que parecem semelhantes, mas têm contextos diferentes;
- uma tabela cuja conclusão muda ao trocar o denominador;
- um gráfico com eixo ou agregação problemática;
- uma menção ambígua a pessoa ou lugar;
- uma classificação errada com custo substantivo;
- uma resposta fluente sem apoio na fonte;
- um conjunto de dados que não pode ser compartilhado integralmente.

O slide seguinte deve perguntar o que ainda precisamos saber para interpretar o caso.
Somente depois são introduzidas definições e métodos.

## 6. Ilustrações e gráficos

As ilustrações devem explicar uma relação ou operação. Não serão usadas apenas como
decoração.

Cada apresentação deverá conter, no mínimo:

- uma ilustração do problema inicial;
- um diagrama do percurso metodológico;
- duas aplicações visuais de conceitos;
- um gráfico ou tabela interpretada quando a unidade envolver dados;
- uma ilustração de erro, limite ou consequência;
- um diagrama de fechamento ligado ao projeto.

### Regras visuais

- priorizar SVGs autorais e gráficos produzidos a partir dos dados da unidade;
- apresentar uma relação principal por figura;
- usar texto alternativo significativo;
- manter contraste suficiente e não depender somente de cor;
- rotular eixos, unidades, denominadores e fontes;
- evitar capturas de código ou tabelas muito extensas;
- mostrar documentos históricos existentes apenas com fonte, licença e contexto;
- identificar imagens geradas por IA como ilustração conceitual, nunca como evidência.

Quando uma figura for apresentada, o slide ou a fala deverá responder:

1. o que deve ser observado?
2. o que a figura permite afirmar?
3. o que ela não permite afirmar?

## 7. Fórmulas matemáticas

As fórmulas serão escritas em LaTeX. Toda fórmula deverá ser precedida por uma
pergunta ou exemplo e seguida por interpretação em linguagem natural.

Exemplo:

```markdown
# Como comparar grupos de tamanhos diferentes?

$$
p = \frac{x}{n}
$$

- $x$: número de ocorrências;
- $n$: total de unidades observadas;
- $p$: proporção no grupo.
```

Regras:

- não apresentar símbolos antes de defini-los;
- usar no máximo uma fórmula principal por slide;
- destacar a unidade de cada quantidade;
- mostrar ao menos um exemplo numérico simples;
- evitar derivações algébricas longas;
- reservar fórmulas para relações que realmente ajudam a compreender o método;
- verificar a renderização no Marp/KaTeX e no visualizador Markdown adotado.

## 8. Código nos slides

Código aparecerá somente quando a sintaxe for indispensável para compreender uma
operação. A apresentação deve privilegiar:

- pergunta;
- entrada;
- trecho curto de código;
- saída visível;
- interpretação;
- limite.

Regras:

- no máximo oito linhas de código por slide;
- não reduzir fonte para acomodar células completas;
- destacar apenas a linha decisiva;
- usar pseudocódigo quando a biblioteca não for o objetivo;
- remeter ao notebook para a implementação integral;
- nunca usar código para substituir argumento ou resposta discursiva.

## 9. Texto e legibilidade

- uma ideia principal por slide;
- títulos que expressem a conclusão ou a pergunta;
- preferir frases curtas;
- limitar listas comuns a aproximadamente cinco itens;
- evitar parágrafos extensos;
- definir termos técnicos no primeiro uso;
- manter exemplos fictícios explicitamente identificados;
- reservar detalhes complementares para notas da pessoa docente.

Uma apresentação didática não precisa conter todo o texto falado. Ela precisa oferecer
estrutura suficiente para que a turma acompanhe o raciocínio.

## 10. Interação com a turma

Cada unidade deverá incluir pelo menos:

- uma pergunta de observação sobre o exemplo inicial;
- uma previsão antes de revelar uma saída;
- uma atividade breve de interpretação em dupla;
- uma decisão metodológica com duas alternativas plausíveis;
- uma pergunta de saída relacionada ao projeto cumulativo.

As atividades maiores permanecem nos notebooks. Nos slides, informar:

- objetivo;
- tempo;
- organização da turma;
- produto esperado;
- notebook e identificador correspondente, quando houver.

## 11. Referências

Afirmações conceituais, métodos, tipologias e exemplos acadêmicos deverão ter fonte.

Usar dois níveis de citação:

- citação abreviada no slide relevante, por exemplo `(Gelman, Hill e Vehtari, 2020)`;
- referência bibliográfica completa no último slide da unidade.

Priorizar:

- artigos revisados por pares;
- livros acadêmicos;
- documentação oficial para bibliotecas e padrões técnicos;
- fontes primárias para documentos, normas e dados;
- referências de Humanidades Digitais que conectem técnica e interpretação.

Não preencher o slide de referências com obras que não aparecem ou não sustentam a
apresentação.

## 12. Quantidade e ritmo

Como cada encontro pode ter quatro horas, cada unidade terá aproximadamente **38 a 52
slides**, incluindo:

- 4–6 slides de abertura, exemplo e agenda;
- 22–30 slides de desenvolvimento com exemplos intercalados;
- 4–7 slides de demonstração ou atividade;
- 4–6 slides de crítica, síntese e projeto;
- 1–2 slides de referências.

O número é uma faixa, não uma meta mecânica. Atividades, discussão e demonstrações
devem ocupar parte substantiva da aula.

## 13. Critérios de revisão

Antes de publicar uma apresentação, verificar:

1. o exemplo aparece antes da teoria?
2. a agenda corresponde ao percurso real?
3. há transições claras entre os blocos?
4. cada conceito possui ao menos uma aplicação?
5. as fórmulas renderizam e são interpretadas?
6. as ilustrações são legíveis, necessárias e acessíveis?
7. gráficos informam dados, escala, unidade e fonte?
8. a linguagem distingue descrição, associação, previsão e causalidade?
9. as atividades indicam dinâmica e produto?
10. o fechamento retorna ao exemplo inicial?
11. o projeto cumulativo aparece explicitamente?
12. o último slide contém referências efetivamente utilizadas?

