def particao(array, esquerda, direita):
    pivo = array[direita]
    indice = esquerda - 1

    for i in range(esquerda, direita):
        if array[i] <= pivo:
            indice += 1
            array[i], array[indice] = array[indice], array[i]

    array[indice + 1], array[direita] = array[direita], array[indice + 1]
    return indice + 1

def quickselect(array, esquerda, direita, k):
    k-=1
    if esquerda <= direita:
        pivo_index = particao(array, esquerda, direita)
        if pivo_index == k:
            return array[pivo_index]
        elif pivo_index > k:
            return quickselect(array, esquerda, pivo_index - 1, k+1)
        else:
            return quickselect(array, pivo_index + 1, direita, k+1)

    return None

array = [15, 456, 312, 6748, 546, 984, 312, 542]
# array_ordenado = [15, 312, 312, 456, 542, 546, 984, 6748]
k = 5
print(f"| Procurando pelo {k} elemento no array")
k_esimo_elemento = quickselect(array.copy(), 0, len(array)-1, k)
print(f"| Elemento: {k_esimo_elemento}\n")
print("--------")
k = 8
print(f"| Procurando pelo {k} elemento no array")
k_esimo_elemento = quickselect(array.copy(), 0, len(array)-1, k)
print(f"| Elemento: {k_esimo_elemento}")