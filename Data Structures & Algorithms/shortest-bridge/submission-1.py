class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:

        rows = len(grid)
        cols = len(grid[0])

        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        visited = set()

        def dfs(r, c): 
            if r<0 or c<0 or r==rows or c==cols or (r, c) in visited or grid[r][c]==0: 
                return 
            
            grid[r][c] = 2
            visited.add((r, c))
            for dr, dc in dirs: 
                dfs(r+dr, c+dc)
        
        found = False
        for r in range(rows): 
            for c in range(cols): 
                if grid[r][c]==1: 
                    dfs(r, c)
                    found = True
                    break
            if found: break
        

        q = deque(list(visited))

        steps = 0

        while q: 
            for _ in range(len(q)): 
                r, c = q.popleft()
                for dr, dc in dirs: 
                    nr = r+dr
                    nc = c+dc
                    if 0<=nr<rows and 0<=nc<cols and (nr, nc) not in visited: 
                        if grid[nr][nc]==1: 
                            return steps
                        q.append((nr, nc))
                        visited.add((nr, nc))
            steps+=1
    
        return steps



            
            

        