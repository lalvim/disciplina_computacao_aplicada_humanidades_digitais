# U06-A05 — Gabarito — grafos

## Exemplo de resolução

Comparam-se o nó de maior força e um nó periférico. Grau responde à diversidade de vizinhos; força, à soma de pesos; intermediação, aos caminhos. Recria-se o grafo com `peso >= 2` e registram-se nós ou pontes perdidos.

No exemplo executado, `Jornal Horizonte` possui a maior força e a maior intermediação. Isso orienta a inspeção de seus documentos, mas não autoriza chamá-lo de instituição dominante. O limiar `peso >= 2` remove vínculos únicos; a comparação deve registrar quais entidades ficam isoladas ou mudam de comunidade.

**Resposta-modelo:** “A posição é central no modelo documental, não prova liderança. Três documentos sustentam as arestas principais e mostram contextos distintos que o grafo agrega.”
