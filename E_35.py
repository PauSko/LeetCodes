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

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        try:
            num = nums.index(target)
        except:
            idx = 1
            flag = 0
            while flag == 0:
                if target-idx in nums:
                    num = nums.index(target-idx)+1
                    flag = 1
                elif target+idx in nums:
                    num = nums.index(target+idx)
                    flag = 1
                idx += 1
        return num  
