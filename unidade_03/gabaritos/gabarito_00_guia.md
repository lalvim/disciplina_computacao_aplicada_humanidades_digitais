# Gabarito orientativo — Diagnóstico inicial

O diagnóstico não pede que o estudante execute todas as transformações. Ele deve
antecipar quais operações serão necessárias e quais delas podem alterar sentido,
unidade de análise ou quantidade de registros.

## Exemplo de resposta preenchida

> Meu projeto recebe um catálogo em CSV, textos em TXT e páginas digitalizadas em
> PNG. Preservarei esses arquivos em `dados/brutos` e produzirei novas versões em
> `intermediarios` e `derivados`. Preciso importar o catálogo, reconhecer texto nas
> imagens, padronizar datas e gêneros, reorganizar indicadores e ligar os documentos
> aos municípios e temas. As decisões de maior risco são a definição de duplicata,
> a transformação de datas parciais, o OCR e as junções, pois podem apagar diferenças,
> introduzir texto incorreto ou multiplicar linhas. Para cada uma, manterei o valor
> original, registrarei a regra e executarei um teste verificável.

Uma forma mais estruturada de apresentar o mesmo diagnóstico seria:

| Transformação prevista | O que pode mudar | Risco principal | Controle proposto |
|---|---|---|---|
| importar CSV e XLSX | tipos atribuídos às colunas | código municipal perder zeros ou planilha errada ser lida | declarar separador, encoding, planilha e `dtype`; conferir dimensões |
| extrair texto ou aplicar OCR | conteúdo textual disponível para busca | caracteres e ordem divergirem da página | manter imagem/PDF, registrar ferramenta e medir uma amostra |
| normalizar títulos, municípios e gêneros | forma de comparação entre valores | variantes relevantes serem fundidas | preservar original e criar coluna derivada |
| normalizar datas | precisão temporal | inverter dia e mês ou inventar partes ausentes | reconhecer formatos explicitamente e registrar a precisão |
| transformar largo em longo | unidade representada por cada linha | interpretar 12 relações como 12 documentos | declarar a unidade antes e depois |
| detectar duplicatas | quantidade de registros | apagar edições ou testemunhos distintos | marcar candidatos e submeter a revisão humana |
| juntar municípios e documentos | número de linhas e cobertura | chave duplicada multiplicar documentos | declarar `many_to_one`, usar `validate` e conferir contagens |

## Por que este exemplo é adequado?

Ele nomeia entradas, saídas, operações e riscos; diferencia transformação técnica de
decisão interpretativa; e antecipa controles concretos. Uma resposta como “vou limpar
os dados com Python” seria insuficiente porque não identifica o que será transformado,
que perda pode ocorrer nem como a decisão será auditada.
