# Gabarito orientativo — Representação e operacionalização

## 1. Resultados dos experimentos

### Unidade de análise

No primeiro experimento:

- há três unidades;
- cada linha representa um documento;
- `id` identifica a unidade;
- `ano`, `genero` e `tema` registram características atribuídas aos documentos.

Não seria adequado afirmar que existem três jornais, três autores ou três temas
distintos apenas porque existem três linhas.

### Categorias exclusivas e múltiplas

Na representação exclusiva, a contagem é:

| Tema | Documentos |
|---|---:|
| educação | 2 |
| trabalho | 1 |

A representação permite uma contagem direta, mas não registra que um documento
pode tratar simultaneamente de educação e progresso ou de educação e trabalho.
A representação com múltiplos temas preserva coexistências, mas exige decidir:

- se cada tema terá o mesmo peso;
- como serão calculadas frequências;
- como tratar divergências entre anotadores;
- qual regra define a presença de um tema.

## 2. Mapa de operacionalização — resposta-modelo

**Conceito:** centralidade do tema educação.

| Dimensão | Indicador | Unidade de análise | Variável ou categoria | Fonte | Regra | Limitação |
|---|---|---|---|---|---|---|
| Presença temática | Tema dominante atribuído | Documento | `tema_dominante` | Texto integral | Após leitura, atribuir uma categoria principal segundo guia | Força exclusividade e perde temas secundários |
| Extensão da discussão | Proporção de palavras em trechos anotados como educação | Documento | `proporcao_educacao` | Texto integral e anotação de trechos | Dividir palavras dos trechos pertinentes pelo total do documento | Extensão não equivale a importância discursiva |

### Comparação

A primeira alternativa é simples, transparente e adequada a uma exploração
inicial, mas reduz a ambiguidade. A segunda representa melhor a extensão do
debate, porém depende de segmentação e anotação mais trabalhosas. Nenhuma mede
diretamente “importância histórica”. A escolha depende do sentido de
centralidade adotado na pergunta.

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

