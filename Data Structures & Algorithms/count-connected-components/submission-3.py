class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        graph = {i:[] for i in range(n)}

        for u, v in edges: 
            graph[u].append(v)
            graph[v].append(u)

        visited = set()

        def dfs(i): 
            if i in visited: 
                return 
            
            visited.add(i)
            for nei in graph[i]: 
                dfs(nei)
        
        components = 0

        for i in range(n): 
            if i not in visited: 
                print(i, visited)
                dfs(i)
                components += 1
        
        return components
