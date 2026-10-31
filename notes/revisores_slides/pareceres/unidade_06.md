# Parecer consolidado dos slides — Unidade 6

## Identificação

- **Unidade:** 6 — Associações e grafos
- **Apresentação:** `slides/unidade_06.md`
- **Data da revisão:** 31 de outubro de 2026
- **Personas aplicadas:** encadeamento narrativo; mediação matemática; edição visual;
  rigor acadêmico; direção de aula
- **Materiais consultados:** diretrizes de slides, plano e README da unidade,
  apresentação, dados fictícios, notebooks, gabaritos e ilustrações citadas

## Decisão

- [x] aprovada com ajustes aplicados
- [ ] aprovada sem ajustes
- [ ] revisão obrigatória

A unidade constrói uma progressão intelectualmente forte: relação entre variáveis,
construção de relações documentais e análise estrutural por grafos. O principal risco
era apresentar esses blocos como métodos sucessivos sem explicitar a mudança de
objeto. As pontes foram incorporadas aos slides e ao roteiro. Também foram corrigidos
um resultado numérico e a incompatibilidade entre atividades integrais e aula de
quatro horas.

## Mapa narrativo revisado

| Bloco | O que retoma | Pergunta ainda aberta | O que acrescenta |
|---|---|---|---|
| abertura | comparação da Unidade 5 | que sentidos diferentes “relação” pode assumir? | unidade, regra e limite comuns aos três sentidos |
| associação categórica | categorias da base tabular | as distribuições mudam entre grupos? | denominador, contingência, esperado, qui-quadrado e V |
| correlação | associação entre categorias | como duas quantidades variam juntas? | forma, Pearson, Spearman, estratos e sensibilidade |
| coocorrência | relações já presentes como colunas | como documentos produzem pares de entidades? | janela, incidência, projeção e proveniência da aresta |
| grafos | nós e arestas definidos | o que a estrutura do modelo revela? | grau, força, intermediação, direção e comunidades |
| oficina | quatro percursos metodológicos | qual método é pertinente ao projeto? | cadeia argumentativa, sensibilidade e não adoção |
| fechamento | caso D001 da abertura | o que a coocorrência autoriza afirmar? | síntese limitada e incremento cumulativo |

## Achados e tratamento

### S6-001 — O papel do grafo não estava explícito no mapa dos três sentidos

- **Gravidade:** alta.
- **Local:** slide “A unidade estudará três sentidos de ‘relação’”.
- **Evidência:** o slide listava associação categórica, correlação e coocorrência;
  grafos apareciam depois e podiam ser entendidos como um quarto tipo de evidência.
- **Consequência:** a turma poderia confundir relação documental com sua representação.
- **Ação aplicada:** o slide agora declara que grafo é uma representação de relações
  previamente definidas, como coocorrência ou correspondência.
- **Verificação:** a passagem coocorrência → grafo preserva a mesma ontologia de aresta.

### S6-002 — Mudanças de bloco dependiam da fala improvisada

- **Gravidade:** alta.
- **Local:** divisores 1–5 e gabaritos U06-A01 a U06-A05.
- **Evidência:** faltavam justificativas explícitas para categoria → quantidade,
  colunas → relações construídas, arestas → estrutura e medidas → oficina.
- **Consequência:** a apresentação podia parecer uma coleção de técnicas.
- **Ação aplicada:** adicionadas pontes com retomada, insuficiência e projeção; os
  divisores agora nomeiam a operação intelectual, não apenas o tópico.
- **Verificação:** os títulos e as pontes reconstroem um argumento cumulativo.

### S6-003 — O gabarito `local × ilustração` misturava convenções de qui-quadrado

- **Gravidade:** alta.
- **Local:** gabarito U06-A02 nos slides.
- **Evidência:** a fórmula e o notebook usam qui-quadrado descritivo sem correção de
  continuidade. Para a tabela `[[20,20],[18,22]]`, isso produz
  $\chi^2\approx0{,}2005$ e $V\approx0{,}0501$. O slide mostrava 0,05 e 0,03,
  correspondentes aproximadamente à correção de continuidade não declarada.
- **Consequência:** o mesmo procedimento parecia produzir resultados incompatíveis.
- **Ação aplicada:** o gabarito agora informa $\chi^2\approx0{,}20$ e
  $V\approx0{,}05$, explicitamente sem correção de continuidade.
- **Verificação:** cálculo reproduzido diretamente de `registros_associacao.csv`.

### S6-004 — Atividades integrais não cabiam no encontro

- **Gravidade:** alta.
- **Local:** U06-A01 a U06-A07 e atividade de saída.
- **Evidência:** os tempos declarados somavam 185 minutos, sem exposição, gabaritos,
  transições ou intervalo.
- **Consequência:** partes centrais seriam aceleradas ou omitidas sem planejamento.
- **Ação aplicada:** os slides distinguem recorte em aula e versão completa no
  notebook/projeto. A oficina é iniciada em aula e concluída no relatório cumulativo.
- **Verificação:** o roteiro apresenta uma rota de 240 minutos com intervalo.

### S6-005 — Terminologia “rede” permanecia no README

- **Gravidade:** média.
- **Local:** `unidade_06/README.md`.
- **Evidência:** título e entrega usavam “rede”, enquanto a unidade adotou “grafo” para
  a estrutura matemática.
- **Consequência:** os dois termos poderiam parecer sinônimos não problematizados.
- **Ação aplicada:** título e entrega foram alinhados a “grafo”. O nome histórico do
  arquivo de oficina foi preservado para não quebrar links.
- **Verificação:** o texto conceitual usa “grafo”; “rede” não aparece como substituto
  terminológico nos slides.

### S6-006 — A apresentação ultrapassa a faixa editorial

- **Gravidade:** média, risco aceito com controle.
- **Local:** apresentação completa, 81 slides.
- **Evidência:** a diretriz sugere 38–52 slides; a Unidade 6 integra quatro famílias
  conceituais, fórmulas, exemplos e gabaritos.
- **Consequência:** não é possível comentar toda tela com igual profundidade.
- **Tratamento:** o roteiro classifica prioridades e encaminha aprofundamentos aos
  notebooks. Referências não são lidas em aula.
- **Condição:** futura redução deve preservar tabelas de origem, exemplos, pontes e
  gabaritos; cortar apenas aprofundamentos duplicados.

## Pontos fortes

1. O caso inicial retorna no fechamento e explicita o limite da coocorrência.
2. Todo arquivo mencionado possui uma amostra tabular anterior ao uso.
3. As fórmulas têm exemplo numérico e representação visual.
4. A projeção mantém uma trilha até os documentos que produziram as arestas.
5. Grau, força e intermediação são ligados a perguntas diferentes.
6. A não adoção do método é tratada como decisão metodológica legítima.
7. Todos os exercícios em aula possuem gabarito imediatamente posterior.

## Viabilidade do encontro de quatro horas

| Faixa | Conteúdo | Duração |
|---|---|---:|
| 00:00–00:25 | orientação, bases, caso inicial e U06-A01 | 25 min |
| 00:25–01:00 | associação categórica e U06-A02 | 35 min |
| 01:00–01:32 | correlação e U06-A03 | 32 min |
| 01:32–01:42 | intervalo | 10 min |
| 01:42–02:17 | coocorrência e U06-A04 | 35 min |
| 02:17–02:52 | grafos e U06-A05 | 35 min |
| 02:52–03:37 | oficina U06-A06 | 45 min |
| 03:37–03:52 | revisão U06-A07 | 15 min |
| 03:52–04:00 | retorno, síntese e saída | 8 min |

## Validação

- correlações, estratificações e sensibilidade foram recalculadas a partir do CSV e
  coincidem com os slides;
- quantidade de nós e arestas, grau, força e intermediação dos exemplos foram
  recalculados e coincidem com a tabela derivada;
- o HTML do Marp deve ser gerado após as alterações;
- o validador da unidade inicia corretamente, mas a execução integral exige
  `matplotlib`, ausente no ambiente local desta revisão.

## Conclusão

A Unidade 6 está pronta para uso com o roteiro docente. Na aplicação, convém observar
se a turma distingue com segurança **relação na fonte**, **relação construída** e
**estrutura do grafo**; essa distinção é o eixo que sustenta toda a unidade.
