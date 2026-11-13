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

palavras = ["apple", "app", "banana", "banner", "ball"]
print(f"| Inserindo palavras {palavras} na trie")
trie = Trie()
for p in palavras:
    trie.insert(p)

busca = ["apple", "app", "apology", "banana", "banner", "ball", "baker"]
print(f"| Busca por palavras {busca}")
for palavra in busca:
    if trie.search(palavra):
        print(f"|\tPalavra {palavra} está na Trie")
    else:
        print(f"|\tPalavra {palavra} não está na Trie")

prefixos  = ["ap", "ba", "ca"]
print(f"| Busca por prefixos {prefixos}")
for prefix in prefixos:
    if trie.starts_with(prefix):
        print(f"|\tPrefixo '{prefix}' encontrado na Trie")
    else:
        print(f"|\tPrefixo '{prefix}' não encontrado na Trie")
