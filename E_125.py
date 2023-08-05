#E_125
#A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all 
#non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.
#Given a string s, return true if it is a palindrome, or false otherwise.

class Solution:
    def isPalindrome(self, s: str) -> bool:
        import re
        s = re.findall("[A-Za-z0-9]+",s)
        s = "".join([w.lower() for w in s])

        reverse = s[::-1]

        if s == reverse:
            return True
        else:
            return False
            
s = "A man, a plan, a canal: Panama"
Solution().isPalindrome(s)
