"""
Desafio Prático — Análise de Imagem de Satélite Simulada
Processo Seletivo — Bolsa IC: Eventos Climáticos e Desastres no RS

Autor: Luiz Carlos da Silva Junior
Data: Junho/2026
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Configura uma semente para garantir que o resultado seja o mesmo
np.random.seed(42)

# Simula uma matriz de 500x500 pixels
# Os valores variam de 0 a 255 (representando a intensidade do pixel)
imagem_satelite = np.random.randint(0, 256, size=(500, 500))

# Simula uma "nuvem" artificial (região com alta refletividade, valores > 240)
imagem_satelite[100:200, 150:250] = np.random.randint(240, 256, size=(100, 100))

print("Matriz da imagem gerada com sucesso!")

def dimensoes_e_tipo(imagem):
    """
    Imprime o tamanho total da imagem (linhas e colunas) e o tipo de dado dos pixels.
    """
    linhas, colunas = imagem.shape
    print(f"\nDimensões da imagem: {linhas} linhas x {colunas} colunas")
    print(f"Tipo de dado dos pixels (dtype): {imagem.dtype}")
    return linhas, colunas, imagem.dtype


def filtro_mascara_nuvens(imagem, limiar=240):
    """
    Conta quantos pixels possuem valor >= limiar (nuvem simulada) e calcula
    a porcentagem que essa "nuvem" ocupa em relação ao total da imagem.
    """
    mascara_nuvens = imagem >= limiar
    qtd_pixels_nuvem = np.sum(mascara_nuvens)
    total_pixels = imagem.size
    percentual_nuvem = (qtd_pixels_nuvem / total_pixels) * 100

    print(f"\nQuantidade de pixels com nuvem (valor >= {limiar}): {qtd_pixels_nuvem}")
    print(f"Percentual de nuvem na imagem: {percentual_nuvem:.2f}%")
    return qtd_pixels_nuvem, percentual_nuvem


def estatistica_regiao_interesse(imagem, linha_inicio=200, linha_fim=300,
                                  coluna_inicio=200, coluna_fim=300):
    """
    Extrai a região de interesse (ROI) da matriz, representando Porto Alegre,
    e calcula o valor médio, máximo e mínimo dos pixels nessa região.
    """
    regiao = imagem[linha_inicio:linha_fim, coluna_inicio:coluna_fim]

    media = np.mean(regiao)
    valor_max = np.max(regiao)
    valor_min = np.min(regiao)

    print(f"\nEstatísticas da Região de Interesse (Porto Alegre) "
          f"[{linha_inicio}:{linha_fim}, {coluna_inicio}:{coluna_fim}]:")
    print(f"Valor médio dos pixels: {media:.2f}")
    print(f"Valor máximo: {valor_max}")
    print(f"Valor mínimo: {valor_min}")
    return media, valor_max, valor_min


def visualizar_imagem(imagem, limiar=240,
                       linha_inicio=200, linha_fim=300,
                       coluna_inicio=200, coluna_fim=300,
                       salvar_em="visualizacao_imagem_satelite.png"):
    """
    Gera uma figura com três painéis:
    1. Imagem original (escala de cinza).
    2. Máscara de nuvens (pixels >= limiar).
    3. Imagem original com a região de interesse (ROI) destacada.
    """
    mascara_nuvens = imagem >= limiar

    fig, eixos = plt.subplots(1, 3, figsize=(15, 5))

    # Painel 1: imagem original
    eixos[0].imshow(imagem, cmap="gray", vmin=0, vmax=255)
    eixos[0].set_title("Imagem de satélite simulada")
    eixos[0].axis("off")

    # Painel 2: máscara de nuvens
    eixos[1].imshow(mascara_nuvens, cmap="gray")
    eixos[1].set_title(f"Máscara de nuvens (>= {limiar})")
    eixos[1].axis("off")

    # Painel 3: imagem original com a ROI destacada
    eixos[2].imshow(imagem, cmap="gray", vmin=0, vmax=255)
    largura_roi = coluna_fim - coluna_inicio
    altura_roi = linha_fim - linha_inicio
    retangulo = patches.Rectangle(
        (coluna_inicio, linha_inicio), largura_roi, altura_roi,
        linewidth=2, edgecolor="red", facecolor="none"
    )
    eixos[2].add_patch(retangulo)
    eixos[2].set_title("ROI - Porto Alegre")
    eixos[2].axis("off")

    plt.tight_layout()
    plt.savefig(salvar_em, dpi=150)
    print(f"\nVisualização salva em: {salvar_em}")
    plt.show()


if __name__ == "__main__":
    dimensoes_e_tipo(imagem_satelite)
    filtro_mascara_nuvens(imagem_satelite)
    estatistica_regiao_interesse(imagem_satelite)
    visualizar_imagem(imagem_satelite)
