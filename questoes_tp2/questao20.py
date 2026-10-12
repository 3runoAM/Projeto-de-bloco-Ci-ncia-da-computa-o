def quantidade_digitos(num, count=0):
    if num == 0: return 1

    if num > 0:
        return quantidade_digitos(num // 10, count + 1)

    return count

numero = 0
print(f"| Número {numero} tem {quantidade_digitos(numero)} digito")
numero = 4
print(f"| Número {numero} tem {quantidade_digitos(numero)} digito")
numero = 50
print(f"| Número {numero} tem {quantidade_digitos(numero)} digitos")
numero = 600
print(f"| Número {numero} tem {quantidade_digitos(numero)} digitos")
numero = 7000
print(f"| Número {numero} tem {quantidade_digitos(numero)} digitos")
numero = 80000
print(f"| Número {numero} tem {quantidade_digitos(numero)} digitos")


