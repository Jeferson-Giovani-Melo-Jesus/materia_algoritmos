def fibonacci(n):
    fib_series = [0, 1]

    for i in range(2, n):
        fib_series.append(fib_series[i - 1] + fib_series[i - 2])

    return fib_series

num_terms = 100
result = fibonacci(num_terms)
print(f"Série de Fibonacci com {num_terms} termos: {result}")