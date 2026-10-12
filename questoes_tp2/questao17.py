def binary_search(lista, num_procurado, inicio=None, fim=None):
    if fim is None:
        fim = len(lista) - 1
    if inicio is None:
        inicio = 0

    if inicio > fim:
        return -1

    meio = (inicio + fim) // 2

    if lista[meio] == num_procurado:
        return meio
    elif lista[meio] < num_procurado:
        return binary_search(lista, num_procurado, meio + 1, fim)
    else:
        return binary_search(lista, num_procurado, inicio, meio - 1)

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]

print(binary_search(lista, 0))
print(binary_search(lista, 1))
print(binary_search(lista, 10))
print(binary_search(lista, 17))