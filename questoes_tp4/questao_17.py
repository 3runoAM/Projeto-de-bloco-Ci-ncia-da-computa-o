import socket
import threading
import time

def servidor():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    HOST = '127.0.0.1'
    PORT = 60000

    server_socket.bind((HOST, PORT))

    print(f"| Servidor online EM {HOST}: {PORT}")
    print(f"| Aguardando cliente...")

    data, client_address = server_socket.recvfrom(1024)
    data = data.decode()

    print("| Mensagem recebida:", data)
    server_socket.sendto(data.upper().encode(), client_address)

    server_socket.close()
    print("| Conexão encerrada")

def cliente():
    time.sleep(3)

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    SERVER_IP = '127.0.0.1'
    SERVER_PORT = 60000

    mensagem = "Olá servidor"
    client_socket.sendto(mensagem.encode(), (SERVER_IP, SERVER_PORT))

    data, server_address = client_socket.recvfrom(1024)
    print("| Resposta do servidor:", data.decode())

    client_socket.close()


thread_servidor = threading.Thread(target=servidor)
thread_cliente = threading.Thread(target=cliente)

thread_servidor.start()
thread_cliente.start()

thread_servidor.join()
thread_cliente.join()