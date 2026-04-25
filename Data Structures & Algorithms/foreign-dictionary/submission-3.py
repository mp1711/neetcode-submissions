from collections import defaultdict, deque
class Solution:
    def foreignDictionary(self, words: List[str]) -> str:

        chars = set()
        for word in words: 
            for ch in word: 
                chars.add(ch)
        
        graph = {i:[] for i in chars}
        indeg = {i:0 for i in chars}

        for i in range(1, len(words)): 
            w1 = words[i-1]
            w2 = words[i]

            if len(w1)>len(w2) and w1[:len(w2)]==w2: 
                return ""
            
            for j in range(len(w1)): 
                if w1[j]!=w2[j]:
                    indeg[w2[j]]+=1
                    graph[w1[j]].append(w2[j])
                    break
        
        q = deque()

        for ch in indeg: 
            if indeg[ch]==0: 
                q.append(ch)
        
        res = []

        while q: 
            node = q.popleft()
            res.append(node)

            for nei in graph[node]: 
                indeg[nei]-=1
                if indeg[nei]==0: 
                    q.append(nei)
        
        return "".join(res) if len(res)==len(chars) else ""









        