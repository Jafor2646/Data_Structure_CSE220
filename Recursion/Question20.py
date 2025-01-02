def array6(a, i):
    if a[i] == 6:
        return True
    if i == len(a)-1:
        return False
    return array6(a, i+1)
print(array6([1,6,4],0))
print(array6([1,4],0))
print(array6([6],0))