from heapq import heapify, heappush, heappop
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:

        minheap = [(c, p) for c, p in zip(capital, profits)]
        heapify(minheap)
        maxheap = []

        while k>0: 
            while minheap and minheap[0][0]<=w: 
                c, p = heappop(minheap)
                heappush(maxheap, -p)

            if maxheap: 
                w += -heappop(maxheap)
                
            k-=1
        
        return w