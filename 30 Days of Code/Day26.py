def calculo_fecha(returned, due):
    if returned[2] < due[2]:
        print(0)
        return

    while True:
        if returned[2] > due[2]:
            print(10000)
            return
        elif returned[1] > due[1]:
            print(500 * (returned[1]-due[1]))
            return
        elif returned[0] > due[0]:
            print(15 * (returned[0]-due[0]))
            return
        print(0)
        return

returned = list(map(int, input().rstrip().split()))
due = list(map(int, input().rstrip().split()))

calculo_fecha(returned, due)