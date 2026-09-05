# Gabarito — Exercícios de múltipla escolha

| Questão | Resposta | Justificativa-modelo |
|---:|:---:|---|
| 1 | B | Manter a entrada imutável e gerar derivados permite comparar versões e reconstruir cada transformação. |
| 2 | A | A linha precisa representar uma unidade de análise declarada; ela não equivale necessariamente a arquivo ou coluna. |
| 3 | C | PDF organiza páginas e pode conter caracteres codificados, imagens ou uma combinação dos dois, exigindo diagnóstico. |
| 4 | B | Um XLSX pode conter várias planilhas; registrar a planilha e os parâmetros identifica o objeto efetivamente importado. |
| 5 | C | A cópia local, acompanhada de proveniência e data, fixa a versão processada sem apagar a responsabilidade do produtor. |
| 6 | A | Extração acessa texto já codificado; OCR formula uma transcrição a partir dos pixels da imagem. |
| 7 | B | Uma amostra comparada a uma referência permite medir erro e localizar casos que exigem revisão. |
| 8 | B | No formato longo, cada linha passa a representar uma combinação entre documento, tema e período. |
| 9 | B | Preservar o original torna possível auditar perdas e modificar posteriormente uma regra de normalização. |
| 10 | B | O código identifica um município; somar, tirar média ou aplicar outras operações aritméticas não possui sentido substantivo. |
| 11 | B | Original e razão permitem distinguir data desconhecida, data parcial e formato inválido, que não são a mesma ausência. |
| 12 | B | Sem inspeção adicional, semelhança entre campos é evidência de uma possível duplicata, não prova para exclusão. |
| 13 | B | `validate="many_to_one"` testa se as chaves observadas respeitam a cardinalidade declarada para a junção. |
| 14 | A | `left_only` identifica uma linha preservada da tabela esquerda que não encontrou chave correspondente à direita. |
| 15 | B | A tabela documento–tema representa explicitamente uma relação 1:N sem sobrescrever temas ou criar listas opacas. |
| 16 | B | A ordem das células não registra sozinha ambiente, versões, parâmetros, entradas e testes necessários à reprodução. |
| 17 | B | “Limpeza” pode naturalizar equivalências e exclusões que resultam de escolhas interpretativas situadas. |
| 18 | B | A Unidade 4 requer uma base com chaves verificadas, testes, log e limites, e não apenas arquivos convertidos. |

## Exemplo de resposta justificada

Na questão 13, uma resolução completa poderia ser:

> **Resposta B.** O catálogo contém vários documentos associados ao mesmo município,
> enquanto a tabela de referência deve conter uma linha por código municipal. Por
> isso, a relação esperada é muitos-para-um. Usar
> `validate="many_to_one"` faz a operação falhar se a tabela municipal tiver a chave
> repetida, evitando que a junção multiplique silenciosamente os documentos. As
> alternativas A, C e D tratam de propriedades que não são verificadas por esse
> argumento.

O exemplo mostra o padrão esperado quando o professor solicitar justificativa: indicar
a alternativa, explicar o conceito, aplicá-lo ao caso e, quando útil, mostrar por que
as demais opções não respondem ao problema.
