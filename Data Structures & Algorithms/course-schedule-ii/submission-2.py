from collections import deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        graph = {i:[] for i in range(numCourses)}
        indegree = [0]*numCourses

        for a, b in prerequisites: 
            graph[b].append(a)
            indegree[a]+=1
        

        res = []
        q = deque()

        for i in range(numCourses): 
            if indegree[i]==0: 
                q.append(i)
        
        while q: 
            course = q.popleft()
            res.append(course)

            for nei in graph[course]: 
                indegree[nei]-=1
                if indegree[nei]==0: 
                    q.append(nei)

        return res if len(res)==numCourses else []
        
        
        


        
