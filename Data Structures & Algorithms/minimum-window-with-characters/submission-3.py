from collections import defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if len(t) > len(s): 
            return ""

        need = defaultdict(int)
        have = defaultdict(int)
        ct = cs = 0
        l = 0
        n = len(s)
        res = [0, n]

        for i in t:
            if i not in need: 
                ct += 1
            need[i] += 1
        
        print(need, ct)

        for r in range(n): 
            
            have[s[r]] += 1
            if have[s[r]]==need[s[r]]: 
                cs += 1
            
            while cs==ct: 
                if res[1]-res[0] > r-l: 
                    res = [l, r]
                have[s[l]] -= 1
                if s[l] in need and have[s[l]] < need[s[l]]: 
                    cs-=1
                l+=1
        
        return s[res[0]:res[1]+1] if l!=0 else ""






            
            




        