# Parecer — Nível acadêmico

## Identificação

**Dimensão:** adequação ao mestrado  
**Versão:** commit `4e89d70` com alterações locais  
**Data:** 30 de julho de 2026  
**Decisão:** **revisão obrigatória**

## Síntese

A unidade possui um bom desenho metodológico e evita apresentar computação como
substituta da interpretação. A progressão entre pergunta, operacionalização,
corpus e evidência é apropriada à formação de pesquisadores.

No estado atual, porém, o conteúdo funciona mais como uma introdução conceitual
bem construída do que como uma unidade de mestrado plenamente sustentada. Não
há leituras acadêmicas, citações ou controvérsias autorais. Conceitos importantes
são apresentados como sínteses corretas, mas sem inserir o estudante em debates
do campo.

## Pontos fortes

1. `01_perguntas_e_problemas_computacionais.ipynb` distingue pergunta
   humanística, pergunta delimitada e tarefa computacional.
2. `02_representacao_e_operacionalizacao.ipynb` compara indicadores alternativos
   e explicita perdas de representação.
3. `04_oficina_projeto_de_pesquisa.ipynb` exige cadeia de evidência, limitações e
   retorno qualitativo, superando o preenchimento meramente burocrático.

## Achados

### NA-001 — Ausência de literatura acadêmica

**Gravidade:** bloqueante.  
**Local:** todos os notebooks.  
**Evidência:** não existem seções de referências, leituras obrigatórias ou
citações autor-data.  
**Consequência:** o estudante não consegue localizar tradições, autores,
controvérsias ou fundamentos das definições.  
**Ação:** incluir leituras essenciais e complementares, citações locais e
questões que coloquem ao menos duas posições em comparação.

### NA-002 — Controvérsias aparecem como conclusões prontas

**Gravidade:** alta.  
**Local:** Notebook 01, “Humanidades Digitais e pesquisa orientada por dados”;
Notebook 03, “Evidência computacional e interpretação humanística”.  
**Evidência:** afirmações como “dados não são o fenômeno em estado puro” são
adequadas, mas não aparecem vinculadas a autores ou posições alternativas.  
**Consequência:** a crítica vira princípio a memorizar, em vez de debate
epistemológico a examinar.  
**Ação:** introduzir a discussão entre dados como dados, *capta* e dados
situados, com leitura e comparação argumentativa.

### NA-003 — Distinções lógicas precisam de casos limítrofes

**Gravidade:** média.  
**Local:** Notebook 01, “Cinco tipos de pergunta”.  
**Evidência:** os exemplos são claros, mas cada pergunta recebe um tipo
predominante sem discutir desenhos híbridos.  
**Consequência:** estudantes podem tratar a tipologia como classificação rígida.  
**Ação:** acrescentar dois casos ambíguos e solicitar que o estudante justifique
tipo predominante, etapas secundárias e mudança de desenho.

### NA-004 — O produto precisa exigir diálogo bibliográfico

**Gravidade:** alta.  
**Local:** Notebook 04, “Minha entrega”.  
**Evidência:** a síntese exige pergunta, corpus, indicador e limites, mas não
exige conceito fundamentado em literatura.  
**Consequência:** um projeto formalmente coerente pode permanecer teoricamente
frágil.  
**Ação:** acrescentar “conceito e autores de referência” e exigir ao menos duas
leituras pertinentes à formulação.

## Julgamento de nível

O raciocínio exigido é potencialmente adequado ao mestrado, sobretudo na
comparação de operacionalizações e na cadeia de evidência. O nível não decorre
da complexidade do Python, mas da densidade teórica e da justificativa
metodológica. Essa densidade ainda precisa ser incorporada por literatura,
controvérsias e diálogo bibliográfico.

## Condições para aprovação

1. resolver NA-001;
2. resolver NA-002 e NA-004;
3. revisar a carga após inserir leituras;
4. submeter a nova versão ao mesmo revisor.

