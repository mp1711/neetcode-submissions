from math import log2
class Solution:
    def countBits(self, n: int) -> List[int]:

        ans = [0]*(n+1)
        for num in range(1, n+1): 
            maxbit = int(log2(num)+1)
            for bit in range(maxbit): 
                if num>>bit & 1 == 1: 
                    ans[num]+=1
        
        return ans



        