def bunnyEars(n):
    if n == 0:
        return 0
    return 2 + bunnyEars(n-1)
print(bunnyEars(0))
print(bunnyEars(1))
print(bunnyEars(2))
