# Gabarito orientativo — Limpeza e qualidade

Resultados esperados:

- tabela larga: 3 × 5; longa: 12 × 4 após separar tema e período;
- seis datas completas com precisão de dia;
- uma data parcial (`1892`), registrada no ano sem inventar dia e mês;
- uma data desconhecida e nenhuma data inválida;
- uma contagem de palavras ausente;
- nenhum gênero fora do mapa;
- D006 e D006-copia formam um grupo de possíveis duplicatas.

Não se deve apagar automaticamente D006-copia. A igualdade dos campos usados é
evidência para revisão, não prova de identidade. Valores originais devem
permanecer disponíveis. Datas parciais e desconhecidas não recebem precisão
inventada.

## Exemplo de resultado das datas

| ID | Original | Data normalizada | Ano | Precisão | Razão quando não há data completa |
|---|---|---|---:|---|---|
| D001 | `1890-01-05` | `1890-01-05` | 1890 | dia | — |
| D002 | `06/02/1891` | `1891-02-06` | 1891 | dia | — |
| D003 | `1892` | ausente | 1892 | ano | dia e mês não informados |
| D004 | `1893-03-12` | `1893-03-12` | 1893 | dia | — |
| D005 | `data desconhecida` | ausente | ausente | desconhecida | data não informada |
| D006 | `1900-08-20` | `1900-08-20` | 1900 | dia | — |
| D006-copia | `20/08/1900` | `1900-08-20` | 1900 | dia | — |
| D007 | `1901-04-09` | `1901-04-09` | 1901 | dia | — |

Esse resultado evita interpretar `1890-01-05` como 1.º de maio. A regra escolhe o
formato pelo padrão visível e só então aplica o parser correspondente.

## Exemplo de resolução — log de transformação

| Campo | Problema | Regra | Justificativa | Casos | Teste | Reversibilidade |
|---|---|---|---|---|---|---|
| tabela de indicadores | tema e período aparecem nos nomes das colunas | aplicar `melt` e separar `tema_periodo` em duas colunas | explicitar as dimensões e produzir uma linha por documento–tema–período | 3 linhas largas tornam-se 12 relações | conferir dimensões 3 × 5 antes e 12 × 4 depois | total, pois o arquivo largo permanece em `brutos` |
| `titulo` | caixa e espaços variam | retirar espaços externos, reduzir espaços internos, converter para minúsculas e remover acentos apenas na chave | permitir comparação sem substituir a grafia de apresentação | D001, D004 e D006-copia, entre outros | original permanece igual; chave não contém espaços externos | total, pois `titulo` é preservado |
| `municipio` | acentos, caixa e espaço duplicado variam | criar `municipio_chave` com a mesma função de chave textual | viabilizar comparação e auditoria; a apresentação vem da tabela de referência | São Paulo, Sao paulo, São  Paulo e Belo horizonte | quatro códigos encontram correspondência municipal | total, pois o original e o nome IBGE coexistem |
| `genero` | caixa, acentos e espaços variam | aplicar chave textual e mapa explícito para editorial, notícia, carta e manifesto | impedir categorias equivalentes apenas na grafia | 8 registros | nenhum gênero sem mapeamento; listar domínio final | total, com `genero_original` e mapa documentado |
| `data_documento` | formatos ISO, brasileiro, ano isolado e desconhecido coexistem | preservar original; reconhecer padrões completos explicitamente; guardar ano e precisão em colunas próprias | impedir inversão dia/mês e falsa precisão | 8 registros; D003 parcial e D005 desconhecido | seis datas completas iguais ao calendário esperado, um ano parcial, um desconhecido e zero inválidas | total, pois `data_original` é mantida |
| `palavras` | D003 não possui contagem | converter para número sem preencher artificialmente; registrar `não contado` | zero palavras seria uma afirmação diferente de contagem ausente | 1 registro | uma ausência numérica e uma razão correspondente | total, pois a ausência e sua razão permanecem explícitas |
| registro | D006 e D006-copia coincidem em título-chave, data, município e palavras | marcar ambos como `possivel_duplicata`; não excluir | sem consultar a fonte não há prova de que sejam o mesmo objeto | 2 registros no mesmo grupo candidato | conferir que ambos permanecem na tabela de 8 linhas | total; a marca pode ser revista após inspeção |

Uma interpretação-modelo: “A padronização aumenta a comparabilidade sem afirmar
que D003 ocorreu em 1.º de janeiro. O ano pode sustentar agregações anuais, mas não
comparações mensais ou diárias. D005 deve permanecer fora de análises temporais que
exijam ano, com a razão registrada.”
