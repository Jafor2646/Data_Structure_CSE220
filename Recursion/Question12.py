def triangle(n):
    if n == 1 or n == 0:
        return n
    return n + triangle(n-1)
print(triangle(0))
print(triangle(1))
print(triangle(2))
