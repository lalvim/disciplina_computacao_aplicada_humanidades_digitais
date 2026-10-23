"""Reconstrói os gráficos calculados usados nos slides da Unidade 5."""

from __future__ import annotations

from collections import Counter
import importlib.util
import math
from pathlib import Path
import re
import unicodedata

import numpy as np
import pandas as pd


RAIZ = Path(__file__).resolve().parents[1]
PASTA_UNIDADE = RAIZ / "unidade_05"
DESTINO = RAIZ / "slides" / "imagens" / "unidade_05"


def carregar_modulo_graficos():
    especificacao = importlib.util.spec_from_file_location(
        "graficos_unidade_05", PASTA_UNIDADE / "graficos.py"
    )
    if especificacao is None or especificacao.loader is None:
        raise RuntimeError("Não foi possível carregar unidade_05/graficos.py")
    modulo = importlib.util.module_from_spec(especificacao)
    especificacao.loader.exec_module(modulo)
    return modulo


def salvar_svg(objeto, nome: str) -> None:
    DESTINO.mkdir(parents=True, exist_ok=True)
    (DESTINO / nome).write_text(objeto.data, encoding="utf-8")


def tokenizar(texto: str, stopwords: set[str]) -> list[str]:
    base = unicodedata.normalize("NFKD", texto.lower())
    base = "".join(c for c in base if not unicodedata.combining(c))
    return [t for t in re.findall(r"[a-z]+", base) if t not in stopwords]


def main() -> None:
    graficos = carregar_modulo_graficos()
    dados = pd.read_csv(PASTA_UNIDADE / "dados" / "documentos.csv")
    a = dados.loc[dados["local"].eq("Capital"), "palavras"].to_numpy()
    b = dados.loc[dados["local"].eq("Interior"), "palavras"].to_numpy()
    diferenca = float(a.mean() - b.mean())

    salvar_svg(
        graficos.estimativas_grupos(a, b, "Capital", "Interior"),
        "01_estimativas_grupos.svg",
    )

    rng = np.random.default_rng(20260906)
    bootstrap = np.array(
        [
            rng.choice(a, size=len(a), replace=True).mean()
            - rng.choice(b, size=len(b), replace=True).mean()
            for _ in range(4000)
        ]
    )
    salvar_svg(
        graficos.histograma_referencia(
            bootstrap, diferenca, "Distribuição bootstrap da diferença"
        ),
        "02_distribuicao_bootstrap.svg",
    )

    rng = np.random.default_rng(20260906)
    combinados = np.concatenate([a, b])
    n_a = len(a)
    permutadas = np.array(
        [
            (lambda valores: valores[:n_a].mean() - valores[n_a:].mean())(
                rng.permutation(combinados)
            )
            for _ in range(5000)
        ]
    )
    salvar_svg(
        graficos.histograma_referencia(
            permutadas, diferenca, "Diferenças sob permutação"
        ),
        "03_distribuicao_permutacao.svg",
    )

    textos = pd.read_csv(PASTA_UNIDADE / "dados" / "documentos_comparacao.csv")
    stopwords = {"a", "e", "o", "de", "do", "da", "em", "nas", "também"}
    contagens = [
        Counter(tokenizar(texto, stopwords)) for texto in textos["texto_comparacao"]
    ]
    matriz = pd.DataFrame(contagens, index=textos["id_documento"]).fillna(0).astype(int)
    matriz.index.name = "id_documento"
    salvar_svg(
        graficos.mapa_calor(
            matriz.iloc[:8, :12], "Recorte da matriz documento-termo"
        ),
        "04_matriz_documento_termo.svg",
    )

    intervalo = np.quantile(bootstrap, [0.025, 0.975])
    valor_p = (1 + np.sum(np.abs(permutadas) >= abs(diferenca))) / (
        len(permutadas) + 1
    )
    sem_extremo = dados.loc[~dados["id_documento"].eq("D023")]
    sensibilidade = (
        sem_extremo.loc[sem_extremo["local"].eq("Capital"), "palavras"].mean()
        - sem_extremo.loc[sem_extremo["local"].eq("Interior"), "palavras"].mean()
    )
    desvio_combinado = math.sqrt(
        ((len(a) - 1) * a.var(ddof=1) + (len(b) - 1) * b.var(ddof=1))
        / (len(a) + len(b) - 2)
    )
    print(f"Quatro gráficos gravados em {DESTINO.relative_to(RAIZ)}")
    print(
        {
            "media_capital": round(float(a.mean()), 3),
            "media_interior": round(float(b.mean()), 3),
            "diferenca": round(diferenca, 3),
            "d_padronizado": round(diferenca / desvio_combinado, 3),
            "sem_D023": round(float(sensibilidade), 3),
            "ic_bootstrap": [round(float(v), 3) for v in intervalo],
            "p_permutacao": round(float(valor_p), 4),
        }
    )


if __name__ == "__main__":
    main()

