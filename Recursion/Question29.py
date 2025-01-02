def equibrilam(arr,idx,left,right):
    if idx==len(arr):
        if left==right:
            return True
        else:
            return False
    if arr[idx] %3==0:
        return equibrilam(arr,idx+1,left+arr[idx],right)
    elif arr[idx] %5==0:
        return equibrilam(arr,idx+1,left,right+arr[idx])
    else:
        return equibrilam(arr,idx+1,left+arr[idx],right) or equibrilam(arr,idx+1,left,right+arr[idx])
def split53(arr):
    return equibrilam(arr,0,0,0)
val = split53([1,1])
print(val)