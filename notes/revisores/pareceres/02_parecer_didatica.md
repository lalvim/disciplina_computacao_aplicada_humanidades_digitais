# Parecer — Didática

## Identificação

**Dimensão:** aprendizagem, progressão e atividades  
**Versão:** commit `4e89d70` com alterações locais  
**Data:** 30 de julho de 2026  
**Decisão:** **aprovada com ajustes**

## Síntese

O percurso possui boa progressão: orientação, tipologia de perguntas,
operacionalização, corpus e oficina integrada. A regra “Markdown para pensar;
Python para experimentar” está bem aplicada. Os gabaritos distinguem resposta
objetiva de resposta-modelo.

O principal risco didático é a carga. Cinco notebooks, 18 questões, produtos
parciais, revisão entre pares e projeto final são ambiciosos para oito horas,
especialmente com estudantes sem Python. Falta distinguir atividades de sala,
preparação e aprofundamento.

## Pontos fortes

1. Os notebooks usam estrutura recorrente e linguagem clara.
2. O Notebook 03 permite observar como critérios alteram o corpus.
3. O Notebook 04 não transforma argumentação em formulário Python.
4. O HTML fornece explicações, não apenas certo ou errado.

## Perfis de estudante

### Sem experiência em Python

**Dificuldade provável:** `DataFrame`, filtragem booleana, `value_counts` e
leitura de formatos aparecem em sequência.  
**Apoio existente:** código pronto e dados pequenos.  
**Apoio ausente:** explicação mínima da anatomia das expressões.  
**Ação:** inserir caixas “Como ler esta célula”, sem transformar a unidade em
curso de sintaxe.

### Com programação, sem Humanidades Digitais

**Dificuldade provável:** interpretar limites substantivos e resistir à ideia de
que a saída resolve a pergunta.  
**Apoio existente:** perguntas de alcance e retorno qualitativo.  
**Apoio ausente:** estudo real publicado que mostre essa integração.  
**Ação:** incluir um caso de pesquisa com fonte bibliográfica.

### Das Humanidades, com projeto amplo

**Dificuldade provável:** reduzir escopo sem reduzir relevância.  
**Apoio existente:** reformulação em níveis e oficina.  
**Apoio ausente:** exemplo de pergunta recusada e revisada após feedback.  
**Ação:** incluir uma trajetória de revisão com comentários.

## Achados

### DI-001 — Carga não priorizada

**Gravidade:** alta.  
**Local:** plano de oito horas e conjunto completo de materiais.  
**Evidência:** 60 células Markdown, 12 de código, 18 questões e oficina extensa.  
**Consequência:** risco de acelerar conceitos ou transformar a oficina em tarefa
extraclasse não declarada.  
**Ação:** marcar cada item como essencial em aula, preparação ou aprofundamento;
atribuir tempo; reduzir o quiz em aula ou usá-lo como revisão assíncrona.

### DI-002 — Código pronto sem apoio de leitura sintática

**Gravidade:** média.  
**Local:** Notebooks 01 a 03.  
**Evidência:** `DataFrame`, filtros, `between`, `value_counts`, `fillna` e
`astype` são executados sem explicação sistemática.  
**Consequência:** estudantes iniciantes podem executar sem compreender o que
mudou.  
**Ação:** incluir explicação curta antes de cada nova construção e uma pergunta
de previsão da saída.

### DI-003 — Pouca recuperação ativa antes do quiz final

**Gravidade:** média.  
**Local:** transições entre Notebooks 01, 02 e 03.  
**Evidência:** há sínteses, mas poucas perguntas curtas de retomada.  
**Ação:** iniciar cada notebook com duas perguntas de recuperação do anterior.

### DI-004 — Diagnóstico sem regra de uso docente

**Gravidade:** baixa.  
**Local:** Notebook 00, “Diagnóstico inicial”.  
**Evidência:** coleta experiência e dúvida, mas não informa como adaptar o
percurso.  
**Ação:** acrescentar ao gabarito docente uma tabela de adaptações.

## Mapa resumido

| Objetivo | Ensino | Prática | Feedback |
|---|---|---|---|
| Tipos de pergunta | Notebook 01 | classificação | gabarito 01 |
| Operacionalização | Notebook 02 | mapa | gabarito 02 |
| Corpus e formatos | Notebook 03 | filtros e leitura | gabarito 03 |
| Evidência e limites | Notebooks 03–04 | cadeia de evidência | gabarito 04 |
| Projeto inicial | Notebook 04 | entrega | rubrica |

## Condições para aprovação plena

1. resolver DI-001;
2. inserir apoio mínimo para leitura do código;
3. reestimar o cronograma após adicionar bibliografia.

