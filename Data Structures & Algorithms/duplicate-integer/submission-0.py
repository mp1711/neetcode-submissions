class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        freq = set()
        for i in nums: 
            if i in freq: 
                return True
            freq.add(i)
        
        return False