class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        maxarea = 0
        rows = len(grid)
        cols = len(grid[0])

        def calcarea(r, c): 
            area = 1
            queue = [(r, c)]
            grid[r][c]=2
            while queue: 
                dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
                row, col = queue.pop(0)
                print(row, col)
                for dr, dc in dirs: 
                    r = row+dr
                    c = col+dc
                    if r in range(rows) and c in range(cols) and grid[r][c]==1:
                        area += 1
                        grid[r][c]=2
                        queue.append((r, c)) 

            return area
        
        for r in range(rows): 
            for c in range(cols): 
                if grid[r][c]==1: 
                    area = calcarea(r, c)
                    maxarea = max(maxarea, area)
        
        return maxarea
