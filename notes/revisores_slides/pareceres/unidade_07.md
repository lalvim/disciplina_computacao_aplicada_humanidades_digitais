# Parecer consolidado dos slides — Unidade 7

## Identificação

- **Unidade:** 7 — Modelos de associação condicionada
- **Apresentação:** `slides/unidade_07.md`
- **Data da revisão:** 31 de outubro de 2026
- **Personas aplicadas:** encadeamento narrativo; mediação matemática; edição visual;
  rigor acadêmico; direção de aula
- **Materiais consultados:** diretrizes de slides, plano da Unidade 7, apresentação,
  README da unidade, dados fictícios e ilustrações citadas

## Decisão

- [x] aprovada com ajustes aplicados
- [ ] aprovada sem ajustes
- [ ] revisão obrigatória

A apresentação possui rigor conceitual, exemplos numéricos e gabaritos adequados. O
principal risco estava nas mudanças de bloco: vários tópicos eram corretos
isoladamente, mas a razão da passagem dependia da fala improvisada. As pontes foram
incorporadas aos divisores e aos fechamentos dos blocos. A carga das atividades
também foi reorganizada em recorte de aula e versão completa no notebook.

## Mapa narrativo revisado

| Bloco | O que retoma | Pergunta ainda aberta | O que acrescenta |
|---|---|---|---|
| abertura | associação estudada na Unidade 6 | por que o número muda entre modelos? | coeficiente pertence a uma especificação |
| regressão simples | resposta e explicativa | como resumir uma associação numérica? | reta, inclinação, resíduos, ajuste e limites |
| regressão múltipla | limites da renda isolada | o que muda ao considerar outras diferenças? | condicionamento, categorias, referência e perfis |
| interação e diagnóstico | modelo com vários termos | a inclinação é igual em todo contexto e para todo caso? | interação, resíduos, influência e sensibilidade |
| regressão logística | lógica de condicionamento | como modelar uma ocorrência sim/não? | probabilidade, chance, logito, OR e padronização |
| oficina | duas famílias de modelos | como transformar saída em argumento? | pertinência, especificação, diagnóstico e limite |
| fechamento | problema inicial | qual frase os dados sustentam? | síntese e incremento do projeto cumulativo |

## Achados e tratamento

### S7-001 — Divisores nomeavam tópicos, mas não justificavam as passagens

- **Gravidade:** alta.
- **Local:** slides 12, 25, 37, 49 e 64.
- **Evidência:** subtítulos anteriores repetiam “regressão simples”, “regressão
  múltipla”, “interação” e “regressão logística” sem recuperar a lacuna anterior.
- **Consequência:** a turma poderia perceber técnicas sucessivas, não um argumento
  cumulativo.
- **Ação aplicada:** divisores agora indicam a operação lógica: ler uma associação,
  comparar perfis, testar inclinações contextuais, mudar o tipo de resposta e reunir
  os elos do argumento.
- **Verificação:** os títulos, lidos em sequência, reconstroem o avanço da unidade.

### S7-002 — Quatro transições internas dependiam de explicação improvisada

- **Gravidade:** média.
- **Local:** gabaritos U07-A01, U07-A02, U07-A03 e U07-A05; slides sobre variável
  omitida e previsões da interação.
- **Evidência:** faltavam pontes entre afirmação e regressão; simples e múltipla;
  explicativas numéricas e categorias; modelo múltiplo e interação; interação e
  diagnóstico; resposta contínua e binária; modelos e oficina.
- **Consequência:** estudantes iniciantes poderiam não perceber qual insuficiência
  motivava o tópico seguinte.
- **Ação aplicada:** inseridas frases com **resultado alcançado → limite → próximo
  passo**.
- **Verificação:** cada bloco responde a uma pergunta explicitamente deixada pelo
  bloco anterior.

### S7-003 — Escolaridade era usada depois sem aparecer na primeira amostra

- **Gravidade:** média.
- **Local:** slide “Arquivos da simulação municipal”.
- **Evidência:** a variável aparecia nos modelos e gráficos, mas não na tabela inicial.
- **Consequência:** o exemplo de interação parecia introduzir uma coluna externa à
  base apresentada.
- **Ação aplicada:** adicionada `escolaridade (anos)` com valores dos três casos;
  unidades de renda e equipamentos também foram explicitadas.
- **Verificação:** todas as explicativas centrais são apresentadas antes do uso.

### S7-004 — Tempos integrais das atividades inviabilizavam o encontro

- **Gravidade:** alta.
- **Local:** U07-A01 a U07-A07 e atividade de saída.
- **Evidência:** as versões completas somavam 230 minutos, sem exposição, gabaritos,
  transições ou intervalo.
- **Consequência:** a pessoa docente teria de omitir conteúdo ou acelerar sem aviso.
- **Ação aplicada:** cada atividade passou a distinguir **recorte em aula** e **versão
  completa no notebook/projeto**. A oficina é iniciada em aula e concluída no mesmo
  relatório-notebook cumulativo.
- **Verificação:** o roteiro docente apresenta cronograma de 240 minutos, incluindo
  intervalo e fechamento.

### S7-005 — A apresentação é mais extensa que a faixa editorial

- **Gravidade:** média, risco aceito com controle.
- **Local:** apresentação completa, 82 slides.
- **Evidência:** a diretriz sugere 38–52 slides; a unidade possui muitas fórmulas,
  exemplos resolvidos e gabaritos.
- **Consequência:** tentar comentar todas as telas com a mesma profundidade é inviável.
- **Tratamento:** o roteiro classifica telas como essenciais, aprofundamento ou apoio
  à atividade e indica quais fórmulas devem receber mais tempo. Referências não são
  lidas em aula.
- **Condição:** em nova redução editorial, preservar exemplos e pontes; cortar
  duplicações ou transferir aprofundamentos para o notebook.

### S7-006 — O resíduo de M150 misturava duas especificações

- **Gravidade:** alta.
- **Local:** slide “Resíduo devolve a reta ao caso” e gabarito U07-A02.
- **Evidência:** o bloco simples atribuía a M150 o resíduo 4,043, que pertence ao
  modelo de interação; no modelo simples, a previsão é 5,225 e o resíduo é 3,175.
- **Consequência:** o exemplo ensinava a fórmula corretamente, mas substituía números
  de outro modelo, contrariando a tese de que resultados pertencem à especificação.
- **Ação aplicada:** o cálculo do bloco simples foi corrigido para
  $8{,}40-5{,}225\approx3{,}175$; o valor 4,043 permaneceu apenas no diagnóstico do
  modelo de interação.
- **Verificação:** cálculo reproduzido diretamente de `municipios_culturais.csv` e dos
  coeficientes da regressão simples.

## Pontos fortes

1. O mesmo problema e a mesma base atravessam modelos, diagnósticos e oficina.
2. Fórmulas possuem tradução, exemplo numérico e representação visual.
3. A linguagem diferencia associação condicionada de causalidade.
4. Categorias de referência, padronização e razão de chances recebem tratamento
   adequado a público iniciante.
5. Todas as atividades possuem gabarito imediatamente posterior.
6. A proveniência de M150 conecta diagnóstico estatístico à crítica do dado.

## Viabilidade do encontro de quatro horas

| Faixa | Conteúdo | Duração |
|---|---|---:|
| 00:00–00:38 | orientação, base, problema e U07-A01 | 38 min |
| 00:38–01:10 | regressão simples e recorte U07-A02 | 32 min |
| 01:10–01:42 | regressão múltipla e recorte U07-A03 | 32 min |
| 01:42–01:52 | intervalo | 10 min |
| 01:52–02:22 | interação, diagnóstico e U07-A04 | 30 min |
| 02:22–02:52 | logística e U07-A05 | 30 min |
| 02:52–03:37 | oficina U07-A06 | 45 min |
| 03:37–03:52 | revisão U07-A07 | 15 min |
| 03:52–04:00 | retorno, síntese e saída | 8 min |

O cronograma é uma rota principal, não autorização para leitura acelerada. Se a turma
precisar de mais tempo nas fórmulas, os aprofundamentos assinalados no roteiro devem
ser encaminhados ao notebook.

## Conclusão

A Unidade 7 está pronta para uso com o roteiro docente. A nova rodada deve observar,
durante a aplicação, se 30 minutos são suficientes para o bloco logístico e se a
oficina iniciada em aula recebe continuidade efetiva no projeto. Esses dados orientarão
uma eventual redução do número de slides.
