def sumDigits(n):
    if n == 0:
        return 0
    x = n % 10
    return x + sumDigits(n//10)
print(sumDigits(6))