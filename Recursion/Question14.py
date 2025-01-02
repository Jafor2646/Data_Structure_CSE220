def array220(a, i):
    if a[i]%10 == 0:
        return True
    if i == len(a)-1:
        return False
    return array220(a, i+1)
print(array220([1,2,20],0))
print(array220([3,20],0))
print(array220([3],0))