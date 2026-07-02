class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = set()
        l = 0
        maxLength = 0
        for r in range(len(s)): 
            while s[r] in chars: 
                chars.remove(s[l])
                l+=1
            if s[r] not in chars: 
                chars.add(s[r])
            maxLength = max(maxLength, r-l+1)
        
        return maxLength
            

        