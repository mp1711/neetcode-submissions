from heapq import heappush, heappop
from collections import defaultdict

class Solution:
    def findCheapestPrice(self, n, flights, src, dst, k):

        graph = defaultdict(list)
        for u, v, w in flights:
            graph[u].append((v, w))

        minheap = [(0, src, 0)]

        best = {}  

        while minheap:
            w1, n1, s1 = heappop(minheap)

            if (n1, s1) in best and best[(n1, s1)] <= w1:
                continue
            best[(n1, s1)] = w1

            if n1 == dst:
                return w1

            if s1 - 1 < k:
                for n2, w2 in graph[n1]:
                    heappush(minheap, (w1 + w2, n2, s1 + 1))

        return -1