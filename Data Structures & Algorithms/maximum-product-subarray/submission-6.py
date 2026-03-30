class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        n = len(nums)
        
        currmax = currmin = nums[0]

        globalmax = nums[0]

        for i in range(1, n): 
            temp = currmax
            currmax = max(currmax*nums[i], nums[i], currmin*nums[i])
            currmin = min(temp*nums[i], nums[i], currmin*nums[i])
            globalmax = max(globalmax, currmax)
                        
        return globalmax

        