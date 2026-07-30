# Plano de ajuste — Finalidades e estruturas das perguntas

## 1. Problema identificado

O Notebook 01 apresenta cinco categorias equivalentes:

1. descritiva;
2. comparativa;
3. associativa;
4. explicativa;
5. preditiva.

Essa lista funciona como recurso didático inicial, mas reúne dimensões
diferentes:

- **descrição, explicação e predição** expressam finalidades da investigação;
- **comparação e associação** expressam estruturas usadas para organizar a
  análise.

Uma investigação pode, por exemplo, ter finalidade descritiva e estrutura
comparativa. Outra pode buscar explicação a partir de comparações e associações.
As categorias, portanto, não são mutuamente exclusivas nem ocupam
necessariamente o mesmo nível lógico.

## 2. Decisão conceitual proposta

Substituir “cinco tipos de pergunta” por um modelo de duas dimensões.

### Dimensão A — Finalidade predominante

- **Descritiva:** caracteriza ocorrências, distribuições, mudanças ou padrões.
- **Explicativa:** investiga mecanismos, condições ou processos relacionados a
  um resultado.
- **Preditiva:** estima um resultado desconhecido em novos casos ou
  observações.

### Dimensão B — Estrutura analítica

- **Comparativa:** confronta grupos, períodos, documentos, versões ou
  contextos.
- **Associativa:** investiga como duas ou mais características variam em
  conjunto.
- **Sem estrutura relacional inicial:** caracteriza um conjunto sem comparação
  ou associação explícita.

Uma mesma pergunta poderá receber uma finalidade e uma ou mais estruturas.

## 3. Fundamentação

A distinção entre explicação e predição deverá ser sustentada por:

SHMUELI, Galit. To Explain or to Predict? *Statistical Science*, v. 25, n. 3,
p. 289–310, 2010. https://doi.org/10.1214/10-STS330.

A implementação deverá acrescentar uma referência metodológica verificável que
trate de perguntas descritivas, comparativas e relacionais. A fonte precisa ser
consultada diretamente antes de ser incluída; não deverá ser usada apenas porque
uma lista de categorias parece semelhante.

O material apresentará o modelo de duas dimensões como uma **organização
didática adotada pela disciplina**, não como taxonomia universal.

## 4. Alterações por arquivo

### `notes/contexto_disciplina.md`

- reformular o conteúdo da Unidade 1;
- substituir “perguntas descritivas, comparativas, associativas, explicativas e
  preditivas” por “finalidades descritivas, explicativas e preditivas; estruturas
  comparativas e associativas”;
- verificar ocorrência semelhante nos objetivos específicos.

### `notes/plano_unidade_01.md`

- atualizar o objetivo de aprendizagem;
- substituir “tipos” por “finalidades e estruturas”;
- ajustar a descrição do Notebook 01.

### `00_guia_da_unidade.ipynb`

- substituir “distinguir cinco tipos” por:
  “distinguir finalidade e estrutura de uma pergunta de pesquisa”.

### `01_perguntas_e_problemas_computacionais.ipynb`

- renomear o item 2;
- explicar as duas dimensões;
- informar que elas podem ser combinadas;
- substituir a coluna `tipo` por `finalidade` e `estrutura`;
- manter o experimento de filtragem, agora com finalidade explícita;
- acrescentar uma matriz de exemplos;
- revisar a atividade guiada e os casos limítrofes;
- solicitar justificativa separada para finalidade e estrutura.

### `04_oficina_projeto_de_pesquisa.ipynb`

- substituir “tipo predominante” por:
  - finalidade predominante;
  - estrutura analítica inicial;
  - justificativa e possíveis etapas secundárias.

### `exercicios_unidade_01.html`

- reescrever as questões 3 e 4;
- avaliar a distinção entre finalidade e estrutura;
- evitar perguntar se uma questão é “predominantemente comparativa”;
- regenerar a versão textual.

### `gabaritos/`

- atualizar `gabarito_01_perguntas.md`;
- atualizar `gabarito_04_oficina.md`;
- atualizar as respostas e justificativas do múltipla escolha;
- preservar exemplos de desenhos híbridos.

### `referencias.md`

- acrescentar Shmueli (2010);
- incluir a referência metodológica adicional depois de verificação;
- indicar qual aspecto cada obra sustenta.

### `scripts/`

- atualizar o gerador dos notebooks;
- atualizar as palavras verificadas em `validar_unidade_01.py`;
- fazer o validador rejeitar a expressão “cinco tipos de pergunta”;
- verificar presença de `finalidade` e `estrutura` no Notebook 01 e na oficina;
- regenerar a versão textual do quiz.

### `revisores/`

- registrar o achado e sua resolução;
- atualizar as matrizes que ainda tratam as cinco categorias como uma taxonomia
  única;
- executar novamente os revisores de nível acadêmico, didática, alinhamento e
  referências.

## 5. Sequência de execução

1. confirmar e verificar as referências metodológicas;
2. atualizar a proposta e o plano;
3. alterar o gerador dos notebooks;
4. reconstruir os cinco notebooks;
5. atualizar o HTML e regenerar sua versão textual;
6. atualizar gabaritos;
7. atualizar validações automáticas;
8. executar todos os notebooks;
9. conferir correspondência entre HTML, versão textual e gabarito;
10. executar nova rodada dos quatro revisores afetados.

## 6. Critérios de aceitação

O ajuste estará concluído quando:

- nenhuma parte do material apresentar as cinco categorias como mutuamente
  exclusivas e equivalentes;
- o estudante puder atribuir finalidade e estrutura separadamente;
- exemplos combinarem corretamente as duas dimensões;
- a distinção explicação–predição possuir referência acadêmica;
- comparação e associação não forem apresentadas como evidência causal;
- notebook, oficina, quiz e gabaritos utilizarem a mesma terminologia;
- todos os notebooks executarem sem erros;
- a versão textual reproduzir as questões atualizadas;
- os revisores não identificarem inconsistência conceitual entre proposta,
  atividade e avaliação.

## 7. Fora do escopo

Este ajuste não introduzirá testes estatísticos, regressão ou modelos
preditivos. Esses métodos pertencem a unidades posteriores. Aqui serão
trabalhadas somente as finalidades das perguntas e suas consequências para o
desenho da pesquisa.

