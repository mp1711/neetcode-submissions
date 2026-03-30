from collections import defaultdict, deque
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:

        graph = defaultdict(list)
        tickets.sort(key = lambda x: (x[0], x[1]))
        res = []

        for fro, to in tickets: 
            graph[fro].append(to)


        res = ["JFK"]

        def dfs(src): 

            if len(res)==len(tickets)+1: 
                return True

            if src not in graph: 
                return False
            
            for i, dst in enumerate(graph[src]): 
                graph[src].pop(i)
                res.append(dst)

                if dfs(dst): 
                    return True

                graph[src].insert(i, dst)    
                res.pop()
        
        dfs("JFK")
        return res





        