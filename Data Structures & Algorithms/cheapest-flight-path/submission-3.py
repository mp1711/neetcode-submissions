from heapq import heappush, heappop
from collections import defaultdict

class Solution:
    def findCheapestPrice(self, n, flights, src, dst, k):
        graph = defaultdict(list)
        for u, v, w in flights:
            graph[u].append((v, w))

        heap = [(0, src, 0)]  # cost, node, edges_used

        while heap:
            cost, node, edges = heappop(heap)

            if edges > k + 1:
                continue

            if node == dst:
                return cost

            for nei, price in graph[node]:
                heappush(heap, (cost + price, nei, edges + 1))

        return -1