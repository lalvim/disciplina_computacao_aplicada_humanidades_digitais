# Gabarito orientativo — Formatos e OCR

O inventário deve registrar a estrutura interna, não só a extensão. CSV requer
separador e encoding; XLSX requer planilha; JSON/XML exigem caminho na
hierarquia; TXT requer convenção externa; PDF deve ser testado para camada
textual. Extração e OCR devem produzir saídas separadas e ligadas à fonte.

## Exemplo de inventário resolvido

| Fonte | Diagnóstico | Operação | Parâmetro ou teste | Saída | Risco |
|---|---|---|---|---|---|
| `documento_textual.pdf` | uma página com camada textual | extração com pypdf | verificar se `extract_text()` retorna conteúdo e conferir a página | texto extraído separado do PDF | ordem de leitura ou caracteres podem divergir da página |
| `pagina_digitalizada.png` | imagem sintética limpa, sem camada textual | OCR | Tesseract, idioma `eng`, segmentação `--psm 7`; comparar com referência | transcrição + CER/WER | mesmo resultado perfeito nesta linha não valida outras páginas |
| `pagina_digitalizada_degradada.png` | mesma linha, degradada de forma controlada | OCR | repetir os mesmos parâmetros para isolar o efeito da qualidade | transcrição + CER/WER | borrão, inclinação e marcas podem confundir caracteres |

No exemplo, o PDF textual retorna “Documento D001 com camada textual”. Na rota
offline fornecida com o material, a comparação de OCR produz:

| Condição | Transcrição | Erros em caracteres | CER | Erros em palavras | WER |
|---|---|---:|---:|---:|---:|
| imagem limpa | `ESCOLA NOTURNA E TRABALHO — 1890` | 0 | 0,000 | 0 | 0,000 |
| imagem degradada | `ESC0LA NOTURNA E TRABALH0 — 189O` | 3 | 0,094 | 3 | 0,500 |

Se o Tesseract estiver instalado, o resultado pode diferir segundo a versão e o
ambiente. Esse contraste não prova que toda imagem limpa terá erro zero; ele mostra
como um teste controlado ajuda a observar o efeito da qualidade da entrada.

## Exemplo de interpretação

Uma resposta adequada seria: “A versão degradada exigiu três substituições de
caractere na saída pré-computada. Isso pode ainda permitir localizar parte da frase,
mas já altera três palavras e pode enviesar contagens lexicais. Para citação, devo
conferir a página e corrigir a transcrição; para busca exploratória, preciso declarar
a taxa de erro e testar uma amostra maior.”

Aceitar variações depende da finalidade: busca pode tolerar erros que uma citação
não tolera. A resposta deve registrar ferramenta, versão quando disponível, idioma,
segmentação, amostra de controle, métrica e procedimento de revisão humana.
