def torreDeHanoi(n, origem, destino, auxiliar):
    if n == 1:
        print(f'Mover disco {n} de {origem} para {destino}')
        return
    torreDeHanoi(n - 1, origem, auxiliar, destino)
    print(f'Mover disco {n} de {origem} para {destino}')
    torreDeHanoi(n - 1, auxiliar, destino, origem)

print(f"| Movendo 1 disco")
torreDeHanoi(1, 'ORIGEM', 'DESTINO', 'AUXILIAR')
print()

print(f"| Movendo 2 discos")
torreDeHanoi(2, 'ORIGEM', 'DESTINO', 'AUXILIAR')
print()

print(f"| Movendo 4 discos")
torreDeHanoi(4, 'ORIGEM', 'DESTINO', 'AUXILIAR')
print()

print(f"| Movendo 5 discos")
torreDeHanoi(5, 'ORIGEM', 'DESTINO', 'AUXILIAR')