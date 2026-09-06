"""Gráficos SVG pequenos, acessíveis e sem dependência gráfica externa."""

from html import escape
from IPython.display import SVG


def _doc(titulo, descricao, corpo, altura=420):
    return SVG(f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 {altura}"
 role="img" aria-labelledby="t d"><title id="t">{escape(titulo)}</title>
 <desc id="d">{escape(descricao)}</desc><style>
 text{{font-family:system-ui;fill:#17324d}} .e{{stroke:#17324d;stroke-width:2}}
 .a{{fill:#dbe8ec;stroke:#17324d}} .b{{fill:#d8ebe7;stroke:#256b6b}}
 </style><rect width="900" height="{altura}" fill="#fffdf8"/>{corpo}</svg>''')


def estimativas_grupos(valores_a, valores_b, nome_a="A", nome_b="B"):
    todos = list(valores_a) + list(valores_b)
    minimo, maximo = min(todos), max(todos)
    escala = lambda v: 110 + 680 * (v - minimo) / (maximo - minimo or 1)
    partes = ['<text x="450" y="32" text-anchor="middle" font-size="22" font-weight="700">Distribuições e médias dos grupos</text>']
    for y, valores, nome, classe in [(135, valores_a, nome_a, "a"), (280, valores_b, nome_b, "b")]:
        partes.append(f'<text x="55" y="{y+5}" font-size="17">{escape(nome)}</text>')
        partes.append(f'<line x1="110" y1="{y}" x2="790" y2="{y}" class="e"/>')
        for i, valor in enumerate(valores):
            partes.append(f'<circle cx="{escala(valor):.1f}" cy="{y+(i%3-1)*16}" r="7" class="{classe}"/>')
        media = sum(valores) / len(valores)
        partes.append(f'<line x1="{escala(media):.1f}" y1="{y-48}" x2="{escala(media):.1f}" y2="{y+48}" stroke="#7b3545" stroke-width="4"/>')
    partes.append(f'<text x="110" y="370" font-size="14">{minimo:.0f}</text><text x="790" y="370" text-anchor="end" font-size="14">{maximo:.0f}</text>')
    desc = f"Pontos dos grupos {nome_a} e {nome_b}; linhas verticais marcam as médias. Valores também são exibidos em tabela no notebook."
    return _doc("Distribuições e médias dos grupos", desc, "".join(partes), 400)


def histograma_referencia(valores, observado, titulo="Distribuição de referência"):
    minimo, maximo = min(valores), max(valores)
    n = 24
    largura = (maximo - minimo) / n or 1
    contagens = [0] * n
    for v in valores:
        i = min(int((v - minimo) / largura), n - 1)
        contagens[i] += 1
    topo = max(contagens) or 1
    partes = [f'<text x="450" y="30" text-anchor="middle" font-size="22" font-weight="700">{escape(titulo)}</text>']
    for i, q in enumerate(contagens):
        h = 260 * q / topo
        x = 90 + i * 30
        partes.append(f'<rect x="{x}" y="{340-h}" width="26" height="{h}" fill="#dbe8ec" stroke="#17324d"/>')
    xobs = 90 + 720 * (observado - minimo) / (maximo - minimo or 1)
    partes.append(f'<line x1="{xobs:.1f}" y1="55" x2="{xobs:.1f}" y2="350" stroke="#7b3545" stroke-width="4"/>')
    partes.append(f'<text x="{xobs:.1f}" y="48" text-anchor="middle" font-size="14">observado</text>')
    partes.append('<line x1="90" y1="340" x2="810" y2="340" class="e"/>')
    desc = f"Histograma de {len(valores)} resultados simulados; linha vertical marca o resultado observado {observado:.2f}."
    return _doc(titulo, desc, "".join(partes), 390)


def mapa_calor(matriz, titulo="Matriz documento-termo"):
    valores = matriz.to_numpy(dtype=float)
    maximo = valores.max() or 1
    celula = min(54, 650 / max(len(matriz.columns), 1))
    esquerda, topo = 180, 85
    partes = [f'<text x="450" y="30" text-anchor="middle" font-size="22" font-weight="700">{escape(titulo)}</text>']
    for j, col in enumerate(matriz.columns):
        partes.append(f'<text x="{esquerda+j*celula+celula/2}" y="70" text-anchor="middle" font-size="11" transform="rotate(-35 {esquerda+j*celula+celula/2} 70)">{escape(str(col))}</text>')
    for i, idx in enumerate(matriz.index):
        partes.append(f'<text x="{esquerda-12}" y="{topo+i*celula+celula*0.65}" text-anchor="end" font-size="12">{escape(str(idx))}</text>')
        for j, v in enumerate(valores[i]):
            op = 0.08 + 0.82 * v / maximo
            partes.append(f'<rect x="{esquerda+j*celula}" y="{topo+i*celula}" width="{celula-2}" height="{celula-2}" fill="#256b6b" fill-opacity="{op:.2f}" stroke="#17324d"/>')
    altura = int(topo + len(matriz) * celula + 45)
    desc = f"Mapa de calor com {len(matriz)} documentos e {len(matriz.columns)} termos; valores exatos aparecem na tabela equivalente."
    return _doc(titulo, desc, "".join(partes), max(320, altura))
