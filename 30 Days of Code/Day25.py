from math import sqrt

def prime(num):
    if num == 1:
        return 'Not prime'
    else:
        for div in range(2, round(sqrt(num)) + 1):
            if num % div == 0:
                return 'Not prime'
        return 'Prime'

arreglo = []
for time in range(int(input())):
    arreglo.append(int(input()))

for time in arreglo:
    print(prime(time))
