def bitwiseAnd(N, K):
    maximo = 0
    for primeros in range(1, N):
        for segundos in range(primeros+1, N+1):
            bitAnd = primeros&segundos
            if bitAnd > maximo and bitAnd < K:
                maximo = bitAnd
                if bitAnd == K - 1:
                    return bitAnd
    return maximo


t = int(input().strip())
for t_itr in range(t):
    first_multiple_input = input().rstrip().split()
    count = int(first_multiple_input[0])
    lim = int(first_multiple_input[1])
    print(bitwiseAnd(count, lim))
