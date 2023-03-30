N = int(input().strip())
names = []

for N_itr in range(N):
    first_multiple_input = input().rstrip().split()
    firstName = first_multiple_input[0]
    emailID = first_multiple_input[1]

    if '@gmail' in emailID:
        names.append(firstName)

print('\n'.join(map(str, sorted(names))))

