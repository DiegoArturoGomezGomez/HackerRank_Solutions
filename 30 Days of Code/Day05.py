if __name__ == '__main__':
    n = int(input().strip())
    for i in range(11):
      print(f'{n} x {i} = {n*i}') if i != 0 else 0