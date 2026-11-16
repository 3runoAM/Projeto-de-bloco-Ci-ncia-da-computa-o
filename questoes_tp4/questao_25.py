from urllib import request

host_url = "http://www.google.com"
print(f"| Diagnóstico {host_url}")

try:
    request_teste = request.urlopen(host_url, timeout=5)
    print("| Servidor ativo")
    print(f"|\tStatus {request_teste.status} {request_teste.reason}")
    print(f"|\tServidor {request_teste.headers['Server']}")
    print(f"|\tServidor {request_teste.getheaders()}")
    print(f"|\tContent type {request_teste.headers['Content-Type']}")
    ip = request_teste.fp.raw._sock.getpeername()[0]
    porta = request_teste.fp.raw._sock.getpeername()[1]
    print(f"|\tIp {ip}")
    print(f"|\tPorta {porta}")
except Exception as e:
    print("Servidor com problema:", e)