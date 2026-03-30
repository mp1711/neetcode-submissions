from math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        n = len(piles)
        l = 1; r = max(piles) 

        def compute_time(speed): 
            time = 0

            for pile in piles: 
                time += pile//speed
                if pile%speed: 
                    time += 1
            
            return time<=h

        res = r

        while l<r: 
            m = l + (r-l)//2
            if compute_time(m): 
                res = m
                r = m
            else: 
                l = m+1
        
        return res

            



            





        