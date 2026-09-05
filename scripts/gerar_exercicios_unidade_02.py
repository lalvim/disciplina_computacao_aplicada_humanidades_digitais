"""Gera o exercício HTML offline e sua versão textual para a Unidade 2."""

from __future__ import annotations

import html
import json
from pathlib import Path


RAIZ = Path(__file__).resolve().parents[1]
UNIDADE = RAIZ / "unidade_02"

QUESTOES = [
    ("População e corpus", "Qual formulação distingue corretamente população de interesse e corpus?",
     ["São sempre conjuntos idênticos.", "A população delimita o alcance pretendido; o corpus reúne casos efetivamente selecionados.", "Corpus é apenas uma amostra probabilística.", "População é o conjunto já digitalizado."], 1,
     "A população se relaciona ao alcance da pergunta; o corpus resulta das condições de acesso e dos critérios adotados."),
    ("População e corpus", "Usar somente itens digitalizados delimita principalmente:",
     ["o fenômeno histórico", "a população de interesse", "a população acessível e o corpus", "a unidade de análise"], 2,
     "Digitalização é uma condição de infraestrutura e acesso, não uma propriedade natural do fenômeno."),
    ("Fontes", "Quando um catálogo institucional pode ser fonte primária?",
     ["Nunca.", "Somente se estiver em CSV.", "Quando a pergunta investiga práticas de catalogação ou da instituição.", "Sempre que substituir os documentos descritos."], 2,
     "O papel de uma fonte depende da relação com a pergunta."),
    ("Fontes", "Uma tabela transcrita de documentos deve ser tratada como:",
     ["o próprio fenômeno", "dado derivado ligado às fontes e decisões de transcrição", "fonte sem proveniência", "prova autossuficiente"], 1,
     "A representação derivada precisa manter rastreabilidade até as fontes."),
    ("Seleção", "Qual critério é mais reproduzível?",
     ["Documentos relevantes.", "Itens interessantes.", "Registros de 1890 a 1900 com ano documentado.", "Fontes de boa qualidade."], 2,
     "O intervalo e o campo tornam a regra verificável, embora a justificativa ainda precise ser defendida."),
    ("Seleção", "Por que registrar motivos de exclusão por item?",
     ["Para eliminar a interpretação.", "Para auditar consequências e reproduzir a seleção.", "Para provar representatividade.", "Para corrigir silêncios históricos."], 1,
     "O registro permite reconstituir regras e examinar perdas."),
    ("Cobertura", "Cobertura e representatividade são:",
     ["sinônimos", "atributos garantidos por bases grandes", "conceitos distintos; representatividade depende do desenho e da inferência", "irrelevantes em corpus"], 2,
     "Boa cobertura em uma dimensão não garante representação adequada da população."),
    ("Cobertura", "Comparar a distribuição de grupos antes e depois do filtro permite:",
     ["medir a importância histórica dos grupos", "observar como a seleção altera o catálogo disponível", "provar causalidade", "recuperar fontes inexistentes"], 1,
     "A comparação diagnostica efeitos do recorte sobre os dados disponíveis."),
    ("Viés de seleção", "Selecionar apenas materiais digitalizados pode favorecer:",
     ["aleatoriamente todos os casos", "instituições e gêneros com mais condições de digitalização", "somente valores ausentes", "a persistência dos identificadores"], 1,
     "Digitalização pode estar sistematicamente associada a recursos, formatos e políticas."),
    ("Ausências e silêncios", "Qual exemplo é um silêncio documental, e não apenas um valor nulo?",
     ["Uma célula sem ano em registro existente.", "Experiências que não foram registradas ou preservadas.", "Um erro de digitação.", "Uma categoria escrita de duas formas."], 1,
     "A ausência no processo documental não se resolve preenchendo a tabela."),
    ("Metadados", "Qual é um metadado administrativo?",
     ["Condição de direitos e acesso.", "Tema interpretado no argumento final.", "Hipótese causal.", "Resultado de um modelo futuro."], 0,
     "Direitos, acesso, formatos e responsáveis apoiam gestão e uso."),
    ("Dicionário de dados", "Um dicionário de dados deve registrar:",
     ["somente nomes das colunas", "definições, tipos, regras, origem e limitações", "apenas código Python", "somente resultados estatísticos"], 1,
     "O dicionário explicita o significado e as restrições dos campos."),
    ("Identificadores", "Qual característica é desejável em um identificador?",
     ["Mudar quando o título é corrigido.", "Ser único no escopo e relativamente persistente.", "Ser sempre o número da linha.", "Conter todos os atributos do item."], 1,
     "Identificadores devem sustentar relações mesmo quando descrições mudam."),
    ("Proveniência", "Qual registro de proveniência é mais completo?",
     ["Apenas a URL.", "Origem, agente, data/versão, condições e transformações.", "Somente o nome do arquivo.", "A contagem de linhas."], 1,
     "Proveniência documenta a cadeia de produção e transformação."),
    ("Ética", "Dados publicamente acessíveis:",
     ["podem sempre ser republicados sem análise", "dispensam segurança", "ainda exigem avaliação de finalidade, riscos, direitos e contexto", "não podem ser pesquisados"], 2,
     "Acesso técnico não encerra as responsabilidades éticas ou legais."),
    ("Ética", "Os princípios CARE enfatizam, entre outros aspectos:",
     ["benefício coletivo e autoridade para controlar", "apenas abertura irrestrita", "eliminação de metadados", "neutralidade das bases"], 0,
     "CARE centra pessoas, propósitos, direitos e interesses indígenas."),
    ("FAIR", "Nos princípios FAIR, dizer que dados são acessíveis significa necessariamente que:",
     ["qualquer pessoa pode baixá-los sem restrição", "existe um procedimento explícito de acesso, que pode incluir autenticação e autorização", "os dados não têm direitos associados", "todos os registros devem ser publicados em uma planilha"], 1,
     "Acessibilidade requer um protocolo claro; dados protegidos podem continuar sujeitos a controle de acesso."),
    ("FAIR e CARE", "Qual afirmação relaciona adequadamente FAIR e CARE?",
     ["CARE substitui todos os requisitos técnicos de FAIR.", "Uma base FAIR é automaticamente justa.", "FAIR focaliza condições de localização e reuso; CARE acrescenta benefício, autoridade, responsabilidade e ética no contexto dos dados indígenas.", "Os dois conjuntos de princípios exigem abertura irrestrita."], 2,
     "As lentes são complementares: capacidade técnica de reuso não resolve sozinha autoridade, direitos ou benefícios."),
    ("Datasheets", "Qual conjunto corresponde às partes propostas em Datasheets for Datasets?",
     ["Somente título, autoria e palavras-chave.", "Motivação, composição, coleta, processamento, usos, distribuição e manutenção.", "Apenas acurácia e desempenho de modelos.", "Somente licença e endereço eletrônico."], 1,
     "A proposta acompanha o ciclo de vida e explicita escolhas, usos, riscos, distribuição e manutenção."),
    ("Questões legais", "Diante de dados pessoais em um projeto real, o estudante deve:",
     ["seguir apenas este notebook", "consultar regras aplicáveis e instâncias institucionais competentes", "publicar primeiro e avaliar depois", "presumir consentimento"], 1,
     "O material é educativo e não substitui avaliação ética, institucional ou jurídica."),
    ("Integração", "Qual protocolo é mais defensável?",
     ["Base grande sem documentação.", "Seleção explícita, cobertura discutida, proveniência e riscos registrados.", "Apenas arquivos disponíveis online.", "Tabela limpa sem ligação com as fontes."], 1,
     "Adequação resulta da coerência entre pergunta, seleção, documentação, limites e responsabilidades."),
]


def gerar_html() -> None:
    dados = [
        {
            "topico": topico,
            "enunciado": enunciado,
            "alternativas": alternativas,
            "correta": correta,
            "explicacao": explicacao,
        }
        for topico, enunciado, alternativas, correta, explicacao in QUESTOES
    ]
    bloco = json.dumps(dados, ensure_ascii=False)
    pagina = f"""<!doctype html>
<html lang="pt-BR"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Exercícios — Unidade 2</title>
<style>
body{{font-family:system-ui,sans-serif;max-width:900px;margin:auto;padding:2rem;line-height:1.5;background:#f7f4ee;color:#24211d}}
h1{{color:#513b2c}} fieldset{{background:white;border:1px solid #c9bba9;border-radius:8px;margin:1rem 0;padding:1rem}}
legend{{font-weight:700}} label{{display:block;padding:.35rem}} button{{padding:.7rem 1rem;font-weight:700}}
.retorno{{margin-top:.7rem;padding:.6rem;border-left:4px solid #765b43;background:#f2eadf}} a{{color:#60452f}}
</style></head><body>
<h1>Exercícios de revisão — Unidade 2</h1>
<p>Marque uma alternativa por questão. A correção apresenta explicações, não apenas a letra.</p>
<noscript><p>JavaScript está desativado. Use a <a href="exercicios_unidade_02_texto.md">versão textual</a>.</p></noscript>
<main id="quiz"></main><button id="corrigir">Corrigir respostas</button>
<p id="resultado" role="status" aria-live="polite"></p>
<script>
const questoes={bloco};
const quiz=document.getElementById("quiz");
questoes.forEach((q,i)=>{{
 const f=document.createElement("fieldset"); const l=document.createElement("legend");
 l.textContent=`${{i+1}}. ${{q.enunciado}}`; f.appendChild(l);
 q.alternativas.forEach((a,j)=>{{const label=document.createElement("label");
 label.innerHTML=`<input type="radio" name="q${{i}}" value="${{j}}"> ${{String.fromCharCode(65+j)}}. ${{a}}`; f.appendChild(label);}});
 const r=document.createElement("div"); r.className="retorno"; r.hidden=true; f.appendChild(r); quiz.appendChild(f);
}});
document.getElementById("corrigir").addEventListener("click",()=>{{
 let acertos=0; [...quiz.children].forEach((f,i)=>{{const m=f.querySelector("input:checked"); const r=f.querySelector(".retorno");
 const ok=m&&Number(m.value)===questoes[i].correta; if(ok)acertos++; r.hidden=false;
 r.textContent=(ok?"Correto. ":"Resposta esperada: "+String.fromCharCode(65+questoes[i].correta)+". ")+questoes[i].explicacao;}});
 document.getElementById("resultado").textContent=`Resultado: ${{acertos}} de ${{questoes.length}}.`;
}});
</script></body></html>"""
    (UNIDADE / "exercicios_unidade_02.html").write_text(pagina, encoding="utf-8")


def gerar_texto() -> None:
    linhas = [
        "# Exercícios da Unidade 2 — versão textual", "",
        "Marque uma alternativa por questão e consulte o gabarito após concluir.", "",
    ]
    for numero, (topico, enunciado, alternativas, _, _) in enumerate(QUESTOES, 1):
        linhas.extend([f"## Questão {numero} — {topico}", "", enunciado, ""])
        for letra, alternativa in zip("ABCD", alternativas):
            linhas.append(f"- [ ] **{letra}.** {alternativa}")
        linhas.append("")
    (UNIDADE / "exercicios_unidade_02_texto.md").write_text(
        "\n".join(linhas), encoding="utf-8"
    )


if __name__ == "__main__":
    gerar_html()
    gerar_texto()
    print("Exercícios da Unidade 2 gerados.")
