"""Gera exercício HTML offline e versão textual da Unidade 3."""

from __future__ import annotations

import json
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]
UNIDADE = RAIZ / "unidade_03"

Q = [
    ("Camadas de dados", "Qual prática preserva melhor a auditabilidade?", ["Editar o CSV recebido", "Manter brutos imutáveis e gerar derivados", "Copiar valores manualmente", "Excluir o original após limpar"], 1, "A separação em camadas permite reconstruir e comparar transformações."),
    ("Estrutura tabular", "Em uma tabela de documentos, cada linha deve representar:", ["uma unidade de análise declarada", "qualquer quantidade de objetos", "uma coluna", "um arquivo obrigatoriamente"], 0, "A unidade da linha precisa ser coerente e explícita."),
    ("Formatos", "Qual afirmação sobre PDF é correta?", ["Sempre contém texto extraível", "É equivalente a TXT", "Pode conter texto, imagem ou ambos", "É sempre tabular"], 2, "PDF é um contêiner orientado à página e exige inspeção."),
    ("Formatos", "Ao importar XLSX, é importante registrar:", ["somente o tamanho", "planilha e parâmetros usados", "apenas a cor das células", "nenhuma decisão"], 1, "Um arquivo pode conter várias planilhas e estruturas."),
    ("Base pública", "Por que manter cópia local com data e proveniência?", ["Porque bases públicas nunca mudam", "Para eliminar a fonte", "Para identificar a versão efetivamente processada", "Para evitar citar o produtor"], 2, "A cópia e a proveniência fixam o objeto usado no processamento."),
    ("Extração e OCR", "Extração de texto e OCR diferem porque:", ["OCR reconhece caracteres em imagem", "extração sempre corrige erros", "OCR lê apenas CSV", "são operações idênticas"], 0, "OCR produz uma transcrição a partir de pixels; extração acessa texto já codificado."),
    ("OCR", "Qual procedimento é metodologicamente adequado?", ["Aceitar toda saída", "Avaliar uma amostra contra referência", "Apagar imagens", "Omitir ferramenta e parâmetros"], 1, "A qualidade deve ser medida e os casos problemáticos revisados."),
    ("Largo e longo", "Ao transformar indicadores largos em longos, muda:", ["a fonte original", "a unidade representada por cada linha", "a licença", "o idioma do texto"], 1, "A linha passa a representar combinações das dimensões explicitadas."),
    ("Normalização", "Por que preservar o valor original?", ["Para impedir qualquer correção", "Para auditar e eventualmente rever a regra", "Para duplicar sem propósito", "Para dispensar documentação"], 1, "Original e derivado permitem rastrear perdas e decisões."),
    ("Códigos", "Um código de município deve ser lido preferencialmente como:", ["medida contínua", "identificador textual", "data", "valor monetário"], 1, "Operações aritméticas não têm sentido para o identificador."),
    ("Datas e ausências", "Converter falhas de data para ausente exige:", ["apagar o original", "guardar original e razão da ausência", "inventar primeiro dia", "excluir a linha"], 1, "A razão diferencia desconhecimento, erro e inaplicabilidade."),
    ("Duplicatas", "Uma possível duplicata deve:", ["ser apagada automaticamente", "ser tratada como hipótese para revisão", "ser identificada só pelo título", "ser ignorada"], 1, "Registros semelhantes podem representar objetos distintos."),
    ("Junções", "O argumento validate='many_to_one' testa:", ["a cor da tabela", "a cardinalidade esperada", "a qualidade do OCR", "o encoding"], 1, "A validação impede aceitar silenciosamente chaves incompatíveis."),
    ("Junções", "O indicador left_only após uma junção significa:", ["registro da esquerda sem correspondência", "duplicata confirmada", "linha vazia", "erro de sintaxe"], 0, "A não correspondência precisa ser diagnosticada, não descartada."),
    ("Integração", "Como representar vários temas por documento?", ["Sobrescrever o tema", "Tabela relacional documento–tema", "Concatenar sem regra", "Duplicar todos os metadados manualmente"], 1, "Uma tabela de relações preserva multiplicidade de forma explícita."),
    ("Reprodutibilidade", "Um notebook numerado, sozinho:", ["garante reprodutibilidade total", "não basta sem ambiente, entradas e testes", "elimina proveniência", "substitui dados brutos"], 1, "Reprodução exige mais que ordem visual."),
    ("Limpeza crítica", "A expressão 'dados limpos' pode ser problemática porque:", ["toda transformação é proibida", "pode ocultar escolhas interpretativas e perdas", "CSV não aceita limpeza", "dados não têm erros"], 1, "Transformações são necessárias, mas devem ser situadas e auditáveis."),
    ("Integração", "Qual produto está pronto para a Unidade 4?", ["Arquivos sobrescritos sem log", "Base processável com chaves, testes, log e limites", "PDFs sem inventário", "Tabela sem unidade declarada"], 1, "A exploração depende de uma base reconstruível e documentada."),
]

def main() -> None:
    dados = [{"topico":a,"enunciado":b,"alternativas":c,"correta":d,"explicacao":e} for a,b,c,d,e in Q]
    bloco = json.dumps(dados, ensure_ascii=False)
    pagina = f'''<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Exercícios — Unidade 3</title><style>body{{font-family:system-ui;max-width:900px;margin:auto;padding:2rem;line-height:1.5;background:#f4f6f7;color:#202528}}fieldset{{background:white;border:1px solid #9aa7ad;border-radius:8px;margin:1rem 0;padding:1rem}}legend{{font-weight:700}}label{{display:block;padding:.35rem}}button{{padding:.7rem 1rem;font-weight:700}}.retorno{{margin-top:.6rem;border-left:4px solid #385b66;padding:.5rem;background:#eaf1f3}}</style></head><body><h1>Exercícios de revisão — Unidade 3</h1><p>Marque uma alternativa por questão.</p><noscript><p>Use a <a href="exercicios_unidade_03_texto.md">versão textual</a>.</p></noscript><main id="quiz"></main><button id="corrigir">Corrigir</button><p id="resultado" role="status" aria-live="polite"></p><script>const questoes={bloco};const quiz=document.getElementById("quiz");questoes.forEach((q,i)=>{{const f=document.createElement("fieldset"),l=document.createElement("legend");l.textContent=`${{i+1}}. ${{q.enunciado}}`;f.appendChild(l);q.alternativas.forEach((a,j)=>{{const x=document.createElement("label");x.innerHTML=`<input type="radio" name="q${{i}}" value="${{j}}"> ${{String.fromCharCode(65+j)}}. ${{a}}`;f.appendChild(x)}});const r=document.createElement("div");r.className="retorno";r.hidden=true;f.appendChild(r);quiz.appendChild(f)}});document.getElementById("corrigir").onclick=()=>{{let n=0;[...quiz.children].forEach((f,i)=>{{const m=f.querySelector("input:checked"),r=f.querySelector(".retorno"),ok=m&&+m.value===questoes[i].correta;if(ok)n++;r.hidden=false;r.textContent=(ok?"Correto. ":"Resposta: "+String.fromCharCode(65+questoes[i].correta)+". ")+questoes[i].explicacao}});document.getElementById("resultado").textContent=`Resultado: ${{n}} de ${{questoes.length}}.`}};</script></body></html>'''
    (UNIDADE/"exercicios_unidade_03.html").write_text(pagina,encoding="utf-8")
    linhas=["# Exercícios da Unidade 3 — versão textual","","Marque uma alternativa e consulte o gabarito após concluir.",""]
    for n,(t,e,alts,_,__) in enumerate(Q,1):
        linhas += [f"## Questão {n} — {t}","",e,""]+[f"- [ ] **{l}.** {a}" for l,a in zip("ABCD",alts)]+[""]
    (UNIDADE/"exercicios_unidade_03_texto.md").write_text("\n".join(linhas),encoding="utf-8")
    print("Exercícios da Unidade 3 gerados.")

if __name__ == "__main__": main()
