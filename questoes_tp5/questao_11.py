from scapy.layers.inet import IP, TCP

host = "192.168.1.1"
porta_inicial = 80
porta_final = 443

pacotes = [
    IP(dst=host) / TCP(dport=port, flags="S") for port in range(porta_inicial, porta_final + 1)
]

for pacote in pacotes:
    print(f"| IP de origem {pacote[IP].src}")
    print(f"| IP de destino {pacote[IP].dst}")
    print(f"| Protocolo {pacote[IP].payload.name}")
    print()