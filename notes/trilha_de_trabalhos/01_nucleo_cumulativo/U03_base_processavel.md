# U03 — Entrega cumulativa: primeira base processável

## Função na trilha

Implementar o protocolo da U02 sem romper a ligação entre fontes, transformações
e registros derivados.

## Entrada herdada

- protocolo `v0.2-protocolo`;
- fontes autorizadas;
- critérios de seleção;
- identificadores e campos previstos;
- riscos e limites conhecidos.

## Produto

**Pacote da primeira base processável — versão `v0.3-base`.**

## Conteúdo mínimo

- inventário de arquivos, formatos e versões;
- dados brutos preservados ou referências de acesso controlado;
- notebook ou script técnico executável;
- importação e extração parametrizadas;
- modelo das tabelas e unidade de cada linha;
- regras de normalização e transformação;
- representação de ausências e duplicatas;
- chaves, cardinalidades e auditoria de junções;
- tabelas derivadas;
- log de transformações;
- testes de esquema, domínios, chaves e contagens;
- relatório de qualidade e casos pendentes;
- instruções de reconstrução.

## Arquivos esperados

1. notebook técnico;
2. dados intermediários e derivados permitidos;
3. dicionário de dados atualizado;
4. log de transformação;
5. relatório de qualidade;
6. ficha de proveniência atualizada;
7. manifesto e registro de mudanças.

## Critérios de aceitação

- a base implementa o protocolo ou documenta seus desvios;
- arquivos brutos não foram sobrescritos;
- IDs permanecem rastreáveis;
- transformações possuem regra e teste;
- junções não multiplicam casos silenciosamente;
- outra pessoa consegue reconstruir a base;
- está claro o que a U04 pode e não pode analisar.

## Passagem para a U04

A U04 recebe uma versão congelada da base processável, seu dicionário, relatório
de qualidade e notebook de reconstrução.

