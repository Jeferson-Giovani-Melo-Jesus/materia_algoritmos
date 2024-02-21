def perfeito (n):
    somaDiv= 0
    for i in range(1, (n//2)+1):
        if ((n % i) == 0):
            somaDiv = somaDiv + i

    return (n == somaDiv)

for n in range (1,501):
    if (perfeito (n)):
        print (n)