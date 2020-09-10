import math


class NewInt1(int):

    def __init__(self):
        self.int_list = list(range(0, 100000))

    def isPerfectSquare(self, x):
        s = int(math.sqrt(x))
        return s * s == x

    def is_fibonacci(self, n):
        return self.isPerfectSquare(5 * n * n + 4) or self.isPerfectSquare(5 * n * n - 4)


newClass = NewInt1()


def fibo(n):
    fib_set = []
    a, b = 0, 1
    while b < n:
        a, b = b, a + b
        fib_set.append(a)
    return fib_set
# fib_set = {int for int in NewInt1.is_fibonacci(int)}
# comprehension_List = [int for int in newClass.int_list if new_set(int)]
