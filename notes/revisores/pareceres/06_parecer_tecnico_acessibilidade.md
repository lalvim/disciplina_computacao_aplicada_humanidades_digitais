# Parecer — Técnica e acessibilidade

## Identificação

**Dimensão:** execução, reprodutibilidade, usabilidade e acesso  
**Versão:** commit `4e89d70` com alterações locais  
**Data:** 30 de julho de 2026  
**Ambiente:** Python 3.10.12, validação local  
**Decisão:** **aprovada com ajustes**

## Testes executados

```text
python3 scripts/validar_unidade_01.py
git diff --check
```

Resultado:

- 5 notebooks válidos;
- 60 células Markdown e 12 de código;
- todas as células de código executadas;
- 18 questões HTML correspondentes ao gabarito;
- dados locais encontrados por caminhos relativos;
- gabaritos e perfis de revisão presentes.

## Pontos fortes

1. O HTML é autocontido e não envia dados.
2. O quiz possui rótulos, foco visível, estado anunciado e redução de movimento.
3. Os dados fictícios estão identificados.
4. O validador compara o gabarito com a chave do HTML.
5. O código dos notebooks funciona offline.

## Achados

### TA-001 — Dependências sem versão

**Gravidade:** média.  
**Local:** `requirements.txt`.  
**Evidência:** `jupyterlab` e `pandas` não possuem limites de versão.  
**Consequência:** futuras versões podem alterar comportamento ou instalação.  
**Ação:** adotar faixas compatíveis ou ambiente bloqueado e documentar a versão
testada.

### TA-002 — HTML depende totalmente de JavaScript sem aviso alternativo

**Gravidade:** média.  
**Local:** `exercicios_unidade_01.html`.  
**Evidência:** perguntas são renderizadas por JavaScript; sem ele, o painel fica
sem conteúdo.  
**Ação:** incluir `<noscript>` com instrução e link para versão textual das
questões ou disponibilizar alternativa acessível.

### TA-003 — Acessibilidade não foi testada com tecnologia assistiva

**Gravidade:** média.  
**Local:** exercício HTML e notebooks.  
**Evidência:** há boas propriedades estruturais, mas somente inspeção de código.  
**Ação:** testar ao menos com leitor de tela e navegação exclusiva por teclado;
registrar navegador e resultado.

### TA-004 — Reconstrução não inclui todos os artefatos

**Gravidade:** média.  
**Local:** `scripts/construir_unidade_01.py`.  
**Evidência:** o script gera notebooks, dados e README, mas não recria HTML,
gabaritos, revisores e pareceres.  
**Consequência:** o nome e a mensagem do script podem sugerir reconstrução
integral.  
**Ação:** delimitar claramente o escopo do gerador ou incorporar os artefatos a
uma fonte reproduzível.

### TA-005 — Validação de cobertura pode induzir interpretação excessiva

**Gravidade:** baixa.  
**Local:** `scripts/validar_unidade_01.py`.  
**Evidência:** procura termos e imprime “9/9 tópicos da ementa”.  
**Ação:** imprimir “presença textual 9/9” e remeter à matriz humana.

## Segurança e privacidade

Não há coleta ou transmissão. O README dos gabaritos explica corretamente que
separação de pasta não produz sigilo. Para avaliação somativa com respostas
ocultas, seria necessário servidor autenticado.

## Condições para aprovação plena

1. resolver TA-002;
2. documentar ambiente reproduzível;
3. executar teste manual de acessibilidade;
4. esclarecer o escopo do gerador.

