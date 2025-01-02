def groupSum(i, a, t):
    if t == 0:
        return True
    if i == len(a):
        return False
    if groupSum(i+1, a, t-a[i]):
        return True
    if groupSum(i+1, a, t):
        return True
    return False
print(groupSum(0,[2,4,8],10))
print(groupSum(0,[2,4,8],14))
print(groupSum(0,[2,4,8],9))