def special_op(arr):
    if len(arr) < 4:
        return None
    if len(arr) == 4:
        return arr[-1] * arr[-2] * arr[-3] * arr[-4]
    return special_op(arr[1:])


arr = [3,4,5,6,7,8]
result = special_op(arr)
print(result)
