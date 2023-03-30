n = int(input())
phoneBook = dict()

for i in range(n):
    name, phone = input().strip().split()
    phoneBook[name] = phone

while True:
    try:
        a = input()
        if a in phoneBook:
            print(a + "=" + phoneBook.get(a))
        else:
            print("Not found")
    except EOFError:
        break
