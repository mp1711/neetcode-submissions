class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        rows = len(grid)
        cols = len(grid[0])

        def dfs(r, c): 

            if r<0 or c<0 or r==rows or c==cols or grid[r][c] in (0, 2): 
                return 0
            
            grid[r][c] = 2

            return 1 + dfs(r+1, c) + dfs(r, c+1) + dfs(r-1, c) + dfs(r, c-1)

        area = 0

        for r in range(rows): 
            for c in range(cols): 
                if grid[r][c]==1: 
                    area = max(area, dfs(r, c))        
        
        return area