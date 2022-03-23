#Given a sorted array of distinct integers and a target value, return the index if the target is found.
#If not, return the index where it would be if it were inserted in order.
#You must write an algorithm with O(log n) runtime complexity.

#Example 1:
#Input: nums = [1,3,5,6], target = 5
#Output: 2

#Example 2:
#Input: nums = [1,3,5,6], target = 2
#Output: 1

nums = [1,3,5,6]
target = 5

def find_idx(nums, target):
    idx = nums.index(target)
    return idx

print(find_idx(nums, target))

'''-------ALTERNATIVE-------'''

nums = [1,3,5,6]
target = 7

def find_idx(nums, target):
    if target in nums:
        idx = nums.index(target)
        return idx
    else:
        for idx in range(len(nums)):
            if nums[idx] < target:
                return idx
            try:
                if nums[idx] < target and nums[idx+1] > target:
                    return idx + 1
            except:
                return len(nums)

print(find_idx(nums, target))
