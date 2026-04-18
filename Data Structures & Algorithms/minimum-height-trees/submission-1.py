from collections import deque
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:

        if n==1: 
            return [0]

        degree = [0]*n
        graph = {i:[] for i in range(n)}        

        for u, v in edges: 
            graph[u].append(v)
            graph[v].append(u)
            degree[u]+=1
            degree[v]+=1
        
        queue = deque()

        for node in range(n): 
            if degree[node]==1: 
                queue.append(node)
        
        total = n
        while total>2: 
            total -= len(queue)
            for _ in range(len(queue)): 
                node = queue.popleft()
                for nei in graph[node]: 
                    degree[nei]-=1
                    if degree[nei]==1: 
                        queue.append(nei)
        
        return list(queue)
