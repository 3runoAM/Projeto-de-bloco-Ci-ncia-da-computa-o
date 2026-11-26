import time

from scapy.layers.dns import DNS, DNSQR
from scapy.layers.inet import IP, UDP
from scapy.sendrecv import sr1

dominio = "google.com"
servidor_dns = "8.8.8.8"

pacote = IP(dst=servidor_dns) / UDP(dport=53) / DNS(rd=1, qd=DNSQR(qname=dominio))

inicio = time.perf_counter()
response = sr1(pacote, timeout=3, verbose=0)
fim = time.perf_counter()

ips = []
dns_servers = []

if response and response.haslayer(DNS):
    dns_layer = response[DNS]

    for i in range(dns_layer.ancount):
        rr = dns_layer.an[i]
        if rr.type == 1:
            ips.append(rr.rdata)

    for i in range(dns_layer.nscount):
        rr = dns_layer.ns[i]
        if rr.type == 2:
            data = rr.rdata
            if isinstance(data, bytes):
                data = data.decode()
            dns_servers.append(data)

print(f"| Dominio consultado")
print(f"|\t {response[DNS].qd.qname.decode()}")
print(f"| IPv4 relacionados")
print(f"|\t {ips}")
print(f"| Servidores dns")
print(f"|\t {dns_servers}")
print(f"| Tempo de consulta")
print(f"|\t {inicio - fim}")
