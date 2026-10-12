def conta_primos_ate_n(n):
    count = 0

    for num in range(1, n+1):
        eh_primo = True
        for divisor in range(1, num):
            if num % divisor == 0 and divisor > 1:
                eh_primo = False
                break
        if eh_primo and num > 1:
            print(f"| {num} é primo")
            count += 1

    return count


n = 10
primos_count = conta_primos_ate_n(n)
print(f"|\tNúmero de primos entre 0 e {n} é de {primos_count}")


n = 20
primos_count = conta_primos_ate_n(n)
print(f"|\tNúmero de primos entre 0 e {n} é de {primos_count}")

