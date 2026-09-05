"""Constrói os diagramas SVG acessíveis da Unidade 3."""

from __future__ import annotations

from html import escape
from pathlib import Path


RAIZ = Path(__file__).resolve().parents[1]
UNIDADE = RAIZ / "unidade_03"
IMAGENS = UNIDADE / "imagens"


CORES = {
    "fundo": "#fbf4e8",
    "papel": "#fffdf8",
    "azul": "#17324d",
    "azul_claro": "#dbe8ec",
    "verde": "#256b6b",
    "verde_claro": "#d8ebe7",
    "terracota": "#a44f32",
    "terracota_claro": "#f2ddd2",
    "ameixa": "#69445f",
    "ameixa_claro": "#eadde7",
    "areia": "#d8b26e",
    "cinza": "#53606c",
}


def texto(
    x: float,
    y: float,
    linhas: list[str],
    classe: str = "corpo",
    ancora: str = "middle",
    intervalo: int = 22,
) -> str:
    spans = "".join(
        f'<tspan x="{x}" dy="{0 if i == 0 else intervalo}">{escape(linha)}</tspan>'
        for i, linha in enumerate(linhas)
    )
    return f'<text x="{x}" y="{y}" class="{classe}" text-anchor="{ancora}">{spans}</text>'


def caixa(
    x: int,
    y: int,
    largura: int,
    altura: int,
    titulo: str,
    linhas: list[str],
    fundo: str,
    contorno: str,
) -> str:
    return "".join(
        [
            f'<rect x="{x}" y="{y}" width="{largura}" height="{altura}" rx="18" '
            f'fill="{fundo}" stroke="{contorno}" stroke-width="3"/>',
            texto(x + largura / 2, y + 34, [titulo], "subtitulo"),
            texto(x + largura / 2, y + 69, linhas, "corpo"),
        ]
    )


def documento(titulo: str, descricao: str, corpo: str, altura: int = 620) -> str:
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 {altura}"
 role="img" aria-labelledby="titulo descricao">
<title id="titulo">{escape(titulo)}</title>
<desc id="descricao">{escape(descricao)}</desc>
<defs>
  <marker id="seta" markerWidth="10" markerHeight="10" refX="8" refY="3"
   orient="auto" markerUnits="strokeWidth">
    <path d="M0,0 L0,6 L9,3 z" fill="{CORES['azul']}"/>
  </marker>
  <style>
    .titulo {{ font: 700 30px system-ui, sans-serif; fill: {CORES['azul']}; }}
    .subtitulo {{ font: 700 19px system-ui, sans-serif; fill: {CORES['azul']}; }}
    .corpo {{ font: 16px system-ui, sans-serif; fill: {CORES['azul']}; }}
    .pequeno {{ font: 14px system-ui, sans-serif; fill: {CORES['azul']}; }}
    .nota {{ font: italic 15px system-ui, sans-serif; fill: {CORES['cinza']}; }}
    .numero {{ font: 700 24px system-ui, sans-serif; fill: #fff; }}
    .seta {{ stroke: {CORES['azul']}; stroke-width: 3; fill: none; marker-end: url(#seta); }}
    .linha {{ stroke: {CORES['azul']}; stroke-width: 3; fill: none; }}
    .tracejada {{ stroke-dasharray: 9 7; }}
  </style>
</defs>
<rect width="1200" height="{altura}" rx="28" fill="{CORES['fundo']}"/>
{corpo}
</svg>
'''


def percurso() -> str:
    partes = [texto(600, 48, ["Da fonte preservada à base processável"], "titulo")]
    itens = [
        ("1", "Ler", ["formatos", "e extração"], CORES["azul_claro"], CORES["azul"]),
        ("2", "Estruturar", ["unidade da linha", "e tipos"], CORES["verde_claro"], CORES["verde"]),
        ("3", "Integrar", ["chaves", "e cardinalidade"], CORES["terracota_claro"], CORES["terracota"]),
        ("4", "Empacotar", ["dados, código", "e documentação"], CORES["ameixa_claro"], CORES["ameixa"]),
    ]
    for i, (numero, titulo, linhas, fundo, contorno) in enumerate(itens):
        x = 95 + i * 275
        partes.append(caixa(x, 125, 220, 165, titulo, linhas, fundo, contorno))
        partes.append(f'<circle cx="{x + 110}" cy="125" r="23" fill="{contorno}"/>')
        partes.append(texto(x + 110, 133, [numero], "numero"))
        if i < len(itens) - 1:
            partes.append(f'<path class="seta" d="M{x + 223},207 H{x + 265}"/>')
    partes.append(caixa(95, 355, 220, 100, "Brutos preservados", ["ponto de entrada", "não sobrescrito"], CORES["papel"], CORES["areia"]))
    partes.append('<path class="seta tracejada" d="M205,350 V300"/>')
    partes.append('<path class="seta tracejada" d="M1025,315 C1025,510 210,530 210,465"/>')
    partes.append(texto(645, 490, ["Testes e limites podem fazer o fluxo retornar às decisões anteriores"], "nota"))
    return documento(
        "Percurso da Unidade 3",
        "Quatro etapas ligam leitura de formatos, estruturação, integração e empacotamento. Os dados brutos permanecem preservados e uma seta de retorno representa auditoria e revisão.",
        "".join(partes),
        550,
    )


def pdf_texto_imagem_ocr() -> str:
    partes = [texto(600, 46, ["PDF: primeiro diagnosticar, depois escolher a operação"], "titulo")]
    partes.append(caixa(55, 205, 205, 120, "Arquivo PDF", ["contêiner de", "páginas"], CORES["papel"], CORES["areia"]))
    partes.append(caixa(355, 180, 255, 170, "Há texto selecionável?", ["teste de extração", "+ inspeção da página"], CORES["azul_claro"], CORES["azul"]))
    partes.append('<path class="seta" d="M263,265 H345"/>')
    partes.append(caixa(720, 90, 360, 125, "Sim: extrair a camada textual", ["avaliar ordem, hifenização", "e caracteres"], CORES["verde_claro"], CORES["verde"]))
    partes.append(caixa(720, 315, 360, 125, "Não: reconhecer a imagem com OCR", ["registrar imagem, ferramenta", "parâmetros e idioma"], CORES["terracota_claro"], CORES["terracota"]))
    partes.append('<path class="seta" d="M612,220 C660,220 670,155 710,155"/>')
    partes.append('<path class="seta" d="M612,310 C660,310 670,377 710,377"/>')
    partes.append(texto(655, 180, ["SIM"], "pequeno"))
    partes.append(texto(655, 356, ["NÃO"], "pequeno"))
    partes.append(caixa(420, 490, 360, 90, "Avaliar contra a página", ["amostra de referência + métrica", "+ leitura humana situada"], CORES["ameixa_claro"], CORES["ameixa"]))
    partes.append('<path class="seta" d="M900,220 C900,475 790,525 790,525"/>')
    partes.append('<path class="seta" d="M900,445 C900,500 830,525 790,525"/>')
    return documento(
        "Decisão entre extração textual e OCR",
        "Um PDF passa por diagnóstico de texto selecionável. A presença de texto leva à extração da camada; a ausência leva ao OCR. Ambas as rotas terminam em avaliação contra a página.",
        "".join(partes),
        630,
    )


def largo_longo() -> str:
    partes = [texto(600, 45, ["Largo e longo mudam a unidade da linha"], "titulo")]
    partes.append(caixa(45, 105, 430, 285, "Tabela larga", ["uma linha = um documento", "tema e período nas colunas"], CORES["azul_claro"], CORES["azul"]))
    colunas = ["ID", "educação 1890", "trabalho 1890", "educação 1900"]
    for i, rotulo in enumerate(colunas):
        x = 70 + i * 95
        partes.append(f'<rect x="{x}" y="230" width="95" height="42" fill="{CORES["papel"]}" stroke="{CORES["azul"]}"/>')
        partes.append(texto(x + 47, 255, [rotulo], "pequeno"))
    for linha, valores in enumerate((["D001", "3", "1", "2"], ["D002", "0", "4", "1"])):
        for i, valor in enumerate(valores):
            x, y = 70 + i * 95, 272 + linha * 42
            partes.append(f'<rect x="{x}" y="{y}" width="95" height="42" fill="{CORES["papel"]}" stroke="{CORES["azul"]}"/>')
            partes.append(texto(x + 47, y + 26, [valor], "pequeno"))
    partes.append('<path class="seta" d="M485,250 H705"/>')
    partes.append(texto(595, 220, ["reorganizar"], "subtitulo"))
    partes.append(texto(595, 285, ["não é resumir"], "nota"))
    partes.append(caixa(725, 105, 430, 350, "Tabela longa", ["uma linha = documento–tema–período", "dimensões passam a valores"], CORES["verde_claro"], CORES["verde"]))
    colunas_longas = ["ID", "tema", "período", "ocorrências"]
    for i, rotulo in enumerate(colunas_longas):
        x = 750 + i * 95
        partes.append(f'<rect x="{x}" y="230" width="95" height="42" fill="{CORES["papel"]}" stroke="{CORES["verde"]}"/>')
        partes.append(texto(x + 47, 255, [rotulo], "pequeno"))
    linhas = [["D001", "educação", "1890", "3"], ["D001", "trabalho", "1890", "1"], ["D001", "educação", "1900", "2"]]
    for linha, valores in enumerate(linhas):
        for i, valor in enumerate(valores):
            x, y = 750 + i * 95, 272 + linha * 42
            partes.append(f'<rect x="{x}" y="{y}" width="95" height="42" fill="{CORES["papel"]}" stroke="{CORES["verde"]}"/>')
            partes.append(texto(x + 47, y + 26, [valor], "pequeno"))
    partes.append(texto(600, 520, ["A forma correta depende da pergunta e da unidade de análise declarada"], "nota"))
    return documento(
        "Transformação de tabela larga em longa",
        "À esquerda, cada linha representa um documento e tema e período aparecem nas colunas. À direita, cada linha representa uma combinação entre documento, tema e período.",
        "".join(partes),
        570,
    )


def transformacao_rastreavel() -> str:
    partes = [texto(600, 46, ["Normalizar sem apagar a evidência"], "titulo")]
    partes.append(caixa(45, 140, 255, 200, "Valor recebido", ["data_documento", "06/02/1891", "ou apenas 1892"], CORES["papel"], CORES["areia"]))
    partes.append(caixa(380, 140, 360, 200, "Regra explícita", ["identificar o padrão", "aplicar parser compatível", "não completar partes ausentes"], CORES["azul_claro"], CORES["azul"]))
    partes.append(caixa(820, 105, 330, 130, "Representação derivada", ["data normalizada", "ou ano conhecido"], CORES["verde_claro"], CORES["verde"]))
    partes.append(caixa(820, 285, 330, 130, "Estado da informação", ["precisão: dia, ano", "ou desconhecida"], CORES["terracota_claro"], CORES["terracota"]))
    partes.append('<path class="seta" d="M303,240 H370"/>')
    partes.append('<path class="seta" d="M743,210 C780,210 785,170 810,170"/>')
    partes.append('<path class="seta" d="M743,270 C780,270 785,350 810,350"/>')
    partes.append(caixa(385, 440, 430, 95, "Log + teste", ["regra, casos afetados, falhas", "reversibilidade e responsável"], CORES["ameixa_claro"], CORES["ameixa"]))
    partes.append('<path class="seta tracejada" d="M985,420 C985,505 830,490 825,490"/>')
    partes.append('<path class="seta tracejada" d="M375,490 C225,490 175,425 175,350"/>')
    return documento(
        "Transformação rastreável de datas",
        "O valor recebido é preservado, uma regra explícita produz representação derivada e registra a precisão da informação. Um log e testes permitem retornar à fonte e revisar a decisão.",
        "".join(partes),
        590,
    )


def cardinalidades() -> str:
    partes = [texto(600, 45, ["Cardinalidade é uma hipótese sobre as relações"], "titulo")]
    paineis = [
        (40, "1 : 1", "documento ↔ texto", 1, 1, CORES["azul_claro"], CORES["azul"]),
        (420, "1 : N", "documento ↔ temas", 1, 3, CORES["verde_claro"], CORES["verde"]),
        (800, "N : N", "documentos ↔ pessoas", 3, 3, CORES["terracota_claro"], CORES["terracota"]),
    ]
    for x, titulo, exemplo, esquerda, direita, fundo, contorno in paineis:
        partes.append(f'<rect x="{x}" y="90" width="360" height="405" rx="22" fill="{fundo}" stroke="{contorno}" stroke-width="3"/>')
        partes.append(texto(x + 180, 132, [titulo], "titulo"))
        partes.append(texto(x + 180, 168, [exemplo], "corpo"))
        esquerda_y = [290] if esquerda == 1 else [235, 290, 345]
        direita_y = [290] if direita == 1 else [235, 290, 345]
        for y in esquerda_y:
            partes.append(f'<circle cx="{x + 85}" cy="{y}" r="20" fill="{CORES["papel"]}" stroke="{contorno}" stroke-width="3"/>')
        for y in direita_y:
            partes.append(f'<circle cx="{x + 275}" cy="{y}" r="20" fill="{CORES["papel"]}" stroke="{contorno}" stroke-width="3"/>')
        for y1 in esquerda_y:
            for y2 in direita_y:
                partes.append(f'<path d="M{x + 106},{y1} L{x + 254},{y2}" stroke="{contorno}" stroke-width="2"/>')
    partes.append(texto(600, 555, ["Declarar e testar a cardinalidade evita multiplicar linhas silenciosamente"], "nota"))
    return documento(
        "Cardinalidades um para um, um para muitos e muitos para muitos",
        "Três painéis representam relações um para um, um para muitos e muitos para muitos. A legenda ressalta que a cardinalidade deve ser declarada e testada antes da junção.",
        "".join(partes),
        600,
    )


def modelo_relacional() -> str:
    partes = [texto(600, 46, ["Uma base processável pode reunir várias tabelas"], "titulo")]
    partes.append(caixa(415, 185, 370, 210, "DOCUMENTOS", ["PK id_documento", "título • data • município", "gênero • palavras"], CORES["azul_claro"], CORES["azul"]))
    partes.append(caixa(45, 105, 265, 130, "TEXTOS", ["PK/FK id_documento", "texto extraído"], CORES["verde_claro"], CORES["verde"]))
    partes.append(caixa(45, 365, 265, 130, "DOCUMENTOS_TEMAS", ["FK id_documento", "tema"], CORES["terracota_claro"], CORES["terracota"]))
    partes.append(caixa(890, 105, 265, 130, "MUNICÍPIOS", ["PK código", "nome • UF"], CORES["ameixa_claro"], CORES["ameixa"]))
    partes.append(caixa(890, 365, 265, 130, "INDICADORES", ["FK id_documento", "tema • período • valor"], "#f1e2bd", "#8a6528"))
    partes.append('<path class="linha" d="M310,170 H405"/>')
    partes.append('<path class="linha" d="M310,430 C360,430 370,340 405,340"/>')
    partes.append('<path class="linha" d="M795,240 C835,240 845,170 880,170"/>')
    partes.append('<path class="linha" d="M795,340 C835,340 845,430 880,430"/>')
    partes.append(texto(350, 156, ["0..1"], "pequeno"))
    partes.append(texto(350, 410, ["0..N"], "pequeno"))
    partes.append(texto(845, 156, ["N..1"], "pequeno"))
    partes.append(texto(845, 410, ["0..N"], "pequeno"))
    partes.append(texto(600, 550, ["Chaves mantêm vínculos sem repetir listas inteiras em uma célula"], "nota"))
    return documento(
        "Modelo relacional didático da Unidade 3",
        "A tabela de documentos conecta-se por chaves a textos, relações documento-tema, municípios e indicadores. As marcações indicam as cardinalidades esperadas.",
        "".join(partes),
        600,
    )


def pacote_processavel() -> str:
    partes = [texto(600, 45, ["A entrega é um pacote auditável, não apenas um CSV"], "titulo")]
    itens = [
        (55, 110, "Dados brutos", ["preservados", "e identificados"], CORES["azul_claro"], CORES["azul"]),
        (335, 110, "Código", ["ordem executável", "e parâmetros"], CORES["verde_claro"], CORES["verde"]),
        (615, 110, "Dados derivados", ["tabelas ligadas", "por chaves"], CORES["terracota_claro"], CORES["terracota"]),
        (895, 110, "Documentação", ["proveniência, log", "e limites"], CORES["ameixa_claro"], CORES["ameixa"]),
    ]
    for x, y, titulo, linhas, fundo, contorno in itens:
        partes.append(caixa(x, y, 250, 155, titulo, linhas, fundo, contorno))
    for x in (305, 585, 865):
        partes.append(f'<path class="seta" d="M{x},188 H{x + 20}"/>')
    partes.append(caixa(260, 355, 300, 115, "Testes", ["esquema • chaves • contagens", "cobertura • reconstrução"], CORES["papel"], CORES["areia"]))
    partes.append(caixa(640, 355, 300, 115, "Parecer de qualidade", ["erros conhecidos", "casos pendentes • usos possíveis"], CORES["papel"], CORES["terracota"]))
    partes.append('<path class="seta" d="M460,350 C460,305 535,295 560,275"/>')
    partes.append('<path class="seta" d="M790,350 C790,305 730,295 700,275"/>')
    partes.append('<path class="seta tracejada" d="M950,480 C950,560 190,560 190,280"/>')
    partes.append(texto(600, 530, ["Se o pacote não permite reconstruir e explicar a base, a transformação permanece incompleta"], "nota"))
    return documento(
        "Componentes de uma base processável",
        "Dados brutos, código, dados derivados e documentação formam um pacote avaliado por testes e parecer de qualidade. Uma seta de retorno representa correções rastreáveis.",
        "".join(partes),
        585,
    )


def main() -> None:
    IMAGENS.mkdir(parents=True, exist_ok=True)
    imagens = {
        "00_percurso_unidade.svg": percurso(),
        "01_pdf_texto_imagem_ocr.svg": pdf_texto_imagem_ocr(),
        "02_largo_longo.svg": largo_longo(),
        "02_transformacao_rastreavel.svg": transformacao_rastreavel(),
        "03_cardinalidades.svg": cardinalidades(),
        "03_modelo_relacional_base.svg": modelo_relacional(),
        "04_pacote_processavel.svg": pacote_processavel(),
    }
    for nome, conteudo in imagens.items():
        (IMAGENS / nome).write_text(conteudo, encoding="utf-8")
    print(f"{len(imagens)} SVGs construídos em {IMAGENS}")


if __name__ == "__main__":
    main()
