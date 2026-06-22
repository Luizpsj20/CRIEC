# Desafio Prático — Análise de Imagem de Satélite Simulada

Este repositório contém a resposta ao desafio prático de programação do processo seletivo
para a Bolsa de Iniciação Científica no projeto **"Eventos Climáticos e Desastres no RS:
Caracterização e Predição com Inteligência Artificial"**.

## Objetivo

A partir de uma matriz simulando uma imagem de satélite (500x500 pixels, valores de 0 a 255),
o script realiza três análises:

1. **Dimensões e tipo de dado** da imagem.
2. **Filtro de máscara de nuvens**: conta e calcula o percentual de pixels considerados
   "nuvem" (valor ≥ 240).
3. **Estatística de uma região de interesse (ROI)**: extrai o subquadrado central
   (linhas 200–300, colunas 200–300), representando Porto Alegre, e calcula média,
   valor máximo e valor mínimo dos pixels nessa região.

## Requisitos

- Python 3.8+
- NumPy
- Matplotlib (apenas para a visualização opcional)

Instalação das dependências:

```bash
pip install numpy matplotlib
```

## Como executar

```bash
python desafio_imagem_satelite.py
```

## Estrutura do código

| Função | Descrição |
|---|---|
| `dimensoes_e_tipo(imagem)` | Imprime o número de linhas/colunas e o `dtype` dos pixels. |
| `filtro_mascara_nuvens(imagem, limiar=240)` | Conta pixels acima do limiar e calcula o percentual de "nuvem" na imagem. |
| `estatistica_regiao_interesse(imagem, ...)` | Extrai a ROI e calcula média, máximo e mínimo dos pixels. |
| `visualizar_imagem(imagem, ...)` *(bônus)* | Gera e salva uma figura com a imagem original, a máscara de nuvens e a ROI destacada. |

A geração da matriz (bloco fornecido no enunciado) é mantida intacta no início do arquivo,
garantindo reprodutibilidade via `np.random.seed(42)`.

## Exemplo de saída

```
Matriz da imagem gerada com sucesso!

Dimensões da imagem: 500 linhas x 500 colunas
Tipo de dado dos pixels (dtype): int64

Quantidade de pixels com nuvem (valor >= 240): 24866
Percentual de nuvem na imagem: 9.95%

Estatísticas da Região de Interesse (Porto Alegre) [200:300, 200:300]:
Valor médio dos pixels: 125.58
Valor máximo: 255
Valor mínimo: 0
```

> **Observação:** o percentual de nuvem (≈9,95%) é maior do que o esperado apenas pelo
> bloco artificial inserido no enunciado (que corresponde a 4% da imagem). Isso ocorre
> porque a imagem de fundo é totalmente aleatória entre 0 e 255, então uma fração dos
> pixels fora do bloco simulado também ultrapassa o limiar de 240 por acaso
> (estatisticamente, ~6,25% dos pixels aleatórios devem cair nessa faixa).

## Autor

Respondido como parte do processo seletivo para a vaga de Iniciação Científica.
