def soma_n_recursivo(lista, n, soma=0):
    if n > len(lista):
        return None

    if n == 0:
        return soma

    soma += lista[n-1]
    return soma_n_recursivo(lista, n-1, soma)

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(soma_n_recursivo(lista, 3))
print(soma_n_recursivo(lista, 10))
print(soma_n_recursivo(lista, 15))