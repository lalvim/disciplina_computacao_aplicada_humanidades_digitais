# Gabarito orientativo — Primeira base processável

Cada item recebe 0, 1 ou 2 pontos conforme a rubrica do notebook. Aprovação
orientativa: ao menos 11/14, sem zero em preservação/proveniência, junções ou
reprodutibilidade. O exemplo a seguir preenche todas as partes da oficina com o
estudo de caso da unidade.

## Exemplo de resolução completa

### 1. Inventário e estrutura

**Pergunta e unidade de análise:** como preparar, de maneira auditável, os registros
documentais do conjunto didático para uma futura análise das relações entre educação
e trabalho no período de 1890 a 1901? A unidade principal é o registro documental,
identificado por `id_documento`. As tabelas documento–tema e indicadores usam,
respectivamente, as unidades relação temática e documento–tema–período.

**Arquivos, formatos, versões e proveniência:** o projeto recebe catálogo em CSV e
XLSX, metadados em JSON e XML, textos em TXT, um PDF textual e duas imagens PNG
sintéticas para OCR. A referência municipal é um extrato didático do IBGE cuja URL,
data de acesso e limitação estão em `proveniencia_base_publica.json`. Os arquivos
didáticos foram preparados em 31 de julho de 2026.

**Estrutura de pastas e política de imutabilidade:** `dados/brutos` contém as entradas
e não será editada durante a análise; `dados/intermediarios` recebe o catálogo
normalizado; `dados/derivados` recebe documentos, temas e indicadores prontos para a
etapa exploratória. Os notebooks registram a ordem das operações e os gabaritos não
fazem parte da cadeia de dados.

**Ambiente e dependências:** Python 3, pandas 2.x, openpyxl 3.x, pypdf 5.x e Pillow
11.x. Tesseract é opcional e, quando usado, sua versão, idioma `eng` e segmentação
`--psm 7` devem ser registrados. Sem Tesseract, usam-se saídas pré-computadas
explicitamente identificadas como tais.

### 2. Importação e extração

| Fonte | Leitor/parâmetros | Estrutura esperada | Teste | Saída |
|---|---|---|---|---|
| `catalogo_messy.csv` | `pd.read_csv`, `sep=";"`, código como `string` | 8 linhas × 7 colunas | conferir dimensões e nomes das colunas | DataFrame do catálogo |
| `catalogo_messy.xlsx` | `pd.read_excel`, planilha `documentos` | mesmos registros do CSV | comparar dimensões com o CSV | DataFrame de controle |
| `metadados.json` | `json.loads`, UTF-8 | 3 objetos; `temas` é lista | conferir IDs e tipos | metadados hierárquicos |
| `metadados.xml` | `ElementTree.parse` | raiz `colecao`, 2 documentos | contar nós `documento` | elementos XML |
| `extrato_codigos_municipios_ibge.csv` | `pd.read_csv`, código como `string` | 4 municípios, códigos únicos | unicidade e proveniência presente | referência municipal |
| `documento_textual.pdf` | `PdfReader.extract_text()` | uma página com camada textual | texto não vazio + inspeção da página | texto extraído |

**PDFs com texto, PDFs de imagem e TXT:** o PDF fornecido tem camada textual e retorna
“Documento D001 com camada textual”; portanto, não requer OCR. Um PDF composto apenas
de imagens seguiria a rota de OCR por página. D001.txt e D002.txt são lidos como UTF-8
e permanecem vinculados a seus IDs pelo arquivo `metadados.json`.

**Plano de OCR, amostra e métrica:** usar as duas PNG sintéticas como amostra
controlada, manter imagem e transcrição separadas e comparar cada saída à referência.
Na rota offline, a imagem limpa apresenta CER 0,000 e WER 0,000; a degradada apresenta
CER 0,094 e WER 0,500. Esses números demonstram o procedimento, mas não definem uma
tolerância universal. Citação exige conferência da página; busca exploratória requer
amostra maior e documentação da taxa de erro.

### 3. Modelo tabular e transformação

**Tabelas e unidade das linhas:** `documentos_processaveis.csv` possui uma linha por
registro documental; `documentos_temas.csv`, uma linha por atribuição temática;
`indicadores_longos.csv`, uma linha por documento–tema–período. Textos são atributos
0..1 do documento nesta versão, e municípios formam uma tabela de referência.

**Decisão largo/longo:** os indicadores são convertidos de 3 linhas e 5 colunas para
12 linhas e 4 colunas. O formato longo é adotado porque tema e período são dimensões
analíticas, não partes do nome de uma variável. A fonte larga permanece preservada.

| Campo | Original preservado | Regra | Justificativa | Teste | Perda possível |
|---|---|---|---|---|---|
| título | sim, em `titulo` | criar `titulo_chave` sem espaços excedentes, caixa ou acentos | comparar variantes | D001 e D004 resultam em `jornal aurora` | diacríticos e diferenças gráficas não servem para apresentação |
| município | sim, em `municipio` | criar chave e depois incorporar nome IBGE | permitir correspondência controlada | oito registros encontram município | grafias históricas podem não equivaler ao município atual |
| gênero | sim, em `genero_original` | mapa explícito para quatro categorias | consolidar variações formais | zero valores sem mapa | categorias locais podem ser comprimidas |
| data | sim, em `data_original` | reconhecer ISO e brasileiro; separar ano parcial e desconhecido | evitar ambiguidade e falsa precisão | 6 completas, 1 anual, 1 desconhecida, 0 inválidas | data completa não pode ser criada para D003 ou D005 |
| palavras | ausência preservada | conversão numérica; razão `não contado` | não confundir ausência com zero | uma ausência e uma razão | nenhuma, desde que a razão seja mantida |

### 4. Ausências e duplicatas

**Representações de ausência e razões:** D003 tem ano 1892, mas
`data_normalizada` ausente porque não há dia e mês; `precisao_data = ano` e a razão é
“dia e mês não informados”. D005 tem ano e data ausentes,
`precisao_data = desconhecida` e razão “data não informada”. A contagem de palavras
de D003 fica ausente com razão “não contado”.

**Chave de duplicata exata:** `id_documento` deve ser único. Nenhum ID é repetido
literalmente.

**Critério de possível duplicata:** combinação de `titulo_chave`, data normalizada,
`municipio_chave` e palavras. Ela marca D006 e D006-copia, mas não demonstra que são
o mesmo documento.

**Decisão:** manter ambos, relacioná-los como candidatos e inspecionar as fontes e os
metadados antes de fundir ou excluir. Se forem o mesmo item, preservar os dois IDs no
log e registrar qual registro foi adotado como canônico.

### 5. Junções e integração

| Tabelas | Chave | Cardinalidade | Validação | Não correspondências |
|---|---|---|---|---|
| documentos + municípios | `codigo_municipio` | N:1 | `validate="many_to_one"`, `indicator=True`, 8 linhas antes/depois | preservar e investigar `left_only`; no exemplo há zero |
| documentos + textos | `id_documento` | 1:0..1 | `validate="one_to_one"`, IDs únicos | manter texto ausente; só D001 e D002 possuem TXT |
| documentos ↔ temas | `id_documento` | 1:N | IDs dos temas devem existir em documentos | rejeitar relação órfã e revisar a origem |
| documentos ↔ indicadores | `id_documento` | 1:N | chave documento–tema–período e 12 relações esperadas | registrar indicador órfão como falha de integridade |

**Vínculo até a fonte:** para D001, partir de uma relação em
`documentos_temas.csv`, localizar o documento pela chave, consultar `metadados.json`
para obter `D001.txt` e retornar ao arquivo bruto. O notebook registra a atividade que
produziu cada tabela.

**Contagens:** a junção municipal começa e termina com 8 linhas e 8 IDs distintos. A
junção textual também mantém 8 documentos. Temas e indicadores permanecem separados
para que suas relações 1:N não multipliquem a tabela principal.

### 6. Registro, testes e reconstrução

**Log de transformações:** registrar para cada campo o problema, a regra, a
justificativa, os casos afetados, o teste, a reversibilidade e o responsável. Exemplo:
“data_documento; quatro padrões; parser por expressão regular; impedir inversão;
oito casos; 6/1/1/0 por precisão; reversível por data_original; pesquisador”.

**Testes:** esquema e dimensões das entradas; unicidade de `id_documento` e dos
códigos municipais; domínio de `genero_padronizado`; distribuição de
`precisao_data`; contagens antes/depois; cobertura das junções; integridade das
chaves estrangeiras; existência dos três CSV derivados.

**Reconstrução:** executar os Notebooks 00, 01, 02 e 03 em ordem a partir de uma cópia
do repositório. O Notebook 02 recria `catalogo_normalizado.csv`; o 03 recria os três
derivados. Nenhuma correção manual deve ser necessária entre as células.

**Erros conhecidos e pendências:** OCR avaliado apenas em duas linhas sintéticas;
mapa de gêneros reduzido ao domínio didático; possível duplicata sem inspeção do
documento; referência municipal contemporânea pode não representar divisões
históricas; apenas dois textos estão disponíveis.

### 7. Autoavaliação preenchida

| Critério | Nota | Evidência no exemplo |
|---|---:|---|
| preservação e proveniência | 2 | brutos separados; extrato IBGE com URL e data |
| importação | 2 | leitores, parâmetros, estruturas e testes declarados |
| limpeza | 2 | original, derivado, regra e teste para cada campo crítico |
| ausências/duplicatas | 2 | razões explícitas e candidatos mantidos para revisão |
| junções | 2 | chaves, cardinalidades, cobertura e contagens auditadas |
| integração | 2 | documentos, temas e indicadores ligados sem listas multivaloradas |
| reprodutibilidade | 2 | ordem de execução e saídas reconstruíveis desde os brutos |
| **Total** | **14/14** | atende ao exemplo integral; projetos reais podem ter pendências justificadas |

### 8. Exemplo de revisão por pares

**Parecer recebido:** “A base é reconstruível e a junção municipal está controlada,
mas `municipio_chave` pode aproximar grafias sem resolver mudanças territoriais. O
critério de duplicata também não foi confirmado na fonte.”

**Mudanças realizadas:** acrescentei ao relatório a limitação histórica da referência
municipal e mantive D006 e D006-copia como candidatos, sem exclusão. Registrei que a
decisão depende de inspeção documental futura.

**O que a Unidade 4 poderá explorar:** contagens descritivas por gênero, município,
ano disponível, tema e período, sempre informando denominadores e cobertura.

**O que ainda não deve concluir:** representatividade histórica do conjunto,
frequência lexical do corpus completo, evolução mensal, equivalência definitiva dos
municípios históricos ou identidade entre D006 e D006-copia.

## Por que este exemplo é adequado?

Ele entrega um pacote coerente, mas não finge eliminar as incertezas. Entradas,
operações, testes, produtos e limites permanecem conectados. A nota máxima ilustra o
nível de documentação esperado; não significa que uma base de pesquisa precise estar
sem casos pendentes, e sim que as pendências devem estar identificadas e governadas.
