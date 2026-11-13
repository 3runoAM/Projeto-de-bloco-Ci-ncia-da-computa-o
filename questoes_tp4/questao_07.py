class No:
    def __init__(self):
        self.filhos = {}
        self.is_fim_palavra = False

class Trie:
    def __init__(self):
        self.root = No()

    def insert(self, palavra):
        no = self.root
        for char in palavra:
            if char not in no.filhos:
                no.filhos[char] = No()
            no = no.filhos[char]
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


palavras = ["apple", "app", "banana", "banner", "ball"]
print(f"| Inserindo palavras {palavras} na trie")
trie = Trie()
for p in palavras:
    trie.insert(p)

print()
trie.imprimir()