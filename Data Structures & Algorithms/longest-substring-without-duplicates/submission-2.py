class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        l = 0
        maxlen = 0
        temp = set()
        n = len(s)

        for r in range(n): 
            if s[r] in temp: 
                while s[l] != s[r]: 
                    temp.remove(s[l])
                    l+=1
                l+=1
            temp.add(s[r])
            maxlen = max(maxlen, r-l+1)
    
        return maxlen



        