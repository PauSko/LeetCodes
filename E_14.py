#Write a function to find the longest common prefix string amongst an array of strings.
#If there is no common prefix, return an empty string "".
#Input: strs = ["flower","flow","flight"]
#Output: "fl"

#Input: strs = ["dog","racecar","car"]
#Output: ""

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs)>1:
            sample = [w for w in strs if len(w) ==  min([len(w) for w in strs])][0]
            strs.remove(sample)
    
            idx = 0
            while True:
                try:
                    common = re.findall("^"+sample,strs[idx])
                    if len(common)!=0:
                        sample = common[0]
                        idx += 1
                    else:
                        if len(sample)>1:
                            sample = sample[:len(sample)-1]
                        else:
                            common = ""
                            break
                except:
                    common = common[0]
                    break
        else:
            common = strs[0]
        return common
