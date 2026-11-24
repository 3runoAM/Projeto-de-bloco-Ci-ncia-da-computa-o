import time


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

def prim(grafo):
    arestas_analisadas = 0
    custo_total = 0
    if not grafo:
        return [], 0

    no_inicial = list(grafo.keys())[0]
    visitados = set([no_inicial])
    filaDePrioridores = MinHeap()

    for vizinho, peso in grafo[no_inicial].items():
        filaDePrioridores.inserir((peso, no_inicial, vizinho))

    arvore_geradora = []

    while filaDePrioridores:
        peso, origem, destino = filaDePrioridores.extrair_min()
        arestas_analisadas += 1
        if destino not in visitados:
            visitados.add(destino)
            arvore_geradora.append((peso, origem, destino))
            custo_total += peso
            for proximo_vizinho, proximo_peso in grafo[destino].items():
                if proximo_vizinho not in visitados:
                    filaDePrioridores.inserir((proximo_peso, destino, proximo_vizinho))

    print(f"|\tArestas analisadas: {arestas_analisadas}")

    return arvore_geradora, custo_total

def kruskal(grafo):
    def find(pai, i):
        if pai[i] == i:
            return i
        return find(pai, pai[i])

    def union(pai, rank, x, y):
        raiz_x = find(pai, x)
        raiz_y = find(pai, y)

        if rank[raiz_x] < rank[raiz_y]:
            pai[raiz_x] = raiz_y
        elif rank[raiz_x] > rank[raiz_y]:
            pai[raiz_y] = raiz_x
        else:
            pai[raiz_y] = raiz_x
            rank[raiz_x] += 1

    arvore_geradora = []
    arestas_na_mst, arestas_analisadas, custo_total = 0, 0, 0

    vertices_map = {nodo: indice for indice, nodo in enumerate(grafo)}
    num_vertices = len(vertices_map)

    arestas = []
    for u in grafo:
        for v, peso in grafo[u].items():
            if vertices_map[u] < vertices_map[v]:
                arestas.append([peso, u, v])
    arestas = sorted(arestas, key=lambda item: item[0])

    pai = []
    rank = []
    for no in range(num_vertices):
        pai.append(no)
        rank.append(0)

    while arestas_analisadas < num_vertices - 1:
        peso, u, v = arestas[arestas_na_mst]
        arestas_na_mst += 1
        x = find(pai, vertices_map[u])
        y = find(pai, vertices_map[v])

        if x != y:
            arestas_analisadas += 1
            arvore_geradora.append([peso, u, v])
            custo_total += peso
            union(pai, rank, x, y)

    print(f"|\tArestas analisadas: {arestas_analisadas}")

    return arvore_geradora, custo_total

grafo = {
    'A': {"B": 2, 'C': 3},
    'B': {"A": 2, "C": 1, "D": 4},
    'C': {"A": 3, "B": 1, "D": 5},
    'D': {"B": 4, "C": 5},
}



print("| Analise de Kruskal")
inicio = time.perf_counter()
arvore, custo = kruskal(grafo)
fim = time.perf_counter()
print(f"|\tTempo de execução {fim - inicio} segundos")
print(f"|\tCusto total da árvore geradora mínima: {custo}")
print(f"|\tÁrvore geradora mínima: {arvore}")



print("| Analise de Prim")
inicio = time.perf_counter()
arvore, custo = prim(grafo)
fim = time.perf_counter()
print(f"|\tTempo de execução {fim - inicio} segundos")
print(f"|\tCusto total da árvore geradora mínima: {custo}")
print(f"|\tÁrvore geradora mínima: {arvore}")
