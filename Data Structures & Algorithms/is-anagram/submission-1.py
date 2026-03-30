class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        n = len(s)
        m = len(t)

        if n!=m: 
            return False


        s_count = [0]*26
        t_count = [0]*26

        for i in range(n): 
            s_count[ord(s[i]) - 97] += 1
            t_count[ord(t[i]) - 97] += 1
        
        for i in range(26): 
            if s_count[i]!=t_count[i]: 
                return False
        
        return True




        