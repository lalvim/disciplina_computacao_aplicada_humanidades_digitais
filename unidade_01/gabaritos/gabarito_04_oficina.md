# Gabarito orientativo — Oficina do projeto

Este arquivo apresenta uma resposta-modelo completa. Ela demonstra coerência
entre as partes, mas não deve ser usada como molde temático obrigatório.

## Como acompanhar o exemplo de resolução

O projeto-modelo reutiliza o mesmo caso dos gabaritos anteriores. A resolução
segue quatro movimentos:

1. recuperar os produtos parciais, sem copiá-los automaticamente;
2. verificar se pergunta, unidade, corpus e operacionalização continuam
   compatíveis;
3. explicitar a cadeia entre operação, resultado, evidência e interpretação;
4. usar autoavaliação e parecer do colega para justificar uma revisão.

Cada seção abaixo apresenta uma decisão e sua consequência para as demais.

## 1. Identificação

**Título provisório:** Progresso em diferentes gêneros da coleção didática de
periódicos.

**Fenômeno:** Formas de enquadramento do progresso em debates jornalísticos
sobre educação e trabalho.

**Contexto:** Três periódicos fictícios, com documentos atribuídos ao período
entre 1890 e 1905.

## 2. Formulação

**Motivação humanística:** Conceitos como progresso podem organizar argumentos
e legitimar posições distintas. Comparar sua presença entre gêneros pode ajudar
a localizar documentos para uma análise contextual aprofundada.

**Conceito e autores de referência:** A noção de dados construídos será
fundamentada em Drucker (2011) e confrontada com a proposta de dados situados de
Lavin (2021). D'Ignazio e Klein (2020) orientarão a análise de poder e contexto
nas categorias.

**Questão ampla:** Como o progresso foi mobilizado em debates públicos sobre
educação e trabalho?

**Pergunta delimitada:** Como a atribuição do tema “progresso” varia entre
editoriais, notícias e cartas dos três periódicos da coleção didática, entre
1890 e 1905?

**Finalidade predominante:** Descritiva, pois a pergunta caracteriza como a
categoria se distribui.

**Estrutura analítica inicial:** Comparativa, pois confronta gêneros
documentais. Uma associação entre gênero e tema poderia ser explorada como
etapa secundária, sem ser tomada automaticamente como explicação causal.

**Tarefa computacional:** Filtrar documentos, agrupar por gênero e calcular a
frequência absoluta e relativa da categoria “progresso”.

**O que mudou em relação ao Notebook 01:** a pergunta deixou de falar apenas em
“aparecer” e passou a nomear explicitamente a atribuição categorial. A mudança
evita sugerir que o tema existe pronto no texto e alinha a pergunta aos dados
efetivamente disponíveis.

## 3. Delimitação

**Unidade de análise:** Documento.

**Fontes:** Tabela de registros, metadados da coleção e, em uma pesquisa real,
texto integral ligado a cada registro.

**Universo de interesse:** Debates jornalísticos do período sobre educação,
trabalho e progresso.

**Corpus disponível:** Doze registros fictícios. O corpus serve apenas para
demonstrar o desenho da pesquisa.

**Recorte:** Documentos entre 1890 e 1905, nos três periódicos e gêneros
disponíveis.

**Inclusão:** Registro com identificador, ano, periódico, gênero e tema.

**Exclusão:** Registro fora do período ou sem os campos necessários. Exclusões
por ilegibilidade deveriam ser quantificadas e discutidas em uma pesquisa real.

**O que mudou em relação ao Notebook 03:** os critérios foram ligados diretamente
aos campos necessários para a comparação por gênero. O alcance também foi
restringido à coleção fictícia, evitando apresentar o conjunto como amostra da
imprensa histórica.

## 4. Operacionalização

| Conceito | Dimensão | Indicador | Variável | Categorias ou valores | Fonte | Regra | Limitação |
|---|---|---|---|---|---|---|---|
| Presença do progresso | Centralidade categorial | Tema dominante atribuído | `tema` | educação, trabalho, progresso | Documento e anotação | Uma categoria principal por documento | Apaga temas secundários e ambiguidade |
| Presença do progresso | Presença lexical | Ocorrências contextualizadas de “progresso” e variantes | `ocorrencias_progresso` | inteiro igual ou maior que zero | Texto integral | Localizar variantes e revisar concordâncias | A palavra pode assumir sentidos diferentes ou o conceito aparecer sem o termo |

Para a exploração inicial, a primeira opção é compatível com os dados
disponíveis. Para uma investigação substantiva, a segunda precisaria ser
combinada com leitura contextual e ampliação das categorias.

**Alternativa inicialmente escolhida:** tema dominante, porque é o único indicador
presente para todos os registros da coleção didática.

**O que mudou em relação ao Notebook 02:** a presença lexical foi mantida como
alternativa futura, mas não como medida disponível no corpus atual. A decisão
separa o que pode ser executado agora do que exigiria textos integrais, lista de
variantes e revisão contextual.

**Raciocínio:** a alternativa escolhida não é considerada teoricamente superior;
ela é apenas compatível com os dados existentes. Sua limitação orienta a cadeia
de evidência e impede interpretar “tema dominante” como importância histórica.

## 5. Esquema inicial

| Campo | Papel | Tipo | Origem | Exemplo |
|---|---|---|---|---|
| `id` | identificador | texto | catálogo | D001 |
| `ano` | metadado temporal | inteiro | catálogo | 1890 |
| `periodico` | metadado documental | categoria | catálogo | Jornal Aurora |
| `genero` | variável documental categórica | categoria | anotação/catalogação | editorial |
| `tema` | variável analítica categórica | categoria | anotação | progresso |
| `texto` | conteúdo documental | texto | transcrição | texto integral |
| `arquivo_origem` | proveniência | texto | repositório | caixa_03.pdf |

## 6. Cadeia de evidência

**Operação:** Comparar a proporção de documentos classificados como “progresso”
entre gêneros.

**Resultado possível:** Proporção maior entre editoriais.

**Evidência possível:** Na coleção e segundo a regra de anotação, “progresso”
aparece mais frequentemente como tema dominante nos editoriais.

**O que não demonstra:** Não prova que editoriais foram historicamente mais
importantes, que a sociedade valorizava mais o progresso nem que o gênero causou
a presença do tema.

**Interpretações alternativas:** A diferença pode resultar da regra de
classificação, da composição do corpus, da extensão dos documentos ou da seleção
dos periódicos.

**Retorno qualitativo:** Reler todos os editoriais classificados como
“progresso”, casos limítrofes e documentos de outros gêneros que utilizam o
vocabulário sem receber a categoria.

**Contexto necessário:** Convenções dos gêneros, projetos editoriais,
circulação, vocabulário do período e historiografia dos debates.

## 7. Limites, vieses e ética

| Dimensão | Risco | Estratégia |
|---|---|---|
| Seleção | Coleção pequena e descontínua | Limitar conclusões e documentar cobertura |
| Representação | Uma categoria dominante apaga polissemia | Preservar notas, casos ambíguos e categorias múltiplas |
| Automação | Busca lexical pode confundir sentidos | Revisar concordâncias e amostra de erros |
| Ética | Categorias históricas podem reproduzir estigmas | Contextualizar termos e evitar naturalização |
| Interpretação | Frequência pode ser confundida com importância | Retornar aos documentos e formular alternativas |

## 8. Síntese-modelo

**Pergunta final:** Como a atribuição do tema “progresso” varia entre editoriais,
notícias e cartas dos três periódicos da coleção didática, entre 1890 e 1905?

**Resumo:** Pretendo investigar diferenças na presença categorial do tema
“progresso” entre gêneros documentais. Cada documento será uma unidade de
análise. O corpus inicial inclui doze registros fictícios e será usado somente
para demonstrar o desenho metodológico. O tema será observado inicialmente por
uma categoria dominante e, em uma etapa posterior, por ocorrências lexicais
revisadas em contexto. A comparação poderá oferecer evidência sobre a
distribuição interna da coleção, mas não sustentará generalizações históricas.
Os principais limites são o caráter fictício dos dados, a pequena cobertura e a
redução produzida pela categoria exclusiva.

**Próxima decisão:** Construir um guia de anotação que defina “progresso” e
registre casos ambíguos.

## 9. Referências utilizadas — exemplo preenchido

1. **DRUCKER, Johanna (2011).** Fundamenta a afirmação de que a categoria `tema`
   é uma construção interpretativa, não uma propriedade transparente do
   documento.
2. **LAVIN, Matthew (2021).** Sustenta a documentação dos dados como situados e a
   necessidade de registrar decisões de seleção e transformação.
3. **D'IGNAZIO, Catherine; KLEIN, Lauren F. (2020).** Orienta a análise de poder,
   ausências e trabalho envolvido na produção da base.

**Por que esta lista é adequada:** cada obra está ligada a uma decisão concreta.
Listar uma referência sem explicar sua função não demonstraria fundamentação.

## 10. Autoavaliação — exemplo de resolução

| Critério | Pontuação | O que ainda precisa ser revisto |
|---|---:|---|
| Relevância humanística | 2 | relacionar o estudo a uma discussão historiográfica mais específica |
| Fundamentação bibliográfica | 2 | incluir bibliografia histórica sobre imprensa, gêneros e progresso |
| Delimitação da pergunta | 3 | manter explícito que se trata da atribuição temática na coleção |
| Unidade de análise | 3 | nenhuma revisão imediata; documento está alinhado às afirmações |
| Viabilidade dos dados | 2 | verificar disponibilidade de textos integrais para a alternativa lexical |
| Operacionalização | 2 | construir e testar o guia de anotação de “progresso” |
| Cadeia de evidência | 3 | preservar releitura de casos divergentes na execução |
| Limites e ética | 2 | detalhar tratamento de vocabulário histórico potencialmente estigmatizante |

**Total orientativo:** 19 de 24.

**Síntese da autoavaliação:** a proposta é coerente para uma exploração didática,
mas ainda não possui fundamentação histórica suficiente nem regra de anotação
testada. A prioridade é construir o guia de categorias e verificar se os textos
integrais permitem uma segunda operacionalização.

**Como pontuar:** a nota 3 não significa perfeição; significa que o elemento está
definido, coerente e criticamente justificado no estágio atual. Não atribuir 3 a
um item apenas porque ele foi mencionado.

## 11. Revisão entre pares — exemplo de resolução

### Parecer recebido

> Consigo identificar que serão observados documentos e que a comparação será por
> gênero. Os dados permitem contar a categoria `tema`, mas a expressão “presença
> do progresso” ainda pode ser entendida como ocorrência do conceito no texto.
> Sugiro que a pergunta diga “atribuição do tema” e que o projeto esclareça quem
> atribuiu a categoria. O alcance está limitado à coleção, mas a motivação ainda
> precisa de bibliografia histórica além das leituras metodológicas.

### Mudanças realizadas e justificativa

1. Substituí “presença do progresso” por “atribuição do tema ‘progresso’” na
   pergunta, para alinhar a linguagem ao indicador disponível.
2. Registrei `tema` como categoria produzida por anotação e defini a construção de
   um guia de anotação como próxima decisão.
3. Mantive a conclusão limitada à coleção didática.
4. Acrescentei como pendência a busca de bibliografia histórica sobre imprensa e
   progresso, pois as referências metodológicas não bastam para interpretar o
   fenômeno.

### Pergunta após a revisão

> Como a atribuição do tema “progresso” varia entre editoriais, notícias e cartas
> dos três periódicos da coleção didática, entre 1890 e 1905?

**Por que o parecer é adequado:** responde aos itens da atividade, identifica uma
decisão prioritária e não reescreve todo o projeto pelo autor. O registro das
mudanças mostra quais sugestões foram aceitas e por quê.

## 12. Rubrica do docente

Pontuar cada critério de 0 a 3:

| Critério | 0 | 1 | 2 | 3 |
|---|---|---|---|---|
| Relevância humanística | Ausente | Tema citado sem justificativa | Relevância explicada | Relevância situada em problema claro |
| Fundamentação bibliográfica | Ausente | Obras listadas sem função | Conceitos ligados a leituras | Autores comparados e mobilizados no desenho |
| Delimitação | Ausente | Muito ampla | Recorte identificável | Recorte claro, viável e justificado |
| Unidade de análise | Ausente | Ambígua | Identificada | Identificada e coerente com as afirmações |
| Dados e corpus | Ausentes | Fontes genéricas | Fontes e critérios indicados | Cobertura, seleção e proveniência discutidas |
| Operacionalização | Ausente | Confunde conceito e indicador | Relação plausível | Alternativas comparadas e regras explícitas |
| Cadeia de evidência | Ausente | Salto entre resultado e conclusão | Alcance básico correto | Alternativas e retorno qualitativo explícitos |
| Limites e ética | Ausentes | Menção genérica | Limitações pertinentes | Riscos ligados a estratégias concretas |

### Interpretação da pontuação

- **0–8:** proposta ainda inicial; requer nova delimitação acompanhada;
- **9–16:** elementos presentes, mas há relações que precisam ser justificadas;
- **17–20:** proposta coerente e viável, com revisões localizadas;
- **21–24:** proposta bem articulada e criticamente justificada.

A pontuação não deve substituir o comentário qualitativo.
