def count(n):
    if n == 0:
        return 0
    x = n%10
    if x == 7:
        return 1 + count(n//10)
    else:
        return 0 + count(n//10)
print(count(717))
print(count(7))
print(count(123))