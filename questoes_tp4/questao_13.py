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

    def dfs(self, inicio, visitados=None):
        if visitados is None:
            visitados = set()

        visitados.add(inicio)
        print(inicio, end=" ")

        for vizinho in self.lista_adjacencias[inicio]:
            if vizinho not in visitados:
                self.dfs(vizinho, visitados)

    def count_vertices_conectados(self):
        visitados = set()

        self.dfs(0, visitados)

        return len(visitados)

grafo = Grafo(8)
grafo.adicionar_aresta(0, 1)
grafo.adicionar_aresta(0, 2)
grafo.adicionar_aresta(1, 3)
grafo.adicionar_aresta(1, 4)
grafo.adicionar_aresta(2, 5)
grafo.adicionar_aresta(5, 6)

print("| Grafo com lista de adjacências construído")
grafo.imprimir_lista()

print(f"| Número de vértices conectados: {grafo.count_vertices_conectados()}")
