import math

if __name__ == '__main__':
    n = int(input().strip())
    binario = []
    while n > 0:
        a = n % 2
        n = math.floor(n / 2)
        binario.append(a)

    binario.reverse()
    contador = 0
    maximo = []

    for numero in binario:
        if numero == 1:
            contador += 1
            maximo.append(contador)
        else:
            contador = 0
    print(max(maximo))