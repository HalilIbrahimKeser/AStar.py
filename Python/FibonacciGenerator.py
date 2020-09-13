import timeit


def fib(max):
    a, b = 0, 1
    while a < max:
        yield a
        a, b = b, a + b


timeit.timeit(print(list(fib(1000000))))
