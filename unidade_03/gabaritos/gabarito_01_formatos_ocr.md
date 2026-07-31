# Gabarito orientativo — Formatos e OCR

O inventário deve registrar a estrutura interna, não só a extensão. CSV requer
separador e encoding; XLSX requer planilha; JSON/XML exigem caminho na
hierarquia; TXT requer convenção externa; PDF deve ser testado para camada
textual. Extração e OCR devem produzir saídas separadas e ligadas à fonte.

No exemplo, o PDF textual retorna “Documento D001 com camada textual”. O OCR
deve ser comparado à referência `ESCOLA NOTURNA E TRABALHO - 1890`. Aceitar
variações depende da finalidade: busca pode tolerar erros que uma citação não
tolera. A resposta deve registrar ferramenta, idioma, segmentação e amostra de
controle.
