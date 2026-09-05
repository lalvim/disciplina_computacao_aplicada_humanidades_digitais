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

## Exemplo de entrada no log de transformação

| Campo | Problema | Regra | Justificativa | Casos | Teste | Reversibilidade |
|---|---|---|---|---|---|---|
| `data_documento` | formatos ISO, brasileiro, ano isolado e desconhecido coexistem | preservar original; reconhecer padrões completos explicitamente; guardar ano e precisão em colunas próprias | impedir inversão dia/mês e falsa precisão | 8 registros; D003 parcial e D005 desconhecido | seis datas completas iguais ao calendário esperado, um ano parcial, um desconhecido e zero inválidas | total, pois `data_original` é mantida |

Uma interpretação-modelo: “A padronização aumenta a comparabilidade sem afirmar
que D003 ocorreu em 1.º de janeiro. O ano pode sustentar agregações anuais, mas não
comparações mensais ou diárias. D005 deve permanecer fora de análises temporais que
exijam ano, com a razão registrada.”
