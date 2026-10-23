"""Gera visualizações calculadas para os slides da Unidade 10.

Os exemplos usam apenas os dados fictícios da unidade e reproduzem as regras
transparentes empregadas nos notebooks.
"""

from __future__ import annotations

from html import escape
from pathlib import Path
import re

import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "unidade_10" / "dados"
OUT = ROOT / "slides" / "imagens" / "unidade_10"
NAVY, TEAL, RUST, PLUM = "#17324d", "#176b68", "#a84f2a", "#69445f"
GRAY, LINE, PAPER, PALE = "#4b5563", "#d8cdbb", "#fffdf7", "#f2eee5"


def open_svg(title: str, description: str) -> list[str]:
    return [
        '<svg xmlns="http://www.w3.org/2000/svg" width="1100" height="590" viewBox="0 0 1100 590" role="img">',
        f"<title>{escape(title)}</title>",
        f"<desc>{escape(description)}</desc>",
        f'<rect width="1100" height="590" fill="{PAPER}"/>',
        '<style>text{font-family:Aptos,Arial,sans-serif}.title{font-size:28px;font-weight:700;fill:#17324d}.label{font-size:19px;fill:#202a33}.small{font-size:16px;fill:#4b5563}.value{font-size:22px;font-weight:700;fill:#17324d}.mono{font-family:monospace;font-size:18px;fill:#17324d}</style>',
    ]


def save(name: str, lines: list[str]) -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / name).write_text("\n".join(lines + ["</svg>", ""]), encoding="utf-8")


def arrow(x1: int, y1: int, x2: int, y2: int, color: str = NAVY) -> str:
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="4" marker-end="url(#seta)"/>'


def definitions() -> str:
    return f'<defs><marker id="seta" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto"><path d="M0,0 L0,6 L9,3 z" fill="{NAVY}"/></marker></defs>'


def initial_ambiguity(documents: pd.DataFrame) -> None:
    text = documents.loc[documents.id_documento.eq("D008"), "texto"].iloc[0]
    lines = open_svg("Uma menção, dois referentes possíveis", "O contexto de D008 distingue a embarcação Santa Rita da cidade homônima.")
    lines += [definitions(), '<text x="550" y="42" text-anchor="middle" class="title">A cadeia “Santa Rita” não determina sozinha a entidade</text>',
              f'<rect x="80" y="82" width="940" height="100" rx="12" fill="{PALE}" stroke="{LINE}"/>',
              f'<text x="550" y="124" text-anchor="middle" class="label">{escape(text[:70])}</text>',
              f'<text x="550" y="155" text-anchor="middle" class="label">{escape(text[70:])}</text>',
              arrow(550, 185, 550, 235),
              f'<rect x="410" y="240" width="280" height="72" rx="12" fill="white" stroke="{RUST}" stroke-width="4"/>',
              '<text x="550" y="285" text-anchor="middle" class="value">menção: Santa Rita</text>',
              arrow(470, 316, 300, 370), arrow(630, 316, 800, 370),
              f'<rect x="105" y="375" width="390" height="120" rx="14" fill="{PALE}" stroke="{PLUM}" stroke-width="4"/>',
              '<text x="300" y="417" text-anchor="middle" class="value">L002 · cidade</text>',
              '<text x="300" y="454" text-anchor="middle" class="small">candidato do catálogo de autoridade</text>',
              f'<rect x="605" y="375" width="390" height="120" rx="14" fill="{PALE}" stroke="{TEAL}" stroke-width="4"/>',
              '<text x="800" y="417" text-anchor="middle" class="value">OUTRO · embarcação</text>',
              '<text x="800" y="454" text-anchor="middle" class="small">contexto: “o vapor” + negação explícita</text>',
              '<text x="550" y="548" text-anchor="middle" class="label">Decisão auditável: não vincular a L002</text>']
    save("01_ambiguidade_santa_rita.svg", lines)


def extraction_counts(documents: pd.DataFrame, authorities: pd.DataFrame) -> None:
    found: list[tuple[str, str]] = []
    for _, row in authorities.fillna("").iterrows():
        for form in [row.nome_canonico, *[x for x in row.variantes.split(";") if x]]:
            for _, document in documents.iterrows():
                if form in document.texto:
                    found.append((document.id_documento, row.tipo))
    counts = pd.Series([kind for _, kind in found]).value_counts()
    labels = [("Pessoas", int(counts.get("PESSOA", 0)), TEAL),
              ("Organizações", int(counts.get("ORGANIZACAO", 0)), RUST),
              ("Lugares", int(counts.get("LUGAR", 0)), PLUM)]
    lines = open_svg("Menções reconhecidas por tipo", "Barras mostram 11 pessoas, 16 organizações e 8 lugares encontrados pelo dicionário nos doze documentos.")
    lines.append('<text x="550" y="42" text-anchor="middle" class="title">O dicionário encontra 35 menções — inclusive um caso errado</text>')
    left, top, width, height = 175, 100, 760, 360
    for tick in range(0, 17, 4):
        x = left + tick / 16 * width
        lines += [f'<line x1="{x}" y1="{top}" x2="{x}" y2="{top+height}" stroke="{LINE}"/>',
                  f'<text x="{x}" y="490" text-anchor="middle" class="small">{tick}</text>']
    for i, (label, value, color) in enumerate(labels):
        y = 125 + i * 115
        bar = value / 16 * width
        lines += [f'<text x="150" y="{y+42}" text-anchor="end" class="label">{label}</text>',
                  f'<rect x="{left}" y="{y}" width="{bar}" height="62" rx="8" fill="{color}"/>',
                  f'<text x="{left+bar-18}" y="{y+41}" text-anchor="end" font-size="25" font-weight="700" fill="white">{value}</text>']
    lines += ['<text x="550" y="532" text-anchor="middle" class="small">contagem de correspondências no corpus fictício</text>',
              '<text x="550" y="565" text-anchor="middle" class="label">Cobertura aparente não equivale a correção</text>']
    save("02_extracoes_por_tipo.svg", lines)


def event_timeline(documents: pd.DataFrame) -> None:
    rules = [
        ("Ana Ferreira", "Liga Aurora", "fundou", "fundação"),
        ("Liga Aurora", "Escola Livre", "inaugurou", "inauguração"),
        ("Dora Silva", "Liga Aurora", "ingressou", "ingresso"),
        ("Escola Livre", "Eva Lima", "contratou", "contratação"),
    ]
    events = []
    for _, doc in documents.iterrows():
        for subject, obj, trigger, event_type in rules:
            if subject in doc.texto and obj in doc.texto and trigger in doc.texto:
                events.append((int(doc.ano), doc.id_documento, event_type, subject, obj))
    lines = open_svg("Eventos extraídos ao longo do tempo", "Linha do tempo apresenta quatro alegações extraídas por regras em 1901, 1902, 1909 e 1912.")
    lines += ['<text x="550" y="42" text-anchor="middle" class="title">Quatro regras produzem quatro alegações rastreáveis</text>',
              f'<line x1="115" y1="300" x2="985" y2="300" stroke="{NAVY}" stroke-width="5"/>']
    xs = [150, 385, 700, 940]
    colors = [TEAL, RUST, PLUM, NAVY]
    for i, ((year, doc, typ, subject, obj), x, color) in enumerate(zip(events, xs, colors)):
        above = i % 2 == 0
        ybox = 95 if above else 345
        yline = 230 if above else 345
        lines += [f'<line x1="{x}" y1="300" x2="{x}" y2="{yline}" stroke="{color}" stroke-width="4"/>',
                  f'<circle cx="{x}" cy="300" r="12" fill="{color}"/>',
                  f'<rect x="{x-105}" y="{ybox}" width="210" height="130" rx="12" fill="{PALE}" stroke="{color}" stroke-width="3"/>',
                  f'<text x="{x}" y="{ybox+32}" text-anchor="middle" class="value">{year} · {doc}</text>',
                  f'<text x="{x}" y="{ybox+64}" text-anchor="middle" class="small">{escape(typ)}</text>',
                  f'<text x="{x}" y="{ybox+94}" text-anchor="middle" class="small">{escape(subject)}</text>',
                  f'<text x="{x}" y="{ybox+117}" text-anchor="middle" class="small">→ {escape(obj)}</text>']
    lines.append('<text x="550" y="555" text-anchor="middle" class="label">A linha organiza alegações da base; não comprova os acontecimentos</text>')
    save("03_linha_do_tempo_eventos.svg", lines)


def evaluation(authorities: pd.DataFrame, documents: pd.DataFrame, gold: pd.DataFrame) -> None:
    forms = []
    for _, row in authorities.fillna("").iterrows():
        for form in [row.nome_canonico, *[x for x in row.variantes.split(";") if x]]:
            forms.append((form, row.id_entidade, row.tipo))
    predictions = []
    selected = documents[documents.id_documento.isin(gold.id_documento.unique())]
    for _, doc in selected.iterrows():
        for form, identity, kind in forms:
            if form in doc.texto:
                predictions.append((doc.id_documento, form, identity, kind))
    predicted = set(predictions)
    reference = set(map(tuple, gold[["id_documento", "mencao", "id_entidade", "tipo"]].to_records(index=False)))
    tp, fp, fn = len(predicted & reference), len(predicted - reference), len(reference - predicted)
    lines = open_svg("Comparação entre predições e anotação de referência", "Diagrama mostra onze verdadeiros positivos, um falso positivo e um falso negativo.")
    lines.append('<text x="550" y="42" text-anchor="middle" class="title">A avaliação localiza acertos e erros — não apenas uma nota</text>')
    cards = [("VP", tp, "extração coincide com o ouro", TEAL),
             ("FP", fp, "sistema propõe; ouro rejeita", RUST),
             ("FN", fn, "ouro registra; sistema perde", PLUM)]
    for i, (abbr, value, label, color) in enumerate(cards):
        x = 70 + i * 345
        lines += [f'<rect x="{x}" y="105" width="305" height="210" rx="16" fill="{PALE}" stroke="{color}" stroke-width="5"/>',
                  f'<text x="{x+152}" y="160" text-anchor="middle" class="value">{abbr}</text>',
                  f'<text x="{x+152}" y="235" text-anchor="middle" font-size="58" font-weight="700" fill="{color}">{value}</text>',
                  f'<text x="{x+152}" y="283" text-anchor="middle" class="small">{label}</text>']
    lines += [f'<rect x="160" y="365" width="780" height="110" rx="14" fill="white" stroke="{LINE}"/>',
              '<text x="550" y="405" text-anchor="middle" class="label">D008 · “Santa Rita”</text>',
              '<text x="550" y="440" text-anchor="middle" class="small">FP: L002/LUGAR · FN: entidade vazia/OUTRO</text>',
              '<text x="550" y="535" text-anchor="middle" class="label">Precisão = revocação = F1 = 11/12 = 0,917</text>']
    save("04_avaliacao_extracoes.svg", lines)


def error_cascade() -> None:
    lines = open_svg("Erro em cascata da extração ao grafo", "Dois percursos contrastam a interpretação contextual correta com uma vinculação equivocada de Santa Rita à cidade.")
    lines += [definitions(), '<text x="550" y="42" text-anchor="middle" class="title">Uma ligação equivocada muda a estrutura analisada</text>']
    for x, title, color in [(65, "com contexto", TEAL), (575, "sem contexto", RUST)]:
        lines += [f'<rect x="{x}" y="85" width="460" height="415" rx="16" fill="{PALE}" stroke="{color}" stroke-width="4"/>',
                  f'<text x="{x+230}" y="125" text-anchor="middle" class="value">{title}</text>']
    left = [(150, 205, "vapor\nSanta Rita"), (405, 205, "Porto\nClaro")]
    right = [(660, 205, "L002\ncidade"), (915, 205, "Porto\nClaro")]
    for x, y, label in left + right:
        parts = label.split("\n")
        lines += [f'<circle cx="{x}" cy="{y}" r="62" fill="white" stroke="{NAVY}" stroke-width="4"/>',
                  f'<text x="{x}" y="{y-4}" text-anchor="middle" class="label">{parts[0]}</text>',
                  f'<text x="{x}" y="{y+22}" text-anchor="middle" class="small">{parts[1]}</text>']
    lines += [arrow(215, 205, 338, 205), arrow(725, 205, 848, 205),
              '<text x="276" y="185" text-anchor="middle" class="small">chegou a</text>',
              f'<text x="786" y="185" text-anchor="middle" class="small" fill="{RUST}">ligação espacial falsa</text>',
              '<text x="295" y="330" text-anchor="middle" class="label">registro: embarcação</text>',
              '<text x="805" y="330" text-anchor="middle" class="label">registro: lugar</text>',
              '<text x="295" y="382" text-anchor="middle" class="small">preserva a negação do texto</text>',
              '<text x="805" y="382" text-anchor="middle" class="small">cria nó e aresta espúrios</text>',
              '<text x="550" y="548" text-anchor="middle" class="label">Centralidade mede o grafo recebido; não corrige sua proveniência</text>']
    save("05_erro_em_cascata.svg", lines)


def main() -> None:
    documents = pd.read_csv(DATA / "documentos.csv")
    authorities = pd.read_csv(DATA / "autoridades.csv")
    gold = pd.read_csv(DATA / "anotacao_ouro.csv").fillna("")
    initial_ambiguity(documents)
    extraction_counts(documents, authorities)
    event_timeline(documents)
    evaluation(authorities, documents, gold)
    error_cascade()
    print(f"Gráficos gravados em {OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
