class MinHeap:
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
        while index > 0 and self._heap[index] < self._heap[pai_index]:
            self._troca(index, pai_index)
            index = pai_index
            pai_index = self._get_pai_index(index)

    def sift_down(self, index):
        ultimo_index = len(self._heap) - 1
        while True:
            filhoE_index = self._get_filho_esquerdo_index(index)
            filhoD_index = self._get_filho_direito_index(index)
            menor = index

            if filhoE_index <= ultimo_index and self._heap[filhoE_index] < self._heap[menor]:
                menor = filhoE_index
            if filhoD_index <= ultimo_index and self._heap[filhoD_index] < self._heap[menor]:
                menor = filhoD_index

            if menor != index:
                self._troca(index, menor)
                index = menor
            else:
                break

    def inserir(self, valor):
        self._heap.append(valor)
        self.sift_up(len(self._heap) - 1)

    def extrair_min(self):
        if not self._heap:
            return None
        if len(self._heap) == 1:
            return self._heap.pop()
        raiz = self._heap[0]
        self._heap[0] = self._heap.pop()
        self.sift_down(0)
        return raiz

    def _olhar(self):
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
heap = MinHeap()
print(f"| Inserindo valores {lista_nums}")
for i in lista_nums:
    heap.inserir(i)

print("| Heap montada:")
print("|\t", end="")
heap.imprimir()

print("\n| Removendo o menor elemento")
menor = heap.extrair_min()
print(f"|\tMenor elemento: {menor}")

print("| Consultando menor elemento após remover o menor")
print(f"|\tMenor elemento: {heap._olhar()}")
