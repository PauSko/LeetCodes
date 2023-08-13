#E_168
#Excel Sheet Column Title
#Given an integer columnNumber, return its corresponding column title as it appears in an Excel sheet.

#Input: columnNumber = 701
#Output: "ZY"

columnNumber = 18278

class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        column_name = list()

        while columnNumber != 0:
            digit = columnNumber%26
            if digit != 0:
                column_name.insert(0,chr(digit+64))
                columnNumber -= digit
                columnNumber = int(columnNumber/26)
            else:
                column_name.insert(0,chr(26+64))
                columnNumber = int(columnNumber/26)-1
        
        answer = "".join(column_name) 

        return answer
    
Solution().convertToTitle(columnNumber)