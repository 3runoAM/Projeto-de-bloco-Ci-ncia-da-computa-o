def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        global chamadas_fib
        chamadas_fib += 2
        return fibonacci(n-1) + fibonacci(n-2)

def fibonacci_memo(n, memoria):
    if n in memoria:
        return memoria[n]
    if n == 0:
        return
    elif n == 1:
        return 1
    else:
        global chamadas_memo
        chamadas_memo += 2
        memoria[n] = fibonacci_memo(n-1, memoria) + fibonacci_memo(n-2, memoria)
        return memoria[n]

chamadas_fib = 0
print(f"| Calculando o numero na posição 10 sequência fibonacci")
print(f"| O numero na posição 10 é {fibonacci(10)}")
print(f"| Número de chamadas recursivas {chamadas_fib}")
print("|-----")

chamadas_memo = 0
print(f"| Calculando o numero na posição 10 sequência fibonacci com memoização")
print(f"| O numero na posição 10 {fibonacci_memo(10, {})}")
print(f"| Número de chamadas recursivas {chamadas_memo}")
