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

a = "11"
b = "1"

def bin_sum(a,b):
    a_lst = list(a)
    b_lst=list(b)
    summ = list()
    flag = 0

    while len(a_lst) > len(b_lst):
        diff = len(a_lst) - len(b_lst)
        b_lst.insert(-diff,0)
        diff -= 1
    while len(b_lst) > len(a_lst):
        diff = len(b_lst) - len(a_lst)
        a_lst.insert(-diff,0)
        diff -= 1

    if len(a_lst) == len(b_lst):
        for i in range(len(a_lst)-1,-1,-1):
            if flag == 0:
                if int(a_lst[i]) + int(b_lst[i]) == 2:
                    #print("Both binary values were 1!")
                    #print("Change of flag")
                    flag = 1
                    #print("Flag is:", flag)
                    summ.insert(-len(summ),"0")

                elif int(a_lst[i]) + int(b_lst[i]) == 1:
                    #print(a[i],"+",b[i], "is 1")
                    #print("Flag is:", flag)
                    summ.insert(-len(summ),"1")

                else:
                    #print(a[i],"+",b[i], "is 0")
                    #print("Flag is:", flag)
                    summ.insert(-len(summ),"0")

            '''1 from previous iteration'''
            elif flag == 1:
                if int(a_lst[i]) + int(b_lst[i]) == 2:
                    #print("Both values were 1!")
                    #print("Flag still 1!")
                    #print("Flag is:", flag)
                    summ.insert(-len(summ),"0")

                elif int(a_lst[i]) + int(b_lst[i]) == 1:
                    #print(a[i],"+",b[i], "is 1, but 1 from previous iteration")
                    #print("Flag is:", flag)
                    summ.insert(-len(summ),"0")

                else:
                    summ.insert(-len(summ),"1")
                    flag = 0
    if flag == 1:
        summ.insert(-len(summ),"1")
    return summ

print(bin_sum(a,b))

# lst = ["a","b","c"]
# string = [''.join(lst)]
# print(string)
