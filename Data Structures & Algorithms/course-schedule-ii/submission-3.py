class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        graph = {i:[] for i in range(numCourses)}

        indeg = [0]*numCourses

        for c, p in prerequisites: 
            graph[p].append(c)
            indeg[c]+=1
        
        queue = []

        for i in range(numCourses): 
            if indeg[i]==0: 
                queue.append(i)
        
        order = []

        while queue: 
            course = queue.pop(0)
            order.append(course)

            for node in graph[course]: 

                indeg[node]-=1
                if indeg[node]==0: 
                    queue.append(node)
        
        return order if len(order)==numCourses else []
        