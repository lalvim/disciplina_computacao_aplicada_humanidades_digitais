# Gabarito orientativo — Oficina do relatório exploratório

Este exemplo mostra o nível de completude esperado. Os dados são inteiramente
fictícios; portanto, os resultados demonstram procedimentos e não sustentam
afirmações históricas reais.

## Exemplo de resolução completa

### 1. Escopo e qualidade da base

**Pergunta exploratória:** como se distribuem a extensão documental e alguns padrões
lexicais na base didática, e de que maneira o caso D023 afeta os agregados anuais?

**Corpus e período:** 24 registros fictícios, dois por ano, entre 1890 e 1901.

**Unidade de análise:** cada linha representa um registro documental identificado por
`id_documento`. Uma linha não representa uma pessoa, uma palavra ou todos os
documentos de determinado ano.

**Variáveis:** `genero`, `local` e `tema` são nominais; `ano` é temporal; `palavras`,
`pessoas` e `paginas` são quantitativas discretas; `id_documento` é identificador; e
`texto` contém o material textual fictício.

**Cobertura e ausências:** não há valores ausentes na tabela. Cada tema aparece seis
vezes, cada gênero oito vezes e cada ano duas vezes. Essa regularidade resulta da
construção didática da base e não deve ser interpretada como equilíbrio histórico.

**Erro conhecido e extremo:** a proveniência informa que D023 foi criado como extremo
deliberado. Sua presença é mantida para estudar o efeito de um caso muito extenso.

**Adequação:** a base é adequada para exercitar cálculo, visualização, retorno aos
casos e formulação de hipóteses. Não é adequada para descrever imprensa, educação ou
trabalho em uma sociedade real.

### 2. Perfil quantitativo

#### Frequências e proporções

Cada um dos quatro temas — educação, trabalho, progresso e saúde — possui seis dos 24
documentos:

| Tema | Frequência | Proporção |
|---|---:|---:|
| educação | 6 | 0,25 |
| trabalho | 6 | 0,25 |
| progresso | 6 | 0,25 |
| saúde | 6 | 0,25 |

O denominador é 24 documentos. A tabela descreve o desenho desta base; ela não mede
a intensidade com que os temas aparecem dentro dos textos.

#### Centro e dispersão da extensão

| Medida de `palavras` | Valor |
|---|---:|
| média | 701,58 |
| mediana | 621,50 |
| Q1 | 459,00 |
| Q3 | 848,75 |
| IQR | 389,75 |
| variância amostral | 138.786,95 |
| desvio-padrão amostral | 372,54 |

A média é maior que a mediana, em parte por causa do valor alto de D023. Variância e
desvio-padrão usam `ddof=1`; os quartis usam interpolação linear.

#### Inspeção de extremos

O limite inferior é −125,625 e o superior, 1.433,375 palavras. D023, com 2.100
palavras, é o único registro fora dos limites. Esse resultado o sinaliza para leitura,
mas não autoriza removê-lo. O próximo passo seria conferir a fonte e a regra de
contagem; aqui a proveniência confirma que se trata de um extremo didático deliberado.

#### Contingência entre gênero e tema

Cada gênero possui dois documentos de cada tema:

| Gênero | educação | progresso | saúde | trabalho |
|---|---:|---:|---:|---:|
| carta | 2 | 2 | 2 | 2 |
| editorial | 2 | 2 | 2 | 2 |
| notícia | 2 | 2 | 2 | 2 |

Como cada linha soma oito, todas as proporções por gênero são 0,25. Não há diferença
descritiva nesta base. A ausência de diferença foi programada na geração dos dados e
não constitui evidência de independência em uma população histórica.

### 3. Perfil textual

**Regras:** conversão para minúsculas e segmentação pela expressão regular
`[a-záàâãéêíóôõúç]+`. A lista de stopwords contém artigos, preposições e outras formas
funcionais declaradas no Notebook 02. Os textos originais permanecem preservados.

**Frequências:** foram obtidos 936 tokens antes das stopwords e 600 tokens de conteúdo.
Termos como `escola`, `noturna`, `trabalho` e `oficinas` aparecem 24 vezes. Sua
frequência relativa é aproximadamente 0,0256 entre todos os tokens e 0,04 entre os
tokens de conteúdo. Os dois valores são corretos, mas respondem a denominadores
diferentes.

**Concordância:** a busca por `trabalho`, com janela de quatro tokens, retorna o ID e
o contexto de cada ocorrência. Um exemplo é “ensino social o trabalho nas oficinas
reúne jornada”. A concordância mostra que o termo pertence a uma frase repetida na
construção dos textos; a frequência isolada não revela essa repetição.

**Colocações:** com frequência mínima 3, `escola noturna`, `noturna amplia`,
`trabalho nas` e `oficinas reúne` aparecem 24 vezes e alcançam PMI aproximada de
5,248. A pontuação alta decorre das combinações fixas usadas nos textos fictícios.
Não se pode convertê-la em importância histórica ou causalidade.

**Diversidade:** o tamanho comum adotado é 19 tokens. D001 tem TTR bruta 0,85 e
TTR-19 de aproximadamente 0,842. D003 tem 57 tokens, TTR bruta aproximada de 0,263 e
TTR-19 de 0,789. A diferença bruta é muito maior porque D003 repete a mesma estrutura;
a padronização reduz o efeito do tamanho, mas permanece sensível ao trecho inicial.

### 4. Quatro visualizações selecionadas

| Figura | Tabela equivalente | Descrição e interpretação | Limite |
|---|---|---|---|
| barras de documentos por tema | quatro temas com frequência 6 | barras iguais mostram composição perfeitamente equilibrada | equilíbrio resulta da fabricação didática da base |
| histograma e boxplot de palavras | faixas de extensão e cinco números | maior parte dos documentos fica abaixo de 1.100 palavras; D023 aparece isolado | bins alteram o histograma e o boxplot apenas sinaliza o caso |
| linha da média de palavras por ano | média e dois documentos de cada ano | 1900 alcança média 1.445, acima dos demais anos | o salto é fortemente influenciado por D023 e não demonstra tendência histórica |
| barras dos termos de conteúdo | frequência absoluta e dois valores relativos | vários termos empatam com 24 ocorrências | repetição de frases produz o padrão lexical |

Exemplo de descrição alternativa da série temporal: “Gráfico de linha com médias
anuais da extensão entre 1890 e 1901; os valores ficam entre 457 e 790 na maioria dos
anos, sobem para 1.445 em 1900 e retornam a 739 em 1901.”

### 5. Retorno a três casos

| Caso | Razão da escolha | Evidência | Efeito sobre a leitura |
|---|---|---|---|
| D023 | único extremo de extensão | 2.100 palavras, tema progresso, ano 1900 | explica grande parte da elevação da média de 1900 |
| D001 | documento curto usado para comparar diversidade | 20 tokens, TTR 0,85 e TTR-19 0,842 | mostra como a TTR bruta pode parecer alta em texto curto |
| D003 | documento mais longo e repetitivo | 57 tokens, TTR 0,263 e TTR-19 0,789 | mostra que tamanho e repetição afetam a diversidade bruta |

Os três casos não provam o comportamento do corpus. Eles explicam por que alguns
agregados assumiram os valores observados e expõem a fabricação dos dados.

### 6. Hipóteses provisórias

| Hipótese | Evidência | Alternativa | Dados adicionais | Método futuro |
|---|---|---|---|---|
| a elevação de 1900 pode estar associada a um documento excepcionalmente extenso | média anual 1.445 e D023 com 2.100 palavras | erro de contagem ou mudança na composição documental | fonte, regra de contagem e corpus ampliado | análise de sensibilidade com e sem D023, sem apagar o registro |
| parte da diferença de TTR pode estar associada ao tamanho e à repetição | D001 e D003 convergem parcialmente após padronização | efeito da escolha do segmento inicial | segmentos adicionais e textos naturais | comparar amostras de mesmo tamanho e posições diferentes |
| colocações altas podem resultar de fórmulas textuais repetidas | bigramas fixos com frequência 24 e PMI 5,248 | convenção discursiva real, caso a base não fosse fictícia | textos diversos e metadados de gênero | concordâncias, comparação entre gêneros e validação em novo corpus |

Todas permanecem provisórias. Nenhuma foi submetida a teste inferencial.

### 7. Limitações e reprodução

As principais limitações são: dados fictícios e balanceados; apenas quatro frases
combinadas e repetidas; D023 deliberadamente construído; dois documentos por ano;
stopwords reduzidas; TTR baseada no trecho inicial; e ausência de informação sobre
processos históricos reais de produção, preservação e seleção.

Para reproduzir, clonar o repositório, abrir `unidade_04`, executar os Notebooks 01,
02 e 03 em ordem e manter os parâmetros publicados: `ddof=1`, interpolação linear,
regra 1,5 IQR, tokenização declarada, janela 4, frequência mínima 3, segmento de 19
tokens e bins `[0, 400, 600, 800, 1000, 2200]`.

### 8. Autoavaliação do exemplo

| Critério | Nota | Evidência |
|---|---:|---|
| escopo e qualidade | 2 | pergunta, unidade, cobertura e artificialidade declaradas |
| correção quantitativa | 2 | denominadores, convenções, extremo e contingência verificados |
| exploração textual | 2 | regras, frequências, concordância, PMI e TTR documentadas |
| visualização e acessibilidade | 2 | quatro famílias, tabelas e descrição alternativa |
| retorno aos casos | 2 | D023, D001 e D003 qualificam agregados diferentes |
| hipóteses e limites | 2 | três hipóteses alternativas e limites específicos |
| reprodutibilidade | 2 | entradas, ordem e parâmetros informados |
| **Total** | **14/14** | exemplo integralmente preenchido |

Uma pesquisa real pode receber nota alta mesmo com dados incompletos ou hipóteses
incertas. O que se avalia é a adequação, a transparência e a capacidade de reconhecer
os limites — não a produção de resultados “bonitos”.
