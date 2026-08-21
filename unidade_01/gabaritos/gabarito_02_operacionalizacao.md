# Gabarito orientativo — Representação e operacionalização

## 0. Retomada — exemplo de resolução

**Pergunta delimitada recuperada do Notebook 01:** Como a categoria temática
“progresso” se distribui entre editoriais, notícias e cartas dos três periódicos
da coleção didática, entre 1890 e 1905?

**Expressão que precisa ser definida:** “categoria temática ‘progresso’”. É
necessário estabelecer se ela será atribuída pela presença da palavra, pela
leitura do argumento, por um vocabulário controlado ou por outra regra. Também é
preciso decidir se um documento poderá receber mais de um tema.

**Raciocínio:** recuperar a pergunta impede operacionalizar um conceito isolado.
A expressão escolhida é justamente o ponto em que uma decisão teórica precisará
ser convertida em regra observável.

## 1. Leitura da tabela e resultado do experimento

### Unidade de análise

Na tabela de exemplo:

- há três unidades;
- cada linha representa um documento;
- `id` identifica a unidade;
- `ano`, `genero` e `tema` registram características atribuídas aos documentos.

Não seria adequado afirmar que existem três jornais, três autores ou três temas
distintos apenas porque existem três linhas.

### Categorias exclusivas e múltiplas

O experimento produz a seguinte comparação:

| Tema | Tema dominante | Múltiplos temas |
|---|---:|---:|
| educação | 2 | 2 |
| trabalho | 1 | 2 |
| progresso | 0 | 1 |

A representação dominante não registra “progresso” porque esse tema aparece
apenas como tema secundário de D001. “Trabalho” passa de uma para duas
ocorrências porque também foi atribuído como tema secundário de D003. Na
representação múltipla, a soma é cinco, embora existam apenas três documentos,
pois um documento pode contribuir para mais de uma categoria.

A representação dominante permite uma contagem direta, mas não registra que um
documento pode tratar simultaneamente de educação e progresso ou de educação e
trabalho. A representação com múltiplos temas preserva coexistências, mas exige
decidir:

- se cada tema terá o mesmo peso;
- como serão calculadas frequências;
- como tratar divergências entre anotadores;
- qual regra define a presença de um tema.

### Resolução das quatro perguntas do experimento

1. **Por que “progresso” desaparece?** D001 possui “educação” como tema
   dominante e também “progresso” na lista de temas atribuídos. Ao conservar
   apenas o dominante, a ocorrência secundária é descartada.
2. **Por que “trabalho” passa de uma para duas ocorrências?** Ele é dominante em
   D002 e secundário em D003. A representação múltipla contabiliza ambos.
3. **Em qual modelo a soma supera o número de documentos?** No modelo de temas
   múltiplos. Há três documentos e cinco relações documento–tema. A unidade de
   contagem passou a ser a atribuição temática, embora a unidade de análise possa
   continuar sendo o documento.
4. **Qual modelo é mais adequado?** A resposta depende da pergunta. Para localizar
   apenas o enquadramento principal segundo uma regra explícita, o modelo
   dominante pode bastar. Para investigar coexistência temática, o modelo
   múltiplo é necessário. Uma resposta adequada declara o objetivo e reconhece o
   custo ou a perda da escolha.

**Exemplo de interpretação indevida:** “Há mais temas do que documentos, logo os
dados estão duplicados.” Não necessariamente: a contagem múltipla mede relações
documento–tema, e um documento pode participar de várias relações.

### Exemplo de tratamento de uma categoria histórica

Suponha que um registro utilize o termo histórico “artista” para descrever uma
ocupação. Não se deve substituí-lo automaticamente pela acepção contemporânea de
profissional das artes.

| Campo | Exemplo preenchido |
|---|---|
| `termo_na_fonte` | artista |
| `categoria_analitica` | trabalhador de ofício, provisoriamente |
| `agente_classificador` | escrivão responsável pelo registro |
| `regra_de_correspondencia` | classificação apoiada no contexto do documento e em bibliografia sobre o vocabulário ocupacional do período |
| `incerteza` | média; confirmar o sentido em ocorrências próximas e fontes correlatas |

**Raciocínio:** o termo original é preservado; a normalização é separada e
provisória; autoria, regra e dúvida permanecem rastreáveis. Se o contexto não
permitir decidir, a categoria analítica pode ficar como “indeterminada” em vez de
forçar uma equivalência.

## 2. Mapa de operacionalização — resposta-modelo

| Conceito | Dimensão | Indicador | Unidade de análise | Variável ou categoria | Fonte | Regra | Limitação |
|---|---|---|---|---|---|---|---|
| Centralidade do tema educação | Presença temática | Tema dominante atribuído | Documento | `tema_dominante` | Texto integral | Após leitura, atribuir uma categoria principal segundo guia | Força exclusividade e perde temas secundários |
| Centralidade do tema educação | Extensão da discussão | Proporção de palavras em trechos anotados como educação | Documento | `proporcao_educacao` | Texto integral e anotação de trechos | Dividir palavras dos trechos pertinentes pelo total do documento | Extensão não equivale a importância discursiva |

### Comparação

A primeira alternativa é simples, transparente e adequada a uma exploração
inicial, mas reduz a ambiguidade. A segunda representa melhor a extensão do
debate, porém depende de segmentação e anotação mais trabalhosas. Nenhuma mede
diretamente “importância histórica”. A escolha depende do sentido de
centralidade adotado na pergunta.

### Como o mapa foi construído

1. **Conceito:** “centralidade” é o problema teórico; não é uma coluna pronta.
2. **Dimensões:** presença e extensão são dois aspectos possíveis do conceito.
3. **Indicadores:** tema dominante e proporção de palavras são traços observáveis,
   mas nenhum equivale automaticamente à centralidade.
4. **Unidade:** o documento é o caso sobre o qual as duas medidas serão
   registradas, permitindo compará-las.
5. **Variáveis:** `tema_dominante` e `proporcao_educacao` tornam a regra
   operacional explícita.
6. **Fontes e regras:** texto integral, anotação e guia de codificação permitem
   reconstruir a produção dos valores.
7. **Limitações:** cada alternativa registra uma perda específica, em vez da frase
   genérica “os dados podem ter viés”.

### Exemplo de comparação e revisão em dupla

**Parágrafo antes da revisão:** “A proporção de palavras é melhor porque é mais
precisa do que uma categoria.”

**Comentário do colega:** a frase confunde precisão numérica com validade. Uma
proporção pode ser calculada de modo exato e ainda representar mal a centralidade;
é necessário explicar como os trechos serão identificados e por que extensão é
um indicador pertinente.

**Parágrafo revisado:** “O tema dominante permite uma exploração simples da
presença, mas apaga coexistências. A proporção de palavras preserva diferenças de
extensão, porém depende da anotação dos trechos e não mede, por si só, importância
histórica. Para minha pergunta, começaria pela presença categorial para localizar
casos e usaria a extensão apenas como pista complementar para releitura.”

**Por que a revisão melhora a resposta:** ela compara ganhos e perdas, relaciona a
escolha à pergunta e não apresenta uma medida numérica como naturalmente
superior.

## 3. Respostas esperadas para a reflexão

### O que aconteceria se a unidade fosse alterada?

Mudar de documento para parágrafo aumentaria o número de unidades e permitiria
examinar variação interna, mas as conclusões passariam a tratar de parágrafos.
Agregar por periódico reduziria a variação visível e produziria afirmações sobre
os periódicos.

### A categoria existe na fonte ou foi criada?

No exemplo, `tema_dominante` é uma categoria analítica produzida pelo
pesquisador. Termos usados pelos documentos podem informar a decisão, mas não
são automaticamente equivalentes à categoria.

### Como registrar ambiguidade?

Respostas possíveis incluem múltiplas categorias, campo de incerteza, comentário
do anotador, categoria “indeterminado” e dupla anotação. A escolha deve ser
documentada.

### Que interpretação seria indevida?

Seria indevido concluir que o documento considera educação seu tema socialmente
mais importante apenas porque recebeu a categoria dominante “educação”.

## 4. Critérios de correção

Avaliar se o estudante:

- diferencia conceito e indicador;
- identifica uma unidade sobre a qual a afirmação pode ser feita;
- formula uma regra observável;
- indica a fonte do valor;
- compara alternativas reais;
- reconhece perdas e ambiguidades.

Não avaliar pela sofisticação da variável. Uma operacionalização simples,
coerente e auditável é preferível a uma medida complexa sem justificativa.

### Exemplo de devolutiva

> O conceito e as duas dimensões estão claros, e a unidade de análise é coerente.
> Revise a regra da segunda alternativa: ainda não está definido como um trecho
> será reconhecido como pertinente. Acrescente um procedimento para casos
> ambíguos e explique se mais de um tema poderá ser atribuído ao documento.
