# Exemplo de entrega cumulativa

Esta pasta contém somente um exemplo preenchido. Seu objetivo é mostrar ao aluno
como um mesmo projeto pode evoluir de forma cumulativa ao longo da disciplina,
sem criar uma coleção paralela de modelos que possa ser confundida com as oficinas
das unidades.

## Notebooks disponíveis

**[`EXEMPLO_PREENCHIDO_projeto_integrador_U01_a_U14.ipynb`](EXEMPLO_PREENCHIDO_projeto_integrador_U01_a_U14.ipynb)**

O arquivo reúne o percurso completo do projeto fictício
`PI-EXEMPLO-IMPRENSA`, da proposta inicial da U01 ao fechamento da U14.
Ele está salvo com as células executadas, de modo que tabelas e gráficos possam ser
vistos sem uma nova execução. No Colab ou no Jupyter, o estudante também pode usar
“Executar tudo” para reconstruir as saídas.

**[`EXEMPLO_PREENCHIDO_IBGE_DADOS_FICTICIOS_U01_a_U14.ipynb`](EXEMPLO_PREENCHIDO_IBGE_DADOS_FICTICIOS_U01_a_U14.ipynb)**

O segundo arquivo apresenta um projeto municipal inspirado na estrutura de dados
do IBGE. Municípios, códigos e valores são inteiramente fictícios. O exemplo permite
ensinar preparação de painel, exploração, comparação pareada, regressão descritiva
e análise temporal antes de uma futura substituição por dados oficiais documentados.

## Diferença essencial

| Oficina | Entrega cumulativa |
|---|---|
| ensina e permite experimentar | registra uma versão do projeto integrador |
| pode usar dados didáticos | usa o corpus-base do projeto ou documenta uma contingência |
| produz exercícios e resultados provisórios | seleciona evidências, interpreta e aponta arquivos técnicos |
| avalia a aprendizagem da unidade | demonstra continuidade entre as unidades |

A entrega pode e deve reunir **código conciso, tabelas, gráficos e análise** quando
esses elementos sustentarem o argumento. Preparações extensas, testes auxiliares e
experimentos descartados podem permanecer em notebooks técnicos complementares,
desde que sejam indicados na entrega.

O exemplo adota a sequência recomendada:

1. texto que apresenta a pergunta da análise;
2. código executável;
3. tabela ou gráfico produzido;
4. interpretação do resultado;
5. explicitação dos limites da evidência.

## Projeto utilizado no exemplo

Cada exemplo acompanha a mesma pergunta e o mesmo corpus versionado da U01 à U14.
Nas unidades condicionais, eles apresentam tanto métodos incorporados quanto decisões
fundamentadas de não adoção.

As demonstrações executáveis aparecem nas etapas em que são metodologicamente
necessárias: construção e verificação da base (U03), exploração e visualização
(U04), comparação e sensibilidade (U05) e análise temporal (U11).

Todos os dados e resultados dos dois exemplos são inventados para fins didáticos. Eles mostram a
lógica e o nível de detalhe esperados, mas não devem ser copiados nem interpretados
como evidência histórica.

## Como usar

1. leia no exemplo somente a etapa correspondente à unidade atual;
2. identifique o que essa etapa herdou e o que preparou para a seguinte;
3. adapte a lógica ao seu projeto, sem copiar dados, resultados ou justificativas;
4. indique os arquivos técnicos que sustentam sua entrega;
5. registre toda mudança de pergunta, corpus, categoria ou método.

O exemplo é reconstruído por `scripts/construir_trilha_de_trabalhos.py`.
