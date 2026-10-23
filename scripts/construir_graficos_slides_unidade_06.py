"""Gera visualizações calculadas usadas nos slides da Unidade 6.

Os SVGs são derivados exclusivamente das bases fictícias da unidade. O script
evita dependência de bibliotecas de renderização: pandas faz os cálculos e o
próprio programa escreve SVG acessível e reproduzível.
"""

from __future__ import annotations

from html import escape
from pathlib import Path

import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "unidade_06" / "dados"
OUT = ROOT / "slides" / "imagens" / "unidade_06"

NAVY = "#17324d"
TEAL = "#176b68"
RUST = "#a84f2a"
PLUM = "#69445f"
GRAY = "#4b5563"
LINE = "#d8cdbb"
PAPER = "#fffdf7"


def svg_open(title: str, description: str) -> list[str]:
    return [
        '<svg xmlns="http://www.w3.org/2000/svg" width="1100" height="590" viewBox="0 0 1100 590" role="img">',
        f"<title>{escape(title)}</title>",
        f"<desc>{escape(description)}</desc>",
        f'<rect width="1100" height="590" fill="{PAPER}"/>',
        '<style>text{font-family:Aptos,Arial,sans-serif}.title{font-size:28px;font-weight:700;fill:#17324d}.label{font-size:20px;fill:#202a33}.small{font-size:16px;fill:#4b5563}.value{font-size:19px;font-weight:700;fill:#17324d}</style>',
    ]


def save(name: str, lines: list[str]) -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / name).write_text("\n".join(lines + ["</svg>", ""]), encoding="utf-8")


def categorical_chart(df: pd.DataFrame) -> None:
    tab = pd.crosstab(df["periodo"], df["tema_educacao"])
    pct = tab.div(tab.sum(axis=1), axis=0) * 100
    lines = svg_open(
        "Proporção de documentos com tema educação por período",
        "Duas barras de cem por cento com 32,5 por cento no primeiro período e 62,5 no segundo.",
    )
    lines.append('<text x="550" y="48" text-anchor="middle" class="title">O denominador muda a leitura</text>')
    x0, width = 245, 700
    for i, period in enumerate(tab.index):
        y = 135 + i * 165
        yes = float(pct.loc[period, "sim"])
        no = 100 - yes
        yes_w = width * yes / 100
        lines += [
            f'<text x="220" y="{y + 37}" text-anchor="end" class="label">{escape(str(period))}</text>',
            f'<rect x="{x0}" y="{y}" width="{width}" height="62" rx="6" fill="#e7e0d4"/>',
            f'<rect x="{x0}" y="{y}" width="{yes_w:.1f}" height="62" rx="6" fill="{TEAL}"/>',
            f'<text x="{x0 + yes_w / 2:.1f}" y="{y + 39}" text-anchor="middle" fill="white" font-size="20" font-weight="700">sim: {yes:.1f}%</text>',
            f'<text x="{x0 + yes_w + (width - yes_w) / 2:.1f}" y="{y + 39}" text-anchor="middle" class="value">não: {no:.1f}%</text>',
            f'<text x="{x0}" y="{y + 91}" class="small">n = {int(tab.loc[period].sum())} documentos</text>',
        ]
    lines += [
        f'<rect x="245" y="485" width="22" height="22" fill="{TEAL}"/><text x="279" y="503" class="small">tema educação = sim</text>',
        '<rect x="510" y="485" width="22" height="22" fill="#e7e0d4"/><text x="544" y="503" class="small">tema educação = não</text>',
        '<text x="550" y="550" text-anchor="middle" class="small">Fonte: registros_associacao.csv · dados inteiramente fictícios</text>',
    ]
    save("01_proporcao_tema_periodo.svg", lines)


def scatter_chart(df: pd.DataFrame) -> None:
    x = df["extensao_palavras"]
    y = df["referencias_instituicoes"]
    xmin, xmax = 200, 650
    ymin, ymax = -0.3, 6.3
    left, top, width, height = 115, 75, 830, 405

    def sx(v: float) -> float:
        return left + (v - xmin) / (xmax - xmin) * width

    def sy(v: float) -> float:
        return top + height - (v - ymin) / (ymax - ymin) * height

    lines = svg_open(
        "Extensão e referências institucionais por local",
        "Diagrama de dispersão com oitenta documentos, distinguindo Capital e Interior.",
    )
    lines.append('<text x="550" y="42" text-anchor="middle" class="title">O coeficiente resume uma nuvem, não a substitui</text>')
    for tick in range(0, 7):
        yy = sy(tick)
        lines += [
            f'<line x1="{left}" y1="{yy:.1f}" x2="{left+width}" y2="{yy:.1f}" stroke="{LINE}"/>',
            f'<text x="95" y="{yy+6:.1f}" text-anchor="end" class="small">{tick}</text>',
        ]
    for tick in [200, 300, 400, 500, 600]:
        xx = sx(tick)
        lines += [
            f'<line x1="{xx:.1f}" y1="{top}" x2="{xx:.1f}" y2="{top+height}" stroke="{LINE}"/>',
            f'<text x="{xx:.1f}" y="510" text-anchor="middle" class="small">{tick}</text>',
        ]
    for _, row in df.iterrows():
        color = TEAL if row["local"] == "Capital" else RUST
        lines.append(f'<circle cx="{sx(row["extensao_palavras"]):.1f}" cy="{sy(row["referencias_instituicoes"]):.1f}" r="5.5" fill="{color}" fill-opacity="0.72" stroke="white"/>')
    lines += [
        f'<line x1="{left}" y1="{top+height}" x2="{left+width}" y2="{top+height}" stroke="{NAVY}" stroke-width="2"/>',
        f'<line x1="{left}" y1="{top}" x2="{left}" y2="{top+height}" stroke="{NAVY}" stroke-width="2"/>',
        '<text x="530" y="552" text-anchor="middle" class="label">extensão (palavras por documento)</text>',
        '<text x="26" y="280" text-anchor="middle" class="label" transform="rotate(-90 26 280)">referências institucionais</text>',
        f'<circle cx="975" cy="130" r="7" fill="{TEAL}"/><text x="992" y="136" class="small">Capital</text>',
        f'<circle cx="975" cy="166" r="7" fill="{RUST}"/><text x="992" y="172" class="small">Interior</text>',
        '<text x="970" y="240" class="value">r global = 0,53</text>',
        '<text x="970" y="276" class="small">Capital: 0,37</text>',
        '<text x="970" y="306" class="small">Interior: 0,61</text>',
        '<text x="970" y="370" class="small">Correlação não</text>',
        '<text x="970" y="395" class="small">demonstra causa.</text>',
    ]
    save("02_dispersao_estratificada.svg", lines)


def network_chart() -> None:
    edges = pd.read_csv(DATA / "arestas_coocorrencia.csv")
    nodes = sorted(set(edges["origem"]) | set(edges["destino"]))
    # Posições fixas: o desenho é reprodutível e não sugere coordenadas históricas.
    pos = {
        "Jornal Horizonte": (535, 260), "Biblioteca Popular": (330, 205),
        "Liga Aurora": (720, 190), "Escola Livre": (665, 370),
        "Círculo Sul": (405, 405), "Teatro União": (210, 365),
        "Sindicato Norte": (865, 330), "Cooperativa Leste": (195, 125),
        "Ana F.": (490, 95), "Bento R.": (810, 90), "Caio M.": (970, 205),
        "Dora S.": (145, 485), "Eva L.": (520, 500), "Fábio C.": (890, 485),
    }
    strength = {node: 0 for node in nodes}
    for row in edges.itertuples(index=False):
        strength[row.origem] += row.peso
        strength[row.destino] += row.peso
    lines = svg_open(
        "Rede projetada de coocorrência",
        "Rede de quatorze entidades e quarenta e duas arestas; espessura representa coocorrências.",
    )
    lines.append('<text x="550" y="38" text-anchor="middle" class="title">Uma projeção torna relações visíveis — e perde contexto</text>')
    for row in edges.itertuples(index=False):
        x1, y1 = pos[row.origem]; x2, y2 = pos[row.destino]
        lines.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="#9ba7ad" stroke-width="{0.8 + row.peso*0.8:.1f}" stroke-opacity="0.55"/>')
    for node in nodes:
        x, y = pos[node]
        radius = 12 + strength[node] * 0.75
        color = RUST if node == "Jornal Horizonte" else (TEAL if " " in node and node.split()[0] not in {"Ana", "Bento", "Caio", "Dora", "Eva", "Fábio"} else PLUM)
        lines += [
            f'<circle cx="{x}" cy="{y}" r="{radius:.1f}" fill="{color}" fill-opacity="0.9" stroke="white" stroke-width="2"/>',
            f'<text x="{x}" y="{y + radius + 18:.1f}" text-anchor="middle" class="small">{escape(node)}</text>',
        ]
    lines += [
        '<text x="840" y="555" class="small">nó maior = maior força (soma dos pesos)</text>',
        '<text x="65" y="555" class="small">posição = recurso visual, não localização geográfica</text>',
    ]
    save("03_rede_coocorrencia.svg", lines)


def main() -> None:
    df = pd.read_csv(DATA / "registros_associacao.csv")
    categorical_chart(df)
    scatter_chart(df)
    network_chart()
    print(f"Gráficos gravados em {OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
