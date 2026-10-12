import asyncio
import time
from random import random

async def coleta_dados_async():
    print(f"| Começando coleta assíncrona usando sleep bloqueante")
    time.sleep(10)
    dado = random()
    print(f"| Retornando dado da coleta {dado}")
    return dado

async def funcao_segundos():
    print("\n|\tComeçando função de segundos")
    for i in range(1,21):
        await asyncio.sleep(1)
        print(f"| Função segundos: segundo {i}")
    print("|\tFunção segundos acabou")


async def main_bloqueante():
    tarefas = [coleta_dados_async(), funcao_segundos()]

    dado = await asyncio.gather(*tarefas)


async def coleta_dados_async_thread():
    print(f"| Começando coleta assíncrona usando sleep bloqueante, mas com to_thread")
    await asyncio.to_thread(time.sleep, 10)
    dado = random()
    print(f"| Retornando dado da coleta {dado}")
    return dado

async def main_com_thread():
    tarefas = [coleta_dados_async_thread(), funcao_segundos()]
    dado = await asyncio.gather(*tarefas)


print("| Exemplo bloqueante entre função assíncrona e thread")
asyncio.run(main_bloqueante())

print("\n| Exemplo não bloqueante com to_thread")
asyncio.run(main_com_thread())