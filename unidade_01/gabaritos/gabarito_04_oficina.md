# Gabarito orientativo — Oficina do projeto

Este arquivo apresenta uma resposta-modelo completa. Ela demonstra coerência
entre as partes, mas não deve ser usada como molde temático obrigatório.

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

**Tipo predominante:** Comparativa, pois confronta gêneros documentais. A
contagem inicial é descritiva.

**Tarefa computacional:** Filtrar documentos, agrupar por gênero e calcular a
frequência absoluta e relativa da categoria “progresso”.

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

## 4. Operacionalização

| Conceito | Dimensão | Indicador | Variável | Fonte | Regra | Limitação |
|---|---|---|---|---|---|---|
| Presença do progresso | Centralidade categorial | Tema dominante atribuído | `tema` | Documento e anotação | Uma categoria principal por documento | Apaga temas secundários e ambiguidade |
| Presença do progresso | Presença lexical | Ocorrências contextualizadas de “progresso” e variantes | `ocorrencias_progresso` | Texto integral | Localizar variantes e revisar concordâncias | A palavra pode assumir sentidos diferentes ou o conceito aparecer sem o termo |

Para a exploração inicial, a primeira opção é compatível com os dados
disponíveis. Para uma investigação substantiva, a segunda precisaria ser
combinada com leitura contextual e ampliação das categorias.

## 5. Esquema inicial

| Campo | Papel | Tipo | Origem | Exemplo |
|---|---|---|---|---|
| `id` | identificador | texto | catálogo | D001 |
| `ano` | metadado temporal | inteiro | catálogo | 1890 |
| `periodico` | metadado documental | categoria | catálogo | Jornal Aurora |
| `genero` | categoria documental | categoria | anotação/catalogação | editorial |
| `tema` | categoria analítica | categoria | anotação | progresso |
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

## 9. Rubrica do docente

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
