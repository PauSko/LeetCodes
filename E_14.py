#Write a function to find the longest common prefix string amongst an array of strings.
#If there is no common prefix, return an empty string "".
#Input: strs = ["flower","flow","flight"]
#Output: "fl"

#Input: strs = ["dog","racecar","car"]
#Output: ""

common=""
strs = ["flower","flow","flight"]
#print(strs.index("flower"))

for item in strs[0]:
    letters = list(item)
    for letter in letters:
        if letter in strs[1] and letter in strs[2]:
            common += letter
            continue
print(common)

    #idx = strs.index(item)
    #strs.insert(idx,items)

#print(strs)
