from heapq import heappop, heappush

class Solution:
    def swimInWater(self, grid):
        n = len(grid)
        heap = [(grid[0][0], 0, 0)]
        visited = set()
        dirs = [(1,0), (-1,0), (0,1), (0,-1)]

        while heap:
            time, r, c = heappop(heap)

            if (r, c) in visited:
                continue
            visited.add((r, c))

            if r == n-1 and c == n-1:
                return time

            for dr, dc in dirs:
                nr, nc = r + dr, c + dc

                if 0 <= nr < n and 0 <= nc < n:
                    new_time = max(time, grid[nr][nc])
                    heappush(heap, (new_time, nr, nc))