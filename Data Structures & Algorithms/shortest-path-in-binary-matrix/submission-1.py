from collections import defaultdict
from heapq import heappush, heappop
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:

        n = len(grid)
        if grid[0][0] or grid[n-1][n-1]: 
            return -1
        
        heap = [(1, 0, 0)]
        vis = set()
        dirs = [(0, 1), (1, 0), (-1, 0), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]

        while heap: 
            steps, r, c = heappop(heap)
            if (r, c) in vis: 
                continue
            if (r, c) == (n-1, n-1): 
                return steps
            
            for dr, dc in dirs:
                nr = r+dr
                nc = c+dc
                if 0<=nr<n and 0<=nc<n and not grid[nr][nc]: 
                    grid[nr][nc] = 1
                    heappush(heap, (steps+1, nr, nc))

        return -1        