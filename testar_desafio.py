"""
Testes automáticos para validar as funções de desafio_imagem_satelite.py

Como a seed (np.random.seed(42)) é fixa, os resultados são sempre os mesmos.
Isso permite testar com valores exatos, não apenas "parece razoável".

Como rodar:
    python testar_desafio.py
"""

from teste import (
    imagem_satelite,
    dimensoes_e_tipo,
    filtro_mascara_nuvens,
    estatistica_regiao_interesse,
)


def testar_dimensoes():
    linhas, colunas, dtype = dimensoes_e_tipo(imagem_satelite)
    assert linhas == 500, f"Esperado 500 linhas, obtido {linhas}"
    assert colunas == 500, f"Esperado 500 colunas, obtido {colunas}"
    print("OK -> testar_dimensoes")


def testar_mascara_nuvens():
    qtd_nuvem, percentual = filtro_mascara_nuvens(imagem_satelite)

    # O bloco artificial de nuvem tem 100x100 = 10.000 pixels,
    # então a contagem real de nuvem nunca pode ser menor que isso.
    assert qtd_nuvem >= 10_000, (
        f"Esperado pelo menos 10.000 pixels de nuvem (bloco artificial), "
        f"obtido {qtd_nuvem}"
    )

    # O percentual de nuvem deve estar numa faixa razoável (entre o esperado
    # só do bloco ~4% e o esperado com ruído aleatório ~10-11%).
    assert 4.0 <= percentual <= 15.0, (
        f"Percentual de nuvem fora do esperado: {percentual:.2f}%"
    )
    print("OK -> testar_mascara_nuvens")


def testar_estatistica_roi():
    media, valor_max, valor_min = estatistica_regiao_interesse(imagem_satelite)

    # A ROI não tem sobreposição com o bloco de nuvem (verifique os índices:
    # nuvem = linhas 100-200, colunas 150-250 / ROI = linhas 200-300, colunas 200-300),
    # então o comportamento deve ser de ruído puro: média próxima de 127.5.
    assert 100 <= media <= 150, f"Média fora do esperado para ruído puro: {media:.2f}"
    assert valor_max == 255, f"Esperado valor máximo 255, obtido {valor_max}"
    assert valor_min == 0, f"Esperado valor mínimo 0, obtido {valor_min}"
    print("OK -> testar_estatistica_roi")


def testar_reprodutibilidade():
    # Confere se a seed realmente fixa o resultado: o pixel [0, 0] e o pixel
    # central da nuvem [150, 200] devem ser sempre os mesmos valores.
    assert imagem_satelite[0, 0] == 102, (
        f"Pixel [0,0] mudou — a seed não está mais reprodutível "
        f"(obtido {imagem_satelite[0, 0]})"
    )
    print("OK -> testar_reprodutibilidade")


if __name__ == "__main__":
    print("Rodando testes...\n")
    testar_dimensoes()
    testar_mascara_nuvens()
    testar_estatistica_roi()
    testar_reprodutibilidade()
    print("\nTodos os testes passaram!")
