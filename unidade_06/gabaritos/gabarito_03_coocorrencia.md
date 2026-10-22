# U06-A04 — Gabarito — coocorrência

## Exemplo de resolução

Filtram-se documentos da Capital, explode-se `entidades`, constrói-se incidência e calcula-se $B^TB$. O peso é o número de documentos do recorte em que o par aparece. Para o par mais forte, listam-se IDs e notas dos documentos.

### Produto esperado

- matriz com documentos nas linhas e entidades nas colunas;
- diagonal zerada na projeção;
- lista sem pares duplicados;
- peso definido em linguagem corrente;
- tabela com os documentos que sustentam um par;
- comparação com o recorte completo.

**Resposta-modelo:** “O par é recorrente sob a regra de mesmo documento; isso não comprova contato. A projeção depende do recorte e documentos com três entidades geram três pares.”
