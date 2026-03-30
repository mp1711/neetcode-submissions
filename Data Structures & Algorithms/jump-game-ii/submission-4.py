from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:

        steps = 0
        n = len(nums)
        l = r = 0

        while r<n-1: 
            maxreach = 0


            for i in range(l, r+1): 
                maxreach = max(maxreach, i + nums[i])
            
            l = r+1
            r = maxreach
            steps+=1
        
        return steps