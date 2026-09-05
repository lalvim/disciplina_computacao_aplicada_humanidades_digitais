# Referências e leituras da Unidade 4

ARNOLD, Taylor; TILTON, Lauren. New Data? The Role of Statistics in DH. In:
GOLD, Matthew K.; KLEIN, Lauren F. (org.). *Debates in the Digital Humanities
2019*. University of Minnesota Press, 2019.
https://doi.org/10.5749/j.ctvg251hk.26.

DRUCKER, Johanna. Humanities Approaches to Graphical Display. *Digital
Humanities Quarterly*, v. 5, n. 1, 2011.
https://www.digitalhumanities.org/dhq/vol/5/1/000091/000091.html.

TUKEY, John W. *Exploratory Data Analysis*. Reading: Addison-Wesley, 1977.

SINCLAIR, Stéfan; ROCKWELL, Geoffrey. Text Analysis and Visualization: Making
Meaning Count. In: SCHREIBMAN, Susan; SIEMENS, Ray; UNSWORTH, John (org.). *A
New Companion to Digital Humanities*. Wiley, 2015.
https://doi.org/10.1002/9781118680605.ch19.

MANNING, Christopher D.; RAGHAVAN, Prabhakar; SCHÜTZE, Hinrich. *Introduction
to Information Retrieval*. Cambridge University Press, 2008.
https://nlp.stanford.edu/IR-book/.

PANDAS DEVELOPMENT TEAM. *pandas User Guide*. Seções sobre estatística
descritiva, categóricas, agrupamento e tabelas cruzadas.
https://pandas.pydata.org/docs/user_guide/.

## Plano de leitura

| Momento | Leitura | Finalidade |
|---|---|---|
| início | Arnold e Tilton (2019) | situar EDA em Humanidades Digitais |
| quantitativo | Tukey (1977), trechos | distinguir exploração e confirmação |
| textual | Sinclair e Rockwell (2015) | relacionar contagem e produção de sentido |
| visual | Drucker (2011) | criticar pressupostos gráficos |
| aprofundamento | Manning et al. (2008) | vocabulário, frequências e associação |

## Convenções matemáticas adotadas

- frequências, proporções, medidas de centro, quartis, intervalo interquartil e
  regra de inspeção do boxplot são apresentados como instrumentos de exploração,
  em diálogo com Tukey (1977);
- `var(ddof=1)` e `std(ddof=1)` são identificados como medidas amostrais com
  denominador $n-1$, coerentes com o padrão do pandas;
- quartis usam `quantile(..., interpolation="linear")`; outras convenções podem
  produzir valores diferentes e devem ser documentadas;
- a PMI usa probabilidades e frequências marginais das posições dos bigramas,
  conforme a apresentação de associação lexical em Manning, Raghavan e Schütze
  (2008);
- frequência relativa e diversidade lexical sempre declaram o conjunto usado no
  denominador.

Documentações técnicas devem ser verificadas antes de cada oferta.
