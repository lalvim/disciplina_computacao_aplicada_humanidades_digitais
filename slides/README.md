# Slides da disciplina

Esta pasta reúne as apresentações em Markdown da disciplina **Computação
Aplicada a Problemas em Humanidades Digitais**. A organização segue as
[diretrizes editoriais](../notes/diretrizes_slides.md) e o
[plano das unidades](../notes/plano_slides_unidades_01_a_14.md).

## Formato

Os arquivos usam a sintaxe do Marp:

- o bloco YAML inicial define tema, paginação e renderização matemática;
- `---` separa os slides;
- fórmulas são escritas em LaTeX e renderizadas com KaTeX;
- comentários HTML contêm notas de condução para a pessoa docente;
- imagens são referenciadas por caminhos relativos e permanecem no diretório
  da unidade que documenta sua autoria, licença e texto alternativo.

O tema comum está em [`tema.css`](tema.css). Não mova uma apresentação sem
ajustar seus caminhos relativos para as imagens.

## Visualização

Editores com suporte a Marp permitem visualizar o arquivo diretamente. Com a
CLI do Marp disponível no ambiente, a partir da raiz do repositório, inicie o
servidor de visualização:

```bash
npx @marp-team/marp-cli --server --theme-set slides/tema.css slides
```

O comando abre um servidor local e atualiza a apresentação durante a edição.

## Exportação

Gerar HTML:

```bash
npx @marp-team/marp-cli --theme-set slides/tema.css --html \
  --output slides/unidade_01.html slides/unidade_01.md
```

Gerar PDF requer um navegador compatível instalado no ambiente:

```bash
npx @marp-team/marp-cli --theme-set slides/tema.css \
  --pdf --output slides/unidade_01.pdf slides/unidade_01.md
```

Os arquivos exportados não são fonte de edição. Corrija sempre o Markdown e
gere novamente a saída.

## Convenções didáticas

Cada apresentação começa com um exemplo ou uma situação-problema antes da
agenda e da teoria. Os slides marcados como atividade informam modalidade,
tempo e produto. A implementação completa dos experimentos permanece nos
notebooks; os slides mostram apenas a entrada, a operação essencial, a saída e
sua interpretação.

Antes de usar em aula, confira:

1. a renderização das fórmulas;
2. a disponibilidade das imagens;
3. a legibilidade em projeção;
4. os links para notebooks e referências;
5. o tempo reservado às atividades.

## Apresentações disponíveis

| Unidade | Tema | Arquivo |
|---|---|---|
| 1 | Questões das Humanidades e problemas computacionais | [`unidade_01.md`](unidade_01.md) |
| 2 | Construção e documentação da base | [`unidade_02.md`](unidade_02.md) |
| 3 | Transformação de fontes em dados analisáveis | [`unidade_03.md`](unidade_03.md) |
| 4 | Exploração quantitativa, textual e visual | [`unidade_04.md`](unidade_04.md) |
| 5 | Comparação quantitativa e textual | [`unidade_05.md`](unidade_05.md) |
| 6 | Associações e grafos | [`unidade_06.md`](unidade_06.md) |
| 7 | Modelos de associação condicionada | [`unidade_07.md`](unidade_07.md) |
| 8 | Classificação supervisionada | [`unidade_08.md`](unidade_08.md) |
| 9 | Agrupamentos e temas | [`unidade_09.md`](unidade_09.md) |
| 10 | Extração estruturada de textos | [`unidade_10.md`](unidade_10.md) |
| 11 | Tempo e espaço | [`unidade_11.md`](unidade_11.md) |
| 12 | Modelos de linguagem responsáveis | [`unidade_12.md`](unidade_12.md) |

As demais unidades serão acrescentadas conforme as etapas definidas no plano.

