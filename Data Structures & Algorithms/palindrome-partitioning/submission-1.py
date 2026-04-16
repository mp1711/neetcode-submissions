class Solution:
    def partition(self, s: str) -> List[List[str]]:

        def check(i, j): 
            l, r = i, j
            while l<=r: 
                if s[l]!=s[r]: 
                    return False
                l+=1
                r-=1
            return True
        
        res = []
        def backtrack(i, path): 
            if i==len(s): 
                res.append(path[:])
            
            for j in range(i, len(s)): 
                if check(i, j): 
                    path.append(s[i:j+1])
                    backtrack(j+1, path)
                    path.pop()
        
        backtrack(0, [])
        
        return res


        