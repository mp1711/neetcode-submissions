class Solution:
    def maxCoins(self, nums: List[int]) -> int:

        nums = [1] + nums + [1]
        n = len(nums)

        dp = [[0]*n for _ in range(n)]

        for ln in range(2, n):
            for l in range(n - ln): 
                r = l+ln
                for k in range(l+1, r): 
                    coins = nums[l]*nums[r]*nums[k]
                    dp[l][r] =  max(dp[l][r], dp[l][k] + dp[k][r] + coins)

        for i in dp: 
            print(i)
        
        return dp[0][n-1]

        