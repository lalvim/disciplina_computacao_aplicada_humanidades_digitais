# Gabarito orientativo — Junções e integração

A atividade pede um plano de integração: quais tabelas existem, o que cada linha
representa, como elas se relacionam e que testes impedem a criação silenciosa de
casos. O exemplo abaixo resolve a atividade com os dados didáticos da unidade.

## Exemplo de resolução — plano de integração

### 1. Tabelas, unidades e chaves

| Tabela | Unidade de cada linha | Chave | Quantidade esperada |
|---|---|---|---:|
| catálogo normalizado | um registro documental | `id_documento` | 8 |
| municípios do IBGE | um município | `codigo_municipio` | 4 |
| textos disponíveis | um texto associado a um documento | `id_documento` | 2 |
| documento–tema | uma atribuição de tema a um documento | `id_documento` + `tema` | 4 |
| indicadores longos | uma combinação documento–tema–período | `id_documento` + `tema` + `periodo` | 12 |

O catálogo é a tabela central nesta versão. `id_documento` é chave primária do
catálogo e chave estrangeira nas tabelas de textos, temas e indicadores. O código
municipal é chave estrangeira no catálogo e chave primária na referência do IBGE.

### 2. Junções e validações

| Tabelas | Chave | Cardinalidade esperada | Como validar | Tratamento de não correspondências |
|---|---|---|---|---|
| catálogo + municípios | `codigo_municipio` | N:1 (`many_to_one`) | código único na referência; `merge(validate="many_to_one", indicator=True)`; 8 linhas antes e depois | preservar `left_only`, listar o código e verificar versão, erro de digitação ou cobertura da referência |
| catálogo + textos | `id_documento` | 1:0..1; operacionalmente `one_to_one` para os textos disponíveis | IDs únicos dos dois lados; junção à esquerda; 8 documentos após a operação | manter texto ausente como ausência, pois nem todo documento possui TXT nesta versão |
| catálogo ↔ documento–tema | `id_documento` | 1:N | IDs da relação devem ser subconjunto dos IDs do catálogo; chave composta sem repetição | manter relação separada e revisar tema órfão em vez de duplicar metadados |
| catálogo ↔ indicadores | `id_documento` | 1:N | unidade documento–tema–período e chave composta declaradas; IDs devem existir no catálogo | indicadores sem documento são registrados como erro de integridade |

### 3. Resultado esperado

A junção municipal mantém oito linhas, oito IDs distintos e zero registros
`left_only`. A integração textual também mantém oito documentos: D001 e D002 recebem
texto, enquanto os demais permanecem com texto ausente. A multiplicidade temática
não é incorporada como uma lista na tabela de documentos; ela permanece na tabela
documento–tema com quatro relações. Os indicadores permanecem em tabela longa com
12 relações.

### 4. Exemplo de rastreamento até a fonte

Para rastrear o tema `educação` associado a D001:

1. localizar D001 em `documentos_temas.csv`;
2. usar `id_documento` para localizar o registro em
   `documentos_processaveis.csv`;
3. consultar `arquivo_texto = D001.txt` em `metadados.json`;
4. retornar a `dados/brutos/D001.txt` e, quando pertinente, ao documento-fonte;
5. consultar o notebook e o log para saber como a relação temática foi criada.

O arquivo derivado não substitui a fonte: a chave, os metadados e o registro da
transformação formam o caminho de volta.

### 5. Resposta-modelo em forma de parecer

> Integrarei primeiro o catálogo à referência municipal por
> `codigo_municipio`, declarando cardinalidade N:1 e preservando todos os registros
> da esquerda. Conferirei número de linhas, IDs únicos e indicador de cobertura.
> Depois ligarei os textos por `id_documento` com cardinalidade 1:0..1. Temas e
> indicadores permanecerão em tabelas relacionais longas, pois um documento pode
> participar de várias relações. Qualquer chave sem correspondência será preservada
> e investigada; não será excluída automaticamente. Cada saída manterá identificadores
> que permitam retornar aos arquivos brutos e ao notebook que a produziu.

## Por que este exemplo é adequado?

Ele declara as unidades antes de juntar, diferencia cardinalidade de cobertura,
define testes mensuráveis e mostra um caminho concreto de proveniência. Dizer apenas
“farei um `merge` pelo ID” não seria suficiente para avaliar se a junção cria linhas,
perde registros ou associa objetos indevidamente.
