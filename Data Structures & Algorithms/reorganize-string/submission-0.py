from heapq import heapify, heappush, heappop
from collections import Counter
from typing import List

class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)
        heap = [[-cnt, char] for char, cnt in count.items()]
        heapify(heap)

        prev = None
        res = []

        while heap or prev:
            if prev and not heap:
                return "" 

            cnt, char = heappop(heap)
            res.append(char)
            cnt += 1  

            if prev:
                heappush(heap, prev)
                prev = None

            if cnt:
                prev = [cnt, char]

        return "".join(res)