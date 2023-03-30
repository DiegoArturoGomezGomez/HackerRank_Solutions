n = int(input().strip())
a = list(map(int, input().rstrip().split()))
swaps = 0

while not a == sorted(a):
    for num in range(len(a) - 1):
        if a[num] > a[num + 1]:
            a[num], a[num + 1] = a[num + 1], a[num]
            swaps += 1

print(f'Array is sorted in {swaps} swaps.')
print(f'First Element: {a[0]}')
print(f'Last Element: {a[-1]}')