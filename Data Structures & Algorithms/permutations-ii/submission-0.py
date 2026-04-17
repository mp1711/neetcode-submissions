class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:

        res = []
        path = []
        nums.sort()

        def backtrack(i, used): 
            if len(path)==len(nums): 
                res.append(path[:])
                return 
            
            for j in range(len(nums)): 
                    
                if used[j] or j > 0 and nums[j] == nums[j-1] and not used[j-1]:
                    continue
                    
                path.append(nums[j])
                used[j] = True
                backtrack(j+1, used)
                path.pop()
                used[j] = False
        
        backtrack(0, [False]*(len(nums)))
        return res
        