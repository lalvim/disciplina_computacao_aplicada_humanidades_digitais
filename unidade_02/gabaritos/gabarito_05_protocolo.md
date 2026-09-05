# Gabarito e rubrica — Protocolo da base

Não há uma única base correta. Avalie cada critério de 0 a 2.

| Critério | 0 — ausente | 1 — parcial | 2 — defensável |
|---|---|---|---|
| alinhamento | dados desconectados da pergunta | ligação implícita | observações necessárias e alcance explícitos |
| seleção | conveniência sem regra | regras sem justificativa/casos | regras reproduzíveis, justificadas e registradas |
| cobertura | não discutida | lista genérica de limites | dimensões, mecanismos, efeitos e mitigação |
| documentação | campos sem definição | dicionário incompleto | esquema, domínios, origem e limitações |
| proveniência | apenas arquivo/URL | origem sem transformações | fonte, agentes, versão, acesso e cadeia |
| governança, reuso, ética e legalidade | ignorados | riscos ou acesso citados genericamente | FAIR, usos, autoridade, pessoas afetadas, proteção e instâncias articulados |
| viabilidade | sem estimativa | dependências vagas | piloto, recursos, autorizações e contingência |

Uma aprovação exige pelo menos 11 de 14 pontos, sem nota zero em ética e
legalidade ou em alinhamento. A nota não substitui parecer do docente.

## Exemplo de resposta — protocolo integrado da base

Este exemplo condensado usa o catálogo fictício. Seu objetivo é mostrar como as
partes do protocolo se sustentam mutuamente, e não oferecer texto para cópia.

### 1. Alinhamento

**Pergunta delimitada:** como a composição do catálogo didático varia por
instituição, tipo documental e grupo representado entre 1890 e 1900, e como os
critérios de digitalização e acesso alteram o corpus disponível?

**Finalidade e estrutura analítica:** finalidade descritiva e estrutura
comparativa. Compararei o catálogo inicialmente acessível com o corpus formado
após o filtro e examinarei distribuições por instituição, gênero documental e
grupo representado. Não farei inferência sobre a população histórica.

**Unidade de análise:** item documental catalogado, identificado por
`id_fonte`.

**Observações necessárias:** ano, instituição, tipo documental, local, grupo
representado, localização, digitalização, condição de acesso e qualidade dos
metadados, além do motivo de inclusão ou exclusão.

### 2. Fontes e cadeia de produção

**Fontes primárias:** os itens documentais seriam primários para perguntas sobre
seus contextos de produção. Para a pergunta deste exemplo, o catálogo e os
registros de acesso/digitalização tornam-se fontes primárias sobre a construção
da coleção consultável.

**Fontes secundárias e dados derivados:** estudos sobre arquivos, seleção e
silêncios orientam a interpretação. O CSV, as tabelas de cobertura e a lista de
exclusões são derivados e devem permanecer vinculados aos registros de origem.

**Instituições e atores:** quatro custodiantes fictícios; produtores originais
dos documentos; equipe que catalogou; pesquisadora que aplicará as regras.

**Finalidade e categorias herdadas:** os documentos não foram produzidos para
responder à pergunta atual. Campos como `grupo_representado` são classificações
didáticas posteriores e não equivalem à autodefinição dos sujeitos.

**Acesso:** público, mediante autorização, restrito ou sem autorização. Acesso
técnico não equivale a licença para reproduzir ou publicar.

### 3. População, corpus e seleção

**População de interesse:** todos os itens das quatro instituições, entre 1890 e
1900, relevantes para descrever a composição e as condições de acesso.

**População acessível:** os 16 registros conhecidos no catálogo, incluindo os
que não podem ser consultados nesta etapa.

**Corpus previsto:** nove itens que satisfazem simultaneamente período,
localização, digitalização e condição de acesso: A001, A002, A004, B001, B002,
C001, C002, C003 e C004.

| Critério | Campo/evidência | Regra | Justificativa | Caso limítrofe |
|---|---|---|---|---|
| inclusão | `ano`, `localizado`, `digitalizado`, `condicao_acesso` | 1890–1900; sim; sim; público ou mediante autorização | compatibilidade com a pergunta e viabilidade remota | C004 entra porque 1900 integra o intervalo |
| exclusão | os mesmos campos | falhar em pelo menos uma regra | não usar material fora do recorte ou sem condição atual de consulta | A003 pode ser reconsiderado após autorização e digitalização |

**Registro das exclusões:** tabela separada, sem apagar casos, contendo um campo
booleano para cada regra, decisão final, data, responsável e observação.

### 4. Cobertura, vieses e silêncios

| Dimensão | Cobertura | Lacuna | Efeito sobre a análise | Mitigação |
|---|---|---|---|---|
| temporal | 1890–1895 e 1900 | 1896–1899 sem registros | impede interpretar continuidade anual | mostrar anos vazios e buscar inventários adicionais |
| espacial | Capital e Interior | combinações desiguais com instituição/tipo | local pode confundir-se com composição institucional | cruzar dimensões e limitar comparações |
| social | cinco grupos no corpus | família proprietária desaparece | proporções resultam parcialmente do filtro | comparar catálogo e corpus |
| institucional | três instituições no corpus | Coleção Particular ausente | favorece acervos digitalizados e acessíveis | negociar consulta/autorização |
| documental | atas, requerimento, cartas e jornais | sem fotografia e diário | restringe conclusões a certos gêneros | buscar versões consultáveis e separar análises por gênero |

**Mecanismo de viés:** a exigência de digitalização seleciona condições de
infraestrutura, que se associam às instituições e aos tipos documentais.

**Silêncios:** experiências nunca registradas, documentos perdidos e vozes
representadas apenas por categorias institucionais não aparecem como simples
valores nulos.

**Limite:** o resultado descreve a composição do catálogo e o efeito das regras;
não mede a presença ou a importância dos grupos na sociedade do período.

### 5. Metadados, identificadores e proveniência

**Identificador:** `id_fonte`, único na versão da base e independente de campos
mutáveis; códigos dos acervos reais seriam preservados em `id_origem`.

| Campo | Definição | Tipo/domínio | Origem | Regra | Limitação |
|---|---|---|---|---|---|
| `grupo_representado` | grupo mais diretamente registrado | categoria documentada | equipe de catalogação | um valor principal por item | não mede voz, autoria ou protagonismo |

**Administrativos e direitos:** custodiante, condição de acesso, licença,
responsável pelo registro, versão e data da consulta.

**Ligação:** todas as tabelas derivadas conservarão `id_fonte`; transcrições e
imagens acrescentarão referência do arquivo, página ou segmento.

**Proveniência:** registrar entidade de entrada, atividade, agente, data, código
executado e saída. Os arquivos recebidos serão preservados sem sobrescrita.

### 6. Governança, reuso, ética e questões legais

**FAIR:** os identificadores, o dicionário e a proveniência oferecem evidências
iniciais de encontrabilidade e reuso. Ainda faltam protocolo de recuperação,
licença, vocabulários relacionados a padrões do campo e política de versões.
Essas lacunas serão registradas como ações, não convertidas em uma nota FAIR.

**Acesso, licença e usos:** `condicao_acesso` descreve consulta e não concede
reutilização. Cada custodiante deverá informar separadamente acesso, reprodução
e publicação. O corpus poderá apoiar o estudo da composição do catálogo e dos
efeitos da seleção; não deverá sustentar inferências sobre a importância
histórica dos grupos nem ser redistribuído sem direitos verificados.

**Datasheet e manutenção:** a pesquisadora manterá uma ficha com motivação,
composição, coleta, processamento, usos, distribuição e manutenção. Cada versão
indicará data, alterações, responsável e forma de comunicar correções.

Embora os dados da atividade sejam fictícios, um projeto real pode conter nomes,
imagens, filiações e informações sensíveis, inclusive relativas a descendentes
ou comunidades. Antes da publicação, consultarei as instâncias institucionais
competentes, verificarei direitos e termos dos acervos e aplicarei minimização.
Arquivos restritos ficarão em área com controle de acesso. Resultados públicos
não incluirão dados que permitam reidentificação sem justificativa e avaliação.

**CARE:** o catálogo fictício não contém dados indígenas reais, portanto não se
alega conformidade. Se as fontes reais envolverem povos, conhecimentos,
territórios ou patrimônio indígenas, benefício, autoridade para controlar,
responsabilidade e ética serão definidos com os povos envolvidos; custódia
institucional ou acesso público não serão tomados como autorização suficiente.

### 7. Viabilidade e contingência

O piloto usará 20 itens ou todos os registros se o conjunto continuar pequeno.
Serão estimadas dez horas para conferir metadados e quatro para documentar
decisões. Dependências: autorização, qualidade das imagens e disponibilidade do
acervo. Se a Coleção Particular permanecer inacessível, o corpus principal será
mantido sem ela e essa ausência será tratada como limite; não será substituída
silenciosamente por outra coleção. Análise de conteúdo integral ficará fora
desta etapa.

### 8. Autoavaliação — exemplo

| Critério | Nota | Evidência ou revisão necessária |
|---|---:|---|
| alinhamento entre pergunta e dados | 2 | pergunta descreve propriedades observáveis no catálogo |
| seleção reproduzível | 2 | campos, regras e casos limítrofes registrados |
| cobertura e vieses | 2 | cinco dimensões e mecanismos discutidos |
| metadados e identificadores | 2 | estratégia e exemplo de campo definidos |
| proveniência | 1 | estrutura prevista, ainda sem log real do piloto |
| governança, reuso, ética e questões legais | 1 | riscos e usos reconhecidos, mas autoridade, termos e protocolo de acesso reais ainda precisam ser verificados |
| viabilidade | 2 | piloto, estimativa e plano alternativo delimitados |

**Total: 12/14. Decisão:** manter com revisão obrigatória da proveniência do
piloto e das condições legais antes de iniciar a coleta real.

### 9. Revisão por pares — exemplo

**Parecer recebido:** o intervalo está claro e as exclusões são auditáveis, mas
`grupo_representado` pode ocultar múltiplos grupos em um mesmo documento. A
resposta também deve deixar explícito se “mediante autorização” permite apenas
consulta ou reprodução.

**Mudanças realizadas:** acrescentei ao dicionário a limitação do campo
`grupo_representado`, previ uma futura tabela de relação muitos-para-muitos e
separei autorização de consulta da licença de reprodução. Essas mudanças evitam
que conveniência da tabela seja confundida com propriedade da fonte.

**Referências mobilizadas:** AHA (2023), Gebru et al. (2021), Rodrigues (2020),
Trouillot (1995), Schwartz e Cook (2002), Wilkinson et al. (2016), Carroll et
al. (2020), W3C PROV-O, ANPD e LGPD, conforme `referencias.md`.
