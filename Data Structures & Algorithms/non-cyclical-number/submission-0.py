class Solution:
    def isHappy(self, n: int) -> bool:

        s = set()

        while True: 
            res = 0
            for i in str(n): 
                res += int(i)**2
            if res==1: 
                return True
            if res in s: 
                return False
            s.add(res)
            n = res
        

        