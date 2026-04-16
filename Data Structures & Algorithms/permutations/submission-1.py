class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        res = []
        def backtrack(path, used): 
            if len(nums)==len(path): 
                res.append(path[:])
                return
            
            for i in range(len(nums)): 
                if not used[i]: 
                    path.append(nums[i])
                    used[i] = True
                    backtrack(path, used)
                    path.pop()
                    used[i] = False

            
        
        backtrack([], [False]*len(nums))
        return res
            



        

        