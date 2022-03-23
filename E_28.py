#Implement strStr().
#Return the index of the first occurrence of needle in haystack,
#or -1 if needle is not part of haystack.

#Input: haystack = "hello", needle = "ll"
#Output: 2

haystack = "hello"
needle = "ll"

def in_str(haystack, needle):
    import re
    try:
        found = re.search(needle,haystack)
        be = found.span()
        index = be[0]
    except:
        index = -1
    return index

print(in_str(haystack, needle))
