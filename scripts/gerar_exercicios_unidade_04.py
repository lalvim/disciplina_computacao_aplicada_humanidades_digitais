"""Gera quiz offline da Unidade 4."""
import json
from pathlib import Path
U=Path(__file__).resolve().parents[1]/"unidade_04"
Q=[
("Variáveis","Código municipal numérico é:",["medida contínua","identificador","proporção","variância"],1,"A aparência numérica não altera seu papel de identificador."),
("Frequências","Uma proporção exige declarar:",["a cor","o denominador","a moda","o OCR"],1,"Sem denominador, a comparação fica ambígua."),
("Centro","Qual medida é mais sensível a um extremo alto?",["média","mediana","moda","quartil"],0,"A média utiliza todos os valores."),
("Dispersão","O desvio-padrão descreve:",["categoria modal","dispersão em torno da média","causalidade","tamanho do corpus"],1,"Ele retorna à unidade da variável."),
("Quartis","O intervalo interquartil é:",["Q3 menos Q1","máximo menos mínimo","média menos moda","variância ao quadrado"],0,"IQR cobre a metade central ordenada."),
("Extremos","Um caso além de 1,5×IQR deve:",["ser apagado","ser inspecionado","provar erro","confirmar hipótese"],1,"A regra sinaliza, não decide."),
("Contingência","Proporções por linha mostram:",["composição dentro de cada linha","causalidade","média textual","OCR"],0,"O denominador é o total da linha."),
("Tokenização","Tokenizar significa:",["segmentar segundo regra","traduzir","testar hipótese","remover contexto sem registro"],0,"A segmentação depende de convenções."),
("Normalização","Converter tudo em minúsculas pode:",["preservar toda distinção","apagar informação de capitalização","calcular quartis","criar PDF"],1,"Normalização tem perdas possíveis."),
("Frequência textual","Frequência relativa divide por:",["total de tokens relevante","número de gráficos","mediana","IQR"],0,"Ela explicita o denominador textual."),
("Concordância","Concordâncias servem para:",["recuperar contexto local","provar associação","remover extremos","calcular variância"],0,"Janelas ligam agregado a ocorrências."),
("N-gramas","Um bigrama contém:",["duas unidades adjacentes","dois quartis","duas tabelas","duas hipóteses"],0,"N define o tamanho da sequência."),
("Colocações","PMI exige cautela porque:",["favorece eventos raros","é sempre causal","não usa palavras","mede mediana"],0,"Frequência mínima e contexto ajudam."),
("Diversidade","TTR bruta é afetada por:",["tamanho do texto","cor do gráfico","ano apenas","tipo do PDF"],0,"Textos maiores tendem a menor TTR."),
("Barras","Barras são adequadas principalmente para:",["categorias","texto integral","causalidade","OCR"],0,"Comprimento facilita comparar categorias."),
("Histograma","A aparência do histograma depende:",["dos intervalos","da moda apenas","do título apenas","do ID"],0,"Bins condicionam a forma visível."),
("Dispersão","Um padrão de pontos prova causalidade?",["sim","não","apenas com cor","sempre em HD"],1,"Exploração de relação não estabelece causa."),
("Relatório","Uma hipótese exploratória deve ser:",["provisória e acompanhada de alternativas","tratada como confirmada","omitida","chamada significativa"],0,"Ela orienta investigação posterior."),]
def main():
 d=[{"topico":a,"enunciado":b,"alternativas":c,"correta":e,"explicacao":f} for a,b,c,e,f in Q]; bloco=json.dumps(d,ensure_ascii=False)
 h=f'''<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width"><title>Unidade 4</title><style>body{{font-family:system-ui;max-width:900px;margin:auto;padding:2rem}}fieldset{{margin:1rem;padding:1rem}}label{{display:block}}.r{{background:#eef;padding:.5rem}}</style></head><body><h1>Exercícios — Unidade 4</h1><noscript><a href="exercicios_unidade_04_texto.md">Versão textual</a></noscript><main id="q"></main><button id="b">Corrigir</button><p id="s" role="status" aria-live="polite"></p><script>const qs={bloco},q=document.getElementById("q");qs.forEach((x,i)=>{{let f=document.createElement("fieldset");f.innerHTML=`<legend>${{i+1}}. ${{x.enunciado}}</legend>`;x.alternativas.forEach((a,j)=>f.innerHTML+=`<label><input type="radio" name="q${{i}}" value="${{j}}">${{String.fromCharCode(65+j)}}. ${{a}}</label>`);f.innerHTML+='<div class="r" hidden></div>';q.appendChild(f)}});b.onclick=()=>{{let n=0;[...q.children].forEach((f,i)=>{{let m=f.querySelector('input:checked'),r=f.querySelector('.r'),ok=m&&+m.value===qs[i].correta;if(ok)n++;r.hidden=false;r.textContent=(ok?'Correto. ':'Resposta: '+String.fromCharCode(65+qs[i].correta)+'. ')+qs[i].explicacao}});s.textContent=`Resultado: ${{n}} de 18.`}};</script></body></html>'''; (U/"exercicios_unidade_04.html").write_text(h,encoding="utf-8")
 linhas=["# Exercícios da Unidade 4 — versão textual",""]
 for i,(t,e,a,_,__) in enumerate(Q,1): linhas += [f"## Questão {i} — {t}","",e,""]+[f"- [ ] **{l}.** {v}" for l,v in zip("ABCD",a)]+[""]
 (U/"exercicios_unidade_04_texto.md").write_text("\n".join(linhas),encoding="utf-8"); print("Quiz 4 gerado")
if __name__=="__main__": main()
