class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:

        cz = 0
        res = 0
        l = r = 0
        n = len(nums)


        for r in range(n): 
            if nums[r]==0: 
                cz += 1
            while cz>k: 
                if nums[l]==0: 
                    cz-=1
                l+=1
            res = max(res, r-l+1)
        
        return res

        