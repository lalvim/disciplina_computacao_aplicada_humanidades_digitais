# Gabarito — Governança, reuso e documentação de bases

Este gabarito apresenta uma resolução possível para o catálogo fictício. A
avaliação deve considerar a qualidade das evidências e justificativas, não a
reprodução literal do exemplo.

## Resultado esperado da auditoria

| Princípio | Evidência examinada | Presente |
|---|---|:---:|
| F | identificadores únicos e não vazios | verdadeiro |
| F | campos do catálogo documentados | verdadeiro |
| A | condição de acesso por registro | verdadeiro |
| A | protocolo de solicitação ou recuperação | falso |
| I | formato estruturado e dicionário de dados | verdadeiro |
| R | origem e transformações registradas | verdadeiro |
| R | licença ou termos de reutilização | falso |

O código verifica a presença de alguns elementos. Ele não demonstra que os
identificadores persistirão, que as definições são semanticamente adequadas ou
que a condição de acesso foi legitimamente estabelecida.

### Respostas às perguntas de interpretação

1. Falta um protocolo de solicitação ou recuperação: endereço, responsável,
   procedimento, autenticação eventualmente necessária e resposta esperada.
2. `condicao_acesso` informa como o item fictício pode ser consultado. Uma
   licença ou termo de uso define permissões e restrições de cópia,
   redistribuição, adaptação e atribuição. Poder consultar não implica poder
   republicar.
3. O código não verifica vocabulários compartilhados, formatos de intercâmbio,
   relações com identificadores externos, semântica legível por máquinas nem
   compatibilidade com padrões do campo.
4. Os testes possuem alcances diferentes e não receberam pesos ou métricas
   justificadas. Um valor verdadeiro pode esconder documentação superficial.
   Somá-los produziria precisão aparente, não uma avaliação FAIR conclusiva.

## Exemplo de resposta — ficha de governança e documentação

### Parte A — evidências FAIR

| Princípio | Evidência | Lacuna | Ação ou decisão |
|---|---|---|---|
| F | os 16 registros possuem `id_fonte` único e todos os campos constam no dicionário | o identificador é apenas local e não há mecanismo público de busca | manter o identificador interno durante o piloto e avaliar URI ou identificador institucional antes da publicação |
| A | cada item possui uma condição de acesso | não há endereço, contato ou procedimento para solicitar os itens | acrescentar ao registro do custodiante o canal de acesso, requisitos, prazo de resposta e data de verificação |
| I | catálogo e dicionário estão em CSV com codificação UTF-8 | categorias como `grupo_representado` são locais e não estão ligadas a vocabulários documentados | publicar o vocabulário local com definições; mapear somente equivalências que forem conceitualmente defensáveis |
| R | origem, finalidade e três transformações estão registradas | faltam licença, versão formal e usos inadequados | criar versão numerada, termos de reutilização e seção de usos e limites no datasheet |

Essa matriz não autoriza concluir que “a base é FAIR”. Ela identifica o que já
pode ser demonstrado e o que precisa de decisão ou documentação adicional.

### Parte B — governança e CARE

**Pertinência ao caso:** os dados da atividade são inteiramente fictícios e não
representam povos indígenas, pessoas ou instituições reais. Assim, não é
possível alegar aplicação substantiva de CARE ao catálogo. Em um projeto real,
a equipe verificaria, com os povos envolvidos e não apenas pela descrição do
acervo, se documentos, conhecimentos, territórios ou patrimônio indígena estão
implicados.

**Benefício e autoridade:** no exercício, a equipe docente controla os arquivos
porque os criou para ensino. Em uma coleção real, custódia institucional não
seria tomada automaticamente como autoridade moral para liberar todos os usos.
Seriam identificados titulares de direitos, povos e comunidades relacionados,
assim como seus protocolos e instâncias de decisão.

**Responsabilidade continuada:** manter contato responsável, corrigir registros,
documentar versões, comunicar mudanças de acesso, retirar conteúdos quando isso
for legitimamente requerido e evitar que classificações produzidas pela equipe
sejam apresentadas como autodescrições das comunidades.

**Ética e usos futuros:** pessoas ou coletividades afetadas precisariam avaliar
riscos de exposição, estigmatização, reidentificação, apropriação de
conhecimentos e recombinação com outras bases. Essa participação não pode ser
substituída pelo preenchimento desta ficha.

### Parte C — exemplo de minidatasheet

**Motivação e responsáveis:** catálogo criado pela equipe docente para ensinar
seleção, cobertura, metadados, proveniência e governança. Não corresponde a um
levantamento histórico e não recebeu financiamento específico.

**Composição, cobertura e lacunas:** contém 16 itens fictícios, quatro
instituições simuladas, seis gêneros documentais e anos de 1890 a 1904. As
lacunas de localização, digitalização e qualidade descritiva foram introduzidas
deliberadamente. A unidade de análise é o item catalogado, não uma pessoa ou
grupo social.

**Coleta e processamento:** os registros foram escritos manualmente em 30 de
julho de 2026. Receberam identificadores e nomes institucionais normalizados. A
equipe criou lacunas para fins didáticos; não houve extração de acervo real,
OCR, entrevista ou classificação automática.

**Usos recomendados:** experimentos de seleção, comparação entre catálogo e
corpus, auditoria de campos e discussão metodológica em sala.

**Usos inadequados:** afirmações sobre instituições, grupos, acervos ou processos
históricos reais; treinamento ou avaliação como se as categorias fossem dados
empíricos; inferência de representatividade social.

**Distribuição, acesso e licença:** os arquivos acompanham o repositório da
disciplina. Antes de sua reutilização externa, deve-se verificar a licença geral
do repositório; as condições de acesso inscritas nos registros são exemplos e
não concedem direitos sobre acervos reais.

**Manutenção e versão:** a equipe docente mantém o conjunto junto ao material da
unidade. Alterações devem atualizar a data, o arquivo de proveniência, o
dicionário, os resultados esperados e os diagramas derivados. Um canal de
contato e uma política explícita de versionamento ainda precisam ser definidos.

### Parte D — exemplo de parecer e revisão

**Parecer da dupla:** a ficha distingue acesso de licença e reconhece que CARE
não pode ser reivindicado para o caso fictício. Entretanto, “vocabulário
documentado” ainda é uma ação vaga, e o contato de manutenção permanece ausente.
Além disso, o uso inadequado em sistemas de classificação deveria ser declarado
explicitamente.

**Mudança realizada:** a versão revista especificou a publicação das definições
do vocabulário local, acrescentou a necessidade de canal de contato e proibiu o
uso do catálogo como conjunto empírico para treinar ou avaliar classificadores.

### Por que esta resposta é defensável?

Ela separa evidência computável de julgamento situado, não confunde FAIR com
abertura irrestrita, preserva o contexto indígena de CARE e adapta o datasheet
sem apresentá-lo como certificado ético. Também transforma lacunas em ações
verificáveis e declara limites que a documentação não consegue resolver.

## Critérios de correção

Uma resposta satisfatória deve:

- apresentar evidências e lacunas para F, A, I e R;
- distinguir condição de acesso de licença ou permissão de reutilização;
- situar CARE na soberania de dados indígenas e evitar alegação automática de
  conformidade;
- documentar as sete partes do ciclo de vida trabalhadas no datasheet;
- indicar ao menos um uso inadequado e uma responsabilidade de manutenção;
- incorporar uma revisão motivada pelo parecer da dupla.
