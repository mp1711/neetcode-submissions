from typing import List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        if sum(gas)<sum(cost): 
            return -1

        s = 0
        pos = 0
        n = len(gas)

        for i in range(len(gas)):
            s += gas[i] - cost[i]

            if s < 0:
                pos = i + 1
                s = 0

        return pos if pos<n else -1