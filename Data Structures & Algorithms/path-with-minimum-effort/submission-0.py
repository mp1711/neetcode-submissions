from heapq import heappush, heappop
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        
        rows = len(heights)
        cols = len(heights[0])

        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        heap = [(0, 0, 0)]
        vis = set()

        while heap: 
            h, r, c = heappop(heap)
            if (r, c) in vis: 
                continue 
            if r==rows-1 and c==cols-1: 
                return h
            vis.add((r, c))

            for dr, dc in dirs: 
                nr = r+dr
                nc = c+dc
                if nr<0 or nc<0 or nr==rows or nc==cols: 
                    continue
                diff = max(h, abs(heights[r][c] - heights[nr][nc]))
                heappush(heap, (diff, nr, nc))

        return -1

            

        