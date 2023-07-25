'''You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can 
you climb to the top?'''

class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        steps = [0]* (n+1)
        steps[1] = 1
        steps[2] = 2
        for i in range(3,n+1):
            steps[i] = steps[i-1] + steps[i-2]
        
        print(steps)
        return steps[n]
