from scapy.layers.l2 import ARP, Ether

subrede = "192.168.1"

pacotes = [
    Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(pdst=f"{subrede}.{i}")
    for i in range(1, 255)
]

for pacote in pacotes:
    arp = pacote[ARP]
    print(f"| IP de origem {arp.psrc}")
    print(f"| IP de destino {arp.pdst}")
    print(f"| MAC de origem {arp.hwsrc}")
    print(f"| MAC de destino {arp.hwdst}")
    print(f"| Protocolo {arp.name}")
    print()
