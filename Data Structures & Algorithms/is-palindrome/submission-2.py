class Solution:
    def isPalindrome(self, s: str) -> bool:

        left, right = 0, len(s)-1

        while left < right: 
            l = s[left]
            r = s[right]

            if not l.isalnum(): 
                left += 1
            elif not r.isalnum(): 
                right -= 1
            elif l.lower()==r.lower(): 
                left += 1
                right -= 1
            else: 
                return False
        
        return True
        