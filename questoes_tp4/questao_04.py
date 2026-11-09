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
        while index > 0:
            pai_index = self._get_pai_index(index)
            if self._heap[index][1:] < self._heap[pai_index][1:]:
                self._troca(index, pai_index)
                index = pai_index
            else:
                break

    def sift_down(self, index):
        ultimo_index = len(self._heap) - 1
        while True:
            filhoE_index = self._get_filho_esquerdo_index(index)
            filhoD_index = self._get_filho_direito_index(index)
            menor = index

            if filhoE_index <= ultimo_index and self._heap[filhoE_index][1:] < self._heap[menor][1:]:
                menor = filhoE_index

            if filhoD_index <= ultimo_index and self._heap[filhoD_index][1:] < self._heap[menor][1:]:
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

    def imprimir(self):
        tam = self.__len__()
        index = 0
        while index < tam:
            tupla = self._heap[index]
            id = tupla[0]
            prioridade = tupla[1]
            tempo_chegada = tupla[2]
            print(f"|\tID: {id}, Prioridade: {prioridade}, Tempo de Chegada: {tempo_chegada}")
            index += 1

    def _olhar(self):
        if self._heap:
            return self._heap[0]
        return None

    def __len__(self):
        return len(self._heap)

class FilaDePrioridade:
    def __init__(self):
        self._min_heap = MinHeap()
        self.id_count = 10

    def enqueue(self, prioridade, tempo_chegada):
        self.id_count += 1
        self._min_heap.inserir((self.id_count, prioridade, tempo_chegada))

    def dequeue(self):
        par_prioridade_elemento = self._min_heap.extrair_min()
        if par_prioridade_elemento:
            return par_prioridade_elemento
        return None

    def olhar(self):
        par_prioridade_elemento = self._min_heap._olhar()
        if par_prioridade_elemento:
            return par_prioridade_elemento
        return None


fila = FilaDePrioridade()

fila.enqueue(1, 10)
fila.enqueue(3, 9)
fila.enqueue(2, 7)
fila.enqueue(2, 8)

print("| Fila de prioridade")
fila._min_heap.imprimir()

print()
extraido = fila.dequeue()
id = extraido[0]
prioridade = extraido[1]
tempo_chegada = extraido[2]
print(f"| Extraindo menor:\n|\tID: {id}, Prioridade: {prioridade}, Tempo de Chegada: {tempo_chegada}")

print()
print("| Fila de prioridade após remoção do menor")
fila._min_heap.imprimir()

print()
extraido = fila.dequeue()
id = extraido[0]
prioridade = extraido[1]
tempo_chegada = extraido[2]
print(f"| Extraindo menor:\n|\tID: {id}, Prioridade: {prioridade}, Tempo de Chegada: {tempo_chegada}")