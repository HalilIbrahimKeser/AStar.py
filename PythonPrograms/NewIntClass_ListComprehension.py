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

int_list = newClass.int_list

fibNumbersFrom_int_list = [int for int in newClass.int_list if newClass.is_fibonacci(int)]
fib_set = set(fibNumbersFrom_int_list)


print([value for value in int_list if value in fib_set])
