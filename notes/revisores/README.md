# Revisão acadêmica e didática da Unidade 1

Esta pasta define uma banca de revisão para avaliar a Unidade 1 antes de sua
publicação ou aplicação em sala. Os revisores possuem focos distintos, mas usam
a mesma escala, o mesmo padrão de evidência e um parecer consolidado.

## Objetivo

Verificar se a unidade:

- possui profundidade apropriada a uma disciplina de mestrado;
- apresenta progressão didática clara;
- está alinhada à ementa, aos objetivos e ao produto previsto;
- pertence efetivamente ao campo das Humanidades Digitais;
- utiliza referências acadêmicas adequadas e verificáveis;
- articula código, interpretação e crítica metodológica;
- é tecnicamente reproduzível e acessível;
- trata limites, vieses e ética com seriedade.

## Arquivos

| Arquivo | Responsabilidade |
|---|---|
| `00_coordenacao_da_revisao.md` | Organizar a banca e consolidar os pareceres |
| `01_revisor_nivel_academico.md` | Avaliar profundidade e adequação ao mestrado |
| `02_revisor_didatica.md` | Avaliar aprendizagem, progressão e atividades |
| `03_revisor_alinhamento.md` | Conferir aderência à proposta da disciplina |
| `04_revisor_humanidades_digitais.md` | Avaliar enquadramento no campo |
| `05_revisor_referencias.md` | Avaliar bibliografia, citações e verificabilidade |
| `06_revisor_tecnico_acessibilidade.md` | Avaliar execução, usabilidade e acessibilidade |
| `matriz_de_avaliacao.md` | Reunir critérios e decisão de publicação |
| `modelo_de_parecer.md` | Padronizar a entrega de cada revisão |

Os pareceres já executados ficam em `pareceres/`. O arquivo
`pareceres/parecer_consolidado.md` registra a decisão da rodada atual.

## Materiais que devem ser lidos

Todos os revisores devem consultar:

1. `notes/contexto_disciplina.md`;
2. `notes/plano_unidade_01.md`;
3. `notes/diretrizes_formatacao_material.md`;
4. `unidade_01/README.md`;
5. os cinco notebooks;
6. `unidade_01/exercicios_unidade_01_texto.md`;
7. os gabaritos relacionados ao seu foco.

O revisor não deve avaliar apenas arquivos isolados. A unidade deve ser
examinada como percurso.

## Escala de gravidade

### Bloqueante

Problema que impede a publicação ou aplicação:

- erro conceitual central;
- conteúdo incompatível com a ementa;
- ausência de referências acadêmicas;
- material que não executa;
- risco ético grave;
- atividade cuja resposta ou avaliação seja incoerente.

### Alta

Problema que compromete significativamente aprendizagem, validade ou rigor:

- conceito importante superficial;
- salto didático;
- operação sem interpretação;
- afirmação acadêmica sem sustentação;
- cobertura insuficiente de objetivo central.

### Média

Problema localizado que reduz clareza ou consistência, mas permite uso com
ajustes:

- exemplo pouco desenvolvido;
- instrução ambígua;
- exercício desalinhado parcialmente;
- referência complementar ausente.

### Baixa

Melhoria editorial ou refinamento:

- título pouco informativo;
- repetição;
- pequeno problema de formatação;
- sugestão de exemplo adicional.

## Tipos de decisão

- **Aprovada:** nenhum achado bloqueante ou alto; ajustes médios não impedem uso.
- **Aprovada com ajustes:** nenhum bloqueante, mas há achados altos ou vários
  médios que precisam ser tratados antes da oferta.
- **Revisão obrigatória:** existe ao menos um achado bloqueante.

## Evidência obrigatória

Todo achado deve indicar:

- arquivo;
- seção, título da célula ou número da questão;
- trecho ou descrição verificável;
- critério violado;
- consequência;
- recomendação concreta.

Exemplo:

> **Local:** `03_dados_corpus_e_evidencias.ipynb` > “Evidência computacional”.
> **Problema:** a interpretação é apresentada sem leitura recomendada.
> **Gravidade:** alta.
> **Ação:** incluir referência metodológica e duas perguntas de discussão.

Não usar avaliações vagas como “está superficial” sem demonstrar onde, por que
e com qual consequência.

## Independência

Cada especialista deve produzir seu parecer antes de ler o parecer dos demais.
Discordâncias devem ser preservadas no relatório consolidado. O coordenador não
deve transformar diversidade de avaliação em unanimidade artificial.
