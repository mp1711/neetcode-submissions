class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        l = 0
        maxlen = 0
        temp = {}
        n = len(s)

        for r in range(n): 
            if s[r] in temp: 
                l = max(l, temp[s[r]] + 1)
            temp[s[r]] = r
            maxlen = max(maxlen, r-l+1)
    
        return maxlen



        