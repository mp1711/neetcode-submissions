class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        n = len(gas)
        gas+=gas
        cost+=cost
        diff = [gas[i] - cost[i] for i in range(len(gas))]

        s = 0
        steps = 0
        for i in range(2*n): 
            if s+diff[i]<0: 
                s = 0
                steps = 0
            else: 
                s+=diff[i]
                steps+=1
            if steps==n: 
                return i-steps+1
        
        return -1
        
        
            

        