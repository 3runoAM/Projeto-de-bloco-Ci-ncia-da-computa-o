def busca_binaria(lista, alvo, inicio=None, fim=None):
    if inicio is None:
        inicio = 0
    if fim is None:
        fim = len(lista) - 1

    while inicio <= fim:
        meio = (inicio + fim) // 2

        if lista[meio] == alvo:
            return meio
        elif lista[meio] < alvo:
            inicio = meio + 1
        else:
            fim = meio - 1

    return -1

def binary_search_recursiva(lista, num_procurado, d, inicio=None, fim=None, profundidade=0):
    if inicio is None:
        inicio = 0
    if fim is None:
        fim = len(lista) - 1

    if profundidade == d:
        return busca_binaria(lista, num_procurado, inicio, fim)

    if inicio > fim:
        return -1

    meio = (inicio + fim) // 2

    if lista[meio] == num_procurado:
        return meio
    elif lista[meio] < num_procurado:
        return binary_search_recursiva(lista, num_procurado, d, meio + 1, fim, profundidade + 1)
    else:
        return binary_search_recursiva(lista, num_procurado, d, inicio, meio - 1, profundidade + 1)


profundidade = 0
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]
print(binary_search_recursiva(lista, 0, 3))
print(binary_search_recursiva(lista, 1, 3))
print(binary_search_recursiva(lista, 10, 3))
print(binary_search_recursiva(lista, 17, 3))