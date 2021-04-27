from functools import lru_cache


@lru_cache(maxsize=None)
def collatz(n):
        if n == 1:
                return 1
        if n & 1:
                return 1 + collatz(3 * n + 1)
        return 1 + collatz(n // 2)


if __name__ == "__main__":
        mx = 0
        ans = 0
        for i in range(1, 1000000):
                if mx < collatz(i):
                        mx = collatz(i)
                        ans = i
        print(ans)