#Given an integer x, return true if x is palindrome integer.
#An integer is a palindrome when it reads the same backward as forward.
#For example, 121 is palindrome while 123 is not.

num =1231

def palindrome(num):
    st_num=str(num)
    left = ""
    right = ""

    if len(st_num) % 2 != 0:
        i_mid = int((len(st_num)+1)/2 - 1)
        for i in range(0,i_mid+1):
            if i == i_mid:
                continue
            else:
                left += st_num[i]
                right += st_num[-i-1]
    else:
        for i in range(0,len(st_num)):
            left += st_num[i]
            right += st_num[-i-1]

    return left == right
print(palindrome(num))

'''ALTERNATIVE''''
num="ABCA"

def palindrome(num):
    right = str(num)
    left = list()
    left_st=""
    for letter in right: #A,B,A
        idx = num.index(letter)
        left.insert(-idx, letter)
    for item in left:
        left_st += item
    return left_st == right

print(palindrome(num))
