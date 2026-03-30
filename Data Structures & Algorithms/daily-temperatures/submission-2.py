class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0]*n
        stack = []
        for i in range(len(temperatures)): 
            if (not stack) or (stack and stack[-1][1]>=temperatures[i]): 
                stack.append((i, temperatures[i]))
            else: 
                while stack and stack[-1][1]<temperatures[i]: 
                    j = stack.pop()[0]
                    res[j] = i - j
                stack.append((i, temperatures[i]))
        
        return res



        