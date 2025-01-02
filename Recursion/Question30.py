def groupSum(idx, arr, target):    
    if idx == len(arr):
        if target == 0:
            return True
        else:
            return False
    if arr[idx]%5==0 and arr[idx+1] ==1:
        return groupSum(idx+2,arr,target-arr[idx])
    elif arr[idx]%5==0:
        return groupSum(idx+1,arr,target-arr[idx])
    else:
        return groupSum(idx+1,arr,target-arr[idx]) or groupSum(idx+1,arr,target)
val = groupSum(0,[2,5,10,4],17)
print(val)