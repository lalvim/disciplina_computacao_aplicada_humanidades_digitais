"""Valida links e células de preparação para uso das unidades no Colab."""

from __future__ import annotations

import json
from pathlib import Path

from apoio_colab import COLAB_GITHUB


RAIZ = Path(__file__).resolve().parents[1]
DEPENDENTES_DO_REPOSITORIO = {
    "unidade_01": {"03_dados_corpus_e_evidencias.ipynb"},
    "unidade_02": {
        "00_guia_da_unidade.ipynb",
        "01_fontes_populacao_e_selecao.ipynb",
        "02_cobertura_vieses_e_silencios.ipynb",
        "03_metadados_identificadores_e_proveniencia.ipynb",
        "04_governanca_reuso_e_documentacao_de_bases.ipynb",
    },
    "unidade_03": {
        "00_guia_da_unidade.ipynb",
        "01_formatos_importacao_e_extracao.ipynb",
        "02_estrutura_limpeza_e_qualidade.ipynb",
        "03_juncoes_integracao_e_reprodutibilidade.ipynb",
    },
    "unidade_04": {
        "00_guia_da_unidade.ipynb",
        "01_exploracao_quantitativa.ipynb",
        "02_exploracao_textual.ipynb",
        "03_visualizacao_exploratoria.ipynb",
    },
    "unidade_05": {
        "00_guia_da_unidade.ipynb",
        "01_estimativas_e_tamanhos_de_efeito.ipynb",
        "02_incerteza_e_testes_de_hipotese.ipynb",
        "03_representacao_vetorial_de_textos.ipynb",
        "04_similaridade_documentos_e_versoes.ipynb",
    },
    "unidade_06": {
        "00_guia_da_unidade.ipynb",
        "01_associacao_variaveis_categoricas.ipynb",
        "02_correlacao_variaveis_numericas.ipynb",
        "03_coocorrencia_e_matrizes_relacionais.ipynb",
        "04_grafos_centralidade_e_comunidades.ipynb",
    },
    "unidade_07": {
        "00_guia_da_unidade.ipynb",
        "01_regressao_linear_simples.ipynb",
        "02_regressao_multipla_e_categorias.ipynb",
        "03_interacoes_residuos_e_qualidade.ipynb",
        "04_regressao_logistica.ipynb",
    },
    "unidade_08": {
        "00_guia_da_unidade.ipynb",
        "01_categorias_anotacao_e_concordancia.ipynb",
        "02_treinamento_teste_e_linha_de_base.ipynb",
        "03_modelos_metricas_e_erros.ipynb",
        "04_classificacao_textual_tfidf_e_embeddings.ipynb",
    },
    "unidade_09": {
        "00_guia_da_unidade.ipynb",
        "01_padronizacao_distancia_e_kmeans.ipynb",
        "02_hierarquia_caracterizacao_e_estabilidade.ipynb",
        "03_agrupamento_de_documentos.ipynb",
        "04_modelagem_de_topicos_e_tempo.ipynb",
    },
    "unidade_10": {
        "00_guia_da_unidade.ipynb", "01_reconhecimento_de_entidades.ipynb",
        "02_desambiguacao_e_vinculacao.ipynb", "03_relacoes_eventos_e_tabelas.ipynb",
        "04_avaliacao_validacao_e_rede.ipynb",
    },
    "unidade_11": {
        "00_guia_da_unidade.ipynb", "01_datas_taxas_e_series.ipynb",
        "02_tendencias_medias_moveis_e_rupturas.ipynb", "03_temas_e_palavras_no_tempo.ipynb",
        "04_distribuicao_espacial_e_taxas.ipynb",
    },
    "unidade_12": {
        "00_guia_da_unidade.ipynb", "01_representacoes_e_transformers.ipynb",
        "02_tarefas_prompting_e_sensibilidade.ipynb", "03_recuperacao_aumentada_por_documentos.ipynb",
        "04_avaliacao_alucinacao_e_privacidade.ipynb",
    },
}


def fonte(celula: dict) -> str:
    valor = celula.get("source", "")
    return "".join(valor) if isinstance(valor, list) else valor


def main() -> None:
    readme_raiz = (RAIZ / "README.md").read_text(encoding="utf-8")
    total = preparacoes = 0

    for unidade, dependentes in DEPENDENTES_DO_REPOSITORIO.items():
        pasta = RAIZ / unidade
        notebooks = sorted(pasta.glob("*.ipynb"))
        esperados = 6 if unidade in {"unidade_02", "unidade_05", "unidade_06", "unidade_07", "unidade_08", "unidade_09", "unidade_10", "unidade_11", "unidade_12"} else 5
        assert len(notebooks) == esperados, (
            f"{unidade}: esperados {esperados} notebooks"
        )
        readme_unidade = (pasta / "README.md").read_text(encoding="utf-8")

        for caminho in notebooks:
            total += 1
            url = f"{COLAB_GITHUB}/{unidade}/{caminho.name}"
            documento = json.loads(caminho.read_text(encoding="utf-8"))
            fontes = [fonte(celula) for celula in documento["cells"]]

            assert sum(url in conteudo for conteudo in fontes) == 1, (
                f"{caminho}: link do Colab ausente ou duplicado"
            )
            assert url in readme_unidade, f"{caminho}: link ausente no README local"
            assert url in readme_raiz, f"{caminho}: link ausente no README principal"

            celulas_preparacao = [
                conteudo
                for conteudo in fontes
                if "# @title Preparação do ambiente" in conteudo
            ]
            esperado = caminho.name in dependentes
            assert len(celulas_preparacao) == int(esperado), (
                f"{caminho}: preparação incompatível com a dependência de arquivos"
            )
            if celulas_preparacao:
                preparacoes += 1
                codigo = celulas_preparacao[0]
                assert "git clone" not in codigo and "!git" not in codigo
                assert "subprocess.run" in codigo
                assert f"PASTA_UNIDADE = REPOSITORIO / {unidade!r}" in codigo
                compile(codigo, str(caminho), "exec")

    assert total == 69
    assert preparacoes == 54
    print(f"OK Colab: {total} links e {preparacoes} preparações seletivas")


if __name__ == "__main__":
    main()
