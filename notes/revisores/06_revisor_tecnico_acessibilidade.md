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
- verificar legibilidade e navegação dos exercícios textuais;
- conferir correspondência entre exercícios e gabarito.

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

### Exercícios textuais

- títulos e questões possuem hierarquia lógica;
- alternativas não dependem apenas de cor ou posição;
- o arquivo permanece legível em tela pequena e por leitor de tela;
- não há recursos externos necessários.

## Segurança e privacidade

- não há coleta de dados do estudante;
- não há envio para serviços externos;
- o material explica que a pasta de gabaritos não constitui controle de acesso;
- dados reais futuros não expõem informações pessoais desnecessárias;
- conteúdo de gabarito não é confundido com controle de acesso.

## Perguntas obrigatórias

1. Um estudante consegue começar apenas com o README?
2. O material funciona em ambiente limpo?
3. Os exercícios são navegáveis por teclado e leitor de tela?
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
