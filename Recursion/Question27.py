def helper(i, nums, t):
    if t == sum(nums)/2:
        return True
    if t>sum(nums)/2 or i == len(nums):
        return False
    return helper(i+1, nums, t+nums[i]) or helper(i+1,nums,t)
def splitArray(nums):
    return helper(0, nums, 0)

print(splitArray([2,2]))
print(splitArray([2,3]))
print(splitArray([5,2,3]))