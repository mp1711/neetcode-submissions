from collections import defaultdict
from heapq import heappush, heappop
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

        graph = defaultdict(list)

        for u, v, w in flights: 
            graph[u].append((v, w))
        

        heap = [(0, 0, src)]
        best = {}

        while heap: 
            price, stops, node = heappop(heap)
            if (stops, node) in best: 
                continue
            best[(stops, node)] = price
            if node==dst: 
                return price
            for nei, wt in graph[node]: 
                if stops<=k: 
                    heappush(heap, (wt+price, stops+1, nei))
        
        return -1