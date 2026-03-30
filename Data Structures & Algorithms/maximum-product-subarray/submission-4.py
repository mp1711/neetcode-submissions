class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        n = len(nums)
        
        dpmax = [1]*(n)
        dpmin = [1]*(n)

        dpmax[0] = nums[0]
        dpmin[0] = nums[0]

        for i in range(1, n): 
            dpmax[i] = max(dpmax[i-1]*nums[i], dpmin[i-1]*nums[i], nums[i])
            dpmin[i] = min(dpmax[i-1]*nums[i], dpmin[i-1]*nums[i], nums[i])
                        
        return max(dpmax)

        