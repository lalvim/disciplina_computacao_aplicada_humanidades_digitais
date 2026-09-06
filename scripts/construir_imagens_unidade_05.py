"""Constrói diagramas SVG acessíveis da Unidade 5."""

from html import escape
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]
IMAGENS = RAIZ / "unidade_05" / "imagens"
C = {
    "fundo": "#fbf4e8", "papel": "#fffdf8", "azul": "#17324d",
    "azulc": "#dbe8ec", "verde": "#256b6b", "verdec": "#d8ebe7",
    "ocre": "#8a6528", "ocrec": "#f1e2bd", "vinho": "#7b3545",
    "vinhoc": "#efdde1", "cinza": "#53606c",
}


def texto(x, y, linhas, classe="corpo", ancora="middle", intervalo=22):
    spans = "".join(
        f'<tspan x="{x}" dy="{0 if i == 0 else intervalo}">{escape(l)}</tspan>'
        for i, l in enumerate(linhas)
    )
    return f'<text x="{x}" y="{y}" class="{classe}" text-anchor="{ancora}">{spans}</text>'


def caixa(x, y, w, h, titulo, linhas, fundo, borda):
    return (
        f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="16" '
        f'fill="{fundo}" stroke="{borda}" stroke-width="3"/>'
        + texto(x + w / 2, y + 32, [titulo], "subtitulo")
        + texto(x + w / 2, y + 66, linhas)
    )


def svg(titulo, desc, corpo, altura=540):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 {altura}"
 role="img" aria-labelledby="titulo descricao">
<title id="titulo">{escape(titulo)}</title>
<desc id="descricao">{escape(desc)}</desc>
<defs>
 <marker id="seta" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L0,6 L9,3 z" fill="{C['azul']}"/></marker>
 <style>.titulo{{font:700 29px system-ui;fill:{C['azul']}}}.subtitulo{{font:700 18px system-ui;fill:{C['azul']}}}.corpo{{font:16px system-ui;fill:{C['azul']}}}.nota{{font:italic 15px system-ui;fill:{C['cinza']}}}.seta{{stroke:{C['azul']};stroke-width:3;fill:none;marker-end:url(#seta)}}.linha{{stroke:{C['azul']};stroke-width:3;fill:none}}.tracejada{{stroke-dasharray:8 7}}</style>
</defs><rect width="1200" height="{altura}" rx="28" fill="{C['fundo']}"/>{corpo}</svg>'''


def fluxo():
    partes = [texto(600, 44, ["Comparar é uma cadeia de decisões"], "titulo")]
    itens = [
        (35, "Pergunta", ["unidades e", "subconjuntos"], C["azulc"], C["azul"]),
        (230, "Estimar", ["diferença", "e escala"], C["verdec"], C["verde"]),
        (425, "Incerteza", ["procedimento e", "pressupostos"], C["ocrec"], C["ocre"]),
        (620, "Representar", ["termos, pesos", "e sequências"], C["vinhoc"], C["vinho"]),
        (815, "Comparar", ["medida e", "sensibilidade"], C["azulc"], C["azul"]),
        (1010, "Interpretar", ["casos, contexto", "e limites"], C["verdec"], C["verde"]),
    ]
    for i, (x, t, ls, f, b) in enumerate(itens):
        partes.append(caixa(x, 125, 155, 145, t, ls, f, b))
        if i < len(itens) - 1:
            partes.append(f'<path class="seta" d="M{x+158},197 H{x+190}"/>')
    partes.append('<path class="seta tracejada" d="M1080,290 C1080,455 125,455 115,290"/>')
    partes.append(texto(600, 385, ["Uma medida alternativa ou um caso divergente pode exigir revisão"], "nota"))
    return svg("Percurso da comparação", "Seis etapas ligam pergunta, estimativa, incerteza, representação, medida e interpretação, com retorno para revisão.", "".join(partes), 470)


def diferenca():
    p = [texto(600, 44, ["Diferença observada não basta"], "titulo")]
    itens = [
        (70, "Diferença", ["quanto A e B", "se afastam?"], C["azulc"], C["azul"]),
        (465, "Incerteza", ["quanto variaria", "o procedimento?"], C["ocrec"], C["ocre"]),
        (860, "Relevância", ["o tamanho importa", "para a pergunta?"], C["verdec"], C["verde"]),
    ]
    for x, t, ls, f, b in itens: p.append(caixa(x, 125, 270, 155, t, ls, f, b))
    p += ['<path class="seta" d="M345,202 H455"/>', '<path class="seta" d="M740,202 H850"/>', texto(600, 355, ["Escala original + distribuição + desenho dos dados + contexto"], "nota")]
    return svg("Diferença, incerteza e relevância", "Três caixas separam tamanho observado, variabilidade do procedimento e importância substantiva no contexto.", "".join(p), 420)


def reamostragem():
    p = [texto(600, 42, ["Reamostrar aproxima a variabilidade de uma estimativa"], "titulo")]
    p.append(caixa(40, 145, 230, 140, "Amostra observada", ["unidades e grupos", "mantidos visíveis"], C["azulc"], C["azul"]))
    for i, y in enumerate([90, 210, 330]):
        p.append(caixa(410, y, 220, 90, f"Reamostra {i+1}", ["com reposição"], C["papel"], C["ocre"]))
        p.append(f'<path class="seta" d="M275,215 C330,215 350,{y+45} 400,{y+45}"/>')
    p.append(caixa(850, 145, 280, 140, "Distribuição bootstrap", ["uma diferença", "por reamostra"], C["verdec"], C["verde"]))
    for y in [135, 255, 375]: p.append(f'<path class="seta" d="M635,{y} C720,{y} 760,215 840,215"/>')
    p.append(texto(600, 475, ["A reamostragem herda a estrutura, a cobertura e os vieses dos dados observados"], "nota"))
    return svg("Fluxo de reamostragem bootstrap", "A amostra observada gera reamostras com reposição e uma distribuição de diferenças; uma nota alerta que vieses são herdados.", "".join(p), 530)


def distribuicao_nula():
    barras = []
    alturas = [18, 28, 42, 65, 95, 130, 170, 205, 230, 205, 170, 130, 95, 65, 42, 28, 18]
    for i, h in enumerate(alturas):
        cor = C["vinho"] if i in {0, 1, 15, 16} else C["azulc"]
        barras.append(f'<rect x="{150+i*52}" y="{390-h}" width="38" height="{h}" fill="{cor}" stroke="{C["azul"]}"/>')
    p = [texto(600, 42, ["Distribuição de referência sob a hipótese nula"], "titulo"), *barras]
    p += [f'<line x1="120" y1="390" x2="1080" y2="390" class="linha"/>', f'<line x1="960" y1="100" x2="960" y2="400" stroke="{C["vinho"]}" stroke-width="4"/>', texto(960, 85, ["resultado observado"], "subtitulo"), texto(600, 455, ["O valor de p é a proporção de resultados tão ou mais extremos sob o modelo nulo"], "nota")]
    return svg("Distribuição nula e resultado observado", "Histograma simétrico de resultados permutados marca as duas caudas e o resultado observado, sem usar um limiar automático.", "".join(p), 510)


def interpretacao_p():
    p = [texto(600, 42, ["O que cada resultado responde"], "titulo")]
    itens = [
        (55, "Estimativa", ["qual diferença", "foi observada?"], C["azulc"], C["azul"]),
        (335, "Intervalo", ["que valores são", "compatíveis?"], C["verdec"], C["verde"]),
        (615, "Valor de p", ["compatibilidade com", "um modelo nulo"], C["ocrec"], C["ocre"]),
        (895, "Contexto", ["a diferença é", "substantiva?"], C["vinhoc"], C["vinho"]),
    ]
    for x, t, ls, f, b in itens: p.append(caixa(x, 120, 250, 150, t, ls, f, b))
    p.append(texto(600, 345, ["Nenhuma caixa substitui desenho, transparência, teoria ou leitura dos casos"], "nota"))
    return svg("Mapa de interpretação inferencial", "Quatro caixas distinguem estimativa, intervalo, valor de p e relevância contextual, seguidas por alerta sobre desenho e teoria.", "".join(p), 410)


def matriz_documento_termo():
    p = [texto(600, 42, ["Do documento à matriz documento-termo"], "titulo")]
    itens = [(45, "Documentos", ["texto preservado", "e identificador"]), (315, "Tokens", ["regra explícita", "de normalização"]), (585, "Vocabulário", ["termos nas", "colunas"]), (855, "Matriz", ["documentos ×", "termos e pesos"])]
    for i, (x, t, ls) in enumerate(itens):
        p.append(caixa(x, 125, 220, 150, t, ls, [C["azulc"], C["verdec"], C["ocrec"], C["vinhoc"]][i], [C["azul"], C["verde"], C["ocre"], C["vinho"]][i]))
        if i < 3: p.append(f'<path class="seta" d="M{x+225},200 H{x+260}"/>')
    p.append(texto(600, 350, ["Ordem e sintaxe são perdidas; a ligação com o texto permite retornar ao contexto"], "nota"))
    return svg("Construção da matriz documento-termo", "Quatro etapas ligam documentos preservados, tokens, vocabulário e uma matriz; a nota registra a perda de ordem e sintaxe.", "".join(p), 420)


def tfidf():
    p = [texto(600, 42, ["TF-IDF combina presença local e raridade na coleção"], "titulo")]
    p.append(caixa(85, 120, 300, 160, "TF", ["quanto o termo", "aparece no documento"], C["azulc"], C["azul"]))
    p.append(caixa(455, 120, 300, 160, "IDF", ["em quantos documentos", "o termo aparece"], C["ocrec"], C["ocre"]))
    p.append(caixa(825, 120, 300, 160, "TF × IDF", ["peso sob uma", "convenção declarada"], C["verdec"], C["verde"]))
    p += ['<path class="seta" d="M390,200 H445"/>', '<path class="seta" d="M760,200 H815"/>', texto(600, 355, ["Peso alto não equivale automaticamente a importância histórica ou temática"], "nota")]
    return svg("Anatomia do TF-IDF", "TF mede frequência local, IDF mede raridade documental e o produto gera um peso dependente da convenção escolhida.", "".join(p), 420)


def metricas():
    p = [texto(600, 42, ["A pergunta determina a medida de comparação"], "titulo")]
    itens = [(55, "Jaccard", ["conjuntos", "presença ou ausência"], C["azulc"], C["azul"]), (335, "Cosseno", ["vetores", "frequências ou pesos"], C["verdec"], C["verde"]), (615, "Edição", ["sequências", "inserir, excluir, trocar"], C["ocrec"], C["ocre"]), (895, "Leitura", ["contexto", "casos divergentes"], C["vinhoc"], C["vinho"])]
    for x, t, ls, f, b in itens: p.append(caixa(x, 120, 250, 150, t, ls, f, b))
    p.append(texto(600, 345, ["Resultados não são intercambiáveis: cada medida preserva e perde relações diferentes"], "nota"))
    return svg("Comparação de métricas textuais", "Jaccard compara conjuntos, cosseno compara vetores, edição compara sequências e a leitura contextualiza resultados divergentes.", "".join(p), 410)


def edicao():
    p = [texto(600, 40, ["Distância de edição acumula decisões locais"], "titulo")]
    palavras_a = ["A", "ESCOLA", "ABRE", "HOJE"]
    palavras_b = ["A", "ESCOLA", "REABRE", "AMANHÃ"]
    for i, w in enumerate(palavras_a): p.append(caixa(210+i*205, 110, 160, 70, w, [], C["azulc"], C["azul"]))
    for i, w in enumerate(palavras_b): p.append(caixa(210+i*205, 300, 160, 70, w, [], C["verdec"], C["verde"]))
    for i in range(4): p.append(f'<path class="linha tracejada" d="M{290+i*205},185 V295"/>')
    p.append(texto(600, 235, ["manter • substituir • inserir • excluir"], "nota"))
    p.append(texto(600, 440, ["A distância localiza esforço de transformação; não interpreta o sentido da mudança"], "nota"))
    return svg("Comparação de versões por edição", "Duas sequências curtas são alinhadas por linhas tracejadas e relacionadas às operações manter, substituir, inserir e excluir.", "".join(p), 500)


def vizinhos():
    p = [texto(600, 42, ["Vizinhos dependem da representação e da métrica"], "titulo")]
    p.append(caixa(475, 190, 250, 120, "Documento consultado", ["texto e contexto", "preservados"], C["vinhoc"], C["vinho"]))
    pontos = [(80, 80, "A", "Jaccard"), (875, 75, "B", "cosseno TF-IDF"), (70, 350, "C", "cosseno contagens"), (890, 355, "D", "caso divergente")]
    for x, y, t, s in pontos:
        p.append(caixa(x, y, 230, 100, f"Documento {t}", [s], C["papel"], C["azul"]))
        p.append(f'<path class="seta tracejada" d="M{600 if x < 400 else 600},{250} L{x+115},{y+50}"/>')
    p.append(texto(600, 500, ["Inspecionar pares concordantes e divergentes revela o que cada medida privilegia"], "nota"))
    return svg("Vizinhos documentais sob diferentes medidas", "Um documento central se liga a quatro vizinhos encontrados por métricas diferentes, incluindo um caso divergente para inspeção.", "".join(p), 560)


def argumento():
    p = [texto(600, 42, ["Do resultado comparativo ao argumento"], "titulo")]
    itens = [(45, "Pergunta", ["comparação", "delimitada"]), (275, "Medida", ["convenção e", "pressupostos"]), (505, "Resultado", ["diferença ou", "similaridade"]), (735, "Casos", ["documentos e", "exceções"]), (965, "Argumento", ["relevância", "e limites"])]
    for i, (x, t, ls) in enumerate(itens):
        p.append(caixa(x, 125, 185, 145, t, ls, [C["azulc"], C["verdec"], C["ocrec"], C["vinhoc"], C["azulc"]][i], [C["azul"], C["verde"], C["ocre"], C["vinho"], C["azul"]][i]))
        if i < 4: p.append(f'<path class="seta" d="M{x+190},198 H{x+220}"/>')
    p.append('<path class="seta tracejada" d="M1055,290 C1055,445 140,445 140,290"/>')
    p.append(texto(600, 375, ["Sensibilidade ou caso contraditório pode exigir uma nova especificação"], "nota"))
    return svg("Cadeia do argumento comparativo", "Pergunta, medida, resultado, casos e argumento aparecem em sequência com retorno para nova especificação.", "".join(p), 460)


def main():
    IMAGENS.mkdir(parents=True, exist_ok=True)
    arquivos = {
        "00_percurso_comparacao.svg": fluxo(),
        "01_diferenca_incerteza_relevancia.svg": diferenca(),
        "02_fluxo_bootstrap.svg": reamostragem(),
        "02_distribuicao_nula.svg": distribuicao_nula(),
        "02_mapa_interpretacao.svg": interpretacao_p(),
        "03_fluxo_matriz_documento_termo.svg": matriz_documento_termo(),
        "03_anatomia_tfidf.svg": tfidf(),
        "04_escolha_metrica.svg": metricas(),
        "04_distancia_edicao.svg": edicao(),
        "04_vizinhos_documentais.svg": vizinhos(),
        "05_cadeia_argumento.svg": argumento(),
    }
    for nome, conteudo in arquivos.items():
        (IMAGENS / nome).write_text(conteudo, encoding="utf-8")
    print(f"{len(arquivos)} SVGs construídos em {IMAGENS}")


if __name__ == "__main__":
    main()
