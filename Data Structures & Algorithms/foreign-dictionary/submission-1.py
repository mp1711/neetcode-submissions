from collections import deque
class Solution:
    def foreignDictionary(self, words: List[str]) -> str:

        chars = set()

        for word in words: 
            for char in word: 
                chars.add(char)
        

        graph = {i:[] for i in chars}
        indegree = {i:0 for i in chars}

        for i in range(1, len(words)): 
            w1, w2 = words[i-1], words[i]

            if len(w1)>len(w2) and w1[:len(w2)]==w2: 
                return ""
            
            for j in range(len(w1)): 
                if w1[j]!=w2[j]: 
                    graph[w1[j]].append(w2[j])
                    indegree[w2[j]]+=1
                    break

        q = deque()

        for c in indegree: 
            if indegree[c]==0: 
                q.append(c)
        
        res = ""

        while q: 
            c = q.popleft()
            res+=c
            for nei in graph[c]: 
                indegree[nei]-=1
                if indegree[nei]==0: 
                    q.append(nei)
        
        return res if len(res)==len(chars) else ""








        
