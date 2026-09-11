# Gabarito — representação textual

**Atividade associada:** `U05-A04`.

## Exemplo de resolução completa

1. Preservar `texto` e `id_documento`.
2. Documentar minúsculas, remoção de acentos, expressão regular e stopwords.
3. Construir uma linha por documento e uma coluna por termo.
4. Definir TF como contagem bruta e $idf=\log((N+1)/(df+1))+1$.
5. Comparar, em D001, a contagem com o peso TF-IDF e ler o texto original.
6. Agregar por período apenas após declarar seus limites.

**Resposta-modelo:** “O termo com maior TF-IDF é distintivo sob esta coleção e regra,
mas não é automaticamente o conceito central do documento. A leitura do trecho deve
verificar negação, enquadramento e repetição artificial.”

## Erros frequentes

- chamar zero de irrelevância;
- esquecer que Bag of Words perde ordem;
- comparar implementações com convenções IDF diferentes sem documentá-las.
