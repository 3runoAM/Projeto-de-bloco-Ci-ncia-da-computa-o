import numpy as np
from numba import jit, prange

@jit(nopython=True,parallel=True)
def multiplicacao_matrizes(matriz_A, matriz_B):
    quantidade_linhas_A = matriz_A.shape[0]
    colunas_A = matriz_A.shape[1]

    quantidade_linhas_B = matriz_B.shape[0]
    colunas_B = matriz_B.shape[1]

    matriz_c = np.zeros((quantidade_linhas_A, colunas_B), dtype=np.int32)

    if colunas_A != quantidade_linhas_B:
        return matriz_c

    for i in prange(quantidade_linhas_A):
        for j in range(colunas_B):
            soma = 0
            for k in range(colunas_A):
                soma += matriz_A[i, k] * matriz_B[k, j]
            matriz_c[i, j] = soma

    return matriz_c

matriz_A = np.array([[1, 2], [4, 5]], dtype=np.int32)
matriz_B = np.array([[1, 2, 3], [4, 5, 6]], dtype=np.int32)
print(multiplicacao_matrizes(matriz_A, matriz_B))