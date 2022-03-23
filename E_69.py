#Given a non-negative integer x, compute and return the square root of x.
#Since the return type is an integer, the decimal digits are truncated, and only the integer part of the result is returned.
#Note: You are not allowed to use any built-in exponent function or operator, such as pow(x, 0.5) or x ** 0.5.

#Example 1:
#Input: x = 4
#Output: 2

#Example 2:
#Input: x = 8
#Output: 2
#Explanation: The square root of 8 is 2.82842..., and since the decimal part is truncated, 2 is returned.

num=17
k=int(num/2)
mnoznik = 0

smaller_nums = list()
exactly_nums = list()

for item in range(k+1):
    #print(item)
    if item * item < num:
        smaller_nums.append((item,"smaller"))
        continue
    if item * item == num:
        exactly_nums.append((item,"exactly"))
        continue
    else:
        break
#print(smaller_nums)
#print(smaller_nums[len(smaller_nums)-1][0])

if len(exactly_nums) == 1:
    mnoznik = exactly_nums[0][0]
else:
    mnoznik = smaller_nums[len(smaller_nums)-1][0]

print(mnoznik)
