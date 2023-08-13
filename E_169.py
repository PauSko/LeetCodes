#E_169 
#Majority Element
#Given an array nums of size n, return the majority element.
#The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

#Input: nums = [3,2,3]
#Output: 3

from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        unique = list()
        items = set(nums)
        for item in items:
            unique.append((item,nums.count(item)))

        freq_num = max(unique,key=lambda pairs:pairs[1])
        num = freq_num[0]
        freq = freq_num[1]

        if freq > len(nums)/2:
            return num
        else:
            pass
 
nums = [2,2,1,1,1,2,2]
Solution().majorityElement(nums)