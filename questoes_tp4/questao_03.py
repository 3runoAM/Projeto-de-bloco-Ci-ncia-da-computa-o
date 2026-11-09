class MaxHeap:
    def __init__(self):
        self._heap = []

    def _get_pai_index(self, index):
        return (index - 1) // 2

    def _get_filho_esquerdo_index(self, index):
        return 2 * index + 1

    def _get_filho_direito_index(self, index):
        return 2 * index + 2

    def _troca(self, i, j):
        self._heap[i], self._heap[j] = self._heap[j], self._heap[i]

    def sift_up(self, index):
        pai_index = self._get_pai_index(index)
        while index > 0 and self._heap[index] > self._heap[pai_index]:
            self._troca(index, pai_index)
            index = pai_index
            pai_index = self._get_pai_index(index)

    def sift_down(self, index):
        ultimo_index = len(self._heap) - 1
        while True:
            filhoE_index = self._get_filho_esquerdo_index(index)
            filhoD_index = self._get_filho_direito_index(index)
            maior = index

            if filhoE_index <= ultimo_index and self._heap[filhoE_index] > self._heap[maior]:
                maior = filhoE_index

            if filhoD_index <= ultimo_index and self._heap[filhoD_index] > self._heap[maior]:
                maior = filhoD_index

            if maior != index:
                self._troca(index, maior)
                index = maior
            else:
                break

    def inserir(self, valor):
        self._heap.append(valor)
        self.sift_up(len(self._heap) - 1)

    def extrair_max(self):
        if not self._heap:
            return None
        if len(self._heap) == 1:
            return self._heap.pop()

        raiz = self._heap[0]
        self._heap[0] = self._heap.pop()
        self.sift_down(0)
        return raiz

    def olhar(self):
        if self._heap:
            return self._heap[0]
        return None

    def __len__(self):
        return len(self._heap)

    def imprimir(self):
        tam = self.__len__()
        index = 0
        while index < tam:
            print(self._heap[index], end=" ")
            index += 1


lista_nums = [6, 4, 23, 3, 8, 17, 25]
heap = MaxHeap()
print(f"| Inserindo valores {lista_nums}")
for i in lista_nums:
    heap.inserir(i)

print("| Heap montada:")
print("|\t", end="")
heap.imprimir()

print("\n| Removendo o maior elemento")
maior = heap.extrair_max()
print(f"|\tMaior elemento: {maior}")

print("| Consultando maior elemento após remover o maior")
print(f"|\tMaior elemento: {heap.olhar()}")
