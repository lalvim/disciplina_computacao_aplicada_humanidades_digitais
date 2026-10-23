"""Gera visualizações calculadas para os slides da Unidade 13.

Requer pandas, NumPy e scikit-learn. Todos os dados são fictícios e foram
construídos para auditoria didática de validade, robustez e vieses.
"""

from __future__ import annotations

from html import escape
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.metrics import accuracy_score, confusion_matrix, f1_score, precision_score, recall_score


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "unidade_13" / "dados"
OUT = ROOT / "slides" / "imagens" / "unidade_13"
NAVY, TEAL, RUST, PLUM = "#17324d", "#176b68", "#a84f2a", "#69445f"
GRAY, LINE, PAPER, PALE = "#4b5563", "#d8cdbb", "#fffdf7", "#f2eee5"


def open_svg(title: str, description: str) -> list[str]:
    return [
        '<svg xmlns="http://www.w3.org/2000/svg" width="1100" height="590" viewBox="0 0 1100 590" role="img">',
        f"<title>{escape(title)}</title>", f"<desc>{escape(description)}</desc>",
        f'<rect width="1100" height="590" fill="{PAPER}"/>',
        '<style>text{font-family:Aptos,Arial,sans-serif}.title{font-size:28px;font-weight:700;fill:#17324d}.label{font-size:19px;fill:#202a33}.small{font-size:16px;fill:#4b5563}.value{font-size:21px;font-weight:700;fill:#17324d}</style>',
    ]


def save(name: str, lines: list[str]) -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / name).write_text("\n".join(lines + ["</svg>", ""]), encoding="utf-8")


def metrics(y, pred) -> dict[str, float]:
    return {
        "Acurácia": accuracy_score(y, pred),
        "Precisão": precision_score(y, pred, zero_division=0),
        "Revocação": recall_score(y, pred, zero_division=0),
        "F1": f1_score(y, pred, zero_division=0),
    }


def baseline_model(data: pd.DataFrame) -> None:
    baseline = np.zeros(len(data), dtype=int)
    values = {"Maioria (classe 0)": metrics(data.classe_ouro, baseline),
              "Modelo": metrics(data.classe_ouro, data.classe_prevista)}
    lines = open_svg("Baseline e modelo em quatro métricas", "Barras mostram baseline com acurácia 0,5 e F1 zero, e modelo com métricas próximas de 0,70.")
    lines.append('<text x="550" y="38" text-anchor="middle" class="title">O modelo supera o baseline — mas a métrica escolhida muda a escala</text>')
    left, top, width = 170, 100, 760
    for tick in [0, .25, .5, .75, 1]:
        x = left + tick * width
        lines += [f'<line x1="{x}" y1="{top}" x2="{x}" y2="480" stroke="{LINE}"/>',
                  f'<text x="{x}" y="512" text-anchor="middle" class="small">{tick:.2f}</text>']
    for i, metric in enumerate(["Acurácia", "Precisão", "Revocação", "F1"]):
        y = 120 + i * 88
        lines.append(f'<text x="150" y="{y+34}" text-anchor="end" class="label">{metric}</text>')
        for j, (method, color) in enumerate([("Maioria (classe 0)", GRAY), ("Modelo", TEAL)]):
            value = values[method][metric]; yy = y + j * 31; bar = value * width
            lines += [f'<rect x="{left}" y="{yy}" width="{max(bar,2):.1f}" height="25" rx="4" fill="{color}"/>',
                      f'<text x="{left+max(bar,2)+10:.1f}" y="{yy+19}" class="small">{value:.3f}</text>']
    lines += [f'<rect x="275" y="540" width="24" height="16" fill="{GRAY}"/><text x="310" y="554" class="small">baseline</text>',
              f'<rect x="510" y="540" width="24" height="16" fill="{TEAL}"/><text x="545" y="554" class="small">modelo</text>',
              '<text x="815" y="554" text-anchor="middle" class="small">n = 240 · classes balanceadas</text>']
    save("01_baseline_modelo.svg", lines)


def confusion(data: pd.DataFrame) -> None:
    matrix = confusion_matrix(data.classe_ouro, data.classe_prevista)
    lines = open_svg("Matriz de confusão da auditoria", "Matriz mostra 84 verdadeiros negativos, 36 falsos positivos, 37 falsos negativos e 83 verdadeiros positivos.")
    lines.append('<text x="550" y="38" text-anchor="middle" class="title">A acurácia de 0,696 contém 73 erros diferentes</text>')
    x0, y0, size = 355, 145, 190
    colors = [[TEAL, RUST], [PLUM, TEAL]]
    labels = [["VN", "FP"], ["FN", "VP"]]
    for i in range(2):
        for j in range(2):
            x, y = x0+j*size, y0+i*size
            lines += [f'<rect x="{x}" y="{y}" width="{size}" height="{size}" fill="{colors[i][j]}" fill-opacity=".82" stroke="white" stroke-width="5"/>',
                      f'<text x="{x+size/2}" y="{y+82}" text-anchor="middle" font-size="25" font-weight="700" fill="white">{labels[i][j]}</text>',
                      f'<text x="{x+size/2}" y="{y+130}" text-anchor="middle" font-size="40" font-weight="700" fill="white">{matrix[i,j]}</text>']
    lines += ['<text x="545" y="115" text-anchor="middle" class="label">classe prevista</text>',
              '<text x="315" y="335" text-anchor="middle" class="label" transform="rotate(-90 315 335)">classe de referência</text>',
              '<text x="450" y="555" text-anchor="middle" class="small">prevê 0</text>',
              '<text x="640" y="555" text-anchor="middle" class="small">prevê 1</text>']
    save("02_matriz_confusao.svg", lines)


def sensitivity(values: pd.DataFrame) -> None:
    values = values.sort_values("f1")
    lines = open_svg("Sensibilidade das especificações", "Barras mostram F1 entre 0,648 no teste temporal e 0,781 sem casos ambíguos.")
    lines.append('<text x="550" y="38" text-anchor="middle" class="title">A conclusão depende de representação, semente, casos e tempo</text>')
    left, width = 410, 570
    for tick in [.6, .65, .7, .75, .8]:
        x = left + (tick-.6)/.2*width
        lines += [f'<line x1="{x}" y1="90" x2="{x}" y2="500" stroke="{LINE}"/>',
                  f'<text x="{x}" y="530" text-anchor="middle" class="small">{tick:.2f}</text>']
    for i, row in enumerate(values.itertuples()):
        y = 112+i*76; bar = (row.f1-.6)/.2*width; color = RUST if row.analise == "teste temporal" else TEAL
        lines += [f'<text x="390" y="{y+28}" text-anchor="end" class="label">{escape(row.analise)}</text>',
                  f'<rect x="{left}" y="{y}" width="{bar:.1f}" height="48" rx="6" fill="{color}"/>',
                  f'<text x="{left+bar+10:.1f}" y="{y+30}" class="small">{row.f1:.3f}</text>']
    lines += ['<text x="550" y="568" text-anchor="middle" class="small">Faixa observada: 0,648–0,781 · cada especificação responde a uma condição diferente</text>']
    save("03_sensibilidade.svg", lines)


def bootstrap(data: pd.DataFrame) -> None:
    rng = np.random.default_rng(42); values = []
    for _ in range(1000):
        sample = data.sample(len(data), replace=True, random_state=int(rng.integers(1_000_000)))
        values.append((sample.classe_ouro == sample.classe_prevista).mean())
    counts, edges = np.histogram(values, bins=np.linspace(.58, .80, 23))
    q025, q50, q975 = np.quantile(values, [.025, .5, .975])
    lines = open_svg("Distribuição bootstrap da acurácia", "Histograma de mil reamostragens mostra mediana 0,696 e intervalo percentil de 0,633 a 0,750.")
    lines.append('<text x="550" y="38" text-anchor="middle" class="title">A incerteza amostral produz uma faixa, não um ponto exato</text>')
    left, top, width, height = 110, 100, 880, 360; maximum = counts.max()
    for i, count in enumerate(counts):
        x = left+i/len(counts)*width; w = width/len(counts)-2; h = count/maximum*height
        lines.append(f'<rect x="{x:.1f}" y="{top+height-h:.1f}" width="{w:.1f}" height="{h:.1f}" fill="{TEAL}"/>')
    for value, label, color in [(q025, "2,5%", RUST), (q50, "mediana", NAVY), (q975, "97,5%", RUST)]:
        x = left+(value-.58)/.22*width
        lines += [f'<line x1="{x:.1f}" y1="{top}" x2="{x:.1f}" y2="{top+height}" stroke="{color}" stroke-width="4"/>',
                  f'<text x="{x:.1f}" y="{top-12}" text-anchor="middle" class="small">{label}: {value:.3f}</text>']
    lines += ['<text x="550" y="505" text-anchor="middle" class="label">intervalo percentil descritivo: 0,633–0,750</text>',
              '<text x="550" y="548" text-anchor="middle" class="small">1.000 reamostragens dos 240 casos observados · não corrige viés de seleção</text>']
    save("04_bootstrap_acuracia.svg", lines)


def subgroup_metrics(data: pd.DataFrame) -> None:
    groups = []
    for dimension in ["periodo", "origem"]:
        for name, group in data.groupby(dimension):
            groups.append((str(name), len(group), f1_score(group.classe_ouro, group.classe_prevista)))
    lines = open_svg("Desempenho por período e origem", "Barras mostram F1 de 0,650 no período antigo, 0,741 no recente, 0,713 na Capital e 0,659 no Interior.")
    lines.append('<text x="550" y="38" text-anchor="middle" class="title">A média geral oculta diferenças entre contextos</text>')
    left, width = 300, 650
    for tick in [0, .25, .5, .75, 1]:
        x = left+tick*width
        lines += [f'<line x1="{x}" y1="90" x2="{x}" y2="490" stroke="{LINE}"/>',
                  f'<text x="{x}" y="520" text-anchor="middle" class="small">{tick:.2f}</text>']
    for i, (name, n, value) in enumerate(groups):
        y = 115+i*90; color = TEAL if name in ["recente", "Capital"] else RUST
        lines += [f'<text x="275" y="{y+30}" text-anchor="end" class="label">{escape(name)} · n={n}</text>',
                  f'<rect x="{left}" y="{y}" width="{value*width:.1f}" height="50" rx="6" fill="{color}"/>',
                  f'<text x="{left+value*width+12:.1f}" y="{y+31}" class="small">F1 = {value:.3f}</text>']
    lines += ['<text x="550" y="565" text-anchor="middle" class="small">Diferença observada orienta investigação; não identifica sozinha o mecanismo causal.</text>']
    save("05_metricas_contexto.svg", lines)


def main() -> None:
    predictions = pd.read_csv(DATA / "predicoes_auditoria.csv")
    analyses = pd.read_csv(DATA / "analises_sensibilidade.csv")
    baseline_model(predictions)
    confusion(predictions)
    sensitivity(analyses)
    bootstrap(predictions)
    subgroup_metrics(predictions)
    print(f"Gráficos gravados em {OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
