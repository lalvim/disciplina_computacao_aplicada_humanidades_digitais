# Proposta de trilha de trabalhos do projeto integrador

## Finalidade

Esta pasta propõe como transformar os produtos das unidades em entregas de um
mesmo projeto de pesquisa. Ela ainda não altera os notebooks da disciplina. Seu
objetivo é orientar uma reformulação posterior das oficinas, dos gabaritos, das
rubricas e do sistema de avaliação.

A trilha preserva um **problema humanístico central** e um **corpus-base
versionado**. Pergunta, recorte, categorias e métodos podem mudar, desde que as
mudanças sejam registradas e justificadas. Continuidade não significa impedir a
revisão; significa tornar a revisão rastreável.

## Arquitetura

```text
NÚCLEO CUMULATIVO
U01 proposta
  ↓
U02 protocolo da base
  ↓
U03 base processável
  ↓
U04 relatório exploratório
  ↓
U05 análise comparativa
  ↓
MÉTODOS CONDICIONAIS
U06 associação ou rede ─┐
U07 regressão           │
U08 classificação      │ escolher segundo a pergunta,
U09 agrupamento         ├ o corpus e a viabilidade
U10 extração            │
U11 tempo ou espaço     │
U12 modelo de linguagem┘
  ↓
FECHAMENTO COMUM
U13 validade e robustez
  ↓
U14 projeto reprodutível e apresentação
```

## O que é obrigatório

Todos os estudantes realizam:

1. as entregas cumulativas das Unidades 1 a 5;
2. uma decisão de aplicabilidade em cada unidade condicional;
3. a incorporação de ao menos um método condicional adequado ao projeto;
4. o fechamento comum das Unidades 13 e 14.

O projeto final deve mobilizar ao menos dois tipos de evidência ou abordagem,
conforme o contexto da disciplina. Isso não significa aplicar todas as técnicas.

## Duas formas válidas de entrega nas unidades condicionais

### Forma A — incorporação ao projeto

Usada quando o método é pertinente e viável. O estudante entrega código,
resultado, inspeção de casos, avaliação e interpretação ligados ao seu corpus.

### Forma B — não adoção fundamentada

Usada quando o método não responde à pergunta ou quando o corpus não satisfaz
seus requisitos. O estudante entrega:

- diagnóstico de aplicabilidade;
- justificativa da não adoção;
- riscos de forçar o método;
- evidência de aprendizagem no laboratório didático da unidade;
- indicação de outro método mais adequado.

Não adotar um método, quando a decisão é tecnicamente e humanisticamente
justificada, constitui uma decisão metodológica válida.

## Estrutura desta pasta

### `01_nucleo_cumulativo/`

- `U01_proposta.md`
- `U02_protocolo_da_base.md`
- `U03_base_processavel.md`
- `U04_relatorio_exploratorio.md`
- `U05_analise_comparativa.md`

### `02_metodos_condicionais/`

- `README.md`
- `U06_associacao_ou_rede.md`
- `U07_regressao.md`
- `U08_classificacao.md`
- `U09_agrupamento_ou_topicos.md`
- `U10_extracao_de_informacoes.md`
- `U11_tempo_ou_espaco.md`
- `U12_modelos_de_linguagem.md`

### `03_fechamento_comum/`

- `U13_validade_e_robustez.md`
- `U14_projeto_final.md`

### `modelos/`

- `manifesto_do_projeto.md`
- `registro_de_mudancas.md`
- `manifesto_de_entrega.md`
- `decisao_de_aplicabilidade.md`
- `rubrica_transversal.md`

### Documento de implantação

- `04_decisoes_para_implantacao.md`

### Exemplo preenchido

- **[Exemplo preenchido completo, da U01 à U14](notebooks_de_entrega/EXEMPLO_PREENCHIDO_projeto_integrador_U01_a_U14.ipynb)**
- [`notebooks_de_entrega/README.md`](notebooks_de_entrega/README.md)
- um único notebook demonstra o encadeamento do projeto;
- as orientações específicas de cada entrega permanecem nas pastas da trilha;
- os notebooks das oficinas continuam sendo os materiais de trabalho das unidades.

## Regra de passagem entre unidades

Cada entrega deve declarar:

1. o que foi herdado da versão anterior;
2. o que foi mantido;
3. o que foi alterado;
4. por que a alteração foi necessária;
5. quais arquivos constituem a entrega;
6. quais decisões permanecem abertas;
7. o que a próxima unidade poderá utilizar.

## Versões sugeridas

| Momento | Versão do projeto | Versão típica do corpus |
|---|---|---|
| U01 | `v0.1-proposta` | corpus pretendido |
| U02 | `v0.2-protocolo` | `corpus-v0` ou inventário previsto |
| U03 | `v0.3-base` | `corpus-v1-processavel` |
| U04 | `v0.4-exploracao` | `corpus-v1.1`, se corrigido |
| U05 | `v0.5-comparacao` | mesma base ou subconjuntos documentados |
| U06–U12 | `v0.x-metodo` | base enriquecida ou derivada, com proveniência |
| U13 | `v0.9-validade` | versões avaliadas e congeladas |
| U14 | `v1.0-final` | versão final documentada |

## Estrutura sugerida do projeto do estudante

```text
projeto_integrador/
├── README.md
├── manifesto_projeto.md
├── CHANGELOG.md
├── dados/
│   ├── brutos/
│   ├── intermediarios/
│   └── derivados/
├── notebooks/
├── relatorios/
├── avaliacao/
├── referencias/
└── entregas/
    ├── U01/
    ├── U02/
    └── ...
```

Os dados brutos não precisam ser duplicados em todas as pastas de entrega. O
manifesto de cada entrega deve apontar para a versão e para os arquivos que a
compõem.

## Princípio de avaliação

A nota de uma unidade não deve premiar a aplicação indiscriminada de uma
técnica. Deve avaliar:

- alinhamento entre problema, dados e método;
- qualidade da justificativa;
- rastreabilidade das mudanças;
- correção técnica;
- interpretação humanística;
- inspeção de casos e erros;
- limites e responsabilidade;
- reprodutibilidade.

Uma rubrica transversal comum aparece em `modelos/rubrica_transversal.md`.

## Situação da proposta

Esta organização resolve a lógica das entregas, mas não resolve sozinha a carga
horária. As decisões que precisam anteceder a alteração dos notebooks estão em
`04_decisoes_para_implantacao.md`.
