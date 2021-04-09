def compute():
    ans = int()
    maxdiv = 0
    step = 1
    while maxdiv < 500:
        ans = step * (step + 1) // 2
        maxdiv = max(get_div(ans), maxdiv)
        step += 1
    return ans


def get_div(n):
    div = 2
    d = 2
    while d ** 2 <= n:
        if n % d == 0:
            div += 2
        if d ** 2 == n:
            div -= 1
        d += 1
    return div


print(compute())