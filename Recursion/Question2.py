def bunnyEars(n):
    if n == 0:
        return 0
    if n%2 == 0:
        return 3 + bunnyEars(n-1)
    else:
        return 2 + bunnyEars(n-1)
print(bunnyEars(0))
print(bunnyEars(1))
print(bunnyEars(2))