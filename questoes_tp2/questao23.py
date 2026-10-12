import time

from numba import prange
from numba.core.decorators import jit


@jit(nopython=True, parallel=True)
def busca_linear_paralela(lista, num):
    menor_indice = len(lista) + 1

    for i in prange(len(lista)):
        if lista[i] == num:
            menor_indice = min(menor_indice, i)

    if menor_indice != len(lista) + 1:
        return menor_indice

    return None

def busca_linear(lista, num):
    if len(lista) >= 10000:
        return busca_linear_paralela(lista, num)

    for i in range(len(lista)):
        if lista[i] == num:
            return i
    return None


array_A = [i for i in range(10000)]
print(f"| Fazendo busca linear com paralelismo pelo número 9999 em lista de tamanho muito grande, 10k")
inicio = time.perf_counter()
numero_encontrado = busca_linear(array_A, 9999)
fim = time.perf_counter()
print(f"| Número {numero_encontrado} foi encontrado no tempo de {fim - inicio} segundos em um array de tamanho 10k")

array_B = [416, 123, 65745, 123, 4156, 475, 63, 45, 64, 563, 4563, 435, 453, 78563, 432, 375, 63745, 7635, 735, 3745]
print(f"| Fazendo busca linear sequencial em lista com um tamanho pequeno, 20")
inicio = time.perf_counter()
numero_encontrado = busca_linear(array_B, 3745)
fim = time.perf_counter()
print(f"| Número {numero_encontrado} foi encontrado no tempo de {fim - inicio} segundos em um array de tamanho 20")