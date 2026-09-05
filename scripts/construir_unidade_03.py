"""Gera dados, notebooks e README da Unidade 3."""

from __future__ import annotations

import csv
import json
import re
from datetime import datetime
from pathlib import Path
from textwrap import dedent
from xml.etree import ElementTree as ET
from zipfile import ZipFile, ZipInfo

import pandas as pd
from PIL import Image, ImageDraw, ImageFilter, ImageFont

from apoio_colab import adicionar_link_na_abertura, preparacao_colab, tabela_links_colab
from construir_imagens_unidade_03 import main as construir_imagens


RAIZ = Path(__file__).resolve().parents[1]
UNIDADE = RAIZ / "unidade_03"
BRUTOS = UNIDADE / "dados" / "brutos"
INTERMEDIARIOS = UNIDADE / "dados" / "intermediarios"
DERIVADOS = UNIDADE / "dados" / "derivados"
DATA_ARQUIVO_DIDATICO = datetime(2026, 7, 31, 12, 0, 0)


def md(conteudo: str) -> dict:
    return {"cell_type": "markdown", "metadata": {}, "source": dedent(conteudo).strip().splitlines(keepends=True)}


def code(conteudo: str) -> dict:
    return {"cell_type": "code", "execution_count": None, "metadata": {}, "outputs": [], "source": dedent(conteudo).strip().splitlines(keepends=True)}


def salvar_notebook(
    nome: str,
    celulas: list[dict],
    requer_repositorio: bool = False,
) -> None:
    publicadas = [adicionar_link_na_abertura(celulas[0], UNIDADE.name, nome)]
    if requer_repositorio:
        publicadas.append(
            code(
                preparacao_colab(
                    UNIDADE.name,
                    pacotes=(
                        ("openpyxl", "openpyxl>=3.1,<4"),
                        ("pypdf", "pypdf>=5,<6"),
                        ("PIL", "Pillow>=11,<12"),
                    ),
                )
            )
        )
    publicadas.extend(celulas[1:])
    doc = {
        "cells": publicadas,
        "metadata": {
            "kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"},
            "language_info": {"name": "python", "version": "3"},
        },
        "nbformat": 4,
        "nbformat_minor": 5,
    }
    (UNIDADE / nome).write_text(json.dumps(doc, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")


def salvar_xlsx_reprodutivel(tabela: pd.DataFrame, caminho: Path) -> None:
    """Grava o XLSX sem datas variáveis no conteúdo ou no contêiner ZIP."""

    with pd.ExcelWriter(caminho, engine="openpyxl") as escritor:
        tabela.to_excel(escritor, index=False, sheet_name="documentos")
        escritor.book.properties.created = DATA_ARQUIVO_DIDATICO
        escritor.book.properties.modified = DATA_ARQUIVO_DIDATICO

    temporario = caminho.with_suffix(".xlsx.tmp")
    with ZipFile(caminho, "r") as origem, ZipFile(temporario, "w") as destino:
        for info in origem.infolist():
            normalizado = ZipInfo(info.filename, (2026, 7, 31, 12, 0, 0))
            normalizado.compress_type = info.compress_type
            normalizado.external_attr = info.external_attr
            normalizado.create_system = info.create_system
            conteudo = origem.read(info.filename)
            if info.filename == "docProps/core.xml":
                conteudo = re.sub(
                    rb"(<dcterms:modified[^>]*>)[^<]+(</dcterms:modified>)",
                    rb"\g<1>2026-07-31T12:00:00Z\g<2>",
                    conteudo,
                )
            destino.writestr(normalizado, conteudo)
    temporario.replace(caminho)


def pdf_textual(caminho: Path, texto: str) -> None:
    seguro = texto.replace("\\", "\\\\").replace("(", "\\(").replace(")", "\\)")
    fluxo = f"BT /F1 14 Tf 72 720 Td ({seguro}) Tj ET".encode("latin-1")
    objetos = [
        b"<< /Type /Catalog /Pages 2 0 R >>",
        b"<< /Type /Pages /Kids [3 0 R] /Count 1 >>",
        b"<< /Type /Page /Parent 2 0 R /MediaBox [0 0 612 792] /Resources << /Font << /F1 4 0 R >> >> /Contents 5 0 R >>",
        b"<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica >>",
        b"<< /Length " + str(len(fluxo)).encode() + b" >>\nstream\n" + fluxo + b"\nendstream",
    ]
    saida = bytearray(b"%PDF-1.4\n")
    offsets = [0]
    for numero, objeto in enumerate(objetos, 1):
        offsets.append(len(saida))
        saida.extend(f"{numero} 0 obj\n".encode() + objeto + b"\nendobj\n")
    xref = len(saida)
    saida.extend(f"xref\n0 {len(objetos)+1}\n".encode())
    saida.extend(b"0000000000 65535 f \n")
    for offset in offsets[1:]:
        saida.extend(f"{offset:010d} 00000 n \n".encode())
    saida.extend(f"trailer << /Size {len(objetos)+1} /Root 1 0 R >>\nstartxref\n{xref}\n%%EOF\n".encode())
    caminho.write_bytes(saida)


def criar_dados() -> None:
    for pasta in [BRUTOS, INTERMEDIARIOS, DERIVADOS]:
        pasta.mkdir(parents=True, exist_ok=True)

    linhas = [
        ["D001", " Jornal Aurora ", "1890-01-05", "São Paulo", "3550308", "Editorial", "860"],
        ["D002", "gazeta popular", "06/02/1891", "Sao paulo", "3550308", "notícia", "610"],
        ["D003", "Correio do Vale", "1892", "Belo Horizonte", "3106200", "Carta", ""],
        ["D004", "JORNAL AURORA", "1893-03-12", "São  Paulo", "3550308", "editorial ", "940"],
        ["D005", "Gazeta Popular", "data desconhecida", "Rio de Janeiro", "3304557", "Noticia", "720"],
        ["D006", "Correio do Vale", "1900-08-20", "Belo Horizonte", "3106200", "carta", "420"],
        ["D006-copia", " Correio do Vale ", "20/08/1900", "Belo horizonte", "3106200", "Carta", "420"],
        ["D007", "Boletim Operário", "1901-04-09", "Recife", "2611606", "manifesto", "500"],
    ]
    with (BRUTOS / "catalogo_messy.csv").open("w", encoding="utf-8", newline="") as arq:
        w = csv.writer(arq, delimiter=";")
        w.writerow(["id_documento", "titulo", "data_documento", "municipio", "codigo_municipio", "genero", "palavras"])
        w.writerows(linhas)

    salvar_xlsx_reprodutivel(
        pd.DataFrame(
            linhas,
            columns=[
                "id_documento",
                "titulo",
                "data_documento",
                "municipio",
                "codigo_municipio",
                "genero",
                "palavras",
            ],
        ),
        BRUTOS / "catalogo_messy.xlsx",
    )
    metadados = [
        {"id_documento": "D001", "arquivo_texto": "D001.txt", "temas": ["educação", "progresso"]},
        {"id_documento": "D002", "arquivo_texto": "D002.txt", "temas": ["trabalho"]},
        {"id_documento": "D003", "arquivo_texto": None, "temas": ["educação"]},
    ]
    (BRUTOS / "metadados.json").write_text(json.dumps(metadados, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    raiz_xml = ET.Element("colecao")
    for item in metadados[:2]:
        doc = ET.SubElement(raiz_xml, "documento", id=item["id_documento"])
        ET.SubElement(doc, "arquivo").text = item["arquivo_texto"]
        ET.SubElement(doc, "tema").text = item["temas"][0]
    ET.ElementTree(raiz_xml).write(BRUTOS / "metadados.xml", encoding="utf-8", xml_declaration=True)

    (BRUTOS / "D001.txt").write_text("A escola noturna foi apresentada como sinal de progresso.\n", encoding="utf-8")
    (BRUTOS / "D002.txt").write_text("O jornal discutiu jornadas de trabalho e instrução.\n", encoding="utf-8")
    pdf_textual(BRUTOS / "documento_textual.pdf", "Documento D001 com camada textual")

    referencia_ocr = "ESCOLA NOTURNA E TRABALHO — 1890"
    imagem = Image.new("L", (1400, 260), "#f8f3e7")
    desenho = ImageDraw.Draw(imagem)
    try:
        fonte_ocr = ImageFont.truetype("DejaVuSerif.ttf", 58)
    except OSError:
        fonte_ocr = ImageFont.load_default()
    desenho.text((80, 86), referencia_ocr, font=fonte_ocr, fill="#26231f")
    desenho.line((55, 55, 1345, 55), fill="#b7aa91", width=2)
    desenho.line((55, 205, 1345, 205), fill="#b7aa91", width=2)
    imagem.save(BRUTOS / "pagina_digitalizada.png")

    degradada = imagem.resize((770, 143)).resize((1400, 260))
    degradada = degradada.rotate(0.65, resample=Image.Resampling.BICUBIC, fillcolor="#f8f3e7")
    degradada = degradada.filter(ImageFilter.GaussianBlur(1.15))
    marcas = ImageDraw.Draw(degradada)
    for x, y, raio in [(155, 92, 15), (393, 170, 9), (690, 72, 12), (1020, 181, 17), (1275, 105, 8)]:
        marcas.ellipse((x - raio, y - raio, x + raio, y + raio), fill="#cfc3ad")
    for x in [245, 744, 1130]:
        marcas.line((x, 38, x + 5, 222), fill="#ded5c4", width=3)
    degradada.save(BRUTOS / "pagina_digitalizada_degradada.png")

    (BRUTOS / "ocr_referencia.txt").write_text(referencia_ocr + "\n", encoding="utf-8")
    (BRUTOS / "ocr_precomputado.txt").write_text(referencia_ocr + "\n", encoding="utf-8")
    (BRUTOS / "ocr_precomputado_degradado.txt").write_text(
        "ESC0LA NOTURNA E TRABALH0 — 189O\n", encoding="utf-8"
    )

    largo = pd.DataFrame({
        "id_documento": ["D001", "D002", "D003"],
        "educacao_1890": [3, 0, 2], "trabalho_1890": [1, 4, 0],
        "educacao_1900": [2, 1, 3], "trabalho_1900": [2, 5, 1],
    })
    largo.to_csv(BRUTOS / "indicadores_largos.csv", index=False)

    municipios = pd.DataFrame([
        ["3550308", "São Paulo", "SP"], ["3106200", "Belo Horizonte", "MG"],
        ["3304557", "Rio de Janeiro", "RJ"], ["2611606", "Recife", "PE"],
    ], columns=["codigo_municipio", "nome_municipio_ibge", "uf"])
    municipios.to_csv(BRUTOS / "extrato_codigos_municipios_ibge.csv", index=False)
    proveniencia = {
        "arquivo": "extrato_codigos_municipios_ibge.csv",
        "fonte": "IBGE — Códigos dos Municípios",
        "url": "https://www.ibge.gov.br/explica/codigos-dos-municipios.php",
        "data_de_acesso": "2026-07-31",
        "nota": "extrato didático de quatro registros; códigos devem ser reverificados antes de reutilização",
    }
    (BRUTOS / "proveniencia_base_publica.json").write_text(json.dumps(proveniencia, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def guia() -> list[dict]:
    return [
        md("""
        # Unidade 3 — Guia de estudo

        ## Como transformar fontes em dados analisáveis?

        **Problema orientador:** como preparar documentos e registros produzidos em
        formatos diferentes sem perder a ligação com as fontes e decisões?

        O protocolo da Unidade 2 definiu o que coletar. Agora construiremos uma
        primeira base processável. “Limpar” não significa tornar os dados neutros:
        significa aplicar regras explícitas, preservar originais, testar resultados e
        documentar perdas. Rawson e Muñoz (2019) alertam que a ideia de limpeza pode
        ocultar trabalho interpretativo e relações de autoridade.

        ![Fontes em papel, imagem e tabela atravessam camadas transparentes de transformação e produzem tabelas, relações e segmentos de texto sempre ligados aos originais preservados.](imagens/00_abertura_conceitual.png)

        A ilustração antecipa o argumento central: transformar não rompe o vínculo
        com a fonte. Cada produto derivado precisa manter um caminho de retorno às
        entradas, regras e decisões que o produziram.
        """),
        md("""
        ## Objetivos e percurso

        | Notebook | Questão | Produto |
        |---|---|---|
        | 00 | Como trabalhar sem perder rastros? | Diagnóstico |
        | 01 | Como ler formatos e extrair texto? | Inventário técnico |
        | 02 | Como estruturar e corrigir com cautela? | Tabela intermediária |
        | 03 | Como juntar e integrar sem criar casos? | Base integrada |
        | 04 | A base está processável e auditável? | Primeira versão da base |

        A unidade usa dados fictícios deliberadamente inconsistentes e um pequeno
        extrato didático dos códigos de municípios do IBGE, acompanhado de
        proveniência. Não há coleta pela internet durante a execução.

        ![Quatro etapas ligam leitura de formatos, estruturação, integração e empacotamento; os dados brutos permanecem preservados e uma seta de retorno representa auditoria e revisão.](imagens/00_percurso_unidade.svg)

        O percurso é cumulativo: cada notebook produz uma representação que será
        retomada pelo seguinte. Testes e limites podem exigir retorno a qualquer
        decisão anterior.
        """),
        code("""
        from pathlib import Path
        import pandas as pd

        raiz_dados = Path("dados")
        bruto = pd.read_csv(raiz_dados / "brutos" / "catalogo_messy.csv", sep=";")
        print("Registros brutos:", len(bruto))
        print("Arquivos brutos:", len(list((raiz_dados / "brutos").iterdir())))
        bruto.head(3)
        """),
        md("""
        ## Regra de ouro: camadas, não sobrescrita

        - `brutos/`: cópias recebidas, imutáveis;
        - `intermediarios/`: resultados de etapas verificáveis;
        - `derivados/`: produtos destinados à análise;
        - notebooks: ordem e justificativa das operações.

        Uma cópia bruta não é “verdade original”; ela é o ponto de entrada preservado
        do fluxo. Proveniência continua necessária.

        ## Diagnóstico

        Que transformações seu projeto exigirá? Quais podem alterar sentido, unidade
        ou quantidade de registros? **Resposta:** Escreva aqui.
        """),
        md("""
        ## Produto e avaliação

        A entrega incluirá inventário, código executável, tabela processável, log de
        transformações, testes de chaves/junções, amostra de controle de OCR e limites.
        Frequências substantivas, gráficos e hipóteses exploratórias pertencem à
        Unidade 4. Consulte `referencias.md` para leituras completas.
        """),
    ]


def formatos() -> list[dict]:
    return [
        md("""
        # Formatos, importação e extração

        ## 1. Formato é estrutura e affordance

        CSV registra uma tabela sem fórmulas ou tipos ricos; XLSX pode conter várias
        planilhas, fórmulas e formatação; JSON e XML expressam hierarquias; TXT não
        define internamente como interpretar seu conteúdo; PDF busca preservar uma
        apresentação de página e pode conter texto, imagem ou ambos. Extensão não
        garante conteúdo nem qualidade.
        """),
        code("""
        import json
        from pathlib import Path
        from xml.etree import ElementTree as ET
        import pandas as pd

        pasta = Path("dados/brutos")
        csv_df = pd.read_csv(pasta / "catalogo_messy.csv", sep=";")
        xlsx_df = pd.read_excel(pasta / "catalogo_messy.xlsx", sheet_name="documentos")
        json_data = json.loads((pasta / "metadados.json").read_text(encoding="utf-8"))
        xml_raiz = ET.parse(pasta / "metadados.xml").getroot()
        txt = (pasta / "D001.txt").read_text(encoding="utf-8")

        print("CSV/XLSX iguais nas dimensões:", csv_df.shape == xlsx_df.shape)
        print("Registros JSON:", len(json_data), "| XML:", len(xml_raiz))
        print("TXT:", txt.strip())
        """),
        md("""
        ### Interpretação

        Leitores diferentes retornam objetos diferentes. Importar com sucesso não
        prova que encoding, separador, planilha, hierarquia ou tipos foram interpretados
        corretamente. Registre parâmetros, versão da fonte e testes esperados.
        """),
        md("""
        ## 2. Base pública sem dependência de rede

        O arquivo `extrato_codigos_municipios_ibge.csv` é uma cópia local pequena da
        tabela do IBGE. O JSON de proveniência registra página, acesso e recorte. Uma
        base pública muda; por isso, citar “IBGE” sem versão/data não basta.
        """),
        code("""
        municipios = pd.read_csv(
            pasta / "extrato_codigos_municipios_ibge.csv",
            dtype={"codigo_municipio": "string"},
        )
        proveniencia = json.loads(
            (pasta / "proveniencia_base_publica.json").read_text(encoding="utf-8")
        )
        print(proveniencia["fonte"], "— acesso:", proveniencia["data_de_acesso"])
        municipios
        """),
        md("""
        ## 3. Extração de PDF não é OCR

        Se o PDF contém caracteres, um leitor pode extrair a camada textual. Se cada
        página é apenas imagem, a extração retorna pouco ou nada e será necessário OCR.
        Mesmo PDF com texto pode ter ordem de leitura problemática, hifenização ou
        caracteres incorretos.

        ![Um arquivo PDF passa pelo teste de texto selecionável: quando há texto, extrai-se a camada textual; quando não há, aplica-se OCR; as duas rotas exigem avaliação contra a página.](imagens/01_pdf_texto_imagem_ocr.svg)

        O diagrama evita uma confusão frequente: OCR não é sinônimo de “abrir PDF”.
        Primeiro se diagnostica o conteúdo; depois se escolhe e avalia a operação.
        """),
        code("""
        from pypdf import PdfReader

        leitor = PdfReader(pasta / "documento_textual.pdf")
        texto_pdf = "\\n".join(pagina.extract_text() or "" for pagina in leitor.pages)
        print(texto_pdf.strip())
        """),
        md("""
        ## 4. OCR como hipótese de transcrição

        OCR reconhece caracteres em imagem. Resolução, inclinação, ruído, layout,
        fonte e idioma afetam o resultado. A documentação do Tesseract recomenda
        inspecionar e preparar imagens quando necessário. A transcrição deve ser
        vinculada à imagem, à ferramenta, aos parâmetros e a uma avaliação de erro.

        As duas imagens abaixo são **simulações didáticas**, não documentos
        históricos. Elas contêm a mesma linha: a primeira está limpa; a segunda foi
        reduzida, ampliada, inclinada, desfocada e marcada de forma controlada.

        ![Linha tipográfica sintética limpa usada como referência no experimento controlado de reconhecimento óptico de caracteres.](dados/brutos/pagina_digitalizada.png)

        ![A mesma linha tipográfica sintética após redução, ampliação, inclinação, desfoque e marcas controladas que dificultam o reconhecimento óptico de caracteres.](dados/brutos/pagina_digitalizada_degradada.png)
        """),
        code("""
        import shutil
        import subprocess

        entradas_ocr = [
            ("imagem limpa", pasta / "pagina_digitalizada.png", pasta / "ocr_precomputado.txt"),
            ("imagem degradada", pasta / "pagina_digitalizada_degradada.png", pasta / "ocr_precomputado_degradado.txt"),
        ]

        def reconhecer_ou_carregar(imagem, precomputado):
            if shutil.which("tesseract"):
                try:
                    processo = subprocess.run(
                        ["tesseract", str(imagem), "stdout", "-l", "eng", "--psm", "7"],
                        capture_output=True, text=True, check=True,
                    )
                    return processo.stdout.strip(), "Tesseract executado agora"
                except subprocess.CalledProcessError:
                    pass
            return (
                precomputado.read_text(encoding="utf-8").strip(),
                "saída pré-computada fornecida com o material",
            )

        resultados_ocr = []
        for condicao, imagem, precomputado in entradas_ocr:
            transcricao, origem = reconhecer_ou_carregar(imagem, precomputado)
            resultados_ocr.append({"condição": condicao, "transcrição": transcricao, "origem": origem})

        pd.DataFrame(resultados_ocr)
        """),
        code("""
        referencia = (pasta / "ocr_referencia.txt").read_text(encoding="utf-8").strip()

        def distancia_edicao(a, b):
            anterior = list(range(len(b) + 1))
            for i, item_a in enumerate(a, 1):
                atual = [i]
                for j, item_b in enumerate(b, 1):
                    atual.append(min(
                        atual[-1] + 1,
                        anterior[j] + 1,
                        anterior[j - 1] + (item_a != item_b),
                    ))
                anterior = atual
            return anterior[-1]

        comparacao = []
        for resultado in resultados_ocr:
            observado = resultado["transcrição"]
            comparacao.append({
                "condição": resultado["condição"],
                "erros em caracteres": distancia_edicao(referencia, observado),
                "CER": distancia_edicao(referencia, observado) / len(referencia),
                "erros em palavras": distancia_edicao(referencia.split(), observado.split()),
                "WER": distancia_edicao(referencia.split(), observado.split()) / len(referencia.split()),
            })

        pd.DataFrame(comparacao).round({"CER": 3, "WER": 3})
        """),
        md("""
        ### Como interpretar a comparação

        CER é a taxa de erro por caractere; WER, por palavra. Zero significa
        coincidência com a transcrição de referência nesta amostra. Valores maiores
        indicam mais edições necessárias, mas **não decidem sozinhos** se o texto é
        adequado: busca exploratória, citação e análise lexical exigem tolerâncias
        diferentes. Uma referência também pode conter erro humano; por isso, a
        página e o protocolo de transcrição continuam indispensáveis.

        ## Atividade — inventário técnico

        Para cada fonte do projeto, registre formato, estrutura interna, leitor,
        encoding/planilha/nó, presença de texto, necessidade de OCR, riscos, teste e
        saída prevista. Diferencie claramente dado recebido, texto extraído e texto
        reconhecido. **Inventário:** Escreva aqui.

        ## Síntese

        A importação é interpretação técnica. O objetivo não é converter tudo para um
        único formato sem crítica, mas produzir representações adequadas, vinculadas e
        testáveis.
        """),
    ]


def limpeza() -> list[dict]:
    return [
        md("""
        # Estrutura tabular, limpeza e qualidade

        ## 1. Uma variável por coluna, uma observação por linha

        A estrutura tabular depende da unidade de análise. Valores atômicos e nomes de
        campos estáveis facilitam seleção e junção, mas não determinam sozinhos a
        ontologia correta. Tabelas separadas podem representar documentos, pessoas,
        lugares e relações sem repetir tudo em uma única linha.
        """),
        code("""
        import pandas as pd
        bruto = pd.read_csv("dados/brutos/catalogo_messy.csv", sep=";", dtype={"codigo_municipio": "string"})
        bruto.info()
        """),
        md("""
        ## 2. Largo e longo

        No formato largo, período e tema aparecem nos nomes das colunas. No longo,
        essas dimensões viram valores. A transformação altera a unidade da linha: de
        documento para combinação documento–tema–período.

        ![Uma tabela larga com uma linha por documento é reorganizada em tabela longa com uma linha por combinação documento, tema e período, sem resumir os valores.](imagens/02_largo_longo.svg)

        Observe que `melt` não apenas muda a aparência: ele redefine o que cada linha
        representa. Essa unidade precisa constar no dicionário de dados.
        """),
        code("""
        largo = pd.read_csv("dados/brutos/indicadores_largos.csv")
        longo = largo.melt(id_vars="id_documento", var_name="tema_periodo", value_name="ocorrencias")
        partes = longo["tema_periodo"].str.extract(r"(?P<tema>.+)_(?P<periodo>\d{4})")
        longo = pd.concat([longo[["id_documento", "ocorrencias"]], partes], axis=1)
        print("Largo:", largo.shape, "| Longo:", longo.shape)
        longo.head(6)
        """),
        md("""
        ## 3. Preservar original, criar versão normalizada

        Não sobrescreveremos títulos, municípios ou gêneros. A coluna original permite
        auditar o mapa de equivalências e recuperar distinções apagadas por uma regra.
        A remoção de acentos pode ajudar correspondência aproximada, mas não deve
        substituir automaticamente a grafia de apresentação.
        """),
        code("""
        import re
        import unicodedata

        def chave_textual(valor):
            if pd.isna(valor):
                return pd.NA
            texto = " ".join(str(valor).strip().lower().split())
            texto = "".join(c for c in unicodedata.normalize("NFD", texto) if unicodedata.category(c) != "Mn")
            return texto

        trabalho = bruto.copy()
        trabalho["titulo_chave"] = trabalho["titulo"].map(chave_textual)
        trabalho["municipio_chave"] = trabalho["municipio"].map(chave_textual)
        mapa_generos = {"editorial": "editorial", "notícia": "notícia", "noticia": "notícia", "carta": "carta", "manifesto": "manifesto"}
        trabalho["genero_original"] = trabalho["genero"]
        trabalho["genero_padronizado"] = trabalho["genero"].map(chave_textual).map(mapa_generos)
        trabalho[["titulo", "titulo_chave", "genero_original", "genero_padronizado"]]
        """),
        md("""
        ## 4. Datas, códigos e ausências

        Código de município é identificador textual, não quantidade. Datas parciais
        não devem receber dia e mês inventados. Um parser explícito separa datas
        completas, anos isolados e valores desconhecidos; guardar o original, a
        precisão e a razão evita transformar incerteza em falsa exatidão.

        ![O valor de data recebido é preservado, passa por uma regra explícita e produz representação derivada, precisão e razão; log e testes permitem retornar à fonte.](imagens/02_transformacao_rastreavel.svg)

        No exemplo, uma data completa pode ocupar `data_normalizada`; um ano isolado
        ocupa `ano_documento`, mas não recebe dia e mês arbitrários. A coluna
        `precisao_data` distingue `dia`, `ano`, `desconhecida` e, se ocorrer, `inválida`.
        """),
        code("""
        trabalho["data_original"] = trabalho["data_documento"]

        def decompor_data(valor):
            texto = str(valor).strip()
            formatos = [
                (r"\d{4}-\d{2}-\d{2}", "%Y-%m-%d"),
                (r"\d{2}/\d{2}/\d{4}", "%d/%m/%Y"),
            ]
            for padrao, formato in formatos:
                if re.fullmatch(padrao, texto):
                    data = pd.to_datetime(texto, format=formato, errors="coerce")
                    if pd.notna(data):
                        return data, data.year, "dia", pd.NA
                    return pd.NaT, pd.NA, "inválida", "data impossível no calendário"
            if re.fullmatch(r"\d{4}", texto):
                return pd.NaT, int(texto), "ano", "dia e mês não informados"
            if texto.casefold() == "data desconhecida":
                return pd.NaT, pd.NA, "desconhecida", "data não informada"
            return pd.NaT, pd.NA, "inválida", "formato não reconhecido"

        datas = trabalho["data_original"].apply(decompor_data).apply(pd.Series)
        datas.columns = ["data_normalizada", "ano_documento", "precisao_data", "razao_data_ausente"]
        datas["ano_documento"] = datas["ano_documento"].astype("Int64")
        trabalho[datas.columns] = datas
        trabalho["palavras"] = pd.to_numeric(trabalho["palavras"], errors="coerce")
        trabalho["razao_palavras_ausente"] = trabalho["palavras"].isna().map({True: "não contado", False: pd.NA})
        trabalho[["data_original", "data_normalizada", "ano_documento", "precisao_data", "razao_data_ausente", "palavras"]]
        """),
        md("""
        ## 5. Duplicatas são uma hipótese

        IDs repetidos detectam um tipo de duplicata. Registros de um mesmo documento
        com IDs diferentes exigem combinação de campos e revisão. Remover pelo título
        isolado poderia apagar edições legítimas.
        """),
        code("""
        trabalho["possivel_duplicata"] = trabalho.duplicated(
            subset=["titulo_chave", "data_normalizada", "municipio_chave", "palavras"],
            keep=False,
        )
        trabalho.loc[trabalho["possivel_duplicata"], ["id_documento", "titulo", "data_original", "palavras"]]
        """),
        md("""
        ## 6. Relatório e exportação intermediária

        Antes/depois deve quantificar transformações, falhas e casos para revisão. A
        saída intermediária não substitui os dados brutos.
        """),
        code("""
        relatorio = {
            "linhas": len(trabalho),
            "datas_sem_precisao_de_dia": int(trabalho["data_normalizada"].isna().sum()),
            "datas_parciais_ano": int(trabalho["precisao_data"].eq("ano").sum()),
            "datas_desconhecidas": int(trabalho["precisao_data"].eq("desconhecida").sum()),
            "datas_invalidas": int(trabalho["precisao_data"].eq("inválida").sum()),
            "palavras_ausentes": int(trabalho["palavras"].isna().sum()),
            "generos_sem_mapeamento": int(trabalho["genero_padronizado"].isna().sum()),
            "registros_em_grupos_de_possiveis_duplicatas": int(trabalho["possivel_duplicata"].sum()),
        }
        trabalho.to_csv("dados/intermediarios/catalogo_normalizado.csv", index=False)
        pd.Series(relatorio, name="quantidade")
        """),
        md("""
        ## Atividade — log de transformação

        Registre campo, problema, regra, justificativa, valores afetados, teste,
        reversibilidade e responsável. Explique que distinção cada regra pode apagar.
        **Log:** Escreva aqui.

        ## Síntese

        Limpeza responsável acrescenta rastreabilidade. Ela não transforma incerteza
        substantiva em certeza técnica nem autoriza exclusão silenciosa.
        """),
    ]


def integracao() -> list[dict]:
    return [
        md("""
        # Junções, integração e reprodutibilidade

        ## 1. Chaves e cardinalidade

        Antes de juntar, declare a unidade de cada tabela e a cardinalidade esperada:
        1:1, 1:N ou N:N. Uma chave duplicada pode multiplicar linhas e fabricar peso
        analítico. `validate` testa a hipótese de cardinalidade; `indicator` mostra a
        cobertura da correspondência.

        ![Três painéis representam relações um para um, um para muitos e muitos para muitos, mostrando por que a cardinalidade precisa ser declarada e testada antes da junção.](imagens/03_cardinalidades.svg)

        Cardinalidade descreve quantas linhas de um lado podem corresponder a cada
        linha do outro. Ela deve ser formulada, confrontada com os dados e testada no
        código antes da junção.
        """),
        code("""
        import json
        import pandas as pd

        catalogo = pd.read_csv("dados/intermediarios/catalogo_normalizado.csv", dtype={"codigo_municipio": "string"})
        municipios = pd.read_csv("dados/brutos/extrato_codigos_municipios_ibge.csv", dtype={"codigo_municipio": "string"})
        integrada = catalogo.merge(
            municipios, on="codigo_municipio", how="left",
            validate="many_to_one", indicator=True,
        )
        integrada["_merge"].value_counts()
        """),
        md("""
        ### Auditoria da junção

        `left_only` não deve ser descartado automaticamente: pode indicar código
        inválido, cobertura incompleta da tabela de referência ou mudança temporal.
        Compare contagens antes e depois e examine chaves sem correspondência.
        """),
        code("""
        auditoria_juncao = {
            "linhas_antes": len(catalogo),
            "linhas_depois": len(integrada),
            "sem_correspondencia": int(integrada["_merge"].eq("left_only").sum()),
            "ids_unicos_antes": int(catalogo["id_documento"].nunique()),
            "ids_unicos_depois": int(integrada["id_documento"].nunique()),
        }
        pd.Series(auditoria_juncao)
        """),
        md("""
        ## 2. Integrar textos, metadados e indicadores

        Um documento pode possuir zero ou um arquivo textual nesta versão, vários
        temas e vários indicadores. Vamos criar uma tabela textual 1:1 apenas para os
        arquivos disponíveis; temas e indicadores permanecem em tabelas longas para
        evitar colunas multivaloradas.

        ![A tabela de documentos conecta-se por chaves a textos, relações documento-tema, municípios e indicadores, com marcações das cardinalidades esperadas.](imagens/03_modelo_relacional_base.svg)

        O desenho não exige um único arquivo físico: ele explicita entidades e
        relações. Separar tabelas evita repetir textos ou armazenar listas inteiras em
        uma célula, preservando as unidades próprias de documentos, temas e indicadores.
        """),
        code("""
        from pathlib import Path

        metadados = json.loads(Path("dados/brutos/metadados.json").read_text(encoding="utf-8"))
        textos = []
        temas = []
        for item in metadados:
            for tema in item["temas"]:
                temas.append({"id_documento": item["id_documento"], "tema": tema})
            if item["arquivo_texto"]:
                caminho = Path("dados/brutos") / item["arquivo_texto"]
                textos.append({"id_documento": item["id_documento"], "texto": caminho.read_text(encoding="utf-8")})
        tabela_textos = pd.DataFrame(textos)
        tabela_temas = pd.DataFrame(temas)
        base_documentos = integrada.merge(tabela_textos, on="id_documento", how="left", validate="one_to_one")
        print("Documentos:", len(base_documentos), "| relações documento-tema:", len(tabela_temas))
        """),
        code("""
        largo = pd.read_csv("dados/brutos/indicadores_largos.csv")
        indicadores = largo.melt(id_vars="id_documento", var_name="tema_periodo", value_name="ocorrencias")
        partes = indicadores["tema_periodo"].str.extract(r"(?P<tema>.+)_(?P<periodo>\d{4})")
        indicadores = pd.concat([indicadores[["id_documento", "ocorrencias"]], partes], axis=1)

        base_documentos.drop(columns="_merge").to_csv("dados/derivados/documentos_processaveis.csv", index=False)
        tabela_temas.to_csv("dados/derivados/documentos_temas.csv", index=False)
        indicadores.to_csv("dados/derivados/indicadores_longos.csv", index=False)
        """),
        md("""
        ## 3. Organização e execução

        Uma estrutura simples separa entrada, intermediários e derivados. Notebooks
        numerados tornam a ordem visível, mas reprodutibilidade também requer ambiente,
        parâmetros, versões e execução desde o início. Saídas derivadas devem poder ser
        reconstruídas sem editar manualmente células intermediárias.
        """),
        code("""
        from pathlib import Path

        verificacoes = {
            "ids_documentos_unicos": base_documentos["id_documento"].is_unique,
            "nenhuma_linha_criada_na_juncao_municipal": len(base_documentos) == len(catalogo),
            "temas_referenciam_documentos": set(tabela_temas["id_documento"]).issubset(set(base_documentos["id_documento"])),
            "arquivos_derivados": len(list(Path("dados/derivados").glob("*.csv"))),
        }
        verificacoes
        """),
        md("""
        ## Atividade — plano de integração

        Desenhe as tabelas, unidades, chaves, cardinalidades, campos compartilhados,
        validações, tratamento de não correspondências e saídas. Indique como um
        resultado será rastreado até a fonte. **Plano:** Escreva aqui.

        ## Síntese

        Junção é uma afirmação de identidade e relação, não mero encaixe de colunas.
        A base processável pode ser plural: tabela de documentos, tabela de relações,
        textos e indicadores ligados por chaves verificadas.
        """),
    ]


def oficina() -> list[dict]:
    return [
        md("""
        # Oficina — Primeira base processável

        Este notebook é um roteiro de projeto. Execute transformações em uma cópia
        própria ou notebook técnico; registre aqui decisões, evidências e resultados.
        Não altere os arquivos brutos.

        ![Dados brutos, código, dados derivados e documentação formam um pacote submetido a testes e parecer de qualidade, com retorno rastreável para correções.](imagens/04_pacote_processavel.svg)

        A figura funciona também como checklist: um CSV isolado não demonstra como a
        base foi produzida, testada ou delimitada. A entrega precisa combinar os
        componentes e manter vínculos entre eles.
        """),
        md("""
        ## 1. Inventário e estrutura

        **Pergunta e unidade de análise:** Escreva aqui.

        **Arquivos, formatos, versões e proveniência:** Escreva aqui.

        **Estrutura de pastas e política de imutabilidade:** Escreva aqui.

        **Ambiente e dependências:** Escreva aqui.
        """),
        md("""
        ## 2. Importação e extração

        | Fonte | Leitor/parâmetros | Estrutura esperada | Teste | Saída |
        |---|---|---|---|---|
        | Escreva aqui | Escreva aqui | Escreva aqui | Escreva aqui | Escreva aqui |

        **PDFs com texto, PDFs de imagem e TXT:** Escreva aqui.

        **Plano de OCR, amostra de controle e métrica de erro:** Escreva aqui.
        """),
        md("""
        ## 3. Modelo tabular e transformação

        **Tabelas e unidade de cada linha:** Escreva aqui.

        **Decisão largo/longo:** Escreva aqui.

        | Campo | Original preservado | Regra | Justificativa | Teste | Perda possível |
        |---|---|---|---|---|---|
        | Escreva aqui | Escreva aqui | Escreva aqui | Escreva aqui | Escreva aqui | Escreva aqui |
        """),
        md("""
        ## 4. Ausências e duplicatas

        **Representações de ausência e razões:** Escreva aqui.

        **Chave de duplicata exata:** Escreva aqui.

        **Critérios de possível duplicata e revisão humana:** Escreva aqui.

        **Decisão de manter, relacionar, fundir ou excluir:** Escreva aqui.
        """),
        md("""
        ## 5. Junções e integração

        | Tabelas | Chave | Cardinalidade | Validação | Não correspondências |
        |---|---|---|---|---|
        | Escreva aqui | Escreva aqui | Escreva aqui | Escreva aqui | Escreva aqui |

        **Vínculo entre texto, metadado, indicador e fonte:** Escreva aqui.

        **Contagens antes/depois e riscos de multiplicação:** Escreva aqui.
        """),
        md("""
        ## 6. Registro e testes

        **Log de transformações:** Escreva aqui.

        **Testes de esquema, domínios, chaves e arquivos:** Escreva aqui.

        **Como reconstruir a base desde os brutos:** Escreva aqui.

        **Erros conhecidos e casos pendentes:** Escreva aqui.
        """),
        md("""
        ## 7. Rubrica

        | Critério | 0 | 1 | 2 | Minha nota/evidência |
        |---|---|---|---|---|
        | preservação e proveniência | ausente | parcial | auditável | Escreva aqui |
        | importação | implícita | parâmetros parciais | testada | Escreva aqui |
        | limpeza | sobrescreve | regras incompletas | original + regra + teste | Escreva aqui |
        | ausências/duplicatas | descartadas | diagnosticadas | justificadas | Escreva aqui |
        | junções | sem controle | chave declarada | cardinalidade auditada | Escreva aqui |
        | integração | arquivos soltos | vínculos parciais | chaves verificadas | Escreva aqui |
        | reprodutibilidade | manual | ordem parcial | reconstruível | Escreva aqui |
        """),
        md("""
        ## 8. Entrega e revisão por pares

        Entregue inventário, notebooks, base processável, tabelas relacionais, log,
        relatório de qualidade e ficha de proveniência. O colega deve tentar localizar
        uma regra não reversível, uma junção perigosa e um limite não documentado.

        **Parecer recebido e mudanças:** Escreva aqui.

        **O que a Unidade 4 poderá explorar e o que ainda não deve concluir:**
        Escreva aqui.
        """),
    ]


def readme() -> None:
    links = tabela_links_colab(
        UNIDADE.name,
        (
            ("Guia da unidade", "00_guia_da_unidade.ipynb"),
            ("Formatos, importação e extração", "01_formatos_importacao_e_extracao.ipynb"),
            ("Estrutura, limpeza e qualidade", "02_estrutura_limpeza_e_qualidade.ipynb"),
            ("Junções, integração e reprodutibilidade", "03_juncoes_integracao_e_reprodutibilidade.ipynb"),
            ("Oficina da base processável", "04_oficina_base_processavel.ipynb"),
        ),
    )
    conteudo = """
    # Unidade 3 — Transformação de fontes em dados analisáveis

    ## Ordem

    1. `00_guia_da_unidade.ipynb`
    2. `01_formatos_importacao_e_extracao.ipynb`
    3. `02_estrutura_limpeza_e_qualidade.ipynb`
    4. `03_juncoes_integracao_e_reprodutibilidade.ipynb`
    5. `04_oficina_base_processavel.ipynb`
    6. `exercicios_unidade_03.html`

    ## Abrir os notebooks no Google Colab

    __LINKS_COLAB__

    O link carrega o notebook diretamente do GitHub. Nos Notebooks 00 a 03,
    execute primeiro a célula **Preparação do ambiente**. Ela clona o
    repositório, posiciona a execução nesta unidade e instala apenas alguma
    dependência ausente. O Notebook 04 é discursivo e não precisa de clonagem.

    ## Dados e dependências

    Dados fictícios e um extrato didático documentado do IBGE ficam separados em
    `brutos`, `intermediarios` e `derivados`. Requer Python 3, pandas, openpyxl,
    pypdf e Pillow. Tesseract é opcional; há saída pré-computada para execução
    offline sem o programa. `imagens/` reúne a ilustração de abertura e sete
    diagramas SVG acessíveis; as duas imagens sintéticas de OCR ficam em `dados/brutos`
    porque são entradas do experimento, não apenas elementos decorativos.

    Nunca edite os dados brutos. Reconstrua intermediários e derivados executando os
    notebooks em ordem. As análises substantivas começam na Unidade 4.

    `exercicios_unidade_03.html` contém 18 questões com correção offline e versão
    textual. `gabaritos/` reúne respostas-modelo e rubrica; `revisores/` contém
    seis roteiros e seus pareceres executados.
    """
    conteudo = dedent(conteudo).replace("__LINKS_COLAB__", links)
    (UNIDADE / "README.md").write_text(conteudo.strip() + "\n", encoding="utf-8")


def main() -> None:
    UNIDADE.mkdir(exist_ok=True)
    criar_dados()
    construir_imagens()
    salvar_notebook("00_guia_da_unidade.ipynb", guia(), requer_repositorio=True)
    salvar_notebook(
        "01_formatos_importacao_e_extracao.ipynb",
        formatos(),
        requer_repositorio=True,
    )
    salvar_notebook(
        "02_estrutura_limpeza_e_qualidade.ipynb",
        limpeza(),
        requer_repositorio=True,
    )
    salvar_notebook(
        "03_juncoes_integracao_e_reprodutibilidade.ipynb",
        integracao(),
        requer_repositorio=True,
    )
    salvar_notebook("04_oficina_base_processavel.ipynb", oficina())
    readme()
    print(f"Unidade 3 construída em: {UNIDADE}")


if __name__ == "__main__":
    main()
