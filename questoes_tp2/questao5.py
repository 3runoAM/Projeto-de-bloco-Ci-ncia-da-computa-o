import asyncio
import time
from asyncio import Queue

class Processo:
    def __init__(self, nome_cliente, conteudo_processo):
        self.cliente = nome_cliente
        self.processo = conteudo_processo

async def servidor(fila_processos):
    print(f"| Servidor iniciado")
    while True:
        try:
            processo = await asyncio.wait_for(fila_processos.get(), timeout=10)
            print(f"| Processo recebido do cliente {processo.cliente}\n|\t{processo.processo}")
        except asyncio.TimeoutError:
            print(f"| Nenhuma requisição recebida nos últimos 10 segundos, encerrando...")
            break

async def cliente_A(fila_processos):
    processo_a1 = Processo("Cliente A", "Hello world! Aqui é o processo do cliente A")
    processo_a2 = Processo("Cliente A", "Estou enviando esse processo pela fila de processos")
    processo_a3 = Processo("Cliente A", "Essa a minha mensagem final! Xeru!")

    processos = [processo_a1, processo_a2, processo_a3]
    for i in range(len(processos)):
        await asyncio.sleep(3)
        await fila_processos.put(processos[i])


async def cliente_B(fila_processos):
    processo_b1 = Processo("Cliente B", "Ola! Aqui é o cliente B, enviando um novo processo para o servidor")
    processo_b2 = Processo("Cliente B", "Está chegando um processo meu aí?")
    processo_b3 = Processo("Cliente B", "Essa a minha mensagem de encerramento! Adeus")

    processos = [processo_b1, processo_b2, processo_b3]
    for i in range(len(processos)):
        await asyncio.sleep(4)
        await fila_processos.put(processos[i])

async def cliente_C(fila_processos):
    processo_b1 = Processo("Cliente C", "Oie! Essa é o meu primeiro processo no servidor, sou o cliente C")
    processo_b2 = Processo("Cliente C", "Essa é a minha segunda mensagem, estou com fome, comi nada hoje, oh")
    processo_b3 = Processo("Cliente C", "Agora que comi, essa é a minha mensagem final, tchau, tchau...")

    processos = [processo_b1, processo_b2, processo_b3]
    for i in range(len(processos)):
        await asyncio.sleep(6)
        await fila_processos.put(processos[i])

async def main_servidor():
    fila_processos = asyncio.Queue()

    tarefas = [servidor(fila_processos), cliente_A(fila_processos), cliente_B(fila_processos), cliente_C(fila_processos)]

    await asyncio.gather(*tarefas)

asyncio.run(main_servidor())