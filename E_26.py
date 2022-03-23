#Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same.
#Input: nums = [0,0,1,1,1,2,2,3,3,4]
#Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
#Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
#It does not matter what you leave beyond the returned k (hence they are underscores).

nums = [0,0,1,1,1,2,2,3,3,4]

def rem_doubles(nums):
    unique=list()
    for item in nums:
        if item not in unique:
            unique.append(item)
        else:
            continue
    if len(unique) < len(nums):
        diff  = len(nums) - len(unique)
        for item in range(diff):
            unique.append('_')
        #unique.append(("_") * (len(nums) - len(unique)))
    return unique

print(rem_doubles(nums))
