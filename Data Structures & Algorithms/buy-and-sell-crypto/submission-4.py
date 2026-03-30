class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        l = 0
        n = len(prices)
        profit = 0

        for r in range(1, n): 
            if prices[r]<prices[l]: 
                l = r
            profit = max(profit, prices[r] - prices[l])
        
        return profit



        