# Cronograma docente — Unidade 1, aula 1 (4 horas)

## 1. Escopo da aula

**Duração total:** 4 horas consecutivas, incluindo intervalo de 15 minutos.

**Materiais principais:**

- `00_guia_da_unidade.ipynb`;
- `01_perguntas_e_problemas_computacionais.ipynb`;
- início de `02_representacao_e_operacionalizacao.ipynb`;
- `gabaritos/gabarito_01_perguntas.md`, para consulta docente.

**Leitura prévia sugerida:** ALVES, Daniel. “As Humanidades Digitais como uma
comunidade de práticas dentro do formalismo académico: dos exemplos
internacionais ao caso português”, especialmente introdução e conclusão.

**Resultado esperado ao final:** cada estudante terá registrado:

1. um interesse inicial de pesquisa;
2. uma pergunta delimitada provisória;
3. sua finalidade predominante;
4. sua estrutura analítica inicial;
5. um conceito que ainda precisa ser operacionalizado.

Esta aula não pretende concluir toda a Unidade 1. O corpus, a cadeia de
evidência e a oficina completa serão trabalhados na segunda aula de quatro
horas.

## 2. Preparação do professor

Antes da aula:

- executar os notebooks 00, 01 e 02 desde o início;
- confirmar que Python, Jupyter e `pandas` funcionam nos computadores;
- abrir previamente os três notebooks e o gabarito do Notebook 01;
- preparar uma cópia limpa dos notebooks para demonstração;
- decidir como os estudantes salvarão suas cópias;
- projetar ou escrever no quadro a distinção:
  **pergunta → dados → operação → evidência → interpretação**;
- ter uma alternativa sem computador: atividades em Markdown podem ser
  respondidas em papel ou editor de texto.

## 3. Cronograma detalhado

| Tempo | Duração | Atividade | Material | Resultado observável |
|---|---:|---|---|---|
| 0:00–0:15 | 15 min | Acolhimento, apresentação da disciplina e problema orientador | Notebook 00 | turma compreende a pergunta central da unidade |
| 0:15–0:30 | 15 min | Diagnóstico individual | Notebook 00 | respostas iniciais registradas |
| 0:30–0:45 | 15 min | Discussão em duplas e coleta de exemplos | Notebook 00, “Atividade em dupla” | interesses e expectativas tornam-se visíveis |
| 0:45–1:05 | 20 min | Humanidades Digitais como campo e comunidade de práticas | Notebook 01 e Alves (2016) | estudante distingue campo de simples uso de ferramentas |
| 1:05–1:25 | 20 min | Dados, *capta* e dados situados | Notebook 01 | turma identifica decisões presentes na produção dos dados |
| 1:25–1:45 | 20 min | Finalidade e estrutura analítica da pergunta | Notebook 01 | estudante diferencia as duas dimensões |
| 1:45–2:00 | 15 min | Experimento Python com a tabela de perguntas | Notebook 01 | código executado e saída interpretada |
| 2:00–2:15 | 15 min | **Intervalo** | — | pausa efetiva |
| 2:15–2:40 | 25 min | Atividade guiada de classificação | Notebook 01 | cinco perguntas classificadas com justificativa |
| 2:40–3:00 | 20 min | Correção dialogada e casos limítrofes | Notebook 01 e gabarito | turma reconhece combinações e desenhos híbridos |
| 3:00–3:25 | 25 min | Da questão ampla à pergunta delimitada e tarefa computacional | Notebook 01 | três níveis distinguidos |
| 3:25–3:40 | 15 min | Produção individual da pergunta provisória | Notebook 01 | produto parcial registrado |
| 3:40–3:55 | 15 min | Conceito, indicador, variável e categoria | início do Notebook 02 | conceito problemático identificado |
| 3:55–4:00 | 5 min | Síntese, bilhete de saída e orientação da próxima aula | Notebook 02 | professor recolhe evidência rápida de aprendizagem |

Total: **240 minutos**.

## 4. Condução de cada bloco

### 0:00–0:15 — Abertura

Apresente o problema orientador sem começar pela programação:

> Como representar computacionalmente um fenômeno histórico, social,
> linguístico ou cultural sem reduzir indevidamente sua complexidade?

Explique que Python será usado quando uma operação ajudar a observar ou testar
uma decisão. Formulações, justificativas e interpretações serão escritas em
Markdown.

Evite apresentar todos os conteúdos da disciplina neste momento. Mostre apenas
o percurso da Unidade 1 e o produto esperado.

### 0:15–0:30 — Diagnóstico

Solicite respostas individuais antes da discussão coletiva. O diagnóstico não
deve ser corrigido como prova. Observe especialmente:

- experiência anterior com programação;
- temas e fontes de interesse;
- confusão entre pergunta e ferramenta;
- expectativa de que os dados sejam registros neutros;
- necessidades de acessibilidade ou apoio técnico.

### 0:30–0:45 — Atividade em dupla e plenária breve

Oriente a turma a preencher a seção **“Atividade em dupla — compreender o
interesse do colega”** do Notebook 00. Cada estudante explica seu interesse a
um colega em dois minutos. O colega deve responder:

1. o que parece ser o fenômeno investigado?
2. que fonte poderia guardar traços desse fenômeno?
3. que aspecto permanece amplo ou ambíguo?

Recolha de três a quatro exemplos, sem tentar reformulá-los completamente.

### 0:45–1:25 — Humanidades Digitais e dados situados

Use Alves (2016) para apresentar Humanidades Digitais como comunidade de
práticas, formação e investigação, não como catálogo de ferramentas.

Ao discutir Drucker e Lavin, peça que a turma identifique uma decisão presente
em qualquer base conhecida: seleção, nomeação, categoria, digitalização,
transcrição ou exclusão.

Pergunta de controle:

> Se uma planilha foi recebida pronta, as decisões anteriores desapareceram?

Resposta esperada: não; elas podem apenas ter ficado menos visíveis.

### 1:25–2:00 — Finalidade, estrutura e experimento

Construa no quadro:

| Dimensão | Possibilidades iniciais |
|---|---|
| finalidade predominante | descritiva, explicativa ou preditiva |
| estrutura analítica inicial | sem relação inicial, comparativa ou associativa |

Use o exemplo:

> Os temas dos editoriais diferem entre Capital e Interior?

Classificação orientativa: finalidade descritiva e estrutura comparativa.

Execute as duas células Python do Notebook 01. Antes de cada saída, solicite uma
previsão. Depois, pergunte o que o código fez e o que ele não justificou.

### 2:15–3:00 — Classificação e casos limítrofes

Organize grupos de três. Para cada pergunta, o grupo deve produzir:

- finalidade;
- estrutura;
- justificativa baseada no que a pergunta solicita;
- possível tarefa inicial;
- algo que essa tarefa não responderia.

Na correção, aceite mais de uma estrutura quando houver justificativa coerente.
Não aceite associação ou comparação como prova automática de explicação.

### 3:00–3:40 — Reformulação da pergunta

Modele um exemplo em três níveis:

1. questão humanística ampla;
2. pergunta delimitada;
3. tarefa computacional inicial.

Depois, cada estudante escreve sua própria versão. Circule pela sala e intervenha
com perguntas, sem reescrever pelo estudante:

- qual é o fenômeno?
- onde e quando ele será observado?
- o que constitui uma observação?
- que fonte poderia sustentar a análise?
- o verbo promete descrição, explicação ou predição?
- que estrutura é necessária?
- o que a operação deixará de fora?

### 3:40–3:55 — Entrada na operacionalização

Apresente apenas a distinção inicial:

- conceito: construção teórica;
- indicador: evidência observável escolhida;
- variável: campo usado para registrar valores;
- categoria ou valor: forma assumida por uma observação.

Peça que cada estudante destaque uma expressão conceitualmente carregada em sua
pergunta, como “modernização”, “prestígio”, “violência”, “participação” ou
“centralidade”. Esse termo abrirá a aula seguinte.

### 3:55–4:00 — Bilhete de saída

Cada estudante entrega ou registra três itens:

1. minha pergunta provisória é…;
2. ainda preciso definir…;
3. a principal limitação ou dúvida é…

Use essas respostas para planejar a retomada da segunda aula.

## 5. Perguntas-chave para o professor

Durante a aula, retome estas perguntas:

- qual afirmação a pesquisa pretende fazer?
- sobre quais unidades essa afirmação será feita?
- finalidade e estrutura estão sendo confundidas?
- que decisão humana precede a operação computacional?
- o resultado descreve o fenômeno ou apenas a representação disponível?
- que leitura contextual ainda será necessária?

## 6. Pontos de atenção

### Turma sem experiência em Python

- execute o código primeiro em projeção;
- explique `DataFrame`, coluna, filtro e resultado antes de pedir alterações;
- não avalie memorização de sintaxe;
- permita trabalho em duplas;
- mantenha a atividade principal em Markdown.

### Turma heterogênea

Estudantes mais experientes podem alterar o filtro e prever a saída, mas não
devem transformar a aula em demonstração de técnicas avançadas. Peça que ajudem
na interpretação e explicação da operação.

### Discussão muito longa

Interrompa com uma síntese parcial e registre questões no quadro para retomar.
Não corte a produção individual da pergunta nem o bilhete de saída.

### Problema técnico

Use as tabelas e perguntas projetadas ou impressas. Nenhum objetivo central da
aula depende de o estudante escrever código.

## 7. Ajustes conforme o ritmo

### Se a turma estiver atrasada

Preserve:

1. distinção entre finalidade e estrutura;
2. atividade guiada com pelo menos três perguntas;
3. formulação individual;
4. conceito a operacionalizar;
5. bilhete de saída.

Transfira para estudo orientado:

- duas perguntas restantes da atividade;
- casos limítrofes;
- exploração adicional da tabela em Python.

### Se a turma estiver adiantada

Não avance para estatística. Use o tempo para:

- comparar duas formulações da mesma pergunta;
- identificar mudanças de finalidade;
- discutir fontes plausíveis e suas ausências;
- revisar perguntas em pares;
- iniciar o mapa de operacionalização do Notebook 02.

## 8. Encaminhamento para a aula 2

Solicite antes do próximo encontro:

- revisar a pergunta provisória;
- ler Rodrigues (2020), com atenção às escolhas éticas e metodológicas da base;
- identificar unidade de análise e duas fontes possíveis;
- trazer uma definição acadêmica preliminar do conceito destacado.

A segunda aula deverá concluir operacionalização, corpus, evidência e oficina do
projeto.
