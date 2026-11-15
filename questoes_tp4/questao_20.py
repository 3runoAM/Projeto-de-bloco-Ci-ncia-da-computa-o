import socket
import threading
import time

def servidor(finalizar_chat_flag):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    HOST = '127.0.0.1'
    PORT = 60000

    server_socket.bind((HOST, PORT))
    server_socket.listen()

    print(f"| Servidor online em {HOST}: {PORT}")
    print(f"| Aguardando cliente...")

    client_socket, client_address = server_socket.accept()

    while True:
        data = client_socket.recv(1024)
        if not data: break

        data = data.decode()
        print(f"| Cliente {client_address} diz: {data}")

        if data == "sair":
            finalizar_chat_flag.set()
            client_socket.close()
            break

        mensagem_servidor = input("Servidor escreve: > ")

        if mensagem_servidor == "sair":
            finalizar_chat_flag.set()
            client_socket.close()
            break

        client_socket.send(mensagem_servidor.encode())

    server_socket.close()


def cliente(finalizar_chat_flag):
    time.sleep(3)

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    SERVER_IP = '127.0.0.1'
    SERVER_PORT = 60000

    client_socket.connect((SERVER_IP, SERVER_PORT))
    print(f"|\tConectado ao servidor em {SERVER_IP}:{SERVER_PORT}")

    while True:
        if finalizar_chat_flag.is_set():
            client_socket.close()
            break

        mensagem_cliente = input("Cliente escreve: ")
        if mensagem_cliente == "sair":
            finalizar_chat_flag.set()
            client_socket.close()
            break

        client_socket.send(mensagem_cliente.encode())
        resposta = client_socket.recv(1024)
        print(f"|\tServidor ({SERVER_IP}:{SERVER_PORT}) diz: {resposta.decode()}")

    client_socket.close()


finalizar_chat_flag = threading.Event()

thread_servidor = threading.Thread(target=servidor, args=(finalizar_chat_flag,))
thread_cliente = threading.Thread(target=cliente, args=(finalizar_chat_flag,))

thread_servidor.start()
thread_cliente.start()

thread_servidor.join()
thread_cliente.join()