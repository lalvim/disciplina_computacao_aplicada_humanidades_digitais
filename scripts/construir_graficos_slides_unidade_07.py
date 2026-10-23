"""Gera visualizações calculadas para os slides da Unidade 7.

Os SVGs usam apenas a base fictícia da unidade. NumPy e pandas fazem os
cálculos; o arquivo escreve SVG diretamente para tornar a reprodução independente
de bibliotecas gráficas.
"""

from __future__ import annotations

from html import escape
from pathlib import Path

import numpy as np
import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "unidade_07" / "dados" / "municipios_culturais.csv"
OUT = ROOT / "slides" / "imagens" / "unidade_07"

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
        '<style>text{font-family:Aptos,Arial,sans-serif}.title{font-size:28px;font-weight:700;fill:#17324d}.label{font-size:19px;fill:#202a33}.small{font-size:16px;fill:#4b5563}.value{font-size:18px;font-weight:700;fill:#17324d}</style>',
    ]


def save(name: str, lines: list[str]) -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / name).write_text("\n".join(lines + ["</svg>", ""]), encoding="utf-8")


def ols(frame: pd.DataFrame, columns: list[str], response: str):
    x = np.column_stack([np.ones(len(frame)), frame[columns].to_numpy(float)])
    y = frame[response].to_numpy(float)
    beta = np.linalg.lstsq(x, y, rcond=None)[0]
    predicted = x @ beta
    residuals = y - predicted
    r2 = 1 - np.sum(residuals**2) / np.sum((y - y.mean()) ** 2)
    return beta, predicted, residuals, r2, x


def axes(lines: list[str], xmin, xmax, ymin, ymax, xticks, yticks, xlabel, ylabel):
    left, top, width, height = 110, 70, 850, 410

    def sx(value): return left + (value - xmin) / (xmax - xmin) * width
    def sy(value): return top + height - (value - ymin) / (ymax - ymin) * height

    for tick in yticks:
        y = sy(tick)
        lines += [f'<line x1="{left}" y1="{y:.1f}" x2="{left+width}" y2="{y:.1f}" stroke="{LINE}"/>',
                  f'<text x="92" y="{y+6:.1f}" text-anchor="end" class="small">{tick}</text>']
    for tick in xticks:
        x = sx(tick)
        lines += [f'<line x1="{x:.1f}" y1="{top}" x2="{x:.1f}" y2="{top+height}" stroke="{LINE}"/>',
                  f'<text x="{x:.1f}" y="508" text-anchor="middle" class="small">{tick}</text>']
    lines += [f'<line x1="{left}" y1="{top+height}" x2="{left+width}" y2="{top+height}" stroke="{NAVY}" stroke-width="2"/>',
              f'<line x1="{left}" y1="{top}" x2="{left}" y2="{top+height}" stroke="{NAVY}" stroke-width="2"/>',
              f'<text x="535" y="552" text-anchor="middle" class="label">{escape(xlabel)}</text>',
              f'<text x="25" y="275" text-anchor="middle" class="label" transform="rotate(-90 25 275)">{escape(ylabel)}</text>']
    return sx, sy


def simple_regression(data: pd.DataFrame) -> None:
    beta, predicted, _, r2, _ = ols(data, ["renda_pc"], "equipamentos_culturais_100mil")
    lines = svg_open("Renda e equipamentos culturais", "Dispersão de 150 municípios fictícios com reta de regressão linear simples.")
    lines.append('<text x="550" y="38" text-anchor="middle" class="title">A reta resume a tendência; os pontos preservam a variação</text>')
    sx, sy = axes(lines, 1100, 3000, 2, 9, [1200, 1600, 2000, 2400, 2800], [2, 3, 4, 5, 6, 7, 8], "renda per capita simulada", "equipamentos por 100 mil")
    for row in data.itertuples(index=False):
        color = RUST if row.id_municipio == "M150" else TEAL
        radius = 8 if row.id_municipio == "M150" else 4.8
        lines.append(f'<circle cx="{sx(row.renda_pc):.1f}" cy="{sy(row.equipamentos_culturais_100mil):.1f}" r="{radius}" fill="{color}" fill-opacity="0.72" stroke="white"/>')
    x1, x2 = data.renda_pc.min(), data.renda_pc.max()
    lines.append(f'<line x1="{sx(x1):.1f}" y1="{sy(beta[0]+beta[1]*x1):.1f}" x2="{sx(x2):.1f}" y2="{sy(beta[0]+beta[1]*x2):.1f}" stroke="{RUST}" stroke-width="4"/>')
    lines += [f'<text x="975" y="130" class="value">R² = {r2:.2f}</text>',
              '<text x="975" y="166" class="small">+500 de renda</text>',
              f'<text x="975" y="192" class="small">≈ +{beta[1]*500:.2f} equipamento</text>',
              f'<circle cx="982" cy="250" r="7" fill="{RUST}"/><text x="998" y="256" class="small">M150</text>']
    save("01_regressao_simples.svg", lines)


def interaction(data: pd.DataFrame) -> None:
    data = data.copy()
    umean = data.urbanizacao_pct.mean(); emean = data.escolaridade_media_anos.mean()
    data["urbanizacao_c"] = data.urbanizacao_pct - umean
    data["escolaridade_c"] = data.escolaridade_media_anos - emean
    data["interacao"] = data.urbanizacao_c * data.escolaridade_c
    beta, _, _, _, _ = ols(data, ["urbanizacao_c", "escolaridade_c", "interacao"], "equipamentos_culturais_100mil")
    lines = svg_open("Interação entre urbanização e escolaridade", "Três retas mostram que a inclinação de urbanização muda conforme a escolaridade.")
    lines.append('<text x="550" y="38" text-anchor="middle" class="title">Interação: a inclinação depende do contexto</text>')
    sx, sy = axes(lines, 40, 100, 2.5, 6.2, [40, 50, 60, 70, 80, 90, 100], [3, 4, 5, 6], "urbanização (%)", "equipamentos previstos por 100 mil")
    colors = [(8, TEAL), (10, PLUM), (12, RUST)]
    grid = np.linspace(42, 98, 80)
    for schooling, color in colors:
        uc = grid - umean; ec = schooling - emean
        pred = beta[0] + beta[1]*uc + beta[2]*ec + beta[3]*uc*ec
        points = " ".join(f"{sx(x):.1f},{sy(y):.1f}" for x, y in zip(grid, pred))
        lines.append(f'<polyline points="{points}" fill="none" stroke="{color}" stroke-width="4"/>')
    for i, (schooling, color) in enumerate(colors):
        y = 125 + i*42
        lines += [f'<line x1="975" y1="{y}" x2="1020" y2="{y}" stroke="{color}" stroke-width="5"/>',
                  f'<text x="1030" y="{y+6}" class="small">{schooling} anos</text>']
    save("02_interacao.svg", lines)


def diagnostics(data: pd.DataFrame) -> None:
    data = data.copy()
    data["urbanizacao_c"] = data.urbanizacao_pct - data.urbanizacao_pct.mean()
    data["escolaridade_c"] = data.escolaridade_media_anos - data.escolaridade_media_anos.mean()
    data["interacao"] = data.urbanizacao_c * data.escolaridade_c
    _, pred, residual, r2, _ = ols(data, ["urbanizacao_c", "escolaridade_c", "interacao"], "equipamentos_culturais_100mil")
    lines = svg_open("Resíduos em função dos valores previstos", "O caso M150 aparece com resíduo positivo muito maior que os demais.")
    lines.append('<text x="550" y="38" text-anchor="middle" class="title">Diagnóstico devolve o resumo aos casos</text>')
    sx, sy = axes(lines, 2.8, 5.8, -2, 4.5, [3, 3.5, 4, 4.5, 5, 5.5], [-2, -1, 0, 1, 2, 3, 4], "valor previsto", "resíduo = observado − previsto")
    lines.append(f'<line x1="{sx(2.8):.1f}" y1="{sy(0):.1f}" x2="{sx(5.8):.1f}" y2="{sy(0):.1f}" stroke="{NAVY}" stroke-width="3"/>')
    for idx, row in data.iterrows():
        special = row.id_municipio == "M150"
        lines.append(f'<circle cx="{sx(pred[idx]):.1f}" cy="{sy(residual[idx]):.1f}" r="{9 if special else 4.8}" fill="{RUST if special else TEAL}" fill-opacity="0.72" stroke="white"/>')
        if special:
            lines.append(f'<text x="{sx(pred[idx])+16:.1f}" y="{sy(residual[idx])+5:.1f}" class="value">M150: resíduo {residual[idx]:.2f}</text>')
    lines += [f'<text x="975" y="340" class="small">R² com M150: {r2:.2f}</text>',
              '<text x="975" y="370" class="small">inspecionar ≠ excluir</text>']
    save("03_diagnostico_residuos.svg", lines)


def logistic(data: pd.DataFrame) -> None:
    variables = ["renda_pc", "urbanizacao_pct", "escolaridade_media_anos", "distancia_capital_km"]
    means = data[variables].mean(); stds = data[variables].std(ddof=0)
    x = ((data[variables] - means) / stds).to_numpy()
    x = np.column_stack([np.ones(len(data)), x])
    y = (data.biblioteca_publica == "sim").astype(float).to_numpy()
    beta = np.zeros(x.shape[1])
    sigmoid = lambda z: 1 / (1 + np.exp(-np.clip(z, -30, 30)))
    for _ in range(8000):
        beta -= 0.08 * (x.T @ (sigmoid(x @ beta) - y)) / len(y)
    grid = np.linspace(40, 100, 121)
    scenarios = pd.DataFrame({v: np.repeat(means[v], len(grid)) for v in variables})
    scenarios["urbanizacao_pct"] = grid
    z = ((scenarios[variables] - means) / stds).to_numpy()
    probability = sigmoid(np.column_stack([np.ones(len(grid)), z]) @ beta)
    lines = svg_open("Probabilidade prevista de biblioteca", "Curva logística cresce entre urbanização de quarenta e cem por cento, mantendo demais variáveis nas médias.")
    lines.append('<text x="550" y="38" text-anchor="middle" class="title">A regressão logística permanece entre 0 e 1</text>')
    sx, sy = axes(lines, 40, 100, 0, 1, [40, 50, 60, 70, 80, 90, 100], [0, .25, .5, .75, 1], "urbanização (%)", "probabilidade prevista de biblioteca")
    points = " ".join(f"{sx(a):.1f},{sy(b):.1f}" for a, b in zip(grid, probability))
    lines.append(f'<polyline points="{points}" fill="none" stroke="{RUST}" stroke-width="5"/>')
    for urban in [50, 90]:
        p = float(np.interp(urban, grid, probability))
        lines += [f'<line x1="{sx(urban):.1f}" y1="{sy(0):.1f}" x2="{sx(urban):.1f}" y2="{sy(p):.1f}" stroke="{TEAL}" stroke-dasharray="7 6"/>',
                  f'<circle cx="{sx(urban):.1f}" cy="{sy(p):.1f}" r="8" fill="{TEAL}"/>',
                  f'<text x="{sx(urban)+12:.1f}" y="{sy(p)-12:.1f}" class="value">{urban}% → {p:.2f}</text>']
    lines.append('<text x="550" y="580" text-anchor="middle" class="small">Demais variáveis mantidas em suas médias · cenário do modelo, não intervenção causal</text>')
    save("04_curva_logistica.svg", lines)


def standardization(data: pd.DataFrame) -> None:
    mean = data["renda_pc"].mean()
    std = data["renda_pc"].std(ddof=0)
    values = [mean - std, mean, mean + std]
    lines = svg_open(
        "Padronização da renda",
        "Três valores da renda são convertidos para menos um, zero e mais um desvio-padrão.",
    )
    lines.insert(5, f'<defs><marker id="arrow" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L0,6 L9,3 z" fill="{GRAY}"/></marker></defs>')
    lines.append('<text x="550" y="48" text-anchor="middle" class="title">A escala muda; a posição relativa permanece</text>')
    lines += [
        f'<line x1="150" y1="210" x2="950" y2="210" stroke="{NAVY}" stroke-width="4"/>',
        '<text x="550" y="155" text-anchor="middle" class="label">renda per capita simulada</text>',
        f'<line x1="150" y1="420" x2="950" y2="420" stroke="{TEAL}" stroke-width="4"/>',
        '<text x="550" y="365" text-anchor="middle" class="label">escala padronizada z</text>',
    ]
    for pos, value, z in zip([250, 550, 850], values, [-1, 0, 1]):
        value_label = f"{value:,.0f}".replace(",", ".")
        lines += [
            f'<circle cx="{pos}" cy="210" r="12" fill="{RUST}"/>',
            f'<text x="{pos}" y="250" text-anchor="middle" class="value">{value_label}</text>',
            f'<line x1="{pos}" y1="270" x2="{pos}" y2="375" stroke="{GRAY}" stroke-width="2" marker-end="url(#arrow)"/>',
            f'<circle cx="{pos}" cy="420" r="12" fill="{TEAL}"/>',
            f'<text x="{pos}" y="462" text-anchor="middle" class="value">z = {z:+d}</text>',
        ]
    lines.append(f'<text x="550" y="535" text-anchor="middle" class="small">média = {mean:.0f} · desvio-padrão = {std:.0f} · dados fictícios</text>')
    save("05_padronizacao.svg", lines)


def main() -> None:
    data = pd.read_csv(DATA)
    simple_regression(data)
    interaction(data)
    diagnostics(data)
    logistic(data)
    standardization(data)
    print(f"Gráficos gravados em {OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
