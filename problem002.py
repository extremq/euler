from functools import lru_cache


# cache the terms, no need for matrix multiplication
@lru_cache(maxsize=None)
def fib(n):
    if n <= 2:
        return n
    return fib(n - 1) + fib(n - 2)


def fib_even_sum(n):
    s = 0
    # reverse it so we use the cached versions instead.
    for i in reversed(range(1, n)):
        if fib(i) % 2 == 0:
            s += fib(i)
    return s


print(fib_even_sum(33))
