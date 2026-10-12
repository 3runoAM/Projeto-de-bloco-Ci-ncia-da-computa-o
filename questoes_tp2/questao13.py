class No:
    def __init__(self, dado):
        self.dado = dado
        self.prox = None

class ListaEncadeada:
    def __init__(self):
        self.inicio = None
        self.tamanho_lista = 0

    def inserir_comeco(self, dado):
        no = No(dado)
        no.prox = self.inicio
        self.inicio = no
        self.tamanho_lista += 1

    def inserir_final(self, dado):
        no = No(dado)
        contador = 0
        if not self.inicio:
            self.inicio = no
            self.tamanho_lista += 1
            return

        contador+=1
        no_atual = self.inicio
        while no_atual.prox:
            no_atual = no_atual.prox
            contador += 1

        no_atual.prox = no
        self.tamanho_lista += 1

    def buscar(self, dado):
        if not self.inicio:
            return None

        no_atual = self.inicio
        while no_atual:
            if no_atual.dado == dado:
                return no_atual
            no_atual = no_atual.prox
        return None

    def remover(self, dado):
        if not self.inicio: return None

        no_atual = self.inicio
        proximo = no_atual.prox
        if no_atual.dado == dado:
            self.inicio = proximo
            no_atual.prox = None
            return no_atual

        while no_atual.prox:
            proximo = no_atual.prox
            if proximo.dado == dado:
                no_atual.prox = no_atual.prox.prox
                proximo.prox = None
                return proximo
            no_atual = no_atual.prox

        return None

    def __str__(self):
        string_saida = ""
        atual = self.inicio

        contador = 0
        while atual:
            string_saida += f"{atual.dado}"
            if atual.prox: string_saida += " -> "
            atual = atual.prox
            contador += 1

        return string_saida


array = [15, 456, 312, 6748, 546, 984, 312, 542]
lista = ListaEncadeada()
for i in array:
    lista.inserir_comeco(i)
print(f"| Lista encadeada:\n|\t{lista.__str__()}\n")

print(f"| Inserindo no fim")
lista.inserir_final("FIM")
print(f"| Lista encadeada:\n|\t{lista.__str__()}\n")

print(f" Inserindo no começo")
lista.inserir_comeco("COMEÇO")
print(f"| Lista encadeada:\n|\t{lista.__str__()}\n")

print(f"| Removendo do começo")
lista.remover("COMEÇO")
print(f"| Lista encadeada:\n|\t{lista.__str__()}\n")

print(f"| Removendo do fim")
lista.remover("FIM")
print(f"| Lista encadeada:\n|\t{lista.__str__()}\n")

print(f"| Removendo no meio")
lista.remover(6748)
print(f"| Lista encadeada:\n|\t{lista.__str__()}\n")