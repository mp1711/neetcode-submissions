class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        if digits[-1]!=9: 
            digits[-1] += 1
            return digits

        n = len(digits)
        i = n-1
        while i>=0: 
            if digits[i]==9: 
                digits[i] = 0
            else: 
                break
            i-=1
        
        if i==-1: 
            digits = [1] + digits
        else: 
            digits[i]+=1
        
        return digits
            


        