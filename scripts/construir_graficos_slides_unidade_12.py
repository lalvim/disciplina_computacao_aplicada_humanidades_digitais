"""Gera visualizações calculadas para os slides da Unidade 12.

Requer pandas e scikit-learn. O corpus e as saídas de modelo são inteiramente
fictícios; nenhum serviço externo é chamado.
"""

from __future__ import annotations

from html import escape
from pathlib import Path

import pandas as pd
from sklearn.decomposition import TruncatedSVD
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "unidade_12" / "dados"
OUT = ROOT / "slides" / "imagens" / "unidade_12"
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


def arrow_defs() -> str:
    return f'<defs><marker id="a" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto"><path d="M0,0 L0,6 L9,3 z" fill="{NAVY}"/></marker></defs>'


def representation_ranking(corpus: pd.DataFrame) -> None:
    vectorizer = TfidfVectorizer()
    matrix = vectorizer.fit_transform(corpus.texto)
    query = vectorizer.transform(["matrículas na escola noturna"])
    tfidf = cosine_similarity(query, matrix)[0]
    svd = TruncatedSVD(n_components=4, random_state=42)
    dense_matrix = svd.fit_transform(matrix)
    dense_query = svd.transform(query)
    dense = cosine_similarity(dense_query, dense_matrix)[0]
    result = corpus.assign(tfidf=tfidf, dense=dense).sort_values("tfidf", ascending=False).head(5)
    lines = open_svg("Rankings dependem da representação", "Pontos conectados comparam similaridade TF-IDF e projeção densa local para cinco documentos.")
    lines.append('<text x="550" y="38" text-anchor="middle" class="title">A mesma consulta produz vizinhanças diferentes</text>')
    left, width = 360, 610
    for tick in [0, .25, .5, .75, 1]:
        x = left + tick * width
        lines += [f'<line x1="{x}" y1="90" x2="{x}" y2="490" stroke="{LINE}"/>',
                  f'<text x="{x}" y="520" text-anchor="middle" class="small">{tick:.2f}</text>']
    for i, row in enumerate(result.itertuples(), 0):
        y = 125 + i * 78; x1 = left + row.tfidf * width; x2 = left + row.dense * width
        lines += [f'<text x="330" y="{y+6}" text-anchor="end" class="label">{row.id_documento}</text>',
                  f'<line x1="{x1:.1f}" y1="{y}" x2="{x2:.1f}" y2="{y}" stroke="{GRAY}" stroke-width="3"/>',
                  f'<circle cx="{x1:.1f}" cy="{y}" r="9" fill="{TEAL}"/>',
                  f'<circle cx="{x2:.1f}" cy="{y}" r="9" fill="{RUST}"/>']
    lines += [f'<circle cx="330" cy="555" r="8" fill="{TEAL}"/><text x="348" y="561" class="small">TF-IDF</text>',
              f'<circle cx="500" cy="555" r="8" fill="{RUST}"/><text x="518" y="561" class="small">projeção SVD local</text>',
              '<text x="800" y="561" text-anchor="middle" class="small">consulta: “matrículas na escola noturna”</text>']
    save("01_rankings_representacoes.svg", lines)


def attention_example() -> None:
    lines = open_svg("Atenção como combinação contextual", "Exemplo didático atribui pesos diferentes a três tokens e os combina para representar o contexto.")
    lines += [arrow_defs(), '<text x="550" y="38" text-anchor="middle" class="title">Atenção pondera sinais conforme o contexto da sequência</text>']
    tokens = [("matrículas", .60, TEAL), ("escola", .30, RUST), ("noturna", .10, PLUM)]
    for i, (token, weight, color) in enumerate(tokens):
        x = 85 + i * 275
        lines += [f'<rect x="{x}" y="110" width="220" height="92" rx="14" fill="{PALE}" stroke="{color}" stroke-width="4"/>',
                  f'<text x="{x+110}" y="148" text-anchor="middle" class="value">{token}</text>',
                  f'<text x="{x+110}" y="181" text-anchor="middle" class="label">peso {weight:.2f}</text>',
                  f'<line x1="{x+110}" y1="208" x2="550" y2="355" stroke="{color}" stroke-width="{2+weight*8:.1f}" marker-end="url(#a)"/>']
    lines += [f'<rect x="405" y="370" width="290" height="100" rx="16" fill="white" stroke="{NAVY}" stroke-width="4"/>',
              '<text x="550" y="410" text-anchor="middle" class="value">representação contextual</text>',
              '<text x="550" y="445" text-anchor="middle" class="small">combinação ponderada dos sinais</text>',
              '<text x="550" y="525" text-anchor="middle" class="label">Exemplo conceitual: os pesos reais dependem do modelo, da camada e do token</text>',
              '<text x="550" y="560" text-anchor="middle" class="small">0,60 + 0,30 + 0,10 = 1,00</text>']
    save("02_atencao_didatica.svg", lines)


def retrieval_comparison(corpus: pd.DataFrame) -> None:
    vectorizer = TfidfVectorizer(); matrix = vectorizer.fit_transform(corpus.texto)
    queries = [
        ("respondível", "Quantas matrículas foram registradas e quantas presenças eram regulares?", TEAL),
        ("ausente", "Quem concluiu o curso?", RUST),
    ]
    lines = open_svg("Recuperação para pergunta respondível e ausente", "Um painel recupera F009 e F002 com pontuações positivas; no outro todos os documentos têm pontuação zero.")
    lines.append('<text x="550" y="38" text-anchor="middle" class="title">Recuperar bem e reconhecer ausência são tarefas diferentes</text>')
    for p, (kind, query, color) in enumerate(queries):
        left = 70 + p * 520
        scores = cosine_similarity(vectorizer.transform([query]), matrix)[0]
        order = scores.argsort()[::-1][:3]
        lines += [f'<rect x="{left}" y="85" width="455" height="420" rx="16" fill="{PALE}" stroke="{color}" stroke-width="4"/>',
                  f'<text x="{left+228}" y="125" text-anchor="middle" class="value">Pergunta {kind}</text>',
                  f'<text x="{left+228}" y="158" text-anchor="middle" class="small">{escape(query[:52])}</text>']
        for i, idx in enumerate(order):
            y = 205 + i * 88; score = scores[idx]; bar = score / .6 * 250
            lines += [f'<text x="{left+68}" y="{y+29}" text-anchor="end" class="label">{corpus.iloc[idx].id_documento}</text>',
                      f'<rect x="{left+85}" y="{y}" width="{max(bar,2):.1f}" height="46" rx="6" fill="{color}"/>',
                      f'<text x="{left+100+max(bar,2):.1f}" y="{y+29}" class="small">{score:.3f}</text>']
        decision = "responder com F009 e F002" if kind == "respondível" else "abster: nenhuma evidência lexical"
        lines.append(f'<text x="{left+228}" y="475" text-anchor="middle" class="label">{decision}</text>')
    lines.append('<text x="550" y="557" text-anchor="middle" class="small">Pontuação zero não prova ausência no mundo; indica ausência de apoio nesta representação e neste corpus.</text>')
    save("03_recuperacao_respondivel_ausente.svg", lines)


def output_audit(outputs: pd.DataFrame) -> None:
    supported = outputs.rotulo_ouro.isin(["adequada", "abstencao_adequada"])
    colors = {"adequada": TEAL, "abstencao_adequada": NAVY, "alucinacao": RUST,
              "contradicao": PLUM, "extrapolacao": "#bd7b2c"}
    labels = {"adequada": "adequada", "abstencao_adequada": "abstinência",
              "alucinacao": "alucinação", "contradicao": "contradição", "extrapolacao": "extrapolação"}
    lines = open_svg("Auditoria das seis saídas hipotéticas", "Seis cartões mostram duas saídas adequadas, uma abstinência adequada e três tipos de erro.")
    lines.append('<text x="550" y="38" text-anchor="middle" class="title">Metade das saídas simuladas tem apoio adequado</text>')
    for i, row in enumerate(outputs.itertuples()):
        col, grid_row = i % 3, i // 3; x, y = 55 + col * 350, 90 + grid_row * 190
        color = colors[row.rotulo_ouro]
        source = row.fontes_declaradas if row.fontes_declaradas else "sem fonte"
        lines += [f'<rect x="{x}" y="{y}" width="320" height="155" rx="14" fill="{PALE}" stroke="{color}" stroke-width="5"/>',
                  f'<text x="{x+28}" y="{y+39}" class="value">{row.id_teste}</text>',
                  f'<text x="{x+292}" y="{y+39}" text-anchor="end" class="small">{escape(source)}</text>',
                  f'<text x="{x+160}" y="{y+86}" text-anchor="middle" font-size="22" font-weight="700" fill="{color}">{labels[row.rotulo_ouro]}</text>',
                  f'<text x="{x+160}" y="{y+124}" text-anchor="middle" class="small">{escape(row.justificativa)}</text>']
    lines += [f'<rect x="235" y="500" width="630" height="54" rx="10" fill="{TEAL}"/>',
              f'<text x="550" y="535" text-anchor="middle" font-size="22" font-weight="700" fill="white">taxa apoiada = {supported.sum()}/{len(outputs)} = {supported.mean():.2f}</text>']
    save("04_auditoria_saidas.svg", lines)


def privacy_flow() -> None:
    lines = open_svg("Decisão de envio e minimização", "Fluxo de decisão verifica sensibilidade, necessidade de serviço externo, termos, minimização e revisão antes do uso.")
    lines += [arrow_defs(), '<text x="550" y="38" text-anchor="middle" class="title">O primeiro controle ocorre antes do envio</text>']
    cards = [
        ("Há dados pessoais,\nsigilosos ou restritos?", 90, 100, RUST),
        ("A tarefa pode\nser local?", 440, 100, TEAL),
        ("Termos, retenção\ne finalidade são aceitáveis?", 790, 100, PLUM),
        ("Minimizar dados\ne registrar versão", 265, 345, NAVY),
        ("Revisar, contestar\ne poder interromper", 615, 345, TEAL),
    ]
    for text_value, x, y, color in cards:
        parts = text_value.split("\n")
        lines += [f'<rect x="{x}" y="{y}" width="260" height="115" rx="15" fill="{PALE}" stroke="{color}" stroke-width="4"/>',
                  f'<text x="{x+130}" y="{y+47}" text-anchor="middle" class="label">{parts[0]}</text>',
                  f'<text x="{x+130}" y="{y+76}" text-anchor="middle" class="label">{parts[1]}</text>']
    lines += [f'<line x1="350" y1="158" x2="430" y2="158" stroke="{NAVY}" stroke-width="4" marker-end="url(#a)"/>',
              f'<line x1="700" y1="158" x2="780" y2="158" stroke="{NAVY}" stroke-width="4" marker-end="url(#a)"/>',
              f'<line x1="920" y1="220" x2="745" y2="340" stroke="{NAVY}" stroke-width="4" marker-end="url(#a)"/>',
              f'<line x1="525" y1="402" x2="605" y2="402" stroke="{NAVY}" stroke-width="4" marker-end="url(#a)"/>',
              '<text x="550" y="520" text-anchor="middle" class="label">Se a proteção não puder ser demonstrada, não enviar é uma decisão válida.</text>',
              '<text x="550" y="558" text-anchor="middle" class="small">Risco, benefício e reversibilidade devem ser avaliados para a tarefa concreta.</text>']
    save("05_fluxo_privacidade.svg", lines)


def main() -> None:
    corpus = pd.read_csv(DATA / "corpus_local.csv")
    outputs = pd.read_csv(DATA / "saidas_modelo_hipotetico.csv").fillna("")
    representation_ranking(corpus)
    attention_example()
    retrieval_comparison(corpus)
    output_audit(outputs)
    privacy_flow()
    print(f"Gráficos gravados em {OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
