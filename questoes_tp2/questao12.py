import time

def insertion_sort(array):
    for i in range(1, len(array)):
        elemento_selecionado = array[i]
        j = i - 1
        while j >= 0 and array[j] > elemento_selecionado:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = elemento_selecionado
    return array

def quicksort(lista):
    if len(lista) <= 1: return lista

    if len(lista) < 10: return insertion_sort(lista)

    pivo = lista[0]

    menores = []
    maiores = []
    for elemento in lista[1:]:
        if elemento < pivo:
            menores.append(elemento)
        else:
            maiores.append(elemento)

    menores_ordenados = quicksort(menores)
    maiores_ordenados = quicksort(maiores)

    return menores_ordenados + [pivo] + maiores_ordenados


array = [15, 456, 312, 6748, 546, 984, 312, 542]
# array_ordenado = [15, 312, 312, 456, 542, 546, 984, 6748]
print(f"| Ordenando lista {array} com quicksort que usa insertion sort")
comeco = time.perf_counter()
lista_ordenada = quicksort(array.copy())
fim = time.perf_counter()
print(f"| Lista ordenada em {fim - comeco} segundos\n|\t{lista_ordenada}")