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

class FilaDePrioridade:
    def __init__(self):
        self._min_heap = MinHeap()

    def enqueue(self, elemento):
        self._min_heap.inserir(elemento)

    def dequeue(self):
        par_prioridade_elemento = self._min_heap.extrair_min()
        if par_prioridade_elemento:
            return par_prioridade_elemento
        return None

    def olhar(self):
        par_prioridade_elemento = self._min_heap._olhar()
        if par_prioridade_elemento:
            return par_prioridade_elemento[1]
        return None

def dijsktra(grafo, inicio):
    distancias = {nodo: float("inf") for nodo in grafo}
    distancias[inicio] = 0
    antecessores = {nodo: None for nodo in grafo}

    filaPrioridades = FilaDePrioridade()
    filaPrioridades.enqueue((0, inicio))

    while filaPrioridades.olhar():
        distancia_atual, nodo_atual = filaPrioridades.dequeue()
        if distancia_atual > distancias[nodo_atual]:
            continue

        for vizinho, peso in grafo[nodo_atual].items():
            distancia = distancia_atual + peso
            if distancia < distancias[vizinho]:
                distancias[vizinho] = distancia
                antecessores[vizinho] = nodo_atual
                filaPrioridades.enqueue((distancia, vizinho))

    return distancias, antecessores

grafo = {
    'A': {"B": 2, 'C': 3},
    'B': {"A": 2, "C": 1, "D": 4},
    'C': {"A": 3, "B": 1, "D": 5},
    'D': {"B": 4, "C": 5},
}

distancias, _ = dijsktra(grafo, 'A')
print(f"| Distancias com dijsktra\n|\t{distancias}")