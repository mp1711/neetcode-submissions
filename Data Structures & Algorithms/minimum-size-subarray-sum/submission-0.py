class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        snums = sum(nums)
        if snums<target: 
            return 0

        n = len(nums)

        if snums == target: 
            return n

        
        l, r = 0, 0
        minlen = n

        s = 0

        while r<n: 

            s += nums[r]

            while s>=target: 
                minlen = min(minlen, r-l+1)
                s -= nums[l]
                l+=1
            
            r+=1
        
        return minlen


        