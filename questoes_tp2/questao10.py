import time

def mediana_de_tres(lista, esquerda, direita):
    if len(lista) <= 3: return lista[0]

    indice_meio = (esquerda + direita) // 2
    comeco = lista[esquerda]
    meio = lista[indice_meio]
    fim = lista[direita]

    if meio < comeco:
        lista[esquerda], lista[indice_meio] = lista[indice_meio], lista[esquerda]
    if fim < comeco:
        lista[direita], lista[esquerda] = lista[esquerda], lista[direita]
    if fim < meio:
        lista[indice_meio], lista[direita] = lista[direita], lista[indice_meio]

    lista[esquerda], lista[indice_meio] = lista[indice_meio], lista[esquerda]

    return lista[esquerda]

def quicksort_mediana(lista, esquerda, direita):
    if len(lista) <= 1: return lista

    pivo = mediana_de_tres(lista, esquerda, direita)

    menores = []
    maiores = []
    for elemento in lista[1:]:
        if elemento < pivo:
            menores.append(elemento)
        else:
            maiores.append(elemento)

    menores_ordenados = quicksort_mediana(menores, 0, len(menores) - 1)
    maiores_ordenados = quicksort_mediana(maiores, 0, len(maiores) - 1)

    return menores_ordenados + [pivo] + maiores_ordenados

def quicksort(lista):
    if len(lista) <= 1: return lista

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

print(f"| Ordenando lista {array} com quicksort com mediana de três")
comeco = time.perf_counter()
lista_ordenada = quicksort_mediana(array.copy(), 0, len(array) - 1)
fim = time.perf_counter()
print(f"| Lista ordenada em {fim - comeco} segundos\n|\t{lista_ordenada}")
print("--------")
print(f"| Ordenando lista {array} com quicksort simples")
comeco = time.perf_counter()
lista_ordenada = quicksort(array.copy())
fim = time.perf_counter()
print(f"| Lista ordenada em {fim - comeco} segundos\n|\t{lista_ordenada}")
