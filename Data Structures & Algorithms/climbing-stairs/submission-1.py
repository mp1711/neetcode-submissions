class Solution:
    def climbStairs(self, n: int) -> int:

        if n<=2: 
            return n

        one = 1
        two = 2

        for i in range(n-2): 
            res = one+two
            one = two
            two = res
        
        return res
        
        
