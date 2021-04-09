primes = []


def primeness_sieve(n):
    result = [True] * (n + 1)
    result[0] = False
    result[1] = False
    for i in range(2, n + 1):
        if result[i]:
            primes.append(i)
            for j in range(i ** 2, n + 1, i):
                result[j] = False

    return result


# the number of primes grows like x/ln(x), so 10001 = x/ln(x)
# let x = e^-t
# e^-t/ln(e^-t) = 10001
# 1/(e^t * ln((e^t)^-1))) = 10001
# -1/(e^t * ln(e^t)) = 10001
# -1/(e^t * t) = 10001
# 10001 * e^t * t = -1
# e^t * t = -1/10001
# W(e^t * t) = W(-1/10001)
# t = W(-1/10001)
# x = e^-W_0(-1/10001) and
# x = e^-W_-1(-1/10001), since the argument is between 0 and -1/e.
# this gives us x approx= 1.0001 and x approx= 116684
# we can add to the second approximation around 10% or 16000 just to make up for the error
sieve = primeness_sieve(130000)
print(primes[10001 - 1])
