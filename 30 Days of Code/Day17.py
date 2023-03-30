class Calculator():
    def power(self, n, p):
        newValue = 1
        if n < 0 or p < 0:
            raise Exception('n and p should be non-negative')
        else:
            for index in range(p):
                newValue *= n
        return newValue


myCalculator = Calculator()
T = int(input())
for i in range(T):
    n, p = map(int, input().split())
    try:
        ans = myCalculator.power(n, p)
        print(ans)
    except Exception as e:
        print(e)