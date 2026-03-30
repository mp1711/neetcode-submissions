class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        # Rule 1: Tree must have exactly n-1 edges
        if len(edges) != n - 1:
            return False
        
        # Build adjacency list
        graph = {i: [] for i in range(n)}
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        visited = set()
        
        def dfs(node, parent):
            visited.add(node)
            
            for neighbor in graph[node]:
                if neighbor == parent:
                    continue
                if neighbor in visited:
                    return False  # cycle detected
                if not dfs(neighbor, node):
                    return False
            
            return True
        
        # Start DFS from node 0
        if not dfs(0, -1):
            return False
        
        # Check if fully connected
        return len(visited) == n