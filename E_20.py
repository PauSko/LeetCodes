#Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
#An input string is valid if:
#Open brackets must be closed by the same type of brackets.
#Open brackets must be closed in the correct order.

#Input: s = "()"
#Output: true

#Input: s = "(]"
#Output: false

#s = "(]"
s = "()"
#s = "()[]{}"

open = ["[","{","("]
close = ["]","}",")"]

for i in range(len(s)):
    if i%2 == 0:
        flag = 0
        if s[i] in open:
            idx = open.index(s[i])
        if close[idx] == s[i+1]:
            flag = 1
        else:
            flag = 0
            break
    else:
        continue
if flag == 1:
    print("True")
else:
    print("False")
