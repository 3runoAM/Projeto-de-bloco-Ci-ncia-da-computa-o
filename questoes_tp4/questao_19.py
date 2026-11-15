import socket
import threading
import time

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
            id_dispositivo, consumo = data.decode().split(" ")
            if int(consumo) > 1000:
                mensagem = (f"ALERTA: Dispositivo {id_dispositivo} com consumo maior que 1000")
                client_socket.sendall(mensagem.encode())
            else:
                mensagem = (f"NORMAL: Dispositivo {id_dispositivo} com consumo normal")
                client_socket.sendall(mensagem.encode())

        client_socket.close()

def dispositivoA():
    time.sleep(3)

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    SERVER_IP = '127.0.0.1'
    SERVER_PORT = 60000

    print(f"| Conectando ao servidor em {SERVER_IP}:{SERVER_PORT}")

    client_socket.connect((SERVER_IP, SERVER_PORT))
    print("| DISPOSITIVO A Conectado ao servidor")

    mensagem = "DISPOSITIVO_A 400"
    client_socket.sendall(mensagem.encode())
    print("| Mensagem enviada")

    resposta = client_socket.recv(1024)
    print("| Resposta do servidor:", resposta.decode())

    client_socket.close()

def dispositivoB():
    time.sleep(6)
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    SERVER_IP = '127.0.0.1'
    SERVER_PORT = 60000

    print(f"| Conectando ao servidor em {SERVER_IP}:{SERVER_PORT}")

    client_socket.connect((SERVER_IP, SERVER_PORT))
    print("| DISPOSITIVO B Conectado ao servidor")

    mensagem = "DISPOSITIVO_B 99000"
    client_socket.sendall(mensagem.encode())
    print("| Mensagem enviada")

    resposta = client_socket.recv(1024)
    print("| Resposta do servidor:", resposta.decode())

    client_socket.close()

def dispositivoC():
    time.sleep(9)

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    SERVER_IP = '127.0.0.1'
    SERVER_PORT = 60000

    print(f"| Conectando ao servidor em {SERVER_IP}:{SERVER_PORT}")

    client_socket.connect((SERVER_IP, SERVER_PORT))
    print("| DISPOSITIVO C Conectado ao servidor")

    mensagem = "DISPOSITIVO_C 1000"
    client_socket.sendall(mensagem.encode())

    resposta = client_socket.recv(1024)
    print("| Resposta do servidor:", resposta.decode())

    client_socket.close()


thread_servidor = threading.Thread(target=servidor, daemon=True)
thread_dA = threading.Thread(target=dispositivoA)
thread_dB = threading.Thread(target=dispositivoB)
thread_dC = threading.Thread(target=dispositivoC)

thread_servidor.start()
thread_dA.start()
thread_dB.start()
thread_dC.start()

thread_dA.join()
thread_dB.join()
thread_dC.join()