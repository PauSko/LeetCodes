#Given two binary strings a and b, return their sum as a binary string.

#Example 1:
#Input: a = "11", b = "1"
#Output: "100"

#Example 2:
#Input: a = "1010", b = "1011"
#Output: "10101"

#num = 0
#for i in range(len(a)):
#    #print(a[i])
#    if int(a[i])==1:
#        num += 2**((len(a)-1)-i)
#print(num)

# def bin_to_num(a,b):
#     num_a = 0
#     for i in range(len(a)):
#         if int(a[i])==1:
#             num_a += 2**((len(a)-1)-i)
#     num_b = 0
#     for i in range(len(b)):
#         if int(b[i])==1:
#             num_b += 2**((len(b)-1)-i)
#     num_outcome = num_a + num_b

a = "1010"
b = "1011"

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        sum_nums = int(a,2) + int(b,2)
        binary = bin(sum_nums)[2:]
        return binary
