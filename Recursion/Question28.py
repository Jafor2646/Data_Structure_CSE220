def spliter(arr,idx,left,right):
    if len(arr) == idx:
        if left%10==0 and right%2==1:
            return True
        else:
            return False
    return spliter(arr,idx+1,left+arr[idx],right) or spliter(arr,idx+1,left,right+arr[idx])
def splitOdd10(arr):
    return spliter(arr,0,0,0)
val = splitOdd10([5,5,6,1])
print(val)