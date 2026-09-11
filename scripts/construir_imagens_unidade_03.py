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


def formatos_estruturas() -> str:
    partes = [texto(600, 46, ["Quatro formatos, quatro maneiras de organizar informação"], "titulo")]
    paineis = [
        (35, "CSV", "tabela plana", CORES["azul_claro"], CORES["azul"]),
        (325, "XLSX", "pasta de planilhas", CORES["verde_claro"], CORES["verde"]),
        (615, "JSON", "objetos e listas", CORES["terracota_claro"], CORES["terracota"]),
        (905, "XML", "elementos aninhados", CORES["ameixa_claro"], CORES["ameixa"]),
    ]
    for x, titulo, subtitulo, fundo, contorno in paineis:
        partes.append(f'<rect x="{x}" y="85" width="260" height="440" rx="20" fill="{fundo}" stroke="{contorno}" stroke-width="3"/>')
        partes.append(texto(x + 130, 125, [titulo], "titulo"))
        partes.append(texto(x + 130, 155, [subtitulo], "nota"))

    # CSV: uma grade sem camadas adicionais.
    for linha in range(4):
        for coluna in range(3):
            x, y = 72 + coluna * 62, 195 + linha * 38
            fill = CORES["papel"] if linha else "#c8dce4"
            partes.append(f'<rect x="{x}" y="{y}" width="62" height="38" fill="{fill}" stroke="{CORES["azul"]}"/>')
    partes.append(texto(165, 385, ["linhas + colunas", "separador e encoding", "tipos precisam ser inferidos"], "corpo", intervalo=25))

    # XLSX: abas e grade representam a pasta que pode conter várias planilhas.
    partes.append(f'<rect x="360" y="195" width="190" height="145" rx="6" fill="{CORES["papel"]}" stroke="{CORES["verde"]}" stroke-width="3"/>')
    for linha in range(1, 4):
        partes.append(f'<path d="M360,{195 + linha * 32} H550" stroke="{CORES["verde"]}"/>')
    for coluna in range(1, 4):
        partes.append(f'<path d="M{360 + coluna * 47},195 V340" stroke="{CORES["verde"]}"/>')
    partes.append(f'<rect x="370" y="340" width="65" height="22" rx="5" fill="{CORES["verde"]}"/>')
    partes.append(f'<rect x="442" y="340" width="65" height="22" rx="5" fill="#94c8bd"/>')
    partes.append(texto(455, 402, ["várias planilhas", "fórmulas e formatação", "selecionar a aba correta"], "corpo", intervalo=25))

    # JSON: árvore com objeto, lista e valores.
    partes.append(texto(745, 205, ["{ documento }"], "subtitulo"))
    partes.append(f'<path class="linha" d="M745,220 V250 M675,250 H815 M675,250 V275 M815,250 V275"/>')
    partes.append(f'<rect x="642" y="275" width="95" height="68" rx="10" fill="{CORES["papel"]}" stroke="{CORES["terracota"]}" stroke-width="3"/>')
    partes.append(texto(689, 302, ["id"], "subtitulo"))
    partes.append(texto(689, 327, ["D001"], "pequeno"))
    partes.append(f'<rect x="753" y="275" width="125" height="68" rx="10" fill="{CORES["papel"]}" stroke="{CORES["terracota"]}" stroke-width="3"/>')
    partes.append(texto(815, 302, ["temas"], "subtitulo"))
    partes.append(texto(815, 327, ["[ ... ]"], "pequeno"))
    partes.append(texto(745, 390, ["chaves + valores", "listas e objetos aninhados", "percorrer a hierarquia"], "corpo", intervalo=25))

    # XML: árvore de elementos explicitada por marcas de abertura e fechamento.
    partes.append(texto(1035, 205, ["<documento>"], "subtitulo"))
    partes.append(f'<path class="linha" d="M1035,220 V250 M965,250 H1105 M965,250 V275 M1105,250 V275"/>')
    partes.append(f'<rect x="925" y="275" width="90" height="68" rx="10" fill="{CORES["papel"]}" stroke="{CORES["ameixa"]}" stroke-width="3"/>')
    partes.append(texto(970, 302, ["<id>"], "subtitulo"))
    partes.append(texto(970, 327, ["D001"], "pequeno"))
    partes.append(f'<rect x="1030" y="275" width="140" height="68" rx="10" fill="{CORES["papel"]}" stroke="{CORES["ameixa"]}" stroke-width="3"/>')
    partes.append(texto(1100, 302, ["<tema>"], "subtitulo"))
    partes.append(texto(1100, 327, ["educação"], "pequeno"))
    partes.append(texto(1035, 390, ["elementos + atributos", "ordem e aninhamento", "navegar pelas marcas"], "corpo", intervalo=25))

    partes.append(texto(600, 580, ["A extensão sugere um leitor; parâmetros, estrutura esperada e testes confirmam a interpretação"], "nota"))
    return documento(
        "Estruturas e possibilidades de ação em CSV, XLSX, JSON e XML",
        "Quatro painéis comparam uma grade tabular CSV, uma pasta XLSX com abas, uma árvore JSON de objetos e listas e uma árvore XML de elementos aninhados. Cada formato exige operações de leitura próprias.",
        "".join(partes),
        620,
    )


def linha_tempo_formatos() -> str:
    partes = [texto(600, 43, ["Marcos históricos dos formatos de dados"], "titulo")]
    partes.append(texto(600, 75, ["As datas representam tipos diferentes de marco: criação, rascunho, apresentação ou padrão"], "nota"))
    partes.append('<path class="linha" d="M80,310 H1120"/>')

    itens = [
        (105, 115, "1990", "HTML", ["publicar documentos", "ligados na Web"], CORES["azul_claro"], CORES["azul"]),
        (300, 355, "1996 → 1998", "XML", ["estruturar e trocar", "informação na Web"], CORES["verde_claro"], CORES["verde"]),
        (495, 115, "2001", "JSON", ["intercâmbio textual", "leve e portável"], CORES["terracota_claro"], CORES["terracota"]),
        (690, 355, "2001", "YAML", ["serialização legível", "por pessoas"], CORES["ameixa_claro"], CORES["ameixa"]),
        (885, 115, "2005*", "CSV", ["documentar a troca", "de tabelas planas"], "#f1e2bd", "#8a6528"),
        (1080, 355, "2006", "XLSX", ["representar e empacotar", "planilhas Office"], CORES["azul_claro"], CORES["azul"]),
    ]
    for x, y, data, formato, objetivo, fundo, contorno in itens:
        partes.append(f'<circle cx="{x}" cy="310" r="11" fill="{contorno}"/>')
        if y < 310:
            partes.append(f'<path class="linha" d="M{x},299 V280"/>')
        else:
            partes.append(f'<path class="linha" d="M{x},321 V345"/>')
        partes.append(caixa(x - 82, y, 164, 165, formato, [data, *objetivo], fundo, contorno))

    partes.append(texto(600, 565, ["* A RFC 4180 registrou uma prática CSV anterior; não corresponde à criação do formato"], "nota"))
    partes.append(texto(600, 598, ["Uma história de formatos é uma história de problemas, usos e processos de padronização"], "nota"))
    return documento(
        "Linha do tempo de formatos de dados",
        "Linha do tempo com HTML em 1990, XML entre 1996 e 1998, JSON e YAML em 2001, documentação do CSV pela RFC 4180 em 2005 e padronização do XLSX em 2006. Uma nota informa que o CSV já era usado antes da RFC.",
        "".join(partes),
        635,
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
        "01_linha_tempo_formatos.svg": linha_tempo_formatos(),
        "01_formatos_estruturas.svg": formatos_estruturas(),
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
