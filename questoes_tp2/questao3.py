import asyncio
from random import random


async def coleta_dados_async(fila_coleta: asyncio.Queue):
    print(f"| Esperando pela coleta assíncrona")
    await asyncio.sleep(2)
    print(f"| Adicionando dados na fila de coleta")
    await fila_coleta.put(random())

async def transforma_dados_async(fila_coleta: asyncio.Queue, fila_transformacao: asyncio.Queue):
    print(f"| Esperando dados coletados na fila de coleta")
    random_num = await fila_coleta.get()
    print(f"| Dados recebidos na fila de coleta\n| Transformando dado: ({random_num} * 999) e adicionando na fila de transformação")
    await fila_transformacao.put(random_num * 999)

async def envia_dados_async(fila_transformacao: asyncio.Queue):
    print(f"| Esperando por dados transformados na fila de transformação")
    dado_transformado = await fila_transformacao.get()
    print(f"| Dados recebidos na fila de transformação\n| Enviando dado {dado_transformado}")
    await asyncio.sleep(2)
    print(f"| Dado {dado_transformado} enviado")

async def main_fila():
    fila_coleta = asyncio.Queue()
    fila_transformacao = asyncio.Queue()

    tarefas = [coleta_dados_async(fila_coleta), transforma_dados_async(fila_coleta, fila_transformacao), envia_dados_async(fila_transformacao)]
    await asyncio.gather(*tarefas)


asyncio.run(main_fila())