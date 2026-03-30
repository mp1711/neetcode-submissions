class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if t=="" or len(t)>len(s): 
            return ""
        
        sf, tf = {}, {}

        ind = [-1, -1]
        res = float('inf')

        for i in t: 
            tf[i] = 1 + tf.get(i, 0)
        
        have = 0
        need = len(tf)

        l = 0
        for r in range(len(s)): 
            ch = s[r]
            sf[ch] = 1 + sf.get(ch, 0)
            if s[r] in tf and tf[ch]==sf[ch]: 
                have+=1
            
            while have==need: 

                if r-l+1 < res: 
                    res = r-l+1
                    ind = [l, r]
                
                sf[s[l]]-=1
                if s[l] in tf and sf[s[l]] < tf[s[l]]: 
                    have-=1
                
                l+=1
    
        return s[ind[0]:ind[1]+1]





