# Plano de produção dos slides — Unidades 1 a 14

## 1. Objetivo

Produzir uma apresentação em Markdown para cada unidade, coerente com os notebooks,
as atividades, as ilustrações e o projeto cumulativo da disciplina. As apresentações
seguirão as [diretrizes de slides](diretrizes_slides.md).

## 2. Organização dos arquivos

```text
slides/
├── README.md
├── unidade_01.md
├── unidade_02.md
├── unidade_03.md
├── unidade_04.md
├── unidade_05.md
├── unidade_06.md
├── unidade_07.md
├── unidade_08.md
├── unidade_09.md
├── unidade_10.md
├── unidade_11.md
├── unidade_12.md
├── unidade_13.md
├── unidade_14.md
└── imagens/
    └── unidade_XX/
```

O arquivo `slides/README.md` explicará como visualizar ou exportar as apresentações.

## 3. Estrutura comum de cada apresentação

1. capa e problema orientador;
2. exemplo inicial ilustrado;
3. pergunta de observação;
4. agenda;
5. objetivos;
6. blocos conceituais, cada um iniciado ou acompanhado por exemplo;
7. demonstração, tabela ou gráfico;
8. atividade breve ligada a um identificador da unidade;
9. erro frequente, limite ou contraponto;
10. retorno ao exemplo inicial;
11. relação com a entrega cumulativa;
12. síntese;
13. pergunta de saída;
14. referências.

## 4. Plano por unidade

### Unidade 1 — Problema computacional

- **Exemplo inicial:** uma pergunta ampla sobre participação cultural que admite
  representações incompatíveis.
- **Núcleo:** finalidades da pesquisa, operacionalização, unidades, corpus, variáveis,
  categorias e tipos de dados.
- **Ilustrações:** percurso pergunta–evidência; mapa de operacionalização; exemplos de
  arquivos estruturados, semiestruturados e não estruturados.
- **Fechamento:** formulação inicial da pergunta do projeto.

### Unidade 2 — Construção da base

- **Exemplo inicial:** duas bases plausíveis que representam populações diferentes.
- **Núcleo:** fontes, seleção, cobertura, metadados, identificadores, proveniência,
  FAIR, CARE e documentação de conjuntos de dados.
- **Ilustrações:** funil de seleção; mapa de ausências; ciclo de vida e governança.
- **Fechamento:** protocolo documentado da base.

### Unidade 3 — Transformação das fontes

- **Exemplo inicial:** a mesma informação em CSV, XLSX, JSON, XML, TXT e PDF.
- **Núcleo:** formatos, extração, OCR, estrutura larga/longa, limpeza, ausências,
  duplicatas, junções e integração.
- **Ilustrações:** linha do tempo dos formatos; pipeline de transformação; chaves de
  junção e tabelas normalizadas.
- **Fechamento:** primeira base processável.

### Unidade 4 — Exploração da base

- **Exemplo inicial:** média semelhante escondendo distribuições diferentes.
- **Núcleo:** tipos de variáveis, tendência central, dispersão, extremos, frequências,
  exploração textual e visualização.
- **Fórmulas:** média, variância, desvio-padrão e proporção.
- **Ilustrações:** hierarquia de variáveis; distribuições; comparação de gráficos.
- **Fechamento:** diagnóstico exploratório incorporado ao relatório.

### Unidade 5 — Comparação

- **Exemplo inicial:** diferença observada que muda após retirar um caso influente.
- **Núcleo:** estimativas, tamanhos de efeito, intervalos, testes, permutação,
  representação textual e similaridade.
- **Fórmulas:** diferença de médias, tamanho de efeito, Jaccard e cosseno.
- **Ilustrações:** distribuições sobrepostas; intervalo; espaço vetorial.
- **Fechamento:** comparação substantiva entre grupos ou documentos.

### Unidade 6 — Associações e redes

- **Exemplo inicial:** coocorrência documental interpretada indevidamente como relação
  social.
- **Núcleo:** tabelas cruzadas, correlação, confundimento, coocorrência, matrizes,
  grafos, centralidades e comunidades.
- **Fórmulas:** valores esperados, V de Cramér, correlações e medidas de rede.
- **Ilustrações:** projeção bipartida; correlação versus causalidade; tipos de
  centralidade.
- **Fechamento:** associação ou rede pertinente ao projeto.

### Unidade 7 — Modelos de associação condicionada

- **Exemplo inicial:** associação entre renda e equipamentos que muda ao considerar
  urbanização e escolaridade.
- **Núcleo:** regressão simples/múltipla, categorias de referência, controle,
  interações, resíduos, diagnóstico e regressão logística.
- **Fórmulas:** modelo linear, interação, probabilidade, chance e logito.
- **Ilustrações:** reta e resíduos; controle; curvas de interação e logística.
- **Fechamento:** modelo associativo ou não adoção fundamentada.

### Unidade 8 — Classificação

- **Exemplo inicial:** documento tematicamente ambíguo classificado com consequências
  diferentes para falso positivo e falso negativo.
- **Núcleo:** anotação, concordância, treino/teste, baseline, logística, árvore,
  TF-IDF, métricas, matriz de confusão e viés entre grupos.
- **Fórmulas:** precisão, revocação, F1 e kappa.
- **Ilustrações:** fluxo de anotação; divisão dos dados; matriz de confusão.
- **Fechamento:** protótipo e análise de erros.

### Unidade 9 — Agrupamentos e temas

- **Exemplo inicial:** os mesmos casos formam grupos diferentes após mudar a escala.
- **Núcleo:** padronização, distância, K-means, hierarquia, estabilidade, agrupamento
  textual e LDA.
- **Fórmulas:** distância euclidiana, padronização, silhueta e mistura de tópicos.
- **Ilustrações:** efeito da escala; dendrograma; termos e documentos por tópico.
- **Fechamento:** padrões tratados como hipóteses, não grupos naturais.

### Unidade 10 — Extração de informações

- **Exemplo inicial:** “Santa Rita” como cidade em um documento e embarcação em outro.
- **Núcleo:** NER, regras, dicionários, vinculação, desambiguação, relações, eventos,
  avaliação e redes derivadas.
- **Fórmulas:** precisão, revocação e F1 da extração.
- **Ilustrações:** menção–entidade; evento; propagação de erros para uma rede.
- **Fechamento:** base estruturada com rastreabilidade até a fonte.

### Unidade 11 — Tempo e espaço

- **Exemplo inicial:** salto de uma série causado por mudança de definição e mapa cuja
  interpretação muda entre contagem e taxa.
- **Núcleo:** crescimento, tendência, médias móveis, séries textuais, mapas, taxas,
  padronização, falácia ecológica e MAUP.
- **Fórmulas:** taxa, crescimento, média móvel e padronização direta.
- **Ilustrações:** ruptura temporal; janelas; mapas de contagem e taxa.
- **Fechamento:** transformação temporal ou distribuição espacial.

### Unidade 12 — Modelos de linguagem

- **Exemplo inicial:** resposta fluente que inventa um número ausente da fonte.
- **Núcleo:** representações, transformers, prompting, RAG, alucinação, sensibilidade,
  rastreabilidade, avaliação, baseline e privacidade.
- **Ilustrações:** arquitetura conceitual; prompt auditável; recuperação e verificação.
- **Fechamento:** experimento controlado ou não adoção responsável.

### Unidade 13 — Validade e vieses

- **Exemplo inicial:** boa métrica global escondendo desempenho pior em período ou
  grupo.
- **Núcleo:** validade de construto, interna e externa, baseline, casos, robustez,
  bootstrap, generalização, vieses e resultados inconclusivos.
- **Fórmulas:** métricas, diferença entre grupos e intervalo bootstrap.
- **Ilustrações:** cadeia de validade; faixa de especificações; cadeia de vieses.
- **Fechamento:** seção priorizada de ameaças à validade.

### Unidade 14 — Documentação e comunicação

- **Exemplo inicial:** projeto tecnicamente reproduzível que não pode publicar os dados
  por risco de reidentificação.
- **Núcleo:** README, dicionário, proveniência, versionamento, ambiente, checks,
  visualização, proteção, direitos, licenças, relatório e apresentação.
- **Fórmulas:** intervalo e exemplo didático de $k$-anonimato, com limites.
- **Ilustrações:** pacote reprodutível; escada da afirmação; plano de compartilhamento.
- **Fechamento:** versão final do projeto e banca simulada.

## 5. Etapas de produção

### Etapa 1 — Base editorial

1. criar `slides/README.md` e tema comum;
2. definir front matter, tipografia, cores, rodapé e componentes reutilizáveis;
3. testar LaTeX, imagens relativas e exportação.

### Etapa 2 — Unidades 1 a 4

Produzir e revisar os slides de formulação, dados, preparação e exploração.

### Etapa 3 — Unidades 5 a 7

Produzir comparação, associação/redes e regressão, com atenção especial às fórmulas.

### Etapa 4 — Unidades 8 a 10

Produzir classificação, agrupamento/tópicos e extração de informações.

### Etapa 5 — Unidades 11 a 14

Produzir tempo/espaço, modelos de linguagem, validade e comunicação final.

### Etapa 6 — Revisão transversal

1. verificar exemplos antes da teoria;
2. conferir agenda e transições;
3. validar fórmulas e referências;
4. verificar acessibilidade das ilustrações;
5. conferir coerência com notebooks e atividades;
6. validar links relativos e exportação das 14 apresentações;
7. revisar progressão e ausência de repetição desnecessária.

## 6. Critérios de conclusão

- 14 arquivos Markdown completos;
- aproximadamente 38–52 slides por unidade, ajustados ao conteúdo;
- agenda e exemplo inicial em todas as unidades;
- exemplos e ilustrações distribuídos ao longo da apresentação;
- fórmulas LaTeX renderizadas e explicadas;
- atividades com dinâmica e produto;
- referências citadas durante a apresentação e completas no encerramento;
- relação explícita com o relatório-notebook cumulativo;
- apresentação legível, acessível e exportável.
