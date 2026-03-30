class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:

        stack = []
        n = len(s)
        temp = ""
        j = 0
        i = 0

        while i<n: 

            if s[i]=="(": 
                stack.append(j)
            
            elif s[i]==")": 
                if stack: 
                    stack.pop()
                else: 
                    i+=1
                    continue
            
            temp += s[i]
        
            i+=1
            j+=1
        
        res = ""

        for i in range(len(temp)):
            if i not in stack:  
                res += temp[i]
        
        return res

        

        

        

        