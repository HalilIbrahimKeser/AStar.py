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

new_set = range(0, 100000)
#fib_set = {int for int in NewInt1.is_fibonacci(int)}
comprehension_List = [int for int in newClass.int_list if new_set(int)]
