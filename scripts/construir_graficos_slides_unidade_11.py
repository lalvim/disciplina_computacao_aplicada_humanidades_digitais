"""Gera visualizações calculadas para os slides da Unidade 11.

Os dados temporais e espaciais são inteiramente fictícios. A grade territorial
não corresponde a nenhum lugar real.
"""

from __future__ import annotations

from html import escape
from pathlib import Path

import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "unidade_11" / "dados"
OUT = ROOT / "slides" / "imagens" / "unidade_11"
NAVY, TEAL, RUST, PLUM = "#17324d", "#176b68", "#a84f2a", "#69445f"
GRAY, LINE, PAPER, PALE = "#4b5563", "#d8cdbb", "#fffdf7", "#f2eee5"


def open_svg(title: str, description: str) -> list[str]:
    return [
        '<svg xmlns="http://www.w3.org/2000/svg" width="1100" height="590" viewBox="0 0 1100 590" role="img">',
        f"<title>{escape(title)}</title>", f"<desc>{escape(description)}</desc>",
        f'<rect width="1100" height="590" fill="{PAPER}"/>',
        '<style>text{font-family:Aptos,Arial,sans-serif}.title{font-size:28px;font-weight:700;fill:#17324d}.label{font-size:19px;fill:#202a33}.small{font-size:16px;fill:#4b5563}.value{font-size:20px;font-weight:700;fill:#17324d}</style>',
    ]


def save(name: str, lines: list[str]) -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / name).write_text("\n".join(lines + ["</svg>", ""]), encoding="utf-8")


def polyline(values, years, left, top, width, height, ymin, ymax, color, stroke=4):
    x = lambda year: left + (year - min(years)) / (max(years) - min(years)) * width
    y = lambda value: top + height - (value - ymin) / (ymax - ymin) * height
    points = " ".join(f"{x(year):.1f},{y(value):.1f}" for year, value in zip(years, values) if pd.notna(value))
    return f'<polyline points="{points}" fill="none" stroke="{color}" stroke-width="{stroke}" stroke-linejoin="round"/>'


def series_count_rate(data: pd.DataFrame) -> None:
    lines = open_svg("Contagem e taxa no tempo", "Dois painéis mostram eventos e taxa por cem mil habitantes, com ruptura de definição em 1990.")
    lines.append('<text x="550" y="38" text-anchor="middle" class="title">A curva muda quando a medida e a definição mudam</text>')
    years = data.ano.tolist()
    for left, values, title, color, ymin, ymax in [
        (75, data.eventos, "Contagem de eventos", RUST, 0, 90),
        (600, data.taxa_100mil, "Taxa por 100 mil", TEAL, 20, 80),
    ]:
        top, width, height = 100, 420, 350
        lines += [f'<rect x="{left}" y="{top}" width="{width}" height="{height}" fill="{PALE}" stroke="{LINE}"/>',
                  f'<text x="{left+width/2}" y="78" text-anchor="middle" class="value">{title}</text>',
                  polyline(values, years, left, top, width, height, ymin, ymax, color)]
        xr = left + (1990 - 1960) / 60 * width
        lines += [f'<line x1="{xr}" y1="{top}" x2="{xr}" y2="{top+height}" stroke="{NAVY}" stroke-width="3" stroke-dasharray="8 6"/>',
                  f'<text x="{xr+8}" y="{top+24}" class="small">1990</text>']
        for year in [1960, 1980, 2000, 2020]:
            x = left + (year - 1960) / 60 * width
            lines.append(f'<text x="{x}" y="480" text-anchor="middle" class="small">{year}</text>')
    lines += ['<text x="550" y="525" text-anchor="middle" class="label">linha tracejada = definição ampliada do registro</text>',
              '<text x="550" y="558" text-anchor="middle" class="small">O salto observado combina processo substantivo, população e mudança administrativa.</text>']
    save("01_contagem_taxa_ruptura.svg", lines)


def moving_windows(data: pd.DataFrame) -> None:
    data = data.copy()
    data["media_3"] = data.taxa_100mil.rolling(3, center=True).mean()
    data["media_9"] = data.taxa_100mil.rolling(9, center=True).mean()
    years = data.ano.tolist(); left, top, width, height = 100, 90, 880, 380
    lines = open_svg("Médias móveis com janelas de três e nove anos", "A janela curta acompanha oscilações; a longa produz uma curva mais suave e perde mais anos nas bordas.")
    lines += ['<text x="550" y="38" text-anchor="middle" class="title">A janela decide quanto detalhe permanece visível</text>',
              f'<rect x="{left}" y="{top}" width="{width}" height="{height}" fill="{PALE}" stroke="{LINE}"/>',
              polyline(data.taxa_100mil, years, left, top, width, height, 25, 75, GRAY, 2),
              polyline(data.media_3, years, left, top, width, height, 25, 75, TEAL, 5),
              polyline(data.media_9, years, left, top, width, height, 25, 75, RUST, 5)]
    xr = left + (1990 - 1960) / 60 * width
    lines += [f'<line x1="{xr}" y1="{top}" x2="{xr}" y2="{top+height}" stroke="{NAVY}" stroke-width="3" stroke-dasharray="8 6"/>']
    for year in [1960, 1970, 1980, 1990, 2000, 2010, 2020]:
        x = left + (year - 1960) / 60 * width
        lines.append(f'<text x="{x}" y="500" text-anchor="middle" class="small">{year}</text>')
    lines += [f'<line x1="180" y1="535" x2="225" y2="535" stroke="{GRAY}" stroke-width="2"/><text x="235" y="541" class="small">taxa anual</text>',
              f'<line x1="405" y1="535" x2="450" y2="535" stroke="{TEAL}" stroke-width="5"/><text x="460" y="541" class="small">janela 3</text>',
              f'<line x1="630" y1="535" x2="675" y2="535" stroke="{RUST}" stroke-width="5"/><text x="685" y="541" class="small">janela 9</text>',
              '<text x="550" y="574" text-anchor="middle" class="small">A suavização descreve a série; não identifica a causa da mudança.</text>']
    save("02_medias_moveis.svg", lines)


def textual_time(data: pd.DataFrame) -> None:
    data = data.copy()
    for term in ["patrimonio", "digital"]:
        data[f"taxa_{term}"] = 100 * data[f"mencoes_{term}"] / data.documentos
        data[f"media_{term}"] = data[f"taxa_{term}"].rolling(5, center=True).mean()
    years = data.ano.tolist(); left, top, width, height = 100, 90, 880, 380
    lines = open_svg("Menções normalizadas ao longo do tempo", "Curvas mostram médias móveis de menções de patrimônio e digital por cem documentos.")
    lines += ['<text x="550" y="38" text-anchor="middle" class="title">Normalizar o volume não resolve a mudança de significado</text>',
              f'<rect x="{left}" y="{top}" width="{width}" height="{height}" fill="{PALE}" stroke="{LINE}"/>',
              polyline(data.media_patrimonio, years, left, top, width, height, 0, 45, TEAL, 5),
              polyline(data.media_digital, years, left, top, width, height, 0, 45, RUST, 5)]
    for tick in [0, 15, 30, 45]:
        y = top + height - tick / 45 * height
        lines += [f'<line x1="{left}" y1="{y}" x2="{left+width}" y2="{y}" stroke="{LINE}"/>',
                  f'<text x="82" y="{y+5}" text-anchor="end" class="small">{tick}</text>']
    for year in [1960, 1970, 1980, 1990, 2000, 2010, 2020]:
        x = left + (year - 1960) / 60 * width
        lines.append(f'<text x="{x}" y="500" text-anchor="middle" class="small">{year}</text>')
    lines += [f'<line x1="300" y1="535" x2="345" y2="535" stroke="{TEAL}" stroke-width="5"/><text x="355" y="541" class="small">patrimônio</text>',
              f'<line x1="595" y1="535" x2="640" y2="535" stroke="{RUST}" stroke-width="5"/><text x="650" y="541" class="small">digital</text>',
              '<text x="550" y="575" text-anchor="middle" class="small">menções por 100 documentos · média móvel centrada de 5 anos</text>']
    save("03_termos_no_tempo.svg", lines)


def color(value: float, low: float, high: float) -> str:
    ratio = 0 if high == low else (value - low) / (high - low)
    a = (242, 238, 229); b = (23, 107, 104)
    rgb = tuple(round(x + ratio * (y - x)) for x, y in zip(a, b))
    return "#%02x%02x%02x" % rgb


def spatial_maps(data: pd.DataFrame) -> None:
    data = data.copy(); data["taxa"] = 100000 * data.ocorrencias / data.populacao
    lines = open_svg("Contagem e taxa em uma grade territorial", "Duas grades comparam ocorrências e taxas por cem mil; T16 lidera em contagem e T13 em taxa.")
    lines.append('<text x="550" y="38" text-anchor="middle" class="title">Trocar o denominador altera a geografia aparente</text>')
    for panel_x, column, title, suffix in [(120, "ocorrencias", "Contagem", ""), (640, "taxa", "Taxa por 100 mil", "")]:
        values = data[column]; low, high = values.min(), values.max(); size = 92
        lines.append(f'<text x="{panel_x+184}" y="85" text-anchor="middle" class="value">{title}</text>')
        for _, row in data.iterrows():
            x = panel_x + int(row.x) * size; y = 440 - int(row.y) * size
            fill = color(row[column], low, high)
            text_color = "white" if (row[column]-low)/(high-low) > .55 else NAVY
            value = f'{row[column]:.0f}'
            lines += [f'<rect x="{x}" y="{y}" width="{size}" height="{size}" fill="{fill}" stroke="white" stroke-width="4"/>',
                      f'<text x="{x+size/2}" y="{y+39}" text-anchor="middle" font-size="18" font-weight="700" fill="{text_color}">{row.codigo}</text>',
                      f'<text x="{x+size/2}" y="{y+66}" text-anchor="middle" font-size="16" fill="{text_color}">{value}</text>']
    lines += ['<text x="304" y="525" text-anchor="middle" class="label">máximo: T16 = 86</text>',
              '<text x="824" y="525" text-anchor="middle" class="label">máximo: T13 = 344</text>',
              '<text x="550" y="570" text-anchor="middle" class="small">Grade abstrata 4 × 4 — não representa território real</text>']
    save("04_contagem_e_taxa_espacial.svg", lines)


def aggregation_problem(data: pd.DataFrame) -> None:
    data = data.copy(); data["taxa"] = 100000 * data.ocorrencias / data.populacao
    data["linha"] = data.y.map(lambda y: f"linha {int(y)+1}")
    data["quadrante"] = data.apply(lambda r: ("norte" if r.y >= 2 else "sul") + "-" + ("leste" if r.x >= 2 else "oeste"), axis=1)
    def aggregate(col):
        a = data.groupby(col).agg(ocorrencias=("ocorrencias", "sum"), populacao=("populacao", "sum"))
        return (100000 * a.ocorrencias / a.populacao).sort_values()
    rows, quads = aggregate("linha"), aggregate("quadrante")
    lines = open_svg("Efeito de duas agregações territoriais", "Barras comparam taxas agregadas por linhas e quadrantes da mesma grade.")
    lines.append('<text x="550" y="38" text-anchor="middle" class="title">As mesmas células formam padrões diferentes quando as fronteiras mudam</text>')
    for left, values, title, color_name in [(95, rows, "Agregação por linhas", TEAL), (615, quads, "Agregação por quadrantes", RUST)]:
        lines.append(f'<text x="{left+190}" y="85" text-anchor="middle" class="value">{title}</text>')
        for i, (label, value) in enumerate(values.items()):
            y = 120 + i * 95; width = (value - 200) / 160 * 360
            lines += [f'<text x="{left}" y="{y+29}" class="small">{escape(label)}</text>',
                      f'<rect x="{left+115}" y="{y}" width="{max(width,8):.1f}" height="48" rx="6" fill="{color_name}"/>',
                      f'<text x="{left+125+max(width,8):.1f}" y="{y+31}" class="small">{value:.1f}</text>']
    lines += ['<text x="550" y="530" text-anchor="middle" class="label">agrupar não apenas resume: também redefine vizinhanças e contrastes</text>',
              '<text x="550" y="567" text-anchor="middle" class="small">Exemplo de MAUP em grade fictícia; não infira características individuais.</text>']
    save("05_agregacoes_maup.svg", lines)


def main() -> None:
    series = pd.read_csv(DATA / "serie_cultural.csv")
    terms = pd.read_csv(DATA / "termos_por_ano.csv")
    territories = pd.read_csv(DATA / "territorios.csv")
    series_count_rate(series)
    moving_windows(series)
    textual_time(terms)
    spatial_maps(territories)
    aggregation_problem(territories)
    print(f"Gráficos gravados em {OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
