#Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
#A subarray is a contiguous part of an array.

#Example 1:
#Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
#Output: 6
#Explanation: [4,-1,2,1] has the largest sum = 6.

#Example 2:
#Input: nums = [1]
#Output: 1

#Example 3:
#Input: nums = [5,4,-1,7,8]
#Output: 23

#nums = [-2,1,-3,4,-1,2,1,-5,4]
#nums = [5,4,-1,7,8]
nums = [1]

def max_sum_cons_nums(nums):
    #nums_lst=list()
    if len(nums) == 1:
        return nums[0]

    if len(nums) > 1:
        sum_lst = list()
        for i in range(len(nums)):
            summ = 0
            for j in range(i+1,len(nums)):
                if len(sum_lst) == 0:
                    summ = nums[i]+nums[j]
                    sum_lst.append((summ,i,j))
                else:
                    summ  += nums[j]
                    sum_lst.append((summ,i,j))
        max_sum = max(sum_lst)
        return max_sum[0]

print(max_sum_cons_nums(nums))
