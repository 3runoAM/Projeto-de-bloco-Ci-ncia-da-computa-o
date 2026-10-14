class No:
    def __init__(self, valor=""):
        self.valor = valor
        self.filhos = {}
        self.eh_fim_da_palavra = False


class Trie:
    def __init__(self):
        self.raiz = No()

    def inserir(self, palavra):
        ip, mascara = palavra.split("/")
        octetos = ip.split(".")[:int(mascara) // 8]

        no_atual = self.raiz
        for char in octetos:
            if char not in no_atual.filhos:
                no_atual.filhos[char] = No()
            no_atual = no_atual.filhos[char]
        no_atual.valor = palavra
        no_atual.eh_fim_da_palavra = True

    def buscar(self, palavra):
        ip, mascara = palavra.split("/")
        octetos = ip.split(".")[:int(mascara) // 8]

        no_atual = self.raiz
        for char in octetos:
            if char not in no_atual.filhos:
                return False
            no_atual = no_atual.filhos[char]
        return no_atual.eh_fim_da_palavra

    def prefixo_maximo(self, palavra):
        print("| Buscando por prefixo máximo")

        no_atual = self.raiz
        ultimo_match = None
        for char in palavra.split(".")[:-1]:
            if char not in no_atual.filhos:
                break
            no_atual = no_atual.filhos[char]
            if no_atual.eh_fim_da_palavra:
                ultimo_match = no_atual.valor

        print(f"| Para {busca} {f'sugerimos {ultimo_match}' if ultimo_match else 'não encontramos nenhuma palavra parecida'}")

    def exibir_arvore(self):
        def busca_em_profundidade(no, prefixo=""):
            if no.eh_fim_da_palavra:
                print(f"|\t{prefixo[1:]}")
            for valor, filhos in no.filhos.items():
                busca_em_profundidade(filhos, prefixo + "." + valor )

        print("| Exibindo palavras encontradas na Trie")
        busca_em_profundidade(self.raiz)



trieDePrefixos = Trie()

trieDePrefixos.inserir("192.168.1.0/24")
trieDePrefixos.inserir("10.0.0.0/8")

trieDePrefixos.exibir_arvore()
print("|--")
busca = "192.168.1.10"
trieDePrefixos.prefixo_maximo(busca)
print("|---")
busca = "10.10.10.10"
trieDePrefixos.prefixo_maximo(busca)
print("|---")
busca = "00.10.10.10"
trieDePrefixos.prefixo_maximo(busca)