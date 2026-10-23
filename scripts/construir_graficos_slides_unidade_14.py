"""Gera visualizações calculadas para os slides da Unidade 14.

Os dados são inteiramente fictícios e servem apenas para ensino de
documentação, reprodução, comunicação e compartilhamento responsável.
"""

from __future__ import annotations

from html import escape
from pathlib import Path
import hashlib

import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "unidade_14" / "dados"
OUT = ROOT / "slides" / "imagens" / "unidade_14"
NAVY, TEAL, RUST, PLUM = "#17324d", "#176b68", "#a84f2a", "#69445f"
GRAY, LINE, PAPER, PALE = "#4b5563", "#d8cdbb", "#fffdf7", "#f2eee5"


def open_svg(title: str, description: str) -> list[str]:
    return [
        '<svg xmlns="http://www.w3.org/2000/svg" width="1100" height="590" viewBox="0 0 1100 590" role="img">',
        f"<title>{escape(title)}</title>", f"<desc>{escape(description)}</desc>",
        f'<rect width="1100" height="590" fill="{PAPER}"/>',
        '<style>text{font-family:Aptos,Arial,sans-serif}.title{font-size:28px;font-weight:700;fill:#17324d}.label{font-size:19px;fill:#202a33}.small{font-size:16px;fill:#4b5563}.value{font-size:21px;font-weight:700;fill:#17324d}.mono{font-family:monospace;font-size:16px;fill:#17324d}</style>',
    ]


def save(name: str, lines: list[str]) -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / name).write_text("\n".join(lines + ["</svg>", ""]), encoding="utf-8")


def manifest(manifesto: pd.DataFrame) -> None:
    lines = open_svg("Manifesto de artefatos e acesso", "Sete cartões apresentam seis artefatos abertos e um conjunto de dados derivados restrito.")
    lines.append('<text x="550" y="38" text-anchor="middle" class="title">Reproduzir não exige abrir tudo do mesmo modo</text>')
    for i, row in enumerate(manifesto.itertuples()):
        col, grid_row = i % 4, i // 4; x, y = 45+col*265, 90+grid_row*190
        color = TEAL if row.acesso == "aberto" else RUST
        filename = row.caminho if len(row.caminho) <= 24 else "…"+row.caminho[-23:]
        lines += [f'<rect x="{x}" y="{y}" width="235" height="145" rx="14" fill="{PALE}" stroke="{color}" stroke-width="4"/>',
                  f'<text x="{x+118}" y="{y+38}" text-anchor="middle" class="mono">{escape(filename)}</text>',
                  f'<text x="{x+118}" y="{y+77}" text-anchor="middle" class="small">{escape(row.papel)}</text>',
                  f'<text x="{x+118}" y="{y+116}" text-anchor="middle" font-size="19" font-weight="700" fill="{color}">{escape(row.acesso)}</text>']
    lines += ['<text x="550" y="500" text-anchor="middle" class="label">6 abertos · 1 restrito · 7 com justificativa de acesso</text>',
              '<text x="550" y="545" text-anchor="middle" class="small">Código e documentação podem ser abertos enquanto dados derivados permanecem protegidos.</text>']
    save("01_manifesto_acesso.svg", lines)


def execution_checks(results_path: Path, results: pd.DataFrame) -> None:
    digest = hashlib.sha256(results_path.read_bytes()).hexdigest()
    checks = [
        ("3 linhas esperadas", len(results) == 3),
        ("5 colunas na ordem", list(results.columns) == ["analise", "estimativa", "limite_inferior", "limite_superior", "alcance"]),
        ("limite inferior ≤ estimativa", (results.limite_inferior <= results.estimativa).all()),
        ("estimativa ≤ limite superior", (results.estimativa <= results.limite_superior).all()),
    ]
    lines = open_svg("Verificações da execução", "Quatro verificações passam e um hash SHA-256 identifica os bytes do arquivo de resultados.")
    lines.append('<text x="550" y="38" text-anchor="middle" class="title">Uma execução reprodutível produz resultados verificáveis</text>')
    for i, (label, passed) in enumerate(checks):
        y = 100+i*82; color = TEAL if passed else RUST
        lines += [f'<circle cx="150" cy="{y}" r="24" fill="{color}"/>',
                  f'<text x="150" y="{y+8}" text-anchor="middle" font-size="25" font-weight="700" fill="white">✓</text>',
                  f'<text x="200" y="{y+7}" class="label">{escape(label)}</text>',
                  f'<text x="900" y="{y+7}" text-anchor="end" class="value">PASSOU</text>']
    lines += [f'<rect x="90" y="445" width="920" height="72" rx="12" fill="{PALE}" stroke="{NAVY}" stroke-width="3"/>',
              '<text x="120" y="474" class="small">SHA-256 do arquivo:</text>',
              f'<text x="120" y="502" class="mono">{digest}</text>',
              '<text x="550" y="558" text-anchor="middle" class="small">O hash detecta mudança de bytes; não garante qualidade, autenticidade ou interpretação correta.</text>']
    save("02_checks_execucao.svg", lines)


def interval_plot(results: pd.DataFrame) -> None:
    lines = open_svg("Estimativas, intervalos e baseline", "Três estimativas são mostradas com intervalos em escala de zero a um e linha de referência em 0,5.")
    lines.append('<text x="550" y="38" text-anchor="middle" class="title">A figura comunica valor, faixa e referência na mesma escala</text>')
    left, top, width = 250, 105, 720
    for tick in [0, .25, .5, .75, 1]:
        x = left+tick*width
        lines += [f'<line x1="{x}" y1="{top}" x2="{x}" y2="450" stroke="{LINE}"/>',
                  f'<text x="{x}" y="490" text-anchor="middle" class="small">{tick:.2f}</text>']
    xb = left+.5*width
    lines.append(f'<line x1="{xb}" y1="{top}" x2="{xb}" y2="450" stroke="{GRAY}" stroke-width="3" stroke-dasharray="8 6"/>')
    colors = [TEAL, RUST, GRAY]
    for i, (row, color) in enumerate(zip(results.itertuples(), colors)):
        y = 155+i*115; xlo = left+row.limite_inferior*width; xhi = left+row.limite_superior*width; x = left+row.estimativa*width
        lines += [f'<text x="220" y="{y+7}" text-anchor="end" class="label">{escape(row.analise)}</text>',
                  f'<line x1="{xlo}" y1="{y}" x2="{xhi}" y2="{y}" stroke="{color}" stroke-width="7"/>',
                  f'<line x1="{xlo}" y1="{y-14}" x2="{xlo}" y2="{y+14}" stroke="{color}" stroke-width="4"/>',
                  f'<line x1="{xhi}" y1="{y-14}" x2="{xhi}" y2="{y+14}" stroke="{color}" stroke-width="4"/>',
                  f'<circle cx="{x}" cy="{y}" r="11" fill="{color}"/>',
                  f'<text x="{x}" y="{y-24}" text-anchor="middle" class="small">{row.estimativa:.2f} [{row.limite_inferior:.2f}, {row.limite_superior:.2f}]</text>']
    lines += ['<text x="610" y="535" text-anchor="middle" class="label">estimativa e intervalo · escala completa de 0 a 1</text>',
              '<text x="610" y="568" text-anchor="middle" class="small">linha tracejada = referência 0,50 · dados fictícios</text>']
    save("03_resultados_intervalos.svg", lines)


def axis_comparison(results: pd.DataFrame) -> None:
    subset = results.iloc[:2]
    lines = open_svg("Escala completa e eixo truncado", "Os mesmos valores 0,71 e 0,68 parecem próximos em escala zero a um e muito diferentes em escala 0,65 a 0,72.")
    lines.append('<text x="550" y="38" text-anchor="middle" class="title">O eixo altera a ênfase visual — não os valores</text>')
    for panel_x, xmin, xmax, title in [(85, 0, 1, "escala 0–1"), (610, .65, .72, "eixo 0,65–0,72")]:
        width = 400
        lines += [f'<rect x="{panel_x}" y="100" width="{width}" height="350" fill="{PALE}" stroke="{LINE}"/>',
                  f'<text x="{panel_x+width/2}" y="82" text-anchor="middle" class="value">{title}</text>']
        for i, row in enumerate(subset.itertuples()):
            y = 180+i*145; ratio = (row.estimativa-xmin)/(xmax-xmin); bar = max(0, min(1, ratio))*width
            color = TEAL if i == 0 else RUST
            lines += [f'<text x="{panel_x+15}" y="{y-15}" class="small">{escape(row.analise)}</text>',
                      f'<rect x="{panel_x}" y="{y}" width="{bar:.1f}" height="58" fill="{color}"/>',
                      f'<text x="{panel_x+bar-12:.1f}" y="{y+38}" text-anchor="end" font-size="22" font-weight="700" fill="white">{row.estimativa:.2f}</text>']
        lines += [f'<text x="{panel_x}" y="480" class="small">{xmin:.2f}</text>',
                  f'<text x="{panel_x+width}" y="480" text-anchor="end" class="small">{xmax:.2f}</text>']
    lines += ['<text x="550" y="535" text-anchor="middle" class="label">Diferença numérica em ambos: 0,03</text>',
              '<text x="550" y="570" text-anchor="middle" class="small">Eixo truncado pode ser útil para detalhe, mas precisa ser explícito e justificado.</text>']
    save("04_eixo_truncado.svg", lines)


def combination_risk(records: pd.DataFrame) -> None:
    keys = ["faixa_etaria", "local", "tema"]
    sizes = records.groupby(keys).size().rename("k").reset_index()
    assessed = records.merge(sizes, on=keys)
    lines = open_svg("Combinações raras após remoção de nomes", "Oito registros são mostrados; seis possuem combinação única de idade, local e tema, e dois formam um par.")
    lines.append('<text x="550" y="38" text-anchor="middle" class="title">Remover o nome não elimina combinações identificáveis</text>')
    headers = [("registro", 80), ("faixa", 230), ("local", 385), ("tema", 570), ("k", 790), ("leitura", 900)]
    for label, x in headers: lines.append(f'<text x="{x}" y="88" class="value">{label}</text>')
    for i, row in enumerate(assessed.itertuples()):
        y = 125+i*50; color = RUST if row.k == 1 else TEAL
        lines += [f'<rect x="55" y="{y-28}" width="990" height="42" fill="{color}" fill-opacity=".10"/>',
                  f'<text x="80" y="{y}" class="small">{row.id_pesquisa}</text>',
                  f'<text x="230" y="{y}" class="small">{row.faixa_etaria}</text>',
                  f'<text x="385" y="{y}" class="small">{row.local}</text>',
                  f'<text x="570" y="{y}" class="small">{escape(row.tema)}</text>',
                  f'<text x="800" y="{y}" text-anchor="middle" font-size="20" font-weight="700" fill="{color}">{row.k}</text>',
                  f'<text x="900" y="{y}" class="small">{"única" if row.k == 1 else "repetida"}</text>']
    lines += ['<text x="550" y="545" text-anchor="middle" class="label">6 de 8 registros têm k = 1 nesta combinação didática</text>',
              '<text x="550" y="575" text-anchor="middle" class="small">k-anonimato descritivo não resolve atributos sensíveis, ligação auxiliar ou finalidade indevida.</text>']
    save("05_combinacoes_raras.svg", lines)


def main() -> None:
    manifesto = pd.read_csv(DATA / "manifesto_projeto.csv")
    results_path = DATA / "resultados_comunicacao.csv"
    results = pd.read_csv(results_path)
    records = pd.read_csv(DATA / "registros_compartilhamento.csv")
    manifest(manifesto)
    execution_checks(results_path, results)
    interval_plot(results)
    axis_comparison(results)
    combination_risk(records)
    print(f"Gráficos gravados em {OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
