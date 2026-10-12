import time

from numba import jit, prange

def soma_numeros(lista_numeros):
    soma = 0
    for i in range(0, len(lista_numeros)):
        soma += lista_numeros[i]
    return soma

@jit(nopython=True, parallel=True)
def soma_numeros_paralelo(lista_numeros):
    soma = 0
    for i in prange(0, len(lista_numeros)):
        soma += lista_numeros[i]
    return soma


lista_numeros = [213, 7456, 49, 63, 4, 512, 34, 561, 23, 1, 756, 8, 123, 456, 453, 453, 789, 9]

inicio = time.perf_counter()
soma = soma_numeros(lista_numeros)
fim = time.perf_counter()
print(f"| Função sequencial somou os números da lista em {fim - inicio} segundos, deu {soma}")
print("|---")
inicio = time.perf_counter()
soma = soma_numeros_paralelo(lista_numeros)
fim = time.perf_counter()
print(f"| Função paralela somou os números da lista em {fim - inicio} segundos, deu {soma}")