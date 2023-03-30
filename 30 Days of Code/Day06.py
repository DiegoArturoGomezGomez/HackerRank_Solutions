T = int(input())
listA = ''
listB = ''

for i in range(T):
    S = input()
    listA = ''
    listB = ''
    for j in range(len(S)):
        if j % 2 == 0:
            listA += S[j]
        else:
            listB += S[j]
    print(listA, listB)