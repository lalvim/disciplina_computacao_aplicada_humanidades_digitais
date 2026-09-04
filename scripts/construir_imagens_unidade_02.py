"""Constrói os diagramas SVG acessíveis da Unidade 2."""

from __future__ import annotations

import csv
from collections import Counter
from html import escape
from pathlib import Path


RAIZ = Path(__file__).resolve().parents[1]
UNIDADE = RAIZ / "unidade_02"
IMAGENS = UNIDADE / "imagens"
DADOS = UNIDADE / "dados" / "catalogo_fontes.csv"


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


def bloco_texto(
    x: float,
    y: float,
    linhas: list[str],
    classe: str = "corpo",
    ancora: str = "middle",
    intervalo: int = 22,
) -> str:
    spans = "".join(
        f'<tspan x="{x}" dy="{0 if indice == 0 else intervalo}">{escape(linha)}</tspan>'
        for indice, linha in enumerate(linhas)
    )
    return f'<text x="{x}" y="{y}" class="{classe}" text-anchor="{ancora}">{spans}</text>'


def caixa(
    x: int,
    y: int,
    largura: int,
    altura: int,
    titulo: str,
    linhas: list[str],
    preenchimento: str,
    contorno: str,
) -> str:
    return "".join(
        [
            f'<rect x="{x}" y="{y}" width="{largura}" height="{altura}" rx="18" '
            f'fill="{preenchimento}" stroke="{contorno}" stroke-width="3"/>',
            bloco_texto(x + largura / 2, y + 32, [titulo], "subtitulo"),
            bloco_texto(x + largura / 2, y + 65, linhas, "corpo"),
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
    .nota {{ font: italic 15px system-ui, sans-serif; fill: {CORES['cinza']}; }}
    .numero {{ font: 700 25px system-ui, sans-serif; fill: #fff; }}
    .seta {{ stroke: {CORES['azul']}; stroke-width: 3; fill: none; marker-end: url(#seta); }}
    .tracejada {{ stroke-dasharray: 9 7; }}
  </style>
</defs>
<rect width="1200" height="{altura}" rx="28" fill="{CORES['fundo']}"/>
{corpo}
</svg>
'''


def percurso() -> str:
    partes = [bloco_texto(600, 48, ["Da pergunta ao protocolo da base"], "titulo")]
    itens = [
        ("00", "Diagnóstico", ["adequação", "e limites"], CORES["azul_claro"], CORES["azul"]),
        ("01", "Seleção", ["população", "e corpus"], CORES["verde_claro"], CORES["verde"]),
        ("02", "Cobertura", ["vieses", "e silêncios"], CORES["terracota_claro"], CORES["terracota"]),
        ("03", "Documentação", ["metadados", "e proveniência"], CORES["ameixa_claro"], CORES["ameixa"]),
        ("04", "Oficina", ["protocolo", "defensável"], "#f1e2bd", "#8a6528"),
    ]
    for indice, (numero, titulo, linhas, fundo, contorno) in enumerate(itens):
        x = 38 + indice * 233
        partes.append(f'<rect x="{x}" y="105" width="195" height="175" rx="18" fill="{fundo}" stroke="{contorno}" stroke-width="3"/>')
        partes.append(f'<circle cx="{x + 97.5}" cy="{130}" r="22" fill="{contorno}"/>')
        partes.append(bloco_texto(x + 97.5, 138, [numero], "numero"))
        partes.append(bloco_texto(x + 97.5, 175, [titulo], "subtitulo"))
        partes.append(bloco_texto(x + 97.5, 210, linhas, "corpo"))
        if indice < len(itens) - 1:
            partes.append(f'<path class="seta" d="M{x + 198},192 H{x + 225}"/>')
    produtos = [
        "pergunta situada",
        "protocolo de seleção",
        "matriz de cobertura",
        "dicionário + cadeia",
        "desenho revisado",
    ]
    for indice, produto in enumerate(produtos):
        x = 38 + indice * 233
        partes.append(f'<rect x="{x}" y="318" width="195" height="54" rx="12" fill="{CORES["papel"]}" stroke="{CORES["areia"]}" stroke-width="2"/>')
        partes.append(bloco_texto(x + 97.5, 350, [produto], "corpo"))
    partes.append('<path class="seta tracejada" d="M1085,410 C1085,530 115,530 115,410"/>')
    partes.append(bloco_texto(600, 474, ["Resultados e limites fazem o projeto retornar às decisões anteriores"], "nota"))
    return documento(
        "Percurso da Unidade 2",
        "Cinco etapas conectam diagnóstico, seleção, cobertura, documentação e oficina; uma seta de retorno indica revisão das decisões.",
        "".join(partes),
        540,
    )


def populacao_corpus() -> str:
    partes = [bloco_texto(600, 47, ["Três conjuntos relacionados, mas não equivalentes"], "titulo")]
    partes.extend(
        [
            f'<rect x="70" y="90" width="760" height="440" rx="35" fill="{CORES["azul_claro"]}" stroke="{CORES["azul"]}" stroke-width="3"/>',
            bloco_texto(105, 130, ["População de interesse"], "subtitulo", "start"),
            bloco_texto(105, 160, ["casos sobre os quais se deseja argumentar"], "corpo", "start"),
            f'<rect x="165" y="195" width="575" height="285" rx="30" fill="{CORES["verde_claro"]}" stroke="{CORES["verde"]}" stroke-width="3"/>',
            bloco_texto(200, 235, ["População acessível"], "subtitulo", "start"),
            bloco_texto(200, 265, ["casos localizáveis e consultáveis", "nas condições do projeto"], "corpo", "start"),
            f'<rect x="295" y="315" width="315" height="115" rx="26" fill="{CORES["terracota_claro"]}" stroke="{CORES["terracota"]}" stroke-width="3"/>',
            bloco_texto(452, 355, ["Corpus"], "subtitulo"),
            bloco_texto(452, 385, ["casos delimitados por", "critérios explícitos"], "corpo"),
            caixa(885, 115, 245, 310, "Mediações", ["produção", "preservação", "catalogação", "localização", "digitalização", "acesso", "seleção"], CORES["papel"], CORES["ameixa"]),
            '<path class="seta" d="M875,270 H760"/>',
            bloco_texto(1005, 470, ["Disponível não significa", "representativo"], "nota"),
        ]
    )
    return documento(
        "População de interesse, população acessível e corpus",
        "Conjuntos aninhados mostram que o corpus é delimitado dentro da população acessível, mediada por produção, preservação, acesso e critérios de seleção.",
        "".join(partes),
        580,
    )


def papeis_fontes() -> str:
    partes = [bloco_texto(600, 48, ["O papel da fonte depende da pergunta"], "titulo")]
    partes.append(caixa(430, 210, 340, 165, "Mesmo catálogo institucional", ["descrições", "categorias", "decisões de acesso"], CORES["papel"], CORES["areia"]))
    partes.append(caixa(55, 95, 310, 165, "Pergunta A", ["O que dizem", "as cartas descritas?"], CORES["azul_claro"], CORES["azul"]))
    partes.append(caixa(835, 95, 310, 165, "Pergunta B", ["Como a instituição", "classificou o acervo?"], CORES["verde_claro"], CORES["verde"]))
    partes.append(caixa(55, 380, 310, 125, "Papel", ["instrumento de localização", "ou dado derivado"], CORES["terracota_claro"], CORES["terracota"]))
    partes.append(caixa(835, 380, 310, 125, "Papel", ["fonte primária sobre", "a prática institucional"], CORES["ameixa_claro"], CORES["ameixa"]))
    partes.extend(
        [
            '<path class="seta" d="M430,265 C350,245 340,205 365,175"/>',
            '<path class="seta" d="M770,265 C850,245 860,205 835,175"/>',
            '<path class="seta" d="M210,265 V375"/>',
            '<path class="seta" d="M990,265 V375"/>',
            bloco_texto(600, 548, ["Um artigo historiográfico pode ser secundário para estudar o passado", "e primário para estudar a historiografia"], "nota"),
        ]
    )
    return documento(
        "Papéis de uma fonte",
        "O mesmo catálogo funciona como dado derivado para uma pergunta sobre cartas e como fonte primária para uma pergunta sobre práticas de catalogação.",
        "".join(partes),
        610,
    )


def cadeia_ausencias() -> str:
    partes = [bloco_texto(600, 46, ["Ausências surgem em momentos diferentes"], "titulo")]
    etapas = [
        ("Experiência", ["pessoas, práticas", "e acontecimentos"]),
        ("Registro", ["algo é", "documentado"]),
        ("Preservação", ["algo sobrevive", "e é localizado"]),
        ("Base", ["algo é", "selecionado"]),
        ("Campo", ["um valor é", "preenchido"]),
    ]
    cores = ["azul", "verde", "terracota", "ameixa", "areia"]
    for i, ((titulo, linhas), cor) in enumerate(zip(etapas, cores)):
        x = 30 + i * 238
        contorno = CORES[cor]
        fundo = CORES.get(f"{cor}_claro", "#f1e2bd")
        partes.append(caixa(x, 100, 190, 125, titulo, linhas, fundo, contorno))
        if i < 4:
            partes.append(f'<path class="seta" d="M{x + 193},162 H{x + 225}"/>')
    perdas = [
        (250, "não registrado", ["ausência no", "registro histórico"]),
        (488, "não preservado", ["silêncio de preservação", "ou localização"]),
        (726, "não incluído", ["ausência", "na base"]),
        (964, "não informado", ["valor ausente", "no registro"]),
    ]
    for x, titulo, linhas in perdas:
        partes.append(f'<path d="M{x},230 V285" stroke="{CORES["terracota"]}" stroke-width="3" stroke-dasharray="6 5"/>')
        partes.append(f'<circle cx="{x}" cy="305" r="18" fill="{CORES["terracota"]}"/>')
        partes.append(bloco_texto(x, 350, [titulo], "subtitulo"))
        partes.append(bloco_texto(x, 382, linhas, "corpo"))
    partes.append(bloco_texto(600, 490, ["Aumentar a coleta pode reduzir lacunas da base, mas não recria experiências nunca registradas"], "nota"))
    return documento(
        "Cadeia de produção das ausências",
        "Da experiência ao campo preenchido, quatro pontos mostram ausência no registro histórico, perda de preservação, ausência na base e valor ausente.",
        "".join(partes),
        550,
    )


def cobertura_catalogo_corpus() -> str:
    with DADOS.open(encoding="utf-8", newline="") as arquivo:
        registros = list(csv.DictReader(arquivo))
    corpus = [
        registro
        for registro in registros
        if 1890 <= int(registro["ano"]) <= 1900
        and registro["localizado"] == "sim"
        and registro["digitalizado"] == "sim"
        and registro["condicao_acesso"] in {"público", "mediante autorização"}
    ]
    total = Counter(r["grupo_representado"] for r in registros)
    selecionado = Counter(r["grupo_representado"] for r in corpus)
    grupos = list(total)
    partes = [bloco_texto(600, 44, ["Cobertura antes e depois dos critérios"], "titulo")]
    partes.extend(
        [
            f'<rect x="760" y="70" width="18" height="18" fill="{CORES["azul"]}"/><text x="788" y="85" class="corpo">catálogo</text>',
            f'<rect x="900" y="70" width="18" height="18" fill="{CORES["terracota"]}"/><text x="928" y="85" class="corpo">corpus</text>',
        ]
    )
    maximo = max(total.values())
    for i, grupo in enumerate(grupos):
        y = 125 + i * 66
        largura_total = 500 * total[grupo] / maximo
        largura_corpus = 500 * selecionado[grupo] / maximo
        partes.append(bloco_texto(275, y + 20, [grupo], "corpo", "end"))
        partes.append(f'<rect x="300" y="{y}" width="{largura_total}" height="20" rx="5" fill="{CORES["azul"]}"/>')
        partes.append(f'<text x="{310 + largura_total}" y="{y + 16}" class="corpo">{total[grupo]}</text>')
        partes.append(f'<rect x="300" y="{y + 26}" width="{largura_corpus}" height="20" rx="5" fill="{CORES["terracota"]}"/>')
        partes.append(f'<text x="{310 + largura_corpus}" y="{y + 42}" class="corpo">{selecionado[grupo]}</text>')
    partes.append(bloco_texto(600, 545, ["As barras descrevem este catálogo fictício; não medem importância ou presença histórica"], "nota"))
    return documento(
        "Cobertura do catálogo e do corpus",
        "Barras comparam seis grupos no catálogo e no corpus. Família proprietária cai de dois para zero; trabalhadores de dois para um; público leitor de cinco para quatro.",
        "".join(partes),
        590,
    )


def documentacao_proveniencia() -> str:
    partes = [bloco_texto(600, 45, ["Documentar significado e trajetória"], "titulo")]
    partes.append(caixa(40, 185, 220, 145, "Fonte", ["documento", "ou conjunto"], CORES["azul_claro"], CORES["azul"]))
    partes.append(caixa(345, 185, 220, 145, "Registro + ID", ["identifica", "sem confundir"], CORES["verde_claro"], CORES["verde"]))
    partes.append(caixa(650, 185, 220, 145, "Transformação", ["seleciona, transcreve", "ou normaliza"], CORES["terracota_claro"], CORES["terracota"]))
    partes.append(caixa(955, 185, 205, 145, "Dado derivado", ["mantém vínculo", "com a fonte"], CORES["ameixa_claro"], CORES["ameixa"]))
    for x in (260, 565, 870):
        partes.append(f'<path class="seta" d="M{x},257 H{x + 78}"/>')
    partes.append(caixa(345, 65, 525, 82, "Dicionário de dados", ["define campo • tipo • domínio • origem • limitação"], CORES["papel"], CORES["areia"]))
    partes.append('<path class="seta tracejada" d="M607,148 V180"/>')
    partes.append(caixa(420, 395, 360, 100, "Proveniência", ["entidades • atividades • agentes", "versões • datas • responsabilidades"], CORES["papel"], CORES["ameixa"]))
    partes.append('<path class="seta tracejada" d="M760,335 C760,375 725,385 700,395"/>')
    partes.append(caixa(55, 410, 245, 75, "Agente", ["quem realizou a atividade"], CORES["papel"], CORES["verde"]))
    partes.append('<path class="seta tracejada" d="M305,448 H412"/>')
    partes.append(bloco_texto(600, 550, ["Auditoria técnica verifica regras; documentação explica o que elas significam e não alcançam"], "nota"))
    return documento(
        "Documentação e proveniência",
        "Uma cadeia liga fonte, registro e identificador, transformação e dado derivado; dicionário define campos e proveniência registra entidades, atividades e agentes.",
        "".join(partes),
        600,
    )


def protocolo_integrado() -> str:
    partes = [bloco_texto(600, 45, ["As partes do protocolo precisam concordar"], "titulo")]
    itens = [
        (80, 105, "1. Pergunta", ["alcance e", "unidade"]),
        (355, 105, "2. Fontes", ["produção e", "custódia"]),
        (630, 105, "3. Seleção", ["regras e", "exclusões"]),
        (905, 105, "4. Cobertura", ["lacunas e", "vieses"]),
        (220, 330, "5. Documentação", ["metadados e", "proveniência"]),
        (500, 330, "6. Ética", ["responsabilidade", "e legalidade"]),
        (780, 330, "7. Viabilidade", ["piloto e", "contingência"]),
    ]
    fundos = [CORES["azul_claro"], CORES["verde_claro"], CORES["terracota_claro"], CORES["ameixa_claro"], CORES["azul_claro"], CORES["terracota_claro"], "#f1e2bd"]
    contornos = [CORES["azul"], CORES["verde"], CORES["terracota"], CORES["ameixa"], CORES["azul"], CORES["terracota"], "#8a6528"]
    for (x, y, titulo, linhas), fundo, contorno in zip(itens, fundos, contornos):
        partes.append(caixa(x, y, 215, 125, titulo, linhas, fundo, contorno))
    for inicio, fim in [((295, 167), (345, 167)), ((570, 167), (620, 167)), ((845, 167), (895, 167)), ((1010, 235), (890, 325)), ((780, 392), (725, 392)), ((500, 392), (445, 392))]:
        partes.append(f'<path class="seta" d="M{inicio[0]},{inicio[1]} L{fim[0]},{fim[1]}"/>')
    partes.append(caixa(400, 505, 400, 85, "Protocolo defensável", ["decisões coerentes, rastreáveis e revisáveis"], CORES["papel"], CORES["ameixa"]))
    partes.append('<path class="seta" d="M327,458 C330,510 370,540 395,540"/>')
    partes.append('<path class="seta tracejada" d="M400,548 C220,650 70,430 145,235"/>')
    partes.append(bloco_texto(190, 610, ["revisão por pares retorna às decisões"], "nota"))
    return documento(
        "Mapa integrado do protocolo da base",
        "Sete componentes — pergunta, fontes, seleção, cobertura, documentação, responsabilidade e viabilidade — convergem para um protocolo defensável e retornam à revisão.",
        "".join(partes),
        670,
    )


def main() -> None:
    IMAGENS.mkdir(parents=True, exist_ok=True)
    imagens = {
        "00_percurso_unidade.svg": percurso(),
        "01_populacao_acessivel_corpus.svg": populacao_corpus(),
        "01_papel_das_fontes.svg": papeis_fontes(),
        "02_cadeia_ausencias.svg": cadeia_ausencias(),
        "02_cobertura_catalogo_corpus.svg": cobertura_catalogo_corpus(),
        "03_documentacao_proveniencia.svg": documentacao_proveniencia(),
        "04_protocolo_integrado.svg": protocolo_integrado(),
    }
    for nome, conteudo in imagens.items():
        (IMAGENS / nome).write_text(conteudo, encoding="utf-8")
    print(f"{len(imagens)} SVGs construídos em {IMAGENS}")


if __name__ == "__main__":
    main()
