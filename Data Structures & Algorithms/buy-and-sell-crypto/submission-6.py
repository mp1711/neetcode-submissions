class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        l, r= 0, len(prices) - 1
        maxprofit = 0

        for r in range(1, len(prices)): 
            if prices[r]<prices[l]: 
                l = r
            maxprofit = max(maxprofit, prices[r] - prices[l])
        
        return maxprofit

        