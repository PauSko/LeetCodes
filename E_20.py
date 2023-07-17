#Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
#An input string is valid if:
#Open brackets must be closed by the same type of brackets.
#Open brackets must be closed in the correct order.

#Input: s = "()"
#Output: true

#Input: s = "(]"
#Output: false

class Solution:
    def isValid(self, s: str) -> bool:          
        import re       
        while len(s) != 0:
            easy_pairs = re.findall("\(\)|\[\]|\{\}",s)
            if(len(easy_pairs))>0:
                if "".join(easy_pairs) == s:
                    flag = 1
                    break
                else:
                    for item in easy_pairs:
                        s = s.replace(item,"")
                        flag = 1
                        continue
            else:
                flag = 0
                break         
        if flag:
            return "true"
        else:
            return "false"
            
s="{}{{}}"        
x = Solution().isValid(s)
