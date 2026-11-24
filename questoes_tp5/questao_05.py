import time

def mochila(itens, capacidade):
    ordenados = sorted(itens, key=lambda x: x[2] / x[1], reverse=True)

    escolhidos = []
    peso_total = 0
    valor_total = 0

    for nome, peso, valor in ordenados:
        if peso_total + peso <= capacidade:
            escolhidos.append(nome)
            peso_total += peso
            valor_total += valor

    return valor_total, peso_total, escolhidos


def mochila_recursiva(itens, capacidade_restante, indice_item=0):
    if capacidade_restante < 0: return -1, []
    if indice_item == len(itens): return 0, []

    nome, peso, valor = itens[indice_item]
    valor_sem, escolhidos_sem = mochila_recursiva(itens, capacidade_restante, indice_item + 1)
    valor_com, escolhidos_com = mochila_recursiva(itens, capacidade_restante - peso, indice_item + 1)

    if valor_com != -1: valor_com += valor

    if valor_com > valor_sem:
        return valor_com, [nome] + escolhidos_com
    return valor_sem, escolhidos_sem


itens = [
    # | NOME, PESO DO ITEM, VALOR DO ITEM
    ("Notebook", 10, 60),
    ("Livro", 20, 100),
    ("Monitor", 30, 120),
    ("Compras", 40, 150)
]
capacidade = 50

inicio = time.perf_counter()
mochila_gulosa = mochila(itens, capacidade)
fim = time.perf_counter()
print(f"| Mochila gulosa com itens {itens} e capacidade {capacidade} ")
print(f"| Tempo execução {fim - inicio} segundos")

inicio = time.perf_counter()
mochila_recursiva = mochila_recursiva(itens, capacidade)
fim = time.perf_counter()
print(f"| Mochila recursiva com itens {itens} e capacidade {capacidade} ")
print(f"| Tempo execução {fim - inicio} segundos")