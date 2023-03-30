class Difference:
    def __init__(self, a):
        self.__elements = a
        self.maximumDifference = 0

    def computeDifference(self):
        self.maximumDifference = 0
        for i in self.__elements:
            for j in self.__elements:
                self.maximumDifference = abs(i - j) if abs(i-j) > self.maximumDifference else self.maximumDifference

_ = input()
a = [int(e) for e in input().split(' ')]
d = Difference(a)
d.computeDifference()
print(d.maximumDifference)