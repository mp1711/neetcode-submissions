class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        def canShip(cnt): 
            thresh = 0
            w = 0
            for weight in weights: 
                if w+weight>cnt: 
                    w = 0
                    thresh += 1
                w += weight

            return thresh+1<=days

        
        l, r = max(weights), sum(weights)
        res = 0

        while l<=r: 
            m = l + (r-l)//2

            if canShip(m): 
                res = m
                r = m-1
            else: 
                l = m+1
        
        return res
        