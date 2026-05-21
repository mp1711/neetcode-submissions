class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        total=0
        x=prices[0]
        for i in range(1,len(prices)):
            if(x>prices[i]):
                x=prices[i]
            else:
                total+=prices[i]-x
                x=prices[i]
                
        return total