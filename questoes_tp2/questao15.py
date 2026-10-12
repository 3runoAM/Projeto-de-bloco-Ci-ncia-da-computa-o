import asyncio
import time

class Processo:
    def __init__(self, nome, tempo_conclusao):
        self.nome = nome
        self.tempo_conclusao = tempo_conclusao
        self.concluido = False

    async def executar_processo(self):
        self.concluido = False
        print(f"| Executando {self.nome}")
        await asyncio.sleep(self.tempo_conclusao)
        self.concluido = True

class Fila:
    def __init__(self, tamanho_max=5):
        self.tamanho_max = tamanho_max
        self.processos = [""] * tamanho_max
        self.slice_tempo = 5
        self.tamanho_atual = 0
        self.inicio = 0
        self.fim = 0

    def enfileirar(self, processo):
        if self.tamanho_atual == self.tamanho_max: raise Exception("Fila cheia, não cabem mais processos")

        self.processos[self.fim] = processo

        self.fim = (self.fim + 1) % self.tamanho_max
        self.tamanho_atual += 1

    def desenfileirar(self):
        if self.tamanho_atual == 0: raise Exception("Fila vazia, não há clientes para sair")

        print(f"| Desenfileirando processo")
        processo = self.processos[self.inicio]
        self.processos[self.inicio] = ""
        self.inicio = (self.inicio + 1) % self.tamanho_max
        self.tamanho_atual -= 1
        print(f"|\tProcesso {processo.nome}:\n|\t\tTempo de conclusão: {processo.tempo_conclusao}s")

        return processo

    def exibir_fila(self):
        if self.tamanho_atual == 0:
            print("Fila vazia")
            print("---------------------------------------------")
            return

        for i in range(self.tamanho_atual):
            id_circular = (self.inicio + i) % self.tamanho_max
            processo = self.processos[id_circular]
            if processo != "":
                print(f"|\tProcesso {processo.nome}:\n\t\tTempo de conclusão: {processo.tempo_conclusao}\n\t\tConcluído: {processo.concluido}")

    async def escalonar_round_robin(self):
        print("| Começando escalonamento round robin")
        rounds = 0
        while self.tamanho_atual > 0:
            try:
                processo = self.desenfileirar()
                try:
                    await asyncio.wait_for(processo.executar_processo(), timeout=self.slice_tempo)
                except asyncio.TimeoutError:
                    pass

                if not processo.concluido:
                    print("|\tProcesso não concluiu a tempo, volta para a fila")
                    tempo_restante = processo.tempo_conclusao - self.slice_tempo
                    if tempo_restante >= 0:
                        processo.tempo_conclusao = tempo_restante

                    self.enfileirar(processo)
                else:
                    print(f"|\tProcesso concluído: {processo.nome}")

                rounds += 1
            except Exception as e:
                print(f"Erro ao desenfileirar: {e}")
                return

processo_A = Processo("Processo A", 3)
processo_B = Processo("Processo B", 8)
processo_C = Processo("Processo C", 2)
processo_D = Processo("Processo D", 10)



fila = Fila(5)
fila.enfileirar(processo_A)
fila.enfileirar(processo_B)
fila.enfileirar(processo_C)
fila.enfileirar(processo_D)

asyncio.run(fila.escalonar_round_robin())