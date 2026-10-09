"""Constrói os cadernos de entrega cumulativa do projeto integrador."""

from __future__ import annotations

import json
from pathlib import Path
from textwrap import dedent


RAIZ = Path(__file__).resolve().parents[1]
PASTA = RAIZ / "notes" / "trilha_de_trabalhos" / "exemplo_de_entrega"


def md(texto: str) -> dict:
    return {
        "cell_type": "markdown",
        "metadata": {},
        "source": dedent(texto).strip().splitlines(keepends=True),
    }


def codigo(texto: str) -> dict:
    return {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": dedent(texto).strip().splitlines(keepends=True),
    }


def salvar(nome: str, celulas: list[dict]) -> None:
    caminho = PASTA / nome
    if caminho.exists():
        anterior = json.loads(caminho.read_text(encoding="utf-8"))
        codigos_anteriores = [
            c for c in anterior.get("cells", []) if c.get("cell_type") == "code"
        ]
        codigos_novos = [c for c in celulas if c.get("cell_type") == "code"]
        fontes_anteriores = ["".join(c.get("source", [])) for c in codigos_anteriores]
        fontes_novas = ["".join(c.get("source", [])) for c in codigos_novos]
        if fontes_anteriores == fontes_novas:
            for nova, antiga in zip(codigos_novos, codigos_anteriores):
                nova["execution_count"] = antiga.get("execution_count")
                nova["outputs"] = antiga.get("outputs", [])

    doc = {
        "cells": celulas,
        "metadata": {
            "kernelspec": {
                "display_name": "Python 3",
                "language": "python",
                "name": "python3",
            },
            "language_info": {"name": "python", "version": "3"},
        },
        "nbformat": 4,
        "nbformat_minor": 5,
    }
    caminho.write_text(
        json.dumps(doc, ensure_ascii=False, indent=1) + "\n",
        encoding="utf-8",
    )


EXEMPLOS = {
    1: """
    **ID:** `PI-EXEMPLO-IMPRENSA` — versão `v0.1-proposta`.

    **Problema:** compreender como um corpus didático de periódicos operários
    fictícios representa a relação entre educação e trabalho entre 1890 e 1910.

    **Pergunta delimitada:** como a centralidade atribuída à educação e sua associação
    discursiva com trabalho variam entre 1890–1899 e 1900–1910?

    **Unidade:** artigo. **Corpus pretendido:** cerca de 300 artigos de quatro
    periódicos fictícios, com imagem, transcrição, data, periódico e gênero.

    **Operacionalização inicial:** “centralidade da educação” será observada por
    anotação humana (`central`, `secundária`, `ausente`) e por frequência relativa de
    vocabulário educacional. As duas medidas não são equivalentes.

    **Limite:** o corpus é de conveniência e não representa toda a imprensa ou todas
    as organizações do período.

    **Passagem:** a U02 deverá verificar acesso, cobertura, direitos, qualidade das
    imagens e viabilidade da anotação.
    """,
    2: """
    **Versão herdada:** `v0.1-proposta`; pergunta mantida, corpus pretendido revisado.

    **Fontes:** 268 imagens sintéticas atribuídas aos periódicos A–D. Após o piloto,
    definiu-se incluir artigos com data e periódico identificáveis e excluir anúncios,
    páginas repetidas e imagens sem legibilidade mínima.

    **Corpus previsto:** 252 artigos; 16 imagens ficam no registro de exclusões.
    A cobertura é maior depois de 1900 e o periódico D só aparece no segundo período.

    **Identificador:** `PER-A-1894-003`; nunca será derivado apenas do título.
    **Campos:** ID, periódico, data, gênero, página, caminho da imagem, transcrição,
    precisão da data, motivo de exclusão e proveniência.

    **Governança:** corpus inteiramente fictício e compartilhável; o protocolo seria
    diferente com pessoas vivas ou acervo restrito.

    **Decisão:** prosseguir, mas tratar desequilíbrio temporal e institucional como
    limite, não como ausência neutra.
    """,
    3: """
    **Entrada:** 252 registros previstos na U02, imagens e metadados preservados em
    `dados/brutos/`.

    **Transformações:** datas foram normalizadas sem apagar o valor recebido;
    gêneros receberam vocabulário controlado; transcrições mantiveram vínculo com a
    imagem; 12 artigos foram marcados como não processáveis segundo regra já prevista.

    **Base processável:** `corpus-v1`, com 240 artigos, uma linha por artigo. As 12
    exclusões permanecem em `registro_exclusoes.csv`.

    **Testes:** 240 IDs únicos; nenhuma junção multiplicou artigos; todos os caminhos
    de transcrição apontam para um arquivo; 18 datas possuem apenas precisão anual.

    **Parecer:** a base permite exploração por período, periódico, gênero e texto,
    mas comparações devem considerar a cobertura desigual e erros de OCR ainda não
    corrigidos em parte das transcrições.
    """,
    4: """
    **Base herdada:** `corpus-v1`, 240 artigos.

    **Pergunta exploratória:** que padrões temporais e textuais justificam uma
    comparação mais controlada entre os dois períodos?

    **Resultado quantitativo fictício:** 24% dos 110 artigos de 1890–1899 e 38% dos
    130 artigos de 1900–1910 foram anotados como educação central. O denominador é o
    número de artigos de cada período.

    **Resultado textual fictício:** a frequência do vocabulário educacional passou de
    8,2 para 12,7 ocorrências por mil tokens. Concordâncias mostraram que “instrução”
    aparece tanto em defesa da educação quanto em críticas institucionais.

    **Retorno aos casos:** um artigo longo elevava a contagem bruta; a frequência
    relativa reduziu, mas não eliminou, sua influência.

    **Hipótese:** no corpus, a educação parece tornar-se mais central no segundo
    período, mas a mudança pode decorrer da composição dos periódicos disponíveis.
    """,
    5: """
    **Contraste herdado:** 1890–1899 (`n=110`) versus 1900–1910 (`n=130`).

    **Medida principal fictícia:** diferença de 14 pontos percentuais na proporção de
    artigos anotados como educação central (`0,38 - 0,24`).

    **Sensibilidade:** ao comparar apenas periódicos presentes nos dois períodos, a
    diferença cai para 11 pontos percentuais. A direção permanece, mas a magnitude
    depende da composição institucional.

    **Casos:** um artigo típico de cada período, um texto extremo em extensão e um
    artigo do segundo período que critica a escolarização qualificaram a leitura.

    **Conclusão limitada:** há diferença descritiva neste corpus; ela não demonstra
    mudança de toda a imprensa operária nem efeito causal do período.

    **Diagnóstico:** classificação e análise temporal parecem aplicáveis; regressão
    explicativa e análise espacial não parecem justificadas nesta versão.
    """,
    6: """
    **Decisão:** Forma A, método complementar — rede de coocorrência entre
    instituições e conceitos, alimentada posteriormente pela extração da U10.

    **Regra:** duas entidades recebem uma aresta quando aparecem no mesmo artigo; o
    peso é o número de artigos compartilhados, não a intensidade de uma relação social.

    **Resultado fictício:** associações educacionais e sindicatos aparecem próximos
    de “curso” e “biblioteca”, mas a inspeção mostrou que parte das coocorrências vem
    de listas de eventos.

    **Limite:** centralidade na rede textual não equivale a importância histórica.
    A dependência da U10 foi registrada como inversão da ordem operacional.
    """,
    7: """
    **Decisão:** Forma B — não incorporar regressão ao projeto.

    **Diagnóstico:** seria possível modelar a anotação “educação central”, mas o
    corpus é de conveniência, possui forte desequilíbrio entre periódicos e só 240
    casos. Um modelo multivariado criaria aparência de explicação sem desenho capaz
    de sustentar causalidade.

    **Laboratório:** a regressão foi executada nos dados didáticos da oficina para
    aprender coeficientes, categorias de referência e resíduos.

    **Alternativa:** manter a comparação estratificada por periódicos e realizar
    análise de sensibilidade. O resultado do laboratório não integra a evidência do
    projeto `PI-EXEMPLO-IMPRENSA`.
    """,
    8: """
    **Decisão:** Forma A — classificação como método principal.

    **Categoria-alvo:** educação `central` versus `não central`, definida em guia de
    anotação. Dois anotadores revisaram 40 casos; divergências foram discutidas antes
    da anotação final de 120 artigos.

    **Experimento fictício:** baseline majoritária com F1 macro 0,41; regressão
    logística com TF-IDF, F1 macro 0,68 no teste preservado.

    **Erros:** referências indiretas a ensino foram frequentemente omitidas; textos
    com listas de escolas produziram falsos positivos.

    **Decisão de uso:** o protótipo pode priorizar revisão humana, mas não substituir
    a anotação nem produzir automaticamente categorias históricas definitivas.
    """,
    9: """
    **Decisão:** Forma B após piloto — não incorporar agrupamento ou tópicos.

    **Piloto fictício:** soluções com quatro e cinco tópicos mudaram muito entre
    sementes; dois tópicos refletiam tamanho e ruído de OCR, não temas interpretáveis.

    **Risco:** nomear os grupos como correntes políticas daria substância histórica a
    uma separação instável produzida pela representação.

    **Aprendizagem:** o laboratório mostrou a necessidade de avaliar estabilidade e
    ler documentos típicos e limítrofes.

    **Alternativa:** manter a categoria anotada na U08 e usar concordâncias para
    investigar vocabulário sem afirmar descoberta automática de temas.
    """,
    10: """
    **Decisão:** Forma A — extrair associações, sindicatos, escolas e localidades
    mencionadas para apoiar a rede da U06.

    **Esquema:** entidade, forma textual, tipo, ID do artigo, trecho, posição e ID
    normalizado. A extração preserva cada menção, não apenas contagens agregadas.

    **Avaliação fictícia em 60 artigos:** precisão 0,88 e revocação 0,76. Nomes
    abreviados de associações foram a principal fonte de omissão; escolas com nomes
    semelhantes exigiram desambiguação humana.

    **Produto:** `entidades-v1.csv`, ligado por `id_artigo` e acompanhado de uma fila
    de casos ambíguos. A base derivada não substitui os textos.
    """,
    11: """
    **Decisão:** Forma A para o percurso temporal; Forma B para o espacial.

    **Temporal:** proporção anual de artigos anotados como educação central, mostrada
    apenas em anos com cobertura mínima declarada. Anos com poucos artigos aparecem
    como pontos, sem linha contínua que sugira cobertura inexistente.

    **Resultado fictício:** o aumento não é monotônico e se concentra em três anos;
    isso enfraquece uma narrativa simples de crescimento contínuo.

    **Espacial não adotado:** o local do periódico registra impressão, não o lugar do
    evento ou o alcance da circulação. Um mapa confundiria unidades diferentes.
    """,
    12: """
    **Decisão:** Forma B após experimento controlado.

    **Tarefa:** extrair organizações nos mesmos 40 artigos usados para avaliar a regra
    e o modelo da U10.

    **Resultado fictício:** o modelo de linguagem obteve F1 0,78, contra 0,80 da
    abordagem de referência revisada; variou entre execuções e inventou uma expansão
    para duas siglas ambíguas.

    **Decisão de não uso:** não houve ganho suficiente para compensar menor
    rastreabilidade e custo. As instruções e saídas foram preservadas como experimento,
    mas não alimentam a base final.
    """,
    13: """
    **Afirmação auditada:** a educação é mais central no segundo período deste corpus.

    **Construto:** frequência lexical e anotação humana capturam dimensões diferentes;
    a conclusão final não as trata como equivalentes.

    **Sensibilidade:** a diferença anotada passa de 14 para 11 pontos percentuais ao
    restringir a comparação aos periódicos comuns. Com uma regra de anotação mais
    estrita, cai para 8 pontos.

    **Erros:** OCR afeta sobretudo artigos do primeiro período; o classificador erra
    referências indiretas; a rede super-representa listas de eventos.

    **Conclusão revisada:** o corpus oferece evidência de uma diferença interna e
    sensível à composição, não de uma transformação geral da imprensa do período.
    """,
    14: """
    **Versão:** `v1.0-final`; corpus congelado `corpus-v1.2`.

    **Narrativa:** a pergunta da U01 foi preservada, mas o corpus caiu de 300 artigos
    pretendidos para 240 processáveis. A U04 formulou a hipótese temporal, a U05
    mostrou sensibilidade à composição, a U08 ofereceu classificação assistida e a
    U10 sustentou a rede da U06. Regressão, tópicos, mapa e modelo de linguagem foram
    recusados com justificativa.

    **Resultado central:** diferença descritiva na centralidade da educação entre os
    períodos, qualificada por cobertura, periódicos e regras de anotação.

    **Pacote:** README, corpus compartilhável fictício, dicionário, notebooks,
    ambiente, tabelas, figuras, testes, manifesto e registro de mudanças.

    **Próximo passo:** ampliar cobertura do primeiro período e revisar OCR antes de
    qualquer argumento histórico mais amplo.
    """,
}


def exemplo(unidade: int) -> dict:
    return md(f"""
    ## Exemplo orientador preenchido — projeto fictício

    > **Atenção:** este exemplo é inteiramente fictício, usa números inventados para
    > fins didáticos e não representa uma pesquisa histórica real. Ele acompanha o
    > mesmo projeto `PI-EXEMPLO-IMPRENSA` ao longo das 14 unidades. Use-o para
    > compreender o nível de detalhe; não copie suas respostas.

    {EXEMPLOS[unidade]}
    """)


TITULOS_EXEMPLO = {
    1: "Proposta inicial",
    2: "Protocolo da base",
    3: "Primeira base processável",
    4: "Relatório exploratório",
    5: "Análise comparativa",
    6: "Associação ou rede",
    7: "Regressão",
    8: "Classificação",
    9: "Agrupamento ou tópicos",
    10: "Extração de informações",
    11: "Tempo ou espaço",
    12: "Modelos de linguagem",
    13: "Validade e robustez",
    14: "Projeto final",
}


EXEMPLOS_IBGE = {
    1: """
    **ID:** `PI-EXEMPLO-IBGE-SINTETICO` — versão `v0.1-proposta`.

    **Problema:** investigar desigualdades municipais de alfabetização e sua relação
    com urbanização entre dois momentos censitários.

    **Pergunta delimitada:** como a taxa de alfabetização varia entre 2010 e 2022
    nos municípios do corpus simulado, e como essa variação se relaciona com a
    urbanização inicial e com as grandes regiões?

    **Unidade:** município-ano. **Corpus pretendido:** indicadores de 60 municípios
    fictícios observados em 2010 e 2022.

    **Cuidado:** a pergunta é descritiva e associativa. Ela não permite afirmar que
    a urbanização cause mudanças na alfabetização.
    """,
    2: """
    **Fonte de referência:** estrutura inspirada em tabelas municipais disponibilizadas
    pelo IBGE/SIDRA. Nesta demonstração, porém, nenhum valor foi coletado do IBGE.

    **População conceitual:** municípios brasileiros nos dois anos. **Corpus
    didático:** 60 municípios inventados, doze por grande região, com duas
    observações por município.

    **Campos planejados:** código municipal fictício, nome fictício, região, ano,
    população, urbanização, alfabetização e renda domiciliar per capita.

    **Proveniência:** o gerador, a semente aleatória e as regras de simulação ficam
    no notebook. Uma pesquisa real registraria tabela SIDRA, código da variável,
    unidade, classificação, data de acesso e notas metodológicas.
    """,
    3: """
    **Estrutura:** base em formato longo, com uma linha por município-ano e chave
    composta por `codigo_municipio` e `ano`.

    **Transformações previstas:** validar chaves, tipos e intervalos; preservar os
    códigos como texto; conferir duas observações por município; manter percentuais
    em escala de 0 a 100.

    **Produto:** `painel_municipal_sintetico-v1`, com 120 linhas e dicionário de
    dados. Os nomes “Município fictício 001” etc. impedem associação com localidades
    reais.
    """,
    4: """
    **Exploração:** comparar centro, dispersão e distribuição das taxas por ano;
    observar a relação entre urbanização e alfabetização; conferir diferenças de
    cobertura antes de interpretar padrões.

    **Evidência esperada:** tabelas resumidas e gráficos que mostrem tanto a mudança
    agregada quanto a heterogeneidade entre municípios.

    **Limite:** o processo gerador foi construído para produzir associações didáticas;
    seus resultados não descrevem o Brasil.
    """,
    5: """
    **Comparação principal:** mudança da alfabetização em cada município entre 2010
    e 2022. O pareamento pelo código evita comparar conjuntos municipais diferentes.

    **Sensibilidade:** observar a mudança média segundo faixas de urbanização inicial
    e segundo região. Diferenças agregadas não substituem a inspeção da distribuição
    das mudanças municipais.

    **Interpretação:** grupos podem apresentar mudanças distintas, mas a simulação
    não oferece desenho causal nem representa amostra probabilística.
    """,
    6: """
    **Decisão:** não incorporar redes. As linhas descrevem municípios e indicadores,
    mas não contêm relações como fluxos migratórios, deslocamentos ou vínculos
    institucionais.

    **Risco de forçar o método:** criar arestas apenas por semelhança de indicadores
    produziria uma rede analítica, não uma rede social ou territorial observada.

    **Alternativa:** preservar comparações, distribuições e associações entre
    variáveis, que respondem melhor à pergunta.
    """,
    7: """
    **Decisão:** incorporar uma regressão linear descritiva simples como diagnóstico
    da associação entre urbanização e alfabetização em 2022.

    **Resposta:** taxa de alfabetização. **Característica:** taxa de urbanização.
    A inclinação resume uma associação média no corpus sintético.

    **Limites:** regiões, renda, história municipal, composição demográfica e erro
    de medição não são controlados. O coeficiente não deve receber interpretação
    causal nem ser generalizado para municípios reais.
    """,
    8: """
    **Decisão:** não incorporar classificação. Transformar alfabetização contínua em
    “alta” e “baixa” apagaria variações e exigiria um limiar substantivo que a
    pergunta não fornece.

    **Aprendizagem transferida:** se uma política pública futura definisse uma classe
    de prioridade, seria necessário documentar o rótulo, avaliar erros entre grupos
    e comparar o modelo com uma regra simples.
    """,
    9: """
    **Decisão:** não incorporar agrupamento ao argumento principal. Um piloto poderia
    agrupar perfis municipais, mas os grupos dependeriam de escala, variáveis e número
    de clusters.

    **Risco:** nomear clusters como “municípios desenvolvidos” naturalizaria uma
    construção algorítmica e multidimensional sem fundamentação conceitual suficiente.
    """,
    10: """
    **Decisão:** não incorporar extração de informações. A base já é tabular e não
    contém documentos dos quais entidades ou relações precisem ser extraídas.

    **Possível extensão:** atas, relatórios municipais ou descrições metodológicas
    poderiam formar outro corpus, com unidade e cadeia de evidência próprias. Essa
    extensão não é necessária para responder à pergunta atual.
    """,
    11: """
    **Decisão:** incorporar comparação temporal limitada a dois pontos. O notebook
    não chama essa diferença de tendência contínua, pois não observa os anos
    intermediários.

    **Análise espacial não incorporada:** o exemplo não possui geometrias nem códigos
    oficiais. Colorir um mapa com municípios inventados seria enganoso. Região é
    utilizada apenas como categoria agregada.
    """,
    12: """
    **Decisão:** não incorporar modelo de linguagem. A pergunta é respondida com
    variáveis numéricas documentadas; gerar resumos automáticos não acrescentaria
    evidência e poderia produzir afirmações incompatíveis com a natureza sintética.

    **Uso responsável possível:** auxiliar a revisão da clareza do texto, mantendo
    verificação humana e sem apresentar texto gerado como análise empírica.
    """,
    13: """
    **Validade de construto:** alfabetização e urbanização são representadas por um
    único indicador simulado cada; os conceitos sociais são mais amplos que essas
    colunas.

    **Robustez:** comparar média e mediana, examinar municípios extremos e repetir a
    análise por região. A associação positiva permanece no conjunto gerado, mas sua
    magnitude depende das regras da simulação.

    **Ameaça decisiva:** validade externa inexistente. O corpus ensina um percurso de
    análise, não produz conhecimento sobre municípios brasileiros reais.
    """,
    14: """
    **Versão:** `v1.0-exemplo-sintetico`.

    **Resultado central:** no conjunto fictício, alfabetização aumenta entre os dois
    momentos e se associa positivamente à urbanização, com heterogeneidade regional
    e municipal.

    **Métodos incorporados:** exploração, comparação pareada, sensibilidade, regressão
    descritiva e comparação temporal de dois pontos. **Métodos recusados:** redes,
    classificação, clusters como argumento, extração e modelos de linguagem.

    **Próxima etapa real:** substituir a simulação por uma consulta documentada ao
    SIDRA, reconstruir o dicionário a partir dos metadados oficiais e reavaliar todas
    as conclusões.
    """,
}


def demonstracao_ibge(unidade: int) -> list[dict]:
    """Código e interpretação do exemplo municipal sintético."""
    if unidade == 3:
        return [
            md("""
            ### Demonstração técnica — gerar o painel municipal sintético

            Esta célula imita a forma de uma base municipal, mas não seus valores.
            A semente torna a simulação reproduzível. Em uma pesquisa real, o código
            começaria pela importação e pela documentação da tabela oficial.
            """),
            codigo("""
            import numpy as np
            import pandas as pd
            import matplotlib.pyplot as plt

            rng = np.random.default_rng(2026)
            regioes = ["Norte", "Nordeste", "Sudeste", "Sul", "Centro-Oeste"]
            municipios = pd.DataFrame({
                "codigo_municipio": [f"F{i:05d}" for i in range(1, 61)],
                "municipio": [f"Município fictício {i:03d}" for i in range(1, 61)],
                "regiao": np.repeat(regioes, 12),
            })

            efeito_regiao = {
                "Norte": -5, "Nordeste": -7, "Sudeste": 6,
                "Sul": 5, "Centro-Oeste": 1,
            }
            municipios["urbanizacao_2010"] = np.clip(
                62 + municipios["regiao"].map(efeito_regiao)
                + rng.normal(0, 11, len(municipios)), 25, 95
            )
            municipios["alfabetizacao_2010"] = np.clip(
                67 + 0.24 * municipios["urbanizacao_2010"]
                + municipios["regiao"].map(efeito_regiao) * 0.25
                + rng.normal(0, 2.8, len(municipios)), 60, 98
            )
            municipios["populacao_2010"] = np.exp(
                rng.normal(np.log(65000), 0.75, len(municipios))
            ).round().astype(int)

            linhas = []
            for ano in [2010, 2022]:
                posterior = ano == 2022
                bloco = municipios[[
                    "codigo_municipio", "municipio", "regiao"
                ]].copy()
                bloco["ano"] = ano
                bloco["populacao"] = (
                    municipios["populacao_2010"]
                    * (1 + (rng.normal(0.10, 0.08, len(municipios)) if posterior else 0))
                ).round().clip(lower=1000).astype(int)
                bloco["urbanizacao_pct"] = np.clip(
                    municipios["urbanizacao_2010"]
                    + (rng.normal(5.5, 1.8, len(municipios)) if posterior else 0),
                    20, 99,
                ).round(1)
                bloco["alfabetizacao_pct"] = np.clip(
                    municipios["alfabetizacao_2010"]
                    + (4 + 0.035 * municipios["urbanizacao_2010"]
                       + rng.normal(0, 1.2, len(municipios)) if posterior else 0),
                    55, 99.5,
                ).round(1)
                bloco["renda_pc"] = np.clip(
                    420 + 11 * bloco["urbanizacao_pct"]
                    + bloco["regiao"].map(efeito_regiao) * 12
                    + (260 if posterior else 0)
                    + rng.normal(0, 120, len(municipios)),
                    250, None,
                ).round(0)
                linhas.append(bloco)

            ibge_sintetico = pd.concat(linhas, ignore_index=True).sort_values(
                ["codigo_municipio", "ano"]
            ).reset_index(drop=True)
            display(ibge_sintetico.head(8))
            """),
            codigo("""
            verificacoes_ibge = pd.Series({
                "linhas": len(ibge_sintetico),
                "municípios únicos": ibge_sintetico["codigo_municipio"].nunique(),
                "chaves município-ano únicas": int(
                    ~ibge_sintetico.duplicated(["codigo_municipio", "ano"]).any()
                ),
                "observações por município": sorted(
                    ibge_sintetico.groupby("codigo_municipio").size().unique().tolist()
                ),
                "percentuais fora de 0–100": int(
                    (~ibge_sintetico["alfabetizacao_pct"].between(0, 100)).sum()
                    + (~ibge_sintetico["urbanizacao_pct"].between(0, 100)).sum()
                ),
            }, name="resultado")
            display(verificacoes_ibge.to_frame())
            """),
            md("""
            **Análise da preparação.** As 120 linhas correspondem a 60 municípios
            observados duas vezes. A chave município-ano é única e os percentuais
            permanecem nos intervalos esperados. Isso verifica a estrutura do painel,
            não a autenticidade ou a representatividade dos valores.
            """),
        ]

    if unidade == 4:
        return [
            md("""
            ### Exploração — centro, dispersão e associação visual

            A tabela resume os anos separadamente. Os gráficos mostram a mudança da
            distribuição e a relação municipal entre urbanização e alfabetização.
            """),
            codigo("""
            resumo_ibge = ibge_sintetico.groupby("ano").agg(
                municipios=("codigo_municipio", "nunique"),
                alfabetizacao_media=("alfabetizacao_pct", "mean"),
                alfabetizacao_mediana=("alfabetizacao_pct", "median"),
                alfabetizacao_dp=("alfabetizacao_pct", "std"),
                urbanizacao_media=("urbanizacao_pct", "mean"),
            )
            display(resumo_ibge.round(2))
            """),
            codigo("""
            fig, eixos = plt.subplots(1, 2, figsize=(12, 4.5))
            for ano, cor in [(2010, "#557a95"), (2022, "#d07c3e")]:
                recorte = ibge_sintetico[ibge_sintetico["ano"].eq(ano)]
                eixos[0].hist(
                    recorte["alfabetizacao_pct"], bins=10, alpha=0.55,
                    color=cor, label=str(ano),
                )
                eixos[1].scatter(
                    recorte["urbanizacao_pct"], recorte["alfabetizacao_pct"],
                    alpha=0.7, color=cor, label=str(ano),
                )
            eixos[0].set_title("Distribuição da alfabetização")
            eixos[0].set_xlabel("Alfabetização (%)")
            eixos[0].set_ylabel("Municípios")
            eixos[0].legend(title="Ano")
            eixos[1].set_title("Urbanização e alfabetização")
            eixos[1].set_xlabel("Urbanização (%)")
            eixos[1].set_ylabel("Alfabetização (%)")
            eixos[1].legend(title="Ano")
            plt.tight_layout()
            plt.show()
            """),
            md("""
            **Análise dos gráficos.** A distribuição de 2022 se desloca para taxas
            de alfabetização maiores, embora permaneça sobreposição entre os anos.
            No diagrama de dispersão, municípios mais urbanizados tendem a apresentar
            alfabetização maior. A nuvem não forma uma linha perfeita: municípios
            com urbanização semelhante ainda diferem, lembrando que uma única variável
            não explica todo o fenômeno.
            """),
        ]

    if unidade == 5:
        return [
            md("""
            ### Comparação pareada — a mudança dentro de cada município

            Em vez de comparar apenas duas médias agregadas, reorganizamos a base
            para calcular quanto cada município mudou entre os dois anos.
            """),
            codigo("""
            painel_mudanca = ibge_sintetico.pivot(
                index=["codigo_municipio", "municipio", "regiao"],
                columns="ano",
                values=["alfabetizacao_pct", "urbanizacao_pct"],
            ).reset_index()
            painel_mudanca.columns = [
                "codigo_municipio", "municipio", "regiao",
                "alfabetizacao_2010", "alfabetizacao_2022",
                "urbanizacao_2010", "urbanizacao_2022",
            ]
            painel_mudanca["mudanca_alfabetizacao_pp"] = (
                painel_mudanca["alfabetizacao_2022"]
                - painel_mudanca["alfabetizacao_2010"]
            )
            painel_mudanca["faixa_urbanizacao_inicial"] = pd.qcut(
                painel_mudanca["urbanizacao_2010"], 3,
                labels=["menor", "intermediária", "maior"],
            )
            mudanca_por_faixa = painel_mudanca.groupby(
                "faixa_urbanizacao_inicial", observed=True
            )["mudanca_alfabetizacao_pp"].agg(["count", "mean", "median", "std"])
            display(mudanca_por_faixa.round(2))
            """),
            codigo("""
            media_regional = painel_mudanca.groupby("regiao")[
                "mudanca_alfabetizacao_pp"
            ].mean().sort_values()
            media_regional.plot.barh(figsize=(8, 4.5), color="#6a8f6b")
            plt.axvline(0, color="#333333", linewidth=1)
            plt.title("Mudança média da alfabetização por região — dados sintéticos")
            plt.xlabel("Mudança entre 2010 e 2022 (pontos percentuais)")
            plt.ylabel("Região")
            plt.tight_layout()
            plt.show()
            """),
            md("""
            **Análise da comparação.** Todas as faixas apresentam mudança média
            positiva no conjunto gerado, mas com dispersão interna. O gráfico regional
            facilita comparar magnitudes, sem transformar região em explicação causal.
            Como cada barra resume doze municípios fictícios, a média não deve apagar
            casos municipais divergentes.
            """),
        ]

    if unidade == 7:
        return [
            md("""
            ### Regressão descritiva — resumir uma associação

            O ajuste abaixo descreve a inclinação da relação em 2022. Ele é usado
            como síntese visual e numérica, não como prova de causalidade.
            """),
            codigo("""
            dados_2022 = ibge_sintetico[ibge_sintetico["ano"].eq(2022)].copy()
            inclinacao, intercepto = np.polyfit(
                dados_2022["urbanizacao_pct"],
                dados_2022["alfabetizacao_pct"], 1,
            )
            previsto = intercepto + inclinacao * dados_2022["urbanizacao_pct"]
            r2 = 1 - (
                ((dados_2022["alfabetizacao_pct"] - previsto) ** 2).sum()
                / ((dados_2022["alfabetizacao_pct"]
                    - dados_2022["alfabetizacao_pct"].mean()) ** 2).sum()
            )
            display(pd.Series({
                "inclinação por 1 p.p. de urbanização": inclinacao,
                "R²": r2,
                "n": len(dados_2022),
            }, name="estimativa").to_frame().round(3))

            x_linha = np.linspace(
                dados_2022["urbanizacao_pct"].min(),
                dados_2022["urbanizacao_pct"].max(), 100,
            )
            plt.figure(figsize=(7.5, 4.5))
            plt.scatter(
                dados_2022["urbanizacao_pct"], dados_2022["alfabetizacao_pct"],
                alpha=0.7, color="#557a95",
            )
            plt.plot(x_linha, intercepto + inclinacao * x_linha, color="#b04a35")
            plt.title("Associação descritiva em 2022 — dados sintéticos")
            plt.xlabel("Urbanização (%)")
            plt.ylabel("Alfabetização (%)")
            plt.tight_layout()
            plt.show()
            """),
            md("""
            **Análise do ajuste.** A inclinação positiva resume a direção observada:
            no corpus simulado, urbanização maior está associada a alfabetização
            maior. O $R^2$ informa quanta variação o ajuste linear resume, não a
            importância histórica da variável. O modelo omite outros fatores e não
            autoriza a frase “urbanização aumenta a alfabetização”.
            """),
        ]

    if unidade == 11:
        return [
            md("""
            ### Comparação temporal agregada por região

            Com apenas dois anos, podemos mostrar diferenças entre pontos, mas não
            trajetórias contínuas. Cada linha abaixo liga duas médias regionais.
            """),
            codigo("""
            regional_ano = ibge_sintetico.groupby(["regiao", "ano"])[
                "alfabetizacao_pct"
            ].mean().unstack("ano")
            display(regional_ano.round(2))

            fig, eixo = plt.subplots(figsize=(8, 5))
            for regiao, valores in regional_ano.iterrows():
                eixo.plot(
                    [2010, 2022], [valores[2010], valores[2022]],
                    marker="o", linewidth=2, label=regiao,
                )
            eixo.set_title("Alfabetização média por região — dados sintéticos")
            eixo.set_xlabel("Ano observado")
            eixo.set_ylabel("Alfabetização média (%)")
            eixo.set_xticks([2010, 2022])
            eixo.legend(title="Região", bbox_to_anchor=(1.02, 1), loc="upper left")
            plt.tight_layout()
            plt.show()
            """),
            md("""
            **Análise do gráfico.** Todas as linhas terminam acima de seu ponto
            inicial porque a simulação incorporou crescimento. As diferenças de
            altura entre regiões também foram parcialmente programadas. O espaço
            entre 2010 e 2022 não contém observações; ligar os pontos ajuda a comparar,
            mas não demonstra uma evolução linear durante os anos intermediários.
            """),
        ]

    return []


def exemplo_ibge() -> list[dict]:
    celulas = [md("""
        # EXEMPLO PREENCHIDO — Projeto com estrutura inspirada em dados do IBGE

        **ID:** `PI-EXEMPLO-IBGE-SINTETICO`

        > **Dados inteiramente fictícios:** este notebook não contém estatísticas
        > oficiais, não foi produzido pelo IBGE e não deve ser citado como fonte sobre
        > o Brasil. Municípios, códigos e valores foram simulados para ensinar a
        > estrutura de uma entrega reprodutível.

        ## Pergunta do projeto

        Como a alfabetização varia entre 2010 e 2022 no corpus municipal sintético,
        e como essa variação se relaciona com urbanização inicial e grandes regiões?

        ## Forma da entrega

        O notebook intercala problema, código, tabelas, gráficos, interpretação e
        limites. O código aparece quando produz uma evidência necessária; decisões
        metodológicas que não exigem cálculo permanecem argumentadas em texto.
        """)]
    for unidade in range(1, 15):
        celulas.append(md(f"""
        ## U{unidade:02d} — {TITULOS_EXEMPLO[unidade]}

        {EXEMPLOS_IBGE[unidade]}
        """))
        celulas.extend(demonstracao_ibge(unidade))
    celulas.append(md("""
        ## Síntese do exemplo

        Este percurso mostra que usar uma estrutura semelhante à de dados públicos
        não dispensa documentação, validação de chaves, definição dos denominadores,
        comparação de distribuições e cautela causal. A substituição futura pelos
        dados oficiais exige nova auditoria; resultados sintéticos não podem ser
        transportados para o Brasil real.
        """))
    return celulas


def demonstracao_analitica(unidade: int) -> list[dict]:
    """Acrescenta código e interpretação onde o projeto produz evidências."""
    if unidade == 3:
        return [
            md("""
            ### Demonstração técnica — construir a base processável

            A célula seguinte cria uma versão sintética e reproduzível do corpus.
            Em uma pesquisa real, esta etapa leria os arquivos preservados em
            `dados/brutos/`; aqui os dados são gerados apenas para que o exemplo
            possa ser executado sem downloads.
            """),
            codigo("""
            import numpy as np
            import pandas as pd
            import matplotlib.pyplot as plt

            rng = np.random.default_rng(42)

            def criar_periodo(periodo, anos, composicao, media_frequencia):
                partes = []
                for periodico, quantidade, centrais in composicao:
                    parte = pd.DataFrame({
                        "periodo": periodo,
                        "ano": rng.choice(anos, quantidade, replace=True),
                        "periodico": periodico,
                        "educacao_central": [True] * centrais
                        + [False] * (quantidade - centrais),
                        "genero": rng.choice(
                            ["editorial", "notícia", "ensaio"],
                            quantidade,
                            p=[0.25, 0.45, 0.30],
                        ),
                        "tokens": np.maximum(
                            120, rng.normal(720, 230, quantidade).round()
                        ).astype(int),
                    })
                    partes.append(parte)
                periodo_df = pd.concat(partes, ignore_index=True)
                frequencias = rng.normal(media_frequencia, 2.2, len(periodo_df))
                frequencias += media_frequencia - frequencias.mean()
                periodo_df["freq_educacao_mil"] = frequencias.round(2)
                return periodo_df

            df = pd.concat([
                criar_periodo(
                    "1890–1899", range(1890, 1900),
                    [("A", 40, 10), ("B", 40, 9), ("C", 30, 7)], 8.2,
                ),
                criar_periodo(
                    "1900–1910", range(1900, 1911),
                    [("A", 35, 13), ("B", 35, 12), ("C", 35, 12), ("D", 25, 12)],
                    12.7,
                ),
            ], ignore_index=True).sample(frac=1, random_state=42).reset_index(drop=True)

            df.insert(0, "id_artigo", [f"ART-{i:03d}" for i in range(1, len(df) + 1)])
            df["mencoes_educacao"] = (
                df["freq_educacao_mil"] * df["tokens"] / 1000
            ).round().clip(lower=0).astype(int)

            display(df.head())
            """),
            codigo("""
            # Verificações mínimas antes da análise
            verificacoes = pd.Series({
                "linhas": len(df),
                "IDs únicos": df["id_artigo"].nunique(),
                "IDs ausentes": int(df["id_artigo"].isna().sum()),
                "anos mínimo e máximo": f"{df['ano'].min()}–{df['ano'].max()}",
                "frequências ausentes": int(df["freq_educacao_mil"].isna().sum()),
            }, name="resultado")
            display(verificacoes.to_frame())
            """),
            md("""
            **Leitura da verificação.** Há 240 linhas e 240 identificadores únicos,
            portanto cada linha pode representar um artigo sem duplicação de ID.
            A cobertura vai de 1890 a 1910 e a variável usada na exploração não tem
            valores ausentes. Esses testes não provam que a base é historicamente
            representativa; apenas confirmam algumas condições técnicas necessárias.
            """),
        ]

    if unidade == 4:
        return [
            md("""
            ### Exploração — resumir antes de interpretar

            Primeiro calculamos os denominadores e as medidas por período. Depois
            produzimos dois gráficos complementares: uma proporção baseada na
            anotação humana e a distribuição de uma frequência lexical.
            """),
            codigo("""
            resumo = (
                df.groupby("periodo", observed=True)
                .agg(
                    artigos=("id_artigo", "size"),
                    artigos_centrais=("educacao_central", "sum"),
                    proporcao_central=("educacao_central", "mean"),
                    media_freq_mil=("freq_educacao_mil", "mean"),
                    mediana_tokens=("tokens", "median"),
                )
            )
            display(resumo.round(3))
            """),
            codigo("""
            ordem = ["1890–1899", "1900–1910"]
            fig, eixos = plt.subplots(1, 2, figsize=(12, 4.2))

            (resumo.loc[ordem, "proporcao_central"] * 100).plot.bar(
                ax=eixos[0], color=["#6b8e9b", "#c87941"]
            )
            eixos[0].set_title("Artigos com educação como tema central")
            eixos[0].set_xlabel("Período")
            eixos[0].set_ylabel("Artigos (%)")
            eixos[0].tick_params(axis="x", rotation=0)
            eixos[0].set_ylim(0, 50)

            dados_boxplot = [
                df.loc[df["periodo"].eq(periodo), "freq_educacao_mil"]
                for periodo in ordem
            ]
            eixos[1].boxplot(dados_boxplot, tick_labels=ordem, showmeans=True)
            eixos[1].set_title("Vocabulário educacional por artigo")
            eixos[1].set_xlabel("Período")
            eixos[1].set_ylabel("Ocorrências por mil tokens")

            plt.tight_layout()
            plt.show()
            """),
            md("""
            **Análise dos resultados.** O primeiro gráfico mostra aproximadamente
            24% de artigos centrais no primeiro período e 38% no segundo. A altura
            das barras só é comparável porque cada valor usa como denominador o total
            de artigos do próprio período. O boxplot aponta também uma frequência
            lexical maior depois de 1900, mas exibe a dispersão e impede que a média
            seja confundida com o comportamento de todos os documentos.

            As duas evidências convergem, mas medem coisas diferentes: uma categoria
            atribuída ao artigo inteiro e ocorrências de vocabulário. Nenhum gráfico,
            isoladamente, demonstra uma transformação geral da imprensa operária.
            """),
        ]

    if unidade == 5:
        return [
            md("""
            ### Comparação e análise de sensibilidade

            Como o periódico D só existe no segundo período, repetimos a comparação
            usando apenas A, B e C. Essa mudança testa quanto o resultado depende da
            composição do corpus.
            """),
            codigo("""
            corpus_comum = df[df["periodico"].isin(["A", "B", "C"])]

            cenarios = pd.DataFrame({
                "corpus completo": df.groupby("periodo")["educacao_central"].mean(),
                "somente periódicos A–C": corpus_comum.groupby("periodo")["educacao_central"].mean(),
            }) * 100
            cenarios.loc["diferença (p.p.)"] = (
                cenarios.loc["1900–1910"] - cenarios.loc["1890–1899"]
            )
            display(cenarios.round(1))
            """),
            codigo("""
            comparacao = cenarios.drop(index="diferença (p.p.)").T
            comparacao.plot.bar(figsize=(8, 4), color=["#6b8e9b", "#c87941"])
            plt.title("Sensibilidade à composição dos periódicos")
            plt.xlabel("Cenário analítico")
            plt.ylabel("Artigos com educação central (%)")
            plt.xticks(rotation=0)
            plt.legend(title="Período")
            plt.ylim(0, 55)
            plt.tight_layout()
            plt.show()
            """),
            md("""
            **Análise dos resultados.** A diferença é de cerca de 14 pontos
            percentuais no corpus completo e 12 pontos quando comparamos somente
            periódicos presentes nos dois períodos. A direção do contraste permanece,
            mas sua magnitude diminui. Portanto, a composição institucional explica
            parte — não toda — da diferença observada. O resultado continua sendo
            descritivo e restrito ao corpus.
            """),
        ]

    if unidade == 11:
        return [
            md("""
            ### Exploração temporal — cobertura e tendência no mesmo gráfico

            Uma linha temporal pode sugerir continuidade mesmo quando alguns anos
            têm poucos documentos. Por isso o código calcula também o número de
            artigos por ano e só liga com uma linha os anos que atingem o limiar
            didático de oito artigos.
            """),
            codigo("""
            anual = (
                df.groupby("ano")
                .agg(
                    artigos=("id_artigo", "size"),
                    proporcao_central=("educacao_central", "mean"),
                )
                .reset_index()
            )
            anual["percentual_central"] = anual["proporcao_central"] * 100

            fig, eixo = plt.subplots(figsize=(10, 4.5))
            eixo.scatter(
                anual["ano"], anual["percentual_central"],
                s=anual["artigos"] * 7, color="#777777", alpha=0.7,
                label="todos os anos (tamanho = cobertura)",
            )
            cobertura_suficiente = anual[anual["artigos"] >= 8]
            eixo.plot(
                cobertura_suficiente["ano"],
                cobertura_suficiente["percentual_central"],
                color="#a34f2a", marker="o",
                label="anos com pelo menos 8 artigos",
            )
            eixo.axvline(1899.5, color="#333333", linestyle="--", linewidth=1)
            eixo.set_title("Centralidade da educação e cobertura anual")
            eixo.set_xlabel("Ano")
            eixo.set_ylabel("Artigos com educação central (%)")
            eixo.set_ylim(0, 100)
            eixo.legend()
            plt.tight_layout()
            plt.show()

            display(anual)
            """),
            md("""
            **Análise do gráfico.** Os percentuais oscilam bastante entre anos e o
            tamanho dos pontos mostra que a cobertura também varia. O segundo período
            tende a ocupar níveis mais altos, mas não há crescimento contínuo ano a
            ano. A linha tracejada apenas separa os períodos definidos na pesquisa;
            ela não prova que 1900 seja uma ruptura histórica. Essa leitura é mais
            cautelosa do que resumir o gráfico como “a educação aumentou”.
            """),
        ]

    return []


def exemplo_completo() -> list[dict]:
    """Reúne em um arquivo visível o exemplo que acompanha os 14 cadernos."""
    celulas = [
        md("""
        # EXEMPLO PREENCHIDO — Projeto integrador da U01 à U14

        **ID do projeto:** `PI-EXEMPLO-IMPRENSA`

        Este notebook mostra, em sequência, como um mesmo projeto poderia evoluir
        ao longo de todas as unidades da disciplina. Ele funciona como referência
        de **encadeamento**, nível de detalhe, registro de decisões e continuidade
        entre as entregas.

        > **Atenção:** o projeto, os periódicos, os dados e todos os resultados são
        > fictícios. Este material não representa uma pesquisa histórica real e não
        > deve ser copiado como resposta. Cada estudante deve trabalhar com sua
        > própria pergunta, seu corpus e suas evidências.

        ## Como ler este exemplo

        1. Observe o que cada unidade recebe da etapa anterior.
        2. Note que o corpus e a pergunta podem ser refinados, desde que a mudança
           seja registrada.
        3. Compare decisões de adoção e de não adoção de métodos.
        4. Use o caderno específico da unidade para produzir sua própria entrega.

        ## O que caracteriza a entrega em notebook

        A entrega não é apenas um relatório textual nem uma coleção de códigos.
        Ela deve construir uma sequência legível de evidências:

        | Elemento | Função |
        |---|---|
        | texto antes do código | apresenta a pergunta e explica por que a operação será feita |
        | código executável | realiza uma transformação, cálculo, tabela ou gráfico necessário |
        | saída selecionada | torna o resultado inspecionável pelo leitor |
        | análise depois da saída | interpreta padrões sem apenas repetir números ou formas |
        | limites | registra o que a evidência não permite concluir |

        Neste exemplo, a U03 constrói e verifica a base; a U04 explora tabelas e
        distribuições; a U05 compara cenários; e a U11 examina uma série temporal.
        As demais unidades mostram decisões que não exigem inserir código apenas
        para aparentar tecnicidade.

        | Percurso | Função no projeto fictício |
        |---|---|
        | U01–U05 | construir pergunta, corpus, base e comparação inicial |
        | U06–U12 | avaliar métodos e incorporar somente os pertinentes |
        | U13–U14 | auditar as conclusões e consolidar o projeto final |
        """)
    ]
    for unidade in range(1, 15):
        celulas.append(md(f"""
        ## U{unidade:02d} — {TITULOS_EXEMPLO[unidade]}

        {EXEMPLOS[unidade]}
        """))
        celulas.extend(demonstracao_analitica(unidade))
    celulas.append(md("""
        ## Síntese das decisões metodológicas do exemplo

        | Unidade | Decisão | Papel no argumento final |
        |---|---|---|
        | U06 | incorporar rede como complemento | explorar coocorrências, sem tratá-las como relações sociais comprovadas |
        | U07 | não incorporar regressão | evitar aparência de explicação incompatível com o desenho |
        | U08 | incorporar classificação assistida | priorizar revisão humana, sem automatizar categorias definitivas |
        | U09 | não incorporar tópicos | evitar interpretar agrupamentos instáveis como correntes históricas |
        | U10 | incorporar extração de entidades | sustentar a rede e preservar ligação com os trechos |
        | U11 | incorporar tempo e recusar mapa | usar a dimensão bem medida e explicitar a inadequação da outra |
        | U12 | não incorporar modelo de linguagem | ganho insuficiente diante da instabilidade e da menor rastreabilidade |

        O resultado final não é a soma indiscriminada de todas as técnicas. É um
        argumento no qual cada método foi escolhido, limitado ou recusado em função
        da pergunta e da qualidade das evidências disponíveis.
        """))
    return celulas


def abertura(unidade: int, titulo: str, produto: str, tipo: str) -> dict:
    if tipo == "cumulativa":
        regra = (
            "Este caderno é uma entrega obrigatória do **núcleo cumulativo**. "
            "Ele deve retomar a versão anterior do mesmo projeto e preparar a próxima."
        )
    elif tipo == "condicional":
        regra = (
            "Este caderno é uma entrega obrigatória de uma **unidade condicional**. "
            "O método pode ser incorporado ao projeto ou recusado de maneira fundamentada."
        )
    else:
        regra = (
            "Este caderno é uma entrega obrigatória do **fechamento comum** e reúne "
            "evidências acumuladas ao longo do projeto."
        )
    return md(f"""
    # PI-U{unidade:02d} — Caderno de entrega cumulativa — {titulo}

    {regra}

    **Produto desta etapa:** {produto}

    ## Antes de preencher: oficina não é entrega cumulativa

    | Oficina da unidade | Caderno de entrega cumulativa |
    |---|---|
    | ensina e permite experimentar o método | registra uma etapa do projeto do estudante |
    | pode usar o corpus didático da disciplina | usa o corpus-base do projeto, salvo contingência documentada |
    | pode conter exercícios, demonstrações e respostas provisórias | apresenta decisões, evidências, interpretação e arquivos entregues |
    | ajuda a aprender o procedimento | demonstra como o procedimento foi ou não incorporado ao argumento |

    Este caderno **não substitui o notebook técnico**. Código, cálculos, tabelas
    derivadas e gráficos devem permanecer em arquivos executáveis. Aqui, registre
    o que foi feito, por que foi feito, o resultado selecionado, seus limites e o
    caminho até os artefatos que sustentam a entrega.

    Use `Escreva aqui.` para substituir os campos. Não apague perguntas apenas
    porque a resposta é negativa ou o método não foi adotado.
    """)


def identificacao(unidade: int, versao: str) -> dict:
    return md(f"""
    ## 0. Identificação e controle de versão

    **ID permanente do projeto:** Escreva aqui.

    **Título vigente:** Escreva aqui.

    **Estudante ou equipe:** Escreva aqui.

    **Unidade:** U{unidade:02d}.

    **Versão sugerida da entrega:** `{versao}`.

    **Versão do corpus-base:** Escreva aqui.

    **Data da entrega:** Escreva aqui.

    **Local dos arquivos do projeto:** Escreva aqui.
    """)


def heranca(unidade_anterior: str, itens: str = "") -> dict:
    complemento = itens or "pergunta, unidade de análise, corpus, identificadores e limites"
    return md(f"""
    ## 1. Herança da entrega anterior

    Recupere a entrega {unidade_anterior}. Não reformule silenciosamente {complemento}.

    | Elemento herdado | Formulação ou versão anterior | Mantido ou alterado? | Justificativa e consequência |
    |---|---|---|---|
    | problema central | Escreva aqui. | Escreva aqui. | Escreva aqui. |
    | pergunta vigente | Escreva aqui. | Escreva aqui. | Escreva aqui. |
    | unidade de análise | Escreva aqui. | Escreva aqui. | Escreva aqui. |
    | corpus e recorte | Escreva aqui. | Escreva aqui. | Escreva aqui. |
    | conceitos, categorias ou variáveis | Escreva aqui. | Escreva aqui. | Escreva aqui. |
    | principal limite conhecido | Escreva aqui. | Escreva aqui. | Escreva aqui. |

    **A continuidade do projeto permanece reconhecível porque:** Escreva aqui.
    """)


def evidencias() -> dict:
    return md("""
    ## Evidências e arquivos da entrega

    Não cole apenas uma saída. Identifique o arquivo executável e explique como ele
    sustenta o resultado apresentado neste caderno.

    | Arquivo, pasta ou link | Função na entrega | Como foi produzido | Versão | Pode ser compartilhado? |
    |---|---|---|---|---|
    | Escreva aqui. | Escreva aqui. | Escreva aqui. | Escreva aqui. | Escreva aqui. |

    **Notebook ou script técnico principal:** Escreva aqui.

    **Ordem mínima de execução:** Escreva aqui.

    **Tabela ou figura central e arquivo que a sustenta:** Escreva aqui.

    **Restrições de acesso, direitos ou privacidade:** Escreva aqui.
    """)


def revisao_e_mudancas() -> dict:
    return md("""
    ## Revisão, mudanças e estado da entrega

    **Parecer ou comentário recebido:** Escreva aqui.

    **Mudanças incorporadas após a revisão:** Escreva aqui.

    **Sugestões não incorporadas e justificativa:** Escreva aqui.

    | Mudança nesta versão | Antes | Depois | Razão | Efeito sobre o projeto |
    |---|---|---|---|---|
    | Escreva aqui. | Escreva aqui. | Escreva aqui. | Escreva aqui. | Escreva aqui. |

    **O que esta entrega permite afirmar:** Escreva aqui.

    **O que esta entrega ainda não permite afirmar:** Escreva aqui.

    **Principal decisão pendente:** Escreva aqui.
    """)


def passagem(proxima: str, itens: str) -> dict:
    return md(f"""
    ## Passagem para {proxima}

    **Produto que seguirá adiante:** Escreva aqui.

    **Arquivos e decisões que a próxima etapa deverá receber:** {itens}

    **Questão que a próxima etapa deverá responder:** Escreva aqui.

    **Risco que não pode ser esquecido na próxima etapa:** Escreva aqui.

    ### Checklist de submissão

    - [ ] identificação e versões preenchidas;
    - [ ] herança ou ponto de partida registrado;
    - [ ] decisões justificadas;
    - [ ] evidências e arquivos localizáveis;
    - [ ] interpretação e limites explícitos;
    - [ ] mudanças registradas;
    - [ ] passagem para a próxima etapa preenchida.
    """)


def decisao_condicional(unidade: int, metodo: str, requisitos: list[str]) -> dict:
    linhas = "\n".join(f"- {item}" for item in requisitos)
    return md(f"""
    ## 2. Decisão de aplicabilidade — {metodo}

    Antes de aplicar o método, verifique se ele responde a uma subpergunta do
    projeto e se o corpus satisfaz seus requisitos.

    **Subpergunta que o método poderia responder:** Escreva aqui.

    **Por que essa subpergunta pertence ao problema central:** Escreva aqui.

    ### Requisitos a verificar

    {linhas}

    | Requisito | Situação no projeto | Evidência | Consequência |
    |---|---|---|---|
    | Escreva aqui. | Escreva aqui. | Escreva aqui. | Escreva aqui. |

    ### Decisão da U{unidade:02d}

    - [ ] **Forma A:** incorporar como método principal;
    - [ ] **Forma A:** incorporar como método complementar;
    - [ ] realizar piloto antes da decisão final;
    - [ ] **Forma B:** não incorporar ao projeto.

    **Decisão argumentada:** Escreva aqui.

    **Risco de forçar o método:** Escreva aqui.
    """)


def rotas_condicionais(conteudo_a: str, conteudo_b: str) -> list[dict]:
    return [
        md(f"""
        ## 3A. Forma A — método incorporado ao projeto

        Preencha esta seção se o diagnóstico sustentou a incorporação.

        {conteudo_a}

        **Código ou notebook de origem:** Escreva aqui.

        **Resultado selecionado:** Escreva aqui.

        **Interpretação humanística:** Escreva aqui.

        **Casos ou documentos inspecionados:** Escreva aqui.

        **Sensibilidade, erros ou especificação alternativa:** Escreva aqui.

        **Limite decisivo:** Escreva aqui.
        """),
        md(f"""
        ## 3B. Forma B — não adoção fundamentada

        Preencha esta seção se o método não foi incorporado. A não adoção não
        dispensa a aprendizagem realizada na oficina.

        {conteudo_b}

        **Requisito que o projeto não satisfaz ou desalinhamento encontrado:**
        Escreva aqui.

        **Por que a aplicação produziria resultado frágil ou irrelevante:**
        Escreva aqui.

        **Laboratório didático realizado e arquivo correspondente:** Escreva aqui.

        **O que o laboratório ensinou sobre o método:** Escreva aqui.

        **Método ou próximo passo mais adequado ao projeto:** Escreva aqui.

        **Declaração:** o resultado do laboratório didático integra a evidência do
        projeto? Responda `não` ou justifique uma exceção. Escreva aqui.
        """),
    ]


def u01() -> list[dict]:
    return [
        abertura(1, "proposta inicial", "proposta argumentada do projeto — `v0.1-proposta`", "cumulativa"),
        exemplo(1),
        identificacao(1, "v0.1-proposta"),
        md("""
        ## 1. Ponto de partida

        Como esta é a primeira entrega, não há uma versão anterior. Registre o ponto
        de partida que permitirá reconhecer o projeto nas unidades seguintes.

        **Fenômeno histórico, social, linguístico ou cultural:** Escreva aqui.

        **Contexto temporal, espacial e institucional:** Escreva aqui.

        **Motivação humanística:** Escreva aqui.

        **Conceito central e autores de referência:** Escreva aqui.
        """),
        md("""
        ## 2. Pergunta e finalidade

        **Questão ampla:** Escreva aqui.

        **Pergunta delimitada:** Escreva aqui.

        **Finalidade predominante:** descrever, comparar, associar, explicar,
        classificar, explorar relações ou outra. Escreva aqui.

        **Estrutura analítica inicial e justificativa:** Escreva aqui.

        **Tarefa computacional possível, sem transformar a técnica no objetivo:**
        Escreva aqui.
        """),
        md("""
        ## 3. Unidade, população e corpus pretendido

        **Unidade de análise:** Escreva aqui.

        **População ou universo de interesse:** Escreva aqui.

        **Corpus ou coleção pretendida:** Escreva aqui.

        **Fontes possíveis:** Escreva aqui.

        **Recortes e critérios iniciais:** Escreva aqui.

        **Acesso e viabilidade ainda não verificados:** Escreva aqui.
        """),
        md("""
        ## 4. Operacionalização e evidência esperada

        | Conceito | Dimensão | Indicador possível | Fonte | Limitação |
        |---|---|---|---|---|
        | Escreva aqui. | Escreva aqui. | Escreva aqui. | Escreva aqui. | Escreva aqui. |

        **Operação prevista:** Escreva aqui.

        **Resultado possível:** Escreva aqui.

        **De que poderia ser evidência:** Escreva aqui.

        **O que não demonstraria:** Escreva aqui.

        **Documentos ou casos que precisariam ser relidos:** Escreva aqui.
        """),
        md("""
        ## 5. Limites, ética e síntese da proposta

        **Limites de seleção, representação e automação:** Escreva aqui.

        **Pessoas ou grupos potencialmente afetados:** Escreva aqui.

        **Riscos de acesso, direitos ou exposição:** Escreva aqui.

        **Resumo autocontido da proposta:** Escreva aqui.

        **Próxima decisão necessária:** Escreva aqui.
        """),
        evidencias(),
        revisao_e_mudancas(),
        passagem("a U02 — protocolo da base", "pergunta, unidade, corpus pretendido, conceitos, fontes possíveis e riscos iniciais. Escreva aqui."),
    ]


def u02() -> list[dict]:
    return [
        abertura(2, "protocolo da base", "protocolo auditável — `v0.2-protocolo`", "cumulativa"),
        exemplo(2),
        identificacao(2, "v0.2-protocolo"),
        heranca("PI-U01", "a pergunta, a unidade, o corpus pretendido e os conceitos"),
        md("""
        ## 2. Fontes e cadeia de produção

        **Fontes primárias em relação à pergunta:** Escreva aqui.

        **Fontes secundárias e dados derivados:** Escreva aqui.

        **Produtores, instituições e custodiantes:** Escreva aqui.

        **Finalidade original e categorias herdadas:** Escreva aqui.

        **Condições materiais e técnicas de acesso:** Escreva aqui.
        """),
        md("""
        ## 3. População, seleção, cobertura e silêncios

        **População de interesse:** Escreva aqui.

        **População acessível:** Escreva aqui.

        **Corpus previsto:** Escreva aqui.

        | Critério | Regra | Justificativa | Caso limítrofe | Registro da decisão |
        |---|---|---|---|---|
        | Escreva aqui. | Escreva aqui. | Escreva aqui. | Escreva aqui. | Escreva aqui. |

        **Cobertura temporal, espacial, social, institucional e documental:**
        Escreva aqui.

        **Silêncios que não equivalem a valores ausentes:** Escreva aqui.
        """),
        md("""
        ## 4. Metadados, proveniência e governança

        **Estratégia de identificadores:** Escreva aqui.

        | Campo | Definição | Tipo ou domínio | Origem | Regra | Limitação |
        |---|---|---|---|---|---|
        | Escreva aqui. | Escreva aqui. | Escreva aqui. | Escreva aqui. | Escreva aqui. | Escreva aqui. |

        **Versão, data de acesso, agente e transformações:** Escreva aqui.

        **Licença, direitos, ética, segurança e controle de acesso:** Escreva aqui.

        **Pessoas ou comunidades afetadas e usos a evitar:** Escreva aqui.
        """),
        md("""
        ## 5. Viabilidade e decisão sobre a base

        **Volume e trabalho de coleta:** Escreva aqui.

        **Amostra piloto e o que ela revelou:** Escreva aqui.

        **Dependências de autorização ou infraestrutura:** Escreva aqui.

        **Plano de contingência:** Escreva aqui.

        **Decisão:** prosseguir, reduzir escopo, mudar fonte, reformular ou
        interromper. Escreva aqui.

        **Justificativa:** Escreva aqui.
        """),
        evidencias(),
        revisao_e_mudancas(),
        passagem("a U03 — base processável", "protocolo aprovado, fontes permitidas, amostra piloto, dicionário preliminar, regras de seleção e restrições. Escreva aqui."),
    ]


def u03() -> list[dict]:
    return [
        abertura(3, "primeira base processável", "pacote de dados, código e documentação — `v0.3-base`", "cumulativa"),
        exemplo(3),
        identificacao(3, "v0.3-base"),
        heranca("PI-U02", "o protocolo, as fontes, os critérios de seleção e os identificadores"),
        md("""
        ## 2. Inventário, importação e extração

        **Arquivos, formatos, versões e proveniência:** Escreva aqui.

        **Política de preservação dos brutos:** Escreva aqui.

        | Fonte | Leitor e parâmetros | Estrutura esperada | Teste | Saída |
        |---|---|---|---|---|
        | Escreva aqui. | Escreva aqui. | Escreva aqui. | Escreva aqui. | Escreva aqui. |

        **PDF, OCR ou outras extrações e amostra de controle:** Escreva aqui.
        """),
        md("""
        ## 3. Modelo, transformações e qualidade

        **Tabelas e unidade de cada linha:** Escreva aqui.

        **Decisão largo/longo e relações entre tabelas:** Escreva aqui.

        | Campo | Original preservado | Regra | Teste | Perda possível |
        |---|---|---|---|---|
        | Escreva aqui. | Escreva aqui. | Escreva aqui. | Escreva aqui. | Escreva aqui. |

        **Ausências, duplicatas e decisões de revisão:** Escreva aqui.
        """),
        md("""
        ## 4. Integração, testes e reconstrução

        | Tabelas | Chave | Cardinalidade | Validação | Não correspondências |
        |---|---|---|---|---|
        | Escreva aqui. | Escreva aqui. | Escreva aqui. | Escreva aqui. | Escreva aqui. |

        **Contagens antes e depois:** Escreva aqui.

        **Testes de esquema, domínios, chaves e arquivos:** Escreva aqui.

        **Como reconstruir a base desde os brutos:** Escreva aqui.

        **Erros conhecidos e casos pendentes:** Escreva aqui.
        """),
        md("""
        ## 5. Parecer de processabilidade

        **O que a base já permite analisar:** Escreva aqui.

        **O que ainda não deve ser analisado ou concluído:** Escreva aqui.

        **Cobertura e limites herdados que permanecem:** Escreva aqui.

        **Versão congelada que seguirá para exploração:** Escreva aqui.
        """),
        evidencias(),
        revisao_e_mudancas(),
        passagem("a U04 — relatório exploratório", "base congelada, dicionário, relatório de qualidade, notebook de reconstrução e limites. Escreva aqui."),
    ]


def u04() -> list[dict]:
    return [
        abertura(4, "relatório exploratório", "relatório auditável — `v0.4-exploracao`", "cumulativa"),
        exemplo(4),
        identificacao(4, "v0.4-exploracao"),
        heranca("PI-U03", "a base processável, o dicionário, a pergunta e os limites de qualidade"),
        md("""
        ## 2. Escopo da exploração

        **Pergunta exploratória derivada do problema central:** Escreva aqui.

        **Corpus, período, unidade e quantidade de registros:** Escreva aqui.

        **Variáveis ou campos selecionados e sua classificação:** Escreva aqui.

        **Ausências, cobertura, erros conhecidos e casos extremos:** Escreva aqui.

        **Por que a base é adequada ou apenas parcialmente adequada:** Escreva aqui.
        """),
        md("""
        ## 3. Evidências exploratórias selecionadas

        Não force todas as famílias. Preencha as que respondem à pergunta e explique
        por que as demais não foram usadas.

        | Família | Procedimento e regra | Resultado | Interpretação | Limite |
        |---|---|---|---|---|
        | quantitativa | Escreva aqui. | Escreva aqui. | Escreva aqui. | Escreva aqui. |
        | textual | Escreva aqui. | Escreva aqui. | Escreva aqui. | Escreva aqui. |
        | categórica, temporal ou outra | Escreva aqui. | Escreva aqui. | Escreva aqui. | Escreva aqui. |

        **Família não utilizada e razão:** Escreva aqui.
        """),
        md("""
        ## 4. Visualizações e retorno aos casos

        | Figura | Pergunta | Tabela equivalente | Padrão descrito | Limite |
        |---|---|---|---|---|
        | Escreva aqui. | Escreva aqui. | Escreva aqui. | Escreva aqui. | Escreva aqui. |

        Selecione casos que confirmem, contradigam ou qualifiquem os agregados.

        | Caso ou ID | Razão da seleção | Evidência documental | Efeito sobre a leitura |
        |---|---|---|---|
        | Escreva aqui. | Escreva aqui. | Escreva aqui. | Escreva aqui. |
        """),
        md("""
        ## 5. Hipóteses provisórias e comparação futura

        | Hipótese | Evidência exploratória | Explicação alternativa | Dados necessários |
        |---|---|---|---|
        | Escreva aqui. | Escreva aqui. | Escreva aqui. | Escreva aqui. |

        **Hipótese ou contraste selecionado para a U05:** Escreva aqui.

        **Grupos, períodos, documentos ou versões que poderiam ser comparados:**
        Escreva aqui.
        """),
        evidencias(),
        revisao_e_mudancas(),
        passagem("a U05 — análise comparativa", "hipótese ou contraste, base e subconjuntos documentados, tabelas, casos e limites. Escreva aqui."),
    ]


def u05() -> list[dict]:
    return [
        abertura(5, "análise comparativa", "comparação com sensibilidade — `v0.5-comparacao`", "cumulativa"),
        exemplo(5),
        identificacao(5, "v0.5-comparacao"),
        heranca("PI-U04", "a hipótese exploratória, os grupos ou documentos, a base e os casos"),
        md("""
        ## 2. Pergunta comparativa e comparabilidade

        **Pergunta comparativa:** Escreva aqui.

        **Grupo, período, documento ou subconjunto A:** Escreva aqui.

        **Grupo, período, documento ou subconjunto B:** Escreva aqui.

        **Critérios, tamanhos e cobertura:** Escreva aqui.

        **Assimetrias de produção, preservação ou acesso:** Escreva aqui.

        **Por que a comparação é defensável:** Escreva aqui.
        """),
        md("""
        ## 3. Especificação principal e resultado

        **Percurso:** quantitativo, textual ou combinado. Escreva aqui.

        **Variável, representação ou quantidade:** Escreva aqui.

        **Medida, fórmula e parâmetros:** Escreva aqui.

        **Resultado principal e tabela:** Escreva aqui.

        **Descrição estrita do resultado:** Escreva aqui.

        **Relevância substantiva sem antecipar causalidade:** Escreva aqui.
        """),
        md("""
        ## 4. Sensibilidade e retorno aos casos

        **Especificação alternativa:** Escreva aqui.

        **O que permaneceu e o que mudou:** Escreva aqui.

        **A conclusão depende da escolha da medida?** Escreva aqui.

        | Caso | Por que foi selecionado | Evidência | Efeito sobre a interpretação |
        |---|---|---|---|
        | típico | Escreva aqui. | Escreva aqui. | Escreva aqui. |
        | influente ou extremo | Escreva aqui. | Escreva aqui. | Escreva aqui. |
        | contraditório | Escreva aqui. | Escreva aqui. | Escreva aqui. |
        """),
        md("""
        ## 5. Diagnóstico inicial dos métodos condicionais

        | Unidade | Método | Parece aplicável? | Evidência ou requisito ausente |
        |---|---|---|---|
        | U06 | associação ou rede | Escreva aqui. | Escreva aqui. |
        | U07 | regressão | Escreva aqui. | Escreva aqui. |
        | U08 | classificação | Escreva aqui. | Escreva aqui. |
        | U09 | agrupamento ou tópicos | Escreva aqui. | Escreva aqui. |
        | U10 | extração | Escreva aqui. | Escreva aqui. |
        | U11 | tempo ou espaço | Escreva aqui. | Escreva aqui. |
        | U12 | modelo de linguagem | Escreva aqui. | Escreva aqui. |

        **Método condicional mais promissor e razão:** Escreva aqui.
        """),
        evidencias(),
        revisao_e_mudancas(),
        passagem("as U06–U12 — métodos condicionais", "comparação, casos, limites e diagnóstico de aplicabilidade. Escreva aqui."),
    ]


CONDICIONAIS = {
    6: {
        "arquivo": "PI_U06_associacao_ou_rede.ipynb",
        "titulo": "associação ou rede",
        "produto": "análise incorporada ou não adoção fundamentada",
        "metodo": "associação entre características ou construção de rede",
        "requisitos": [
            "duas variáveis pertinentes ou entidades e relações identificáveis;",
            "unidade, escala, direção e peso interpretáveis;",
            "quantidade e cobertura adequadas;",
            "possíveis confundidores ou regras de criação de arestas;",
            "retorno aos registros e fontes.",
        ],
        "a": "Escolha o percurso quantitativo ou relacional. Defina variáveis, entidades, arestas, pesos e medida antes de calcular.",
        "b": "Explique se faltam variáveis, relações, desambiguação, cobertura ou significado substantivo para a rede ou associação.",
    },
    7: {
        "arquivo": "PI_U07_regressao.ipynb",
        "titulo": "regressão e associação ajustada",
        "produto": "modelo incorporado ou não adoção fundamentada",
        "metodo": "regressão linear ou logística introdutória",
        "requisitos": [
            "variável de resposta definida;",
            "variáveis explicativas justificadas;",
            "número de observações compatível;",
            "categorias de referência e pressupostos;",
            "linguagem não causal quando o desenho for observacional.",
        ],
        "a": "Registre resposta, explicativas, especificação, coeficientes em unidades compreensíveis, diagnóstico e casos influentes.",
        "b": "Explique se falta resposta, tamanho, variação, desenho ou justificativa para tratar o modelo como parte do argumento.",
    },
    8: {
        "arquivo": "PI_U08_classificacao.ipynb",
        "titulo": "classificação",
        "produto": "protótipo incorporado ou não adoção fundamentada",
        "metodo": "classificação supervisionada",
        "requisitos": [
            "categoria-alvo teoricamente relevante;",
            "guia e amostra de anotação;",
            "concordância ou revisão das divergências;",
            "separação de treinamento e teste;",
            "linha de base, métricas e análise de erros.",
        ],
        "a": "Documente finalidade, categorias, anotação, baseline, modelo, matriz de confusão, erros e diferenças entre grupos.",
        "b": "Explique se a categoria é instável, a anotação inviável, os exemplos insuficientes ou o uso preditivo irrelevante.",
    },
    9: {
        "arquivo": "PI_U09_agrupamento_ou_topicos.ipynb",
        "titulo": "agrupamento ou tópicos",
        "produto": "análise incorporada ou não adoção fundamentada",
        "metodo": "agrupamento de registros ou modelagem exploratória de tópicos",
        "requisitos": [
            "quantidade e diversidade suficientes;",
            "representação e distância justificadas;",
            "parâmetros e alternativas documentados;",
            "avaliação de estabilidade;",
            "leitura qualitativa de casos típicos e limítrofes.",
        ],
        "a": "Registre representação, parâmetros, estabilidade, caracterização, casos e cautelas na nomeação dos grupos ou tópicos.",
        "b": "Explique se o corpus é pequeno, homogêneo, teoricamente categorizado ou se o agrupamento produziria reificação.",
    },
    10: {
        "arquivo": "PI_U10_extracao_de_informacoes.ipynb",
        "titulo": "extração de informações",
        "produto": "base derivada incorporada ou não adoção fundamentada",
        "metodo": "extração de entidades, eventos ou relações",
        "requisitos": [
            "corpus textual e esquema de extração;",
            "regra, dicionário ou modelo documentado;",
            "amostra manual de referência;",
            "estratégia de desambiguação;",
            "vínculo entre resultado, trecho e documento.",
        ],
        "a": "Defina esquema, método, avaliação de inclusões e omissões, ambiguidades, proveniência e revisão humana.",
        "b": "Explique se o projeto não possui textos, entidades relevantes, amostra validável ou recursos para desambiguação.",
    },
    11: {
        "arquivo": "PI_U11_tempo_ou_espaco.ipynb",
        "titulo": "tempo ou espaço",
        "produto": "análise temporal ou espacial incorporada, ou não adoção fundamentada",
        "metodo": "análise temporal ou espacial",
        "requisitos": [
            "datas, períodos, lugares ou geometrias confiáveis;",
            "cobertura e denominadores conhecidos;",
            "unidades comparáveis;",
            "mudanças de definição ou território documentadas;",
            "visualização ligada a uma pergunta, não decorativa.",
        ],
        "a": "Escolha tempo ou espaço. Registre unidades, cobertura, tabela equivalente, transformação observada, casos e limites.",
        "b": "Explique se datas, lugares, denominadores, cobertura ou quantidade de unidades impedem uma análise defensável.",
    },
    12: {
        "arquivo": "PI_U12_modelos_de_linguagem.ipynb",
        "titulo": "modelos de linguagem",
        "produto": "experimento controlado incorporado ou não adoção fundamentada",
        "metodo": "modelo de linguagem comparado a uma referência",
        "requisitos": [
            "tarefa e saída esperada definidas;",
            "método de referência;",
            "mesma amostra e critérios de avaliação;",
            "versão, instruções e parâmetros registrados;",
            "permissão, privacidade, custo e inspeção de erros.",
        ],
        "a": "Compare o modelo com uma baseline, registre protocolo, resultados, acertos, erros, instabilidade, custo e decisão de uso.",
        "b": "Explique se dados, autorização, baseline, custo, estabilidade ou benefício impedem a incorporação responsável.",
    },
}


def condicional(unidade: int, config: dict) -> list[dict]:
    celulas = [
        abertura(unidade, config["titulo"], config["produto"], "condicional"),
        exemplo(unidade),
        identificacao(unidade, f"v0.{unidade}-{config['titulo'].replace(' ', '-')}") ,
        heranca("PI-U05 ou da última entrega incorporada", "o problema, o corpus, as hipóteses, os resultados e os limites"),
        decisao_condicional(unidade, config["metodo"], config["requisitos"]),
    ]
    celulas.extend(rotas_condicionais(config["a"], config["b"]))
    celulas.extend([
        evidencias(),
        revisao_e_mudancas(),
        passagem("a próxima unidade condicional ou a U13", "decisão de aplicabilidade, resultado incorporado ou parecer de não adoção, laboratório e limites. Escreva aqui."),
    ])
    return celulas


def u13() -> list[dict]:
    return [
        abertura(13, "validade e robustez", "dossiê de validade — `v0.9-validade`", "fechamento"),
        exemplo(13),
        identificacao(13, "v0.9-validade"),
        heranca("do conjunto das entregas PI-U01 a PI-U12", "o problema, as versões do corpus, os resultados incorporados e as recusas metodológicas"),
        md("""
        ## 2. Inventário do argumento a avaliar

        | Afirmação ou resultado | Arquivo de origem | Método | Evidência | Alcance atual |
        |---|---|---|---|---|
        | Escreva aqui. | Escreva aqui. | Escreva aqui. | Escreva aqui. | Escreva aqui. |

        **Principal contribuição pretendida:** Escreva aqui.

        **Resultado negativo ou inconclusivo que deve ser preservado:** Escreva aqui.
        """),
        md("""
        ## 3. Validade de construto e dos dados

        **Relação entre conceitos, indicadores e operações:** Escreva aqui.

        **Dimensões não observadas:** Escreva aqui.

        **Seleção, cobertura e silêncios:** Escreva aqui.

        **Erros de extração, anotação ou transformação:** Escreva aqui.

        **Efeito das ausências, duplicatas e mudanças de versão:** Escreva aqui.
        """),
        md("""
        ## 4. Robustez, sensibilidade e inspeção de erros

        | Decisão avaliada | Alternativa | Resultado original | Resultado alternativo | Consequência |
        |---|---|---|---|---|
        | Escreva aqui. | Escreva aqui. | Escreva aqui. | Escreva aqui. | Escreva aqui. |

        **Linha de base e pressupostos:** Escreva aqui.

        **Casos contraditórios, extremos ou influentes:** Escreva aqui.

        **Erros sistemáticos e grupos afetados:** Escreva aqui.
        """),
        md("""
        ## 5. Alcance, ética e revisão das conclusões

        | Conclusão anterior | Manter, reduzir ou retirar? | Nova formulação | Razão |
        |---|---|---|---|
        | Escreva aqui. | Escreva aqui. | Escreva aqui. | Escreva aqui. |

        **Condições de generalização:** Escreva aqui.

        **Riscos, usos indevidos e restrições de compartilhamento:** Escreva aqui.

        **Correções obrigatórias antes da U14:** Escreva aqui.
        """),
        evidencias(),
        revisao_e_mudancas(),
        passagem("a U14 — projeto final", "versões congeladas, matriz de validade, sensibilidades, conclusões revisadas e correções obrigatórias. Escreva aqui."),
    ]


def u14() -> list[dict]:
    return [
        abertura(14, "projeto final", "projeto reprodutível e apresentação — `v1.0-final`", "fechamento"),
        exemplo(14),
        identificacao(14, "v1.0-final"),
        heranca("PI-U13", "as conclusões avaliadas, o corpus congelado, os métodos incorporados e as limitações"),
        md("""
        ## 2. Narrativa cumulativa do projeto

        **Como a pergunta mudou desde a U01:** Escreva aqui.

        **Como o corpus evoluiu desde a U02:** Escreva aqui.

        **Como a base foi produzida na U03:** Escreva aqui.

        **Que hipóteses surgiram na U04:** Escreva aqui.

        **Que comparação foi realizada na U05:** Escreva aqui.

        **Que métodos condicionais foram incorporados ou recusados:** Escreva aqui.

        **Como a U13 alterou as conclusões:** Escreva aqui.
        """),
        md("""
        ## 3. Relatório acadêmico final

        Confirme a presença das partes e indique onde estão:

        | Parte | Arquivo ou seção | Situação |
        |---|---|---|
        | problema, pergunta e literatura | Escreva aqui. | Escreva aqui. |
        | fontes, corpus e unidade | Escreva aqui. | Escreva aqui. |
        | construção dos dados | Escreva aqui. | Escreva aqui. |
        | exploração e comparação | Escreva aqui. | Escreva aqui. |
        | método incorporado | Escreva aqui. | Escreva aqui. |
        | resultados e casos | Escreva aqui. | Escreva aqui. |
        | validade e robustez | Escreva aqui. | Escreva aqui. |
        | interpretação, ética e limites | Escreva aqui. | Escreva aqui. |
        """),
        md("""
        ## 4. Pacote reprodutível

        - [ ] README com ordem de execução;
        - [ ] dados compartilháveis ou instruções de acesso;
        - [ ] dicionário e proveniência;
        - [ ] código e notebooks;
        - [ ] ambiente e dependências;
        - [ ] tabelas e figuras;
        - [ ] licenças e restrições;
        - [ ] manifesto e registro de mudanças;
        - [ ] testes ou verificações principais.

        **Procedimento de reprodução testado por:** Escreva aqui.

        **Resultado do teste de reprodução:** Escreva aqui.
        """),
        md("""
        ## 5. Apresentação, defesa e síntese final

        **Pergunta e contribuição em duas frases:** Escreva aqui.

        **Principal resultado:** Escreva aqui.

        **Caso ou documento que qualifica o resultado:** Escreva aqui.

        **Limite decisivo:** Escreva aqui.

        **Demonstração breve de reprodutibilidade:** Escreva aqui.

        **Pergunta recebida na defesa e resposta:** Escreva aqui.

        **Próxima versão possível da pesquisa:** Escreva aqui.
        """),
        evidencias(),
        revisao_e_mudancas(),
        md("""
        ## Encerramento da trilha

        **Qual decisão mudou mais o projeto?** Escreva aqui.

        **Qual método foi mais útil e qual foi recusado?** Escreva aqui.

        **Qual resultado permaneceu incerto?** Escreva aqui.

        **O projeto final distingue descrição, associação, predição, explicação e
        causalidade? Como?** Escreva aqui.

        ### Checklist final

        - [ ] versão `v1.0-final` identificada;
        - [ ] corpus e resultados correspondem ao relatório;
        - [ ] código executado desde o início;
        - [ ] restrições de compartilhamento respeitadas;
        - [ ] conclusões compatíveis com a avaliação da U13;
        - [ ] referências e créditos completos;
        - [ ] apresentação preparada.
        """),
    ]


def main() -> None:
    PASTA.mkdir(parents=True, exist_ok=True)
    salvar(
        "EXEMPLO_PREENCHIDO_PROJETO_JORNAIS_U01_a_U14.ipynb",
        exemplo_completo(),
    )
    salvar(
        "EXEMPLO_PREENCHIDO_IBGE_DADOS_FICTICIOS_U01_a_U14.ipynb",
        exemplo_ibge(),
    )
    print(f"2 exemplos completos construídos em {PASTA}")


if __name__ == "__main__":
    main()
