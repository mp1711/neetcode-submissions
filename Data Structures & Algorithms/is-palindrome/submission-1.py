class Solution:
    def isPalindrome(self, s: str) -> bool:

        i = 0; j = len(s)-1
        s = s.lower()


        while i<j: 
            if not s[i].isalnum(): 
                i+=1
            elif not s[j].isalnum(): 
                j-=1
            elif s[i]!=s[j]: 
                print(i, j, s[i], s[j])
                return False
            else: 
                i+=1
                j-=1
        
        return True
        