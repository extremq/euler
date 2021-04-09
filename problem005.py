import math


# Naive solution, computes the highest power of all the prime numbers up until n
def evenly_divisible(n):
    #  up to n, not 20
    factors = [0] * n
    for i in range(n, 1, -1):
        clone = i
        d = 1
        while clone > 1:
            d = d + 1
            p = 0
            while clone % d == 0:
                clone = clone / d
                p = p + 1
            factors[d] = max(factors[d], p)

    number = 1
    for i in range(2, n):
        if factors[i] > 0:
            number = number * i ** factors[i]

    return number


print(evenly_divisible(20))


# Optimised solution, using LCM's associativeness
# LCM(x,y) = x * y / GCD(x, y)
def optimised_evenly_divisible(n):
    number = 1
    for i in range(2, n):
        number = number * i // math.gcd(i, number)
    return number


print(optimised_evenly_divisible(20))
