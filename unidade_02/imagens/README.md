# Recursos visuais da Unidade 2

As imagens desta pasta apoiam relações conceituais que seriam mais difíceis de
compreender apenas em prosa. Os notebooks mantêm a explicação textual e usam
caminhos relativos, permitindo execução offline, no Jupyter e após a clonagem
do repositório no Google Colab.

## Diagramas autorais

Os sete SVGs foram produzidos especificamente para esta unidade pelo script
`scripts/construir_imagens_unidade_02.py` e seguem a licença geral do
repositório:

- `00_percurso_unidade.svg` — percurso cumulativo dos cinco notebooks;
- `01_populacao_acessivel_corpus.svg` — relação entre população de interesse,
  população acessível, corpus e mediações;
- `01_papel_das_fontes.svg` — mudança do papel de uma fonte conforme a pergunta;
- `02_cadeia_ausencias.svg` — pontos distintos de produção das ausências;
- `02_cobertura_catalogo_corpus.svg` — comparação calculada entre catálogo e
  corpus por grupo representado;
- `03_documentacao_proveniencia.svg` — funções complementares de identificador,
  dicionário de dados e proveniência;
- `04_protocolo_integrado.svg` — articulação das partes do protocolo da base.

Todos os SVGs contêm `<title>`, `<desc>` e rótulos que não dependem somente de
cor. A comparação de cobertura é reconstruída a partir de
`dados/catalogo_fontes.csv`, evitando divergência entre a figura e o
experimento.

## Ilustração conceitual gerada

### `00_abertura_conceitual.png`

- **Finalidade:** abertura visual da Unidade 2.
- **Origem:** gerada em 4 de setembro de 2026 com a ferramenta integrada de
  geração de imagens da OpenAI.
- **Natureza:** ilustração conceitual; não representa fontes, instituições ou
  acervos históricos reais.
- **Alterações posteriores:** nenhuma; o arquivo foi copiado integralmente da
  saída selecionada.
- **Texto alternativo:** conjunto heterogêneo de fontes atravessa filtros de
  seleção até formar uma base organizada; registros não selecionados permanecem
  documentados e ligados à cadeia de proveniência.

### Prompt final

```text
Use case: scientific-educational
Asset type: wide conceptual opening illustration for Unit 2 of a master's-level
Jupyter course in Digital Humanities
Primary request: represent the construction of a research database as a
critical, documented process rather than a neutral pile of records
Scene/backdrop: warm cream background; archival folders, index cards and varied
source fragments enter a sequence of translucent selection gates; some records
continue into an organized dataset while excluded records remain visibly
documented at the side; metadata tags, a provenance trail and a small magnifying
lens suggest audit and review
Subject: sources, selection, coverage, documentation and critical review; no
people and no real historical document
Style/medium: polished editorial illustration with subtle paper texture and
crisp geometric forms, visually compatible with an academic notebook
Composition/framing: wide landscape composition, approximately 3:1, clear
left-to-right flow with generous margins and no embedded words
Lighting/mood: calm, rigorous, reflective
Color palette: deep navy, muted teal, terracotta, plum and sand on warm cream;
strong accessible contrast
Text: no text, no letters, no numbers
Constraints: conceptual illustration only; excluded records must remain visible
rather than being discarded; distinguish sources, selection gates, organized
data and provenance through shape as well as color; no logos, no watermark
Avoid: photorealistic archives, fake handwriting, historical scenes, people,
decorative clutter, neon technology, binary code, floating dashboards,
stock-photo aesthetic
```

## Princípios de uso

- Os diagramas não substituem definições, tabelas ou resultados executáveis.
- A ilustração de abertura não deve ser interpretada como evidência histórica.
- Barras da comparação de cobertura descrevem apenas os dados fictícios.
- Alterações nos dados exigem nova execução do script de construção das imagens.
