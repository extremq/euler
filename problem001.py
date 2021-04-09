def sum_of_multiple_of_3_or_5(n):
    s = 0
    for i in range(1, n):
        if i % 3 == 0 or i % 5 == 0:
            s += i

    return s


print(sum_of_multiple_of_3_or_5(1000))
