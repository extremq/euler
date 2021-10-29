def compute():
    answer = factorial(40) // (factorial(20) ** 2)

    print(answer)

def factorial(x):
    if x == 1: 
        return 1
    return x * factorial(x - 1)

if __name__ == "__main__":
    compute()