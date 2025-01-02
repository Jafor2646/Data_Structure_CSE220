def array11(a, i):
    if i == len(a)-1:
        if a[i] == 11:
            return 1
        return 0
    if a[i] == 11:
        return 1 + array11(a, i+1)
    return array11(a, i+1)
print(array11([1, 2, 11], 0))
print(array11([11, 11], 0))
print(array11([1,2,3,4], 0))