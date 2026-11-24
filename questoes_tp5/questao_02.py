class Grafo:
    def __init__(self):
        self.grafo = []
        self.num_vertices = 0
        self.vertices_map = {}

    def adicionar_aresta(self, u, v, peso):
        if u not in self.vertices_map:
            self.vertices_map[u] = self.num_vertices
            self.num_vertices += 1
        if v not in self.vertices_map:
            self.vertices_map[v] = self.num_vertices
            self.num_vertices += 1
        self.grafo.append([peso, u, v])

    def find(self, pai, i):
        if pai[i] == i:
            return i
        return self.find(pai, pai[i])

    def union(self, pai, rank, x, y):
        raiz_x = self.find(pai, x)
        raiz_y = self.find(pai, y)

        if rank[raiz_x] < rank[raiz_y]:
            pai[raiz_x] = raiz_y
        elif rank[raiz_x] > rank[raiz_y]:
            pai[raiz_y] = raiz_x
        else:
            pai[raiz_y] = raiz_x
            rank[raiz_x] += 1

    def kruskal(self):
        resultado = []
        i, e, custo_total = 0, 0, 0

        self.grafo = sorted(self.grafo, key=lambda item: item[0])

        pai = list(range(self.num_vertices))
        rank = [0] * self.num_vertices

        while e < self.num_vertices - 1 and i < len(self.grafo):
            peso, u, v = self.grafo[i]
            i += 1
            x = self.find(pai, self.vertices_map[u])
            y = self.find(pai, self.vertices_map[v])

            if x != y:
                e += 1
                resultado.append([peso, u, v])
                custo_total += peso
                self.union(pai, rank, x, y) 

        return resultado, custo_total

    def exibir_grafo(self, arestas_grafo, arestas_mst):
        print("Arestas do grafo original:")
        for peso, u, v in arestas_grafo:
            print(f"  {u} -- {v} (peso: {peso})")

        print("\nArestas da árvore geradora mínima:")
        for peso, u, v in arestas_mst:
            print(f"  {u} -- {v} (peso: {peso})")


grafo = Grafo()

grafo.adicionar_aresta("A", "B", 4)
grafo.adicionar_aresta("A", "C", 4)
grafo.adicionar_aresta("B", "C", 2)
grafo.adicionar_aresta("C", "D", 3)
grafo.adicionar_aresta("C", "E", 1)
grafo.adicionar_aresta("C", "F", 6)
grafo.adicionar_aresta("D", "F", 2)
grafo.adicionar_aresta("E", "F", 3)

arestas_originais = list(grafo.grafo)
mst, custo = grafo.kruskal()

grafo.exibir_grafo(arestas_originais, mst)
print(f"\n| Custo total da MST: {custo}")