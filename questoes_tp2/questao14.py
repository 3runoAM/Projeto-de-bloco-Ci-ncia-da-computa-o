class No:
    def __init__(self, valor):
        self.valor = valor
        self.next = None
        self.prev = None

class ListaDuplamenteEncadeada:
    def __init__(self):
        self.head = None
        self.tail = None
        self.tamanho_lista = 0

    def inserir_comeco(self, valor):
        novo_no = No(valor)
        if self.head is None:
            self.head = self.tail = novo_no
            self.tamanho_lista+=1
            return

        novo_no.next = self.head
        self.head.prev = novo_no
        self.head = novo_no
        self.tamanho_lista += 1

    def remover_comeco(self):
        if self.head is None: return None
        valor = self.head.valor
        self.head = self.head.next

        if self.head:
            self.head.prev = None
        else:
            self.tail = None

        self.tamanho_lista -= 1
        return valor

    def inserir_final(self, valor):
        novo_no = No(valor)
        if self.tail is None:
            self.tail = self.head = novo_no
            self.tamanho_lista += 1
            return

        novo_no.prev = self.tail
        self.tail.next = novo_no
        self.tail = novo_no
        self.tamanho_lista += 1

    def remover_final(self):
        if self.tail is None: return None
        valor = self.tail.valor
        self.tail = self.tail.prev

        if self.tail:
            self.tail.next = None
        else:
            self.head = None

        self.tamanho_lista -= 1
        return valor

    def remover(self, valor):
        if self.head is None: return None

        atual = self.head
        while atual:
            if atual.valor == valor:
                if atual == self.head:
                    return self.remover_comeco()
                elif atual == self.tail:
                    return self.remover_final()
                else:
                    atual.prev.next = atual.next
                    atual.next.prev = atual.prev
                    self.tamanho_lista -= 1
                    return valor
            atual = atual.next
        return None

    def exibir(self):
        string = "\n\t\t Head -> "
        if self.head is None:
            print(string + "| None | <- Tail\n")
            return

        atual = self.head
        while atual:
            string += f"| {atual.valor} |"
            if atual.next:
                string += " <-> "
            atual = atual.next
        string += " <- Tail\n"

        print(string)

array = [15, 456, 312, 6748, 546, 984, 312, 542]
lista = ListaDuplamenteEncadeada()
for i in array:
    lista.inserir_final(i)

print(f"| Lista duplamente encadeada")
lista.exibir()

print(f"| Removendo elemento 312")
lista.remover(312)
lista.exibir()