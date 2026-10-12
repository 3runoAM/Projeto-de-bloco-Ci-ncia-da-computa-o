import time

def soma_entre(lista, inicio, fim):
    if inicio == fim: return lista[inicio]

    total = 0
    comeco = time.perf_counter()
    for i in range(inicio, fim):
        chave = (total, lista[i])

        if chave not in memo:
            memo[chave] = total + lista[i]

        total = memo[chave]

    fim = time.perf_counter()
    print(f"|\tTempo de execução: {fim - comeco} segundos")
    return total


memo = {}
lista = [2, 8, 9, 7, 4, 6, 1, 5, 3]
print(f"| Somando pela primeira vez e construíndo o memo")
total = soma_entre(lista, 0, len(lista))
print(f"| Total: {total}")
print("| ----")
print(f"| Somando pela segunda vez usando o memo")
total = soma_entre(lista, 0, len(lista))
print(f"| Total: {total}")
