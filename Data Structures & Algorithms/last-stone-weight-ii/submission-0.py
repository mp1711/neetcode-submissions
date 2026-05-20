class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:

        S = sum(stones)

        half = S//2

        dp = [False]*(half+1)
        
        dp[0] = True


        for s in stones: 
            for i in range(half, s-1, -1):
                dp[i] |= dp[i-s]
        

        for i in range(half, -1, -1): 
            if dp[i]: 
                return S-2*i
        
        return 0
        