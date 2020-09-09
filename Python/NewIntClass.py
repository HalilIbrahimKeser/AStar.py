import math


class NewInt(int):

    def __init__(self):
        self.my_list = list(range(0, 1000))

    def isPerfectSquare(self, x):
        s = int(math.sqrt(x))
        return s * s == x

    def is_fibonacci(self, n):
        return self.isPerfectSquare(5 * n * n + 4) or self.isPerfectSquare(5 * n * n - 4)

newClass = NewInt()
fibonacci_list = [int for int in newClass.my_list if newClass.is_fibonacci(int)]
print(fibonacci_list)

#beregning hentet fra: https://www.geeksforgeeks.org/python-program-for-how-to-check-if-a-given-number-is-fibonacci-number/
#list comprehensions: https://www.digitalocean.com/community/tutorials/understanding-list-comprehensions-in-python-3