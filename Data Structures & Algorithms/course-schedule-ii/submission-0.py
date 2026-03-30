class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        graph = {i:[] for i in range(numCourses)}

        indegree = [0]*numCourses

        for c, p in prerequisites: 
            graph[p].append(c)
            indegree[c]+=1
        
        queue = []
        for i in range(numCourses): 
            if indegree[i]==0: 
                queue.append(i)
        
        order = []

        while queue: 
            course = queue.pop(0)
            order.append(course)

            for node in graph[course]: 
                indegree[node]-=1
                if indegree[node]==0: 
                    queue.append(node)
            
        
        if len(order)==numCourses: 
            return order
        
        return []
                
        


        
