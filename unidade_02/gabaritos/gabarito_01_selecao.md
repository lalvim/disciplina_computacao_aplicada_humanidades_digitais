# Gabarito orientativo — Fontes e seleção

## Resultado do experimento

Os critérios incluem nove registros: A001, A002, A004, B001, B002, C001, C002,
C003 e C004. Sete registros são excluídos. Um item pode acumular motivos de
exclusão; por isso, a soma dos motivos não coincide necessariamente com o total
excluído.

| Motivo | Quantidade | Registros |
|---|---:|---|
| fora do período | 4 | A005, B004, C005 e D002 |
| não localizado | 1 | D001 |
| sem digitalização | 5 | A003, B003, C005, D001 e D002 |
| acesso incompatível | 3 | A003, D001 e D002 |

## Interpretação esperada

- “não digitalizado” descreve infraestrutura e acesso, não o fenômeno;
- excluir itens não digitalizados reduz instituições, tipos e grupos de modo
  desigual;
- acesso mediante autorização exige procedimento e registro, não exclusão
  automática;
- o corpus final deve ser acompanhado da tabela de decisões.

## Critérios da atividade

A resposta deve distinguir população de interesse, população acessível e
corpus; relacionar o papel das fontes à pergunta; formular regras verificáveis;
prever casos limítrofes; e explicar como exclusões serão preservadas.

## Exemplo de resposta — protocolo de seleção

O exemplo abaixo responde ao roteiro do notebook. Ele usa a base fictícia e
não constitui a única solução possível.

**População de interesse:** itens documentais catalogados pelas quatro
instituições fictícias entre 1890 e 1900 que permitam examinar como diferentes
grupos sociais aparecem na composição do acervo disponível.

**População acessível e condições de acesso:** os 16 registros do catálogo
didático formam o levantamento inicialmente acessível. A consulta efetiva está
condicionada a localização, existência de representação digital e acesso
público ou mediante autorização. Itens restritos continuam registrados, mas
não entram no corpus desta etapa.

**Unidade de análise:** cada item documental identificado por `id_fonte`. As
contagens descrevem itens catalogados, não pessoas, acontecimentos ou a
importância histórica dos grupos.

**Fontes e relação com a pergunta:** atas, requerimentos, cartas, fotografias,
jornais e diários seriam fontes primárias se a pergunta investigasse os
contextos e atores que os produziram. O catálogo é um dado derivado para estudar
esses documentos, mas pode ser tratado como fonte primária se a pergunta se
voltar às práticas de descrição, digitalização e acesso da instituição.

**Critérios de inclusão, justificativas e evidências:** incluir registros com
`ano` entre 1890 e 1900, `localizado = sim`, `digitalizado = sim` e
`condicao_acesso` igual a `público` ou `mediante autorização`. O período decorre
da pergunta; localização e digitalização tornam a atividade viável a distância;
a condição de acesso evita utilizar itens sem autorização. A evidência de cada
decisão fica nos campos correspondentes do catálogo.

**Critérios de exclusão e casos limítrofes:** excluir itens fora do período,
não localizados, não digitalizados ou com acesso restrito/sem autorização. A003
é um caso limítrofe porque está no período e foi localizado, mas não foi
digitalizado e possui acesso restrito. Antes de uma exclusão definitiva, seria
necessário consultar o custodiante sobre acesso presencial ou autorização.
C004, de 1900, deve ser incluído porque o intervalo foi definido como inclusivo.

**Como as exclusões serão registradas:** manter uma tabela com uma linha por
`id_fonte` e colunas booleanas para cada regra, além de `incluido`, data da
decisão, responsável e observação. Não apagar registros excluídos: preservar os
motivos permite auditar o recorte e testar critérios alternativos.

### Por que esta resposta é defensável?

Ela liga cada regra à pergunta ou a uma condição de viabilidade, explicita a
unidade contada, conserva casos excluídos e reconhece que o corpus remoto não é
sinônimo da população histórica nem de todos os materiais existentes.
