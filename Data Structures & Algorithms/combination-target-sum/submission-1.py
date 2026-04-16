class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        res = []

        def backtrack(i, path): 
            if i==len(nums) or sum(path)>target: 
                return 
            if sum(path)==target: 
                res.append(path[:])
                return 

            path.append(nums[i])
            backtrack(i, path)
            path.pop()
            backtrack(i+1, path)
            
        backtrack(0, [])
        return res