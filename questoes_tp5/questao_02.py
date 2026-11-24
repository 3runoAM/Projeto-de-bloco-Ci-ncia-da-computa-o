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

def prim(grafo):
    if not grafo:
        return []

    no_inicial = list(grafo.keys())[0]
    visitados = set([no_inicial])
    filaDePrioridores = MinHeap()

    for peso, vizinho in grafo[no_inicial]:
        filaDePrioridores.inserir((peso, no_inicial, vizinho))

    arvore_geradora = []

    while filaDePrioridores:
        peso, origem, destino = filaDePrioridores.extrair_min()
        if destino not in visitados:
            visitados.add(destino)
            arvore_geradora.append((peso, origem, destino))
            for proximo_peso, proximo_vizinho in grafo[destino]:
                if proximo_vizinho not in visitados:
                    filaDePrioridores.inserir((proximo_peso, destino, proximo_vizinho))

    return arvore_geradora

grafo = {
    'A': [(2, 'B'), (3, 'C')],
    'B': [(2, 'A'), (1, 'C'), (4, 'D')],
    'C': [(3, 'A'), (1, 'B'), (5, 'D')],
    'D': [(4, 'B'), (5, 'C')],
}

print(prim(grafo))