from numba import jit, prange

@jit(nopython=True, parallel=True)
def conta_primos_ate_n_paralelo(n):
    count = 0

    for num in prange(1, n+1):
        eh_primo = True
        for divisor in range(1, num):
            if num % divisor == 0 and divisor > 1:
                eh_primo = False
                break
        if eh_primo and num > 1:
            count += 1

    return count



n = 10
primos_count = conta_primos_ate_n_paralelo(n)
print(f"| Número de primos entre 0 e {n} é de {primos_count}")

n = 20
primos_count = conta_primos_ate_n_paralelo(n)
print(f"| Número de primos entre 0 e {n} é de {primos_count}")