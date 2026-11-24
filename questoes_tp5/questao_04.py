def mochila(itens, capacidade):
    ordenados = sorted(itens, key=lambda x: x[2] / x[1], reverse=True)

    print(ordenados)
    escolhidos = []
    peso_total = 0
    valor_total = 0

    for nome, peso, valor in ordenados:
        if peso_total + peso <= capacidade:
            escolhidos.append(nome)
            peso_total += peso
            valor_total += valor

    return valor_total, peso_total, escolhidos


itens = [
    # NOME DO ITEM, PESO DO ITEM, VALOR DO ITEM
    ("Notebook", 10, 60),
    ("Livro", 20, 100),
    ("Monitor", 30, 120),
    ("Compras", 40, 150)
]

print(mochila(itens, 50))