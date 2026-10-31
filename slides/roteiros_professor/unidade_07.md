# Roteiro de fala — Unidade 7

## Modelos de associação condicionada

**Apresentação associada:** `slides/unidade_07.md`  
**Duração:** 4 horas, com intervalo de 10 minutos  
**Público:** pós-graduação em Humanidades, com experiência matemática heterogênea  
**Problema orientador:** quais características estão associadas a um resultado quando
outras diferenças observadas são consideradas?

## Ideia que organiza toda a aula

Um coeficiente não é uma propriedade isolada do mundo. Ele resume uma comparação
definida por uma resposta, um conjunto de explicativas, escalas, casos e decisões.
A aula começa com um número que muda entre modelos e termina com uma afirmação cuja
força é compatível com essas condições.

## Cronograma da rota principal

| Tempo | Slides | Bloco |
|---:|---:|---|
| 00:00–00:38 | 1–11 | orientação, base, problema e U07-A01 |
| 00:38–01:10 | 12–24 | regressão linear simples e U07-A02 |
| 01:10–01:42 | 25–36 | regressão múltipla, categorias e U07-A03 |
| 01:42–01:52 | — | intervalo |
| 01:52–02:22 | 37–48 | interação, diagnóstico e U07-A04 |
| 02:22–02:52 | 49–63 | regressão logística e U07-A05 |
| 02:52–03:37 | 64–74 | oficina U07-A06 |
| 03:37–03:52 | 75–76 | revisão por pares U07-A07 |
| 03:52–04:00 | 77–82 | retorno, síntese, saída e referências |

Os tempos exigem que as atividades conceituais sejam executadas em seu **recorte em
aula**. A versão completa continua nos notebooks. Se as fórmulas exigirem mais tempo,
abrevie os slides classificados como aprofundamento; não abrevie as pontes.

---

## Bloco 1 — Orientar, apresentar a base e produzir o problema

### Slide 1 — Unidade 7

**Intenção:** anunciar que a unidade estuda explicação associativa, não causalidade automática.

**Fala sugerida:** “Na unidade anterior observamos associações entre variáveis. Hoje
daremos um passo adicional: perguntar se uma associação permanece quando comparamos
casos semelhantes em outras características. Isso aumenta a precisão da comparação,
mas não transforma, por si só, associação em causa.”

**Ponte:** “Para saber onde chegaremos, vamos primeiro visualizar o percurso da aula.”

**Tempo/Prioridade:** 1 min · essencial.

### Slide 2 — Agenda

**Intenção:** oferecer um mapa e reduzir a ansiedade diante de vários termos novos.

**Fala sugerida:** percorra os seis itens como uma sequência: uma relação simples;
outras características; diferenças de inclinação; resposta sim/não; tradução dos
números; aplicação no projeto. Diga que os blocos não são técnicas independentes.

**Ponte:** “Essa sequência será avaliada pelo que vocês conseguirão fazer, não por
memorizar fórmulas.”

**Tempo/Prioridade:** 1 min · essencial.

### Slide 3 — Ao final, você deverá conseguir…

**Intenção:** converter conteúdos em ações observáveis.

**Fala sugerida:** destaque três capacidades: definir corretamente a comparação,
traduzir números para linguagem substantiva e reconhecer limites. Avise que cada
atividade exercitará uma dessas ações.

**Ponte:** “Essas capacidades formam um ciclo, que começa antes do cálculo.”

**Tempo/Prioridade:** 1 min · essencial.

### Slide 4 — O percurso da unidade

**Intenção:** mostrar o modelo como parte de uma cadeia argumentativa.

**Fala sugerida:** leia o diagrama da esquerda para a direita. Enfatize que
especificação vem antes da estimação e que diagnóstico devolve o modelo aos casos.
“O cálculo ocupa o meio do percurso; não substitui pergunta, fonte nem interpretação.”

**Interação:** peça que a turma identifique em qual etapa costuma concentrar mais atenção.

**Ponte:** “Para percorrer essa cadeia, precisamos conhecer a base e seus limites.”

**Tempo/Prioridade:** 2 min · essencial.

### Slide 5 — Base fictícia de municípios

**Intenção:** situar unidade de observação, respostas e explicativas antes do uso.

**Fala sugerida:** “Cada linha é um município fictício; não uma pessoa e não um
estado. Temos uma resposta contínua — equipamentos por 100 mil — e outra binária —
presença de biblioteca. Os padrões foram construídos para tornar conceitos visíveis.”
Reforce que não se fazem afirmações sobre municípios reais.

**Ponte:** “Agora veremos como esses casos aparecem nos arquivos que sustentam todos
os exemplos seguintes.”

**Tempo/Prioridade:** 2 min · essencial.

### Slide 6 — Arquivos da simulação municipal

**Intenção:** tornar concreto o registro de dados e sua proveniência.

**Fala sugerida:** primeiro percorra uma linha da tabela: identificador, região, renda,
urbanização, escolaridade e taxa de equipamentos. Depois contraste os arquivos:
o CSV contém observações; o JSON documenta geração, limite e alteração deliberada de
M150. “Proveniência não é decoração: ela orientará uma decisão de diagnóstico.”

**Interação:** pergunte qual é a unidade de `escolaridade` e qual é a unidade de
`equipamentos`.

**Ponte:** “Com a base conhecida, podemos observar a tensão que moverá toda a aula:
o número da renda muda quando o modelo muda.”

**Tempo/Prioridade:** 3 min · essencial.

### Slide 7 — Antes da teoria: a associação mudou

**Intenção:** produzir uma pergunta antes de apresentar regressão múltipla.

**Fala sugerida:** mantenha os dois números visíveis. “A mesma base e a mesma renda
produzem +0,703 num modelo e +0,574 em outro. Não escolham ainda o ‘melhor’. Perguntem
qual comparação cada número resume.”

**Interação:** dê 30 segundos para uma votação: primeiro número, segundo ou nenhum
como “verdadeira influência”. Solicite uma justificativa.

**Ponte:** “A resposta está no conjunto de condições que define cada coeficiente.”

**Tempo/Prioridade:** 3 min · essencial.

### Slide 8 — Nenhum coeficiente existe fora do modelo

**Intenção:** formular a tese central da unidade.

**Fala sugerida:** contraste “municípios que apenas diferem em renda na tabela” com
“perfis matematicamente igualados nos termos incluídos”. Explique que a segunda frase
é uma comparação condicional, não observação literal de dois municípios idênticos.

**Ponte:** “Para interpretar qualquer resultado, teremos então de tornar suas
condições visíveis.”

**Tempo/Prioridade:** 2 min · essencial.

### Slide 9 — O que precisamos examinar?

**Intenção:** transformar a tese em checklist de leitura.

**Fala sugerida:** agrupe as perguntas em três momentos: antes do ajuste — resposta,
variáveis e escala; durante — comparabilidade e ausências; depois — falhas e
sensibilidade. Não leia a lista como itens isolados.

**Ponte:** “Antes da primeira equação, vamos praticar o grau de força que uma
afirmação pode assumir.”

**Tempo/Prioridade:** 2 min · essencial.

### Slide 10 — U07-A01 · Graduar a afirmação

**Intenção:** ativar conhecimentos prévios e distinguir níveis de inferência.

**Condução:** duplas, 8 minutos. Na rota de aula, peça os itens 1, 2 e uma versão
associativa do item 3. Avise que a versão completa inclui os três níveis.

**Antes de iniciar:** esclareça que “explicação alternativa” não é desculpa genérica;
deve nomear uma característica plausivelmente ligada à renda e aos equipamentos.

**Ponte para o gabarito:** “Vamos comparar não apenas frases, mas o tipo de evidência
que cada verbo exige.”

**Tempo/Prioridade:** 8 min · atividade.

### Slide 11 — Gabarito U07-A01

**Intenção:** estabilizar vocabulário e abrir a regressão simples.

**Fala sugerida:** peça primeiro uma alternativa da turma. Em seguida, percorra a
escada: descrição observa padrão; associação condicionada declara termos incluídos;
causalidade imagina intervenção. Destaque que formulação causal pode ser hipótese
legítima, mas não conclusão deste desenho.

**Ponte:** “Para compreender a frase condicionada, precisamos primeiro aprender a
ler o coeficiente no modelo mínimo: uma resposta e uma explicativa.”

**Tempo/Prioridade:** 3 min · essencial.

---

## Bloco 2 — Regressão linear simples

### Slide 12 — Uma resposta, uma explicativa

**Intenção:** marcar a redução deliberada da complexidade.

**Fala sugerida:** “Começaremos com um modelo incompleto de propósito. Se não
conseguirmos interpretar uma inclinação simples, adicionar termos apenas multiplicará
a confusão.”

**Ponte:** “Antes da reta, olhemos os municípios como pontos.”

**Tempo/Prioridade:** 30 s · essencial.

### Slide 13 — Comece pelos casos

**Intenção:** ancorar a regressão na dispersão observada.

**Fala sugerida:** oriente o olhar: primeiro a nuvem, depois a direção geral, por fim
M150. “A reta resume uma tendência positiva; a distância dos pontos mostra tudo que
ela não descreve.”

**Interação:** pergunte se uma reta positiva implica que todo município de maior renda
tem mais equipamentos que todo município de menor renda.

**Ponte:** “Precisamos definir precisamente o que a reta afirma — e o que não afirma.”

**Tempo/Prioridade:** 2 min · essencial.

### Slide 14 — O que é regressão linear?

**Intenção:** apresentar o método em linguagem comum.

**Fala sugerida:** leia a tabela por papéis, não por nomes técnicos: casos entram,
uma quantidade é a resposta, renda organiza a comparação e o modelo devolve valores
previstos. Explique que “médio previsto” não significa que cada caso obedecerá à reta.

**Ponte:** “Agora vamos converter a curiosidade substantiva em papéis explícitos.”

**Tempo/Prioridade:** 2 min · essencial.

### Slide 15 — Da pergunta às variáveis

**Intenção:** ensinar especificação antes da fórmula.

**Fala sugerida:** mostre que a pergunta já contém unidade, resposta, explicativa e
alcance. Aponte a diferença entre “equipamentos” e “equipamentos por 100 mil”: o
denominador altera o que está sendo comparado.

**Ponte:** “Com os papéis definidos, a equação apenas compacta essa relação.”

**Tempo/Prioridade:** 2 min · essencial.

### Slide 16 — A reta é uma hipótese de forma

**Intenção:** traduzir a equação e resolver uma previsão.

**Fala sugerida:** apresente $\beta_0$ como ponto de partida, $\beta_1$ como mudança por
unidade e o resíduo como parte não descrita. Substitua renda 2.000 e obtenha 4,05.
Na figura, localize esse ponto na reta. “Linear” significa inclinação constante no
intervalo observado, não certeza.

**Ponte:** “A conta funciona em renda 2.000; mas o ponto de partida da reta, renda
zero, pode não ter significado substantivo.”

**Tempo/Prioridade:** 3 min · essencial.

### Slide 17 — O intercepto pode não ser substantivo

**Intenção:** impedir interpretação mecânica de todo coeficiente.

**Fala sugerida:** compare zero com o intervalo observado. “A equação precisa do
intercepto; nosso argumento histórico não precisa fingir que renda zero é um caso
comparável.” Diferencie necessidade matemática e relevância substantiva.

**Ponte:** “A inclinação, por outro lado, é central, mas sua unidade original é pouco
legível.”

**Tempo/Prioridade:** 1 min · aprofundamento.

### Slide 18 — Reexpresse a inclinação

**Intenção:** mostrar que escala de comunicação é uma decisão analítica.

**Fala sugerida:** multiplique a inclinação por 500 e acompanhe na figura a mudança
horizontal e vertical. Diga a frase inteira, incluindo unidade e “em média”.

**Interação:** peça à turma uma versão para aumento de 1.000 unidades, sem novo ajuste.

**Ponte:** “A inclinação resume a tendência; a diferença entre cada caso e essa
tendência recebe um nome.”

**Tempo/Prioridade:** 2 min · essencial.

### Slide 19 — Resíduo devolve a reta ao caso

**Intenção:** ligar modelo agregado e observação individual.

**Fala sugerida:** leia o segmento vertical como observado menos previsto. No modelo
simples, resolva M150: 8,40 menos 5,225, aproximadamente 3,175. “Resíduo positivo não
significa dado bom; significa observado acima do resumo.” Avise que o mesmo caso terá
outro resíduo quando a especificação mudar.

**Ponte:** “Podemos examinar um caso ou resumir quanto da variação total a reta
organiza.”

**Tempo/Prioridade:** 2 min · essencial.

### Slide 20 — R² responde a uma pergunta limitada

**Intenção:** interpretar ajuste sem causalidade.

**Fala sugerida:** evite derivar a fórmula. Explique que o denominador representa a
variação em torno da média e o numerador, a variação que restou nos resíduos. Traduza
41,2% e diga explicitamente que não é porcentagem causada pela renda.

**Ponte:** “Proporção de variação não informa o tamanho típico do erro na unidade que
usamos para falar de cultura.”

**Tempo/Prioridade:** 3 min · essencial.

### Slide 21 — Erro na unidade da resposta

**Intenção:** diferenciar R² de medidas de erro.

**Fala sugerida:** compare RMSE e MAE sem aprofundar a derivação. Destaque que ambos
voltam a “equipamentos por 100 mil”. O RMSE reage mais a erros grandes; por isso M150
terá mais peso nele.

**Ponte:** “Mesmo vários resumos numéricos podem esconder uma forma inadequada.”

**Tempo/Prioridade:** 1 min · aprofundamento.

### Slide 22 — Uma reta pode esconder estruturas

**Intenção:** preparar diagnóstico e modelos mais complexos.

**Fala sugerida:** selecione três riscos: curvatura, grupos com inclinações distintas
e casos extremos. Relacione cada um a uma pergunta visual. Não transforme a lista em
catálogo abstrato.

**Ponte:** “Vamos condensar essa leitura em uma conclusão curta e revisável.”

**Tempo/Prioridade:** 1 min · essencial.

### Slide 23 — U07-A02 · Ler uma regressão simples

**Intenção:** praticar interpretação completa.

**Condução:** 8 minutos em aula: itens 1, 2 e 5. Cada pessoa escreve; a dupla revisa
verbos. A inspeção detalhada de dois casos fica para a versão de 25 minutos no notebook.

**Ponte para o gabarito:** “Confiram se a frase contém unidade, escala, qualidade do
ajuste e limite, e não apenas o sinal do coeficiente.”

**Tempo/Prioridade:** 8 min · atividade.

### Slide 24 — Gabarito U07-A02

**Intenção:** modelar uma conclusão substantiva e limitada.

**Fala sugerida:** percorra tabela, casos e conclusão nessa ordem. No modelo simples,
M150 fica aproximadamente 3,18 acima da previsão; no modelo de interação usado mais
adiante, ficará cerca de 4,04 acima. Não misture resíduos de especificações distintas.
Enfatize que renda sozinha deixa informação não descrita.

**Ponte:** “Essa insuficiência motiva o próximo bloco: considerar outras diferenças
observadas no mesmo modelo.”

**Tempo/Prioridade:** 2 min · essencial.

---

## Bloco 3 — Regressão múltipla, condicionamento e categorias

### Slide 25 — Condicionar uma associação

**Intenção:** marcar a passagem de comparação bruta para perfis condicionais.

**Fala sugerida:** “Não estamos abandonando a regressão simples; estamos tornando
explícitas diferenças que ela misturava.”

**Ponte:** “O primeiro sinal dessa mudança aparece no próprio coeficiente da renda.”

**Tempo/Prioridade:** 30 s · essencial.

### Slide 26 — A pergunta ficou mais específica

**Intenção:** retomar os números da abertura com vocabulário já construído.

**Fala sugerida:** compare linha a linha. O modelo múltiplo tem melhor ajuste interno
e menor coeficiente para renda, mas isso não o torna automaticamente verdadeiro.
“Mudou a comparação, portanto mudou a resposta.”

**Ponte:** “Vejamos quais termos definem essa nova comparação.”

**Tempo/Prioridade:** 2 min · essencial.

### Slide 27 — Várias explicativas na mesma expressão

**Intenção:** generalizar a equação sem perder as variáveis concretas.

**Fala sugerida:** associe cada letra à variável e use a figura. Para renda, resolva
o bloco de 500 e inclua a cláusula “mantidos os demais termos”. Explique que manter
fixo é operação do modelo, não ato sobre municípios reais.

**Ponte:** “Essa cláusula é frequentemente resumida pela palavra ‘controlar’, que
precisa ser usada com cautela.”

**Tempo/Prioridade:** 3 min · essencial.

### Slide 28 — “Controlar” significa condicionar

**Intenção:** conter uma metáfora causal excessiva.

**Fala sugerida:** aponte para as setas e diga: “o modelo organiza comparações nos
termos observados; não domina o processo histórico nem corrige a fonte”. Use
“condicionado a” como tradução preferencial.

**Ponte:** “O limite mais evidente é tudo aquilo que o modelo não incluiu.”

**Tempo/Prioridade:** 2 min · essencial.

### Slide 29 — Variável omitida pode alterar o coeficiente

**Intenção:** mostrar que adicionar termos exige argumento.

**Fala sugerida:** dê um exemplo simples com política municipal ligada a renda e
equipamentos. Explique que a terceira condição depende do argumento causal e evita
controlar mecanicamente consequências da própria explicativa.

**Ponte:** “Até aqui as explicativas eram números. Região também pode entrar, mas não
como 1, 2, 3, 4 e 5.”

**Tempo/Prioridade:** 2 min · aprofundamento.

### Slide 30 — Categorias não são números ordenados

**Intenção:** introduzir indicadores e referência.

**Fala sugerida:** mostre o problema de atribuir números às regiões. Leia o indicador
Sudeste como uma pergunta de sim/não. Com cinco regiões, quatro colunas mais o
intercepto bastam; quando todas são zero, o caso pertence à referência.

**Ponte:** “A região sem coluna própria não foi apagada; ela ancora os contrastes.”

**Tempo/Prioridade:** 3 min · essencial.

### Slide 31 — A referência não desapareceu

**Intenção:** tornar a codificação interpretável.

**Fala sugerida:** leia cada coeficiente como frase comparativa com Centro-Oeste e
adicione “mantidos os termos numéricos”. A referência participa do ajuste e fornece o
ponto de comparação.

**Ponte:** “Se mudarmos esse ponto, mudam as frases dos coeficientes, mas não o que o
modelo prevê para cada caso.”

**Tempo/Prioridade:** 2 min · essencial.

### Slide 32 — Trocar a referência muda a frase, não a previsão

**Intenção:** separar parametrização e resultado substantivo.

**Fala sugerida:** use uma analogia de distância: dizer que uma cidade está 100 km ao
norte de A ou 50 km ao sul de B muda a origem da descrição, não sua localização.
Reforce que não se troca referência para fabricar sinal conveniente.

**Ponte:** “A forma mais segura de comunicar o conjunto dos termos é voltar a perfis
completos.”

**Tempo/Prioridade:** 2 min · essencial.

### Slide 33 — Perfis tornam o modelo legível

**Intenção:** converter coeficientes múltiplos em previsões substantivas.

**Fala sugerida:** percorra cada coluna antes da previsão. A diferença de 1,22 combina
várias mudanças; não atribua tudo à renda. Chame os perfis de cenários, não de
municípios típicos ou intervenções.

**Ponte:** “Perfis também evitam uma comparação enganosa entre coeficientes escritos
em escalas diferentes.”

**Tempo/Prioridade:** 2 min · essencial.

### Slide 34 — Coeficientes em escalas diferentes não competem

**Intenção:** impedir ranking mecânico de ‘importância’.

**Fala sugerida:** compare um real, um quilômetro e um ano. “O tamanho escrito depende
da régua.” Prefira mudanças plausíveis ou perfis e inclua teoria e incerteza.

**Ponte:** “Vamos praticar condicionamento, referência e perfis como partes da mesma
interpretação.”

**Tempo/Prioridade:** 1 min · essencial.

### Slide 35 — U07-A03 · Controle e referência

**Intenção:** testar a leitura integrada do modelo múltiplo.

**Condução:** grupos de três, 8 minutos, itens 1–3. Distribua papéis: interpretação,
conferência de escala e revisão da linguagem. Os perfis ficam para a versão completa.

**Ponte para o gabarito:** “A resposta deve declarar o modelo, a comparação e a
referência; um sinal isolado não basta.”

**Tempo/Prioridade:** 8 min · atividade.

### Slide 36 — Gabarito U07-A03

**Intenção:** consolidar condicionamento e preparar interação.

**Fala sugerida:** mostre que Centro-Oeste continua no ajuste e que os perfis não são
efeitos de intervenção. Retome a diferença entre 0,703 e 0,574 como produto de
especificações distintas.

**Ponte:** “Mesmo o modelo múltiplo ainda supõe uma inclinação comum. E se a associação
entre urbanização e equipamentos variar conforme escolaridade?”

**Tempo/Prioridade:** 2 min · essencial.

---

## Bloco 4 — Interação, diagnóstico e sensibilidade

### Slide 37 — A inclinação depende do contexto?

**Intenção:** apresentar a nova insuficiência do modelo anterior.

**Fala sugerida:** “Condicionar adicionou características. Interagir pergunta se uma
característica modifica a associação da outra.”

**Ponte:** “Vamos transformar isso numa pergunta concreta.”

**Tempo/Prioridade:** 30 s · essencial.

### Slide 38 — Interação modifica a pergunta

**Intenção:** introduzir interação por meio de linguagem substantiva.

**Fala sugerida:** contraste “urbanização está associada?” com “essa associação muda
em diferentes níveis de escolaridade?”. Na figura, destaque que retas não paralelas
representam inclinações diferentes.

**Ponte:** “Para interpretar o modelo, precisamos escolher um ponto de comparação
legível para urbanização e escolaridade.”

**Tempo/Prioridade:** 2 min · essencial.

### Slide 39 — Centralizar torna o ponto de comparação legível

**Intenção:** explicar centralização antes do produto de interação.

**Fala sugerida:** resolva 80 menos 74,16. Diga que zero passa a significar média, não
ausência da característica. Enfatize que previsões não mudam; mudam intercepto e
leitura dos termos.

**Ponte:** “Com zeros substantivamente úteis, o produto das duas diferenças passa a
representar a interação.”

**Tempo/Prioridade:** 3 min · essencial.

### Slide 40 — O modelo de interação

**Intenção:** mostrar por que não existe uma única inclinação.

**Fala sugerida:** não derive cálculo diferencial. Leia a segunda expressão como:
inclinação de urbanização = parte comum + ajuste conforme escolaridade. Resolva o
exemplo de 12 anos e localize a reta correspondente na figura.

**Ponte:** “Como o coeficiente do produto é difícil de imaginar, interpretaremos
previsões em valores reconhecíveis.”

**Tempo/Prioridade:** 3 min · essencial.

### Slide 41 — Leia previsões, não apenas o produto

**Intenção:** traduzir interação para três cenários.

**Fala sugerida:** compare as inclinações em 8, 10 e 12 anos, não apenas alturas em um
ponto. Declare que as linhas são previsões condicionais. “Agora sabemos como o resumo
varia; ainda não sabemos onde ele falha para casos concretos.”

**Ponte:** “Essa segunda pergunta pertence ao diagnóstico.”

**Tempo/Prioridade:** 2 min · essencial.

### Slide 42 — Diagnóstico pergunta onde o resumo falha

**Intenção:** conectar interação e inspeção dos casos.

**Fala sugerida:** leia o fluxo: valores previstos, resíduos, casos e decisão.
Diagnóstico não é caça a dados incômodos; é abertura do modelo à crítica documental e
substantiva.

**Ponte:** “A base foi construída com um caso que torna essa responsabilidade visível.”

**Tempo/Prioridade:** 1 min · essencial.

### Slide 43 — Resíduos revelam o caso M150

**Intenção:** reencontrar o caso anunciado na proveniência.

**Fala sugerida:** localize M150, compare 8,40 observado com 4,36 previsto e relembre
o JSON. “O gráfico detecta diferença; a proveniência ajuda a interpretá-la.”

**Ponte:** “Mas estar distante verticalmente não é a única forma de um caso chamar
atenção.”

**Tempo/Prioridade:** 2 min · essencial.

### Slide 44 — Alavancagem e resíduo não são a mesma coisa

**Intenção:** distinguir três diagnósticos.

**Fala sugerida:** use perguntas: o resultado foi mal previsto? O perfil de
explicativas é incomum? O ajuste mudaria sem o caso? Associe-as a resíduo, alavancagem
e influência. Compare M150 e M145.

**Ponte:** “Para saber se uma decisão altera a conclusão, precisamos manter e comparar
duas versões do modelo.”

**Tempo/Prioridade:** 2 min · aprofundamento.

### Slide 45 — Sensibilidade mantém as duas versões

**Intenção:** ensinar transparência diante de decisão contestável.

**Fala sugerida:** observe ajuste e interação nas duas linhas. Não conclua apenas que
“sem M150 é melhor”; diga que a pergunta é quanto a conclusão depende dele. A
proveniência justifica o teste, não o apagamento silencioso.

**Ponte:** “Melhorar uma métrica nunca é razão suficiente para excluir uma observação.”

**Tempo/Prioridade:** 2 min · essencial.

### Slide 46 — “Melhorar o ajuste” não justifica excluir

**Intenção:** recentrar a decisão na fonte e no desenho.

**Fala sugerida:** escolha dois contrastes: erro de entrada pode ser corrigido; evento
histórico excepcional pode ser justamente o objeto de interesse. A mesma aparência
estatística pode exigir decisões opostas.

**Ponte:** “Vamos agora construir uma decisão que combine interação, diagnóstico e
proveniência.”

**Tempo/Prioridade:** 1 min · essencial.

### Slide 47 — U07-A04 · Interação e diagnóstico

**Intenção:** integrar interpretação e decisão auditável.

**Condução:** duplas, 8 minutos, itens 1, 3 e 5. Peça uma frase sobre inclinação, uma
leitura de M150 e uma decisão reconstruível. Gráfico completo fica no notebook.

**Ponte para o gabarito:** “Confiram se a decisão preserva as duas versões e distingue
resultado estatístico de justificativa documental.”

**Tempo/Prioridade:** 8 min · atividade.

### Slide 48 — Gabarito U07-A04

**Intenção:** fechar resposta contínua e preparar resposta binária.

**Fala sugerida:** destaque que a interação sugere heterogeneidade, mas é sensível ao
caso. A conclusão combina fórmula, figura, proveniência e limite causal.

**Ponte:** “Até aqui previmos uma quantidade. Agora manteremos a lógica de
condicionamento, mas a resposta será uma ocorrência: biblioteca, sim ou não.”

**Tempo/Prioridade:** 2 min · essencial.

---

## Bloco 5 — Regressão logística

### Slide 49 — Quando a resposta é sim ou não

**Intenção:** anunciar mudança no tipo de resposta, não abandono do percurso.

**Fala sugerida:** “Pergunta, explicativas, condicionamento, diagnóstico e limites
continuam. O que muda é a forma matemática necessária para uma resposta binária.”

**Ponte:** “Primeiro, vejamos por que uma reta é inadequada.”

**Tempo/Prioridade:** 30 s · essencial.

### Slide 50 — Uma reta não respeita probabilidades

**Intenção:** motivar logística por um problema concreto.

**Fala sugerida:** explique que 0 e 1 são categorias observadas, enquanto o modelo
produz probabilidades. Uma reta ilimitada pode sair de 0–1 e impõe mudança constante.

**Ponte:** “Precisamos de um método que preserve probabilidades válidas.”

**Tempo/Prioridade:** 2 min · essencial.

### Slide 51 — O que é regressão logística?

**Intenção:** definir o método antes da fórmula.

**Fala sugerida:** percorra papéis como no slide 14. Diferencie quantidade de
bibliotecas e probabilidade de presença. “0,82 é uma expectativa para um perfil, não
uma fração de biblioteca e não uma garantia.”

**Ponte:** “Comparar os dois modelos lado a lado ajuda a separar o que permanece e o
que muda.”

**Tempo/Prioridade:** 2 min · essencial.

### Slide 52 — Linear e logística: o que muda?

**Intenção:** relacionar o novo ao conhecido.

**Fala sugerida:** leia as linhas resposta, saída e forma. Não aprofunde ainda
log-chance; anuncie que será construída em duas etapas. Destaque que categorias e
interações podem aparecer em ambos.

**Ponte:** “Para chegar ao coeficiente logístico, começaremos por distinguir
probabilidade de chance.”

**Tempo/Prioridade:** 2 min · essencial.

### Slide 53 — Probabilidade e chance

**Intenção:** introduzir a primeira transformação com exemplos simples.

**Fala sugerida:** resolva 0,20: uma ocorrência e quatro não ocorrências. Depois 0,75:
três para uma. Mostre que chance 3 não é probabilidade 3; são escalas distintas.

**Interação:** peça a chance de $p=0,50$ antes de revelar a linha.

**Ponte:** “A chance é positiva, mas ainda limitada de um lado; o logaritmo a coloca
numa escala sem esses limites.”

**Tempo/Prioridade:** 3 min · essencial.

### Slide 54 — Do intervalo limitado à reta

**Intenção:** visualizar probabilidade → chance → logito.

**Fala sugerida:** siga o diagrama da esquerda para a direita. Não faça derivação do
logaritmo. Explique sua função: permitir uma combinação linear que depois retorna a
uma probabilidade válida.

**Ponte:** “Agora a fórmula logística deixa de parecer arbitrária: ela registra essa
ida e volta entre escalas.”

**Tempo/Prioridade:** 2 min · essencial.

### Slide 55 — O modelo logístico

**Intenção:** apresentar as duas direções da transformação.

**Fala sugerida:** na primeira expressão, as explicativas produzem log-chance. Na
segunda, $\eta$ retorna à probabilidade. Resolva $\eta=0$ e localize 0,50 no centro da
curva.

**Ponte:** “Os coeficientes estão em log-chances; exponenciá-los produz uma escala
mais comunicável.”

**Tempo/Prioridade:** 3 min · essencial.

### Slide 56 — Exponenciar produz razão de chances

**Intenção:** interpretar sinal e magnitude sem confundir com probabilidade.

**Fala sugerida:** explique OR como fator multiplicativo nas chances. Resolva
$e^{0,480}=1,62$. Repita: não é 62 pontos percentuais e não é probabilidade 1,62.

**Ponte:** “Ainda falta dizer o que significa uma unidade de urbanização quando as
explicativas usam réguas tão diferentes.”

**Tempo/Prioridade:** 3 min · essencial.

### Slide 57 — Por que padronizar?

**Intenção:** explicar a unidade dos OR apresentados.

**Fala sugerida:** mostre média, desvio e exemplo de renda. “Zero passa a ser a média;
um significa um desvio acima.” Diga que padronização não torna variáveis equivalentes
em significado e não elimina a necessidade de perfis.

**Ponte:** “Com essa unidade comum declarada, podemos ler a tabela de razões de chances.”

**Tempo/Prioridade:** 3 min · essencial.

### Slide 58 — Saída do modelo fictício

**Intenção:** praticar leitura condicionada de OR.

**Fala sugerida:** leia apenas dois termos em voz alta: renda acima de 1 e distância
próxima de 1. Inclua “por um desvio-padrão” e “demais termos fixos”. Não faça ranking
causal. Destaque a ausência de intervalos como limite didático.

**Ponte:** “Razões de chances ainda são abstratas; voltaremos à probabilidade para dois
perfis de urbanização.”

**Tempo/Prioridade:** 2 min · essencial.

### Slide 59 — Volte das chances à probabilidade

**Intenção:** comunicar mudança em escala familiar.

**Fala sugerida:** localize 50% e 90% no eixo horizontal e 0,443 e 0,820 no vertical.
Declare o que permaneceu na média. A diferença 0,38 pertence a esses cenários, não é
efeito universal da urbanização.

**Ponte:** “A curva mostra por que um mesmo fator nas chances não produz sempre a
mesma diferença de probabilidade.”

**Tempo/Prioridade:** 2 min · essencial.

### Slide 60 — A mesma razão não implica a mesma diferença

**Intenção:** prevenir interpretação linear de OR.

**Fala sugerida:** use a curva em S: no centro há maior deslocamento vertical; nas
extremidades, menor. Por isso, peça valores iniciais e perfis mantidos fixos sempre
que alguém disser “aumenta a chance”.

**Ponte:** “Mesmo uma interpretação interna correta ainda não garante desempenho em
novos casos.”

**Tempo/Prioridade:** 1 min · aprofundamento.

### Slide 61 — Ajuste interno não é desempenho futuro

**Intenção:** delimitar Unidade 7 e preparar Unidade 8.

**Fala sugerida:** diferencie descrever a própria base e avaliar generalização. Diga
que treino, teste, calibração e justiça serão tratados na classificação. Evite abrir
um segundo curso aqui.

**Ponte:** “Antes de aplicar qualquer modelo ao projeto, vamos conferir se conseguimos
traduzir chance e probabilidade corretamente.”

**Tempo/Prioridade:** 1 min · reserva/aprofundamento.

### Slide 62 — U07-A05 · Interpretar ocorrência

**Intenção:** verificar as traduções essenciais.

**Condução:** 8 minutos, itens 1, 2 e 4. Cada pessoa calcula; a dupla verifica unidade
da padronização e troca verbo causal por associativo. A comparação dos perfis fica na
versão completa.

**Ponte para o gabarito:** “Uma resposta completa precisa circular entre probabilidade,
chance, OR e linguagem substantiva sem confundir as escalas.”

**Tempo/Prioridade:** 8 min · atividade.

### Slide 63 — Gabarito U07-A05

**Intenção:** consolidar a logística e abrir a oficina.

**Fala sugerida:** corrija as duas conversões; leia a OR com sua unidade; compare as
duas probabilidades; termine com a frase associativa. Pergunte qual cláusula impede
uma leitura causal.

**Ponte:** “Agora temos duas famílias de modelos. O desafio final não é escolher a
mais sofisticada, mas decidir se alguma é pertinente e documentar o argumento.”

**Tempo/Prioridade:** 2 min · essencial.

---

## Bloco 6 — Oficina e projeto cumulativo

### Slide 64 — Oficina

**Intenção:** mudar de exposição para produção.

**Fala sugerida:** “A oficina reúne as peças da aula. Não adotar regressão pode ser
uma decisão metodologicamente superior, desde que sustentada.”

**Ponte:** “Primeiro, relembremos quais elos um resultado completo precisa conter.”

**Tempo/Prioridade:** 30 s · essencial.

### Slide 65 — O argumento precisa de todos os elos

**Intenção:** oferecer uma rubrica visual para a produção.

**Fala sugerida:** percorra pergunta, especificação, ajuste, diagnóstico, casos e
afirmação. Diga que a tabela de coeficientes ocupa apenas um elo. Peça que as equipes
usem a cadeia como checklist.

**Ponte:** “Antes do primeiro elo computacional, existe uma decisão: o modelo é
pertinente para a pergunta e a base?”

**Tempo/Prioridade:** 1 min · essencial.

### Slide 66 — Antes de modelar, verifique a pertinência

**Intenção:** legitimar a não adoção fundamentada.

**Fala sugerida:** destaque resposta definida, variação, comparabilidade e número de
casos. “Não fabriquem linhas nem convertam conceitos em números apenas para cumprir a
técnica.”

**Ponte:** “A entrega deve começar registrando essa decisão.”

**Tempo/Prioridade:** 1 min · essencial.

### Slide 67 — U07-A06 · Incremento do relatório-notebook

**Intenção:** definir o produto da oficina.

**Condução:** explique que os 40 minutos iniciam uma seção que será concluída na
versão de 70 minutos. Confirme que ninguém criará outro relatório. Peça que cada equipe
escolha caminho e produza ao menos pertinência, especificação e uma saída comentada.

**Ponte:** “Há três caminhos aceitáveis; o critério é adequação, não complexidade.”

**Tempo/Prioridade:** apresentação 2 min; trabalho distribuído até o slide 72.

### Slide 68 — Três caminhos legítimos

**Intenção:** permitir escolha consciente.

**Fala sugerida:** linear para quantidade; logística para ocorrência; não adoção para
base ou pergunta incompatível. Peça às equipes que anunciem seu caminho em uma frase.

**Ponte:** “Qualquer caminho começa com decisões escritas antes do código.”

**Tempo/Prioridade:** 1 min · essencial.

### Slide 69 — Especifique antes do código

**Intenção:** fornecer formulário de pré-especificação.

**Fala sugerida:** indique que cada linha previne uma ambiguidade posterior. Dê 6
minutos para preencher resposta, explicativas, categorias e eventual transformação.
Interação ou exclusão só entram se houver pergunta e justificativa.

**Ponte:** “Depois de especificar, o resultado precisa aparecer junto de sua leitura.”

**Tempo/Prioridade:** 7 min · atividade.

### Slide 70 — Mostre resultado e interpretação juntos

**Intenção:** orientar a seção analítica do notebook.

**Fala sugerida:** peça uma figura ou tabela curta, um diagnóstico e um caso concreto.
Reserve 18 minutos para execução e redação. Circule perguntando: “o que esta saída
responde?” e “qual frase ela não autoriza?”.

**Ponte:** “A força dessa frase deve corresponder ao desenho e às evidências.”

**Tempo/Prioridade:** 19 min · atividade.

### Slide 71 — Uma escada de linguagem

**Intenção:** apoiar a redação da conclusão.

**Fala sugerida:** peça que cada equipe identifique em qual degrau sua evidência está.
Reserve 5 minutos para reescrever verbos fortes. Causalidade não é proibida como
pergunta; precisa de desenho e hipóteses que a atividade atual não oferece.

**Ponte:** “Vamos organizar os minutos restantes para que a seção tenha começo, meio
e limite explícito.”

**Tempo/Prioridade:** 6 min · atividade.

### Slide 72 — Roteiro dos 70 minutos

**Intenção:** relacionar recorte em aula e versão completa.

**Fala sugerida:** mostre que a turma está produzindo uma versão parcial em 40 minutos.
Marque quais etapas deverão ser concluídas posteriormente. Reserve os minutos finais
do bloco para salvar, nomear pendências e registrar o próximo passo.

**Ponte:** “Antes de encerrar a oficina, comparem a estrutura de vocês com um exemplo
de entrega.”

**Tempo/Prioridade:** 3 min · essencial.

### Slide 73 — Gabarito U07-A06 — 1/2

**Intenção:** oferecer exemplo de especificação, não molde obrigatório.

**Fala sugerida:** identifique pergunta, unidade, resposta, escala da renda,
condicionantes e diagnóstico. Pergunte a uma equipe onde esses elementos aparecem em
seu trabalho.

**Ponte:** “A especificação só se completa quando os números são convertidos em uma
conclusão limitada.”

**Tempo/Prioridade:** 2 min · essencial.

### Slide 74 — Gabarito U07-A06 — 2/2

**Intenção:** modelar o fechamento da análise.

**Fala sugerida:** destaque quatro movimentos: comparar modelos; indicar mudança do
coeficiente; inspecionar M150; limitar a causalidade. Reforce que não adoção pode ter
a mesma qualidade argumentativa.

**Ponte:** “Agora outra equipe verificará se esses elos são visíveis sem explicação oral.”

**Tempo/Prioridade:** 2 min · essencial.

---

## Bloco 7 — Revisão, retorno e fechamento

### Slide 75 — U07-A07 · Afirmação, evidência e limite

**Intenção:** testar autonomia comunicativa do notebook.

**Condução:** revisão em pares, 10 minutos. O leitor não pergunta ao autor. Deve
registrar um ponto claro, uma dúvida e uma mudança prioritária. O autor decide e
documenta.

**Ponte para o gabarito:** “O objetivo não é uniformizar textos, mas verificar se a
cadeia argumentativa pode ser reconstruída.”

**Tempo/Prioridade:** 10 min · atividade.

### Slide 76 — Gabarito U07-A07

**Intenção:** mostrar feedback específico e acionável.

**Fala sugerida:** contraste “está confuso” com a dúvida concreta sobre termos fixos.
Mostre que a mudança prioritária liga figura, condicionantes e M150. Peça que os
autores registrem aceitar ou justificar não aceitar o comentário.

**Ponte:** “Voltaremos agora ao número que abriu a aula e veremos o que podemos dizer
depois de todo o percurso.”

**Tempo/Prioridade:** 2 min · essencial.

### Slide 77 — Retorno ao exemplo inicial

**Intenção:** fechar o arco narrativo.

**Fala sugerida:** reapresente 0,703 e 0,574. A resposta à pergunta inicial não é
escolher o “verdadeiro”; é declarar a comparação de cada um e preferir a especificação
por argumento, não por aparência. Leia a frase permitida e a frase proibida.

**Ponte:** “Essa disciplina analítica deve aparecer no projeto cumulativo.”

**Tempo/Prioridade:** 2 min · essencial.

### Slide 78 — O que entra no projeto cumulativo?

**Intenção:** tornar a continuidade da entrega explícita.

**Fala sugerida:** peça que cada equipe marque o que já iniciou e o que continua
pendente. Destaque pertinência, previsão substantiva, falha do modelo e sensibilidade.

**Ponte:** “Esses itens condensam as sete ideias centrais da unidade.”

**Tempo/Prioridade:** 1 min · essencial.

### Slide 79 — Síntese

**Intenção:** recuperar o percurso como relações, não lista para memorização.

**Fala sugerida:** conecte em cadeia: especificação define coeficiente; condicionamento
não garante causa; categorias criam contrastes; interação contextualiza inclinações;
resíduos retornam aos casos; logística exige tradução; diagnóstico integra o resultado.

**Ponte:** “A última tarefa é produzir uma frase que revele essa cadeia.”

**Tempo/Prioridade:** 1 min · essencial.

### Slide 80 — Saída · Uma frase que você sustentaria

**Intenção:** obter evidência individual de aprendizagem.

**Condução:** peça preenchimento individual. Se não houver tempo para compartilhar,
recolha no diário de pesquisa. Aceite não adoção fundamentada.

**Ponte:** “Guardem a frase; ela será o critério para revisar a seção do projeto.”

**Tempo/Prioridade:** 4–5 min · atividade. Na rota apertada, iniciar em aula e concluir
imediatamente após.

### Slides 81–82 — Referências

**Intenção:** documentar sustentação acadêmica e caminhos de aprofundamento.

**Fala sugerida:** não leia a bibliografia. Aponte Gelman, Hill e Vehtari para
interpretação de regressão; Hosmer e colaboradores para logística; Hernán e Robins
para inferência causal; Underwood e Drucker para a articulação com Humanidades
Digitais. Reforce a natureza fictícia da base.

**Tempo/Prioridade:** exibir ao final; reserva.

---

## Registro após a aula

Preencher antes da próxima oferta:

- **Transição que funcionou melhor:**
- **Transição que ainda pareceu abrupta:**
- **Dúvida matemática recorrente:**
- **Slide que exigiu mais tempo:**
- **Aprofundamento encaminhado ao notebook:**
- **Atividade que ultrapassou o recorte:**
- **Alteração recomendada nos slides:**
- **Alteração recomendada neste roteiro:**
