#E_119
#Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.
#Input: rowIndex = 3
#Output: [1,3,3,1]

from typing import List

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        answer = []
        turn = 0
        while turn <= rowIndex:
            if len(answer)==0:
                answer.append([1])
                turn += 1
            elif len(answer) == 1:
                answer.append([1,1])
                turn += 1
            else:
                new = []
                lst=list(range(0,turn+1))
                for idx in lst:
                    if idx == 0 or idx == turn:
                        new.append(1)
                    else:
                        summ = sum(answer[turn-1][idx-1:idx+1])
                        new.append(summ)
                answer.append(new)
                turn+=1
        return answer[-1]

Solution().getRow(3)
