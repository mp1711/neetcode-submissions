from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        
        if n == 1:
            return 0
        
        steps = 0
        currentEnd = 0
        farthest = 0
        
        for i in range(n - 1): 
            
            farthest = max(farthest, i + nums[i])
            
            if i == currentEnd:
                steps += 1
                currentEnd = farthest
        
        return steps