"""Constrói os diagramas SVG acessíveis da Unidade 4."""

from __future__ import annotations

from html import escape
from pathlib import Path


RAIZ = Path(__file__).resolve().parents[1]
IMAGENS = RAIZ / "unidade_04" / "imagens"

CORES = {
    "fundo": "#fbf4e8",
    "papel": "#fffdf8",
    "azul": "#17324d",
    "azul_claro": "#dbe8ec",
    "verde": "#256b6b",
    "verde_claro": "#d8ebe7",
    "terracota": "#a44f32",
    "terracota_claro": "#f2ddd2",
    "ameixa": "#69445f",
    "ameixa_claro": "#eadde7",
    "areia": "#d8b26e",
    "cinza": "#53606c",
}


def texto(x, y, linhas, classe="corpo", ancora="middle", intervalo=22):
    spans = "".join(
        f'<tspan x="{x}" dy="{0 if i == 0 else intervalo}">{escape(linha)}</tspan>'
        for i, linha in enumerate(linhas)
    )
    return f'<text x="{x}" y="{y}" class="{classe}" text-anchor="{ancora}">{spans}</text>'


def caixa(x, y, largura, altura, titulo, linhas, fundo, contorno):
    return "".join(
        [
            f'<rect x="{x}" y="{y}" width="{largura}" height="{altura}" rx="18" '
            f'fill="{fundo}" stroke="{contorno}" stroke-width="3"/>',
            texto(x + largura / 2, y + 34, [titulo], "subtitulo"),
            texto(x + largura / 2, y + 70, linhas, "corpo"),
        ]
    )


def documento(titulo, descricao, corpo, altura=600):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 {altura}"
 role="img" aria-labelledby="titulo descricao">
<title id="titulo">{escape(titulo)}</title>
<desc id="descricao">{escape(descricao)}</desc>
<defs>
  <marker id="seta" markerWidth="10" markerHeight="10" refX="8" refY="3"
   orient="auto" markerUnits="strokeWidth">
    <path d="M0,0 L0,6 L9,3 z" fill="{CORES['azul']}"/>
  </marker>
  <style>
    .titulo {{ font: 700 30px system-ui, sans-serif; fill: {CORES['azul']}; }}
    .subtitulo {{ font: 700 19px system-ui, sans-serif; fill: {CORES['azul']}; }}
    .corpo {{ font: 16px system-ui, sans-serif; fill: {CORES['azul']}; }}
    .pequeno {{ font: 14px system-ui, sans-serif; fill: {CORES['azul']}; }}
    .nota {{ font: italic 15px system-ui, sans-serif; fill: {CORES['cinza']}; }}
    .seta {{ stroke: {CORES['azul']}; stroke-width: 3; fill: none; marker-end: url(#seta); }}
    .linha {{ stroke: {CORES['azul']}; stroke-width: 3; fill: none; }}
    .tracejada {{ stroke-dasharray: 9 7; }}
  </style>
</defs>
<rect width="1200" height="{altura}" rx="28" fill="{CORES['fundo']}"/>
{corpo}
</svg>
'''


def percurso():
    partes = [texto(600, 46, ["Explorar é construir um percurso de evidência"], "titulo")]
    itens = [
        (45, "Base documentada", ["corpus, unidade", "e qualidade"], CORES["azul_claro"], CORES["azul"]),
        (280, "Descrever", ["quantidades", "e textos"], CORES["verde_claro"], CORES["verde"]),
        (515, "Visualizar", ["padrões", "e casos"], CORES["terracota_claro"], CORES["terracota"]),
        (750, "Ler de perto", ["documentos", "e contextos"], CORES["ameixa_claro"], CORES["ameixa"]),
        (985, "Perguntar", ["hipóteses", "e limites"], "#f1e2bd", "#8a6528"),
    ]
    for i, (x, titulo, linhas, fundo, contorno) in enumerate(itens):
        partes.append(caixa(x, 125, 170, 145, titulo, linhas, fundo, contorno))
        if i < len(itens) - 1:
            partes.append(f'<path class="seta" d="M{x + 174},198 H{x + 225}"/>')
    partes.append('<path class="seta tracejada" d="M1070,290 C1070,495 140,495 130,290"/>')
    partes.append(texto(600, 420, ["Casos, limites e novas perguntas podem exigir revisar decisões anteriores"], "nota"))
    return documento(
        "Percurso da exploração",
        "Cinco etapas ligam base documentada, descrição, visualização, leitura próxima e formulação de hipóteses e limites. Uma seta retorna às decisões anteriores.",
        "".join(partes), 500,
    )


def niveis_escrita():
    partes = [texto(600, 46, ["Do resultado calculado à pergunta seguinte"], "titulo")]
    itens = [
        (55, "Procedimento", ["o que foi calculado?", "com qual regra?"], CORES["azul_claro"], CORES["azul"]),
        (285, "Descrição", ["que valores", "aparecem?"], CORES["verde_claro"], CORES["verde"]),
        (515, "Interpretação", ["que leitura situada", "é plausível?"], CORES["terracota_claro"], CORES["terracota"]),
        (745, "Limite", ["o que não pode", "ser afirmado?"], CORES["ameixa_claro"], CORES["ameixa"]),
        (975, "Próximo passo", ["que caso ou dado", "examinar?"], "#f1e2bd", "#8a6528"),
    ]
    for i, (x, titulo, linhas, fundo, contorno) in enumerate(itens):
        partes.append(caixa(x, 125, 180, 155, titulo, linhas, fundo, contorno))
        if i < len(itens) - 1:
            partes.append(f'<path class="seta" d="M{x + 184},202 H{x + 220}"/>')
    partes.append(texto(600, 355, ["Descrição não é explicação; hipótese não é conclusão"], "nota"))
    return documento(
        "Camadas da escrita exploratória",
        "A escrita começa no procedimento, passa pela descrição e interpretação, declara o limite e termina em um próximo passo. A legenda distingue descrição, explicação e conclusão.",
        "".join(partes), 420,
    )


def tipos_variaveis():
    partes = [texto(600, 44, ["A escala conceitual orienta operações e gráficos"], "titulo")]
    itens = [
        (45, "Nominal", ["distingue categorias", "frequências • barras"], CORES["azul_claro"], CORES["azul"]),
        (335, "Ordinal", ["categorias ordenadas", "posição • barras ordenadas"], CORES["verde_claro"], CORES["verde"]),
        (625, "Quantitativa", ["conta ou mede", "centro • dispersão"], CORES["terracota_claro"], CORES["terracota"]),
        (915, "Temporal", ["ordena no tempo", "pontos • linha cautelosa"], CORES["ameixa_claro"], CORES["ameixa"]),
    ]
    for x, titulo, linhas, fundo, contorno in itens:
        partes.append(caixa(x, 110, 240, 155, titulo, linhas, fundo, contorno))
    partes.append(caixa(400, 330, 400, 120, "Identificador", ["parece número, mas identifica", "não se soma nem se calcula média"], CORES["papel"], CORES["areia"]))
    partes.append(texto(600, 515, ["O dtype do arquivo não substitui a decisão teórica sobre a variável"], "nota"))
    return documento(
        "Tipos de variáveis e escolhas analíticas",
        "Quatro caixas relacionam escalas nominal, ordinal, quantitativa e temporal a operações e gráficos. Uma quinta caixa alerta que identificadores numéricos não são medidas.",
        "".join(partes), 560,
    )


def tokenizacao():
    partes = [texto(600, 44, ["Cada regra transforma o texto e pode apagar distinções"], "titulo")]
    itens = [
        (45, "Texto preservado", ["forma recebida", "e ID da fonte"], CORES["papel"], CORES["areia"]),
        (285, "Normalizar", ["minúsculas", "e pontuação"], CORES["azul_claro"], CORES["azul"]),
        (525, "Tokenizar", ["segmentar segundo", "uma regra"], CORES["verde_claro"], CORES["verde"]),
        (765, "Filtrar", ["stopwords", "declaradas"], CORES["terracota_claro"], CORES["terracota"]),
        (1005, "Contar", ["frequência", "e denominador"], CORES["ameixa_claro"], CORES["ameixa"]),
    ]
    for i, (x, titulo, linhas, fundo, contorno) in enumerate(itens):
        partes.append(caixa(x, 115, 150, 145, titulo, linhas, fundo, contorno))
        if i < len(itens) - 1:
            partes.append(f'<path class="seta" d="M{x + 154},188 H{x + 230}"/>')
    perdas = ["capitalização", "pontuação", "fronteiras", "palavras funcionais"]
    for i, perda in enumerate(perdas):
        x = 360 + i * 240
        partes.append(f'<path class="linha tracejada" d="M{x},270 V330"/>')
        partes.append(texto(x, 355, [perda], "pequeno"))
    partes.append(texto(600, 425, ["Preservar o original permite revisar o que cada transformação retirou"], "nota"))
    return documento(
        "Fluxo de tokenização e normalização",
        "O texto preservado passa por normalização, tokenização, filtro e contagem. Linhas tracejadas indicam possíveis perdas de capitalização, pontuação, fronteiras e palavras funcionais.",
        "".join(partes), 480,
    )


def pmi():
    partes = [texto(600, 44, ["PMI compara o par observado com suas marginais"], "titulo")]
    partes.append(caixa(70, 120, 270, 150, "Par observado", ["c(a,b)", "quantas vezes a b ocorre"], CORES["terracota_claro"], CORES["terracota"]))
    partes.append(caixa(465, 90, 270, 125, "Marginal esquerda", ["cL(a)", "a na primeira posição"], CORES["azul_claro"], CORES["azul"]))
    partes.append(caixa(465, 260, 270, 125, "Marginal direita", ["cR(b)", "b na segunda posição"], CORES["verde_claro"], CORES["verde"]))
    partes.append(caixa(860, 120, 270, 150, "PMI", ["mais que o esperado?", "comparar + interpretar"], CORES["ameixa_claro"], CORES["ameixa"]))
    partes.append('<path class="seta" d="M343,195 H455"/>')
    partes.append('<path class="seta" d="M738,155 C790,155 805,175 850,185"/>')
    partes.append('<path class="seta" d="M738,320 C790,320 805,250 850,220"/>')
    partes.append(caixa(355, 435, 490, 95, "Cautela obrigatória", ["frequência mínima + concordâncias", "associação lexical não é causalidade"], "#f1e2bd", "#8a6528"))
    partes.append('<path class="seta tracejada" d="M995,280 C995,485 855,485 855,485"/>')
    return documento(
        "Componentes e interpretação da PMI",
        "A frequência do bigrama é comparada às frequências marginais esquerda e direita. O resultado leva a frequência mínima e concordâncias, não diretamente a uma conclusão causal.",
        "".join(partes), 580,
    )


def escolha_grafico():
    partes = [texto(600, 44, ["Comece pela pergunta, não pelo formato"], "titulo")]
    linhas = [
        (105, "Categorias", "Como se distribuem?", "Barras", CORES["azul_claro"], CORES["azul"]),
        (205, "Uma quantitativa", "Como varia?", "Histograma + boxplot", CORES["verde_claro"], CORES["verde"]),
        (305, "Duas quantitativas", "Como covariam?", "Dispersão", CORES["terracota_claro"], CORES["terracota"]),
        (405, "Tempo", "Como muda por período?", "Pontos + linha", CORES["ameixa_claro"], CORES["ameixa"]),
        (505, "Termos", "Quais são frequentes?", "Barras", "#f1e2bd", "#8a6528"),
    ]
    for y, dado, pergunta, grafico, fundo, contorno in linhas:
        partes.append(caixa(45, y, 250, 75, dado, [], fundo, contorno))
        partes.append(caixa(405, y, 330, 75, pergunta, [], CORES["papel"], contorno))
        partes.append(caixa(845, y, 310, 75, grafico, [], fundo, contorno))
        partes.append(f'<path class="seta" d="M300,{y + 38} H395"/>')
        partes.append(f'<path class="seta" d="M740,{y + 38} H835"/>')
    return documento(
        "Escolha de gráficos pela pergunta e pelas variáveis",
        "Cinco linhas ligam tipos de dados e perguntas a barras, histograma e boxplot, dispersão, pontos e linha, ou barras de termos.",
        "".join(partes), 620,
    )


def ciclo_casos():
    partes = [texto(600, 44, ["Leitura distante e leitura próxima se corrigem mutuamente"], "titulo")]
    partes.append(caixa(85, 170, 320, 175, "Agregados", ["frequências • médias", "gráficos • colocações", "padrões candidatos"], CORES["azul_claro"], CORES["azul"]))
    partes.append(caixa(795, 170, 320, 175, "Casos e trechos", ["extremos • exceções", "concordâncias • contexto", "vozes e silêncios"], CORES["terracota_claro"], CORES["terracota"]))
    partes.append('<path class="seta" d="M415,215 C540,115 665,115 785,215"/>')
    partes.append('<path class="seta" d="M785,310 C665,415 540,415 415,310"/>')
    partes.append(texto(600, 125, ["selecionar casos que qualificam o padrão"], "nota"))
    partes.append(texto(600, 455, ["rever categoria, contagem, hipótese e limite"], "nota"))
    return documento(
        "Ciclo entre agregados e casos",
        "Agregados orientam a seleção de casos e trechos; a leitura próxima retorna aos agregados para revisar categorias, contagens, hipóteses e limites.",
        "".join(partes), 520,
    )


def argumento():
    partes = [texto(600, 44, ["Uma figura participa de uma cadeia argumentativa"], "titulo")]
    itens = [
        (60, "Pergunta", ["o que se quer", "descrever?"], CORES["azul_claro"], CORES["azul"]),
        (290, "Tabela", ["valores e", "denominador"], CORES["verde_claro"], CORES["verde"]),
        (520, "Figura", ["escala, unidade", "e casos"], CORES["terracota_claro"], CORES["terracota"]),
        (750, "Leitura", ["descrição +", "interpretação"], CORES["ameixa_claro"], CORES["ameixa"]),
        (980, "Limite", ["o que não", "se conclui"], "#f1e2bd", "#8a6528"),
    ]
    for i, (x, titulo, linhas, fundo, contorno) in enumerate(itens):
        partes.append(caixa(x, 140, 160, 145, titulo, linhas, fundo, contorno))
        if i < len(itens) - 1:
            partes.append(f'<path class="seta" d="M{x + 164},212 H{x + 220}"/>')
    partes.append(texto(600, 365, ["Se a tabela não sustenta a figura, a cadeia precisa ser revista"], "nota"))
    return documento(
        "Cadeia argumentativa de uma visualização",
        "Pergunta, tabela, figura, leitura e limite aparecem em sequência. A legenda afirma que divergências entre tabela e figura exigem revisão.",
        "".join(partes), 430,
    )


def main():
    IMAGENS.mkdir(parents=True, exist_ok=True)
    arquivos = {
        "00_percurso_exploracao.svg": percurso(),
        "00_camadas_escrita.svg": niveis_escrita(),
        "01_tipos_variaveis.svg": tipos_variaveis(),
        "02_fluxo_tokenizacao.svg": tokenizacao(),
        "02_anatomia_pmi.svg": pmi(),
        "03_escolha_grafico.svg": escolha_grafico(),
        "04_ciclo_agregados_casos.svg": ciclo_casos(),
        "04_cadeia_argumento.svg": argumento(),
    }
    for nome, conteudo in arquivos.items():
        (IMAGENS / nome).write_text(conteudo, encoding="utf-8")
    print(f"{len(arquivos)} diagramas SVG construídos em {IMAGENS}")


if __name__ == "__main__":
    main()
