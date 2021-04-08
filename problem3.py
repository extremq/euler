def largest_prime_factor(x):
    d = 1
    while x > 1:
        d = d + 1
        while x % d == 0:
            x = x / d
    return d


print(largest_prime_factor(600851475143))
