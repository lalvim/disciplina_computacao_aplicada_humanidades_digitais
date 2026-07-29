# Revisor técnico e de acessibilidade

## Pergunta central

Os materiais são executáveis, reproduzíveis, utilizáveis e acessíveis nas
condições reais da disciplina?

## Execução

- instalar dependências em ambiente limpo;
- executar os notebooks na ordem;
- verificar caminhos relativos;
- confirmar ausência de dependências implícitas;
- testar reconstrução dos notebooks;
- executar `python3 scripts/validar_unidade_01.py`;
- verificar funcionamento offline do HTML;
- conferir correspondência entre quiz e gabarito.

## Qualidade técnica

- células executam do início ao fim;
- imports aparecem antes do uso;
- nomes são compreensíveis;
- código possui finalidade didática;
- dados fictícios estão identificados;
- mensagens e saídas não expõem caminhos sensíveis;
- arquivos gerados não divergem de sua fonte;
- instruções de instalação são suficientes.

## Acessibilidade

### Notebooks

- títulos possuem hierarquia lógica;
- tabelas possuem cabeçalhos;
- instruções não dependem apenas de cor;
- linguagem é clara;
- links têm rótulos informativos;
- saídas extensas são evitadas;
- gráficos futuros devem ter título, eixos, legenda e alternativa textual.

### HTML

- navegação funciona por teclado;
- foco é visível;
- formulários possuem rótulos;
- mensagens de correção são anunciadas;
- contraste é suficiente;
- interface responde a telas pequenas;
- animação reduzida é respeitada;
- conteúdo permanece legível sem JavaScript, ou a dependência é informada;
- não há recursos externos necessários.

## Segurança e privacidade

- não há coleta de dados do estudante;
- não há envio para serviços externos;
- o material explica que respostas do HTML não são secretas;
- dados reais futuros não expõem informações pessoais desnecessárias;
- conteúdo de gabarito não é confundido com controle de acesso.

## Perguntas obrigatórias

1. Um estudante consegue começar apenas com o README?
2. O material funciona em ambiente limpo?
3. O quiz é utilizável apenas com teclado?
4. Há barreiras para leitores de tela ou baixa visão?
5. Existe dependência de internet não declarada?
6. A reconstrução preserva alterações manuais?
7. Os dados e resultados são reproduzíveis?

## Entrega

Usar `modelo_de_parecer.md` e incluir:

- ambiente testado;
- comandos executados;
- resultados;
- barreiras de acessibilidade;
- achados por gravidade;
- decisão.

