class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        diff = {}

        for i, n in enumerate(nums): 
            d = target - n
            if d in diff: 
                return [diff[d], i]
            diff[n] = i
        
        return []