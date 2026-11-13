class No:
    def __init__(self):
        self.filhos = {}
        self.is_fim_palavra = False
        self.quantidade_palavras = 0


class Trie:
    def __init__(self):
        self.root = No()

    def insert(self, palavra):
        no = self.root
        for char in palavra:
            if char not in no.filhos:
                no.filhos[char] = No()
            no = no.filhos[char]
            no.quantidade_palavras += 1
        no.is_fim_palavra = True

    def search(self, palavra):
        no = self.root
        for char in palavra:
            if char not in no.filhos:
                return False
            no = no.filhos[char]
        return no.is_fim_palavra

    def starts_with(self, prefixo):
        no = self.root
        for char in prefixo:
            if char not in no.filhos:
                return False
            no = no.filhos[char]
        return True

    def autocomplete(self, prefixo):
        no = self.root
        sugestoes = []
        for char in prefixo:
            if char not in no.filhos:
                return []
            no = no.filhos[char]
        self.suggestions(no, prefixo, sugestoes)
        return sugestoes

    def suggestions(self, no, palavra_atual, lista_sugestoes):
        if no.is_fim_palavra:
            lista_sugestoes.append(palavra_atual)
        for char, filhos in sorted(no.filhos.items()):
            self.suggestions(filhos, palavra_atual + char, lista_sugestoes)

    def imprimir(self, no=None, prefixo=""):
        if no is None:
            no = self.root

        filhos = no.filhos.items()
        for indice, (caractere, filho) in enumerate(filhos):
            ultimo = indice == len(filhos) - 1
            marcador = "└── " if ultimo else "├── "
            palavra = caractere + (" *" if filho.is_fim_palavra else "")
            print(prefixo + marcador + palavra)
            novo_prefixo = prefixo + ("    " if ultimo else "│   ")
            self.imprimir(filho, novo_prefixo)

    def get_prefixo_frequente(self, k):
        prefixo_mais_frequente = {"prefixo": "", "contagem": 0}

        def dfs_prefixo(no, prefixo, k, nivel=0):
            if nivel == k:
                if no.quantidade_palavras > prefixo_mais_frequente["contagem"]:
                    prefixo_mais_frequente["prefixo"] = prefixo
                    prefixo_mais_frequente["contagem"] = no.quantidade_palavras

            for char, filhos in sorted(no.filhos.items()):
                dfs_prefixo(filhos, prefixo + char, k, nivel + 1)

        dfs_prefixo(self.root, "", k)

        return prefixo_mais_frequente["prefixo"], prefixo_mais_frequente["contagem"]


trie = Trie()
ips = ["192.168.1.45", "10.0.42.118", "172.16.254.3", "192.168.0.105", "10.10.5.89", "172.31.255.12", "10.240.1.77"]
print(f"| Inserindo os ips {ips} na trie")
for ip in ips:
    trie.insert(ip)

trie.imprimir()

k = 3
prefixo_mais_frequente, contagem_prefixo_frequente = trie.get_prefixo_frequente(k)
print(
    f"O ip mais frequente de tamanho {k} é {prefixo_mais_frequente} com {str(contagem_prefixo_frequente)} ips associados")

k = 6
prefixo_mais_frequente, contagem_prefixo_frequente = trie.get_prefixo_frequente(k)
print(
    f"O ip mais frequente de tamanho {k} é {prefixo_mais_frequente} com {str(contagem_prefixo_frequente)} ips associados")

k = 2
prefixo_mais_frequente, contagem_prefixo_frequente = trie.get_prefixo_frequente(k)
print(
    f"O ip mais frequente de tamanho {k} é {prefixo_mais_frequente} com {str(contagem_prefixo_frequente)} ips associados")
