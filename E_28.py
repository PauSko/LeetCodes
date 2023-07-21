#Implement strStr().
#Return the index of the first occurrence of needle in haystack,
#or -1 if needle is not part of haystack.

#Input: haystack = "hello", needle = "ll"
#Output: 2

haystack = "hello"
needle = "ll"

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        import re
        try:
            match = re.search(needle,haystack).span()[0]
        except:
            match = -1
        return match
