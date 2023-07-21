#Given an integer array nums and an integer val, remove all occurrences of val in nums in-place.
#The relative order of the elements may be changed.

#Input: nums = [3,2,2,3], val = 3
#Output: 2, nums = [2,2,_,_]
#Explanation: Your function should return k = 2, with the first two elements of nums being 2.
#It does not matter what you leave beyond the returned k (hence they are underscores).

nums = [3,2,2,3]
val = 3

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        while val in nums:
            nums.remove(val)
        return len(nums)
