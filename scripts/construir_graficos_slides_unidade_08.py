"""Gera visualizações calculadas para os slides da Unidade 8.

O script reproduz a divisão e os modelos dos notebooks. Requer pandas, NumPy e
scikit-learn, as mesmas dependências instaladas na preparação do ambiente da
unidade no Google Colab.
"""

from __future__ import annotations

from html import escape
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.dummy import DummyClassifier
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, cohen_kappa_score, confusion_matrix, f1_score, precision_score, recall_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder
from sklearn.tree import DecisionTreeClassifier


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "unidade_08" / "dados"
OUT = ROOT / "slides" / "imagens" / "unidade_08"

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
        '<style>text{font-family:Aptos,Arial,sans-serif}.title{font-size:28px;font-weight:700;fill:#17324d}.label{font-size:19px;fill:#202a33}.small{font-size:16px;fill:#4b5563}.value{font-size:20px;font-weight:700;fill:#17324d}</style>',
    ]


def save(name: str, lines: list[str]) -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / name).write_text("\n".join(lines + ["</svg>", ""]), encoding="utf-8")


def metrics(y, predicted):
    return {
        "Acurácia": accuracy_score(y, predicted),
        "Precisão": precision_score(y, predicted, pos_label="relevante", zero_division=0),
        "Revocação": recall_score(y, predicted, pos_label="relevante", zero_division=0),
        "F1": f1_score(y, predicted, pos_label="relevante", zero_division=0),
    }


def agreement_chart(annotations: pd.DataFrame) -> None:
    labels = ["não relevante", "relevante"]
    matrix = confusion_matrix(annotations["anotador_a"], annotations["anotador_b"], labels=labels)
    agreement = (annotations["anotador_a"] == annotations["anotador_b"]).mean()
    kappa = cohen_kappa_score(annotations["anotador_a"], annotations["anotador_b"])
    lines = svg_open("Concordância entre anotadores", "Matriz dois por dois com vinte e sete acordos e cinco desacordos.")
    lines.append('<text x="550" y="42" text-anchor="middle" class="title">Concordar não elimina os casos difíceis</text>')
    x0, y0, cell = 315, 130, 145
    lines += ['<text x="460" y="92" text-anchor="middle" class="label">Anotador B</text>',
              '<text x="165" y="285" text-anchor="middle" class="label" transform="rotate(-90 165 285)">Anotador A</text>']
    for j, label in enumerate(["não", "sim"]):
        lines.append(f'<text x="{x0+j*cell+cell/2}" y="120" text-anchor="middle" class="small">{label}</text>')
    for i, label in enumerate(["não", "sim"]):
        lines.append(f'<text x="{x0-20}" y="{y0+i*cell+cell/2+6}" text-anchor="end" class="small">{label}</text>')
        for j in range(2):
            color = TEAL if i == j else RUST
            opacity = 0.28 + matrix[i, j] / matrix.max() * 0.62
            lines += [f'<rect x="{x0+j*cell}" y="{y0+i*cell}" width="{cell}" height="{cell}" fill="{color}" fill-opacity="{opacity:.2f}" stroke="white" stroke-width="4"/>',
                      f'<text x="{x0+j*cell+cell/2}" y="{y0+i*cell+cell/2+10}" text-anchor="middle" font-size="34" font-weight="700" fill="{NAVY}">{matrix[i,j]}</text>']
    lines += [f'<text x="680" y="190" class="value">Acordo: {agreement:.1%}</text>',
              f'<text x="680" y="240" class="value">Kappa: {kappa:.3f}</text>',
              '<text x="680" y="310" class="small">27 coincidências</text>',
              '<text x="680" y="340" class="small">5 discordâncias</text>',
              '<text x="550" y="535" text-anchor="middle" class="small">Fonte: amostra_anotacao.csv · dados fictícios</text>']
    save("01_concordancia.svg", lines)


def split_chart(train: pd.DataFrame, test: pd.DataFrame) -> None:
    lines = svg_open("Divisão estratificada entre treino e teste", "Cento e vinte documentos de treino e quarenta de teste, ambos equilibrados entre classes.")
    lines.append('<text x="550" y="42" text-anchor="middle" class="title">O teste fica reservado antes das escolhas</text>')
    rows = [("Treino", train, 150), ("Teste", test, 335)]
    for label, frame, y in rows:
        counts = frame["classe_alvo"].value_counts()
        total = len(frame); width = 720
        no = int(counts["não relevante"]); yes = int(counts["relevante"])
        no_w = width * no / total
        lines += [f'<text x="180" y="{y+42}" text-anchor="end" class="label">{label}: n={total}</text>',
                  f'<rect x="210" y="{y}" width="{no_w}" height="70" fill="{PLUM}" rx="7"/>',
                  f'<rect x="{210+no_w}" y="{y}" width="{width-no_w}" height="70" fill="{TEAL}" rx="7"/>',
                  f'<text x="{210+no_w/2}" y="{y+44}" text-anchor="middle" fill="white" font-size="20" font-weight="700">não: {no}</text>',
                  f'<text x="{210+no_w+(width-no_w)/2}" y="{y+44}" text-anchor="middle" fill="white" font-size="20" font-weight="700">sim: {yes}</text>']
    lines += [f'<rect x="300" y="500" width="22" height="22" fill="{PLUM}"/><text x="334" y="518" class="small">não relevante</text>',
              f'<rect x="540" y="500" width="22" height="22" fill="{TEAL}"/><text x="574" y="518" class="small">relevante</text>']
    save("02_divisao_treino_teste.svg", lines)


def comparison_chart(results: dict[str, dict[str, float]]) -> None:
    lines = svg_open("Comparação de métricas por modelo", "Barras com acurácia, precisão, revocação e F1 para linha de base, logística, árvore e classificador textual.")
    lines.append('<text x="550" y="40" text-anchor="middle" class="title">Uma métrica isolada muda a história que contamos</text>')
    left, top, width, height = 110, 85, 860, 390
    for tick in [0, .25, .5, .75, 1]:
        y = top + height - tick*height
        lines += [f'<line x1="{left}" y1="{y}" x2="{left+width}" y2="{y}" stroke="{LINE}"/>',
                  f'<text x="92" y="{y+5}" text-anchor="end" class="small">{tick:.2f}</text>']
    names = list(results); metric_names = ["Acurácia", "Precisão", "Revocação", "F1"]
    colors = [NAVY, TEAL, RUST, PLUM]; group = width/len(names); bar_w = 38
    for i, name in enumerate(names):
        center = left + group*(i+.5)
        for j, metric in enumerate(metric_names):
            value=results[name][metric]; x=center+(j-1.5)*(bar_w+4); y=top+height-value*height
            lines.append(f'<rect x="{x:.1f}" y="{y:.1f}" width="{bar_w}" height="{value*height:.1f}" fill="{colors[j]}" rx="3"/>')
        lines.append(f'<text x="{center}" y="505" text-anchor="middle" class="small">{escape(name)}</text>')
    for j,(metric,color) in enumerate(zip(metric_names,colors)):
        x=180+j*205; lines += [f'<rect x="{x}" y="545" width="18" height="18" fill="{color}"/>',f'<text x="{x+27}" y="560" class="small">{metric}</text>']
    save("03_comparacao_modelos.svg", lines)


def confusion_comparison(matrices: dict[str, np.ndarray]) -> None:
    lines = svg_open("Matrizes de confusão", "Duas matrizes comparam árvore por metadados e TF-IDF com regressão logística.")
    lines.append('<text x="550" y="40" text-anchor="middle" class="title">A mesma acurácia pode esconder erros muito diferentes</text>')
    for panel,(name,matrix) in enumerate(matrices.items()):
        base_x=105+panel*535; x0=base_x+125; y0=145; cell=125
        lines.append(f'<text x="{base_x+250}" y="92" text-anchor="middle" class="value">{escape(name)}</text>')
        lines.append(f'<text x="{base_x+250}" y="125" text-anchor="middle" class="small">previsto → não / sim</text>')
        for i in range(2):
            lines.append(f'<text x="{x0-18}" y="{y0+i*cell+cell/2+5}" text-anchor="end" class="small">{"não" if i==0 else "sim"}</text>')
            for j in range(2):
                color=TEAL if i==j else RUST; opacity=.25+matrix[i,j]/max(1,matrix.max())*.65
                lines += [f'<rect x="{x0+j*cell}" y="{y0+i*cell}" width="{cell}" height="{cell}" fill="{color}" fill-opacity="{opacity:.2f}" stroke="white" stroke-width="4"/>',
                          f'<text x="{x0+j*cell+cell/2}" y="{y0+i*cell+cell/2+10}" text-anchor="middle" font-size="32" font-weight="700" fill="{NAVY}">{matrix[i,j]}</text>']
        lines.append(f'<text x="{base_x+43}" y="{y0+cell}" text-anchor="middle" class="small" transform="rotate(-90 {base_x+43} {y0+cell})">real</text>')
    lines += [f'<rect x="340" y="490" width="20" height="20" fill="{TEAL}"/><text x="370" y="507" class="small">acerto</text>',
              f'<rect x="520" y="490" width="20" height="20" fill="{RUST}"/><text x="550" y="507" class="small">erro</text>',
              '<text x="550" y="552" text-anchor="middle" class="small">ordem das células: verdadeiros negativos, falsos positivos, falsos negativos, verdadeiros positivos</text>']
    save("04_matrizes_confusao.svg", lines)


def group_chart(evaluation: pd.DataFrame) -> None:
    rows=[]
    for period, group in evaluation.groupby("periodo"):
        rows.append((period,len(group),metrics(group["classe_alvo"],group["previsto"])))
    lines=svg_open("Desempenho da árvore por período", "Barras mostram forte diferença de revocação entre os dois períodos no teste.")
    lines.append('<text x="550" y="42" text-anchor="middle" class="title">A média geral oculta onde os erros se concentram</text>')
    metrics_to_show=["Acurácia","Revocação","F1"]; colors=[NAVY,RUST,TEAL]
    for i,(period,n,vals) in enumerate(rows):
        x0=180+i*440
        lines.append(f'<text x="{x0+130}" y="105" text-anchor="middle" class="value">{escape(period)} · n={n}</text>')
        for j,m in enumerate(metrics_to_show):
            x=x0+j*95; h=vals[m]*320; y=455-h
            lines += [f'<rect x="{x}" y="{y:.1f}" width="68" height="{h:.1f}" fill="{colors[j]}" rx="4"/>',
                      f'<text x="{x+34}" y="{y-10:.1f}" text-anchor="middle" class="small">{vals[m]:.2f}</text>',
                      f'<text x="{x+34}" y="482" text-anchor="middle" class="small">{m[:3]}.</text>']
    lines.append('<text x="550" y="548" text-anchor="middle" class="small">Auditoria descritiva: grupos de vinte casos produzem estimativas instáveis</text>')
    save("05_metricas_periodo.svg",lines)


def terms_chart(terms: np.ndarray, coefficients: np.ndarray) -> None:
    frame=pd.DataFrame({"term":terms,"coef":coefficients})
    chosen=pd.concat([frame.nsmallest(4,"coef"),frame.nlargest(4,"coef")]).sort_values("coef")
    lines=svg_open("Termos associados às classes", "Barras à esquerda se associam a não relevante; barras à direita, a relevante.")
    lines.append('<text x="550" y="40" text-anchor="middle" class="title">O modelo aprende associações — inclusive atalhos</text>')
    center=555; scale=330/max(abs(chosen.coef)); lines.append(f'<line x1="{center}" y1="75" x2="{center}" y2="520" stroke="{NAVY}" stroke-width="2"/>')
    for i,row in enumerate(chosen.itertuples(index=False)):
        y=90+i*55; w=abs(row.coef)*scale; x=center if row.coef>=0 else center-w; color=TEAL if row.coef>=0 else PLUM
        lines += [f'<rect x="{x:.1f}" y="{y}" width="{w:.1f}" height="32" fill="{color}" rx="4"/>',
                  f'<text x="{center + (w+12 if row.coef>=0 else -w-12):.1f}" y="{y+23}" text-anchor="{"start" if row.coef>=0 else "end"}" class="small">{escape(row.term)}</text>']
    lines += ['<text x="210" y="555" text-anchor="middle" class="small">associado a “não relevante”</text>',
              '<text x="890" y="555" text-anchor="middle" class="small">associado a “relevante”</text>']
    save("06_termos_modelo.svg",lines)


def main() -> None:
    data=pd.read_csv(DATA/"documentos_classificacao.csv")
    annotations=pd.read_csv(DATA/"amostra_anotacao.csv")
    train,test=train_test_split(data,test_size=.25,random_state=42,stratify=data["classe_alvo"])
    predictions={}; result={}
    baseline=DummyClassifier(strategy="most_frequent").fit([[0]]*len(train),train["classe_alvo"])
    predictions["Linha de base"]=baseline.predict([[0]]*len(test)); result["Base"]=metrics(test["classe_alvo"],predictions["Linha de base"])
    columns=["periodo","origem"]
    for name,estimator in {
        "Logística":LogisticRegression(max_iter=1000,random_state=42),
        "Árvore":DecisionTreeClassifier(max_depth=3,min_samples_leaf=8,random_state=42),
    }.items():
        prep=ColumnTransformer([("categorias",OneHotEncoder(handle_unknown="ignore"),columns)])
        model=Pipeline([("preparo",prep),("modelo",estimator)]).fit(train[columns],train["classe_alvo"])
        predictions[name]=model.predict(test[columns]);result[name]=metrics(test["classe_alvo"],predictions[name])
    text_model=Pipeline([("tfidf",TfidfVectorizer(lowercase=True,ngram_range=(1,2),min_df=2)),("modelo",LogisticRegression(max_iter=1000,random_state=42))]).fit(train["texto"],train["classe_alvo"])
    predictions["TF-IDF"]=text_model.predict(test["texto"]);result["TF-IDF"]=metrics(test["classe_alvo"],predictions["TF-IDF"])
    agreement_chart(annotations);split_chart(train,test);comparison_chart(result)
    confusion_comparison({"Árvore · metadados":confusion_matrix(test["classe_alvo"],predictions["Árvore"],labels=["não relevante","relevante"]),"TF-IDF + logística":confusion_matrix(test["classe_alvo"],predictions["TF-IDF"],labels=["não relevante","relevante"])})
    group_chart(test.assign(previsto=predictions["Árvore"]))
    terms_chart(text_model.named_steps["tfidf"].get_feature_names_out(),text_model.named_steps["modelo"].coef_[0])
    print(f"Gráficos gravados em {OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
