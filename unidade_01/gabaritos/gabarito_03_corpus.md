# Gabarito orientativo — Dados, corpus e evidências

## 0. Retomada — exemplo de resolução

**Unidade de análise recuperada do Notebook 02:** documento jornalístico.

**Indicador e fonte:** tema dominante atribuído após leitura do texto integral,
registrado no campo `tema_dominante` segundo um guia de anotação.

**Raciocínio:** a resposta nomeia separadamente aquilo sobre o que se fará a
afirmação, o traço usado para observar o conceito e a fonte da qual o valor será
produzido. Dizer apenas “a unidade é o jornal e o indicador é o CSV” confundiria
entidade analítica, instituição e formato de arquivo.

## 1. Resultados dos experimentos

### Como acompanhar a resolução

Os experimentos não servem apenas para obter números. Em cada saída, a resolução
deve identificar: a regra aplicada, os registros incluídos, o resultado direto e
o limite da interpretação.

### Delimitação

- **Corpus A:** 6 documentos publicados entre 1890 e 1895.
- **Corpus B:** 4 editoriais em todo o período disponível.

**Resolução do Corpus A:** `between(1890, 1895)` inclui os dois limites. Permanecem
D001, D002, D003, D004, D005 e D006. A regra é temporal e não seleciona por tema,
gênero ou local.

**Resolução do Corpus B:** a condição `genero == "editorial"` mantém D001, D004,
D007 e D010. A regra é documental e cobre todo o intervalo disponível.

**Comparação:** ambos são recortes legítimos para perguntas diferentes. Corpus A
permite examinar um período; Corpus B permite examinar um gênero. O maior número
de documentos não torna automaticamente um recorte superior.

### Distribuição temática

| Tema | Coleção completa | Corpus 1890–1895 | Apenas editoriais |
|---|---:|---:|---:|
| educação | 4 | 2 | 2 |
| progresso | 4 | 2 | 2 |
| trabalho | 4 | 2 | 0 |

O equilíbrio da coleção completa não permanece no corpus de editoriais:
“trabalho” desaparece desse recorte. O resultado mostra o efeito do critério de
seleção sobre a composição analisada; não demonstra uma transformação
histórica.

**Exemplo de resolução:** primeiro conte os temas na coleção completa; depois
repita a mesma operação em cada recorte; por fim, compare coluna a coluna.
“Trabalho” vale zero entre os editoriais porque nenhum dos quatro registros
selecionados recebeu esse tema. A conclusão correta é sobre a composição do
recorte, não sobre a ausência histórica do trabalho em editoriais.

### Formatos

- `documentos_exemplo.csv`: estruturado como tabela;
- `metadados_exemplo.json`: semiestruturado, com objetos e listas;
- `texto_exemplo.txt`: texto corrido, não previamente organizado em campos.

Classificar TXT como não estruturado não significa negar sua estrutura
linguística, retórica ou documental.

**Como resolver:** observe o modo como cada arquivo organiza informação. O CSV
declara linhas e colunas; o JSON preserva pares chave–valor, listas e objetos; o
TXT guarda uma sequência textual sem campos computacionais regulares. O formato
não determina sozinho a qualidade, a historicidade ou a utilidade da fonte.

### Contagem por local

A coleção contém:

| Categoria | Documentos |
|---|---:|
| Capital | 6 |
| Interior | 6 |

A conclusão válida é restrita à coleção didática. Não é possível inferir que a
produção jornalística histórica estivesse igualmente dividida.

**Exemplo de resposta completa:** “A operação encontrou seis registros
classificados como Capital e seis como Interior na coleção didática. Esse
equilíbrio descreve apenas os dados disponíveis. Sem conhecer população,
preservação e critérios de seleção, ele não sustenta uma afirmação sobre a
produção jornalística histórica.”

### Resumo programático do Corpus A

| Campo | Resultado |
|---|---|
| nome | Documentos de 1890 a 1895 |
| número de documentos | 6 |
| primeiro ano | 1890 |
| último ano | 1895 |
| periódicos distintos | 3 |
| gêneros | carta, editorial, notícia |

**Interpretação:** a função resume características registradas no corpus. Ela não
avalia representatividade, qualidade das fontes, adequação das categorias ou
relevância histórica.

## 2. Ficha do corpus — resposta-modelo

**Universo de interesse:** Debates jornalísticos sobre educação, trabalho e
progresso em periódicos publicados entre 1890 e 1905.

**Tipo do conjunto:** Corpus didático de conveniência. Os doze registros foram
simulados para ensino, não selecionados de uma população histórica conhecida.

**Unidade de análise:** Documento jornalístico.

**Critérios de inclusão:** Registros dos três periódicos fictícios, com ano entre
1890 e 1905 e metadados mínimos de gênero, local, tema e extensão.

**Critérios de exclusão:** Registros sem identificação ou fora da cobertura
declarada. Em uma pesquisa real, critérios ligados à ilegibilidade precisariam
ser registrados, pois podem introduzir viés.

**Formatos e metadados:** CSV para registros tabulares, JSON para documentação
da coleção e TXT para exemplo de conteúdo. Seriam necessários identificador,
data, periódico, gênero, local, proveniência e ligação com o arquivo digital.

**Ausências e silêncios:** A coleção não inclui textos integrais para todos os
registros, autoria, informações sobre circulação, vozes dos leitores ou
documentos que não foram preservados. As categorias são simplificadas.

**Alcance das conclusões:** É possível demonstrar operações e comparar recortes
dentro da coleção. Não é possível produzir afirmações históricas sobre a
imprensa ou a sociedade.

**Instituições, trabalho e autoridade:** A coleção foi produzida pelo material
didático, que define campos e categorias. Em uma pesquisa real, seria necessário
registrar quem produziu as fontes, preservou, digitalizou, descreveu, anotou,
financiou e mantém a base, além de como essas posições afetam as categorias.

### Como a ficha foi construída

1. O universo foi formulado a partir do problema substantivo, não do arquivo
   disponível.
2. O conjunto foi chamado de coleção de conveniência porque não deriva de seleção
   probabilística nem pretende representar uma população conhecida.
3. A unidade de análise foi alinhada às linhas e às afirmações sobre documentos.
4. Inclusão e exclusão foram escritas como regras verificáveis.
5. Formatos foram separados dos metadados necessários à interpretação.
6. Ausências incluem tanto campos inexistentes quanto vozes e documentos que o
   processo de preservação pode ter excluído.
7. O alcance foi limitado ao que a coleção pode sustentar.
8. A ficha identificou instituições e trabalho porque os dados não surgem sem
   produção, classificação e manutenção.

### Revisão em dupla — exemplo de resolução

**Trecho inicial sobre inclusão:** “Incluir jornais relevantes para o tema.”

**Comentário do colega sobre critério impreciso:** “Relevante” não permite decidir
quais registros entram. Defina período, periódicos, gêneros, campos obrigatórios e
regra temática.

**Trecho inicial sobre ausências:** “Alguns documentos podem estar ausentes.”

**Comentário sobre silêncio pouco discutido:** especifique se faltam textos
integrais, autoria, circulação, grupos sociais, períodos ou documentos não
preservados e explique como isso afeta a pergunta.

**Trecho inicial sobre alcance:** “O corpus mostrará como a imprensa brasileira
discutia progresso.”

**Comentário sobre extrapolação:** doze registros fictícios não representam a
imprensa brasileira. A conclusão deve permanecer na coleção e na demonstração
metodológica.

**Revisão registrada:** substituir os trechos vagos pelos critérios, ausências e
alcance apresentados na ficha-modelo acima.

**Justificativa da mudança:** os novos enunciados são auditáveis e distinguem
universo de interesse, conjunto disponível e alcance efetivo da evidência.

## 3. Critérios de correção

Uma ficha adequada:

- distingue universo de interesse do conjunto disponível;
- nomeia corretamente a unidade de análise;
- explicita critérios de inclusão e exclusão;
- identifica formatos e metadados relevantes;
- reconhece ausências, cobertura e processos de seleção;
- identifica instituições, trabalho e autoridade classificatória;
- limita as conclusões ao conjunto que pode sustentá-las.

### Exemplo de devolutiva

> A unidade, os formatos e o alcance estão bem definidos. Transforme “fontes
> relevantes” em critérios verificáveis e acrescente como a ausência de textos
> integrais afeta a possibilidade de interpretar os temas atribuídos. Identifique
> também quem realizou a anotação temática.
