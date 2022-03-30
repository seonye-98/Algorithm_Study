'''
70. Climbing Stairs
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?


n번째 계단에 도착하려면 n-1, n-2번째 계단에 도달하는 방법의 수를
합친 것과 같다.
'''

class Solution:
    
    def climbStairs(self, n):
        fn = [0,1,2]

        for i in range(3, n+1):
            fn.append(fn[i-1] + fn[i-2])
        
        return fn[n]


'''
sol2)
class Solution:
    
    def climbStairs(self, n: int) -> int:       
        if n <=2:
            return n
        
        a, b, c = 0, 1, 2
        
        # bottom up
        for i in range(3, n+1):
            a, b = b, c
            c = a + b
            
        return c

sol3)
Backtracking + Memoization
class Solution:
    
    @lru_cache(maxsize=128)
    def climbStairs(self, n: int) -> int:       
        # backtracking
        
        if n == 0 or n == 1: 
            return 1
        
        return self.climbStairs(n-1) + self.climbStairs(n-2)
'''