import math


class NewInt(int):

    def __init__(self, max):
        super().__init__()
        self.max = max

    def isPerfectSquare(x):
        s = int(math.sqrt(x))
        return s * s == x

    def is_fibonacci(n):
        return n.isPerfectSquare(5 * n * n + 4) or n.isPerfectSquare(5 * n * n - 4)

    for i in range(0, 1001):
        if (is_fibonacci(i) == True):
            list_variable = [i]
        else:
            print(i, "False")

