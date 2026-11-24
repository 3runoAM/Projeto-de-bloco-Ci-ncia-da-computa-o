class Grafo:
    def __init__(self):
        self.adjacencias = {}

    def adicionar_cidade(self, nome):
        if nome not in self.adjacencias:
            self.adjacencias[nome] = {}

    def adicionar_aresta(self, cidade_a, cidade_b, custo):
        self.adjacencias[cidade_a][cidade_b] = custo
        self.adjacencias[cidade_b][cidade_a] = custo

    def imprimir(self):
        for cidade, vizinhas in self.adjacencias.items():
            print(f"{cidade}: {vizinhas}")

    def vizinho_mais_proximo(self, cidade_inicial):
        caminho = [cidade_inicial]
        ja_visitadas = {cidade_inicial}
        custo_total = 0

        while len(caminho) < len(self.adjacencias):
            cidade_atual = caminho[-1]
            proxima_cidade = None
            menor_custo = float("inf")

            for candidata, custo in self.adjacencias[cidade_atual].items():
                if candidata not in ja_visitadas and custo < menor_custo:
                    menor_custo = custo
                    proxima_cidade = candidata

            caminho.append(proxima_cidade)
            ja_visitadas.add(proxima_cidade)
            custo_total += menor_custo


        ultima_cidade = caminho[-1]
        custo_total += self.adjacencias[ultima_cidade][cidade_inicial]
        caminho.append(cidade_inicial)
        return caminho, custo_total


grafo = Grafo()
grafo.adicionar_cidade("Lisboa")
grafo.adicionar_cidade("Coimbra")
grafo.adicionar_cidade("Faro")
grafo.adicionar_cidade("Porto")

grafo.adicionar_aresta("Lisboa", "Porto", 2)
grafo.adicionar_aresta("Lisboa", "Coimbra", 9)
grafo.adicionar_aresta("Lisboa", "Faro", 10)
grafo.adicionar_aresta("Porto", "Coimbra", 6)
grafo.adicionar_aresta("Porto", "Faro", 4)
grafo.adicionar_aresta("Coimbra", "Faro", 3)

grafo.imprimir()

caminho, custo = grafo.vizinho_mais_proximo("Lisboa")
print("Caminho:", caminho, "Custo:", custo)