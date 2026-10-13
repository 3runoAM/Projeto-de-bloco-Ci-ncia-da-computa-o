from numba import jit, prange

@jit(nopython=True, parallel=True)
def conta_frequencia(array):
    frequencia = {}

    for num_i in prange(len(array)):
        num = array[num_i]
        if num not in frequencia:
            frequencia[num] = 0
        frequencia[num] += 1

    return frequencia

def exibir_frequencia(frequencia):
    for num, freq in frequencia.items():
        print(f"|\tNúmero {num} aparece {freq} vezes")

array = [1, 1, 1, 1, 1, 1, 1]
print(f"| Contando frequência dos valores no array {array}")
frequencia = conta_frequencia(array)
exibir_frequencia(frequencia)

print("----------------")
array = [1, 1, 1, 3, 1, 1, 1, 2]
print(f"| Contando frequência dos valores no array {array}")
frequencia = conta_frequencia(array)
exibir_frequencia(frequencia)

print("----------------")
array = [0,0,0,0, 2, 2, 2]
print(f"| Contando frequência dos valores no array {array}")
frequencia = conta_frequencia(array)
exibir_frequencia(frequencia)