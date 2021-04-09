# a < b < c, so the max triplet is 1, 499, 500 for which a + b + c = 1000
def compute():
    for b in range(1, 500):
        for a in range(1, b):
            c = 1000 - a - b
            if a**2 + b**2 == c**2:
                return a * b * c


print(compute())
