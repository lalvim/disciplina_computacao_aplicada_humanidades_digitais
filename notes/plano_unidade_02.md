# Plano de execução — Unidade 2

**Situação:** executado em 30 de julho de 2026 e ampliado em 4 de setembro de
2026. A ampliação introduz FAIR, CARE e *Datasheets for Datasets* antes da
oficina final.

Este plano segue as
[diretrizes de formatação e escrita do material](diretrizes_formatacao_material.md)
e dá continuidade ao produto elaborado na Unidade 1.

## 1. Escopo

**Unidade:** Como construir uma base adequada à pergunta?

**Problema orientador:** Quais dados são necessários e como saber se eles
representam adequadamente o fenômeno investigado?

**Carga horária sugerida:** 8 horas, distribuídas em duas semanas.

**Produto da unidade:** Protocolo da base contendo descrição das fontes,
unidades de análise, critérios de seleção, cobertura, metadados, proveniência,
limitações e cuidados éticos e legais.

## 2. Objetivos de aprendizagem

Ao concluir a unidade, o estudante deverá ser capaz de:

1. relacionar pergunta, unidade de análise, população de interesse e corpus;
2. distinguir fonte primária, fonte secundária e dado derivado conforme a
   pergunta e a cadeia de produção;
3. formular e aplicar critérios reproduzíveis de inclusão e exclusão;
4. avaliar cobertura sem confundi-la automaticamente com representatividade;
5. identificar vieses de seleção, ausências e silêncios documentais;
6. especificar metadados e elaborar um dicionário de dados;
7. propor identificadores estáveis e verificar sua unicidade;
8. registrar proveniência e transformações previstas;
9. distinguir encontrabilidade, acesso, interoperabilidade e reuso;
10. situar CARE na soberania e governança de dados indígenas;
11. documentar motivação, composição, usos, distribuição e manutenção;
12. reconhecer responsabilidades éticas e questões legais da coleta;
13. documentar uma base defensável para o projeto da disciplina.

## 3. Organização dos materiais

```text
unidade_02/
├── 00_guia_da_unidade.ipynb
├── 01_fontes_populacao_e_selecao.ipynb
├── 02_cobertura_vieses_e_silencios.ipynb
├── 03_metadados_identificadores_e_proveniencia.ipynb
├── 04_governanca_reuso_e_documentacao_de_bases.ipynb
├── 05_oficina_protocolo_da_base.ipynb
├── dados/
├── gabaritos/
├── revisores/
├── exercicios_unidade_02_texto.md
├── referencias.md
└── README.md
```

## 4. Conteúdo dos notebooks

### Notebook 00 — Guia da unidade

- retomada do projeto da Unidade 1;
- objetivos, percurso, carga e produto;
- apresentação do estudo de caso didático;
- diagnóstico inicial e critérios de avaliação.

### Notebook 01 — Fontes, população e seleção

- população de interesse, população acessível e corpus;
- fontes primárias e secundárias como relações com a pergunta;
- dados governamentais, institucionais e documentais;
- critérios de inclusão e exclusão;
- experimento de seleção reproduzível;
- registro e justificação das exclusões.

**Produto parcial:** protocolo de seleção.

### Notebook 02 — Cobertura, vieses e silêncios

- cobertura temática, temporal, geográfica, institucional e social;
- representatividade como argumento dependente do desenho;
- viés de seleção;
- ausência de registro, ausência na base e valor ausente;
- silêncios documentais e relações de poder;
- comparação computacional entre universo acessível e corpus selecionado.

**Produto parcial:** matriz de cobertura, lacunas e consequências.

### Notebook 03 — Metadados, identificadores e proveniência

- metadados descritivos, administrativos, estruturais e de proveniência;
- dicionário de dados;
- identificadores e unicidade;
- cadeia de custódia e proveniência;
- verificação computacional de campos, domínios, duplicatas e rastreabilidade;
- documentação da origem sem realizar ainda a limpeza da Unidade 3.

**Produto parcial:** dicionário de dados e registro de proveniência.

### Notebook 04 — Governança, reuso e documentação de bases

- princípios FAIR e sua ênfase em reutilização por pessoas e máquinas;
- diferença entre acessibilidade e abertura irrestrita;
- princípios CARE no contexto da soberania de dados indígenas;
- relações e tensões entre FAIR e CARE;
- ciclo de vida proposto em *Datasheets for Datasets*;
- adaptação crítica para bases históricas e culturais;
- auditoria computacional limitada a evidências verificáveis;
- discussão em duplas sobre autoridade, acesso e usos;
- elaboração de ficha de governança e documentação.

**Produto parcial:** ficha com evidências FAIR, análise situada de governança e
minidatasheet.

### Notebook 05 — Oficina do protocolo da base

- adequação da base à pergunta;
- fontes e condições de acesso;
- unidade, população e corpus;
- inclusão, exclusão e registro das decisões;
- cobertura, vieses, ausências e silêncios;
- esquema de metadados e identificadores;
- proveniência;
- ética, proteção de dados, direitos autorais e termos de uso;
- plano de contingência e rubrica de autoavaliação.

**Produto final:** protocolo documentado da base do projeto.

## 5. Estratégia didática

Markdown será usado para conceitos, decisões, justificativas e interpretação.
Python será usado quando operações sobre registros permitirem observar as
consequências de critérios de seleção, calcular cobertura, verificar
identificadores ou auditar metadados. Não será usado como formulário.

Os dados didáticos serão fictícios, pequenos e deliberadamente imperfeitos.
Eles incluirão lacunas de cobertura e registros excluíveis para que o estudante
possa distinguir erro técnico de limitação documental.

## 6. Cronograma sugerido

### Semana 1 — 4 horas

1. preparação e diagnóstico — 30 minutos;
2. Notebook 00 — 20 minutos;
3. Notebook 01 — 1 hora e 30 minutos;
4. Notebook 02 — 1 hora e 40 minutos.

### Semana 2 — 4 horas

1. Notebook 03 — 1 hora e 15 minutos;
2. Notebook 04, incluindo discussão em duplas — 1 hora e 25 minutos;
3. Notebook 05 e revisão por pares — 1 hora;
4. revisão objetiva — 20 minutos.

Os trechos introdutórios sobre CARE e *datasheets* que antes apareciam nos
Notebooks 02 e 03 foram convertidos em transições para o Notebook 04. A ficha
produzida nele reduz o tempo de preenchimento da oficina, preservando as oito
horas totais em vez de apenas acrescentar conteúdo.

## 7. Dependências e limites de escopo

- Python 3;
- `pandas`;
- execução integralmente offline.

Limpeza, padronização, junções, extração de texto e OCR serão tratados na
Unidade 3. A Unidade 2 pode diagnosticar esses problemas, mas não ensinará
ainda suas técnicas de correção.

## 8. Etapas de execução

1. registrar este plano;
2. verificar referências acadêmicas, técnicas e normativas;
3. criar dados didáticos e documentação de proveniência;
4. produzir os seis notebooks;
5. preparar exercícios e gabaritos;
6. criar roteiros de revisão adaptados à Unidade 2;
7. executar todos os notebooks;
8. validar cobertura, coerência, acessibilidade e carga;
9. executar a primeira rodada de revisores;
10. corrigir achados necessários antes da publicação.

## 9. Critérios de conclusão

- os doze conteúdos da ementa estarão ensinados e aplicados;
- toda seleção deixará rastros reproduzíveis;
- cobertura e representatividade serão conceitualmente distinguidas;
- ausências documentais não serão reduzidas a valores nulos;
- metadados, dicionário, identificadores e proveniência serão demonstrados;
- FAIR, CARE e *datasheets* serão distinguidos e aplicados sem automatizar
  decisões de governança;
- ética e questões legais serão apresentadas como parte do desenho;
- todos os notebooks executarão sem erros;
- exercício, gabaritos e oficina usarão terminologia consistente;
- o produto final permitirá auditar a adequação da base à pergunta.
