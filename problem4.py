def largest_palindrome():
    palindrome = 0
    for i in range(999, 100, -1):
        for j in range(i, 100, -1):
            if str(i * j) == str(i * j)[::-1]:  # check for the reversed product
                palindrome = max(palindrome, i * j)
    return palindrome


print(largest_palindrome())
