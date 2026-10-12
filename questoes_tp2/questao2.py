import asyncio
import time

def simular_funcao_custosa():
    print("|\tComeçando função custosa")
    time.sleep(20)
    print(f"| Função custosa acabou")

async def funcao_segundos():
    print("\n|\tComeçando função de segundos")
    for i in range(1,21):
        await asyncio.sleep(1)
        print(f"| Função segundos: segundo {i}")
    print("|\tFunção segundos acabou")

async def main_thread():
    print("|\tChamando função custosa dentro de uma thread")
    await asyncio.gather(asyncio.to_thread(simular_funcao_custosa), funcao_segundos())
    print("|\tFunção custosa dentro da thread acabou")
    print("------------")
    print("| Chamando função custosa fora de uma thread")
    simular_funcao_custosa()
    await funcao_segundos()

asyncio.run(main_thread())