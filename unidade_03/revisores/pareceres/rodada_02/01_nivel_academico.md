# Parecer — Nível acadêmico — Rodada 2

**Data:** 4 de setembro de 2026

**Decisão:** revisão obrigatória — **5/6**.

## Evidências examinadas

- Notebook 00: problema, regra de camadas e produto;
- Notebook 01: formatos, PDF e experimento de OCR;
- Notebook 02: normalização, ausências e duplicatas;
- Notebook 03: cardinalidade, junções e integração;
- Notebook 04: autonomia, rubrica e produto final;
- gabaritos e dados intermediários gerados.

## Avaliação

A unidade excede um tutorial de sintaxe. Preservação do bruto, reversibilidade,
cardinalidade, razões de ausência e crítica à metáfora da limpeza exigem
julgamento metodológico compatível com mestrado. A oficina também pede que o
estudante delimite o que a base processável ainda não permite concluir.

## Achados

| ID | Gravidade | Evidência | Análise | Recomendação |
|---|---|---|---|---|
| U3-ACA-01 | alta | Notebook 02, seção 4; `dados/intermediarios/catalogo_normalizado.csv` | A operação `pd.to_datetime(..., dayfirst=True)` converte datas ISO incorretamente e transforma formatos válidos em ausências. D001 vira `1890-05-01`, D004 vira `1893-12-03`, D007 vira `1901-09-04` e cinco registros resultam em `NaT`. Isso contradiz a defesa da preservação de sentido e torna a base derivada academicamente insegura. | Separar formatos explicitamente: ISO completo, dia/mês/ano, ano isolado e valor desconhecido. Representar precisão em campo próprio e testar cada caso antes de exportar. |

Não há problema de nível na seleção dos conceitos; a revisão é obrigatória
porque o principal exemplo de transformação produz evidência incorreta.
