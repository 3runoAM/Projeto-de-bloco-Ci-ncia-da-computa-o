import time
import tracemalloc

class Pilha:
    def __init__(self, tamanho_maximo=5):
        self.items = []
        self._tamanho_max = tamanho_maximo

    def adicionar(self, item):
        if len(self.items) < self._tamanho_max:
            self.items.insert(0, item)
            return

    def remover(self):
        if len(self.items) > 0:
            return self.items.pop(0)

    def mostrar_pilha_join(self):
        print(f"PILHA: {', '.join(self.items)}\n")


class Fila:
    def __init__(self):
        self.fila = []

    def adicionar(self, item):
        self.fila.append(item)

    def remover(self):
        return self.fila.pop(0)

    def mostrar_fila(self):
        print(f"FILA: {self.fila}\n")


class HashTable:
    def __init__(self):
        self.hash_table = {}

    def adicionar(self, item):
        chave = f"{hash(item)}"
        if chave in self.hash_table:
            print("Valor já existe na tabela")
            return
        self.hash_table[chave] = item

    def procurar_por_item(self, item):
        chave = f"{hash(item)}"
        if chave in self.hash_table:
            item = self.hash_table[chave]
            print(f"Retornando {item} correspondente a chave {chave} da tabela")
            return item
        print(f"'{item}' não encontrado na tabela")
        return False

    def remover(self, item):
        chave = f"{hash(item)}"
        if chave in self.hash_table:
            del self.hash_table[chave]
            return
        print(f"'{item}' não encontrado na tabela")
        return False

    def mostrar_tabela(self):
        print(f"HASH TABLE: {self.hash_table}\n")


def montar_pilha(lista_original):
    pilha = Pilha(len(lista_original) + 1)

    tracemalloc.start()
    tempoPilhaMontagemInicio = time.perf_counter()

    for item in lista_original:
        pilha.adicionar(item)

    tempoPilhaMontagemFim = time.perf_counter()
    memoriaMontagemPilha, _ = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    tracemalloc.reset_peak()

    tempoMontagemPilha = tempoPilhaMontagemFim - tempoPilhaMontagemInicio
    print(
        f"Tempo para montar a pilha: {tempoMontagemPilha} segundos\nMemoria usada para montar a pilha: {memoriaMontagemPilha} bytes\n")

    return pilha, memoriaMontagemPilha, tempoMontagemPilha


def montar_fila(lista_original):
    fila = Fila()

    tempoFilaMontagemInicio = time.perf_counter()
    tracemalloc.start()

    for item in lista_original:
        fila.adicionar(item)

    tempoFilaMontagemFim = time.perf_counter()
    memoriaMontagemFila, _ = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    tracemalloc.reset_peak()

    tempoMontagemFila = tempoFilaMontagemFim - tempoFilaMontagemInicio
    print(
        f"Tempo para montar a fila: {tempoMontagemFila} segundos\nMemoria usada para montar a fila: {memoriaMontagemFila} bytes\n")

    return fila, memoriaMontagemFila, tempoMontagemFila


def montar_tabela_hash(lista_original):
    tabela = HashTable()

    tempoMontagemTabelaInicio = time.perf_counter()
    tracemalloc.start()

    for item in lista_original:
        tabela.adicionar(item)

    tempoMontagemTabelaFim = time.perf_counter()
    memoriaMontagemTabela, _ = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    tracemalloc.reset_peak()

    tempoMontagemTabela = tempoMontagemTabelaFim - tempoMontagemTabelaInicio
    print(
        f"Tempo para montar a tabela hash: {tempoMontagemTabela} segundos\nMemoria usada para montar a tabela hash: {memoriaMontagemTabela} bytes\n")

    return tabela, memoriaMontagemTabela, tempoMontagemTabela


def get_listagem():
    with open("listagem_arquivos.txt", "r") as arquivo:
        return [string_num.strip() for string_num in arquivo]


print("# Extraindo listagem do arquivo...")
listagem = get_listagem()

print("\n# Montando fila a partir da listagem para os testes...")
fila, memoriaMontagemFila, tempoMontagemFila = montar_fila(listagem)

print("# Primeiro teste------------------------")
print("# Recuperando o primeiro elemento")
tempoFilaItem1Inicio = time.perf_counter()
tracemalloc.start()

primeiroItemFila = fila.remover()

tempoFilaItem1Fim = time.perf_counter()
memoriaAtualFilaItem1, _ = tracemalloc.get_traced_memory()
tracemalloc.stop()
tracemalloc.reset_peak()

tempoRemocaoItem1Fila = tempoFilaItem1Fim - tempoFilaItem1Inicio
print(
    f"Tempo para recuperar o primeiro item '{primeiroItemFila}' da fila: {tempoRemocaoItem1Fila} segundos\nMemoria alocada para recuperar o primeiro item: {memoriaAtualFilaItem1} bytes\n")

print("# Remontando fila para o próximo teste...")
fila, memoriaMontagemFila, tempoMontagemFila = montar_fila(listagem)

print("# Segundo teste-----------------------------------")
print("# Recuperando o elemento número 100")
tempoFilaitem100Inicio = time.perf_counter()
tracemalloc.start()

for i in range(99):
    fila.remover()
item100Fila = fila.remover()

tempoFilaItem100Fim = time.perf_counter()
memoriaAtualFilaItem100, _ = tracemalloc.get_traced_memory()
tracemalloc.stop()
tracemalloc.reset_peak()

tempoRemocaoItem100Fila = tempoFilaItem100Fim - tempoFilaitem100Inicio
print(
    f"Tempo para recuperar o item 100 '{item100Fila}' da fila: {tempoRemocaoItem100Fila} segundos\nMemoria alocada para recuperar o item 100: {memoriaAtualFilaItem100} bytes\n")

print("# Remontando fila para o próximo teste...")
fila, memoriaMontagemFila, tempoMontagemFila = montar_fila(listagem)

print("# Terceiro teste--------")
print("# Recuperando o elemento número 1000")
tempoFilaitem1000Inicio = time.perf_counter()
tracemalloc.start()

for i in range(999):
    fila.remover()
item1000Fila = fila.remover()

tempoFilaItem1000Fim = time.perf_counter()
memoriaAtualFilaItem1000, _ = tracemalloc.get_traced_memory()
tracemalloc.stop()
tracemalloc.reset_peak()

tempoRemocaoItem1000Fila = tempoFilaItem1000Fim - tempoFilaitem1000Inicio
print(
    f"Tempo para recuperar o item 1000 '{item1000Fila}' da fila: {tempoRemocaoItem1000Fila} segundos\nMemoria alocada para recuperar o item 1000: {memoriaAtualFilaItem1000} bytes\n")

print("# Remontando fila para o próximo teste...")
fila, memoriaMontagemFila, tempoMontagemFila = montar_fila(listagem)

print("# Quarto teste----------------")
print("# Recuperando o elemento número 5000")
tempoFilaItem5000Inicio = time.perf_counter()
tracemalloc.start()

for i in range(4999):
    fila.remover()
item5000Fila = fila.remover()

tempoFilaItem5000Fim = time.perf_counter()
memoriaAtualFilaItem5000, _ = tracemalloc.get_traced_memory()
tracemalloc.stop()
tracemalloc.reset_peak()

tempoRemocaoItem5000Fila = tempoFilaItem5000Fim - tempoFilaItem5000Inicio
print(
    f"Tempo para recuperar o item 5000 '{item5000Fila}' da fila: {tempoRemocaoItem5000Fila} segundos\nMemoria alocada para recuperar o item 5000: {memoriaAtualFilaItem5000} bytes\n")

print("# Remontando fila para o próximo teste...")
fila, memoriaMontagemFila, tempoMontagemFila = montar_fila(listagem)

print("# Quinto teste---------------------------------")
print("Recuperar o último item da fila")
tempoFilaUltimoInicio = time.perf_counter()
tracemalloc.start()

for i in range(9999):
    fila.remover()
itemUltimoFila = fila.remover()

tempoFilaUltimoFim = time.perf_counter()
memoriaUltimoItemFila, _ = tracemalloc.get_traced_memory()
tracemalloc.stop()
tracemalloc.reset_peak()

tempoRemocaoUltimoFila = tempoFilaUltimoFim - tempoFilaUltimoInicio
print(
    f"Tempo para recuperar o último item da fila '{itemUltimoFila}' da fila: {tempoRemocaoUltimoFila} segundos\nMemoria alocada para recuperar o último item da fila: {memoriaUltimoItemFila} bytes\n")

print("# Sexto teste------------")
print("# Adicionando item a fila")
tempoAdicaoFilaInicio = time.perf_counter()
tracemalloc.start()

fila.adicionar("arquivoX")

tempoAdicaoFilaFim = time.perf_counter()
memoriaAtualFilaItemAdicao, _ = tracemalloc.get_traced_memory()
tracemalloc.stop()
tracemalloc.reset_peak()

tempoAdicaoFila = tempoAdicaoFilaFim - tempoAdicaoFilaInicio
print(
    f"Tempo para adicionar um item na fila: {tempoAdicaoFila} segundos\nMemoria alocada para adicionar um item na fila: {memoriaAtualFilaItemAdicao} byte\n")

print("Fim dos testes da fila-------------------------------")

print("\n# Montando pilha a partir da listagem para os testes...\n")
pilha, memoriaMontagemPilha, tempoMontagemPilha = montar_pilha(listagem)

print("# Primeiro teste------------------")
print("# Recuperando o primeiro elemento\n")
tempoItem1PilhaInicio = time.perf_counter()
tracemalloc.start()

item1Pilha = pilha.remover()

tempoItem1PilhaFim = time.perf_counter()
memoriaAtualPilhaItem1, _ = tracemalloc.get_traced_memory()
tracemalloc.stop()
tracemalloc.reset_peak()

tempoRemocaoItem1Pilha = tempoItem1PilhaFim - tempoItem1PilhaInicio
print(
    f"Tempo para recuperar o primeiro item '{item1Pilha}' da pilha: {tempoRemocaoItem1Pilha} segundos\nMemoria alocada para recuperar o primeiro item da pilha: {memoriaAtualPilhaItem1} bytes\n")

print("\n# Remontando pilha para o proximo teste...\n")
pilha, memoriaMontagemPilha, tempoMontagemPilha = montar_pilha(listagem)

print("# Segundo teste-----------------------------------")
print("# Recuperando o elemento número 100")
tempoItem100PilhaInicio = time.perf_counter()
tracemalloc.start()

for i in range(99):
    pilha.remover()
item100Pilha = pilha.remover()

tempoItem100PilhaFim = time.perf_counter()
memoriaAtualPilhaItem100, _ = tracemalloc.get_traced_memory()
tracemalloc.stop()
tracemalloc.reset_peak()

tempoRemocaoItem100Pilha = tempoItem100PilhaFim - tempoItem100PilhaInicio
print(
    f"Tempo para recuperar o item 100 '{item100Pilha}' da pilha: {tempoRemocaoItem100Pilha} segundos\nMemoria alocada para recuperar o item 100 da pilha: {memoriaAtualPilhaItem100} bytes\n")

print("\n# Remontando pilha para o proximo teste...\n")
pilha, memoriaMontagemPilha, tempoMontagemPilha = montar_pilha(listagem)

print("# Terceiro teste--------")
print("# Recuperando o elemento número 1000")
tempoItem1000PilhaInicio = time.perf_counter()
tracemalloc.start()

for i in range(999):
    pilha.remover()
item1000Pilha = pilha.remover()

tempoItem1000PilhaFim = time.perf_counter()
memoriaAtualPilhaItem1000, _ = tracemalloc.get_traced_memory()
tracemalloc.stop()
tracemalloc.reset_peak()

tempoRemocaoItem1000Pilha = tempoItem1000PilhaFim - tempoItem1000PilhaInicio
print(
    f"Tempo para recuperar o item 1000 '{item1000Pilha}' da pilha: {tempoRemocaoItem1000Pilha} segundos\nMemoria alocada para recuperar o item 1000 da pilha: {memoriaAtualPilhaItem1000} bytes\n")

print("\n# Remontando pilha para o proximo teste...\n")
pilha, memoriaMontagemPilha, tempoMontagemPilha = montar_pilha(listagem)

print("# Quarto teste----------------------------")
print("# Recuperando o elemento número 5000")
tempoItem5000PilhaInicio = time.perf_counter()
tracemalloc.start()

for i in range(4999):
    pilha.remover()
item5000Pilha = pilha.remover()

tempoItem5000PilhaFim = time.perf_counter()
memoriaAtualPilhaItem5000, _ = tracemalloc.get_traced_memory()
tracemalloc.stop()
tracemalloc.reset_peak()

tempoRemocaoItem5000Pilha = tempoItem5000PilhaFim - tempoItem5000PilhaInicio
print(
    f"Tempo para recuperar o item 5000 '{item5000Pilha}' da pilha: {tempoRemocaoItem5000Pilha} segundos\nMemoria alocada para recuperar o item 5000 da pilha: {memoriaAtualPilhaItem5000} bytes\n")

print("\n# Remontando pilha para o proximo teste...\n")
pilha, memoriaMontagemPilha, tempoMontagemPilha = montar_pilha(listagem)

print("# Quinto teste ------------------")
print("# Recuperando o último elemento da pilha")
tempoPilhaUltimoInicio = time.perf_counter()
tracemalloc.start()

for i in range(9999):
    pilha.remover()
itemUltimoPilha = pilha.remover()

tempoPilhaUltimoFim = time.perf_counter()
memoriaUltimoItemPilha, _ = tracemalloc.get_traced_memory()
tracemalloc.stop()
tracemalloc.reset_peak()

tempoRemocaoUltimoPilha = tempoPilhaUltimoFim - tempoPilhaUltimoInicio
print(
    f"Tempo para recuperar o último item da pilha '{itemUltimoPilha}' da pilha: {tempoRemocaoUltimoPilha} segundos\nMemoria alocada para recuperar o último item da pilha: {memoriaUltimoItemPilha} bytes\n")

print("# Sexto teste-----------------")
print("# Adicionando um elemento a pilha")
tempoAdicaoPilhaInicio = time.perf_counter()
tracemalloc.start()

pilha.adicionar("arquivoX")

tempoAdicaoPilhaFim = time.perf_counter()
memoriaAtualPilhaAdicao, _ = tracemalloc.get_traced_memory()
tracemalloc.stop()
tracemalloc.reset_peak()

tempoAdicaoPilha = tempoAdicaoPilhaFim - tempoAdicaoPilhaInicio
print(
    f"Tempo para adicionar um item na pilha: {tempoAdicaoPilha} segundos\nMemoria alocada para adicionar um item na pilha: {memoriaAtualPilhaAdicao} bytes\n")

print("Fim dos testes de pilha-------------------------------")

print("\n# Montando tabela hash a partir da listagem para os testes...")
tabela, memoriaMontagemTabela, tempoMontagemTabela = montar_tabela_hash(listagem)

print("# Primeiro teste---------------")
print("# Recuperando o primeiro elemento")
tempoItem1HashInicio = time.perf_counter()
tracemalloc.start()

item1Hash = tabela.procurar_por_item("arquivo0")

tempoItem1HashFim = time.perf_counter()
memoriaAtualItem1Hash, _ = tracemalloc.get_traced_memory()
tracemalloc.stop()
tracemalloc.reset_peak()

tempoRemocaoItem1Hash = tempoItem1HashFim - tempoItem1HashInicio
print(
    f"Tempo para recuperar o item 1 '{item1Hash}' da tabela hash: {tempoRemocaoItem1Hash} segundos\nMemoria alocada para recuperar o item 1 da tabela hash: {memoriaAtualItem1Hash} bytes\n")

print("# Segundo teste-----------------------------------")
print("# Recuperando o elemento número 100")
tempoItem100HashInicio = time.perf_counter()
tracemalloc.start()

item100Hash = tabela.procurar_por_item("arquivo1087")

tempoItem100HashFim = time.perf_counter()
memoriaAtualItem100Hash, _ = tracemalloc.get_traced_memory()
tracemalloc.stop()
tracemalloc.reset_peak()

tempoRemocaoItem100Hash = tempoItem100HashFim - tempoItem100HashInicio
print(
    f"Tempo para recuperar o item 100 '{item100Hash}' da tabela hash: {tempoRemocaoItem100Hash} segundos\nMemoria alocada para recuperar o item 100 da tabela hash: {memoriaAtualItem100Hash} bytes\n")

print("# Terceiro teste--------------")
print("# Recuperando o elemento número 1000")
tempoItem1000HashInicio = time.perf_counter()
tracemalloc.start()

item1000Hash = tabela.procurar_por_item("arquivo1898")

tempoItem1000HashFim = time.perf_counter()
memoriaAtualItem1000Hash, _ = tracemalloc.get_traced_memory()
tracemalloc.stop()
tracemalloc.reset_peak()

tempoRemocaoItem1000Hash = tempoItem1000HashFim - tempoItem1000HashInicio
print(
    f"Tempo para recuperar o item 1000 '{item1000Hash}' da tabela hash: {tempoRemocaoItem1000Hash} segundos\nMemoria alocada para recuperar o item 1000 da tabela hash: {memoriaAtualItem1000Hash} bytes\n")

print("# Quarto teste----------------")
print("# Recuperando o elemento número 5000")
tempoItem5000HashInicio = time.perf_counter()
tracemalloc.start()

item5000Hash = tabela.procurar_por_item("arquivo5498")

tempoItem5000HashFim = time.perf_counter()
memoriaAtual5000Hash, _ = tracemalloc.get_traced_memory()
tracemalloc.stop()
tracemalloc.reset_peak()

tempoRemocaoItem5000Hash = tempoItem5000HashFim - tempoItem5000HashInicio
print(
    f"Tempo para recuperar o item 5000 '{item5000Hash}' da tabela hash: {tempoRemocaoItem5000Hash} segundos\nMemoria alocada para recuperar o item 5000 da tabela hash: {memoriaAtual5000Hash} bytes\n")

print("# Quinto teste------------")
print("# Recuperando ultimo elemento da tabela")
tempoUltimoInicio = time.perf_counter()
tracemalloc.start()

ultimoItemTabela = tabela.procurar_por_item("arquivo9999")

tempoUltimoTabelaFim = time.perf_counter()
memoriaUltimoTabela, _ = tracemalloc.get_traced_memory()
tracemalloc.stop()
tracemalloc.reset_peak()

tempoUltimoTabela = tempoUltimoTabelaFim - tempoUltimoInicio
print(
    f"Tempo para recuperar o ultimo item da tabela hash '{ultimoItemTabela}': {tempoUltimoTabela} segundos\nMemoria alocada para recuperar o item 5000 da tabela hash: {memoriaUltimoTabela} bytes\n")

print("# Sexto teste ---------------")
print("# Adicionando item a tabela hash")
tempoAdicaoTabelaInicio = time.perf_counter()
tracemalloc.start()

tabela.adicionar("arquivoX")

tempoAdicaoTabelaFim = time.perf_counter()
memoriaAtualAdicaoTabela, _ = tracemalloc.get_traced_memory()
tracemalloc.stop()
tracemalloc.reset_peak()

tempoAdicaoTabela = tempoAdicaoTabelaFim - tempoAdicaoTabelaInicio
print(
    f"Tempo para adicionar um item na tabela hash: {tempoAdicaoTabela} segundos\nMemoria alocada para adicionar um item a tabela hash: {memoriaAtualAdicaoTabela} bytes\n")

print("# Setimo teste-------------------")
print("# Removendo item da tabela hash")
tempoRemocaoTabelaInicio = time.perf_counter()
tracemalloc.start()

tabela.remover("arquivoX")

tempoRemocaoTabelaFim = time.perf_counter()
memoriaAtualRemocaoTabela, _ = tracemalloc.get_traced_memory()
tracemalloc.stop()
tracemalloc.reset_peak()

tempoRemocaoTabela = tempoRemocaoTabelaFim - tempoRemocaoTabelaInicio
print(
    f"Tempo para remover um item da tabela hash: {tempoRemocaoTabela} segundos\nMemoria alocada para remover um item da tabela hash: {memoriaAtualRemocaoTabela} bytes\n")
