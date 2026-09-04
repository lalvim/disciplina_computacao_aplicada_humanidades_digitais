# Gabarito orientativo — Metadados e proveniência

## Auditorias

O catálogo possui 16 registros, 16 identificadores únicos, nenhum identificador
ausente ou duplicado. Todos os campos observados estão documentados e os
domínios simples verificados não contêm valores inesperados.

Esses resultados não provam qualidade substantiva nem persistência dos
identificadores. Eles confirmam apenas propriedades verificadas.

## Produto parcial

Uma resposta adequada especifica:

- identificador independente de atributos mutáveis;
- escopo em que a unicidade é garantida;
- definições e domínios explícitos;
- origem e responsável por cada campo;
- vínculo entre fonte e registro derivado;
- versão, data de acesso, agentes e transformações;
- limitações que não podem ser detectadas pelo código.

## Exemplo de resposta — documentação do projeto

**Estratégia de identificadores e escopo de unicidade:** cada item receberá um
`id_fonte` textual, único e não vazio dentro da versão publicada da base. O
identificador não incorporará ano, instituição ou gênero, pois esses atributos
podem ser corrigidos. Quando existir um código do acervo de origem, ele será
preservado separadamente em `id_origem`.

**Metadados mínimos e justificativa:** registrar `id_fonte`, instituição
custodiante, tipo documental, data ou intervalo, local, grupo representado,
estado de localização, disponibilidade digital, condição de acesso e qualidade
dos metadados. Esses campos permitem identificar o item, reconstruir o recorte,
avaliar cobertura e distinguir inexistência, inacessibilidade e falta de
descrição.

**Exemplo de entrada do dicionário de dados:**

| Campo | Definição | Tipo/domínio | Origem | Regra | Limitação |
|---|---|---|---|---|---|
| `grupo_representado` | grupo mais diretamente registrado no item | categoria; vocabulário documentado | atribuição da equipe | um valor principal por item nesta versão | simplifica documentos com múltiplos grupos e não mede voz ou protagonismo |
| `condicao_acesso` | condição informada pelo custodiante | público, mediante autorização, restrito ou sem autorização | instituição custodiante | registrar o valor consultado, sem convertê-lo em licença | pode mudar e exige nova verificação antes da publicação |

**Origem, custodiante, versão e data de acesso:** o catálogo didático foi
produzido pela equipe docente em 30 de julho de 2026 a partir de registros
inteiramente simulados. Em um projeto real, cada registro informaria instituição
custodiante, URL ou referência arquivística, versão e data de consulta.

**Transformações previstas e responsável:** a equipe de pesquisa importará o
CSV, validará identificadores, normalizará apenas cópias de trabalho e criará a
tabela de inclusão/exclusão. Cada etapa receberá data, agente, versão de entrada,
script ou notebook usado e arquivo de saída. Os dados recebidos não serão
sobrescritos.

**Relação entre registro derivado e fonte:** `id_fonte` será mantido em todas as
tabelas derivadas. Uma transcrição ou imagem digital incluirá também
`arquivo_origem`, referência arquivística e, quando pertinente, página ou
segmento. Assim, uma contagem poderá ser rastreada até o registro e o documento
que a sustentam.

### Exemplo de registro de proveniência

| Entidade de entrada | Atividade | Agente | Saída | Data | Observação |
|---|---|---|---|---|---|
| `catalogo_fontes.csv`, versão 1 | aplicação dos quatro critérios de seleção | pesquisadora responsável | `decisoes_selecao.csv`, versão 1 | 2026-09-04 | preserva uma linha por item e todos os motivos de exclusão |

### Por que esta resposta é defensável?

Ela não reduz documentação a nomes de colunas: define significado, domínio,
origem, transformação, responsabilidade e limitações, mantendo a ligação entre
o dado derivado e a fonte.
