class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid: 
            return 0

        
        row = len(grid)
        cols = len(grid[0])


        islands = 0

        def bfs(r, c): 
            queue = [(r, c)]
            grid[r][c]="2"

            while queue: 
                r, c = queue.pop(0)
                dirs = [[0, 1], [1, 0], [-1, 0], [0, -1]]

                for dr, dc in dirs: 
                    if r+dr in range(row) and c+dc in range(cols) and grid[r+dr][c+dc]=="1": 
                        grid[r+dr][c+dc] = "2"
                        queue.append((r+dr, c+dc))



        for r in range(row): 
            for c in range(cols): 
                if grid[r][c]=='1': 
                    bfs(r, c)
                    islands+=1
        
        return islands

        