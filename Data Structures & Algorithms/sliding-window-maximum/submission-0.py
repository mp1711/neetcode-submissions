class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        mx = [-1, -1]
        res = []

        for r in range(k, len(nums)+1): 
            l = r-k
            while l<r: 
                if nums[l]>mx[0]: 
                    mx[0] = nums[l]
                    mx[1] = l
                l+=1
            res.append(mx[0])
            mx[0] = -1
        
        return res

