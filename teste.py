import numpy as np

# Configura uma semente para garantir que o resultado seja o mesmo
np.random.seed(42)

# Simula uma matriz de 500x500 pixels
# Os valores variam de 0 a 255 (representando a intensidade do pixel)
imagem_satelite = np.random.randint(0, 256, size=(500, 500))

# Simula uma "nuvem" artificial (região com alta refletividade, valores > 240)
imagem_satelite[100:200, 150:250] = np.random.randint(240, 256, size=(100, 100))

print("Matriz da imagem gerada com sucesso!")