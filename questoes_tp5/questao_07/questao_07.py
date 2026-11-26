# import subprocess
# PARA CRIAR O CERTIFICADO E A CHAVE DO TSL
# subprocess.run([
#     "openssl", "req", "-x509", "-newkey", "rsa:2048", "-nodes",
#     "-keyout", "key.pem", "-out", "cert.pem", "-days", "365",
#     "-subj", "/CN=localhost",
#     "-addext", "subjectAltName=DNS:localhost,IP:127.0.0.1",
# ])

import socket
import ssl
import threading
import time

def servidor():
    contexto = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    contexto.load_cert_chain(certfile="cert.pem", keyfile="key.pem")

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    HOST = '127.0.0.1'
    PORT = 60000

    server_socket.bind((HOST, PORT))
    server_socket.listen(1)

    print(f"| Servidor online EM {HOST}: {PORT}")
    print(f"| Aguardando cliente...")
    client_socket, client_address = server_socket.accept()

    print("| Cliente conectado:", client_address)
    tls_client_socket = contexto.wrap_socket(client_socket, server_side=True)

    data = tls_client_socket.recv(1024)
    print("| Mensagem recebida:", data.decode())

    resposta = "Mensagem recebida!"
    tls_client_socket.sendall(resposta.encode())

    tls_client_socket.close()
    server_socket.close()
    print("| Conexão encerrada")


def cliente():
    time.sleep(3)

    contexto = ssl.create_default_context()
    contexto.load_verify_locations("cert.pem")

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    SERVER_IP = '127.0.0.1'
    SERVER_PORT = 60000

    print(f"| Conectando ao servidor em {SERVER_IP}:{SERVER_PORT}")

    client_socket.connect((SERVER_IP, SERVER_PORT))
    print("\n| Conectado ao servidor")

    tls_socket = contexto.wrap_socket(client_socket, server_hostname="localhost")

    mensagem = "Olá servidor"
    tls_socket.sendall(mensagem.encode())
    print("| Mensagem enviada")

    resposta = tls_socket.recv(1024)
    print("| Resposta do servidor:", resposta.decode())

    tls_socket.close()


thread_servidor = threading.Thread(target=servidor)
thread_cliente = threading.Thread(target=cliente)

thread_servidor.start()
thread_cliente.start()

thread_servidor.join()
thread_cliente.join()