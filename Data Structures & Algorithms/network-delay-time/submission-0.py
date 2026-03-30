from heapq import heapify, heappop, heappush
from collections import defaultdict
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        graph = defaultdict(list)
        for u, v, w in times: 
            graph[u].append((v, w))
    
        minheap = [(0, k)]
        visit = set()
        t = 0

        while minheap: 
            w1, n1 = heappop(minheap)
            if n1 in visit: 
                continue
            visit.add(n1)
            t = max(t, w1)
            for n2, w2 in graph[n1]: 
                if n2 not in visit: 
                    heappush(minheap, (w1+w2, n2))
    
        return t if len(visit)==n else -1
        