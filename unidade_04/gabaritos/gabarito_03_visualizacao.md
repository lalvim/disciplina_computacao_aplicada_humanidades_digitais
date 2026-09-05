# Gabarito — Visualização exploratória

Este gabarito apresenta uma resolução possível com a base fictícia. Uma resposta
adequada deve justificar o gráfico pela pergunta e pela escala das variáveis,
apresentar a tabela correspondente e separar descrição, interpretação e limite.

## Exemplo 1 — Barras por tema

**Pergunta:** como os documentos se distribuem entre os temas atribuídos?

| Tema | Documentos | Proporção |
|---|---:|---:|
| educação | 6 | 25% |
| progresso | 6 | 25% |
| saúde | 6 | 25% |
| trabalho | 6 | 25% |

**Escolha do gráfico:** barras são apropriadas porque `tema` é nominal e o
objetivo é comparar frequências entre categorias.

**Descrição:** os quatro temas possuem seis documentos, correspondentes a 25%
dos 24 registros cada.

**Interpretação e limite:** a igualdade resulta da construção deliberada da base
didática. Não indica equilíbrio de temas em um corpus histórico real nem mede a
importância cultural de cada tema.

## Exemplo 2 — Histograma e boxplot

| Intervalo de palavras | Documentos |
|---|---:|
| 0–400 | 3 |
| 400–600 | 8 |
| 600–800 | 6 |
| 800–1.000 | 4 |
| 1.000–2.200 | 3 |

O boxplot apresenta $Q_1=459$, mediana de 621,5 e $Q_3=848,75$. O limite
superior de 1,5 IQR é 1.433,375 palavras. D023, com 2.100 palavras, deve aparecer
como ponto separado, e não como extremidade do whisker.

**Descrição:** a maior concentração ocorre entre 400 e 800 palavras; D023 está
isolado acima do limite superior.

**Interpretação e limite:** D023 merece inspeção documental, mas o gráfico não
demonstra erro e não autoriza exclusão automática. A aparência do histograma
também depende dos intervalos escolhidos.

## Exemplo 3 — Dispersão entre páginas e palavras

**Escolha do gráfico:** ambas as variáveis são quantitativas; cada ponto mantém
um documento como unidade de análise. Forma e cor podem distinguir gêneros, mas
os IDs e a tabela equivalente continuam necessários.

**Descrição:** há grande dispersão de palavras para números de páginas
semelhantes. D023 possui cinco páginas e 2.100 palavras. Na base, a correlação
linear entre páginas e palavras é aproximadamente 0,24.

**Interpretação e limite:** existe no máximo uma relação linear fraca neste
conjunto. O gráfico não demonstra que páginas causam maior extensão textual, e
D023 influencia fortemente qualquer resumo da relação.

## Exemplo 4 — Série temporal

Cada ano contém somente dois documentos. As médias variam de 457 palavras em
1895 a 1.445 em 1900. A média de 1900 é elevada por D023.

**Representação recomendada:** mostrar os 24 documentos como pontos ou cruzes e
sobrepor as médias anuais, sempre indicando `n = 2`. A linha entre médias é apenas
um auxílio visual.

**Limite:** os pontos ligados não demonstram mudança histórica contínua. A série
descreve a composição do corpus fictício e não uma população histórica.

## Exemplo 5 — Frequências textuais

Após a regra de tokenização e a retirada das stopwords declaradas, há 600 tokens
de conteúdo. Os dez primeiros termos — como `escola`, `noturna`, `instrução` e
`trabalho` — aparecem 24 vezes cada.

**Escolha do gráfico:** barras horizontais preservam valores e permitem ordenar
termos. Uma nuvem de palavras ocultaria diferenças pequenas e não apresentaria
uma escala verificável.

**Limite:** as frequências decorrem de frases repetidas na construção didática da
base. Elas servem para exercitar o procedimento, não para sustentar interpretação
histórica.

## Checklist de correção

Uma resposta completa deve incluir:

- pergunta e justificativa do tipo de gráfico;
- título informativo, eixos, unidades e denominador;
- tabela equivalente e identificação de casos relevantes;
- descrição alternativa que não dependa da imagem;
- interpretação situada e limite específico;
- retorno ao documento quando um extremo ou padrão exigir contexto.
