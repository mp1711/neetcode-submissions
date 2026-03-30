class Solution:
    def longestPalindrome(self, s: str) -> str:

        res = ""
        reslen = 0
        n = len(s)
        for i in range(len(s)): 
            l = i
            r = i
            while l>=0 and r<n and s[l]==s[r]:
                if reslen<(r-l+1): 
                    reslen = r-l+1
                    res = s[l:r+1]
                l-=1
                r+=1
            

            l = i
            r = i+1
            while l>=0 and r<n and s[l]==s[r]:
                if reslen<(r-l+1): 
                    reslen = r-l+1
                    res = s[l:r+1]
                l-=1
                r+=1

        
        return res
            


                 

        