class Grafo:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.lista_adjacencias = {i: [] for i in range(num_vertices)}

    def adicionar_aresta(self, u, v, peso=1):
        self.lista_adjacencias[u].append(v)
        self.lista_adjacencias[v].append(u)

    def remover_aresta(self, u, v):
        if u in self.lista_adjacencias and v in self.lista_adjacencias[u]:
            self.lista_adjacencias[u].remove(v)
        if v in self.lista_adjacencias and u in self.lista_adjacencias[v]:
            self.lista_adjacencias[v].remove(u)

    def imprimir_lista(self):
        for vertice, vizinhos in self.lista_adjacencias.items():
            print(f"Vértice {vertice}: {vizinhos}")
        return None

    def bfs(self, inicio):
        visitados = set()
        fila = [inicio]
        visitados.add(inicio)

        while fila:
            vertice = fila.pop(0)
            print(vertice, end=" ")

            for vizinho in self.lista_adjacencias[vertice]:
                if vizinho not in visitados:
                    visitados.add(vizinho)
                    fila.append(vizinho)


grafo = Grafo(8)
grafo.adicionar_aresta(0, 1)
grafo.adicionar_aresta(0, 2)
grafo.adicionar_aresta(1, 3)
grafo.adicionar_aresta(1, 4)
grafo.adicionar_aresta(2, 5)
grafo.adicionar_aresta(5, 6)

print("| Grafo com lista de adjacências construído")
grafo.imprimir_lista()


vertice = 0
print(f"| Busca por largura a partir do vértice {vertice}", end="\n|\t")
grafo.bfs(vertice)
print()

vertice = 3
print(f"| Busca por largura a partir do vértice {vertice}", end="\n|\t")
grafo.bfs(vertice)
print()

vertice = 7
print(f"| Busca por largura a partir do vértice {vertice}", end="\n|\t")
grafo.bfs(vertice)
print()
