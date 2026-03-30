from collections import deque

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights:
            return []
        
        rows, cols = len(heights), len(heights[0])
        
        pacific = set()
        atlantic = set()
        
        def bfs(queue, visited):
            directions = [(1,0), (-1,0), (0,1), (0,-1)]
            
            while queue:
                r, c = queue.popleft()
                
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    
                    if (0 <= nr < rows and 
                        0 <= nc < cols and 
                        (nr, nc) not in visited and 
                        heights[nr][nc] >= heights[r][c]):
                        
                        visited.add((nr, nc))
                        queue.append((nr, nc))
        
        pacific_queue = deque()
        atlantic_queue = deque()
        
        for c in range(cols):
            pacific_queue.append((0, c))
            pacific.add((0, c))
        
        for r in range(rows):
            pacific_queue.append((r, 0))
            pacific.add((r, 0))
        
        for c in range(cols):
            atlantic_queue.append((rows - 1, c))
            atlantic.add((rows - 1, c))
        
        for r in range(rows):
            atlantic_queue.append((r, cols - 1))
            atlantic.add((r, cols - 1))
        
        bfs(pacific_queue, pacific)
        bfs(atlantic_queue, atlantic)
        
        result = []
        for r in range(rows):
            for c in range(cols):
                if (r, c) in pacific and (r, c) in atlantic:
                    result.append([r, c])
        
        return result