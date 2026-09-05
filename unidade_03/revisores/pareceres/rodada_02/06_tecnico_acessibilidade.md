# Parecer — Técnico e acessibilidade — Rodada 2

**Data:** 4 de setembro de 2026

**Decisão:** revisão obrigatória — **3/6**.

## Evidências examinadas

- execução de todas as células desde os dados brutos;
- hashes dos arquivos brutos;
- ambiente sem Tesseract e uso do fallback;
- links e preparação do Colab;
- HTML, versão textual e gabaritos;
- código do validador da Unidade 3.

## Resultados positivos

- os cinco notebooks executam do início ao fim;
- os arquivos brutos mantêm os mesmos hashes;
- o fallback funciona sem Tesseract;
- os 18 itens do HTML correspondem ao gabarito;
- os links e células de preparação do Colab passam na validação;
- a oficina não usa Python como formulário.

## Achados

| ID | Gravidade | Evidência | Análise | Recomendação |
|---|---|---|---|---|
| U3-TEC-01 | alta | `pd.to_datetime(..., dayfirst=True)` no Notebook 02 | Com pandas 2.2.3, o primeiro formato é aplicado de modo incompatível à série mista; três datas ISO têm dia e mês invertidos e cinco valores viram `NaT`. O gabarito informa apenas uma data não parseável. Os derivados persistem esse erro. | Implementar parsing explícito por padrões, distinguir data completa de ano parcial, regenerar derivados e corrigir o gabarito. |
| U3-TEC-02 | média | `scripts/validar_unidade_03.py` | O validador confirma execução e presença de termos, mas não testa valores esperados. Por isso aprovou a base com datas corrompidas. Também exige literalmente `92%` e `Aprovada` no parecer antigo, o que torna a revisão circular e ignora novas rodadas. | Acrescentar asserções semânticas para datas, duplicatas, cardinalidades, saídas e gabaritos; validar apenas existência/estrutura dos pareceres, sem fixar antecipadamente sua decisão. |
| U3-TEC-03 | baixa | HTML e notebooks | Estrutura semântica, teclado, contraste automatizável e alternativa textual estão adequados; permanece ausente um teste manual com leitor de tela e ampliação. | Realizar teste manual antes da oferta e registrar ambiente, navegador e resultado. |

A execução sem exceções não basta para aprovação técnica enquanto as saídas
semanticamente incorretas forem aceitas pelos testes.
