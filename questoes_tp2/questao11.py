def quicksort(lista):
    if len(lista) <= 1: return lista

    pivo_a = lista[0]
    pivo_b = lista[-1]

    if pivo_a > pivo_b:
        pivo_a = lista[-1]
        pivo_b = lista[0]

    menores_a = []
    entre_a_b = []
    maiores_b = []
    for elemento in lista[1:-1]:
        if elemento < pivo_a:
            menores_a.append(elemento)
        elif pivo_a <= elemento <= pivo_b:
            entre_a_b.append(elemento)
        else:
            maiores_b.append(elemento)

    menores_ordenados = quicksort(menores_a)
    entre_ordenados = quicksort(entre_a_b)
    maiores_ordenados = quicksort(maiores_b)

    return menores_ordenados + [pivo_a] + entre_ordenados + [pivo_b] + maiores_ordenados

lista_a = [213, 7456, 49, 63, 4, 512, 34, 561, 23, 1, 756, 8, 123, 456, 453, 453, 789, 9]
# lista_ordenada = [1, 4, 8, 9, 23, 34, 49, 63, 123, 213, 453, 453, 456, 512, 561, 756, 789, 7456]
print(quicksort(lista_a))

#lista_ordenada = [2, 14, 31, 31, 45, 54, 64, 78, 317, 6758]
lista_b = [14, 64, 54, 6758, 31, 31, 317, 2, 78, 45]
print(quicksort(lista_b))
