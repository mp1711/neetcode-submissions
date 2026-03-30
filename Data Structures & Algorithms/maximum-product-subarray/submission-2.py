class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        n = len(nums)
        
        dpmax = [1]*(n+1)
        dpmin = [1]*(n+1)

        for i in range(1, n+1): 
            dpmax[i] = max(dpmax[i-1]*nums[i-1], dpmin[i-1]*nums[i-1], nums[i-1])
            dpmin[i] = min(dpmax[i-1]*nums[i-1], dpmin[i-1]*nums[i-1], nums[i-1])
        
        print(dpmax, dpmin)
        
        return max(dpmax[1:])

        