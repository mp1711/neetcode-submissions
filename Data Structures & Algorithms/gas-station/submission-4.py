class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        if sum(cost)>sum(gas): 
            return -1
        
        res = 0
        total = gas[0] - cost[0]
        for i in range(1, len(cost)): 
            if total<0: 
                res = i
                total = 0
            total += (gas[i] - cost[i])
        
        return res
        