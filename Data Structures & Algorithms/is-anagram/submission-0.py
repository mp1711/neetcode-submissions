from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        sf, tf = defaultdict(int), defaultdict(int)

        if len(s)!=len(t): 
            return False 
        
        for i in range(len(s)): 
            sf[s[i]]+=1
            tf[t[i]]+=1
        
        for i in sf: 
            if i not in tf or tf[i]!=sf[i]: 
                return False
        return True
