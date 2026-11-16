import asyncio
import re
import socket
import threading
import time

import telnetlib3


def servidor():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    HOST = '127.0.0.1'
    PORT = 60000

    server_socket.bind((HOST, PORT))
    server_socket.listen()

    print(f"| Servidor online em {HOST}: {PORT}")

    while True:
        print(f"| Aguardando cliente...")
        client_socket, client_address = server_socket.accept()

        print("| Cliente conectado:", client_address)
        while True:
            data = client_socket.recv(1024)
            if not data: break

            data = data.decode()
            if not bool(re.match("r'^\\w+ \\d+$'", data)):
                client_socket.sendall(f"Mensagem recebida: {data}".encode())
                continue

            id_dispositivo, consumo = data.split(" ")
            if int(consumo) > 1000:
                mensagem = (f"ALERTA: Dispositivo {id_dispositivo} com consumo maior que 1000")
                client_socket.sendall(mensagem.encode())
            else:
                mensagem = (f"NORMAL: Dispositivo {id_dispositivo} com consumo normal")
                client_socket.sendall(mensagem.encode())
        client_socket.close()

async def cliente_teste():
    try:
        HOST = '127.0.0.1'
        PORT = 60000

        reader, writer = await telnetlib3.open_connection(HOST, PORT)

        print("|\tConectado")
        time.sleep(2)

        print("|\tEnviando mensagem de teste")
        writer.write("TESTE DE CONEXÃO")
        await writer.drain()

        resposta = await reader.read(1024)
        print("|\tResposta do servidor:\n\t", resposta)
        writer.close()

    except Exception as e:
        print("Erro:", e)


thread_servidor = threading.Thread(target=servidor, daemon=True)

thread_servidor.start()
asyncio.run(cliente_teste())
