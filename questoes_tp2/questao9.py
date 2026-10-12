def mediana_de_tres(lista, esquerda, direita):
    meio = (esquerda + direita) // 2

    if lista[meio] < lista[esquerda]:
        lista[esquerda], lista[meio] = lista[meio], lista[esquerda]
    if lista[direita] < lista[esquerda]:
        lista[esquerda], lista[direita] = lista[direita], lista[esquerda]
    if lista[direita] < lista[meio]:
        lista[meio], lista[direita] = lista[direita], lista[meio]

    lista[meio], lista[direita] = lista[direita], lista[meio]
    return lista[direita]

def particao(array, esquerda, direita, count_pivo):
    if count_pivo > 3 and (direita - esquerda + 1) > 3:
        mediana_de_tres(array, esquerda, direita)

    pivo = array[direita]
    indice = esquerda - 1

    for i in range(esquerda, direita):
        if array[i] <= pivo:
            indice += 1
            array[i], array[indice] = array[indice], array[i]

    array[indice + 1], array[direita] = array[direita], array[indice + 1]
    return indice + 1

def quickselect(array, esquerda, direita, k, count_pivo=0):
    k-=1
    if esquerda <= direita:
        count_pivo += 1
        pivo_index = particao(array, esquerda, direita, count_pivo)
        if pivo_index == k:
            return array[pivo_index]
        elif pivo_index > k:
            return quickselect(array, esquerda, pivo_index - 1, k+1, count_pivo)
        else:
            return quickselect(array, pivo_index + 1, direita, k+1, count_pivo)

    return None

lista_numeros = [213, 7456, 49, 63, 4, 512, 34, 561, 23, 1, 756, 8, 123, 456, 453, 453, 789, 9]
# lista_ordenada = [1, 4, 8, 9, 23, 34, 49, 63, 123, 213, 453, 453, 456, 512, 561, 756, 789, 7456]
k = 5
print(f"| Procurando pelo {k} elemento na lista {lista_numeros}")
print(f"| O {k} menor elemento é: {quickselect(lista_numeros, 0, len(lista_numeros) - 1, k)}")
k = 10
print(f"| Procurando pelo {k} elemento na lista {lista_numeros}")
print(f"| O {k} menor elemento é: {quickselect(lista_numeros, 0, len(lista_numeros) - 1, k)}")
k = 18
print(f"| Procurando pelo {k} elemento na lista {lista_numeros}")
print(f"| O {k} menor elemento é: {quickselect(lista_numeros, 0, len(lista_numeros) - 1, k)}")