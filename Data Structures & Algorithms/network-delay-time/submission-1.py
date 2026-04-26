from collections import defaultdict
from heapq import heappush, heappop
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        graph = defaultdict(list)

        for u, v, t in times: 
            graph[u].append((v, t))
        
        heap = [(0, k)]
        visited = set()
        res = -1
        while heap: 
            time, node = heappop(heap)
            if node in visited: 
                continue
            visited.add(node)
            res = max(res, time)
            for nei, nei_time in graph[node]: 
                if nei not in visited: 
                    heappush(heap, (time + nei_time, nei))
        
        return res if len(visited)==n else -1