def compute():
    n = 2 ** 1000
    sum = 0

    for digit in str(n):
        sum += int(digit)

    print(sum)

if __name__ == "__main__":
    compute()