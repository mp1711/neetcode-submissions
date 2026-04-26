from collections import defaultdict
from heapq import heappush, heappop
class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:

        graph = defaultdict(list)

        for ind, prob in enumerate(succProb): 
            u, v = edges[ind]
            graph[u].append((v, prob))
            graph[v].append((u, prob))
        
        heap = [(-1, start_node)]
        vis = set()

        while heap: 
            prob, node = heappop(heap)
            if node==end_node: 
                return -prob
            if node in vis: 
                continue
            vis.add(node)

            for nei, p in graph[node]: 
                heappush(heap, (prob*p, nei))

        return 0