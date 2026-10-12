import asyncio
import time
from random import random

async def coleta_dados_async(numero_coleta):
    print(f"| Começando coleta assíncrona {numero_coleta}")
    await asyncio.sleep(2)
    print(f"| Retornando dados da coleta assíncrona {numero_coleta}")
    return random()

async def main():
    tarefas = []
    for i in range(5):
        tarefas.append(coleta_dados_async(i))

    comeco = time.perf_counter()
    dados = await asyncio.gather(*tarefas)
    fim = time.perf_counter()

    print(f"| Coleta assíncrona terminou em {fim - comeco} segundos")
    print(f"| {dados}")
    print()

asyncio.run(main())

print("---------")

def coleta_dados(numero_coleta):
    print(f"| Começando coleta {numero_coleta}")
    time.sleep(2)
    print(f"| Retornando dados da coleta {numero_coleta}")
    return random()

dados = []
comeco = time.perf_counter()
for i in range(5):
    dados.append(coleta_dados(i))
fim = time.perf_counter()

print(f"| Coleta sequencial terminou em {fim - comeco} segundos")
print(f"| {dados}")