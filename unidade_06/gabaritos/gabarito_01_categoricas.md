# U06-A02 — Gabarito — associação categórica

## Exemplo de resolução

Cruza-se `local` com `tem_ilustracao`. O denominador é o total de documentos de cada local, porque a pergunta compara a proporção ilustrada dentro de Capital e Interior. Exibem-se contagens, porcentagens por linha, esperados e V de Cramér. Quatro registros — dois por combinação contrastante — são inspecionados.

### Procedimento

1. confirme que cada linha representa um documento;
2. use `pd.crosstab` para as frequências observadas;
3. repita com `normalize="index"` e multiplique por 100;
4. calcule esperados a partir dos totais marginais;
5. calcule V e verifique células pequenas;
6. abra os quatro documentos e confira a codificação.

**Resposta-modelo:** “A proporção difere no corpus fictício, mas V resume apenas associação. Período e gênero podem compor a diferença; não concluímos que o local cause ilustração.”

## Erros frequentes

Misturar denominadores; interpretar V como causalidade; omitir células raras.
