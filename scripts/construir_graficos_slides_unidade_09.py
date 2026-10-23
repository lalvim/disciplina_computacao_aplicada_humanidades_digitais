"""Gera visualizações calculadas para os slides da Unidade 9.

Requer pandas, NumPy e scikit-learn, as mesmas dependências dos notebooks da
unidade. Todos os dados são fictícios.
"""

from __future__ import annotations

from html import escape
from pathlib import Path

import numpy as np
import pandas as pd
from scipy.optimize import linear_sum_assignment
from sklearn.cluster import AgglomerativeClustering, KMeans
from sklearn.decomposition import LatentDirichletAllocation
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.metrics import adjusted_rand_score, silhouette_score
from sklearn.preprocessing import StandardScaler


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "unidade_09" / "dados"
OUT = ROOT / "slides" / "imagens" / "unidade_09"
NAVY, TEAL, RUST, PLUM = "#17324d", "#176b68", "#a84f2a", "#69445f"
GRAY, LINE, PAPER = "#4b5563", "#d8cdbb", "#fffdf7"
COLORS = [TEAL, RUST, PLUM, NAVY, "#7b8f3d", "#bd7b2c"]


def svg_open(title: str, description: str) -> list[str]:
    return [
        '<svg xmlns="http://www.w3.org/2000/svg" width="1100" height="590" viewBox="0 0 1100 590" role="img">',
        f"<title>{escape(title)}</title>", f"<desc>{escape(description)}</desc>",
        f'<rect width="1100" height="590" fill="{PAPER}"/>',
        '<style>text{font-family:Aptos,Arial,sans-serif}.title{font-size:28px;font-weight:700;fill:#17324d}.label{font-size:19px;fill:#202a33}.small{font-size:16px;fill:#4b5563}.value{font-size:20px;font-weight:700;fill:#17324d}</style>',
    ]


def save(name: str, lines: list[str]) -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / name).write_text("\n".join(lines + ["</svg>", ""]), encoding="utf-8")


def aligned_labels(reference: np.ndarray, candidate: np.ndarray) -> np.ndarray:
    table = pd.crosstab(reference, candidate).to_numpy()
    rows, cols = linear_sum_assignment(-table)
    mapping = {col: row for row, col in zip(rows, cols)}
    return np.array([mapping[x] for x in candidate])


def scale_clusters(data: pd.DataFrame, raw: np.ndarray, standardized: np.ndarray) -> None:
    standardized = aligned_labels(raw, standardized)
    changed = raw != standardized
    lines = svg_open("Agrupamentos antes e depois da padronização", "Dois painéis mostram os mesmos casos; dezoito mudam de grupo após a padronização.")
    lines.append('<text x="550" y="38" text-anchor="middle" class="title">A mesma instituição pode ganhar outros vizinhos</text>')
    xmin, xmax = data.eventos_ano.min(), data.eventos_ano.max(); ymin, ymax = data.orcamento_anual.min(), data.orcamento_anual.max()
    def draw(panel_x, labels, title):
        left, top, width, height = panel_x, 105, 400, 365
        sx=lambda v:left+(v-xmin)/(xmax-xmin)*width
        sy=lambda v:top+height-(v-ymin)/(ymax-ymin)*height
        lines.extend([f'<rect x="{left}" y="{top}" width="{width}" height="{height}" fill="#f5f0e6" stroke="{LINE}"/>',
                      f'<text x="{left+width/2}" y="82" text-anchor="middle" class="value">{title}</text>'])
        for idx,row in data.iterrows():
            stroke=NAVY if changed[idx] else "white"; sw=2.5 if changed[idx] else 1
            lines.append(f'<circle cx="{sx(row.eventos_ano):.1f}" cy="{sy(row.orcamento_anual):.1f}" r="5.5" fill="{COLORS[labels[idx]]}" fill-opacity="0.75" stroke="{stroke}" stroke-width="{sw}"/>')
        lines.extend([f'<text x="{left+width/2}" y="505" text-anchor="middle" class="small">eventos por ano</text>',
                      f'<text x="{left-30}" y="{top+height/2}" text-anchor="middle" class="small" transform="rotate(-90 {left-30} {top+height/2})">orçamento</text>'])
    draw(100, raw, "sem padronizar"); draw(600, standardized, "padronizado")
    lines += [f'<circle cx="410" cy="548" r="7" fill="white" stroke="{NAVY}" stroke-width="3"/><text x="430" y="554" class="small">18 de 120 mudaram de grupo</text>',
              '<text x="785" y="554" class="small">cores = grupos após alinhar apenas os números</text>']
    save("01_efeito_padronizacao.svg", lines)


def k_diagnostics(values: list[dict]) -> None:
    lines=svg_open("Inércia e silhueta por número de grupos", "A inércia cai continuamente; a silhueta atinge maior valor em três grupos.")
    lines.append('<text x="550" y="38" text-anchor="middle" class="title">Nenhuma curva escolhe a interpretação por nós</text>')
    panels=[(90, "Inércia", "inercia", 0, max(x["inercia"] for x in values)*1.12),(610,"Silhueta","silhueta",0,0.75)]
    for left,title,key,ymin,ymax in panels:
        top,width,height=100,390,350; sx=lambda k:left+(k-2)/4*width; sy=lambda v:top+height-(v-ymin)/(ymax-ymin)*height
        lines += [f'<rect x="{left}" y="{top}" width="{width}" height="{height}" fill="#f5f0e6" stroke="{LINE}"/>',f'<text x="{left+width/2}" y="82" text-anchor="middle" class="value">{title}</text>']
        points=" ".join(f'{sx(x["k"]):.1f},{sy(x[key]):.1f}' for x in values); lines.append(f'<polyline points="{points}" fill="none" stroke="{RUST if key=="inercia" else TEAL}" stroke-width="4"/>')
        for x in values:
            lines += [f'<circle cx="{sx(x["k"]):.1f}" cy="{sy(x[key]):.1f}" r="7" fill="{RUST if key=="inercia" else TEAL}"/>',
                      f'<text x="{sx(x["k"]):.1f}" y="480" text-anchor="middle" class="small">{x["k"]}</text>',
                      f'<text x="{sx(x["k"]):.1f}" y="{sy(x[key])-12:.1f}" text-anchor="middle" class="small">{x[key]:.3f}</text>']
        lines.append(f'<text x="{left+width/2}" y="520" text-anchor="middle" class="small">número de grupos k</text>')
    save("02_inercia_silhueta.svg",lines)


def profile_heatmap(data: pd.DataFrame, labels: np.ndarray, variables: list[str]) -> None:
    z=pd.DataFrame(StandardScaler().fit_transform(data[variables]),columns=variables).assign(cluster=labels)
    means=z.groupby("cluster").mean()
    names=["acervo","eventos","público","orçamento"]
    lines=svg_open("Perfis padronizados dos grupos", "Mapa de calor mostra médias padronizadas de quatro variáveis em três grupos.")
    lines.append('<text x="550" y="40" text-anchor="middle" class="title">Descreva os perfis antes de nomeá-los</text>')
    x0,y0,cw,ch=295,120,155,110
    for j,name in enumerate(names):lines.append(f'<text x="{x0+j*cw+cw/2}" y="100" text-anchor="middle" class="small">{name}</text>')
    for i in range(3):
        lines.append(f'<text x="{x0-25}" y="{y0+i*ch+ch/2+6}" text-anchor="end" class="label">Grupo {i}</text>')
        for j,var in enumerate(variables):
            val=means.loc[i,var]; color=TEAL if val>=0 else PLUM; opacity=.18+min(abs(val)/1.5,.82)
            lines += [f'<rect x="{x0+j*cw}" y="{y0+i*ch}" width="{cw}" height="{ch}" fill="{color}" fill-opacity="{opacity:.2f}" stroke="white" stroke-width="3"/>',
                      f'<text x="{x0+j*cw+cw/2}" y="{y0+i*ch+ch/2+8}" text-anchor="middle" font-size="24" font-weight="700" fill="{NAVY}">{val:+.2f}</text>']
    lines += [f'<rect x="330" y="500" width="22" height="22" fill="{PLUM}" fill-opacity=".65"/><text x="363" y="518" class="small">abaixo da média</text>',
              f'<rect x="590" y="500" width="22" height="22" fill="{TEAL}" fill-opacity=".65"/><text x="623" y="518" class="small">acima da média</text>']
    save("03_perfis_grupos.svg",lines)


def stability_chart(values: list[float]) -> None:
    lines=svg_open("Estabilidade em vinte subamostras", "Vinte barras atingem ARI igual a um na base sintética.")
    lines.append('<text x="550" y="40" text-anchor="middle" class="title">Estabilidade perfeita também precisa de contexto</text>')
    left,top,width,height=95,100,900,350; bw=width/len(values)-6
    for i,val in enumerate(values):
        x=left+i*(bw+6); h=val*height
        lines.append(f'<rect x="{x:.1f}" y="{top+height-h:.1f}" width="{bw:.1f}" height="{h:.1f}" fill="{TEAL}" rx="3"/>')
    lines += [f'<line x1="{left}" y1="{top}" x2="{left+width}" y2="{top}" stroke="{NAVY}" stroke-dasharray="7 5"/>',
              '<text x="70" y="106" text-anchor="end" class="small">1,0</text>',
              '<text x="550" y="500" text-anchor="middle" class="small">20 subamostras de 80% dos casos</text>',
              '<text x="550" y="545" text-anchor="middle" class="label">Resultado esperado de perfis didáticos muito separados — não garantia externa</text>']
    save("04_estabilidade.svg",lines)


def text_clusters(terms: np.ndarray, centers: np.ndarray, counts: np.ndarray) -> None:
    lines=svg_open("Termos característicos dos agrupamentos textuais", "Três cartões apresentam termos associados a educação, saúde e cultura.")
    lines.append('<text x="550" y="40" text-anchor="middle" class="title">Os termos sugerem nomes; os documentos podem contestá-los</text>')
    labels=["hipótese: educação","hipótese: saúde","hipótese: cultura"]
    for c in range(3):
        x=65+c*345; top=100; top_terms=terms[centers[c].argsort()[-6:][::-1]]
        lines += [f'<rect x="{x}" y="{top}" width="310" height="385" rx="14" fill="#f2eee5" stroke="{COLORS[c]}" stroke-width="5"/>',
                  f'<text x="{x+155}" y="{top+48}" text-anchor="middle" class="value">Grupo {c} · n={counts[c]}</text>',
                  f'<text x="{x+155}" y="{top+84}" text-anchor="middle" class="small">{labels[c]}</text>']
        for j,term in enumerate(top_terms):lines.append(f'<text x="{x+35}" y="{top+135+j*39}" class="label">• {escape(term)}</text>')
    lines.append('<text x="550" y="545" text-anchor="middle" class="small">Silhueta cosseno = 0,434 · nomes são interpretações provisórias</text>')
    save("05_clusters_textuais.svg",lines)


def topic_evolution(evolution: pd.DataFrame) -> None:
    lines=svg_open("Mistura média de tópicos por período", "Três linhas mostram proporções médias de componentes probabilísticos em três períodos.")
    lines.append('<text x="550" y="40" text-anchor="middle" class="title">Uma curva temporal descreve a composição do corpus</text>')
    left,top,width,height=120,90,820,390; periods=list(evolution.index); sx=lambda i:left+i/(len(periods)-1)*width; sy=lambda v:top+height-v*height
    for tick in [0,.25,.5,.75,1]:
        y=sy(tick);lines += [f'<line x1="{left}" y1="{y}" x2="{left+width}" y2="{y}" stroke="{LINE}"/>',f'<text x="95" y="{y+5}" text-anchor="end" class="small">{tick:.2f}</text>']
    for t,col in enumerate(evolution.columns):
        pts=" ".join(f'{sx(i):.1f},{sy(v):.1f}' for i,v in enumerate(evolution[col]));lines.append(f'<polyline points="{pts}" fill="none" stroke="{COLORS[t]}" stroke-width="4"/>')
        for i,v in enumerate(evolution[col]):lines += [f'<circle cx="{sx(i):.1f}" cy="{sy(v):.1f}" r="7" fill="{COLORS[t]}"/>',f'<text x="{sx(i):.1f}" y="{sy(v)-12:.1f}" text-anchor="middle" class="small">{v:.3f}</text>']
    for i,p in enumerate(periods):lines.append(f'<text x="{sx(i):.1f}" y="510" text-anchor="middle" class="small">{escape(str(p))}</text>')
    for t in range(3):lines += [f'<line x1="{965}" y1="{145+t*42}" x2="{1010}" y2="{145+t*42}" stroke="{COLORS[t]}" stroke-width="5"/>',f'<text x="1020" y="{151+t*42}" class="small">Tópico {t}</text>']
    lines.append('<text x="550" y="560" text-anchor="middle" class="small">Mudança na média não demonstra mudança histórica sem inspeção das fontes e da composição</text>')
    save("06_evolucao_topicos.svg",lines)


def main() -> None:
    institutions=pd.read_csv(DATA/"instituicoes_culturais.csv"); documents=pd.read_csv(DATA/"documentos_temas.csv")
    variables=["itens_acervo","eventos_ano","publico_ano","orcamento_anual"]
    x=institutions[variables];xz=StandardScaler().fit_transform(x)
    raw=KMeans(n_clusters=3,random_state=42,n_init=20).fit_predict(x)
    model=KMeans(n_clusters=3,random_state=42,n_init=20).fit(xz);labels=model.labels_
    evaluations=[]
    for k in range(2,7):
        m=KMeans(n_clusters=k,random_state=42,n_init=20).fit(xz);evaluations.append({"k":k,"inercia":m.inertia_,"silhueta":silhouette_score(xz,m.labels_)})
    rng=np.random.default_rng(42);stability=[]
    for repetition in range(20):
        idx=np.sort(rng.choice(len(xz),size=int(.8*len(xz)),replace=False));partial=KMeans(n_clusters=3,random_state=repetition,n_init=20).fit_predict(xz[idx]);stability.append(adjusted_rand_score(labels[idx],partial))
    vectorizer=TfidfVectorizer(min_df=2,ngram_range=(1,2),stop_words=None);xt=vectorizer.fit_transform(documents.texto);text_model=KMeans(n_clusters=3,random_state=42,n_init=20).fit(xt)
    counter=CountVectorizer(min_df=2);xc=counter.fit_transform(documents.texto);lda=LatentDirichletAllocation(n_components=3,random_state=42,learning_method="batch",max_iter=80,doc_topic_prior=.1,topic_word_prior=.1);mix=lda.fit_transform(xc)
    evolution=pd.DataFrame(mix,columns=["t0","t1","t2"]).assign(periodo=documents.periodo).groupby("periodo")[["t0","t1","t2"]].mean()
    scale_clusters(institutions,raw,labels);k_diagnostics(evaluations);profile_heatmap(institutions,labels,variables);stability_chart(stability)
    text_clusters(vectorizer.get_feature_names_out(),text_model.cluster_centers_,np.bincount(text_model.labels_));topic_evolution(evolution)
    print(f"Gráficos gravados em {OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
