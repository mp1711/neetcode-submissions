class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        res = [0]*len(temperatures)

        stack = []

        for ind, val in enumerate(temperatures): 

            while stack and stack[-1][1]<val: 
                sind, sval = stack.pop()
                res[sind] = ind-sind
            
            stack.append([ind, val])
        
        return res


            


        
        