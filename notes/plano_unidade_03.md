# Plano de execução — Unidade 3

**Situação:** executado em 31 de julho de 2026. A primeira rodada dos seis
revisores aprovou a unidade com ajustes baixos de manutenção. A segunda rodada,
realizada em 4 de setembro de 2026, determinou revisão obrigatória antes da
oferta; consulte `unidade_03/revisores/pareceres/rodada_02/`.

Este plano segue as
[diretrizes de formatação e escrita do material](diretrizes_formatacao_material.md)
e usa o protocolo da base produzido na Unidade 2.

## 1. Escopo

**Unidade:** Como transformar fontes em dados analisáveis?

**Problema orientador:** Como preparar documentos e registros produzidos em
formatos diferentes sem perder a ligação com as fontes e as decisões de
transformação?

**Carga horária sugerida:** 10 horas, distribuídas em duas semanas. A carga é
maior que a das unidades anteriores porque inclui uma oficina técnica integrada.

**Produto:** Primeira versão processável da base do projeto, acompanhada de
registro de transformações, relatório de qualidade e vínculos entre textos,
metadados e indicadores.

## 2. Objetivos de aprendizagem

Ao concluir a unidade, o estudante deverá ser capaz de:

1. reconhecer princípios de uma estrutura tabular consistente;
2. importar CSV, planilha, JSON, XML e TXT, reconhecendo que PDF requer inspeção;
3. distinguir extração de texto existente de OCR sobre imagem;
4. avaliar erros e incertezas introduzidos pelo OCR;
5. importar uma base pública com proveniência e cópia local estável;
6. transformar dados entre formatos largo e longo;
7. limpar valores sem apagar sua forma original;
8. padronizar nomes, datas e códigos com regras explícitas;
9. detectar duplicatas exatas e possíveis, sem removê-las automaticamente;
10. diagnosticar e representar valores ausentes;
11. realizar junções com validação de chaves e cobertura;
12. integrar textos, metadados e indicadores preservando identificadores;
13. organizar um projeto em notebooks, dados brutos, intermediários e derivados.

## 3. Organização

```text
unidade_03/
├── 00_guia_da_unidade.ipynb
├── 01_formatos_importacao_e_extracao.ipynb
├── 02_estrutura_limpeza_e_qualidade.ipynb
├── 03_juncoes_integracao_e_reprodutibilidade.ipynb
├── 04_oficina_base_processavel.ipynb
├── dados/{brutos,intermediarios,derivados}/
├── imagens/
├── gabaritos/
├── revisores/
├── exercicios_unidade_03.html
├── exercicios_unidade_03_texto.md
├── referencias.md
└── README.md
```

## 4. Notebooks

### 00 — Guia

Retomada do protocolo, objetivos, ambiente, dados fictícios, diagnóstico e
produto. Introdução ao princípio: dados brutos são preservados; transformações
produzem novas camadas.

### 01 — Formatos, importação e extração

- affordances e limites de CSV, XLSX, JSON, XML, TXT e PDF;
- importação local com `pandas` e biblioteca padrão;
- base pública representada por uma cópia didática com proveniência;
- PDF com texto versus PDF de imagem;
- experimento introdutório de OCR e comparação com transcrição de referência;
- erros de OCR como dados a avaliar.

**Produto parcial:** inventário de fontes, formatos, leitores e riscos.

### 02 — Estrutura, limpeza e qualidade

- princípios de dados tabulares;
- largo e longo;
- espaços, caixa, acentos, categorias, nomes, datas e códigos;
- preservação de valores originais;
- ausências e razões de ausência;
- duplicatas exatas e potenciais;
- relatório antes/depois e regras de transformação.

**Produto parcial:** tabela intermediária e log de transformações.

### 03 — Junções, integração e reprodutibilidade

- chaves primárias e estrangeiras;
- cardinalidades 1:1, 1:N e N:N;
- `merge(..., validate=..., indicator=True)`;
- registros sem correspondência e expansão indevida de linhas;
- integração entre documentos, textos, metadados e indicadores;
- organização do projeto e execução ordenada.

**Produto parcial:** base integrada e relatório da junção.

### 04 — Oficina da base processável

- inventário e cópia imutável dos dados brutos;
- plano de importação;
- regras de limpeza e mapa de categorias;
- decisões sobre ausências e duplicatas;
- plano de OCR e controle de qualidade;
- junções e testes de integridade;
- exportação da primeira base processável;
- ficha de proveniência e limitações.

**Produto final:** pacote processável da base do projeto.

## 5. Estratégia didática

Python será usado porque transformação e auditoria são objetivos explícitos da
unidade. Toda operação terá pergunta, entrada, saída e interpretação. Decisões
substantivas, regras e justificativas permanecerão em Markdown.

O estudo de caso conterá erros deliberados e dados inteiramente fictícios. O
código nunca sobrescreverá os dados brutos. Cada correção produzirá coluna ou
arquivo derivado e será documentada.

O percurso visual combina uma abertura conceitual, diagramas SVG autorais e duas
imagens sintéticas controladas para o experimento de OCR. Figuras serão usadas
para processos, decisões e relações; resultados tabulares continuarão como tabelas
ou saídas reproduzíveis de código. Cada ilustração terá texto alternativo,
explicação no entorno e documentação em `unidade_03/imagens/README.md`.

## 6. Dependências

- Python 3;
- `pandas` e `openpyxl`;
- `pypdf` para PDF com camada textual;
- Pillow para produzir a imagem didática;
- Tesseract como dependência opcional de sistema para o experimento de OCR.

O notebook deverá continuar executável sem Tesseract, usando uma transcrição de
OCR previamente gerada e identificada como tal.

## 7. Limites de escopo

- não ensinar estatística descritiva ou visualização;
- não realizar OCR massivo nem treinamento de modelos;
- não coletar dados ao vivo durante a aula;
- não tratar limpeza como produção de uma versão definitivamente correta;
- não descartar automaticamente ausências, duplicatas ou registros sem junção.

## 8. Execução

1. registrar e revisar o plano;
2. verificar referências técnicas e acadêmicas;
3. criar dados brutos em múltiplos formatos;
4. construir os cinco notebooks;
5. produzir exercícios e gabaritos;
6. criar e executar seis revisores;
7. validar execução, cobertura, integridade e reprodutibilidade;
8. corrigir achados altos ou bloqueantes;
9. produzir e integrar o conjunto visual acessível;
10. marcar o plano como executado.

## 9. Critérios de conclusão

- os treze conteúdos estarão ensinados e aplicados;
- todos os formatos serão apresentados com código ou justificativa técnica;
- o material distinguirá extração de texto e OCR;
- dados brutos permanecerão inalterados;
- transformações e junções serão auditáveis;
- todos os notebooks executarão offline e em ordem;
- exercícios e gabaritos estarão consistentes;
- imagens terão função didática explícita, texto alternativo e arquivos locais;
- o pacote final preparará a exploração da Unidade 4.
