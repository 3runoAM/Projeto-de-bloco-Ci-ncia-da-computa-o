class Aviao:
    def __init__(self, id, tempo_solicitacao, combustivel, tempo_pouso):
        self.id = id
        self.tempo_solicitacao = tempo_solicitacao
        self.combustivel = combustivel
        self.tempo_pouso = tempo_pouso

    def aviao_tupla(self):
        return (self.combustivel, self.tempo_solicitacao, self.tempo_pouso)

class MinHeap:
    def __init__(self):
        self._heap = []

    def _get_pai_index(self, index):
        return (index - 1) // 2

    def _get_filho_esquerdo_index(self, index):
        return 2 * index + 1

    def _get_filho_direito_index(self, index):
        return 2 * index + 2

    def _troca(self, i, j):
        self._heap[i], self._heap[j] = self._heap[j], self._heap[i]

    def sift_up(self, index):
        while index > 0:
            pai_index = self._get_pai_index(index)
            if self._heap[index].aviao_tupla() < self._heap[pai_index].aviao_tupla():
                self._troca(index, pai_index)
                index = pai_index
            else:
                break

    def sift_down(self, index):
        ultimo_index = len(self._heap) - 1
        while True:
            filhoE_index = self._get_filho_esquerdo_index(index)
            filhoD_index = self._get_filho_direito_index(index)
            menor = index

            if filhoE_index <= ultimo_index and self._heap[filhoE_index].aviao_tupla() < self._heap[menor].aviao_tupla():
                menor = filhoE_index

            if filhoD_index <= ultimo_index and self._heap[filhoD_index].aviao_tupla() < self._heap[menor].aviao_tupla():
                menor = filhoD_index

            if menor != index:
                self._troca(index, menor)
                index = menor
            else:
                break

    def inserir(self, valor):
        self._heap.append(valor)
        self.sift_up(len(self._heap) - 1)

    def extrair_min(self):
        if not self._heap:
            return None
        if len(self._heap) == 1:
            return self._heap.pop()
        raiz = self._heap[0]
        self._heap[0] = self._heap.pop()
        self.sift_down(0)
        return raiz

    def imprimir(self):
        tam = self.__len__()
        index = 0
        while index < tam:
            aviao = self._heap[index]
            id = aviao.id
            tempo_solicitacao = aviao.tempo_solicitacao
            combustivel = aviao.combustivel
            tempo_pouso = aviao.tempo_pouso
            print(
                f"|\tAVIÃO: {id}, Tempo de Solicitação: {tempo_solicitacao}, Combustível: {combustivel}, Tempo de Pouso: {tempo_pouso}")
            index += 1

    def _olhar(self):
        if self._heap:
            return self._heap[0]
        return None

    def __len__(self):
        return len(self._heap)


class FilaDePrioridade:
    def __init__(self):
        self._min_heap = MinHeap()
        self.id_count = 10
        self.sem_combustivel = set()

    def enqueue(self, tempo_solicitacao, combustivel, tempo_pouso):
        self.id_count += 1
        self._min_heap.inserir(Aviao(self.id_count, tempo_solicitacao, combustivel, tempo_pouso))

    def dequeue(self):
        aviao = self._min_heap.extrair_min()
        if aviao:
            for tempo_pouso in range(aviao.tempo_pouso):
                for aviao_no_ar in self._min_heap._heap:
                    aviao_no_ar.combustivel -= 1
                    if aviao_no_ar.combustivel <= 0 and aviao_no_ar not in self.sem_combustivel:
                        self.sem_combustivel.add(aviao_no_ar)
                        continue
            return aviao
        return None

    def olhar(self):
        aviao = self._min_heap._olhar()
        if aviao:
            return aviao
        return None

    def mostrar_avioes_sem_combustivel(self):
        print("| Aviões sem combustível:")
        for aviao in self.sem_combustivel:
            id = aviao.id
            tempo_solicitacao = aviao.tempo_solicitacao
            combustivel = aviao.combustivel
            tempo_pouso = aviao.tempo_pouso
            print(f"|\tAVIÃO: {id}, Tempo de Solicitação: {tempo_solicitacao}, Combustível: {combustivel}, Tempo de Pouso: {tempo_pouso}")


fila = FilaDePrioridade()


fila.enqueue(4, 2, 3)  # Combustível alto (não fica sem)
fila.enqueue(3, 2, 2)   # Combustível crítico
fila.enqueue(2, 5, 4) # Combustível muito alto (não fica sem)
fila.enqueue(2, 5, 2)   # Pouco combustível (quase crítico)
fila.enqueue(1, 9, 3)   # tempo_solicitacao, combustivel, tempo_pouso

print("| Aeropoto com fila de prioridade")
fila._min_heap.imprimir()

print("| Pousando avião...")

aviao = fila.dequeue()
if aviao:
    print(f"|\tAVIÃO: {aviao.id}, Tempo de Solicitação: {aviao.tempo_solicitacao}, Combustível: {aviao.combustivel}, Tempo de Pouso: {aviao.tempo_pouso}")

fila.mostrar_avioes_sem_combustivel()

print("| Pousando avião...")

aviao = fila.dequeue()
if aviao:
    print(f"|\tAVIÃO: {aviao.id}, Tempo de Solicitação: {aviao.tempo_solicitacao}, Combustível: {aviao.combustivel}, Tempo de Pouso: {aviao.tempo_pouso}")

fila.mostrar_avioes_sem_combustivel()
