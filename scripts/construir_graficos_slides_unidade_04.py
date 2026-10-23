"""Reconstrói os gráficos calculados usados nos slides da Unidade 4."""

from __future__ import annotations

from collections import Counter
import importlib.util
from pathlib import Path
import re

import pandas as pd


RAIZ = Path(__file__).resolve().parents[1]
PASTA_UNIDADE = RAIZ / "unidade_04"
DESTINO = RAIZ / "slides" / "imagens" / "unidade_04"


def carregar_modulo_graficos():
    especificacao = importlib.util.spec_from_file_location(
        "graficos_unidade_04", PASTA_UNIDADE / "graficos.py"
    )
    if especificacao is None or especificacao.loader is None:
        raise RuntimeError("Não foi possível carregar unidade_04/graficos.py")
    modulo = importlib.util.module_from_spec(especificacao)
    especificacao.loader.exec_module(modulo)
    return modulo


def salvar_svg(objeto, nome: str) -> None:
    DESTINO.mkdir(parents=True, exist_ok=True)
    (DESTINO / nome).write_text(objeto.data, encoding="utf-8")


def tokenizar(texto: str) -> list[str]:
    return re.findall(r"[a-záàâãéêíóôõúç]+", texto.lower())


def main() -> None:
    graficos = carregar_modulo_graficos()
    dados = pd.read_csv(PASTA_UNIDADE / "dados" / "documentos.csv")

    temas = dados["tema"].value_counts().sort_index()
    salvar_svg(
        graficos.barras_categorias(
            temas.index.tolist(),
            temas.tolist(),
            "Documentos por tema (n = 24)",
            "Tema atribuído",
            "Número de documentos",
            "Quatro barras de mesma altura mostram seis documentos em cada tema.",
        ),
        "00_barras_temas.svg",
    )

    palavras = dados["palavras"]
    salvar_svg(
        graficos.distribuicao_anotada(
            palavras.tolist(),
            dados["id_documento"].tolist(),
            palavras.mean(),
            palavras.median(),
        ),
        "01_centro_e_extremo.svg",
    )

    faixas = [0, 400, 600, 800, 1000, 2200]
    salvar_svg(
        graficos.histograma_boxplot(
            palavras.tolist(), faixas, dados["id_documento"].tolist()
        ),
        "02_histograma_boxplot.svg",
    )

    salvar_svg(
        graficos.dispersao(
            dados["paginas"].tolist(),
            palavras.tolist(),
            dados["genero"].tolist(),
            dados["id_documento"].tolist(),
            "Páginas e extensão dos documentos",
            "Páginas",
            "Palavras",
        ),
        "03_dispersao_paginas_palavras.svg",
    )

    resumo_anual = dados.groupby("ano")["palavras"].agg(n="size", media="mean")
    salvar_svg(
        graficos.serie_temporal(
            dados["ano"].tolist(),
            palavras.tolist(),
            dados["id_documento"].tolist(),
            resumo_anual["media"].to_dict(),
            resumo_anual["n"].to_dict(),
        ),
        "04_serie_temporal.svg",
    )

    tokens_por_documento = dados["texto"].map(tokenizar)
    todos_tokens = [token for documento in tokens_por_documento for token in documento]
    stopwords = {
        "a", "o", "e", "de", "do", "da", "como", "em", "nas", "um",
        "uma", "também",
    }
    tokens_conteudo = [token for token in todos_tokens if token not in stopwords]
    top = Counter(tokens_conteudo).most_common(10)
    tabela_termos = pd.DataFrame(top, columns=["termo", "frequencia"]).sort_values(
        "frequencia"
    )
    salvar_svg(
        graficos.barras_horizontais(
            tabela_termos["termo"].tolist(),
            tabela_termos["frequencia"].tolist(),
            f"Termos frequentes após stopwords (Nc = {len(tokens_conteudo)})",
            "Dez barras horizontais ordenadas mostram frequências absolutas dos tokens de conteúdo.",
        ),
        "05_frequencias_textuais.svg",
    )

    tamanhos = tokens_por_documento.map(len)
    tamanho_padrao = int(tamanhos.min())
    ttr = tokens_por_documento.map(lambda tokens: len(set(tokens)) / len(tokens))
    ttr_padronizada = tokens_por_documento.map(
        lambda tokens: len(set(tokens[:tamanho_padrao])) / tamanho_padrao
    )
    salvar_svg(
        graficos.ttr_duplo(
            tamanhos.tolist(),
            ttr.tolist(),
            ttr_padronizada.tolist(),
            tamanho_padrao,
        ),
        "06_ttr_bruta_padronizada.svg",
    )

    print(f"Sete gráficos gravados em {DESTINO.relative_to(RAIZ)}")


if __name__ == "__main__":
    main()

