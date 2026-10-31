# Roteiro de fala — Unidade 6

## Associações e grafos

**Apresentação associada:** `slides/unidade_06.md`  
**Duração:** 4 horas, com intervalo de 10 minutos  
**Público:** pós-graduação em Humanidades, com experiência matemática heterogênea  
**Problema orientador:** quando um padrão entre dados sustenta uma relação — e quando
ele é efeito da forma de observar ou construir os dados?

## Ideia que organiza toda a aula

A palavra “relação” pode nomear objetos diferentes. Uma distribuição conjunta, uma
correlação, uma coocorrência construída e uma aresta de correspondência não fornecem
a mesma evidência. Antes de medir, é preciso declarar unidade, regra e limite. O grafo
representa relações já definidas; não cria, sozinho, o significado histórico delas.

## Cronograma da rota principal

| Tempo | Slides | Bloco |
|---:|---:|---|
| 00:00–00:25 | 1–14 | orientação, bases, caso inicial e U06-A01 |
| 00:25–01:00 | 15–28 | associação categórica e U06-A02 |
| 01:00–01:32 | 29–40 | correlação e U06-A03 |
| 01:32–01:42 | — | intervalo |
| 01:42–02:17 | 41–50 | coocorrência, projeção e U06-A04 |
| 02:17–02:52 | 51–63 | grafos, centralidades e U06-A05 |
| 02:52–03:37 | 64–73 | oficina U06-A06 |
| 03:37–03:52 | 74–75 | revisão por pares U06-A07 |
| 03:52–04:00 | 76–81 | retorno, síntese, saída e referências |

Os recortes em aula preservam a operação conceitual principal. A produção integral
continua nos notebooks e no relatório cumulativo. Em caso de atraso, abrevie os itens
marcados como aprofundamento; preserve as transições e o retorno às fontes.

---

## Bloco 1 — Orientar e distinguir sentidos de relação

### Slide 1 — Unidade 6

**Intenção:** apresentar “relação” como problema metodológico.

**Fala sugerida:** “Hoje não perguntaremos apenas se duas coisas estão relacionadas.
Perguntaremos que operação produziu essa relação e o que ela permite afirmar. Uma
associação estatística e uma ligação entre entidades não são evidências equivalentes.”

**Ponte:** “A agenda organiza essas diferenças antes de chegarmos às medidas.”

**Tempo/Prioridade:** 1 min · essencial.

### Slide 2 — Agenda

**Intenção:** mostrar que a aula progride de variáveis para documentos e grafos.

**Fala sugerida:** percorra os tópicos como transformação do objeto: categorias;
quantidades; documentos que geram pares; pares que formam grafos; análise aplicada.
Avise que o mesmo princípio — unidade, regra e limite — atravessa tudo.

**Ponte:** “Ao final, essas etapas deverão aparecer como capacidades observáveis.”

**Tempo/Prioridade:** 1 min · essencial.

### Slide 3 — Ao final, você deverá conseguir…

**Intenção:** situar resultados de aprendizagem.

**Fala sugerida:** destaque três verbos: construir, interpretar e justificar. Não
basta calcular V, correlação ou centralidade; é preciso reconstruir a origem do
resultado e decidir se ele é pertinente ao problema.

**Ponte:** “Essas capacidades formam um percurso que sempre retorna aos documentos.”

**Tempo/Prioridade:** 1 min · essencial.

### Slide 4 — O percurso da unidade

**Intenção:** visualizar a progressão e o retorno às fontes.

**Fala sugerida:** leia o diagrama da esquerda para a direita. Diferencie associação
entre colunas de construção de arestas. Mostre que o retorno aos documentos fecha o
ciclo e impede que o grafo se torne evidência autônoma.

**Interação:** pergunte onde a turma imagina ocorrer a maior perda de contexto.

**Ponte:** “Para responder, primeiro precisamos separar os sentidos da palavra relação.”

**Tempo/Prioridade:** 2 min · essencial.

### Slide 5 — Três sentidos de “relação”

**Intenção:** estabelecer o vocabulário que organiza a unidade.

**Fala sugerida:** leia as três perguntas em linguagem comum. Enfatize: associação
categórica compara distribuições; correlação compara covariação numérica;
coocorrência depende de uma janela. Explique que grafo não é quarto tipo de evidência:
é uma representação de relações previamente definidas.

**Ponte:** “Agora conheceremos as duas bases que sustentam esses sentidos.”

**Tempo/Prioridade:** 2 min · essencial.

### Slide 6 — Base fictícia: registros e documentos

**Intenção:** distinguir duas unidades de observação.

**Fala sugerida:** `registros_associacao.csv` sustenta comparações entre variáveis;
`documentos_entidades.csv` sustenta a construção de coocorrências. Ambos são
fictícios. Não integre as linhas como se fossem o mesmo universo.

**Ponte:** “Uma amostra de cada arquivo torna essa diferença concreta.”

**Tempo/Prioridade:** 2 min · essencial.

### Slide 7 — Como são os dois arquivos de origem?

**Intenção:** mostrar registros antes de qualquer resultado derivado.

**Fala sugerida:** percorra uma linha de cada tabela. No primeiro arquivo, tema e
extensão são colunas do mesmo registro. No segundo, as entidades estão listadas em um
documento, mas ainda não formam arestas.

**Interação:** peça à turma que identifique a unidade de cada linha.

**Ponte:** “Do segundo arquivo derivaremos duas tabelas relacionais com significados
distintos.”

**Tempo/Prioridade:** 2 min · essencial.

### Slide 8 — Tabelas derivadas para os grafos

**Intenção:** distinguir coocorrência construída de correspondência registrada.

**Fala sugerida:** “Uma tabela conta pares mencionados no mesmo documento; a outra
registra remetente e destinatário. Ambas podem virar grafos, mas não dizem a mesma
coisa.” Destaque as unidades relacionais.

**Ponte:** “Vamos ver o formato de uma aresta em cada caso.”

**Tempo/Prioridade:** 1 min · essencial.

### Slide 9 — Como são as duas tabelas?

**Intenção:** tornar visíveis peso e direção.

**Fala sugerida:** na coocorrência, a ordem origem–destino é apenas convenção e peso é
número de documentos. Na correspondência, remetente e destinatário preservam
assimetria e cartas contam eventos. Não interprete `origem` da primeira tabela como
remetente.

**Ponte:** “Para entender como a primeira tabela nasceu, voltaremos a uma única linha.”

**Tempo/Prioridade:** 2 min · essencial.

### Slide 10 — Antes da teoria: de uma linha à coocorrência

**Intenção:** produzir a pergunta central com caso concreto.

**Fala sugerida:** leia D001 e conte três entidades. Explique que os três pares não
estavam escritos na fonte; foram produzidos pela escolha do documento como janela.

**Interação:** pergunte: “podemos afirmar contato entre Ana F. e Liga Aurora?” Espere
uma justificativa, não apenas sim ou não.

**Ponte:** “A resposta exige separar o que veio da fonte do que foi acrescentado pela
operação.”

**Tempo/Prioridade:** 2 min · essencial.

### Slide 11 — Fonte, operação e interpretação

**Intenção:** estabelecer três níveis que não devem ser colapsados.

**Fala sugerida:** a fonte registra menções; a operação forma pares; o resultado
registra contexto compartilhado. Filiação, colaboração ou contato seriam
interpretações adicionais que exigem evidência. Use a figura para mostrar a passagem
documento–entidade para entidade–entidade.

**Ponte:** “O exemplo seguinte abre a caixa-preta dessa passagem em três tabelas.”

**Tempo/Prioridade:** 2 min · essencial.

### Slide 12 — Da incidência às arestas

**Intenção:** apresentar a sequência completa antes da formalização matricial.

**Fala sugerida:** leia da esquerda para a direita: presença da entidade em cada
documento; comparação das colunas; lista de pares e pesos. Preserve os IDs porque eles
permitem voltar da aresta à fonte.

**Ponte:** “Com esse vocabulário, podemos testar qual evidência cada frase relacional
realmente exigiria.”

**Tempo/Prioridade:** 2 min · essencial.

### Slide 13 — U06-A01 · Que relação está sendo afirmada?

**Intenção:** diagnosticar a tradução de frases em unidade, evidência e limite.

**Condução:** duplas, 8 minutos. Escolha uma das duas frases. Exija unidade, evidência,
conclusão permitida e excessiva. A versão completa de 12 minutos pode tratar ambas.

**Ponte para o gabarito:** “Corrigiremos pelo vínculo entre frase e evidência, não por
uma palavra-chave isolada.”

**Tempo/Prioridade:** 8 min · atividade.

### Slide 14 — Gabarito U06-A01

**Intenção:** estabilizar o princípio comum e abrir associação categórica.

**Fala sugerida:** contraste documento como unidade de correlação e par como unidade
relacional. Mostre que “variam juntas” e “compartilham contexto” são conclusões
diferentes. Em ambas, causalidade ou vínculo social ainda seriam excessivos.

**Ponte:** “Começaremos pelas categorias, onde escolher o denominador é a primeira
decisão interpretativa.”

**Tempo/Prioridade:** 2 min · essencial.

---

## Bloco 2 — Associação categórica

### Slide 15 — Categorias aparecem juntas?

**Intenção:** anunciar a primeira família de relação.

**Fala sugerida:** “Aqui a relação já está nas colunas da tabela. Não construiremos
arestas; compararemos distribuições entre grupos.”

**Ponte:** “O procedimento começa com contagens, mas não termina nelas.”

**Tempo/Prioridade:** 30 s · essencial.

### Slide 16 — Como investigar associação categórica?

**Intenção:** oferecer o algoritmo conceitual antes da fórmula.

**Fala sugerida:** agrupe os cinco passos: organizar tabela; escolher denominador;
comparar proporções; inspecionar vieses. Enfatize que associação descritiva significa
distribuição diferente, não mecanismo causal.

**Ponte:** “Vamos executar esse percurso para período e tema educação.”

**Tempo/Prioridade:** 2 min · essencial.

### Slide 17 — Comece pela tabela de contingência

**Intenção:** tornar o denominador explícito.

**Fala sugerida:** leia primeiro totais de linha e coluna. A pergunta compara períodos,
portanto o denominador é 40 em cada linha. Resolva 25/40. Diga que outro denominador
responderia a outra pergunta.

**Ponte:** “Convertendo as duas linhas em proporções, veremos se as distribuições
mudam.”

**Tempo/Prioridade:** 3 min · essencial.

### Slide 18 — Caso 1 · Há associação descritiva

**Intenção:** mostrar uma diferença substantivamente visível.

**Fala sugerida:** compare a coluna “sim”: 32,5% e 62,5%. Expresse a diferença como 30
pontos percentuais, não “30% maior”. Declare o universo: estes 80 documentos fictícios.

**Ponte:** “Para compreender o contraste, observaremos agora um caso quase sem
diferença.”

**Tempo/Prioridade:** 2 min · essencial.

### Slide 19 — Caso 2 · Quase não há associação

**Intenção:** construir uma referência visual para associação fraca.

**Fala sugerida:** as linhas diferem no máximo 2,5 pontos. Conhecer o período quase não
reduz a incerteza sobre gênero nesta base. Não diga que as variáveis são universalmente
independentes.

**Ponte:** “A comparação visual é central; agora formalizaremos o que esperaríamos sob
independência.”

**Tempo/Prioridade:** 2 min · essencial.

### Slide 20 — O que esperaríamos sem associação?

**Intenção:** explicar frequência esperada com os mesmos totais marginais.

**Fala sugerida:** use linha 40, coluna 38 e total 80. Resolva 19. Explique que esperado
não significa previsão histórica; é a contagem compatível com independência dados os
totais observados.

**Ponte:** “Compararemos cada contagem observada a esse cenário de referência.”

**Tempo/Prioridade:** 3 min · essencial.

### Slide 21 — Observado e esperado

**Intenção:** tornar as discrepâncias concretas antes da soma.

**Fala sugerida:** percorra os sinais +6 e −6. A simetria decorre dos totais iguais.
Peça que a turma identifique quais células concentram o tema além do esperado.

**Ponte:** “O qui-quadrado transforma essas quatro diferenças em uma medida única.”

**Tempo/Prioridade:** 2 min · essencial.

### Slide 22 — Qui-quadrado reúne os desvios

**Intenção:** ligar fórmula, célula e gráfico.

**Fala sugerida:** resolva a contribuição de uma célula e explique por que se eleva ao
quadrado. Aponte as barras. A estatística cresce com discrepância e com tamanho da base;
não possui uma escala fixa de intensidade substantiva.

**Ponte:** “Para obter uma escala entre zero e um, normalizaremos esse resultado.”

**Tempo/Prioridade:** 3 min · essencial.

### Slide 23 — V de Cramér

**Intenção:** explicar normalização e o papel de k.

**Fala sugerida:** $k$ é o menor número de categorias entre linhas e colunas; aqui é
2. Substitua 7,22, 80 e 2. Interprete 0,30 como intensidade nesta tabela, sem rótulo
universal nem causalidade.

**Ponte:** “Dois exemplos extremos ajudam a compreender a escala.”

**Tempo/Prioridade:** 3 min · essencial.

### Slide 24 — V próximo de zero

**Intenção:** ligar valor pequeno a distribuições semelhantes.

**Fala sugerida:** retome o caso gênero. Conhecer a linha pouco informa sobre a coluna.
Reforce que zero é relativo à categorização, ao corpus e ao recorte.

**Ponte:** “No extremo oposto, uma categoria determina perfeitamente a outra na
tabela.”

**Tempo/Prioridade:** 1 min · essencial.

### Slide 25 — V igual a 1

**Intenção:** visualizar associação máxima sem causalidade.

**Fala sugerida:** em cada período só aparece uma categoria. Conhecer a linha determina
a coluna, mas não explica o processo. Associação perfeita pode ser artefato de uma
classificação ou construção hipotética.

**Ponte:** “Entre zero e um, nenhuma medida corrige problemas na formação da base.”

**Tempo/Prioridade:** 1 min · aprofundamento.

### Slide 26 — A associação pode ser produzida pela base

**Intenção:** reintegrar crítica documental.

**Fala sugerida:** escolha três riscos: classificação instável, preservação desigual e
OCR. Mostre como cada um pode alterar células da tabela antes do cálculo.

**Ponte:** “A atividade precisa registrar medida e risco de viés no mesmo produto.”

**Tempo/Prioridade:** 1 min · essencial.

### Slide 27 — U06-A02 · Associação categórica

**Intenção:** praticar denominador, tabela e interpretação.

**Condução:** grupos de três, 8 minutos, itens 1–3. Um membro define a pergunta, outro
constrói a tabela e o terceiro confere denominadores. Medida e parágrafo completos
continuam no notebook.

**Ponte para o gabarito:** “Antes do coeficiente, confiram se a porcentagem responde à
pergunta declarada.”

**Tempo/Prioridade:** 8 min · atividade.

### Slide 28 — Gabarito U06-A02

**Intenção:** modelar resultado fraco e explicitar a convenção de cálculo.

**Fala sugerida:** compare 50% e 55%. Sem correção de continuidade, o qui-quadrado é
aproximadamente 0,20 e V, 0,05. A diferença descritiva é pequena; ainda assim, não se
prova igualdade universal. Nomeie a convenção para evitar números incompatíveis.

**Ponte:** “Categorias exigiram proporções. Para duas quantidades, começaremos pela
forma da nuvem, não por uma tabela cruzada.”

**Tempo/Prioridade:** 2 min · essencial.

---

## Bloco 3 — Correlação e explicações alternativas

### Slide 29 — Duas medidas variam juntas?

**Intenção:** marcar a mudança de tipo de variável.

**Fala sugerida:** “Saímos de combinações de categorias e passamos a pares numéricos
por documento. A pergunta agora é direção e forma da covariação.”

**Ponte:** “Antes de calcular, olhemos os 80 pares.”

**Tempo/Prioridade:** 30 s · essencial.

### Slide 30 — Veja a nuvem antes do coeficiente

**Intenção:** priorizar forma, grupos e extremos.

**Fala sugerida:** oriente o olhar para tendência positiva, dispersão e cores de local.
Pergunte se uma linha única representa igualmente Capital e Interior. Um coeficiente
é resumo da nuvem, não seu substituto.

**Ponte:** “Pearson compactará a tendência linear em um número.”

**Tempo/Prioridade:** 2 min · essencial.

### Slide 31 — Correlação de Pearson

**Intenção:** interpretar r com exemplo e figura.

**Fala sugerida:** não derive a fórmula. Explique que desvios de x e y com o mesmo
sinal contribuem positivamente. Os 80 pares produzem 0,53. A medida não está em
palavras nem referências e não prova causa.

**Ponte:** “O sinal e o módulo respondem a perguntas diferentes.”

**Tempo/Prioridade:** 3 min · essencial.

### Slide 32 — Sinal e magnitude

**Intenção:** construir leitura básica de r.

**Fala sugerida:** sinal indica direção; módulo indica proximidade de uma linha. Zero
significa pouca associação linear, não ausência de qualquer padrão. Desenhe no ar uma
curva em U como contraexemplo.

**Ponte:** “Se a ordem cresce sem formar uma linha, outra medida pode resumir melhor.”

**Tempo/Prioridade:** 2 min · essencial.

### Slide 33 — Spearman observa a ordem

**Intenção:** diferenciar escala original e postos.

**Fala sugerida:** transforme valores em posições e resolva o exemplo pequeno. Spearman
captura tendência monotônica e reduz dependência da distância entre valores. Pearson
0,53 e Spearman 0,51 são próximos aqui, mas o gráfico continua necessário.

**Ponte:** “Um número global ainda pode misturar relações distintas entre grupos.”

**Tempo/Prioridade:** 3 min · essencial.

### Slide 34 — A associação muda entre estratos

**Intenção:** mostrar heterogeneidade contextual.

**Fala sugerida:** compare conjunto, Capital e Interior. Estratificar não corrige
automaticamente; revela que composição e contexto participam do padrão. Não escolha
o maior coeficiente como o ‘verdadeiro’.

**Ponte:** “Outra pergunta é quanto o resultado depende de uma decisão ou caso.”

**Tempo/Prioridade:** 2 min · essencial.

### Slide 35 — Sensibilidade pergunta “e se?”

**Intenção:** introduzir comparação de especificações.

**Fala sugerida:** com e sem o maior valor, r muda de 0,745 para 0,733. Isso indica
estabilidade diante dessa decisão específica, não robustez universal. Explique por que
registrar ambas as versões é melhor que apagar o caso.

**Ponte:** “Mesmo um padrão estável não identifica o mecanismo que o produziu.”

**Tempo/Prioridade:** 2 min · essencial.

### Slide 36 — Correlação não identifica o mecanismo

**Intenção:** separar descrição de causalidade.

**Fala sugerida:** percorra as possibilidades da figura: direção direta, reversa,
causa comum, seleção e coincidência. O mesmo coeficiente pode ser compatível com
histórias diferentes.

**Ponte:** “Essas histórias devem ser escritas como explicações rivais que orientam
novas evidências.”

**Tempo/Prioridade:** 2 min · essencial.

### Slide 37 — Escreva explicações rivais

**Intenção:** ligar número e investigação substantiva.

**Fala sugerida:** escolha extensão–circulação. Classifique as alternativas em
causalidade direta, reversa, causa comum, seleção e dependência de casos. Não é preciso
decidir agora; é preciso impedir que uma hipótese se torne conclusão automática.

**Ponte:** “Há ainda um risco anterior à interpretação: procurar muitos pares e mostrar
somente o mais impressionante.”

**Tempo/Prioridade:** 2 min · essencial.

### Slide 38 — Muitos testes produzem achados ocasionais

**Intenção:** distinguir exploração de confirmação.

**Fala sugerida:** explique seleção após ver resultados em linguagem comum. Registrar
todos os pares tentados torna o percurso auditável. Evite aprofundar correções de
múltiplos testes; o objetivo é transparência exploratória.

**Ponte:** “A atividade combinará gráfico, coeficientes, sensibilidade e alternativas.”

**Tempo/Prioridade:** 1 min · aprofundamento.

### Slide 39 — U06-A03 · Correlação com auditoria

**Intenção:** praticar leitura anterior ao coeficiente.

**Condução:** duplas, 8 minutos, itens 1–3. Exija justificativa da pergunta, inspeção
do gráfico e comparação Pearson–Spearman. Sensibilidade e alternativas continuam na
versão completa.

**Ponte para o gabarito:** “O gabarito será avaliado pela estabilidade da interpretação,
não pela quantidade de casas decimais.”

**Tempo/Prioridade:** 8 min · atividade.

### Slide 40 — Gabarito U06-A03

**Intenção:** integrar medida global, estratos, caso e limite.

**Fala sugerida:** os coeficientes são positivos em todos os recortes e mudam pouco
sem R013. Leia os valores do caso. A estabilidade fortalece a descrição na base, mas
não a hipótese causal.

**Ponte:** “Até aqui, as relações já existiam como pares de colunas. Agora construiremos
relações entre entidades a partir do conteúdo dos documentos.”

**Tempo/Prioridade:** 2 min · essencial.

---

## Bloco 4 — Coocorrência, incidência e projeção

### Slide 41 — Como documentos viram relações?

**Intenção:** marcar uma mudança ontológica, não apenas técnica.

**Fala sugerida:** “Extensão e circulação estavam registradas em cada linha. Uma aresta
Ana–Liga não estava pronta: ela depende de janela, extração de entidades e regra de
projeção.”

**Ponte:** “A primeira decisão determina quantos pares cada documento pode gerar.”

**Tempo/Prioridade:** 30 s · essencial.

### Slide 42 — Uma janela produz pares

**Intenção:** mostrar crescimento combinatório e efeito de documentos densos.

**Fala sugerida:** resolva 3 entidades → 3 pares e 10 → 45. Use a figura para lembrar
a projeção. Documentos com muitas entidades podem dominar pesos e estrutura.

**Ponte:** “O significado desses pares depende do limite escolhido para ‘ocorrer junto’.”

**Tempo/Prioridade:** 3 min · essencial.

### Slide 43 — Coocorrência depende de uma janela

**Intenção:** transformar janela em decisão substantiva.

**Fala sugerida:** compare documento, parágrafo e frase. Janela ampla aumenta cobertura
e ruído; estreita aumenta proximidade textual e pode perder relações discursivas.
Escolha deve corresponder à pergunta e ao gênero documental.

**Ponte:** “Depois de escolher a janela, registramos presença numa matriz que conserva
documentos e entidades.”

**Tempo/Prioridade:** 2 min · essencial.

### Slide 44 — Matriz de incidência

**Intenção:** apresentar o grafo bipartido em forma tabular.

**Fala sugerida:** linhas são documentos, colunas são entidades e 1 indica menção.
Mostre onde Ana e Liga coincidem. Avise que outras entidades foram omitidas apenas da
visualização, não da definição.

**Ponte:** “Comparar colunas transforma incidências em pesos de coocorrência.”

**Tempo/Prioridade:** 2 min · essencial.

### Slide 45 — A projeção multiplica incidências

**Intenção:** ligar matriz, fórmula e exemplo.

**Fala sugerida:** explique $B^TB$ como comparação entre colunas. A diagonal conta
frequência individual; fora da diagonal conta documentos compartilhados. Resolva
Ana–Liga = 2. Remover diagonal é decisão registrada.

**Ponte:** “A projeção facilita comparação estrutural, mas comprime os documentos
intermediários.”

**Tempo/Prioridade:** 3 min · essencial.

### Slide 46 — Bipartida ou projetada?

**Intenção:** explicitar ganho e perda de representação.

**Fala sugerida:** bipartida preserva fonte; projetada facilita pares. Recomende manter
uma tabela aresta–documentos mesmo quando a análise usa projeção.

**Ponte:** “Nem toda tabela de arestas, porém, nasce de projeção.”

**Tempo/Prioridade:** 2 min · essencial.

### Slide 47 — Coocorrência não é correspondência

**Intenção:** distinguir ontologias de aresta.

**Fala sugerida:** coocorrência é construída e normalmente simétrica; correspondência
registra envio e é dirigida. Ambas cabem em grafos, mas as medidas devem ser traduzidas
segundo a fonte. Só depois dessa definição faz sentido medir estrutura.

**Ponte:** “Antes, ainda precisamos examinar o que um peso alto pode realmente medir.”

**Tempo/Prioridade:** 2 min · essencial.

### Slide 48 — O peso pode medir popularidade da fonte

**Intenção:** conter interpretação social de frequência documental.

**Fala sugerida:** entidade frequente cria muitos pares. Peso alto pode refletir
documento longo, republicação ou ambiguidade de nome. “Forte” deve ser traduzido como
contagem definida, não intensidade social presumida.

**Ponte:** “A atividade exigirá uma trilha que permita auditar uma aresta até as fontes.”

**Tempo/Prioridade:** 2 min · essencial.

### Slide 49 — U06-A04 · Matriz relacional auditável

**Intenção:** praticar construção e limite da aresta.

**Condução:** grupos de três, 8 minutos, itens 1, 2 e 5. Definam unidade e janela,
montem pequena incidência e escrevam o que uma aresta significaria. Projeção e retorno
integral ficam no notebook.

**Ponte para o gabarito:** “Uma aresta correta precisa de peso e de documentos que
expliquem sua origem.”

**Tempo/Prioridade:** 8 min · atividade.

### Slide 50 — Gabarito U06-A04

**Intenção:** modelar projeção auditável e abrir estrutura do grafo.

**Fala sugerida:** leia peso e IDs juntos. A ligação é simétrica, documental e limitada
ao recorte. Com nós e arestas definidos, grau e centralidade poderão responder a
perguntas sobre esse modelo — não sobre uma sociedade inteira.

**Ponte:** “Agora podemos perguntar o que a estrutura do grafo mostra.”

**Tempo/Prioridade:** 2 min · essencial.

---

## Bloco 5 — Estrutura do grafo

### Slide 51 — O que a estrutura do grafo mostra?

**Intenção:** subordinar medidas à definição das arestas.

**Fala sugerida:** “Não começamos pelo desenho. Chegamos a ele depois de definir fonte,
janela, direção e peso.”

**Ponte:** “Primeiro, um vocabulário mínimo.”

**Tempo/Prioridade:** 30 s · essencial.

### Slide 52 — Vocabulário mínimo de um grafo

**Intenção:** definir G, nós, arestas, direção, peso e atributos.

**Fala sugerida:** traduza cada símbolo para a base: entidades como nós; coocorrências
ou cartas como arestas; documentos compartilhados ou cartas como peso. Não aceite
termos abstratos sem domínio histórico.

**Ponte:** “A projeção fictícia permite visualizar esse vocabulário em conjunto.”

**Tempo/Prioridade:** 2 min · essencial.

### Slide 53 — Um grafo projetado da base fictícia

**Intenção:** ensinar a legenda antes da interpretação.

**Fala sugerida:** posição é layout, tamanho é força e espessura é peso. Não use
proximidade na tela como distância histórica. Peça que a turma localize Jornal
Horizonte, mas não o chame ainda de ‘mais importante’.

**Ponte:** “O desenho orienta perguntas; as medidas precisam ser calculadas.”

**Tempo/Prioridade:** 2 min · essencial.

### Slide 54 — Visualização não é medida

**Intenção:** separar geometria do layout e estrutura do grafo.

**Fala sugerida:** mudar a semente pode mudar posições sem mudar arestas. Centro
geométrico não é centralidade; aglomerado visual não é automaticamente comunidade.

**Ponte:** “Começaremos pela pergunta estrutural mais simples: quantos vizinhos?”

**Tempo/Prioridade:** 2 min · essencial.

### Slide 55 — Grau

**Intenção:** explicar centralidade de grau normalizada.

**Fala sugerida:** $\deg(v)$ conta vizinhos e $n-1$ conta vizinhos possíveis. Resolva
11/13. Diga explicitamente que $C_D(v)$ é centralidade de grau, não qualquer
centralidade. Muitos parceiros registrados não equivalem a prestígio.

**Ponte:** “O grau ignora quantas vezes cada ligação ocorreu.”

**Tempo/Prioridade:** 3 min · essencial.

### Slide 56 — Força

**Intenção:** introduzir soma dos pesos incidentes.

**Fala sugerida:** resolva 3+2+1. Compare nó com muitos vizinhos de peso 1 e nó com
poucos vínculos repetidos. Traduza força segundo a unidade do peso; aqui, documentos
compartilhados.

**Ponte:** “Grau e força descrevem vizinhança; outra medida pergunta pela posição em
caminhos.”

**Tempo/Prioridade:** 3 min · essencial.

### Slide 57 — Intermediação

**Intenção:** explicar betweenness como participação em caminhos mínimos.

**Fala sugerida:** $s$ e $t$ são os extremos; $v$ é o nó avaliado. O numerador conta
caminhos mínimos que passam por v e o denominador todos os caminhos mínimos do par.
Use o diagrama de ponte e interprete 0,311 apenas no grafo modelado.

**Ponte:** “As três medidas podem destacar nós diferentes porque respondem a perguntas
diferentes.”

**Tempo/Prioridade:** 3 min · essencial.

### Slide 58 — Medidas respondem a perguntas diferentes

**Intenção:** impedir síntese vaga em “importância”.

**Fala sugerida:** grau = diversidade de vizinhos; força = volume de peso; intermediação
= posição em caminhos. Exija que toda centralidade seja nomeada e ligada à pergunta.

**Ponte:** “Até aqui usamos grafo não dirigido; a correspondência exige preservar
assimetria.”

**Tempo/Prioridade:** 2 min · essencial.

### Slide 59 — Grafos dirigidos preservam assimetria

**Intenção:** traduzir entrada, saída e força no corpus epistolar.

**Fala sugerida:** compare destinatários distintos e cartas enviadas; são grau e força
de saída. A direção permite perguntas que a coocorrência simétrica não contém.

**Ponte:** “Preservar direção também expõe registros estranhos que exigem auditoria.”

**Tempo/Prioridade:** 2 min · essencial.

### Slide 60 — Um autorremetimento exige retorno ao registro

**Intenção:** mostrar que anomalia estrutural é pergunta documental.

**Fala sugerida:** Fábio → Fábio pode ser erro, conflito de nomes, cópia ou convenção.
Nem remover nem manter automaticamente. A medida sinaliza; a fonte decide a
interpretação.

**Ponte:** “Também devemos resistir a interpretar automaticamente resultados de
algoritmos de agrupamento.”

**Tempo/Prioridade:** 2 min · essencial.

### Slide 61 — Comunidades são partições algorítmicas

**Intenção:** distinguir densidade computacional de grupo histórico.

**Fala sugerida:** resultado varia com algoritmo, resolução, pesos, direção e ausências.
“Comunidade” é termo técnico do método; grupo social autoconsciente é hipótese
histórica adicional.

**Ponte:** “A atividade retornará de duas medidas às arestas e aos documentos.”

**Tempo/Prioridade:** 2 min · aprofundamento.

### Slide 62 — U06-A05 · Estrutura e retorno aos casos

**Intenção:** integrar medida e auditoria.

**Condução:** grupos de três, 8 minutos, itens 1–3. Escolham dois nós, duas medidas e
arestas que expliquem a diferença. O retorno a documentos continua no notebook.

**Ponte para o gabarito:** “Uma interpretação de centralidade sem arestas concretas é
apenas um rótulo.”

**Tempo/Prioridade:** 8 min · atividade.

### Slide 63 — Gabarito U06-A05

**Intenção:** modelar comparação estrutural limitada.

**Fala sugerida:** compare grau, força e intermediação de Jornal Horizonte e Caio M.
Os documentos explicam a posição. “Mais central no grafo documental” é permitido;
“ator dominante” excede seleção, janela e projeção.

**Ponte:** “A oficina reunirá essa disciplina com as análises categórica e numérica.”

**Tempo/Prioridade:** 2 min · essencial.

---

## Bloco 6 — Oficina e projeto cumulativo

### Slide 64 — Oficina

**Intenção:** mudar de exposição para escolha metodológica.

**Fala sugerida:** “Não é obrigatório usar grafo. A entrega pede um método pertinente
ou uma não adoção bem argumentada.”

**Ponte:** “Qualquer trilha deve formar a mesma cadeia de justificativa.”

**Tempo/Prioridade:** 30 s · essencial.

### Slide 65 — Uma análise defensável forma uma cadeia

**Intenção:** fornecer rubrica visual da oficina.

**Fala sugerida:** percorra pergunta, unidade, construção, resultado, casos e limite.
Se a equipe não consegue explicar como a base produziu o resultado, o elo de
construção está ausente.

**Ponte:** “A atividade começa pela escolha de uma entre três trilhas.”

**Tempo/Prioridade:** 1 min · essencial.

### Slide 66 — U06-A06 · Oficina

**Intenção:** definir produto e continuidade.

**Condução:** 35 minutos em aula, versão completa de 55. As equipes atualizam o mesmo
relatório-notebook. Exija escolha da trilha e pelo menos pergunta, unidade, operação,
uma evidência e limite no recorte de aula.

**Ponte:** “Vamos esclarecer o que cada trilha precisa demonstrar.”

**Tempo/Prioridade:** 2 min de orientação + trabalho nos slides seguintes.

### Slide 67 — Trilha A · Associação

**Intenção:** orientar análise categórica ou numérica.

**Fala sugerida:** selecione tabela ou gráfico antes da medida; declare denominador ou
forma da nuvem; inclua sensibilidade e explicação rival. Reserve 3 minutos para as
equipes A escreverem sua pergunta e unidade.

**Ponte:** “Na trilha de grafo, a operação de construção da aresta exige registro ainda
mais explícito.”

**Tempo/Prioridade:** 4 min · atividade.

### Slide 68 — Trilha B · Grafo

**Intenção:** orientar uma análise relacional auditável.

**Fala sugerida:** peça significado histórico de nó e aresta, direção, peso, janela e
proveniência. Visualização sem legenda ou medida sem retorno a casos não completa a
análise. Equipes B registram sua ontologia de aresta.

**Ponte:** “Se essa ontologia não puder ser defendida, a não adoção é uma alternativa
legítima.”

**Tempo/Prioridade:** 4 min · atividade.

### Slide 69 — Trilha C · Não adoção

**Intenção:** legitimar decisão negativa fundamentada.

**Fala sugerida:** escolha duas razões: nomes irresolvíveis e ausências dominantes.
Não adoção precisa demonstrar inadequação e propor método alternativo, não apenas
declarar dificuldade.

**Ponte:** “Qualquer trilha deve testar ao menos uma decisão capaz de alterar o resultado.”

**Tempo/Prioridade:** 3 min · atividade.

### Slide 70 — Sensibilidade mínima

**Intenção:** transformar decisão analítica em objeto de comparação.

**Fala sugerida:** cada equipe escolhe uma alternativa compatível com sua trilha.
Registre versão A, versão B, o que mudou e por quê. Reserve 8 minutos para execução ou
planejamento reproduzível.

**Ponte:** “O produto final combina essa comparação com texto, código, visualização e
retorno à fonte.”

**Tempo/Prioridade:** 9 min · atividade.

### Slide 71 — O produto deve combinar evidências

**Intenção:** evitar entrega reduzida a código ou imagem.

**Fala sugerida:** distribua funções: texto pergunta e interpreta; código reproduz;
tabela mostra valores; gráfico permite inspeção; fonte recupera contexto; limite
restringe a frase. Reserve 10 minutos para produzir a primeira versão da seção.

**Ponte:** “Compararemos essa versão com um exemplo completo de associação numérica.”

**Tempo/Prioridade:** 11 min · atividade.

### Slide 72 — Gabarito U06-A06 — 1/2

**Intenção:** oferecer exemplo de especificação e evidência.

**Fala sugerida:** identifique unidade, variáveis, dispersão, dois coeficientes,
sensibilidade e caso R013. Peça às equipes que localizem equivalentes em sua trilha,
sem copiar o tema.

**Ponte:** “A tabela se torna argumento somente quando os números entram numa conclusão
limitada.”

**Tempo/Prioridade:** 2 min · essencial.

### Slide 73 — Gabarito U06-A06 — 2/2

**Intenção:** modelar a redação final.

**Fala sugerida:** destaque descrição positiva, estabilidade específica, explicações
alternativas e limite causal. Lembre que trilhas B e C seguem a mesma cadeia.

**Ponte:** “Agora outra equipe testará se essa cadeia pode ser reconstruída sem
explicação oral.”

**Tempo/Prioridade:** 2 min · essencial.

---

## Bloco 7 — Revisão, retorno e fechamento

### Slide 74 — U06-A07 · Revisão por pares

**Intenção:** testar auditabilidade do produto.

**Condução:** troca entre equipes, 10 minutos. O parecer registra uma força e duas
revisões. O leitor verifica unidade, construção, visualização, sensibilidade, casos e
limite sem pedir explicação ao autor.

**Ponte para o gabarito:** “Uma boa revisão nomeia o problema e uma alteração
verificável.”

**Tempo/Prioridade:** 10 min · atividade.

### Slide 75 — Gabarito U06-A07

**Intenção:** mostrar feedback específico e acionável.

**Fala sugerida:** a força localiza unidade e regra; as revisões pedem acessibilidade
e sensibilidade temporal. Compare com comentários vagos como “melhorar o gráfico”.

**Ponte:** “Fecharemos retornando às três entidades que abriram a aula.”

**Tempo/Prioridade:** 2 min · essencial.

### Slide 76 — Retorno ao caso inicial

**Intenção:** fechar o arco narrativo da coocorrência.

**Fala sugerida:** a conclusão permitida é contexto documental compartilhado segundo
a janela. Leia as cinco inferências não autorizadas. Pergunte que evidência adicional
seria necessária para sustentar contato direto.

**Ponte:** “Essa cautela precisa permanecer registrada no projeto cumulativo.”

**Tempo/Prioridade:** 2 min · essencial.

### Slide 77 — O que entra no projeto cumulativo?

**Intenção:** explicitar continuidade da entrega.

**Fala sugerida:** peça que as equipes marquem o que foi iniciado e o que falta.
Destaque formação da relação, sensibilidade, casos e decisão de manter ou abandonar.

**Ponte:** “Esses elementos condensam as ideias centrais da unidade.”

**Tempo/Prioridade:** 1 min · essencial.

### Slide 78 — Síntese

**Intenção:** recuperar o percurso como cadeia lógica.

**Fala sugerida:** conecte: denominador define comparação; correlação não define
mecanismo; janela constrói coocorrência; projeção perde contexto; centralidades
respondem a perguntas distintas; comunidades são algorítmicas; fontes limitam tudo.

**Ponte:** “A saída transforma essa síntese em três decisões do próprio projeto.”

**Tempo/Prioridade:** 1 min · essencial.

### Slide 79 — Saída · Complete três frases

**Intenção:** obter evidência individual de aprendizagem.

**Condução:** cada estudante registra unidade relacional, decisão sensível e limite.
Se o tempo terminar, iniciar em aula e concluir imediatamente depois. As respostas
abrem a seção da Unidade 6 no relatório.

**Tempo/Prioridade:** 4–5 min · atividade.

### Slides 80–81 — Referências

**Intenção:** documentar sustentação e aprofundamento.

**Fala sugerida:** não leia a lista. Aponte Agresti para dados categóricos; Pearson e
Spearman para correlação; Freeman e Newman para centralidade e grafos; Moretti e
Grandjean para aplicações em Humanidades. Reforce a natureza fictícia dos dados.

**Tempo/Prioridade:** exibir ao final · reserva.

---

## Registro após a aula

- **Transição que funcionou melhor:**
- **A turma distinguiu grafo de tipo de evidência?**
- **Dúvida recorrente sobre denominadores ou V:**
- **Dúvida recorrente sobre correlação e causalidade:**
- **Dúvida recorrente sobre projeção:**
- **Medida de centralidade mais difícil:**
- **Atividade que ultrapassou o recorte:**
- **Conteúdo encaminhado ao notebook:**
- **Alteração recomendada nos slides:**
- **Alteração recomendada neste roteiro:**
