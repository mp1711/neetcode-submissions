from math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        l, r = 1, max(piles)
        ind = r

        while l<=r: 
            m = (l+r)//2
            hours = 0

            for i in piles: 
                hours += ceil(i/m)
            
            if hours<=h: 
                r = m-1
                ind = min(ind, m)

            else: 
                l = m+1
            
        
        return ind



        