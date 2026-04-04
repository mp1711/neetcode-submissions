from heapq import heappush, heappop
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        heap = []

        for point in points: 
            dist = point[0]**2 + point[1]**2
            heappush(heap, (-dist, point))

            if len(heap)>k: 
                heappop(heap)
        
        return [i[1] for i in heap]
        