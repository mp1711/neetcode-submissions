class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:

        n = len(isConnected)
        par = [i for i in range(n)]
        rank = [1 for _ in range(n)]

        def find(node):
            if node!=par[node]: 
                par[node] = find(par[node])
            return par[node]
        

        def union(n1, n2): 
            p1 = find(n1)
            p2 = find(n2)

            if p1==p2: 
                return False
            
            if rank[p1]>=rank[p2]: 
                par[p2] = par[p1]
                rank[p1] += rank[p2]
            else: 
                par[p1] = par[p2]
                rank[p2] += rank[p1]
            
            return True

        edges = set()
        res = n
        for r in range(n): 
            for c in range(r+1, n): 
                if isConnected[r][c] and r!=c and union(r, c): 
                    res -= 1
        
        return res