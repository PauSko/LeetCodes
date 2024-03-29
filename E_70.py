#E_70
#You are climbing a staircase. It takes n steps to reach the top.
#Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

#Input: n = 3
#Output: 3
#Explanation: There are three ways to climb to the top.
#1. 1 step + 1 step + 1 step
#2. 1 step + 2 steps
#3. 2 steps + 1 step


class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        
        outcomes = [0]*(n+1)
        outcomes[:3] = [0,1,2]
        
        for idx in range(3,n+1):
            outcomes[idx] = outcomes[idx-1]+outcomes[idx-2]
            
        return outcomes[-1]   
                
x = Solution().climbStairs(5)
