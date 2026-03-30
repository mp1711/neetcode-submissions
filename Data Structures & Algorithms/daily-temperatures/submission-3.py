class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        n = len(temperatures)
        res = [0]*n

        stack = []

        for r in range(n): 
            if stack: 
                while stack and temperatures[stack[-1]]<temperatures[r]: 
                    ind = stack.pop()
                    res[ind] = r - ind
            stack.append(r)
        
        return res
            
        