from heapq import heappush, heappop
from collections import defaultdict
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

        graph = defaultdict(list)

        for u, v, w in flights: 
            graph[u].append((v, w))
        
        minheap = [(0, src, 0)]
        res = []

        while minheap: 
            w1, n1, s1 = heappop(minheap)
            if n1 == dst: 
                res.append((s1, w1))
                continue
            for n2, w2 in graph[n1]: 
                if s1-1<k: 
                    heappush(minheap, (w1+w2, n2, s1+1))


        minweight = float("inf")
        for stop, weight in res: 
            if stop-1>k: 
                continue
            minweight = min(weight, minweight)

        return minweight if minweight!=float("inf") else -1





        