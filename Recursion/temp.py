def splitArray(nums):
    return helper(0, nums, 0)

def helper(start, nums, target):
    if target == sum(nums) / 2:
        return True
    if target > sum(nums) / 2 or start == len(nums):
        return False
    # Either include or exclude the current number and check the next numbers
    return helper(start + 1, nums, target + nums[start]) or helper(start + 1, nums, target)
print(splitArray([2,2]))
print(splitArray([2,3]))
print(splitArray([5,2,3]))
print(splitArray([2, 2, 3, 5]))
print(splitArray([2, 3, 5, 8]))
print(splitArray([2, 3, 5, 8, 5, 4, 5]))