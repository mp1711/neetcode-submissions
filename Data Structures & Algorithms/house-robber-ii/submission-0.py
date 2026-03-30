class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n==1: 
            return nums[0]
        
        if n==2: 
            return max(nums[0], nums[1])
        
        def rob(arr): 
            p1 = 0
            p2 = 0

            for i in range(len(arr)): 
                temp = max(p1+arr[i], p2)
                p1 = p2
                p2 = temp
            
            return temp
        
        return max(rob(nums[1:]), rob(nums[:-1]))


        