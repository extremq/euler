def primeness_sieve(n):
    prime_sum = 0
    result = [True] * (n + 1)
    result[0] = False
    result[1] = False
    for i in range(2, n + 1):
        if result[i]:
            prime_sum = prime_sum + i  # add the prime!
            for j in range(i ** 2, n + 1, i):
                result[j] = False
    return prime_sum


print(primeness_sieve(2000000))
