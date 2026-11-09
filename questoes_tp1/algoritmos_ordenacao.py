import time

def selection_sort(array):
    for limite_organizado in range(len(array)):
        index_menor_valor = limite_organizado
        for index_scanner in range(limite_organizado, len(array)):
            if array[index_scanner] < array[index_menor_valor]:
                index_menor_valor = index_scanner

        if array[index_menor_valor] < array[limite_organizado]:
            array[limite_organizado], array[index_menor_valor] = array[index_menor_valor], array[limite_organizado]
    return array

def insertion_sort(array):
    for index_a_organizar in range(1, len(array)):
        elemento_a_organizar = array[index_a_organizar]
        index_elemento_organizado = index_a_organizar - 1
        while (index_elemento_organizado >= 0) and elemento_a_organizar < array[index_elemento_organizado]:
            array[index_elemento_organizado + 1] = array[index_elemento_organizado]
            index_elemento_organizado -= 1
        array[index_elemento_organizado + 1] = elemento_a_organizar
    return array

def bubble_sort(array):
    tamanho_array = len(array)
    for index in range(tamanho_array):
        for inner in range(0, tamanho_array - index - 1):
            elemento_atual = array[inner]
            prox_elemento = array[inner + 1]
            if elemento_atual > prox_elemento:
                array[inner], array[inner + 1] = array[inner + 1], array[inner]
    return array

with open("listagem_arquivos.txt", "r") as arquivo:
    lista_original = [int(string_num.replace("arquivo", "")) for string_num in arquivo]

    lista_bubble = lista_original.copy()

    tempoComecoBubble = time.perf_counter()
    lista_ordenada_bubble = bubble_sort(lista_bubble)
    tempoFimBubble = time.perf_counter()

    tempoBubble = tempoFimBubble - tempoComecoBubble
    print(
        f"Tempo do bubble: {tempoBubble} segundos\nLista original: {lista_original}\nLista ordenada: {lista_ordenada_bubble}")

    lista_insertion = lista_original.copy()

    tempoComecoInsertion = time.perf_counter()
    lista_ordenada_insertion = insertion_sort(lista_insertion)
    tempoFimInsertion = time.perf_counter()

    tempoInsertion = tempoFimInsertion - tempoComecoInsertion
    print(
        f"Tempo do insertion: {tempoInsertion} segundos\nLista original: {lista_original}\nLista ordenada: {lista_ordenada_insertion}")

    lista_selection = lista_original.copy()
    tempoComecoSelection = time.perf_counter()
    lista_ordenada_selection = selection_sort(lista_selection)
    tempoFimSelection = time.perf_counter()

    tempoSelection = tempoFimSelection - tempoComecoSelection
    print(
        f"Tempo do selection: {tempoSelection} segundos\nLista original: {lista_original}\nLista ordenada: {lista_ordenada_selection}")
