class Solution:
    def myPow(self, x: float, n: int) -> float:

        if x==1 or n==0: 
            return 1
        
        def rpow(x, n): 
            if n==0: 
                return 1
            
            flag = n%2
            half = rpow(x, n//2)
            if flag: 
                return half*half*x
            else: 
                return half*half
        
        return rpow(x, n) if n>0 else 1/rpow(x, -n) 
        