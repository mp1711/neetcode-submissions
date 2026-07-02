class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        need = [0]*26
        window = [0]*26

        for i in s1: 
            need[ord(i)-97]+=1
        
        l = 0
        k = len(s1)

        for r in range(len(s2)): 
            window[ord(s2[r])-97]+=1

            if r>=k:                 
                window[ord(s2[r-k])-97]-=1

            if window==need: 
                return True
                    
        return False
        