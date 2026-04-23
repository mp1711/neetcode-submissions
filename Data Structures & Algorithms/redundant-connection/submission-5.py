class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        n = len(edges)
        par = {i:i for i in range(1, n+1)}
        rank = {i:1 for i in range(1, n+1)}

        def find(node): 
            if node!=par[node]: 
                par[node] = find(par[node])
            return par[node]
                
        def union(n1, n2): 
            p1 = find(n1)
            p2 = find(n2)

            if p1==p2: 
                return False
            
            if rank[p2]>rank[p1]: 
                par[p1] = par[p2]
                rank[p2] += rank[p1]
            else: 
                par[p2] = par[p1]
                rank[p1] += rank[p2]
            
            return True
        
        res = []
        for r, c in edges: 
            if not union(r, c): 
                res = [r, c]
        
        return res


        