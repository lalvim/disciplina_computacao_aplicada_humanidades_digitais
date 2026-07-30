# Segunda revisão — Técnica e acessibilidade

**Decisão:** aprovada com ajustes.

## Achados da Rodada 1

| Achado | Situação | Evidência |
|---|---|---|
| TA-001 — dependências sem versão | Resolvido | faixas em `requirements.txt` |
| TA-002 — ausência sem JavaScript | Resolvido | `<noscript>` e versão Markdown |
| TA-003 — teste assistivo | Pendente | requer tecnologia assistiva real |
| TA-004 — escopo do gerador | Resolvido | docstring e mensagem delimitam artefatos |
| TA-005 — mensagem de cobertura | Resolvido | “presença textual” |

## Testes

- notebooks executados em sequência;
- 18 questões verificadas no HTML e na versão textual;
- bibliografia e citações verificadas estruturalmente;
- gabaritos e pareceres presentes;
- `git diff --check` sem erros.

## Ajuste restante

**TA2-001 — Teste com leitor de tela**  
**Gravidade:** média.  
Realizar teste manual com NVDA, Orca ou VoiceOver antes da distribuição pública
e registrar navegador, sistema e barreiras encontradas.

