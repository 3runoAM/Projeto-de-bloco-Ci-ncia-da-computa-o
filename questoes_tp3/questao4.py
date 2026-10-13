class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

class ArvoreBinariaBusca:
    def __init__(self):
        self.raiz = None

    def inserir(self, valor):
        if self.raiz is None:
            self.raiz = No(valor)
        else:
            self._inserir_recursivo(self.raiz, valor)

    def _inserir_recursivo(self, no_atual, valor):
        if valor < no_atual.valor:
            if no_atual.esquerda is None:
                no_atual.esquerda = No(valor)
            else:
                self._inserir_recursivo(no_atual.esquerda, valor)
        else:
            if no_atual.direita is None:
                no_atual.direita = No(valor)
            else:
                self._inserir_recursivo(no_atual.direita, valor)

    def buscar(self, valor_buscado):
        return self.buscar_recursivo(self.raiz, valor_buscado)

    def buscar_recursivo(self, no_atual, valor_buscado):
        if no_atual is None or no_atual.valor == valor_buscado:
            return no_atual

        if valor_buscado < no_atual.valor:
            return self.buscar_recursivo(no_atual.esquerda, valor_buscado)
        else:
            return self.buscar_recursivo(no_atual.direita, valor_buscado)

    def remover(self, valor):
        self.raiz = self.remover_recursivo(self.raiz, valor)

    def remover_recursivo(self, no_atual, valor):
        if no_atual is None: return no_atual

        if valor < no_atual.valor:
            no_atual.esquerda = self.remover_recursivo(no_atual.esquerda, valor)
        elif valor > no_atual.valor:
            no_atual.direita = self.remover_recursivo(no_atual.direita, valor)

        else:
            if no_atual.esquerda is None:
                return no_atual.direita
            elif no_atual.direita is None:
                return no_atual.esquerda

            atual = no_atual.direita
            while atual.esquerda is not None:
                atual = atual.esquerda

            no_atual.valor = atual.valor  # atualiza o valor para trocar de lugar com a menor da direita e...=
            no_atual.direita = self.remover_recursivo(no_atual.direita, atual.valor)  # ...apaga o menor da direita

        return no_atual  # retorna a raiz da subarvoreatual

    def calcular_altura(self, no_atual):
        if no_atual is None:
            return 0

        altura_esquerda = self.calcular_altura(no_atual.esquerda)
        altura_direita = self.calcular_altura(no_atual.direita)

        return max(altura_esquerda, altura_direita) + 1

    def exibir_em_ordem(self, no_atual):
        if no_atual:
            self.exibir_em_ordem(no_atual.esquerda)
            print(no_atual.valor, end=" ")
            self.exibir_em_ordem(no_atual.direita)

    def exibir_arvore(self, no_atual=None, nivel = 0):
        if no_atual is None and nivel == 0:
            no_atual = self.raiz

        if no_atual is not None:
            self.exibir_arvore(no_atual.direita, nivel+1)
            print("                         " * nivel + f"-> {no_atual.valor}")
            self.exibir_arvore(no_atual.esquerda, nivel+1)

    def get_maior_valor(self):
        if self.raiz is None:
            return None

        atual = self.raiz
        while atual.direita is not None:
            atual = atual.direita

        return atual.valor


lista_aleatorios = [50, 30, 70, 20, 40, 60, 80]
print(f"| Construindo árvore com a lista {lista_aleatorios}")
arvore = ArvoreBinariaBusca()
for num_aleatorio in lista_aleatorios:
    arvore.inserir(num_aleatorio)
print(f"| Árvore construída")
arvore.exibir_arvore(arvore.raiz)
print(f"| Maior valor da árvore: {arvore.get_maior_valor()}")

