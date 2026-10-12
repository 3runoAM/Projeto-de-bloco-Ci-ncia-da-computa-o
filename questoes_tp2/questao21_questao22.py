class No:
    def __init__(self, chave, valor):
        self.chave = chave
        self.valor = valor
        self.prox = None

class HashTableEncadeada:
    def __init__(self, numero_buckets, limite_fator_carga):
        self.numero_buckets = numero_buckets
        self.tabela = [[] for _ in range(numero_buckets)]
        self.quantidade_nos = 0
        self.limite_fator_carga = limite_fator_carga

    def funcao_hash(self, chave):
        return hash(chave) % self.numero_buckets

    def inserir(self, chave, valor):
        index = self.funcao_hash(chave)
        no_raiz = self.tabela[index]
        no_atual = no_raiz

        while no_atual:
            if no_atual.chave == chave:
                no_atual.valor = valor
                return
            no_atual = no_atual.prox

        novo_no = No(chave, valor)
        novo_no.prox = no_raiz
        self.tabela[index] = novo_no
        self.quantidade_nos += 1

        if self.calcular_carga() > self.limite_fator_carga:
            self.redimensionar_tabela()

    def recuperar(self, chave):
        index = self.funcao_hash(chave)
        no_raiz = self.tabela[index]

        no_atual = no_raiz
        while no_atual:
            if no_atual.chave == chave:
                return no_atual.valor
            no_atual = no_atual.prox

        return None

    def remover(self, chave):
        index = self.funcao_hash(chave)
        no_raiz = self.tabela[index]
        no_anterior = None

        no_atual = no_raiz
        while no_atual:
            if no_atual.chave == chave:
                if no_anterior:
                    no_anterior.prox = no_atual.prox
                    self.quantidade_nos -= 1
                    return None
                else:
                    self.tabela[index] = no_raiz.prox
                    self.quantidade_nos -= 1
                    return None
            no_anterior = no_atual
            no_atual = no_atual.prox
        return None

    def __len__(self):
        return self.quantidade_nos

    def redimensionar_tabela(self):
        tabela_antiga = self.tabela
        self.numero_buckets = self.numero_buckets * 2 + 1
        self.tabela = [[] for _ in range(self.numero_buckets)]

        self.quantidade_nos = 0
        for no_atual in tabela_antiga:
            while no_atual:
                self.inserir(no_atual.chave, no_atual.valor)
                no_atual = no_atual.prox

    def calcular_carga(self):
        return self.quantidade_nos / self.numero_buckets

tabela_hash = HashTableEncadeada(10, 1.0)
print("|------------------------------------------------------")
print(f"| Criando tabela hash com:\n|\t{tabela_hash.numero_buckets} buckets\n|\tlimite_fator_carga de fator de carga {tabela_hash.limite_fator_carga}\n|\tFator de carga atual: {tabela_hash.calcular_carga()}")
print("|------------------------------------------------------")
print(f"| Inserindo valores na tabela hash encadeada")
tabela_hash.inserir("Bruno", "0000000000")
tabela_hash.inserir("Gernan", "1111111111")
tabela_hash.inserir("Loba", "222222222222")
tabela_hash.inserir("Caio", "3333333333333")
tabela_hash.inserir("Cinthia", "4444444444")
print("|------------------------------------------------------")
print(f"| Quantidade de nós após inserir")
print(f"| Quantidade de nós: {tabela_hash.__len__()}")
print(f"|\t\tFator de carga atual: {tabela_hash.calcular_carga()}")
print("|------------------------------------------------------")
print(f"| Atualizando o elemento com chave Bruno na tabela")
tabela_hash.inserir("Bruno", "-")
print("|------------------------------------------------------")
print(f"| Recuperando o elemento que acabou de ser atualizado")
print(f"| Valor: {tabela_hash.recuperar('Bruno')}")
print("|------------------------------------------------------")
print(f"| Removendo o elemento com chave Bruno da tabela")
tabela_hash.remover("Bruno")
print("|------------------------------------------------------")
print(f"| Quantidade de nós após remover a chave Bruno")
print(f"| Quantidade de nós: {tabela_hash.__len__()}")
print(f"|\t\tFator de carga atual: {tabela_hash.calcular_carga()}")
print("|------------------------------------------------------")
print(f"| Tentando recuperar o elemento que acabou de ser removido")
print(f"| Valor: {tabela_hash.recuperar('Bruno')}")
print("|------------------------------------------------------")
print(f"| Inserindo valores até o redimensionamento acontecer")
tabela_hash.inserir("Bruno", "0000000000")
tabela_hash.inserir("Lena", "555555555555555")
tabela_hash.inserir("Marcos", "6666666666666666")
tabela_hash.inserir("Mariana", "77777777777777")
tabela_hash.inserir("Gildenio", "88888888888888")
tabela_hash.inserir("Gilvanira", "99999999999999")
print(f"| Quantidade de nós antes a tabela ser redimensionada: {tabela_hash.__len__()}")
tabela_hash.inserir("Gilda", "10101010101010101010")
print(f"| Quantidade de nós após a tabela ser redimensionada: {tabela_hash.__len__()}")
print(f"|\t\tFator de carga atual: {tabela_hash.calcular_carga()}")