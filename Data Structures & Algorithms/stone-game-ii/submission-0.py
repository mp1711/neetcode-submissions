class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        suff = piles[:]

        for i in range(n-2, -1, -1): 
            suff[i] = suff[i]+suff[i+1]

        dp = {}

        def backtrack(i, M): 

            if i>=n: 
                return 0
            
            if i+2*M>=n: 
                return suff[i]
            
            if (i, M) in dp: 
                return dp[(i, M)]
            
            best = 0
            for X in range(1, 2*M+1): 
                best = max(best,
                suff[i] - backtrack(i + X, max(M, X)))
            
            dp[(i, M)] = best

            return best
        
        return backtrack(0, 1)
        