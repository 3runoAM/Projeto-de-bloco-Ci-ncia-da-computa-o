import socket
import threading
import time

def servidor():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    HOST = '127.0.0.1'
    PORT = 60000

    server_socket.bind((HOST, PORT))
    server_socket.listen(1)

    print(f"| Servidor online EM {HOST}:{PORT}")
    print(f"| Aguardando cliente...")
    client_socket, client_address = server_socket.accept()

    print("| Cliente conectado:", client_address)

    data = client_socket.recv(1024)
    print("| Mensagem recebida:", data.decode())

    resposta = "Mensagem recebida!"
    client_socket.sendall(resposta.encode())

    client_socket.close()
    server_socket.close()
    print("| Conexão encerrada")


def cliente():
    time.sleep(3)

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    SERVER_IP = '127.0.0.1'
    SERVER_PORT = 60000

    print(f"| Conectando ao servidor em {SERVER_IP}:{SERVER_PORT}")

    client_socket.connect((SERVER_IP, SERVER_PORT))
    print("| Conectado ao servidor")

    mensagem = "Olá servidor"
    client_socket.sendall(mensagem.encode())
    print("| Mensagem enviada")

    resposta = client_socket.recv(1024)
    print("| Resposta do servidor:", resposta.decode())

    client_socket.close()


thread_servidor = threading.Thread(target=servidor)
thread_cliente = threading.Thread(target=cliente)

thread_servidor.start()
thread_cliente.start()

thread_servidor.join()
thread_cliente.join()