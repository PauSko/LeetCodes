#E_118
#Given an integer numRows, return the first numRows of Pascal's triangle.
#Input: numRows = 5
#Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        answer = []
        turn = 0
        while turn < numRows:
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
        return answer