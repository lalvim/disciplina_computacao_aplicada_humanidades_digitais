# Parecer — Alinhamento

## Identificação

**Dimensão:** ementa, objetivos, diretrizes e produto  
**Versão:** commit `4e89d70` com alterações locais  
**Data:** 30 de julho de 2026  
**Decisão:** **aprovada com ajustes**

## Síntese

Os nove conteúdos da Unidade 1 estão presentes e conectados ao produto previsto.
O percurso não antecipa modelos estatísticos ou processamento textual de
unidades posteriores. A oficina final concretiza a formulação inicial da
pergunta.

O alinhamento formal é forte. Os ajustes necessários dizem respeito à
profundidade de “pesquisa orientada por dados” e à explicitação da relação entre
cada produto parcial e a entrega.

## Matriz de cobertura

| Conteúdo | Local | Profundidade | Atividade | Situação |
|---|---|---|---|---|
| Humanidades Digitais | Notebook 01 | introdutória | reflexão | parcial |
| Tipos de pergunta | Notebook 01 | adequada | classificação | coberto |
| Operacionalização | Notebook 02 | adequada | mapa | coberto |
| Unidade de análise | Notebook 02 | adequada | experimento/reflexão | coberto |
| População, amostra e corpus | Notebook 03 | adequada | filtros/ficha | coberto |
| Variáveis, categorias, documentos e metadados | Notebook 02 | adequada | comparação | coberto |
| Tipos de dados | Notebook 03 | adequada | leitura de formatos | coberto |
| Evidência e interpretação | Notebook 03 | adequada | cadeia | coberto |
| Limites da quantificação e automação | Notebook 03 e 04 | adequada | avaliação crítica | coberto |

## Achados

### AL-001 — Humanidades Digitais apenas parcialmente desenvolvidas

**Gravidade:** alta.  
**Local:** Notebook 01, primeira seção.  
**Evidência:** o campo é definido de modo plural, mas sem história, exemplos de
projetos, comunidade de práticas ou debate bibliográfico.  
**Consequência:** o primeiro conteúdo da ementa é mencionado com correção, mas
não ensinado com profundidade equivalente aos demais.  
**Ação:** incluir breve enquadramento histórico, dois projetos reais contrastantes
e leitura acadêmica.

### AL-002 — Produtos parciais não são explicitamente reutilizados

**Gravidade:** média.  
**Local:** transições para o Notebook 04.  
**Evidência:** a oficina repete campos dos produtos anteriores, mas não instrui o
estudante a copiar, revisar e justificar mudanças.  
**Ação:** indicar em cada seção qual produto recuperar e incluir campo “o que
mudou e por quê”.

### AL-003 — Critério automático verifica presença, não profundidade

**Gravidade:** baixa.  
**Local:** `scripts/validar_unidade_01.py`, `validar_cobertura`.  
**Evidência:** a checagem procura termos.  
**Consequência:** “9/9 tópicos” pode ser interpretado como validação pedagógica.  
**Ação:** renomear a mensagem para “presença textual” e manter a profundidade
como responsabilidade da revisão humana.

## Produto final

O produto está alinhado. Inclui pergunta, tipo, unidade, corpus,
operacionalização, evidência e limites. Deve incorporar referência conceitual
para atingir o nível de mestrado, mas não precisa antecipar a base processável
da Unidade 3.

## Condições para aprovação plena

1. resolver AL-001;
2. resolver AL-002;
3. distinguir validação estrutural de revisão acadêmica.

