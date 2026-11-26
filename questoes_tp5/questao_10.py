from scapy.layers.inet import IP, TCP
from scapy.sendrecv import sr1

def buscar_portas_txp(host, porta_inicial, porta_final):
    if porta_inicial > porta_final:
        porta_inicial, porta_final = porta_final, porta_inicial

    for port in range(porta_inicial, porta_final+1):
        pacote = IP(dst=host) / TCP(dport=port, flags="S")
        response = sr1(pacote, timeout=1, verbose=0)

        if response:
            if response.haslayer(TCP):
                print(f"Porta {host}:{port}", end=" ")
                if response[TCP].flags == 0x12:
                    print("ABERTA")

                elif response[TCP].flags == 0x14:
                    print("FECHADA")
        else:
            print("Sem resposta (filtrada)")


host = "192.168.1.1" # input("| Digite o host\n|\t>")
porta_inicial = 80 # int(input("| Digite a porta inicial da varredura\n|\t>"))
porta_final = 443 # int(input("| Digite a porta final da varredura (deve ser menor que a porta inicial)\n|\t>"))

buscar_portas_txp(host, porta_inicial, porta_final)