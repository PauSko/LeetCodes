#Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
#You may assume that each input would have exactly one solution, and you may not use the same element twice.
#You can return the answer in any order.

#Input: nums = [2,7,11,15], target = 9
#Output: [0,1]
#Output: Because nums[0] + nums[1] == 9, we return [0, 1].

nums_lst = [7,11,15,2]
target = 9

def twoSum(nums_lst,target):
    for i in range(len(nums_lst)):
        for j in range(i + 1,len(nums_lst)):
            if nums_lst[i] + nums_lst[j] == target:
                return [i, j]

print(twoSum(nums_lst,target))
