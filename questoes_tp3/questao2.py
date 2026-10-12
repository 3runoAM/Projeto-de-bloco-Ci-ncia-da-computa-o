import time

from numba import jit, prange
import numpy as np

def gerar_matriz_imagem(altura, largura):
    return np.random.randint(0, 256, size=(altura, largura), dtype=np.uint8)

def inverter_escala_sequencial(matriz):
    altura, largura = matriz.shape

    matriz_retorno = np.empty_like(matriz)
    for i in range(altura):
        for j in range(largura):
            matriz_retorno[i, j] = 255 - matriz[i, j]
    return matriz_retorno


@jit(nopython=True, parallel=True)
def inverter_escala_paralela(matriz):
    altura, largura = matriz.shape

    matriz_retorno = np.empty_like(matriz)
    for i in prange(altura):
        for j in range(largura):
            matriz_retorno[i, j] = 255 - matriz[i, j]

    return matriz_retorno


matriz_500_x_500 = gerar_matriz_imagem(500, 500)
matriz_2000_x_2000 = gerar_matriz_imagem(2000, 2000)

print("| Invertendo escala de cinza com paralelismo")
print("|\tMatriz 500x500")
print(f"| Matriz antes da inversão (linha 1) {matriz_500_x_500[0]}")
comeco = time.perf_counter()
matriz = inverter_escala_paralela(matriz_500_x_500)
fim = time.perf_counter()
print(f"| Matriz após inversão (linha 1) {matriz[0]}")
print(f"| Matriz de 500x500 invertida com paralelismo em {fim - comeco} segundos")
print("---")
print("|\tMatriz 2000x2000")
print(f"| Matriz antes da inversão (linha 1) {matriz_2000_x_2000[0]}")
comeco = time.perf_counter()
matriz = inverter_escala_paralela(matriz_2000_x_2000)
fim = time.perf_counter()
print(f"| Matriz após inversão (linha 1) {matriz[0]}")
print(f"| Matriz de 2000x2000 invertida com paralelismo em {fim - comeco} segundos")

print("------------------")
print("| Invertendo escala de cinza com sequencial")
print("|\tMatriz 2000x2000 (linha 1)")
print(f"| Matriz antes da inversão (linha 1) {matriz_500_x_500[0]}")
comeco = time.perf_counter()
matriz = inverter_escala_paralela(matriz_500_x_500)
fim = time.perf_counter()
print(f"| Matriz após inversão (linha 1) {matriz[0]}")
print(f"| Matriz de 500x500 invertida sequencialmente em {fim - comeco} segundos")
print("---")
print("|\tMatriz 2000x2000")
print(f"| Matriz antes da inversão (linha 1) {matriz_2000_x_2000[0]}")
comeco = time.perf_counter()
matriz = inverter_escala_paralela(matriz_2000_x_2000)
fim = time.perf_counter()
print(f"| Matriz após inversão (linha 1) {matriz[0]}")
print(f"| Matriz de 2000x2000 invertida sequencialmente em {fim - comeco} segundos")
