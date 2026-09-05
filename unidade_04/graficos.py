"""Gráficos SVG acessíveis e sem dependências externas para a Unidade 4."""

from __future__ import annotations

from html import escape

from IPython.display import SVG


AZUL = "#17324d"
VERDE = "#256b6b"
TERRACOTA = "#a44f32"
AMEIXA = "#69445f"
CINZA = "#53606c"
FUNDO = "#fffdf8"


def _documento(titulo, descricao, corpo, largura=760, altura=430):
    return SVG(
        f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {largura} {altura}"
 role="img" aria-labelledby="titulo descricao">
<title id="titulo">{escape(titulo)}</title>
<desc id="descricao">{escape(descricao)}</desc>
<style>
text {{ font-family: system-ui, sans-serif; fill: {AZUL}; }}
.titulo {{ font-size: 19px; font-weight: 700; }}
.eixo {{ font-size: 13px; }}
.rotulo {{ font-size: 12px; }}
.grade {{ stroke: #c7cfd3; stroke-width: 1; }}
.linha {{ stroke: {AZUL}; stroke-width: 2; fill: none; }}
</style>
<rect width="{largura}" height="{altura}" fill="{FUNDO}"/>
{corpo}
</svg>'''
    )


def _escala(valor, minimo, maximo, inicio, fim):
    return inicio + (valor - minimo) * (fim - inicio) / (maximo - minimo or 1)


def _eixos(titulo, eixo_x, eixo_y, x0=90, y0=350, x1=710, y1=55):
    return "".join(
        [
            f'<text x="{x0}" y="28" class="titulo">{escape(titulo)}</text>',
            f'<path d="M{x0},{y1} V{y0} H{x1}" class="linha"/>',
            f'<text x="{(x0+x1)/2}" y="410" class="eixo" text-anchor="middle">{escape(eixo_x)}</text>',
            f'<text x="20" y="{(y0+y1)/2}" class="eixo" text-anchor="middle" transform="rotate(-90 20 {(y0+y1)/2})">{escape(eixo_y)}</text>',
        ]
    )


def distribuicao_anotada(valores, ids, media, mediana):
    minimo, maximo = min(valores), max(valores)
    corpo = _eixos(
        "Extensão dos documentos: média, mediana e caso extremo",
        "Palavras por documento", "Documentos", y0=260, y1=75,
    )
    for valor, identificador in zip(valores, ids):
        x = _escala(valor, minimo, maximo, 100, 700)
        corpo += f'<circle cx="{x}" cy="180" r="6" fill="{VERDE}" stroke="{AZUL}"/>'
        if identificador == "D023":
            corpo += f'<text x="{x-5}" y="155" class="rotulo" text-anchor="end" font-weight="700">D023</text>'
    for valor, cor, rotulo, y in [
        (media, TERRACOTA, f"média = {media:.1f}", 95),
        (mediana, AMEIXA, f"mediana = {mediana:.1f}", 118),
    ]:
        x = _escala(valor, minimo, maximo, 100, 700)
        corpo += f'<line x1="{x}" y1="75" x2="{x}" y2="250" stroke="{cor}" stroke-width="3" stroke-dasharray="7 5"/>'
        corpo += f'<text x="{x+5}" y="{y}" class="rotulo" fill="{cor}">{escape(rotulo)}</text>'
    for valor in [minimo, 500, 1000, 1500, maximo]:
        x = _escala(valor, minimo, maximo, 100, 700)
        corpo += f'<line x1="{x}" y1="260" x2="{x}" y2="267" class="linha"/><text x="{x}" y="285" class="rotulo" text-anchor="middle">{valor:g}</text>'
    return _documento(
        "Extensão, média e mediana",
        f"Vinte e quatro documentos aparecem sobre um eixo de {minimo:g} a {maximo:g} palavras. A média é {media:.1f}, a mediana {mediana:.1f} e D023, com {maximo:g} palavras, está isolado à direita.",
        corpo, altura=320,
    )


def ttr_duplo(tokens, ttr, ttr_padronizada, tamanho):
    minimo_x, maximo_x = min(tokens), max(tokens)
    corpo = '<text x="50" y="28" class="titulo">Efeito do tamanho textual antes e depois da padronização</text>'
    paineis = [(55, "TTR bruta", ttr, TERRACOTA), (405, f"TTR nos primeiros {tamanho} tokens", ttr_padronizada, VERDE)]
    for x0, titulo, ys, cor in paineis:
        corpo += f'<text x="{x0}" y="62" class="eixo" font-weight="700">{escape(titulo)}</text>'
        corpo += f'<path d="M{x0},80 V330 H{x0+300}" class="linha"/>'
        minimo_y, maximo_y = min(ys), max(ys)
        for x, y in zip(tokens, ys):
            px = _escala(x, minimo_x, maximo_x, x0 + 10, x0 + 290)
            py = _escala(y, minimo_y, maximo_y, 320, 90)
            corpo += f'<circle cx="{px}" cy="{py}" r="5" fill="{cor}" stroke="{AZUL}"/>'
        corpo += f'<text x="{x0+150}" y="375" class="eixo" text-anchor="middle">Tokens no documento</text>'
        corpo += f'<text x="{x0-35}" y="205" class="eixo" text-anchor="middle" transform="rotate(-90 {x0-35} 205)">Razão forma–token</text>'
        for valor in [minimo_x, maximo_x]:
            px = _escala(valor, minimo_x, maximo_x, x0 + 10, x0 + 290)
            corpo += f'<text x="{px}" y="350" class="rotulo" text-anchor="middle">{valor:g}</text>'
    return _documento(
        "Comparação entre TTR bruta e padronizada",
        f"Dois painéis relacionam tamanho e diversidade. O primeiro usa a TTR bruta; o segundo usa os primeiros {tamanho} tokens de cada documento para controlar o tamanho.",
        corpo, altura=400,
    )


def barras_categorias(rotulos, valores, titulo, eixo_x, eixo_y, descricao):
    maximo = max(valores) or 1
    corpo = _eixos(titulo, eixo_x, eixo_y)
    largura = 500 / len(valores)
    for i, (rotulo, valor) in enumerate(zip(rotulos, valores)):
        x = 125 + i * largura
        y = _escala(valor, 0, maximo * 1.15, 350, 65)
        corpo += f'<rect x="{x}" y="{y}" width="{largura-25}" height="{350-y}" fill="{VERDE}" stroke="{AZUL}"/>'
        corpo += f'<text x="{x+(largura-25)/2}" y="{y-8}" class="rotulo" text-anchor="middle">{valor:g}</text>'
        corpo += f'<text x="{x+(largura-25)/2}" y="375" class="rotulo" text-anchor="middle">{escape(str(rotulo))}</text>'
    for valor in range(0, int(maximo) + 1, max(1, int(maximo) // 3)):
        y = _escala(valor, 0, maximo * 1.15, 350, 65)
        corpo += f'<line x1="85" y1="{y}" x2="710" y2="{y}" class="grade"/><text x="78" y="{y+4}" class="rotulo" text-anchor="end">{valor}</text>'
    return _documento(titulo, descricao, corpo)


def histograma_boxplot(valores, limites, ids):
    contagens = [sum(a < v <= b for v in valores) for a, b in zip(limites, limites[1:])]
    minimo, maximo = min(valores), max(valores)
    ordenados = sorted(valores)
    def quantil_linear(p):
        posicao = (len(ordenados) - 1) * p
        inferior = int(posicao)
        superior = min(inferior + 1, len(ordenados) - 1)
        fracao = posicao - inferior
        return ordenados[inferior] + fracao * (ordenados[superior] - ordenados[inferior])

    q1 = quantil_linear(.25)
    mediana = quantil_linear(.5)
    q3 = quantil_linear(.75)
    iqr = q3 - q1
    li, ls = q1 - 1.5 * iqr, q3 + 1.5 * iqr
    validos = [v for v in valores if li <= v <= ls]
    whisker_min, whisker_max = min(validos), max(validos)
    corpo = '<text x="65" y="28" class="titulo">Distribuição e boxplot da extensão</text>'
    corpo += '<path d="M90,55 V245 H710" class="linha"/>'
    for i, contagem in enumerate(contagens):
        x = 115 + i * 110
        y = _escala(contagem, 0, max(contagens) * 1.15, 245, 70)
        corpo += f'<rect x="{x}" y="{y}" width="90" height="{245-y}" fill="#d8ebe7" stroke="{AZUL}"/><text x="{x+45}" y="{y-7}" class="rotulo" text-anchor="middle">{contagem}</text>'
        corpo += f'<text x="{x+45}" y="265" class="rotulo" text-anchor="middle">{limites[i]}–{limites[i+1]}</text>'
    corpo += '<text x="400" y="292" class="eixo" text-anchor="middle">Palavras por documento</text>'
    escala = lambda v: _escala(v, minimo, maximo, 105, 700)
    corpo += f'<line x1="{escala(whisker_min)}" y1="345" x2="{escala(whisker_max)}" y2="345" stroke="{AZUL}" stroke-width="3"/>'
    corpo += f'<rect x="{escala(q1)}" y="320" width="{escala(q3)-escala(q1)}" height="50" fill="#f2ddd2" stroke="{AZUL}" stroke-width="2"/>'
    corpo += f'<line x1="{escala(mediana)}" y1="320" x2="{escala(mediana)}" y2="370" stroke="{AMEIXA}" stroke-width="4"/>'
    for valor, identificador in zip(valores, ids):
        if valor < li or valor > ls:
            x = escala(valor)
            corpo += f'<polygon points="{x},335 {x+8},345 {x},355 {x-8},345" fill="{TERRACOTA}" stroke="{AZUL}"/><text x="{x-10}" y="325" class="rotulo" text-anchor="end" font-weight="700">{escape(identificador)}</text>'
    return _documento(
        "Histograma e boxplot da extensão",
        f"O histograma usa cinco intervalos. O boxplot mostra Q1 {q1:g}, mediana {mediana:g}, Q3 {q3:g}, whiskers de {whisker_min:g} a {whisker_max:g} e D023 separado em {maximo:g} palavras.",
        corpo, altura=410,
    )


def dispersao(xs, ys, grupos, ids, titulo, eixo_x, eixo_y):
    simbolos = {"editorial": "circle", "notícia": "rect", "carta": "polygon"}
    cores = {"editorial": AZUL, "notícia": TERRACOTA, "carta": VERDE}
    minimo_x, maximo_x, minimo_y, maximo_y = min(xs), max(xs), min(ys), max(ys)
    corpo = _eixos(titulo, eixo_x, eixo_y)
    for x, y, grupo, identificador in zip(xs, ys, grupos, ids):
        px = _escala(x, minimo_x, maximo_x, 105, 690)
        py = _escala(y, minimo_y, maximo_y, 335, 70)
        if simbolos[grupo] == "circle":
            corpo += f'<circle cx="{px}" cy="{py}" r="6" fill="{cores[grupo]}"/>'
        elif simbolos[grupo] == "rect":
            corpo += f'<rect x="{px-6}" y="{py-6}" width="12" height="12" fill="{cores[grupo]}"/>'
        else:
            corpo += f'<polygon points="{px},{py-7} {px+7},{py+6} {px-7},{py+6}" fill="{cores[grupo]}"/>'
        if identificador == "D023":
            corpo += f'<text x="{px-8}" y="{py-8}" class="rotulo" text-anchor="end" font-weight="700">D023</text>'
    for valor in range(int(minimo_x), int(maximo_x) + 1):
        px = _escala(valor, minimo_x, maximo_x, 105, 690)
        corpo += f'<text x="{px}" y="372" class="rotulo" text-anchor="middle">{valor}</text>'
    for i, grupo in enumerate(["editorial", "notícia", "carta"]):
        corpo += f'<text x="{510+i*75}" y="48" class="rotulo" fill="{cores[grupo]}">{escape(grupo)}</text>'
    return _documento(
        titulo,
        "Cada ponto representa um documento; círculos são editoriais, quadrados são notícias e triângulos são cartas. D023 é identificado como caso extremo.",
        corpo,
    )


def serie_temporal(anos, valores, ids, medias, ns):
    minimo_x, maximo_x, minimo_y, maximo_y = min(anos), max(anos), min(valores), max(valores)
    corpo = _eixos("Documentos e média anual da extensão", "Ano atribuído", "Palavras por documento")
    pontos_media = []
    for ano, media in medias.items():
        px = _escala(ano, minimo_x, maximo_x, 105, 690)
        py = _escala(media, minimo_y, maximo_y, 335, 70)
        pontos_media.append(f"{px},{py}")
        corpo += f'<text x="{px}" y="{py-10}" class="rotulo" text-anchor="middle">n={ns[ano]}</text>'
    corpo += f'<polyline points="{" ".join(pontos_media)}" fill="none" stroke="{TERRACOTA}" stroke-width="3"/>'
    for ano, valor, identificador in zip(anos, valores, ids):
        px = _escala(ano, minimo_x, maximo_x, 105, 690)
        py = _escala(valor, minimo_y, maximo_y, 335, 70)
        corpo += f'<path d="M{px-5},{py-5} L{px+5},{py+5} M{px-5},{py+5} L{px+5},{py-5}" stroke="{CINZA}" stroke-width="2"/>'
        if identificador == "D023":
            corpo += f'<text x="{px-8}" y="{py+20}" class="rotulo" text-anchor="end" font-weight="700">D023</text>'
    for ano, media in medias.items():
        px = _escala(ano, minimo_x, maximo_x, 105, 690)
        py = _escala(media, minimo_y, maximo_y, 335, 70)
        corpo += f'<circle cx="{px}" cy="{py}" r="5" fill="{TERRACOTA}"/>'
        corpo += f'<text x="{px}" y="372" class="rotulo" text-anchor="middle">{ano}</text>'
    return _documento(
        "Série temporal com observações e médias",
        "Cruzes representam dois documentos em cada ano; círculos unidos representam médias anuais. D023 aparece em 1900 e eleva fortemente a média desse ano.",
        corpo,
    )


def barras_horizontais(rotulos, valores, titulo, descricao):
    maximo = max(valores) or 1
    corpo = f'<text x="75" y="28" class="titulo">{escape(titulo)}</text>'
    for i, (rotulo, valor) in enumerate(zip(rotulos, valores)):
        y = 55 + i * 34
        largura = 500 * valor / maximo
        corpo += f'<text x="120" y="{y+17}" class="rotulo" text-anchor="end">{escape(str(rotulo))}</text>'
        corpo += f'<rect x="135" y="{y}" width="{largura}" height="22" fill="{AMEIXA}" stroke="{AZUL}"/>'
        corpo += f'<text x="{145+largura}" y="{y+17}" class="rotulo">{valor:g}</text>'
    corpo += '<text x="390" y="410" class="eixo" text-anchor="middle">Frequência absoluta</text>'
    return _documento(titulo, descricao, corpo, altura=430)
