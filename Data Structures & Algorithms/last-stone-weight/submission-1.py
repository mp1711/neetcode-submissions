from heapq import heapify, heappop, heappush
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stone_heap = [-1 * i for i in stones]
        heapify(stone_heap)

        while len(stone_heap)>1: 
            x, y = heappop(stone_heap), heappop(stone_heap)
            if x==y: 
                continue
            x-=y
            heappush(stone_heap, x)
        
        return -stone_heap[0] if stone_heap else 0

        