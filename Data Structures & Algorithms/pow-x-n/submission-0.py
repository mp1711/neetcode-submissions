class Solution:
    def myPow(self, x: float, n: int) -> float:

        if x==1 or n==0: 
            return 1
        
        def rpow(x, n): 
            if n==0: 
                return 1
            if n==1: 
                return x
            
            flag = n%2
            if flag: 
                return rpow(x, n//2)*rpow(x, n//2+1)
            else: 
                return rpow(x, n//2)*rpow(x, n//2)
        
        return rpow(x, n) if n>0 else 1/rpow(x, -n) 
        