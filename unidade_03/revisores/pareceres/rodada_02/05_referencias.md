# Parecer — Referências — Rodada 2

**Data:** 4 de setembro de 2026

**Decisão:** aprovada com ajuste baixo — **5/6**.

## Evidências examinadas

- `referencias.md` e citações dos notebooks;
- Rawson e Muñoz, Wickham, Van Hooland, Verborgh e De Wilde;
- Hill e Hengchen;
- documentação oficial de pandas, pypdf, Tesseract e Library of Congress;
- proveniência do extrato do IBGE.

## Avaliação

Os dados bibliográficos das leituras acadêmicas correspondem às publicações. A
documentação do pypdf sustenta a distinção entre extração e OCR; a documentação
do Tesseract sustenta a influência de resolução, ruído, inclinação e
segmentação; e a documentação do pandas sustenta `merge(validate=...,
indicator=True)`.

## Achados

| ID | Gravidade | Evidência | Análise | Recomendação |
|---|---|---|---|---|
| U3-REF-01 | baixa | `referencias.md`, documentação técnica | Os links de software apontam para documentação corrente e podem mudar de comportamento entre versões. A referência genérica ao pandas não encaminha diretamente à semântica de `to_datetime`, central ao erro encontrado. | Registrar versões testadas e acrescentar links específicos para `to_datetime`, `merge` e `melt`; manter a verificação antes de cada oferta. |
| U3-REF-02 | baixa | `proveniencia_base_publica.json` | A página do IBGE bloqueou leitura automatizada nesta revisão, embora o endereço e os quatro códigos estejam consistentes com o extrato usado. | Fazer verificação manual da página e atualizar a data de acesso antes da oferta; preservar a cópia local e sua proveniência. |

Fontes verificadas: [Rawson e Muñoz](https://dhdebates.gc.cuny.edu/read/untitled-f2acf72c-a469-49d8-be35-67f9ac1e3a60/section/07154de9-4903-428e-9c61-7a92a6f22e51),
[Wickham](https://www.jstatsoft.org/v59/i10/),
[Van Hooland et al.](https://programminghistorian.org/en/lessons/cleaning-data-with-openrefine),
[Hill e Hengchen](https://researchportal.helsinki.fi/en/publications/quantifying-the-impact-of-dirty-ocr-on-historical-text-analysis-e/),
[pandas](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.to_datetime.html),
[pypdf](https://pypdf.readthedocs.io/en/stable/user/extract-text.html),
[Tesseract](https://tesseract-ocr.github.io/tessdoc/ImproveQuality.html) e
[Library of Congress](https://www.loc.gov/preservation/digital/formats/).
